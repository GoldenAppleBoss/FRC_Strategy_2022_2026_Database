"""Prevent known version figures from disappearing through grouping or gallery caps."""
import json
from pathlib import Path
import re
import sqlite3
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
def read(p):return [json.loads(l) for l in (ROOT/p).read_text().splitlines() if l.strip()]
checks=0
def check(ok,label):
    global checks
    assert ok,label
    checks+=1

rs=read('data/mechanism_revisions.jsonl');ims=read('data/mechanism_images.jsonl')
notes={n['id']:n for n in read('data/technical_mechanisms.jsonl')}
byid={r['id']:r for r in rs}
check(len(byid)==len(rs),'unique revisions')
check(len([r for r in rs if r['robot_id']=='2026-4414' and r['family']=='rotor'])==10,'all ten known rotor renders')
check(len([r for r in rs if r['robot_id']=='2026-4414' and r['family']=='shooter'])==11,'all eleven known shooter renders')
for r in rs:
    check(r['id'] in notes and notes[r['id']]['mechanism_revision_id']==r['id'],'individual technical note '+r['id'])
    check(notes[r['id']]['image_ids']==r['image_ids'],'exact note/figure relationship')
    check(r['event_installation'] is None and r['paired_other_mechanism_revision'] is None,'no invented event or pairing')
    if r['previous_revision_id']:
        prev=byid[r['previous_revision_id']]
        check(prev['family']==r['family'] and prev['robot_id']==r['robot_id'] and prev['ordinal']==r['ordinal']-1,'same-family ordinal predecessor')
    for iid in r['image_ids']:
        im=next(i for i in ims if i['id']==iid)
        check(im['publisher_label']==r['publisher_label'] and im['mechanism_revision_id']==r['id'],'publisher label / figure identity')
        check(im['image_url']==r['source_image_url'],'original publisher image locator retained')
    p=json.loads((ROOT/f'agent/robot_packets/{r["robot_id"]}.json').read_text())
    check(r in p['mechanism_revisions'],'complete revision in packet')
    hit=json.loads(subprocess.check_output([sys.executable,str(ROOT/'scripts/query_agent.py'),'search',r['publisher_label'],'--robot',r['robot_id'],'--kind','mechanism_revision'],text=True))
    check(any(x['id']==r['id']+':revision' for x in hit['results']),'exact revision retrieval '+r['publisher_label'])
    check('not' in r['team_stated_rationale'].lower() and r['reported_performance'].startswith('No '),'unknown rationale and outcomes explicit')
con=sqlite3.connect(ROOT/'frc_strategy.sqlite')
check(not con.execute('PRAGMA foreign_key_check').fetchall(),'revision foreign keys')
check({row[0]:json.loads(row[1]) for row in con.execute('SELECT id,data_json FROM mechanism_revisions')}==byid,'SQL source parity')
con.close()
html=(ROOT/'index.html').read_text()
db=json.loads(re.search(r'<script id="database" type="application/json">(.*?)</script>',html,re.S)[1])
check(db['mechanismRevisions']==rs,'reader contains all individual revisions')
check('n.image_ids.slice(0,4)' not in html,'no hidden first-four image truncation')
catalog={i['id']:i for i in read('agent/image_catalog.jsonl')}
check(all(iid in catalog for r in rs for iid in r['image_ids']),'all revision assets in delivered catalogue')
baseline=json.loads((ROOT/'data/revision_preservation_baseline.json').read_text())
for iid,digest in baseline['images'].items():
    check(iid in catalog and catalog[iid]['sha256']==digest,'pre-correction image preserved byte-for-byte '+iid)
check(set(baseline['technical_note_ids'])<=set(notes),'all pre-correction technical notes preserved')
check(set(baseline['parameter_ids'])<={p['id'] for p in read('data/technical_parameters.jsonl')},'all pre-correction parameters preserved')
check(set(baseline['robot_ids'])<={p['id'] for p in read('data/robot_dossiers.jsonl')},'all pre-correction robot dossiers preserved')
audit=read('data/revision_coverage.jsonl')
check(next(a for a in audit if a['robot_id']=='2026-4414')['unresolved_image_ids']==[],'all known 4414 labeled figures mapped')
check({a['robot_id'] for a in audit}>={'2026-4414','2018-2898','2018-971'},'other known version-labeled figures audited without fabricated interpretation')
result=dict(status='passed',checks=checks,individual_revisions=len(rs),rotor_revisions=10,shooter_revisions=11,scope='Known publication labels, images, typed records and retrieval, not complete event/version certification or performance reproduction.')
(ROOT/'REVISION_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
