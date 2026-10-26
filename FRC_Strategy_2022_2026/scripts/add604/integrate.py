from pathlib import Path
import json,csv,copy,hashlib,shutil,subprocess,openpyxl,pymupdf
from content import NOTES,SOURCES
R=Path(__file__).resolve().parents[2]
def read(p):return [json.loads(x) for x in (R/p).read_text().splitlines() if x.strip()]
def write(p,a):(R/p).write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in a))
def obj(p,a):(R/p).write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
robots=read('data/robot_dossiers.jsonl');notes=read('data/technical_mechanisms.jsonl');audits=read('data/binder_audit.jsonl');contexts=read('data/context_documents.jsonl');sources=read('data/sources.jsonl')
rank={(int(a['year']),int(a['team'])):a for a in csv.DictReader((R/'data/epa_rankings_2022_2026.csv').open())}
code=R.parent/'research604-code2022';commit=subprocess.check_output(['git','-C',str(code),'rev-parse','HEAD'],text=True).strip()
names={2022:'Octopus Prime',2023:'2023 published robot (name not independently confirmed)',2024:'Domotron',2025:'The Flush; separate offseason Quixshot',2026:'Toploader'}
extra2025='https://www.chiefdelphi.com/t/team-604-quixilver-2025-offseason-robot-quixshot/504607/55'
discovery=[]
for year,rows in NOTES.items():
 rid=f'{year}-604';a=next((x for x in robots if x['id']==rid),None);isnew=a is None
 if isnew:
  a=copy.deepcopy(robots[0]);rr=rank.get((year,604),{});a.update(id=rid,year=year,team=604,team_name='Quixilver',robot=names[year],images=[],source_post_count=0,cad_code_links=[],source_ids=[],technical_note_ids=[],deep_context='',epa_rank=int(rr['epa_rank']) if rr else None,epa=float(rr['epa']) if rr else None,epa_pre_champs=float(rr['pre_champs_epa']) if rr else None,epa_breakdown=json.loads(rr['epa_breakdown_json']) if rr else {},game={2022:'RAPID REACT',2023:'CHARGED UP',2026:'REBUILT'}[year],tags=['user-requested supplemental reference'],subsystems={k:'Unresolved in reviewed sources; do not infer absence.' for k in ['drivetrain','intake','transfer','scoring','endgame','controls']},coverage={k:'partial / unresolved detail' for k in ['drivetrain','intake','transfer','scoring','endgame','controls']},versions=[],primary=[],limits=[],architecture='',analysis='')
  robots.append(a)
  a['selection_scope']='User-requested supplemental reference outside original 25/year cohort; original selections preserved.'
 a['robot']=names[year]
 src=SOURCES[year];sid='604-source-'+str(year)
 if sid not in [s['id'] for s in sources]:sources.append({'id':sid,'url':src,'title':f'604 {year} primary technical release','kind':'published_robot_code' if year==2022 else 'team_technical_release','review_basis':'Selected primary-source sections reviewed; no CAD or all-version certification','retrieved_on':'2026-10-26'})
 if src not in a['primary']:a['primary'].append(src)
 if sid not in a['source_ids']:a['source_ids'].append(sid)
 a['limits']=list(dict.fromkeys(a['limits']+['Selected primary publications/code reviewed; exact per-event installation and exhaustive intermediate revisions remain unresolved.','New 2023/2026 source images were located but direct downloads returned HTTP 403; source links are retained, no new local image extraction is claimed.']))
 a['version_audit']='Version-specific primary-source study; not exhaustive per-event certification'
 a['strict_acceptance']='provisional; unresolved geometry and version details explicitly retained'
 body=f'# {rid} — Quixilver: {names[year]}\n\nPrimary source: {src}\n\nReviewed 2026-10-26. This is a source-bounded technical study. Construction, stated intent, interpretation and unresolved evidence are separate.\n'
 if year==2022:body+=f'\nCode commit: {commit}. Read the original FRC-2022 tree. FRC-2022-NEW is a learning rewrite, not certified event code. File locators: Intake.java, BallPath.java, Launcher.java, Climber.java and Calibration.java under FRC-2022/src/com/_604robotics/robot2022/.\n'
 for i,(sub,version,construction,reason,analysis) in enumerate(rows,1):
  nid=f'604-expansion-{year}-{i}'
  n={'id':nid,'robot_id':rid,'year':year,'binder_id':None,'subsystem':sub,'title':version+' · '+sub,'version_label':version,'construction':construction,'team_stated_reason':reason,'engineering_analysis':analysis,'recommended_validation':'Verify the installed configuration and interfaces against the original publication/CAD; prototype full acquisition-to-output cycles, recovery and service access under the intended loaded and defended conditions. These tests are proposed, not performed.','limitations':'Source report or published-code behavior, not independent performance testing. Geometry, dates and unreviewed mechanisms remain unknown.','pdf_pages':[],'page_references':['Repository README and original subsystem/Calibration files'] if year==2022 else ['Team release, selected mechanism sections and identified replies'],'source_url':src,'additional_sources':[extra2025] if year==2025 and i==len(rows) else [],'evidence_type':'published_code_review' if year==2022 else 'team_publication_paraphrase','performance_status':'team_reported_or_unmeasured','image_ids':[],'review_scope':'Selected primary technical sections; exact CAD geometry and every competition version not audited'}
  notes=[x for x in notes if x['id']!=nid];notes.append(n)
  if nid not in a['technical_note_ids']:a['technical_note_ids'].append(nid)
  if isnew:
   prev=a['subsystems'][sub];a['subsystems'][sub]=(prev+' '+construction if not prev.startswith('Unresolved') else construction);a['coverage'][sub]='documented synopsis'
  body+=f'\n## {version} · {sub}\n\n### Published construction or code\n\n{construction}\n\n### Stated rationale and boundaries\n\n{reason}\n\n### Engineering interpretation\n\n{analysis}\n\n### Validation still required\n\n{n["recommended_validation"]}\n'
 if year==2025:
  body+='\n## Distinct offseason machine\n\nQuixshot is a separate robot. The team’s July reply explains that a ground intake intended for the in-season machine conflicted with climber packaging and was installed on the launcher instead. Launch velocity differentials were manually tuned. The first offseason answer explicitly says no algae or deep climb at that point. Do not combine the two robots into one imaginary in-season architecture. Source: '+extra2025+'\n';a['versions'].append('In-season The Flush is distinct from offseason Quixshot; intake packaging pivot documented July 2025.')
 if year==2024:a['versions'].append('May 2025 release follow-up identifies unresolved 2024 axle-bolt and deploy-chain failures; later 2026 independent arms address the coupling.')
 if isnew:
  a['architecture']=' '.join(x[2] for x in rows[:2]);a['analysis']=' '.join(x[4] for x in rows[-2:]);a['versions']=[x[1] for x in rows];a['versions']=list(dict.fromkeys(a['versions']))
 body+='\n## Evidence limits\n\n'+'\n'.join('- '+x for x in a['limits'])+'\n'
 if year==2023:body+='\nThe reviewed publication does not establish charge-station balance construction or exact drivetrain hardware. FIRST’s carried-forward robot-name field is not treated as authoritative identity for this different-season machine.\n'
 (R/f'docs/context/{rid}-primary-study.md').write_text(body)
 contexts=[c for c in contexts if c['id']!=rid+'-primary-study'];contexts.append({'id':rid+'-primary-study','title':f'{rid} primary-source mechanisms and strategic context','year':year,'robot_id':rid,'kind':'robot_deep_note','body':body,'source_urls':[src]+([extra2025] if year==2025 else [])})
 a['deep_context']=body
 audit=next((v for v in audits if v['robot_id']==rid),None)
 if audit is None:
  audit={'robot_id':rid,'year':year,'team':604,'epa_rank':a['epa_rank'],'status':'primary_source_review_no_verified_binder','search':{'query':f'604 {year} technical release','review_date':'2026-10-26'},'additional_searches':[],'reviewed_source_ids':[],'technical_note_ids':[],'candidate_attempts':[],'interpretation':'Primary technical release/code reviewed; no standalone binder certification.','exhaustive_binder_discovery':False,'every_competition_version_certified':False};audits.append(audit)
 audit['technical_note_ids']=a['technical_note_ids'];audit['reviewed_source_ids']=list(dict.fromkeys(audit['reviewed_source_ids']+[sid]));a['binder_audit']=audit
 (R/f'robots/{rid}.md').write_text(body)
 discovery.append({'robot_id':rid,'primary_source':src,'review_scope':'Published technical narrative and selected code, not full CAD or all-event audit','new_dossier':isnew,'new_technical_notes':len(rows),'code_commit':commit if year==2022 else None,'image_access':'Known linked images; new downloads denied (403)' if year in [2023,2026] else 'Existing extracted image associations preserved'})

# Preserve the supplied documents as historical team inputs, with exact cell/page provenance.
(R/'team1833').mkdir(exist_ok=True)
uploads=R.parent/'upload'
shutil.copy2(uploads/'Copy of Team Task List.xlsx',R/'team1833/task_list_2026.xlsx');shutil.copy2(uploads/'2026 Mechanical Subsystem research_pros and cons lists.pdf',R/'team1833/mechanical_research_2026.pdf')
w=openpyxl.load_workbook(uploads/'Copy of Team Task List.xlsx',data_only=False)
cells=[{'sheet':s.title,'cell':c.coordinate,'value':c.value,'kind':'formula' if c.data_type=='f' else 'source_value'} for s in w for row in s for c in row if c.value is not None]
obj('team1833/task_list_cells.json',cells)
d=pymupdf.open(uploads/'2026 Mechanical Subsystem research_pros and cons lists.pdf');obj('team1833/mechanical_research_pages.json',[{'page':i+1,'text':p.get_text()} for i,p in enumerate(d)])
teamdoc='''# 1833’s supplied 2026 design workflow

The original workbook and PDF are preserved under team1833/. Their statements are historical team planning, not validated game rules or independent mechanism measurements. Cell-level and PDF-page text exports permit exact retrieval. No source workbook or PDF was edited.

The workbook contains parallel group task lists, numeric priority/difficulty judgments, formulas multiplying those ordinal values, and a cleaned must/might/won’t list. Some sheets have inconsistent priority scales. The cleaned list’s repeated “No” final-decision cells must not be interpreted as rejecting every must-do task. Group 4 even distinguishes autonomous climb priority in qualifications versus eliminations. Keep group opinions and later decisions separate instead of silently averaging them into a consensus.

The PDF maps requirements into intake, storage, shooter, climb, electrical and chassis concepts. It records historical mechanism references, pros/cons and open prototype questions about compression and roller materials. It explicitly asks for service access, wire protection and mechanical/electrical compatibility. The shooter page contains proposed distances, angles and velocities; these are unverified calculations, with launch-height, drag and other assumptions needing reconstruction before reuse. References such as 2020 spindexer slot capacity must not become universal capacity limits for 2026 bulk serializers.

For the agent: reproduce the task-to-requirement-to-concept chain, preserve alternatives and open tests, and distinguish kickoff judgments from later evidence. The early climb priorities are historical inputs; the user’s later correction and tower-only data establish a fuel-first default for the studied 2026 competitive context. Do not overwrite the original documents to make hindsight look like the initial decision. A future task sheet should carry rule revision, phase, partner assumptions, expected contribution, ordinal priority meaning, development cost, evidence and decision rationale. A mechanism comparison should identify which requirement it serves and what observation would change the choice.
'''
(R/'docs/context/1833-design-workflow.md').write_text(teamdoc);contexts.append({'id':'1833-design-workflow','title':'1833 supplied task and subsystem research workflow','year':2026,'robot_id':None,'kind':'team_process_reference','body':teamdoc,'source_urls':[]})
robots.sort(key=lambda x:(x['year'],x['epa_rank'] or 99999,x['team']))
for f,a in [('data/robot_dossiers.jsonl',robots),('data/technical_mechanisms.jsonl',notes),('data/binder_audit.jsonl',audits),('data/context_documents.jsonl',contexts),('data/sources.jsonl',sources),('data/604_research_audit.jsonl',discovery)]:write(f,a)
# Normalized exports retain original schema and all original selections.
write('tables/sources.jsonl',sources)
write('tables/technical_mechanisms.jsonl',[{k:v for k,v in n.items()} for n in []]) if False else None
old=read('tables/technical_mechanisms.jsonl');oldids={n['id'] for n in old}
for n in notes:
 if n['id'] not in oldids:
  old.append({'id':n['id'],'robot_id':n['robot_id'],'binder_id':None,'subsystem':n['subsystem'],'title':n['title'],'construction':n['construction'],'team_stated_reason':n['team_stated_reason'],'engineering_analysis':n['engineering_analysis'],'recommended_validation':n['recommended_validation'],'limitations':n['limitations'],'metadata_json':json.dumps(n,ensure_ascii=False)})
write('tables/technical_mechanisms.jsonl',old)
write('tables/binder_audit.jsonl',[{'robot_id':a['robot_id'],'status':a['status'],'metadata_json':json.dumps(a,ensure_ascii=False)} for a in audits])
write('tables/context_documents.jsonl',[{'id':c['id'],'title':c['title'],'year':c.get('year'),'robot_id':c.get('robot_id'),'kind':c['kind'],'body_markdown':c['body'],'source_urls_json':json.dumps(c.get('source_urls',[]))} for c in contexts])
write('tables/robot_dossiers.jsonl',[{'id':a['id'],'year':a['year'],'team':a['team'],'team_name':a['team_name'],'robot_name':a['robot'],'epa_rank':a['epa_rank'],'epa':a['epa'],'epa_pre_champs':a['epa_pre_champs'],'architecture':a['architecture'],'analyst_inference':a['analysis'],'limits_json':json.dumps(a['limits']),'coverage_json':json.dumps(a['coverage']),'version_audit':a['version_audit'],'strict_acceptance':a['strict_acceptance'],'tags_json':json.dumps(a['tags'])} for a in robots])
write('tables/subsystems.jsonl',[{'robot_id':a['id'],'subsystem':k,'description':v,'coverage_status':a['coverage'][k],'source_ids_json':json.dumps(a['source_ids'])} for a in robots for k,v in a['subsystems'].items()])
vr=read('tables/versions.jsonl');rs=read('tables/robot_sources.jsonl')
for a in robots:
 if a['team']==604:
  vr=[v for v in vr if v['robot_id']!=a['id']]
  for i,v in enumerate(a['versions']):vr.append({'id':a['id']+'-version-'+str(i),'robot_id':a['id'],'ordinal':i,'description':v,'date_start':None,'date_end':None,'status':'publication snapshot; event chronology unresolved','source_ids_json':json.dumps(a['source_ids'])})
  for sid in a['source_ids']:
   if not any(v['robot_id']==a['id'] and v['source_id']==sid for v in rs):rs.append({'robot_id':a['id'],'source_id':sid,'relationship':'primary technical study'})
write('tables/versions.jsonl',vr);write('tables/robot_sources.jsonl',rs)
payload=json.loads((R/'data/reader_payload.json').read_text());payload.update(robots=robots,technicalNotes=notes,binderAudit=audits,contextDocs=contexts,sources=sources)
audit=json.loads((R/'data/audit.json').read_text());audit.update(robots=128,robots_by_year={str(y):sum(a['year']==y for a in robots) for y in range(2022,2027)},provisional_dossiers=128,technical_notes=len(notes),agent_robot_packets=128,robot_years_with_technical_reviews=128,context_documents=len(contexts),supplemental_604_dossiers=3,original_selection_cohort=125,edition='604 five-season expansion and 1833 process references',snapshot='2026-10-26');payload['audit']=audit
obj('data/audit.json',audit);obj('data/reader_payload.json',payload)
for fname,rows in [('data/robot_index.csv',robots)]:
 with (R/fname).open() as f:fields=next(csv.reader(f))
 with (R/fname).open('w',newline='') as f:
  out=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');out.writeheader()
  for a in rows:out.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in a.items()})
for p in [R/'README.md',R/'AGENTS.md',R/'agent/README.md']:
 s=p.read_text();s='> Current 604 expansion: 128 dossiers = original 125 plus supplemental 2022/2023/2026 604 entries; existing 2024/2025 entries expanded. Original 25/year selections are preserved. Read docs/context/1833-design-workflow.md and data/604_research_audit.jsonl. Visual match audits are no longer required by the user; commentary attribution remains mandatory.\n\n'+s;p.write_text(s)
print('Dossiers',len(robots),'Notes',len(notes),'604 years',[a['year'] for a in robots if a['team']==604])
