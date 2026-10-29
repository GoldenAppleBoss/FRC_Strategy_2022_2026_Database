"""Verify derived agent records, source locators, original image bytes and CLI behavior."""
import base64,hashlib,json,pathlib,re,sqlite3,subprocess,sys

root=pathlib.Path(__file__).resolve().parents[1]
checks=0
def check(value,message):
 global checks
 assert value,message
 checks+=1
def jl(path):return [json.loads(x) for x in (root/path).read_text().splitlines() if x.strip()]
def query(*args):
 return json.loads(subprocess.check_output([sys.executable,str(root/'scripts/query_agent.py'),*args],text=True))

manifest=json.loads((root/'agent/manifest.json').read_text())
robots=jl('data/robot_dossiers.jsonl');notes=jl('data/technical_mechanisms.jsonl');parameters=jl('data/technical_parameters.jsonl');units=jl('agent/retrieval_units.jsonl');claims=jl('agent/claims.jsonl');images=jl('agent/image_catalog.jsonl')
check(len(robots)==141,'141 dossiers')
check(len({x['id'] for x in units})==len(units),'unique unit IDs')
check(len(claims)==len(notes)*5+len(parameters),'all typed claim fields retained')
check(len(images)==569,'569 image associations')
html=(root/'index.html').read_text();assets=json.loads(re.search(r'<script id="image-assets" type="application/json">(.*?)</script>',html,re.S)[1]);db=json.loads(re.search(r'<script id="database" type="application/json">(.*?)</script>',html,re.S)[1])
check(len(assets)==569,'569 embedded assets')
check('src="${esc(im.path)}"' not in html,'no folder-dependent gallery image rendering')
for im in images:
 path=root/im['path'];check(path.is_file(),'original image path exists: '+im['id'])
 raw=path.read_bytes();check(hashlib.sha256(raw).hexdigest()==im['sha256'],'image hash: '+im['id'])
 check(base64.b64decode(assets[im['id']]['base64'])==raw,'embedded byte identity: '+im['id'])
 check(assets[im['id']]['mime']==im['media_type'],'MIME matches catalog: '+im['id'])
for r in robots:
 p=json.loads((root/f'agent/robot_packets/{r["id"]}.json').read_text())
 check(p['dossier']==r,'packet dossier preserved: '+r['id'])
 check(p['technical_notes']==[n for n in notes if n['robot_id']==r['id']],'full technical note fields preserved: '+r['id'])
 check(p['published_parameters']==[n for n in parameters if n['robot_id']==r['id']],'published parameters preserved: '+r['id'])
 check(all((root/x).is_file() for x in p['required_reading']),'packet required-reading paths')
 check(all((root/x['path']).is_file() for x in p['images']),'packet image paths from corpus root')
for u in units:
 locator=u['source_locator'];check(bool(locator) and (root/locator['file']).is_file(),'unit local locator: '+u['id'])
 if u.get('robot_packet'):check((root/u['robot_packet']).is_file(),'unit packet exists: '+u['id'])
 if u.get('required_game_context'):check((root/u['required_game_context']).is_file(),'unit game chapter exists: '+u['id'])
for v in jl('agent/publication_versions.jsonl'):
 check(v['event_start'] is None and v['date_start'] is None,'no invented date/event boundary')
for file in ['frc_strategy.sqlite','agent/retrieval.sqlite']:
 con=sqlite3.connect(root/file);check(con.execute('PRAGMA integrity_check').fetchone()[0]=='ok','SQLite integrity '+file)
 if file=='frc_strategy.sqlite':check(not con.execute('PRAGMA foreign_key_check').fetchall(),'research foreign keys')
 else:check(con.execute('SELECT count(*) FROM units').fetchone()[0]==len(units),'all units indexed')
 con.close()
r=query('search','slapdown','--year','2026','--kind','technical_claim','--limit','100')
check(r['matches']>0 and all(x['year']==2026 and x['kind']=='technical_claim' for x in r['results']),'year/kind search filters')
check(any(x.get('version_label')=='RE-BLITZ rebuild' for x in r['results']),'rebuild version retrievable')
r=query('search','floor','--robot','2026-254','--evidence','analyst_inference')
check(r['matches']>0 and all(x['robot']=='2026-254' and x['evidence']=='analyst_inference' for x in r['results']),'robot/evidence filter')
r=query('search','L1','algae','--year','2025','--limit','200')
check(r['matches']>0 and any(x['robot']=='2025-1323' for x in r['results']),'2025 role context retrievable')
r=query('packet','2026-2910');check(len(r['publication_version_groups'])>=2,'original and rebuild groups in one complete packet')
r=query('images','--robot','2026-2910');check(bool(r) and all(x['robot_id']=='2026-2910' for x in r),'image command')
r=query('read',units[0]['id']);check(r==units[0],'exact unit retrieval')
r=query('search','noresult0918273');check(r['matches']==0 and not r['results'],'explicit empty result')
r=query('search','PCH','--year','2026','--kind','event_benchmark');check(r['matches']>0 and all(x['kind']=='event_benchmark' for x in r['results']),'event benchmarks searchable')
r=query('search','tower','--kind','tower_sample');check(r['matches']>0,'tower-only aggregates searchable')
r=query('search','2022cmptx_sf1m1','--kind','einstein_record');check(r['matches']==1 and r['results'][0]['visual_review'] is False,'exact Einstein key and no-visual-review boundary')
check(db['robots']==robots and db['technicalNotes']==notes,'reader current data parity')
check(db['agentManifest']==manifest,'reader machine manifest parity')
check(len(jl('agent/evaluation_cases.jsonl'))==60,'evaluation cases present')

check(len([r for r in robots if r['year']==2018])==7 and len([r for r in robots if r['year']==2019])==6,'curated historical cohort counts')
check(all(r['epa'] is None and r['epa_rank'] is None for r in robots if r['year'] in [2018,2019]),'no fabricated historical EPA')
r=query('search','handoff','--year','2019','--kind','technical_claim','--limit','100');check(r['matches']>0,'historical handoff retrievable')
r=query('packet','2019-1323');check(any(n.get('code_revision') for n in r['technical_notes']),'pinned code evidence retained')
check(len(db['games'])==7 and all((root/f'docs/game_{y}.md').is_file() for y in [2018,2019]),'historical game chapters integrated')
check('2018' in subprocess.check_output([sys.executable,str(root/'scripts/query_agent.py'),'game','2018'],text=True),'historical game CLI')
check(all(u['required_game_context'] for u in units if u.get('robot') and u.get('year') in [2018,2019]),'historical retrieval attaches game context')

broken=[];refs=0
for f in root.rglob('*.md'):
 for m in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)',f.read_text()):
  u=m[1]
  if re.match(r'(?:https?:|mailto:|#)',u):continue
  refs+=1
  if not (f.parent/u.split('#')[0]).is_file():broken.append([str(f.relative_to(root)),u])
check(not broken,'all local Markdown reference paths resolve')
result={'status':'passed','checks':checks,'counts':manifest['counts'],'local_markdown_references':refs,'broken_local_references':broken,'scope':'Navigation, byte identity, metadata/packet preservation, CLI filtering and SQLite integrity; not new source review or model reasoning evaluation.'}
(root/'AGENT_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
