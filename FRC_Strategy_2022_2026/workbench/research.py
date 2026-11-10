"""Bounded research navigation. Full source records remain available on demand."""
import argparse,json,pathlib,subprocess,sys
R=pathlib.Path(__file__).resolve().parents[1]
def read(p):return [json.loads(l) for l in (R/p).read_text().splitlines() if l.strip()]
def emit(x):print(json.dumps(x,ensure_ascii=False,indent=2))
a=argparse.ArgumentParser(description=__doc__);sub=a.add_subparsers(dest='op',required=True)
p=sub.add_parser('catalog');p.add_argument('--year',type=int)
p=sub.add_parser('search');p.add_argument('terms',nargs='+');p.add_argument('--year');p.add_argument('--kind');p.add_argument('--limit',type=int,default=12)
p=sub.add_parser('packet');p.add_argument('robot');p.add_argument('--section',choices=['dossier','technical_notes','published_parameters','images','physical_studies','mechanism_revisions','architecture_cases','source_review'])
x=a.parse_args()
if x.op=='catalog':emit([dict(id=r['id'],architecture=r['architecture'],tags=r['tags'],packet='agent/robot_packets/'+r['id']+'.json') for r in read('data/robot_dossiers.jsonl') if not x.year or r['year']==x.year])
elif x.op=='packet':
 if not __import__('re').fullmatch(r'(201[89]|202[2-6])-\d+',x.robot):a.error('Invalid robot id')
 p=R/'agent/robot_packets'/(x.robot+'.json');v=json.loads(p.read_text());emit(v.get(x.section) if x.section else v)
else:
 cmd=[sys.executable,str(R/'scripts/query_agent.py'),'search',*x.terms,'--any','--limit',str(x.limit)]
 if x.year:cmd+=['--year',x.year]
 if x.kind:cmd+=['--kind',x.kind]
 v=json.loads(subprocess.check_output(cmd,text=True));v['results']=[{k:r.get(k) for k in ['id','title','kind','evidence','robot','version_label','source_locator','source_urls','image_ids','robot_packet']}|{'excerpt':r['text'][:900],'read_full_record_with':'scripts/query_agent.py read '+r['id']} for r in v['results']];emit(v)
