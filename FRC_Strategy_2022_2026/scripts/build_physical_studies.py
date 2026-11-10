"""Build drawings, Markdown, coverage and normalized exports from physical-study JSONL.

Canonical research: data/physical_studies.jsonl and mechanism_interfaces.jsonl.
Drawings are explicitly unscaled reconstructions, never fabrication geometry.
Run before rebuild_database.py and build_agent_and_reader.py.
"""
import collections
import csv
import hashlib
import json
import math
from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    return [json.loads(line) for line in (ROOT/name).read_text().splitlines() if line.strip()]

def write(name, rows):
    (ROOT/name).write_text(''.join(json.dumps(row, ensure_ascii=False,separators=(',',':'))+'\n' for row in rows))

def obj(name, data):
    (ROOT/name).write_text(json.dumps(data, ensure_ascii=False, **({'separators':(',',':')} if name=='data/reader_payload.json' else {'indent':2}))+'\n')

def font(size):
    for name in ['DejaVuSans.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf','C:/Windows/Fonts/arial.ttf']:
        try:return ImageFont.truetype(name,size)
        except OSError:pass
    return ImageFont.load_default(size=size)

def drawing(study, view):
    """Physical arrangement plus contact-order inset; shapes have no geometric scale."""
    pic = Image.new('RGB', (1400, 1000), '#fafbf9')
    d = ImageDraw.Draw(pic)
    navy, green, orange = '#193342', '#227c68', '#a44b18'
    def label(x,y,text,width=45,color=navy,size=21):
        d.multiline_text((x,y), '\n'.join(textwrap.wrap(text,width)),font=font(size),fill=color,spacing=6)
    def box(b,text,fill='#e0ece7',width=22):
        d.rounded_rectangle(b,12,fill=fill,outline=navy,width=3)
        label(b[0]+12,b[1]+12,text,width,size=20)
    def arrow(points):
        d.line(points,fill=orange,width=6)
        a,b=points[-2:];ang=math.atan2(b[1]-a[1],b[0]-a[0])
        d.polygon([b,(b[0]-17*math.cos(ang-.5),b[1]-17*math.sin(ang-.5)),(b[0]-17*math.cos(ang+.5),b[1]-17*math.sin(ang+.5))],fill=orange)
    def dashed(b):
        x0,y0,x1,y1=b
        for x in range(x0,x1,20):
            d.line((x,y0,min(x+10,x1),y0),fill=orange,width=3)
            d.line((x,y1,min(x+10,x1),y1),fill=orange,width=3)
        for y in range(y0,y1,20):
            d.line((x0,y,x0,min(y+10,y1)),fill=orange,width=3)
            d.line((x1,y,x1,min(y+10,y1)),fill=orange,width=3)
    label(45,25,study['robot_id']+' / '+study['version_label'],85,size=26)
    label(45,105,view.upper()+' - EDITORIAL RECONSTRUCTION - NOT TO SCALE',90,color=orange,size=23)
    family=study['layout']['family']
    if view=='top':
        d.rectangle((270,230,930,730),outline=navy,width=7)
        dashed((235,195,965,765))
        label(280,170,'Rear / launcher side (editorial orientation)',60,size=19)
        label(300,780,'Front / acquisition side',45,size=20)
        label(1000,240,'Dashed: bumper / motion envelope schematic; offsets UNKNOWN',27,color=orange)
        if family!='partial':
            for x,y in [(290,250),(800,250),(290,620),(800,620)]:
                box((x,y,x+105,y+85),'Drive module','#e3e5eb',9)
        if family=='rotor':
            d.ellipse((405,300,795,670),fill='#e0ece7',outline=navy,width=3)
            d.ellipse((525,405,675,555),outline=orange,width=4)
            label(448,330,'Circular bucket',25)
            label(530,435,'Up-feed',14,size=19)
            label(995,380,'Upper turret supported over bucket; yaw sweep UNKNOWN',28)
            arrow([(900,400),(660,450)])
            box((410,690,790,760),'Front intake + linked sliding wall',width=30)
            label(435,245,'Rear battery access',30,size=18)
        elif family=='lift':
            box((420,310,780,590),'Central shoulder / A-frame; mast and wrist above',width=25)
            box((390,670,810,760),'Shared-axis coral / algae pickups',width=30)
            dashed((375,205,825,665))
            label(995,400,'Mast/wrist swept footprint UNKNOWN; dashed allocation is not CAD',28)
            arrow([(600,710),(600,590),(600,410)])
        elif family=='dual':
            box((140,370,285,610),'Left collector',width=10)
            box((915,370,1060,610),'Right collector',width=10)
            box((430,390,770,610),'Constrained serpentine; inlet merge UNKNOWN',width=22)
            box((415,245,785,345),'Fixed launcher',width=25)
            arrow([(280,490),(430,490)]);arrow([(915,490),(770,490)])
            arrow([(600,390),(600,345)])
        else:
            box((415,260,785,350),'Launcher / rear structure',width=25)
            box((415,390,785,605),'Low feed' if family=='note' else 'Hopper above floor; hidden interfaces UNKNOWN',width=24)
            box((390,690,810,760),'Front intake',width=28)
            arrow([(600,690),(600,605)]);arrow([(600,390),(600,350)])
            if family=='partial':
                label(1000,420,'Module locations are a generic locator only: historical positions UNKNOWN',28,color=orange)
        label(45,850,study['layout']['frame'],105,size=21)
        battery={'2026-1678':'Battery/electronics below hinged floor. Battery extraction clearance UNKNOWN.',
                 '2026-604':'Rear battery access and split bucket are source-supported. Exact compartment geometry UNKNOWN.',
                 '2026-2910':'Electronics under brainpan require underside access; rebuild partly above pan. Battery route UNKNOWN.'}
        label(45,895,battery.get(study['robot_id'],'Battery and electronics locations / service route UNKNOWN in this reconstruction.'),110,size=19)
    elif view=='side':
        # Common editorial local axis, with robot-specific support / path structures.
        d.line((100,750,1250,750),fill=navy,width=3)
        box((270,670,1060,720),'Chassis / reaction into drive rails',width=60)
        box((180,610,270,720),'Bumper',width=6)
        label(60,765,'Front / pickup',25,size=19);label(1070,765,'Rear',15,size=19)
        if family=='lift':
            d.line((650,635,820,255),fill=navy,width=25)
            dashed((565,190,1010,630))
            box((730,205,970,305),'Carriage + wrist',width=17)
            box((130,510,365,605),'Donor intake',width=16)
            d.line((600,635,700,415,850,635),fill=navy,width=6)
            label(945,335,'A-frame / shoulder reaction',25)
            arrow([(330,530),(520,445),(760,280)])
            label(65,320,'Direct handoff at coordinated shoulder/lift/wrist pose; overlap UNKNOWN',33)
        elif family=='rotor':
            box((370,500,820,630),'Circular bucket / rotating capture',width=30)
            box((660,300,775,505),'Ball column',width=8)
            box((590,220,910,315),'Historical yaw turret',width=24)
            d.line((530,635,530,195,990,195,990,635),fill=navy,width=7)
            label(1020,300,'Upper support; exact attachment loads UNKNOWN',23)
            arrow([(170,570),(400,550),(700,550),(700,320)])
            label(360,420,'Split bucket and removable rear wall for service',35,size=18)
        elif family=='note':
            box((340,530,650,610),'Flat note transport',width=23)
            box((700,435,1030,575),'Elevation launcher',width=23)
            d.ellipse((660,530,705,575),outline=orange,width=5)
            dashed((650,370,1085,610))
            arrow([(170,580),(440,565),(685,550),(900,480)])
            label(640,285,'Pivot-related feed; exact overlap / deflector shape UNKNOWN',42)
            label(100,420,'Note remains approximately flat at acquisition',32)
        else:
            box((330,525,775,620),'Floor / constrained path' if family=='dual' else 'Roller floor under inventory',width=33)
            box((820,275,1110,480),'Launcher / hood',width=20)
            if family=='partial':
                label(800,190,'Internal locations UNKNOWN',35,color=orange)
            d.line((810,635,810,260,1120,260,1120,635),fill=navy,width=5)
            arrow([(150,580),(410,560),(740,540),(870,460),(995,325)])
            dashed((275,240,815,635))
            label(300,285,'Storage / deployed envelope; exact outline UNKNOWN',33)
            if study['robot_id']=='2026-1678':
                box((390,615,775,665),'Electrical bay below floor',width=35)
                label(70,150,'Upper storage moves with climber; front wall with intake',50)
            if study['robot_id']=='2026-2910' and family=='wide':
                label(80,150,'Intake rests on bumper fabric; expansion follows intake',50)
        label(45,850,'Solid geometry: editorial module placement, not measured outlines. Dashed: motion/storage extent UNKNOWN.',110,size=20)
        label(45,905,'Source dimensions only in labels. No CAD-derived measurement; no certified battery extraction or ground clearance.',110,size=19)
    else:
        label(80,180,'Difficult transition: physical contact order, source-supported portions only. Exact positions and gaps UNKNOWN.',98,size=23)
        def ball(x,y,r=29):d.ellipse((x-r,y-r,x+r,y+r),fill='#f4ca58',outline=navy,width=3)
        def roller(x,y,r=23,passive=False):d.ellipse((x-r,y-r,x+r,y+r),fill='#e3e5eb' if passive else '#77b5a5',outline=navy,width=3)
        if family=='rotor':
            d.ellipse((105,300,475,625),outline=navy,width=5)
            ball(195,420);ball(255,530);ball(390,370)
            d.arc((175,365,405,570),20,290,fill=green,width=8)
            arrow([(280,595),(340,555)])
            label(100,645,'TOP: capture sweeps through bucket inventory',31)
            d.rectangle((740,295,845,605),outline=navy,width=4)
            for y in [555,490,425,360]:ball(792,y)
            roller(720,560);roller(865,560)
            arrow([(790,600),(790,265)])
            label(620,640,'SIDE: successive fuel pushes ball column upward',35)
            label(965,310,'Separate rotation and up-feed drives; tube from corrugated plastic / printed ends',29)
            label(965,505,'Top outlet readiness pauses feed. Historical turret retained; fixed outlet redesign unvalidated.',29,color=orange)
        elif family=='lift':
            # Coral is a tube, not a spherical fuel piece. Two poses express handoff
            # ownership, without inventing a dimensionally exact donor/receiver pose.
            for x,t in [(120,'1. Donor captures / centers'),(780,'2. Receiver captures; donor clears')]:
                d.rounded_rectangle((x,410,x+330,465),15,fill='#f4ca58',outline=navy,width=3)
                roller(x+80,390);roller(x+235,490)
                label(x,545,t,31)
            roller(1130,385);roller(1130,490)
            dashed((1020,330,1220,525))
            arrow([(480,440),(735,440)])
            label(90,275,'Diffuse Banner / CANdi: donor detection',40)
            label(755,275,'Retroreflective Banner / CANdi: claw capture',43)
            label(420,655,'Unknown mechanical overlap and timing: these two detections are different ownership states.',65,color=orange)
        elif family=='note':
            d.ellipse((130,470,420,505),fill='#f4ca58',outline=navy,width=3)
            d.ellipse((205,479,345,496),fill='#fafbf9',outline=navy,width=2)
            for x in [150,270,390]:roller(x,535,21)
            d.ellipse((720,430,1010,465),fill='#f4ca58',outline=navy,width=3)
            d.ellipse((795,439,935,456),fill='#fafbf9',outline=navy,width=2)
            roller(750,490,23);roller(950,490,23);roller(950,400,23)
            d.ellipse((580,480,620,520),outline=orange,width=5)
            dashed((450,365,720,600))
            arrow([(390,480),(730,445)])
            label(95,300,'Flat note / stationary transport',35)
            label(780,300,'Pivoting launcher contacts',32)
            label(415,620,'Pivot-related power routing is known; exact piece-support overlap is UNKNOWN.',53,color=orange)
            label(930,590,'Under-shooter dead space: deflector blocks entry. Final shape not recovered.',30)
        elif family=='dual':
            box((100,340,350,445),'Left intake',width=18)
            box((100,555,350,660),'Right intake',width=18)
            dashed((500,340,770,660))
            label(525,425,'MERGE geometry UNKNOWN',17,color=orange)
            arrow([(350,390),(500,430)]);arrow([(350,605),(500,550)])
            box((920,390,1250,580),'Serpentine / feeder',width=22)
            arrow([(770,490),(920,490)])
            label(925,630,'Successive contacts are source-supported; merge route not invented.',30)
        else:
            # Schematic section through floor-to-launcher; counts and positions here
            # illustrate contacts, never a replica of all physical rollers.
            for x,y in [(150,590),(250,575),(350,560),(450,545)]:roller(x,y)
            ball(220,520);ball(425,490)
            roller(640,475,42);roller(730,445,24,passive=family=='partial')
            ball(700,390)
            roller(895,350,70);roller(1020,310,26);roller(1065,250,26)
            arrow([(170,515),(430,480),(660,430),(820,345),(1050,190)])
            label(80,640,'Floor contacts supply supported stream',30)
            label(520,560,'Passive upper restraint' if family=='partial' else 'Feeder / backing turn travel upward',30)
            label(895,430,'Drum / hood contacts',25)
            if family=='partial':
                label(920,520,'Source compression: drum 3/8 in; final 1/2 in. Gap definition UNKNOWN.',29,color=orange)
            else:
                label(520,280,'Curved support path: exact section / contact gaps UNKNOWN',37,color=orange)
        label(65,785,study['unknowns'][0],110,color=orange,size=20)
        label(65,850,'Yellow: piece states. Green: powered contact. Gray: passive contact. These are editorial symbols, not CAD.',115,size=19)
        label(85,900,'Use cited source figures to identify actual parts. This drawing does not establish ownership overlap or fit.',110,size=20)
    path=f'images/physical/{study["id"]}-{view}.png'
    pic.save(ROOT/path)
    return path

def main():
    from build_architecture_exports import build as build_architectures
    build_architectures()
    from build_revision_exports import build
    build()
    studies=read('data/physical_studies.jsonl')
    interfaces=read('data/mechanism_interfaces.jsonl')
    notes=read('data/technical_mechanisms.jsonl')
    params=read('data/technical_parameters.jsonl')
    sources=read('data/sources.jsonl')
    source_by_url={s['url'].split('#')[0]:s for s in sources}
    def source_id(url):
        base=url.split('#')[0]
        if base not in source_by_url:
            source=dict(id='physical-source-'+hashlib.sha256(base.encode()).hexdigest()[:16],url=base,title='Physical study / parameter source',kind='technical_source_reference',review_basis='Selected source claims only; detailed review/visual scope belongs to study and image metadata',retrieved_on='2026-11-07')
            sources.append(source);source_by_url[base]=source
        return source_by_url[base]['id']
    for p in params:p['source_record_id']=source_id(p['source_url'])
    for s in studies:s['source_record_ids']=[source_id(u) for u in s['source_urls']]
    write('data/technical_parameters.jsonl',params)
    write('data/physical_studies.jsonl',studies)
    write('data/sources.jsonl',sources);write('tables/sources.jsonl',sources)
    images=[i for i in read('data/mechanism_images.jsonl') if i.get('kind')!='editorial_physical_reconstruction']
    contexts=[c for c in read('data/context_documents.jsonl') if c.get('kind')!='physical_robot_study']
    (ROOT/'docs/physical').mkdir(exist_ok=True)
    coverage=[]
    for s in studies:
        paths=[]
        for view in ['top','side','transition']:
            path=drawing(s,view);paths.append(path)
            images.append(dict(id=s['id']+'-'+view,robot_id=s['robot_id'],kind='editorial_physical_reconstruction',path=path,
                source_url=s['source_urls'][0],caption=f'{s["version_label"]}: {view}. {s["drawing_provenance"]}',
                publisher_label=f'{s["robot_id"]} {view} reconstruction',review_status='generated deterministic editorial drawing; inspect source figures separately',
                visual_review='Editorial artifact, not primary-source visual evidence',whole_robot_photo=False,
                rights='Original editorial drawing; underlying team reference attribution retained.',provenance=s['drawing_provenance'],study_id=s['id']))
        body=f'# {s["robot_id"]}: {s["version_label"]}\n\nGenerated from `data/physical_studies.jsonl`; edit that authoritative record.\n\n'
        body+='## Whole robot and packaging\n\n'+s['packaging']+'\n\n## Piece flow\n\n'+s['piece_flow']+'\n\n'
        body+='## Annotated views\n\n'+s['drawing_provenance']+'\n\n'
        for path in paths:body+=f'![{Path(path).stem}](../../{path})\n\n'
        for m in s['mechanisms']:
            body+='## '+m['title']+'\n\n'
            for field,title in [('construction','Published construction'),('team_stated_rationale','Team rationale / attribution boundary'),('operating_sequence','Editorial operating reconstruction'),('engineering_interpretation','Engineering interpretation'),('transfer','Transfer and compatibility limits'),('unknowns','Unknowns'),('validation_not_performed','Proposed validation, not performed')]:
                body+='### '+title+'\n\n'+m[field]+'\n\n'
            for iid in m['image_ids']:
                im=next(i for i in images if i['id']==iid)
                body+=f'![{im["caption"]}](../../{im["path"]})\n\nFigure `{iid}`. [Source]({im["source_url"]}). '+im.get('limitations','Visible scope only; hidden geometry, precise dimensions and event installation are not established.')+'\n\n'
            body+='### Evidence coverage\n\n| Evidence | State | Reason |\n|---|---|---|\n'
            for field,a in m['coverage'].items():body+=f'| {field} | {a["state"]} | {a["reason"]} |\n'
            body+='\n'
            coverage.append(dict(robot_id=s['robot_id'],study_id=s['id'],mechanism_id=m['id'],version_label=s['version_label'],assessment='explicit_editorial_review_2026-11-07',evidence=m['coverage']))
        body+='## Interface records\n\n'
        for p in interfaces:
            if p['study_id']!=s['id']:continue
            body+='### '+p['id']+'\n\n| Field | State | Value / limitation |\n|---|---|---|\n'
            for k,a in p.items():
                if isinstance(a,dict) and 'state' in a:
                    body+=f'| {k} | {a["state"]} | {a["value"] if a["value"] is not None else "Unknown"}. {a["reason"]} |\n'
            body+='\n'+p['transfer_limit']+'\n\n'
        body+='## Remaining whole-robot gaps\n\n'+'\n'.join('- '+x for x in s['unknowns'])+'\n\n## Sources\n\n'+'\n'.join('- '+u for u in s['source_urls'])+'\n'
        path='docs/physical/'+s['id']+'.md';(ROOT/path).write_text(body)
        contexts.append(dict(id=s['id'],robot_id=s['robot_id'],year=int(s['robot_id'][:4]),kind='physical_robot_study',title=s['robot_id']+' physical construction / interfaces / transfer',body=body,source_urls=s['source_urls']))
    # Unassessed legacy descriptions must not silently become complete evidence.
    for r in read('data/robot_dossiers.jsonl'):
        for sub in r['subsystems']:
            if any(c.get('mechanism_id') and c['robot_id']==r['id'] and next(n['subsystem'] for n in notes if n['id']==c['mechanism_id'])==sub for c in coverage):continue
            coverage.append(dict(robot_id=r['id'],subsystem=sub,assessment='legacy_not_reassessed',evidence={
                k:dict(state='unknown',value=None,reason='Legacy synopsis retained; evidence-specific review not completed in this upgrade. Unknown assessment does not mean missing mechanism.')
                for k in ['synopsis','construction','operating_sequence','interfaces','packaging','useful_image_inspected','parameters','version','source_locator','remaining_unknowns']}))
    write('data/evidence_coverage.jsonl',coverage)
    write('data/mechanism_images.jsonl',images)
    write('data/context_documents.jsonl',contexts)
    # Regenerate normalized tables from authoritative JSONL; no ad-hoc dual writes.
    write('tables/technical_mechanisms.jsonl',[dict(id=n['id'],robot_id=n['robot_id'],binder_id=n.get('binder_id'),subsystem=n['subsystem'],title=n['title'],construction=n['construction'],team_stated_reason=n['team_stated_reason'],engineering_analysis=n['engineering_analysis'],recommended_validation=n['recommended_validation'],limitations=n['limitations'],metadata_json=json.dumps(n,ensure_ascii=False)) for n in notes])
    write('tables/technical_parameters.jsonl',[dict(id=p['id'],robot_id=p['robot_id'],binder_id=p.get('binder_id'),component=p['component'],pdf_page=p.get('pdf_page'),published_parameters=p['published_parameters'],source_url=p['source_url'],metadata_json=json.dumps(p,ensure_ascii=False)) for p in params])
    write('tables/mechanism_images.jsonl',[dict(id=i['id'],robot_id=i['robot_id'],path=i['path'],source_url=i['source_url'],caption=i['caption'],publisher_label=i.get('publisher_label'),review_status=i.get('review_status'),metadata_json=json.dumps(i,ensure_ascii=False)) for i in images])
    write('tables/context_documents.jsonl',[dict(id=c['id'],title=c['title'],year=c.get('year'),robot_id=c.get('robot_id'),kind=c['kind'],body_markdown=c['body'],source_urls_json=json.dumps(c.get('source_urls',[]))) for c in contexts])
    write('tables/physical_studies.jsonl',[dict(id=s['id'],robot_id=s['robot_id'],version_label=s['version_label'],data_json=json.dumps(s,ensure_ascii=False)) for s in studies])
    write('tables/mechanism_interfaces.jsonl',[dict(id=p['id'],study_id=p['study_id'],mechanism_id=p['mechanism_id'],role=p['role'],data_json=json.dumps(p,ensure_ascii=False)) for p in interfaces])
    write('tables/physical_figure_links.jsonl',[dict(mechanism_id=m['id'],image_id=iid) for s in studies for m in s['mechanisms'] for iid in m['image_ids']])
    payload=json.loads((ROOT/'data/reader_payload.json').read_text())
    payload.update(mechanismRevisions=read('data/mechanism_revisions.jsonl'),contextDocs=contexts,technicalNotes=notes,technicalParameters=params,physicalStudies=studies,mechanismInterfaces=interfaces,evidenceCoverage=coverage)
    robots=read('data/robot_dossiers.jsonl')
    audits=read('data/binder_audit.jsonl')
    for a in audits:
        a['technical_note_ids']=[n['id'] for n in notes if n['robot_id']==a['robot_id']]
        a['physical_study_ids']=[s['id'] for s in studies if s['robot_id']==a['robot_id']]
    write('data/binder_audit.jsonl',audits)
    write('tables/binder_audit.jsonl',[dict(robot_id=a['robot_id'],status=a['status'],metadata_json=json.dumps(a,ensure_ascii=False)) for a in audits])
    payload['binderAudit']=audits
    for r in robots:
        r['binder_audit']=next(a for a in audits if a['robot_id']==r['id'])
        r['images']=[i for i in images if i['robot_id']==r['id']]
        r['technical_note_ids']=[n['id'] for n in notes if n['robot_id']==r['id']]
        r['evidence_coverage_path']='data/evidence_coverage.jsonl'
        for s in studies:
            if s['robot_id']==r['id']:
                r['primary']=list(dict.fromkeys(r['primary']+s['source_urls']))
                r['source_ids']=list(dict.fromkeys(r['source_ids']+s['source_record_ids']))
    write('data/robot_dossiers.jsonl',robots)
    payload['robots']=robots
    payload['sources']=sources
    associations=read('tables/robot_sources.jsonl')
    existing={(a['robot_id'],a['source_id']) for a in associations}
    for s in studies:
        for sid in s['source_record_ids']:
            if (s['robot_id'],sid) not in existing:
                associations.append(dict(robot_id=s['robot_id'],source_id=sid,relationship='physical study primary / retained technical source'))
                existing.add((s['robot_id'],sid))
    write('tables/robot_sources.jsonl',associations)
    write('tables/robot_dossiers.jsonl',[dict(id=r['id'],year=r['year'],team=r['team'],team_name=r['team_name'],robot_name=r['robot'],epa_rank=r['epa_rank'],epa=r['epa'],epa_pre_champs=r['epa_pre_champs'],architecture=r['architecture'],analyst_inference=r['analysis'],limits_json=json.dumps(r['limits']),coverage_json=json.dumps(r['coverage']),version_audit=r['version_audit'],strict_acceptance=r['strict_acceptance'],tags_json=json.dumps(r['tags'])) for r in robots])
    index=ROOT/'data/robot_index.csv'
    with index.open() as f:cols=next(csv.reader(f))
    with index.open('w',newline='') as f:
        out=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore',lineterminator='\n');out.writeheader()
        for r in robots:out.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()})
    audit=json.loads((ROOT/'data/audit.json').read_text())
    audit.update(robots=len(robots),architecture_cases=len(read('data/architecture_cases.jsonl')),snapshot='2026-11-07',technical_notes=len(notes),curated_images=len(images),robot_years_with_images=len({i['robot_id'] for i in images}),context_documents=len(contexts),physical_studies=len(studies),mechanism_interface_ports=len(interfaces),published_parameters=len(params),evidence_coverage='Explicit mechanism assessments; legacy rows marked unassessed, not complete.')
    payload['audit']=audit;obj('data/audit.json',audit);obj('data/reader_payload.json',payload)
    summary=dict(robot_dossiers=len(robots),technical_notes=len(notes),technical_parameters=len(params),parameter_robot_years=len({p['robot_id'] for p in params}),images=len(images),source_images=sum(i.get('kind')!='editorial_physical_reconstruction' for i in images),editorial_drawings=sum(i.get('kind')=='editorial_physical_reconstruction' for i in images),dossiers_without_images=sum(not any(i['robot_id']==r['id'] for i in images) for r in robots),dossiers_with_one_note=sum(sum(n['robot_id']==r['id'] for n in notes)==1 for r in robots),architecture_and_interfaces_notes=sum(n['subsystem']=='architecture_and_interfaces' for n in notes),notes_without_image_ids=sum(not n['image_ids'] for n in notes),physical_studies=len(studies),interface_ports=len(interfaces),reviewed_mechanism_assessments=sum(c['assessment']!='legacy_not_reassessed' for c in coverage))
    obj('data/physical_upgrade_metrics.json',summary)
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
