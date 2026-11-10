import base64, collections, hashlib, io, json, mimetypes, pathlib, re, sqlite3
from PIL import Image

ROOT=pathlib.Path(__file__).resolve().parents[1] if pathlib.Path(__file__).parent.name=='scripts' else pathlib.Path('image_fix/FRC_Strategy_2022_2026').resolve()
def readj(name): return [json.loads(l) for l in (ROOT/name).read_text().splitlines() if l.strip()]
def writej(name,rows):
 p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows))
def writejson(name,value):
 p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

html=(ROOT/'scripts/reader_template_v3.html').read_text().replace('__DATABASE_JSON__',(ROOT/'data/reader_payload.json').read_text().strip())
db=json.loads((ROOT/'data/reader_payload.json').read_text())
robots=readj('data/robot_dossiers.jsonl'); notes=readj('data/technical_mechanisms.jsonl');params=readj('data/technical_parameters.jsonl')
images=readj('data/mechanism_images.jsonl');contexts=readj('data/context_documents.jsonl');binders=readj('data/binder_sources.jsonl');audits=readj('data/binder_audit.jsonl')
physical=readj('data/physical_studies.jsonl');interfaces=readj('data/mechanism_interfaces.jsonl');coverage=readj('data/evidence_coverage.jsonl')
architecture_cases=readj('data/architecture_cases.jsonl')
revisions=readj('data/mechanism_revisions.jsonl')
db['architectureCases']=architecture_cases
db['architectureOwnerAccounts']=readj('data/architecture_owner_accounts.jsonl')
db['architectureResearchLedger']=readj('data/architecture_research_ledger.jsonl')
db['mechanismRevisions']=revisions
db.update(physicalStudies=physical,mechanismInterfaces=interfaces,evidenceCoverage=coverage)
db.update(robots=robots,technicalNotes=notes,technicalParameters=params,contextDocs=contexts,binderSources=binders,binderAudit=audits)
db['audit']=json.loads((ROOT/'data/audit.json').read_text())
db['videoReviews']=readj('data/roboreplay_review_ledger.jsonl')
db['einstein']=readj('data/einstein_reviews.jsonl')
docpaths={p.read_text().strip():str(p.relative_to(ROOT)) for p in (ROOT/'docs').rglob('*.md')}
for d in db['contextDocs']:d['path']=docpaths.get(d['body'].strip(),'')

# Figure metadata and embedded bytes share stable image IDs. Original images are unchanged.
assets={};catalog=[]
for im in images:
 p=ROOT/im['path'];raw=p.read_bytes()
 with Image.open(io.BytesIO(raw)) as pic: width,height=pic.size;fmt=pic.format;pic.verify()
 mime=Image.MIME.get(fmt,mimetypes.guess_type(str(p))[0] or 'application/octet-stream')
 assets[im['id']]={'mime':mime,'base64':base64.b64encode(raw).decode('ascii')}
 catalog.append({**im,'media_type':mime,'width_px':width,'height_px':height,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
 'path_base':'corpus_root','reader_asset_id':im['id'],'reader_url':'index.html#image='+im['id'],
 'interpretation_boundary':im.get('limitations') or 'Caption and editorial label aid retrieval. A source-associated crop does not establish dimensions, hidden geometry, material, event installation, or causal performance.'})
writej('agent/image_catalog.jsonl',catalog)

claims=[];units=[]
def addunit(uid,title,text,kind,evidence,year=None,robot=None,subsystem=None,locator=None,sources=None,**extra):
 units.append({'id':uid,'title':title,'text':text,'kind':kind,'evidence':evidence,'year':year,'robot':robot,'subsystem':subsystem,
 'source_locator':locator,'source_urls':sources or [],'robot_packet':f'agent/robot_packets/{robot}.json' if robot else None,
 'required_game_context':f'docs/game_{year}.md' if year in [2018,2019,*range(2022,2027)] else None,**extra})

fields={'construction':'team_publication_paraphrase','team_stated_reason':'team_reason_or_boundary_paraphrase',
 'engineering_analysis':'analyst_inference','recommended_validation':'proposed_test_not_performed','limitations':'evidence_boundary'}
for n in notes:
 for field,evidence in fields.items():
  if field=='construction':evidence=n.get('construction_evidence',evidence)
  claim={'id':n['id']+':'+field,'robot_id':n['robot_id'],'year':n['year'],'technical_note_id':n['id'],'binder_id':n['binder_id'],
   'version_label':n['version_label'],'subsystem':n['subsystem'],'field':field,'evidence':evidence,'text':n[field],
   'source_url':n['source_url'],'page_references':n['page_references'],'additional_sources':n.get('additional_sources',[]),
   'source_attribution_scope':('Read the architecture case typed premises. Owner testimony, primary publications and editorial reconstruction have distinct scopes; a linked public source does not independently establish an owner recollection.' if n.get('architecture_case_id') else 'Published source and selected page locators apply to this note. A reason/boundary may explicitly say that the team did not state its intent. These are paraphrases, not quotations or independent reproductions.'),
   'image_ids':n['image_ids'],'review_scope':n.get('review_scope','Selected technical-publication review'),'source_evidence_type':n.get('evidence_type'),'limitations':n['limitations'],'version_scope':'Publication/source snapshot label only; no unverified event/date interval inferred'}
  claims.append(claim)
  addunit(claim['id'],n['title']+' · '+field,n[field],'technical_claim',evidence,n['year'],n['robot_id'],n['subsystem'],
   {'file':'data/technical_mechanisms.jsonl','id':n['id'],'field':field},[n['source_url']]+n.get('additional_sources',[]),
   version_label=n['version_label'],page_references=n['page_references'],image_ids=n['image_ids'],
   related_note_id=n['id'],read_sibling_fields=True,limitations=n['limitations'])
for p in params:
 rid=p['robot_id'];year=int(rid.split('-')[0])
 claims.append({'id':p['id'],'robot_id':rid,'year':year,'binder_id':p['binder_id'],'evidence':'team_reported_parameter',
  'text':p['published_parameters'],'component':p['component'],'source_url':p['source_url'],'pdf_page':p.get('pdf_page'),
  'notation':p['notation'],'version_label':p.get('version_label'),'units':p.get('units'),'source_record_id':p.get('source_record_id'),'operating_conditions':p.get('operating_conditions'),'source_location':p.get('source_location'),'evidence_status':p.get('evidence_status'),'limitations':'Selected source notation; no automated unit/ratio normalization, fabrication approval or independent performance test.'})
 addunit(p['id'],p['component']+' published parameters',p['published_parameters'],'published_parameter','team_reported_parameter',year,rid,None,
  {'file':'data/technical_parameters.jsonl','id':p['id']},[p['source_url']],notation=p['notation'],pdf_page=p.get('pdf_page'),version_label=p.get('version_label'),units=p.get('units'),source_record_id=p.get('source_record_id'),operating_conditions=p.get('operating_conditions'),source_location=p.get('source_location'))
writej('agent/claims.jsonl',claims)

versionrecords=[]
for r in robots:
 rid=r['id']; ns=[n for n in notes if n['robot_id']==rid]; ps=[p for p in params if p['robot_id']==rid]
 cs=[d for d in contexts if d.get('robot_id')==rid];bs=[b for b in binders if b['robot_id']==rid];ims=[im for im in catalog if im['robot_id']==rid]
 labels=[]
 for n in ns:
  if n['version_label'] not in labels: labels.append(n['version_label'])
 versions=[{'id':rid+':publication-version:'+str(i+1),'label':label,'robot_id':rid,
  'label_type':'existing_technical_note_publication_label','event_start':None,'event_end':None,'date_start':None,'date_end':None,
  'technical_note_ids':[n['id'] for n in ns if n['version_label']==label],
  'source_urls':list(dict.fromkeys(n['source_url'] for n in ns if n['version_label']==label)),
  'boundary':'Grouping preserves published labels. It is not a new certification of chronology, every revision, or installation at an event.'} for i,label in enumerate(labels)]
 versionrecords+=versions
 packet={'schema_version':'1.0','id':rid,'year':r['year'],'team':r['team'],'corpus_status':'provisional_research',
  'required_reading':[f'docs/game_{r["year"]}.md','docs/AGENT_GUIDE.md','docs/TECHNICAL_EVIDENCE_GUIDE.md','docs/1833_DESIGN_DOCTRINE.md','docs/DESIGN_REVIEW_PROTOCOL.md','docs/1833_PLAIN_LANGUAGE_AND_PHYSICAL_DESIGN.md','docs/1833_SOLO_RP_AND_DECISION_ECONOMICS.md'],
  'path_base':'corpus_root','dossier':r,'technical_notes':ns,'published_parameters':ps,'technical_publications':bs,
  'publication_version_groups':versions,'context_documents':cs,'images':ims,
  'physical_studies':[s for s in physical if s['robot_id']==rid],
  'interface_ports':[p for p in interfaces if p['robot_id']==rid],
  'mechanism_revisions':[v for v in revisions if v['robot_id']==rid],
  'architecture_cases':[c for c in architecture_cases if c['robot_id']==rid],
  'architecture_research_ledger':[c for c in db['architectureResearchLedger'] if c['robot_id']==rid],
  'evidence_coverage':[c for c in coverage if c['robot_id']==rid],
  'binder_audit':next(a for a in audits if a['robot_id']==rid),
  'claim_ids':[c['id'] for c in claims if c['robot_id']==rid],
  'retrieval_contract':{'read_game_first':True,'read_entire_note_before_using_one_claim':True,'unknown_is_not_absent':True,
   'source_reports_are_not_independent_tests':True,'whole_robot_context_required':True,'cross_team_compatibility_verified':False}}
 writejson(f'agent/robot_packets/{rid}.json',packet)
 for field,text in [('architecture',r['architecture']),('analysis',r['analysis'])]+list(r['subsystems'].items()):
  addunit(rid+':dossier:'+field,f'{rid} {r["team_name"]} · {field}',text,'dossier_synopsis','mixed_synopsis_coarse_source_mapping',r['year'],rid,field if field in r['subsystems'] else None,
   {'file':'data/robot_dossiers.jsonl','id':rid,'field':('subsystems.' if field in r['subsystems'] else '')+field},r['primary'],
   coverage=r['coverage'],version_audit=r['version_audit'],limits=r['limits'])
writej('agent/publication_versions.jsonl',versionrecords)

# An integrated evidence hit carries construction, sequence, packaging, figures and
# limitations together. It supplements fine-grained claims, rather than replacing them.
for s in physical:
 for m in s['mechanisms']:
  text=json.dumps(dict(mechanism=m,packaging=s['packaging'],piece_flow=s['piece_flow'],whole_robot_unknowns=s['unknowns']),ensure_ascii=False,indent=2)
  addunit(m['id']+':physical',m['title']+' construction packaging piece flow transfer',text,'physical_mechanism','source_bounded_editorial_reconstruction',int(s['robot_id'][:4]),s['robot_id'],m['subsystem'],{'file':'data/physical_studies.jsonl','id':s['id'],'mechanism_id':m['id']},s['source_urls'],version_label=s['version_label'],image_ids=m['image_ids'],coverage=m['coverage'],limits=m['unknowns'],interface_ids=[p['id'] for p in interfaces if p['mechanism_id']==m['id']],drawing_ids=[s['id']+'-'+v for v in ['top','side','transition']])
for p in interfaces:
 addunit(p['id'],p['mechanism_id']+' '+p['role']+' compatibility interface',json.dumps(p,ensure_ascii=False,indent=2),'mechanism_interface','partial_contract_not_compatibility_certification',int(p['robot_id'][:4]),p['robot_id'],locator={'file':'data/mechanism_interfaces.jsonl','id':p['id']},sources=p['source_urls'],version_label=p['version_label'],image_ids=p['image_ids'])
for c in coverage:
 uid='coverage:'+c.get('mechanism_id',c['robot_id']+':'+c.get('subsystem',''))
 addunit(uid,c['robot_id']+' evidence-specific coverage',json.dumps(c,ensure_ascii=False),'evidence_coverage','editorial_assessment',int(c['robot_id'][:4]),c['robot_id'],locator={'file':'data/evidence_coverage.jsonl','id':c.get('mechanism_id',c['robot_id'])})
for c in readj('data/cohort_coverage.jsonl'):
 addunit('cohort:'+c['robot_id'],c['robot_id']+' '+c['cohort'],json.dumps(c,ensure_ascii=False),'cohort_coverage','targeted_supplement_no_rank' if c['cohort']=='targeted_architecture_supplement' else 'retained_rank_snapshot',c['year'],c['robot_id'] if c['dossier_present'] else None,locator={'file':'data/cohort_coverage.jsonl','id':c['robot_id']})
for v in revisions:
 addunit(v['id']+':revision',v['publisher_label']+' '+v['family']+' prototype change history',json.dumps(v,ensure_ascii=False,indent=2),'mechanism_revision','visually_inspected_CAD_with_editorial_comparison',int(v['robot_id'][:4]),v['robot_id'],'transfer' if v['family']=='rotor' else 'scoring',{'file':'data/mechanism_revisions.jsonl','id':v['id']},[v['source_url'],v['source_image_url']],version_label=v['publisher_label'],image_ids=v['image_ids'],previous_revision_id=v['previous_revision_id'],event_installation=v['event_installation'],paired_other_mechanism_revision=None,limits=v['unknowns'])
for c in architecture_cases:
 addunit(c['id'],c['robot_id']+' '+c['title']+' simplicity architecture handoff',json.dumps(c,ensure_ascii=False,indent=2),'architecture_case','typed_premises_with_editorial_hypothesis',c['year'],c['robot_id'],'architecture_and_interfaces',{'file':'data/architecture_cases.jsonl','id':c['id']},c['source_urls'],version_label=c['version_label'],image_ids=c['image_ids'],read_whole_case=True)
for c in readj('data/revision_coverage.jsonl'):
 addunit('revision-coverage:'+c['robot_id'],c['robot_id']+' known revision figure coverage',json.dumps(c,ensure_ascii=False),'revision_coverage','label_audit_not_exhaustive_history',int(c['robot_id'][:4]),c['robot_id'],locator={'file':'data/revision_coverage.jsonl','id':c['robot_id']})
for c in readj('data/cohort_research_attempts.jsonl'):
 addunit('research-attempt:'+c['robot_id'],c['robot_id']+' unresolved primary construction research',json.dumps(c,ensure_ascii=False),'research_attempt','retrieval_scope_not_absence',int(c['robot_id'][:4]),locator={'file':'data/cohort_research_attempts.jsonl','id':c['robot_id']})

def chunks(text):
 # Respect headings and paragraph boundaries. Long paragraphs are retained intact.
 sections=re.split(r'(?m)(?=^#{1,4} )',text)
 for section in sections:
  title=section.splitlines()[0].lstrip('# ').strip() if section.strip() else ''
  buf=[];size=0
  for para in section.split('\n\n'):
   if buf and size+len(para)>6000:yield title,'\n\n'.join(buf);buf=[];size=0
   buf.append(para);size+=len(para)+2
  if any(buf):yield title,'\n\n'.join(buf)

for g in db['games']:
 for i,(title,text) in enumerate(chunks(g['analysis'])):
  if text.strip():addunit(f'game:{g["year"]}:{i+1}',title,text,'game_context','analyst_synthesis_with_attributed_evidence',g['year'],locator={'file':f'docs/game_{g["year"]}.md','section':title,'part':i+1})
for d in contexts:
 path=docpaths.get(d['body'].strip())
 for i,(title,text) in enumerate(chunks(d['body'])):
  if text.strip():addunit(f'context:{d["id"]}:{i+1}',title,text,'context','mixed_context_read_attribution',d.get('year'),d.get('robot_id'),locator={'file':path or 'data/context_documents.jsonl','id':d['id'],'section':title,'part':i+1},sources=d.get('source_urls',[]))
for im in catalog:
 addunit('image:'+im['id'],im.get('publisher_label') or im['caption'],im['caption'],'image_metadata','editorial_reconstruction_not_source_evidence' if im.get('kind')=='editorial_physical_reconstruction' else 'source_associated_visual_reference',int(im['robot_id'].split('-')[0]),im['robot_id'],locator={'file':'agent/image_catalog.jsonl','id':im['id']},sources=[im['source_url']],image_ids=[im['id']],inspection_scope=im.get('visual_review') or im.get('review_status'))
for v in db['videoReviews']:
 addunit('video:'+v['video_id'],v['title'],(v.get('source_summary') or 'Pending transcript review.')+'\n\n'+(v.get('transfer_analysis') or ''),'video_review',v['review_status'],v.get('season'),locator={'file':'data/roboreplay_review_ledger.jsonl','video_id':v['video_id']},sources=[v['url']],visual_review=False)
 for i,s in enumerate(v.get('expanded_review',{}).get('sections',[]),1):
  for field,evidence in [('source_account','attributed_video_commentary'),('engineering_or_strategy_analysis','analyst_inference')]:
   addunit('video-detail:'+v['video_id']+':'+str(i)+':'+field,s['title'],s[field],'video_analysis',evidence,v.get('season'),locator={'file':'data/roboreplay_review_ledger.jsonl','video_id':v['video_id'],'section':i,'field':field},sources=[s['url']],visual_review=False,full_context_document=v['expanded_review']['expanded_document'],remaining_uncertainties=v['expanded_review']['remaining_uncertainties'],review_scope=v['expanded_review']['enrichment_scope'])
for b in readj('data/benchmarks.jsonl'):
 addunit('benchmark:'+b['event'],f'{b["year"]} {b["name"]} · {b["type"]} · week {b["week"]}',json.dumps(b,ensure_ascii=False,indent=2),
  'event_benchmark','derived_event_benchmark',b['year'],locator={'file':'data/benchmarks.jsonl','event':b['event']},
  sources=[b['source_url'],b['data_url'],b['tba_url']],event=b['event'],event_week=b['week'],event_type=b['type'],
  interpretation_boundary='Alliance clean-score summaries and model-estimated team EPA retain distinct denominators. Historical observations do not guarantee wins or establish individual scoring counts.')
for m in readj('data/einstein_reviews.jsonl'):
 addunit('einstein:'+m['key'],f'{m["year"]} Einstein {m["name"]}',json.dumps(m,ensure_ascii=False,indent=2),
  'einstein_record','mixed_match_record_read_note_attribution',m['year'],locator={'file':'data/einstein_reviews.jsonl','key':m['key']},
  sources=[m['numeric_source_url'],m['tba_url']]+[e['url'] for e in m.get('evidence',[]) if e.get('url')],
  visual_review=False,tactical_review_complete=m['tactical_review_complete'],
  interpretation_boundary='Read each strategic note kind separately. Scores, arithmetic, reported commentary and analyst interpretation are distinct. No completed visual audit; do not invent observed tactics.')
for m in readj('data/einstein_reviews.jsonl'):
 for i,c in enumerate(m.get('commentary_timeline',[]),1):
  for field,evidence in [('account','attributed_video_commentary'),('conditional_analysis','analyst_inference')]:
   addunit('match-commentary:'+m['key']+':'+str(i)+':'+field,c['title'],c[field],'match_commentary',evidence,m['year'],locator={'file':'data/einstein_reviews.jsonl','key':m['key'],'timeline_event':i,'field':field},sources=[c['source_url']],visual_review=False,match_clock_alignment=None,source_video_seconds=[c['source_start_seconds'],c['source_end_seconds']],match_key=m['key'],read_sibling_fields=True,limitations='Edited commentary timestamp, not aligned match clock or independently observed action.')
 addunit('visual-audit:'+m['key'],m['key']+' visual audit status',json.dumps(m['visual_audit'],ensure_ascii=False),'visual_audit_status','workflow_status_not_match_observation',m['year'],locator={'file':'data/einstein_visual_audit.jsonl','match_key':m['key']},sources=[m['video_url']] if m.get('video_url') else [],visual_review=False,complete=False)
for t in readj('data/tower_summary_2026.jsonl'):

 uid='tower:2026:'+re.sub(r'[^a-z0-9]+','-',t['group'].lower()).strip('-')
 addunit(uid,'2026 tower-only sample · '+t['group'],json.dumps(t,ensure_ascii=False,indent=2),'tower_sample','derived_component_sample',2026,
  locator={'file':'data/tower_summary_2026.jsonl','group':t['group']},
  interpretation_boundary='Selected stored alliance rows, not an all-season census. Keep valid/missing denominators. Tower component fields are not endgame EPA.',
  supporting_rows='data/tower_component_sample_2026.jsonl')
writej('agent/retrieval_units.jsonl',units)
con=sqlite3.connect(ROOT/'agent/retrieval.sqlite')
con.executescript('DROP TABLE IF EXISTS search;DROP TABLE IF EXISTS units;CREATE TABLE units(id TEXT UNIQUE,year INTEGER,robot TEXT,kind TEXT,evidence TEXT,subsystem TEXT,payload TEXT);CREATE VIRTUAL TABLE search USING fts5(title,text,metadata,tokenize="unicode61");')
for u in units:
 cur=con.execute('INSERT INTO units VALUES(?,?,?,?,?,?,?)',(u['id'],u['year'],u['robot'],u['kind'],u['evidence'],u['subsystem'],json.dumps(u,ensure_ascii=False)))
 con.execute('INSERT INTO search(rowid,title,text,metadata) VALUES(?,?,?,?)',(cur.lastrowid,u['title'],u['text'],' '.join(str(u.get(x) or '') for x in ['robot','year','version_label','subsystem','kind'])))
con.commit();con.close()

manifest={'schema_version':'1.0','edition':'2026-10-27-2018-2019-historical-context','path_base':'corpus_root','entry_point':'AGENTS.md',
 'reader':'index.html','reader_images':'All source image bytes embedded in index.html; no image network or sibling-folder requests needed.',
 'counts':{'robot_packets':len(robots),'retrieval_units':len(units),'claims':len(claims),'images':len(catalog),'technical_notes':len(notes),'published_parameters':len(params),'robot_years_with_technical_reviews':len(set(n['robot_id'] for n in notes))},
 'files':{'complete_robot_packets':'agent/robot_packets/{YEAR-TEAM}.json','retrieval_units':'agent/retrieval_units.jsonl','retrieval_index':'agent/retrieval.sqlite','claims':'agent/claims.jsonl','images':'agent/image_catalog.jsonl','publication_versions':'agent/publication_versions.jsonl','query_cli':'scripts/query_agent.py','games':'docs/game_{YEAR}.md','benchmarks':'data/benchmarks.jsonl','einstein_records':'data/einstein_reviews.jsonl','tower_sample_summary':'data/tower_summary_2026.jsonl','tower_component_rows':'data/tower_component_sample_2026.jsonl','binder_discovery_audit':'data/binder_audit.jsonl','full_sql_database':'frc_strategy.sqlite','methodology':'docs/METHODOLOGY.md','evaluation_cases':'agent/evaluation_cases.jsonl'},
 'semantics':{'robot_id':'YEAR-TEAM; team number alone is ambiguous','image_paths':'Relative to corpus root, including inside packets; never relative to the packet file','units':'Published strings retain source units and ratio order. No automatic physical normalization.','version_groups':'Publication labels, not audited competition intervals. Null dates mean unknown.','evidence':'Types describe attribution, not calibrated probabilities. Analyst inference is not a team statement. Proposed tests are not performed.','search_ranking':'FTS5 bm25 lexical relevance only; not confidence, causation, robot quality or EPA.','field_sourcing':'Technical notes have source/page locators; dossier synopsis fields retain coarser source bundles.','manuals':'Source links and narrative references are retained; rule-version completeness and field CAD coverage are not certified. Verify governing rules for a new design.','scope':'125 provisional dossiers: 27 robot-years with reviewed technical publications and 98 with focused source studies; zero exhaustive version certifications. 33 inherited full-caption reviews with selected-passage enrichment, plus two new full available-caption reads. Eleven prior pending exports recovered; nine await full content review. All 80 canonical Einstein visual audits remain pending. Full channel and replay-attempt inventories remain unverified.'},
 'required_workflow':['Read AGENTS.md and the full game chapter for the target year.','Set role, event stage, partner assumptions and team resources.','Search explicit year/function; inspect typed evidence, scope and source locators.','Load complete robot packets, including sibling claim fields and limitations.','Open the referenced image bytes with image-capable tools; text captions do not confer visual understanding.','Check exact version, mechanism interfaces, performance conditions and rule applicability.','Recommend a coherent architecture, alternatives, unresolved issues and a decision-changing test.'],
 'generation':{'script':'scripts/build_agent_and_reader.py','inputs':'Included data JSONL, embedded game chapters, Markdown docs and original image bytes','network_required':False}}
manifest['files'].update(video_quiz_prompts='data/roboreplay_quiz_prompts.jsonl',quiz_protocol='docs/QUIZ_PROTOCOL.md',technical_study_audit='data/technical_study_audit.jsonl',einstein_visual_audit='data/einstein_visual_audit.jsonl',visual_audit_protocol='docs/EINSTEIN_VISUAL_AUDIT.md',transcript_recovery='data/transcript_recovery_ledger.jsonl')
manifest['files'].update(task_list_template='team1833/1833_Task_List_Template.xlsx',task_list_protocol='docs/TASK_LIST_PROTOCOL.md',task_list_schema='team1833/task_template_schema.json')
manifest['required_workflow'].insert(2,'For each new manual analysis, material rules revision or new/revised robot design brief, follow docs/TASK_LIST_PROTOCOL.md and deliver a filled copy of the one-sheet 1833 task template before the final architecture recommendation. Preserve human decisions separately; no group tabs.')
manifest['semantics']['scope']='128 provisional dossiers: original 125 plus supplemental 2022/2023/2026 Team 604 entries. 27 robot-years retain earlier reviewed technical-publication coverage; the other focused studies and new 604 primary-source studies have their own explicit scopes. Zero exhaustive version certifications. 35 available full-caption reviews; nine recovered transcripts await content review. No visual Einstein audit is claimed or required by the user. Full channel inventory remains unverified.'
manifest['files'].update(conversation_bootstrap='team1833/START_NEW_CONVERSATION.md',team_design_profile='team1833/design_profile.json',design_doctrine='docs/1833_DESIGN_DOCTRINE.md',design_review_protocol='docs/DESIGN_REVIEW_PROTOCOL.md',optimization_references='docs/1833_OPTIMIZATION_REFERENCES.md',design_review_schema='team1833/design_review_schema.json',design_rubric='agent/design_rubric.json',design_review_skeleton='examples/design_review_skeleton.json',research_ledger='data/1833_research_ledger.jsonl',task_audit_cli='scripts/audit_task_workbook.py',design_validator_cli='scripts/validate_design_review.py')
manifest['team_constraints']=json.loads((ROOT/'team1833/design_profile.json').read_text())['hard_constraints']
manifest['required_workflow'][1]='Apply the 1833 owner mandate: elite primary contributor, no support-only architecture, no turret; establish event stage, partners and actual resources.'
manifest['required_workflow'].insert(3,'Follow DESIGN_REVIEW_PROTOCOL.md: compare viable primary non-turret architectures with common timed scenarios, capacity/storage trade studies, physical envelope, row-specific dependencies and consistent release targets; apply the rubric and human review.')
manifest['files']['solo_rp_and_iteration_cost']='docs/1833_SOLO_RP_AND_DECISION_ECONOMICS.md'
manifest['required_workflow'].insert(2,'Prioritize independently achievable RP and owned scoring prerequisites. Use cheap spatial/analytical decisions first and justify physical tests by decision value and iteration cost; preserve the owner four-lane decision chronology.')
manifest['files']['actuation_and_history_scope']='docs/1833_ACTUATION_AND_HISTORY_SCOPE.md'
manifest['required_workflow'].insert(2,'No pneumatic actuation for 1833. Respect historical scope; 2018/2019 now have thirteen curated primary-source studies; read the scope audit and transfer guide, not an assumed top25 cohort.')
manifest['files'].update(historical_transfer='docs/HISTORICAL_2018_2019_TRANSFER.md',historical_coverage='data/historical_2018_2019_audit.json',blind_test_prompt='team1833/BLIND_TEST_PROMPT.md')
manifest['semantics']['scope']='141 provisional dossiers: original125, three604 supplements, thirteen curated2018/2019 primary-source studies (seven2018, six2019). Historical EPA/ranks unretrieved/null, no new top25 selection. Selected technical notes, version distinctions, parameters and credited figures; zero exhaustive version certifications. Earlier video review and Einstein scopes remain unchanged:35 available-caption studies, nine pending content reviews, no visual match audit.'
manifest['historical_expansion']=json.loads((ROOT/'data/historical_2018_2019_audit.json').read_text())
manifest['required_workflow'].insert(3,'For historical transfer, read HISTORICAL_2018_2019_TRANSFER.md; compare whole mechanisms and preserve current owner constraints, source/version boundaries and null historical rankings.')
manifest['edition']='2026-10-27-plain-physical-design'
manifest['files']['plain_physical_design']='docs/1833_PLAIN_LANGUAGE_AND_PHYSICAL_DESIGN.md'
manifest['required_workflow'].insert(1,'Read docs/1833_PLAIN_LANGUAGE_AND_PHYSICAL_DESIGN.md. Explain actual construction, borrowed features, packaging and full piece cycles in plain language; calculations must constrain choices. Apply the revised rubric anchors.')
manifest['edition']='2026-11-07-physical-evidence-and-revision-history'
manifest['schema_version']='1.2'
manifest['counts']['mechanism_revisions']=len(revisions)
manifest['files'].update(mechanism_revisions='data/mechanism_revisions.jsonl',revision_coverage='data/revision_coverage.jsonl')
manifest['semantics']['revision_history']='Publisher prototype ordinals are independent per mechanism. Do not assign final feature-list specifications backward to every prototype, or pair rotor and shooter ordinals without an explicit source. A changed render pose is not proof of a hardware revision.'
manifest['counts'].update(physical_studies=len(physical),physical_mechanisms=sum(len(s['mechanisms']) for s in physical),interface_ports=len(interfaces),editorial_drawings=sum(i.get('kind')=='editorial_physical_reconstruction' for i in images))
manifest['files'].update(physical_studies='data/physical_studies.jsonl',mechanism_interfaces='data/mechanism_interfaces.jsonl',evidence_coverage='data/evidence_coverage.jsonl',cohort_coverage='data/cohort_coverage.jsonl',physical_upgrade_report='docs/PHYSICAL_UPGRADE_REPORT.md')
manifest['generation']['prebuild_script']='scripts/build_physical_studies.py'
manifest['semantics']['physical_evidence']='Source-bounded editorial reconstruction; explicit unknowns and inspected figure scope travel with every integrated mechanism hit. Editorial drawings are not inspected source images or measured CAD.'
manifest['semantics']['coverage']='Legacy description fields do not establish completeness. Read explicit supported/partial/unknown/not_applicable evidence assessments, including unassessed legacy rows.'
manifest['required_workflow'].append('For physical studies, retrieve kind physical_mechanism and interface ports; never infer drop-in compatibility from shared piece type or a schematic. Use compare-interfaces to expose unresolved checks.')
manifest['required_workflow'].append('For sources with revision galleries, query mechanism_revision and inspect each relevant revision before transferring final feature-list parameters. Prototype labels do not establish a competition configuration or a rotor/shooter pairing.')
manifest['edition']='2026-11-07-complete-architecture-research'
manifest['counts']['architecture_cases']=len(architecture_cases)
manifest['files'].update(architecture_cases='data/architecture_cases.jsonl',architecture_protocol='docs/ARCHITECTURE_RESEARCH_PROTOCOL.md',owner_accounts='data/architecture_owner_accounts.jsonl',architecture_research_ledger='data/architecture_research_ledger.jsonl',architecture_evaluations='agent/architecture_evaluation_cases.jsonl')
manifest['semantics']['scope']='143 provisional dossiers: original125, three604 supplements, thirteen2018/2019 curated studies and two targeted2023 architecture supplements (1746,6328). Ranked cohorts and prior source/video scopes preserved. Five architecture cases are source-bounded engineering analyses, not controlled performance comparisons. Zero exhaustive version certifications.'
manifest['required_workflow'].insert(2,'Read ARCHITECTURE_RESEARCH_PROTOCOL.md; agent owns discovery and causal engineering explanation. Compare full architectures and cost vectors, preserve owner testimony, counterevidence and reversal conditions. Ask only consequential unresolved questions.')
writejson('agent/manifest.json',manifest)

# HTML changes: all galleries use embedded images; Markdown supports actual images and relative links.
html=html.replace('Expanded context · 258 curated images',f'Expanded context · {len(catalog)} embedded images')
css='''\n.image-open{display:block;width:100%;border:0;padding:0;background:#f5f7f5;cursor:zoom-in}.text-button{border:0;padding:0;background:none;color:var(--green);text-decoration:underline;cursor:pointer;font-size:inherit}.inline-image{max-width:720px;margin:12px 0}.inline-image img{width:100%;height:auto}.image-error{padding:12px;color:var(--red)}#image-dialog{width:min(96vw,1500px);max-width:96vw;max-height:94vh;border:1px solid var(--line);border-radius:12px;padding:16px;background:white;color:var(--ink)}#image-dialog::backdrop{background:#102820db}.image-dialog-tools{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:12px}.image-dialog-tools button{padding:6px 12px;border:1px solid var(--line);border-radius:6px;background:var(--light)}#full-image{display:block;max-width:100%;height:auto;margin:12px auto}#image-description{font-size:13px;overflow-wrap:anywhere}.image-scroll{max-height:70vh;overflow:auto}.gallery figcaption{overflow-wrap:anywhere}\n'''
html=html.replace('</style>',css+'</style>')
dialog='''<dialog id="image-dialog" aria-labelledby="image-description"><div class="image-dialog-tools"><button data-close-image>Close</button><button id="image-download">Download original image</button><a id="image-original" target="_blank" rel="noopener">Original source</a></div><p id="image-description"></p><div class="image-scroll"><img id="full-image" alt=""></div></dialog>'''
html=html.replace('<script id="database"',dialog+'\n<script id="database"',1)
db['agentManifest']=manifest
db['agentGuide']=(ROOT/'docs/AGENT_GUIDE.md').read_text()
# Match bodies to their Markdown locations to resolve links in the source document's directory.
html=re.sub(r'(<script id="database" type="application/json">).*?(</script>)',lambda m:m[1]+json.dumps(db,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+m[2],html,count=1,flags=re.S)
asset_tag='<script id="image-assets" type="application/json">'+json.dumps(assets,separators=(',',':'))+'</script>\n'
html=html.replace("<script>\n'use strict';",asset_tag+"<script>\n'use strict';",1)
js=(ROOT/'scripts/reader_images_and_agent.js').read_text()
# Insert before initial render, after function declarations, but before they are invoked.
html=html.replace('tabs();render();\n</script>',js+"\nfunction handleImageHash(){const id=new URLSearchParams(location.hash.slice(1)).get('image');if(id)openImage(id);}\nwindow.addEventListener('hashchange',handleImageHash);\ntabs();render();\nhandleImageHash();\n</script>")
html=html.replace('function markdown(s){','function markdown(s,base=\'\'){const inline=t=>inlineWithImages(t,base);')
html=html.replace("sources:'Sources',audit:","agent:'Agent entry point',sources:'Sources',audit:")
html=html.replace('context,replay,binders,sources,audit:','context,replay,binders,agent,sources,audit:')
html=html.replace("${ims.map(im=>`<figure>","${ims.map(im=>`<figure>") # replacement below is intentionally restricted to the two known renderers.
lines=html.splitlines()
for i,line in enumerate(lines):
 if line.startswith('${ims.length?`<div class="gallery">'):
  lines[i]='${ims.length?`<div class="gallery">${ims.map(figure).join(\'\')}</div>`:\'<p class="muted">No curated image is included for this dossier yet.</p>\'}'
 elif line.startswith(' const fig=im=>'):
  lines[i]=' const fig=figure;'
html='\n'.join(lines)+'\n'
html=html.replace('markdown(a.body);','markdown(a.body,a.path||\'\');').replace('markdown(c.analysis)','markdown(c.analysis,\'docs/game_\'+c.year+\'.md\')')
# Search construction and parameter text as well as synopsis/tag text.
html=html.replace('const sourceMap=',"const robotSearchText=a=>JSON.stringify([a,...DB.technicalNotes.filter(n=>n.robot_id===a.id),...DB.technicalParameters.filter(p=>p.robot_id===a.id),...(DB.physicalStudies||[]).filter(s=>s.robot_id===a.id),...(DB.mechanismInterfaces||[]).filter(p=>p.robot_id===a.id)]).toLowerCase();\nconst sourceMap=",1)
html=html.replace('words.every(w=>JSON.stringify(a).toLowerCase().includes(w))','words.every(w=>robotSearchText(a).includes(w))')
html='\n'.join(line.replace('JSON.stringify(a).toLowerCase().includes(w)','robotSearchText(a).includes(w)') if 'DB.robots.filter(a=>' in line else line for line in html.splitlines())+'\n'
html=html.replace('${num(a.context_words)}</b>new contextual words','${num(a.context_words)}</b>indexed contextual words')
html=html.replace("agent:'Agent entry point'","architectures:'Architecture decisions',agent:'Agent entry point'")
html=html.replace('binders,agent,sources','binders,architectures,agent,sources')
from enhance_workbench import enhance
html=enhance(html)
(ROOT/'index.html').write_text(html)
writejson('agent/build_summary.json',{'counts':manifest['counts'],'embedded_image_bytes':sum(len(base64.b64decode(a['base64'])) for a in assets.values()),'html_bytes':(ROOT/'index.html').stat().st_size})
print(json.dumps(manifest['counts'],indent=2))
