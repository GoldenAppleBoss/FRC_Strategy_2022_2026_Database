"""Merge new source reviews into the latest saved standalone reader."""
from pathlib import Path
import base64
import gzip
import hashlib
import io
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parent
HTML = ROOT.parent / 'current/index.html'
OUTPUT = ROOT.parent / 'delivery/index.html'
text = HTML.read_text()

def tag(name):
    match = re.search(r'<script id="' + name + r'"[^>]*>(.*?)</script>', text, re.S)
    if match is None:
        raise ValueError(f'Missing {name} script')
    return match

def js(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))

def rows(raw):
    return [json.loads(line) for line in raw.splitlines() if line.strip()]

def jsonl(values):
    return ''.join(js(row) + '\n' for row in values).encode()

def encode(raw):
    return base64.b64encode(raw).decode()

db_tag = json.loads(tag('database')[1])
db = json.loads(gzip.decompress(base64.b64decode(db_tag['base64'])))
package = json.loads(tag('workbench-package')[1])
with zipfile.ZipFile(io.BytesIO(base64.b64decode(package['base64']))) as archive:
    files = {key: archive.read(key) for key in archive.namelist() if not key.endswith('/')}
assets = json.loads(tag('image-assets')[1])
robots = {r['id']: r for r in db['robots']}
reviews = {r['robot_id']: r for r in db['dossierReviews']}
audit = rows(files['data/image_visual_audit.jsonl'])
excluded = {r['image_id'] for r in audit if r['decision'] == 'excluded'}
units = {r['id']: r for r in rows(files['agent/retrieval_units.jsonl'])}
image_manifest = ROOT/'new_images.jsonl'
if image_manifest.exists():
    from PIL import Image
    added = {}
    for source in rows(image_manifest.read_bytes()):
        local = ROOT/source.pop('local_image')
        iid = source['id']
        rid = source['robot_id']
        if iid in assets:
            continue
        with Image.open(local) as picture:
            picture = picture.convert('RGB')
            picture.thumbnail((1350, 1350))
            width, height = picture.size
            out = io.BytesIO()
            picture.save(out, 'WEBP', quality=84, method=4)
        blob = out.getvalue()
        source.update(path=f'images/overview/{iid}.webp', media_type='image/webp',
                      width_px=width, height_px=height, bytes=len(blob),
                      sha256=hashlib.sha256(blob).hexdigest(), path_base='corpus_root',
                      reader_asset_id=iid, reader_url='index.html#image='+iid)
        assets[iid] = dict(mime='image/webp', base64=encode(blob))
        robots[rid]['images'].append(source)
        packet_key = f'agent/robot_packets/{rid}.json'
        packet = json.loads(files[packet_key])
        packet['dossier'] = robots[rid]
        packet['images'].append(source)
        files[packet_key] = js(packet).encode()
        audit.append(dict(image_id=iid, robot_id=rid, path=source['path'],
                          decision='retained_robot_overview', reason=source['interpretation_boundary']))
        added[iid] = source
        uid = 'image:'+iid
        units[uid] = dict(id=uid, title=source['caption'], text=js(source), kind='image_metadata',
                          evidence='visually_reviewed_team_publication', year=robots[rid]['year'], robot=rid,
                          subsystem=None, source_locator=dict(file='agent/image_catalog.jsonl',id=iid),
                          source_urls=[source['source_url']], robot_packet=packet_key,
                          required_game_context=f"docs/game_{robots[rid]['year']}.md")
    for key in ('data/mechanism_images.jsonl','agent/image_catalog.jsonl'):
        files[key] = jsonl(rows(files[key])+list(added.values()))
    files['data/robot_dossiers.jsonl'] = jsonl(db['robots'])
    files['data/image_visual_audit.jsonl'] = jsonl(audit)

pending_start = set(robots) - set(reviews)
keys = {'source_reviews', 'whole_robot_explanation', 'piece_flow', 'packaging_and_motion',
        'subsystems', 'revisions', 'transferable_principles', 'disconfirming_conditions', 'remaining_gaps'}
for name in ('2018','2019','historical','2022','2023','2024','2025','2026','extra','main'):
    path = ROOT / (name + '.jsonl')
    if not path.exists():
        continue
    # Research workers append incrementally. Ignore only a possible unfinished final write.
    raw = path.read_bytes()
    if raw and not raw.endswith(b'\n'):
        raw = raw[:raw.rfind(b'\n') + 1]
    for review in rows(raw):
        rid = review['robot_id']
        if rid not in robots:
            raise ValueError(f'Unknown robot {rid}')
        if keys - review.keys() or not review['source_reviews'] or not review['subsystems']:
            raise ValueError(f'Incomplete review {rid}')
        for source in review['source_reviews']:
            if not all(source.get(k) for k in ('url','title','locator','review_basis','facts','limitations')):
                raise ValueError(f'Incomplete source {rid}')
        reviews[rid] = review

def unit(uid, title, value, kind, robot, urls, **location):
    rid = robot['id']
    units[uid] = dict(
        id=uid, title=title, text=js(value), kind=kind,
        evidence='source_review_with_separate_interpretation',
        year=robot['year'], robot=rid, subsystem=None,
        source_locator=dict(file='data/dossier_research_reviews.jsonl', robot_id=rid, **location),
        source_urls=urls, robot_packet=f'agent/robot_packets/{rid}.json',
        required_game_context=f"docs/game_{robot['year']}.md"
    )

for rid, review in reviews.items():
    packet_path = f'agent/robot_packets/{rid}.json'
    packet = json.loads(files[packet_path])
    packet['source_review'] = review
    files[packet_path] = js(packet).encode()
    robot = robots[rid]
    unit('review:'+rid, f"{rid} {robot['robot']} complete robot study", review,
         'dossier_review', robot, [s['url'] for s in review['source_reviews']])
    prefix = 'review:'+rid+':mechanism:'
    for stale in [k for k in units if k.startswith(prefix)]:
        del units[stale]
    for index, mechanism in enumerate(review['subsystems']):
        unit(prefix+str(index+1), rid+' '+mechanism['name'], mechanism, 'reviewed_subsystem',
             robot, mechanism.get('source_urls', []), subsystem_index=index)


comparison_file = ROOT/'design_comparisons.jsonl'
if comparison_file.exists():
    comparisons = rows(comparison_file.read_bytes())
    for comparison in comparisons:
        assert set(comparison['robots']) <= robots.keys()
        key = 'design-comparison:'+comparison['id']
        source_urls = list(dict.fromkeys(s['url'] for rid in comparison['robots']
                                         for s in reviews.get(rid, {}).get('source_reviews', [])))
        units[key] = dict(id=key, title=comparison['title'], text=js(comparison),
                          kind='design_comparison', evidence='cross_case_analysis',
                          year=None, robot=None, subsystem=None,
                          source_locator=dict(file='data/design_comparisons.jsonl', id=comparison['id']),
                          source_urls=source_urls, robot_packet=None, required_game_context=None)
    db['designComparisons'] = comparisons
    files['data/design_comparisons.jsonl'] = jsonl(comparisons)

db['dossierReviews'] = [reviews[k] for k in sorted(reviews)]
files['data/dossier_research_reviews.jsonl'] = jsonl(db['dossierReviews'])
files['data/dossier_review_coverage.json'] = js(dict(
    reviewed=len(reviews), roster=len(robots), pending=sorted(robots.keys()-reviews.keys()),
    active_images=len(assets), excluded_images=len(excluded)
)).encode()
files['agent/retrieval_units.jsonl'] = jsonl(units.values())
manifest = db['agentManifest']
manifest['counts'].update(deep_dossier_reviews=len(reviews), retrieval_units=len(units), images=len(assets))
if db.get('designComparisons'):
    manifest['counts']['design_comparisons'] = len(db['designComparisons'])
    manifest['files']['design_comparisons'] = 'data/design_comparisons.jsonl'
files['agent/manifest.json'] = js(manifest).encode()

research_path = 'workbench/research.py'
files[research_path] = files[research_path].decode().replace(
    "'mechanism_revisions','architecture_cases'])",
    "'mechanism_revisions','architecture_cases','source_review'])"
).replace('emit(v[x.section] if x.section else v)', 'emit(v.get(x.section) if x.section else v)').encode()
contract_path = 'workbench/RUN_CONTRACT.md'
contract = files[contract_path].decode().replace(
    'Search beyond the five curated architecture examples.',
    'Search by piece path, packaging constraint and failure mode across seasons and teams.'
)
rule = 'Read each selected packet’s source_review where available. The reviewed_subsystem records point back to the full review. Use benchmark distributions with their stated event stage and sample denominator.'
if rule not in contract:
    contract += '\n' + rule + '\n'
files[contract_path] = contract.encode()
files.pop('maintenance/build.py', None)
for name in ['merge.py','verify.py','RESUME.md','human.js']:
    files['maintenance/'+name] = (ROOT/name).read_bytes()
for key in package['corpus_files']:
    package['corpus_files'][key] = hashlib.sha256(files[key].replace(b'\r\n',b'\n')).hexdigest()
buffer = io.BytesIO()
with zipfile.ZipFile(buffer,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for key,value in sorted(files.items()):
        archive.writestr(key,value)
raw = buffer.getvalue()
package.update(base64=encode(raw),sha256=hashlib.sha256(raw).hexdigest())
application = tag('application-source')[1]
marker = '// The reader starts in the design workspace.'
start = application.index(marker)
end = application.index('\ntabs();render();\nhandleImageHash();', start)
application = application[:start]+(ROOT/'human.js').read_text()+application[end:]
replacements = {'application-source':application, 'database':js(dict(encoding='gzip',base64=encode(gzip.compress(js(db).encode(),mtime=0)))),
                'workbench-package':js(package), 'image-assets':js(assets)}
for name,body in sorted(replacements.items(),key=lambda item:tag(item[0]).start(1),reverse=True):
    match = tag(name)
    text = text[:match.start(1)]+body+text[match.end(1):]
assert len(robots)==143 and len(db['mechanismRevisions'])==21
assert not set(assets)&excluded and len(db['benchmarks'])==292
assert set(assets)=={image['id'] for r in robots.values() for image in r['images']}
OUTPUT.parent.mkdir(exist_ok=True)
tmp = OUTPUT.with_suffix('.tmp')
tmp.write_text(text)
tmp.replace(OUTPUT)
print(js(dict(reviews=len(reviews), new=len(pending_start&reviews.keys()), pending=len(robots)-len(reviews), bytes=OUTPUT.stat().st_size)))
