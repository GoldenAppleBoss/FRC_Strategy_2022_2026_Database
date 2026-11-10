"""Publish evidence-bounded architecture comparisons from authoritative JSONL.

Called by the physical prebuild. Source facts, owner testimony and original
engineering hypotheses remain separate in SQL, retrieval packets and the reader.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def read(p):return [json.loads(l) for l in (ROOT/p).read_text().splitlines() if l.strip()]
def write(p,rows):(ROOT/p).write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows))

def build():
 cases=read('data/architecture_cases.jsonl');notes=[n for n in read('data/technical_mechanisms.jsonl') if not n.get('architecture_case_id')]
 contexts=[c for c in read('data/context_documents.jsonl') if c.get('kind') not in ['architecture_case','architecture_research_protocol']]
 (ROOT/'docs/architecture').mkdir(exist_ok=True)
 for c in cases:
  facts=' '.join(p['text'] for p in c['premises'])
  fields=[('piece_flow','Piece flow'),('packaging','Physical arrangement and swept space'),('independent_motions','Independent motions and powered functions'),('burdens_avoided','Burdens avoided'),('burdens_retained','Burdens retained'),('engineering_hypothesis','Engineering hypothesis'),('rival_explanation','Rival explanation'),('reversal_conditions','When the preference reverses'),('unknowns','Unknowns'),('decision_changing_check','Proposed check; not performed'),('outcome_status','Outcome evidence')]
  body='# '+c['robot_id']+': '+c['title']+'\n\nVersion: '+c['version_label']+'\n\n## Evidence premises\n\n'
  for p in c['premises']:body+='- **'+p['type']+'**: '+p['text']+' Locator: '+p['locator']+'\n'
  for k,t in fields:body+='\n## '+t+'\n\n'+c[k]+'\n'
  body+='\n## Sources\n\n'+'\n'.join('- '+u for u in c['source_urls'])+'\n'
  path='docs/architecture/'+c['id']+'.md';(ROOT/path).write_text(body)
  contexts.append(dict(id=c['id'],robot_id=c['robot_id'],year=c['year'],kind='architecture_case',title=c['title'],body=body,source_urls=c['source_urls']))
  owner=any(p['type']=='owner_firsthand_account' for p in c['premises'])
  notes.append(dict(id=c['id']+'-note',architecture_case_id=c['id'],robot_id=c['robot_id'],year=c['year'],binder_id=None,subsystem='architecture_and_interfaces',title=c['title'],version_label=c['version_label'],construction=facts+' Physical arrangement: '+c['packaging']+' Piece path: '+c['piece_flow'],team_stated_reason='Read typed premises for team explanations. Remaining causal analysis is editorial; it is not a claim about the team\'s intent.',engineering_analysis='Motions: '+c['independent_motions']+' Avoided: '+c['burdens_avoided']+' Retained: '+c['burdens_retained']+' Hypothesis: '+c['engineering_hypothesis']+' Rival: '+c['rival_explanation']+' Reversal: '+c['reversal_conditions'],recommended_validation=c['decision_changing_check'],limitations=c['unknowns']+' '+c['outcome_status'],source_url=c['source_urls'][0],additional_sources=c['source_urls'][1:],page_references=[p['locator'] for p in c['premises']],image_ids=c['image_ids'],evidence_type='owner_account_with_partial_public_correspondence' if owner else 'mixed_typed_primary_premises_with_editorial_inference',construction_evidence='owner_testimony_and_partial_primary_correspondence' if owner else 'mixed_primary_premises_read_attribution',review_scope='Selected captions/publications/code and inherited physical studies; not a controlled performance comparison.',code_revision=c.get('code_revision')))
 # The long protocol is also embedded and searchable, rather than only a local link.
 protocol=(ROOT/'docs/ARCHITECTURE_RESEARCH_PROTOCOL.md').read_text()
 contexts.append(dict(id='architecture-research-protocol',robot_id=None,year=None,kind='architecture_research_protocol',title='Research complete architectures with minimal owner explanation',body=protocol,source_urls=[]))
 write('data/technical_mechanisms.jsonl',notes);write('data/context_documents.jsonl',contexts)
 robots=read('data/robot_dossiers.jsonl');sources=read('data/sources.jsonl');byurl={s['url']:s['id'] for s in sources};associations=read('tables/robot_sources.jsonl');existing={(a['robot_id'],a['source_id']) for a in associations}
 for c in cases:
  r=next(r for r in robots if r['id']==c['robot_id'])
  for u in c['source_urls']:
   if u not in byurl:
    sid='architecture-source-'+hashlib.sha256(u.encode()).hexdigest()[:16];byurl[u]=sid;sources.append(dict(id=sid,url=u,title='Architecture comparison selected primary source',kind='technical_source_reference',review_basis='Selected claims only; typed premises and exact review scope in architecture case',retrieved_on='2026-11-07'))
   sid=byurl[u]
   if sid not in r['source_ids']:r['source_ids'].append(sid)
   if u not in r['primary']:r['primary'].append(u)
   if (r['id'],sid) not in existing:associations.append(dict(robot_id=r['id'],source_id=sid,relationship='architecture comparison selected source'));existing.add((r['id'],sid))
 write('data/robot_dossiers.jsonl',robots);write('data/sources.jsonl',sources);write('tables/robot_sources.jsonl',associations)
 # Existing summaries remain intact; add normalized subsystem rows only for supplements.
 subs=read('tables/subsystems.jsonl');keys={(s['robot_id'],s['subsystem']) for s in subs}
 for r in robots:
  for k,v in r['subsystems'].items():
   if (r['id'],k) not in keys:subs.append(dict(robot_id=r['id'],subsystem=k,description=v,coverage_status=r['coverage'][k],source_ids_json=json.dumps(r['source_ids'])))
 write('tables/subsystems.jsonl',subs)
 write('tables/architecture_cases.jsonl',[dict(id=c['id'],robot_id=c['robot_id'],version_label=c['version_label'],data_json=json.dumps(c,ensure_ascii=False)) for c in cases])
 return cases
if __name__=='__main__':build()
