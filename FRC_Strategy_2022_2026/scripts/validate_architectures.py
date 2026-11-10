"""Check architecture export parity and consequential attribution boundaries.

This is a corpus contract check, not an evaluation of future LLM reasoning.
"""
import json,pathlib,sqlite3,subprocess,sys,hashlib
R=pathlib.Path(__file__).resolve().parents[1]
def read(p):return [json.loads(l) for l in (R/p).read_text().splitlines() if l.strip()]
baseline=json.loads((R/'data/architecture_preservation_baseline.json').read_text())
for key,path in [('robots','robot_dossiers'),('notes','technical_mechanisms'),('images','mechanism_images'),('parameters','technical_parameters')]:
 rows=read('data/'+path+'.jsonl');assert set(baseline[key])<={r['id'] for r in rows}
 if key=='notes':
  byid={r['id']:r for r in rows}
  for rid,digest in baseline['note_content_hashes'].items():assert hashlib.sha256(json.dumps(byid[rid],sort_keys=True).encode()).hexdigest()==digest,rid
cs=read('data/architecture_cases.jsonl');robots=read('data/robot_dossiers.jsonl');notes=read('data/technical_mechanisms.jsonl');units=read('agent/retrieval_units.jsonl');claims=read('agent/claims.jsonl')
assert len(cs)==5 and len({c['id'] for c in cs})==5
con=sqlite3.connect(R/'frc_strategy.sqlite');assert con.execute('select count(*) from architecture_cases').fetchone()[0]==5
required=['piece_flow','packaging','independent_motions','burdens_avoided','burdens_retained','engineering_hypothesis','rival_explanation','reversal_conditions','unknowns','decision_changing_check','source_urls','version_label','premises']
for c in cs:
 assert all(c.get(k) for k in required),c['id']
 assert all(p.get('type') and p.get('locator') and p.get('text') for p in c['premises'])
 packet=json.loads((R/f'agent/robot_packets/{c["robot_id"]}.json').read_text());assert c in packet['architecture_cases']
 assert json.loads(con.execute('select data_json from architecture_cases where id=?',(c['id'],)).fetchone()[0])==c
 u=next(u for u in units if u['id']==c['id']);assert json.loads(u['text'])==c and u['kind']=='architecture_case'
 assert any(n.get('architecture_case_id')==c['id'] for n in notes)
owner=next(c for c in cs if c['id'].endswith('1746-owner'))
claim=next(c for c in claims if c['id']==owner['id']+'-note:construction');assert claim['evidence']=='owner_testimony_and_partial_primary_correspondence'
assert owner['version_label']!=next(c for c in cs if c['id'].endswith('1746-iri'))['version_label']
assert 'not predicted outcomes' in owner['unknowns']
ma=next(c for c in cs if c['robot_id']=='2023-6328');assert len(ma['code_revision'])==40 and 'not successful physical transfer' in ma['premises'][1]['text']
for rid in ['2023-1746','2023-6328']:
 r=next(r for r in robots if r['id']==rid);assert r['epa_rank'] is None and r['selection_scope']=='targeted_architecture_supplement'
 assert any(c['robot_id']==rid and c['cohort']=='targeted_architecture_supplement' for c in read('data/cohort_coverage.jsonl'))
q=json.loads(subprocess.check_output([sys.executable,str(R/'scripts/query_agent.py'),'search','handoff','--kind','architecture_case','--limit','100'],text=True));assert any(x['robot']=='2023-6328' for x in q['results'])
assert len(read('agent/architecture_evaluation_cases.jsonl'))==8
assert len(read('data/mechanism_revisions.jsonl'))==21
out={'status':'passed','architecture_cases':5,'new_targeted_dossiers':2,'reasoning_evaluation_prompts':8,'scope':'Export parity, attribution, chronology boundaries, retrieval and preserved revision count; mechanical hypotheses and model performance not validated.'}
(R/'ARCHITECTURE_VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
