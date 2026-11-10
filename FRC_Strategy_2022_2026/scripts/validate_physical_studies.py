"""Check evidence relationships, source scope, SQL/reader parity and connected retrieval."""
import base64
import collections
import hashlib
import json
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

from PIL import Image
from interface_compatibility import compare

ROOT=Path(__file__).resolve().parents[1]
def read(p):return [json.loads(l) for l in (ROOT/p).read_text().splitlines() if l.strip()]
def write(p,a):(ROOT/p).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in a))
checks=0
def check(ok,message):
    global checks
    assert ok,message
    checks+=1

studies=read('data/physical_studies.jsonl');ports=read('data/mechanism_interfaces.jsonl')
notes=read('data/technical_mechanisms.jsonl');images=read('data/mechanism_images.jsonl')
params=read('data/technical_parameters.jsonl');coverage=read('data/evidence_coverage.jsonl')
ns={n['id']:n for n in notes};ims={i['id']:i for i in images};ps={p['id']:p for p in ports}
states={'supported','partial','unknown','not_applicable'}
check(len(studies)==7 and len({s['id'] for s in studies})==7,'separate original/rebuild plus five other studies')
check(len(ps)==len(ports)==20,'unique interface ports')
check(len(ns)==len(notes),'unique mechanism note IDs')
check(len(ims)==len(images),'unique image IDs')
for s in studies:
    packet=json.loads((ROOT/f'agent/robot_packets/{s["robot_id"]}.json').read_text())
    check(s in packet['physical_studies'],'complete source study in packet '+s['id'])
    check(all(p in packet['interface_ports'] for p in ports if p['study_id']==s['id']),'all interface contracts in packet')
    check('Unknown' in (ROOT/f'docs/physical/{s["id"]}.md').read_text(),'explicit evidence gaps in written study')
    for m in s['mechanisms']:
        check(m['id'] in ns,'mechanism technical-note relationship')
        check(ns[m['id']]['version_label']==s['version_label'],'exact study/note version')
        check(all(nid in ns for nid in m['note_ids']),'inherited source-note links resolve')
        check(all(i in ims for i in m['image_ids']),'mechanism-image links resolve')
        check(not any(ims[i]['kind']=='editorial_physical_reconstruction' for i in m['image_ids']),'editorial diagram never substitutes for primary visual evidence')
        check(m['coverage']['useful_image_inspected']['state']!='supported' or bool(m['image_ids']),'no image-free visual certification')
        check(all(x['state'] in states and x['reason'] for x in m['coverage'].values()),'typed coverage states and reasons')
        check(m['construction']==ns[m['id']]['construction'],'canonical construction agrees with ordinary note')
        check(m['unknowns']==ns[m['id']]['limitations'],'limitations travel with note')
for p in ports:
    check(p['mechanism_id'] in ns and p['study_id'] in {s['id'] for s in studies},'port foreign relationships')
    check(all(x['reason'] and x['state'] in states for x in p.values() if isinstance(x,dict) and 'state' in x),'port evidence reasons')
sources={s['id']:s for s in read('data/sources.jsonl')}
for p in params:
    check(bool(p.get('version_label')) and bool(p.get('source_location')) and bool(p.get('units')) and bool(p.get('operating_conditions')),'parameter source/version/conditions '+p['id'])
    check(p['source_url'].startswith('https://'),'parameter source URL')
    check(p['source_record_id'] in sources and sources[p['source_record_id']]['url'].split('#')[0]==p['source_url'].split('#')[0],'parameter source-record relationship '+p['id'])

image_audit=[]
access={a['url']:a for a in read('data/physical_source_access.jsonl')}
for im in images:
    path=ROOT/im['path']
    with Image.open(path) as pic:pic.verify()
    check(path.is_file(),'local asset exists and decodes '+im['id'])
    a=access.get(im['source_url'])
    image_audit.append(dict(image_id=im['id'],robot_id=im['robot_id'],path=im['path'],local_status='present_and_decodable',sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        external_destination_status=a['status'] if a else 'untested_this_pass',
        external_scope=a['detail'] if a else 'No new request; inherited attribution retained. Untested is not broken.',
        evidence_kind=im['kind'],visual_scope=im.get('visual_review',im.get('review_status','inherited metadata')),
        source_identity='editorial_not_source_image' if im['kind']=='editorial_physical_reconstruction' else 'See exact inspected scope / inherited metadata; no all-image fresh identity certification',
        useful_detail_limit=im.get('limitations','Crop or overview only; inspect hidden interfaces separately.')))
write('data/image_evidence_audit.jsonl',image_audit)
for n in notes:check(all(i in ims for i in n['image_ids']),'all note-to-image references '+n['id'])

con=sqlite3.connect(ROOT/'frc_strategy.sqlite')
check(con.execute('PRAGMA integrity_check').fetchone()[0]=='ok','research SQL integrity')
check(not con.execute('PRAGMA foreign_key_check').fetchall(),'all research foreign keys')
for table,rows in [('physical_studies',studies),('mechanism_interfaces',ports)]:
    actual={a[0]:json.loads(a[1]) for a in con.execute('SELECT id,data_json FROM '+table)}
    check(actual=={r['id']:r for r in rows},'research SQL canonical parity '+table)
for table,rows in [('technical_mechanisms',notes),('technical_parameters',params),('mechanism_images',images)]:
    actual={a[0]:json.loads(a[1]) for a in con.execute('SELECT id,metadata_json FROM '+table)}
    check(actual=={r['id']:r for r in rows},'normalized source metadata parity '+table)
con.close()

html=(ROOT/'index.html').read_text()
db=json.loads(re.search(r'<script id="database" type="application/json">(.*?)</script>',html,re.S)[1])
assets=json.loads(re.search(r'<script id="image-assets" type="application/json">(.*?)</script>',html,re.S)[1])
check(db['physicalStudies']==studies and db['mechanismInterfaces']==ports and db['evidenceCoverage']==coverage,'offline reader canonical parity')
for s in studies:
    for view in ['top','side','transition']:
        iid=s['id']+'-'+view
        check(base64.b64decode(assets[iid]['base64'])==(ROOT/ims[iid]['path']).read_bytes(),'drawing bytes embedded '+iid)

def query(*args):return json.loads(subprocess.check_output([sys.executable,str(ROOT/'scripts/query_agent.py'),*args],text=True))
examples=[]
for rid,term in [('2026-2910','backing'),('2026-1678','floor'),('2025-1323','handoff'),('2026-604','column'),('2026-27','restraint'),('2024-1690','pivot')]:
    r=query('search',term,'--robot',rid,'--kind','physical_mechanism','--limit','3')
    check(r['matches']>0,'connected retrieval '+rid)
    for hit in r['results']:
        text=json.loads(hit['text'])
        check(all(k in text for k in ['mechanism','packaging','piece_flow','whole_robot_unknowns']),'integrated construction/packaging/flow/gaps')
        check(all(k in text['mechanism'] for k in ['construction','operating_sequence','transfer','image_ids','unknowns']),'integrated evidence and transfer')
    examples.append(dict(command=f'python scripts/query_agent.py search {term} --robot {rid} --kind physical_mechanism --limit 3',matches=r['matches'],results=r['results']))
(ROOT/'data/physical_retrieval_examples.json').write_text(json.dumps(examples,ensure_ascii=False,indent=2)+'\n')
fuel=ps['physical-2026-1678-floor-output'];note=ps['physical-2024-1690-launcher-input']
check(compare(fuel,note)['status']=='incompatible_as_documented','cross-game mismatch rejected')
matching=compare(fuel,ps['physical-2026-2910-rebuild-launch-input'])
check(matching['status']=='unresolved' and not matching['compatible'],'same fuel never implies fit')
blocked=compare(ps['physical-2026-604-serializer-output'],ps['physical-2026-604-turret-ready-input'])
check(any('turret' in x for x in blocked['conflicts']),'1833 turret restriction exposed')
check(compare(note,fuel)['status']=='incompatible_as_documented','wrong port direction rejected')
historical=compare(ps['physical-2026-604-serializer-output'],ps['physical-2026-604-turret-ready-input'],False)
check(historical['status']=='unresolved' and not historical['compatible'],'historical policy bypass still needs physical evidence')

cohort=read('data/cohort_coverage.jsonl')
ranked=[c for c in cohort if c['cohort']=='original_ranked_cohort']
check(len(ranked)==125 and sum(c['dossier_present'] for c in ranked)==106,'125 ranked slots / 106 present')
check(sum(c['cohort']=='documented_substitution' for c in cohort)==19,'all substitutions preserved')
check(sum(c['cohort']=='curated_historical' for c in cohort)==13,'historical scope preserved')
check(len(read('data/cohort_research_attempts.jsonl'))==2,'both priority 1323 investigations retained')
check('aluminum' in ns['study6-2026-1678']['limitations'] and 'steel' in ns['study6-2026-1678']['construction'],'material discrepancy travels with earlier claim')
check(next(m for s in studies if s['robot_id']=='2026-27' for m in s['mechanisms'])['coverage']['useful_image_inspected']['state']=='partial','thumbnail never certified as internal figure')

result=dict(status='passed',checks=checks,source_images=len([i for i in images if i['kind']!='editorial_physical_reconstruction']),editorial_drawings=21,connected_retrieval_examples=len(examples),
    limitations=['No mechanical experiments or model-quality benchmark performed.','No complete CAD measurement or all-event version certification.','Team 27 internal figure recovery and several anchor interfaces remain open.','External URLs not newly tested are explicitly untested.'])
(ROOT/'PHYSICAL_UPGRADE_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
