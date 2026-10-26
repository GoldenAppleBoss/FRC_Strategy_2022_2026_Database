"""Rebuild the SQLite database from this package's exact table exports; Python standard library only."""
import json,pathlib,sqlite3,sys
root=pathlib.Path(__file__).resolve().parents[1]
target=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else root/'frc_strategy.sqlite'
if target.exists():target.unlink()
con=sqlite3.connect(target);con.executescript((root/'schema.sql').read_text())
order=['metadata','seasons','robot_dossiers','sources','robot_sources','subsystems','versions','selection_audit','season_epa','events','matches','team_events','benchmarks','einstein_reviews','context_documents','mechanism_images','source_posts','cad_code_links','video_reviews','binder_sources','binder_audit','technical_mechanisms','technical_parameters','tower_summary_2026']
for table in order:
 with (root/'tables'/(table+'.jsonl')).open() as f:
  for line in f:
   a=json.loads(line);cols=list(a)
   con.execute('INSERT INTO '+table+' ('+','.join(cols)+') VALUES ('+','.join('?' for _ in cols)+')',list(a.values()))
for a in con.execute('SELECT id,team_name,robot_name,architecture,analyst_inference,tags_json FROM robot_dossiers').fetchall():
 descriptions=con.execute('SELECT description FROM subsystems WHERE robot_id=?',(a[0],)).fetchall()
 deep=con.execute('SELECT body_markdown FROM context_documents WHERE robot_id=?',(a[0],)).fetchall()
 con.execute('INSERT INTO robot_search VALUES (?,?)',(a[0],' '.join(str(v or '') for v in a[1:])+' '+' '.join(v[0] for v in descriptions+deep)))
for a in con.execute('SELECT id,kind,title,body_markdown FROM context_documents').fetchall():con.execute('INSERT INTO context_search VALUES (?,?,?)',(a[0],a[1],a[2]+' '+a[3]))
for a in con.execute('SELECT video_id,title,source_summary,transfer_analysis FROM video_reviews').fetchall():con.execute('INSERT INTO context_search VALUES (?,?,?)',(a[0],'video_review',' '.join(str(x or '') for x in a[1:])))
con.commit();print('Integrity:',con.execute('PRAGMA integrity_check').fetchone()[0]);print('Robots:',con.execute('SELECT count(*) FROM robot_dossiers').fetchone()[0]);con.close()
