"""Local corpus retrieval. Python standard library only; no model or network calls."""
import argparse, json, pathlib, re, sqlite3

ROOT = pathlib.Path(__file__).resolve().parents[1]

def emit(value):
    print(json.dumps(value, ensure_ascii=False, indent=2))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='command', required=True)
    s = sub.add_parser('search', help='Literal token search; all terms required unless --any')
    s.add_argument('terms', nargs='+')
    for flag in ['year', 'robot', 'kind', 'evidence', 'subsystem']:
        s.add_argument('--'+flag)
    s.add_argument('--limit', type=int, default=10)
    s.add_argument('--any', action='store_true', dest='any_term')
    r = sub.add_parser('read'); r.add_argument('id')
    r = sub.add_parser('packet'); r.add_argument('robot')
    r = sub.add_parser('images'); r.add_argument('--robot', required=True)
    r = sub.add_parser('game'); r.add_argument('year', type=int, choices=[2018,2019,*range(2022,2027)])
    args = ap.parse_args()
    if args.command == 'packet':
        if not re.fullmatch(r'(?:201[89]|202[2-6])-\d+', args.robot): ap.error('Use a supported YEAR-TEAM, such as 2019-1323 or 2026-2910')
        p=ROOT/'agent/robot_packets'/(args.robot+'.json')
        if not p.exists(): ap.error('Robot is not in this corpus; inspect agent/manifest.json and the coverage audit')
        emit(json.loads(p.read_text())); return
    if args.command == 'game':
        print((ROOT/f'docs/game_{args.year}.md').read_text()); return
    if args.command == 'images':
        emit([json.loads(l) for l in (ROOT/'agent/image_catalog.jsonl').read_text().splitlines()
              if json.loads(l)['robot_id']==args.robot]); return
    con=sqlite3.connect('file:'+str(ROOT/'agent/retrieval.sqlite')+'?mode=ro', uri=True)
    if args.command == 'read':
        row=con.execute('SELECT payload FROM units WHERE id=?',(args.id,)).fetchone()
        if not row: ap.error('Unknown retrieval-unit ID')
        emit(json.loads(row[0])); return
    if not 1 <= args.limit <= 200: ap.error('--limit must be between 1 and 200')
    tokens=re.findall(r'\w+', ' '.join(args.terms), flags=re.UNICODE)
    if not tokens: ap.error('Provide at least one word or number')
    # Quoted tokens make input literal; FTS operators are never accepted from the query.
    expression=(' OR ' if args.any_term else ' AND ').join('"'+x+'"' for x in tokens)
    where=['search MATCH ?']; params=[expression]
    for field in ['year','robot','kind','evidence','subsystem']:
        value=getattr(args,field)
        if value is not None: where.append('u.'+field+'=?');params.append(value)
    total=con.execute('SELECT count(*) FROM search JOIN units u ON u.rowid=search.rowid WHERE '+' AND '.join(where),params).fetchone()[0]
    rows=con.execute('SELECT u.payload,bm25(search) FROM search JOIN units u ON u.rowid=search.rowid WHERE '+' AND '.join(where)+' ORDER BY bm25(search),u.id LIMIT ?',params+[args.limit]).fetchall()
    emit({'query':' '.join(args.terms),'mode':'any_token' if args.any_term else 'all_tokens',
          'filters':{k:getattr(args,k) for k in ['year','robot','kind','evidence','subsystem'] if getattr(args,k) is not None},
          'matches':total,'returned':len(rows),'results':[dict(json.loads(r[0]),retrieval_score=r[1]) for r in rows],
          'next_step':'Read each hit’s robot_packet and required_game_context, plus its source_locator. Ranking measures lexical relevance, not truth, quality, or robot performance.'})

if __name__=='__main__': main()
