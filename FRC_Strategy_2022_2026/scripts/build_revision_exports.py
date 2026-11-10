"""Publish individual mechanism revisions without collapsing them into a final robot.

Edit data/mechanism_revisions.jsonl. This module is called by the physical
prebuild so an ordinary full rebuild also refreshes all revision exports.
"""
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def read(name):return [json.loads(l) for l in (ROOT/name).read_text().splitlines() if l.strip()]
def write(name,rows):(ROOT/name).write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in rows))

def build():
    revisions=read('data/mechanism_revisions.jsonl')
    notes=[n for n in read('data/technical_mechanisms.jsonl') if not n.get('mechanism_revision_id')]
    images=read('data/mechanism_images.jsonl');ims={i['id']:i for i in images}
    contexts=[c for c in read('data/context_documents.jsonl') if c.get('kind')!='mechanism_revision_history']
    for r in revisions:
        notes.append(dict(id=r['id'],mechanism_revision_id=r['id'],robot_id=r['robot_id'],year=int(r['robot_id'][:4]),binder_id='web-4414' if r['robot_id']=='2026-4414' else None,
            subsystem='transfer' if r['family']=='rotor' else 'scoring',title=r['publisher_label']+': individual prototype construction and change',
            version_label=r['robot_id']+' '+r['publisher_label']+' (publisher CAD prototype)',
            construction='Visible source-render construction: '+r['visible_construction'],team_stated_reason=r['team_stated_rationale'],
            engineering_analysis='Observed comparison: '+r['change_from_previous']+' Engineering interpretation: '+r['engineering_interpretation']+' Transfer limit: '+r['transfer_limit'],
            recommended_validation=r['validation_not_performed'],limitations=r['unknowns']+' '+r['reported_performance']+' Cross-family pairing is unknown.',
            source_url=r['source_url'],additional_sources=[r['source_image_url']],page_references=[],image_ids=r['image_ids'],
            evidence_type='visually_inspected_publisher_CAD_with_separate_editorial_change_analysis',performance_status=r['reported_performance'],review_scope=r['visual_review']))
        for iid in r['image_ids']:
            im=ims[iid];im['mechanism_revision_id']=r['id'];im['visual_review']=r['visual_review']
            im['source_locator']=r['source_locator'];im['visible_construction']=r['visible_construction']
            im['version_scope']='Publisher prototype ordinal only; event installation and rotor/shooter pairing unknown'
    # Feature-overview facts must not leak into all historical prototypes.
    for n in notes:
        if n['robot_id']=='2026-4414' and not n.get('mechanism_revision_id'):
            limit=' This is a cross-revision feature overview, not a single certified configuration. Do not apply these motor, contact or parameter descriptions to every RotorV1–V10 or ShooterV1–V11; read the individual revision records.'
            if limit not in n['limitations']:n['limitations']+=limit
    for rid in dict.fromkeys(r['robot_id'] for r in revisions):
        rs=[r for r in revisions if r['robot_id']==rid]
        body=f'# {rid}: individual rotor and shooter revisions\n\n'
        body+='Generated from `data/mechanism_revisions.jsonl`. These are publisher-labeled CAD prototypes, not certified event installations or a complete hardware genealogy. Rotor and shooter numbers are independent. In particular, RotorV10 and ShooterV11 are not a verified paired configuration.\n\n'
        body+='The source gallery supplies renders and ordinal labels. It does not provide a per-revision explanation of why each change was made. Visible differences, engineering interpretation, team rationale and reported outcomes are therefore separate below. A changed view or pose does not prove changed hardware.\n\n'
        for family in dict.fromkeys(r['family'] for r in rs):
            body+='## '+family.title()+' sequence\n\n| Publisher revision | Visible comparison | Evidence limit |\n|---|---|---|\n'
            for r in rs:
                if r['family']==family:body+=f'| {r["publisher_label"]} | {r["change_from_previous"]} | No event installation, per-revision outcome or cross-family pairing certified |\n'
            body+='\n'
        for r in rs:
            body+='## '+r['publisher_label']+'\n\n'
            for k,title in [('visible_construction','Visible construction'),('change_from_previous','Comparison to previous gallery ordinal'),('engineering_interpretation','Engineering interpretation'),('team_stated_rationale','Team rationale'),('reported_performance','Reported performance'),('unknowns','Unknowns'),('transfer_limit','Transfer limit')]:
                body+='### '+title+'\n\n'+r[k]+'\n\n'
            for iid in r['image_ids']:
                im=ims[iid];body+=f'![{r["publisher_label"]}](../{im["path"]})\n\n[Exact publisher image]({r["source_image_url"]}) · [Gallery]({r["source_url"]}). {r["visual_review"]}.\n\n'
        path='docs/'+rid+'_REVISION_HISTORY.md';(ROOT/path).write_text(body)
        contexts.append(dict(id=rid+'-revision-history',title=rid+' rotor and shooter revision history',year=int(rid[:4]),robot_id=rid,kind='mechanism_revision_history',body=body,source_urls=list(dict.fromkeys(r['source_url'] for r in rs))))
    audit=[]
    for rid in dict.fromkeys(i['robot_id'] for i in images if re.search(r'V\d',i.get('publisher_label') or '')):
        figures=[i for i in images if i['robot_id']==rid and re.search(r'V\d',i.get('publisher_label') or '')]
        linked={iid for r in revisions if r['robot_id']==rid for iid in r['image_ids']}
        audit.append(dict(robot_id=rid,version_labeled_image_ids=[i['id'] for i in figures],individual_revision_records=[r['id'] for r in revisions if r['robot_id']==rid],
            unresolved_image_ids=[i['id'] for i in figures if i['id'] not in linked],status='all_known_labeled_figures_have_individual_records' if all(i['id'] in linked for i in figures) else 'review_required_shared_or_unmapped_version_figures',
            boundary='Image-label audit only, not a census of all versions. Shared V1/V2 figures require interpretation; unknown does not mean historical content was deleted.'))
    write('data/technical_mechanisms.jsonl',notes);write('data/mechanism_images.jsonl',images);write('data/context_documents.jsonl',contexts)
    write('data/revision_coverage.jsonl',audit)
    write('tables/mechanism_revisions.jsonl',[dict(id=r['id'],robot_id=r['robot_id'],family=r['family'],ordinal=r['ordinal'],previous_revision_id=r['previous_revision_id'],data_json=json.dumps(r,ensure_ascii=False)) for r in revisions])
    return revisions

if __name__=='__main__':build()
