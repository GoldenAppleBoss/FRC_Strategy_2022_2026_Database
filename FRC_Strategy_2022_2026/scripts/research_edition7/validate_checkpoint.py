from pathlib import Path
import collections,hashlib,json,re,sqlite3,subprocess,sys,zipfile
ROOT=Path(__file__).resolve().parents[2]
def rj(p):return [json.loads(l) for l in (ROOT/p).read_text().splitlines() if l.strip()]
def wj(p,v):(ROOT/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
checks=0
def check(v,msg):
 global checks
 assert v,msg
 checks+=1

ledger=rj('data/roboreplay_review_ledger.jsonl');recovery=rj('data/transcript_recovery_ledger.jsonl');matches=rj('data/einstein_reviews.jsonl');audits=rj('data/einstein_visual_audit.jsonl')
check(len(recovery)==11,'recovery count')
check(len({r['video_id'] for r in recovery})==11,'recovery identity')
for r in recovery:
 p=Path('/workspace/scratch')/f'roboreplay-{r["video_id"]}.txt'
 if p.exists():check(hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],'retained export fingerprint')
 check(r['timestamped_segments']>100,'nontrivial timestamped export')
 check(not r['raw_transcript_redistributed'] and not r['visual_review'],'scope')
check(sum(v['review_status']=='full_transcript_review' for v in ledger)==35,'caption reviews')
check(sum(v['review_status']=='unreviewed' for v in ledger)==9,'pending content review')
check(all(v['transcript_status']=='downloaded' for v in ledger),'prior inventory has no pending retrieval')
for r in recovery:
 v=next(v for v in ledger if v['video_id']==r['video_id'])
 check(bool(v['reviewed_ranges_seconds'])==r['new_full_caption_review'],'retrieval vs review')
 if r['new_full_caption_review']:
  er=v['expanded_review'];check(not er['full_caption_review_status_inherited'],'new full read identified')
  for s in er['sections']:
   check(r['first_caption_start_seconds']<=s['start_seconds']<=s['end_seconds']<=r['last_caption_start_seconds'],'new source window inside available-caption span')
   check(s['url']==v['url']+f'&t={s["start_seconds"]}s','navigation URL')
check(sum(len(v.get('expanded_review',{}).get('sections',[])) for v in ledger)==132,'expanded sections')
check(len(rj('data/roboreplay_quiz_prompts.jsonl'))==114,'quiz prompts')
check(len(matches)==len(audits)==80,'canonical matches')
check(collections.Counter(m['year'] for m in matches)=={2022:18,2023:15,2024:15,2025:16,2026:16},'year inventory')
check(all(m.get('video_url') for m in matches),'candidate video links')
check(len({m['video_url'] for m in matches})==80,'no duplicate candidate recordings')
check(sum(bool(a['access_attempt']) for a in audits)==6,'test scope')
check(all(not a['complete'] and not a['visual_review'] and not a['observed_events'] for a in audits),'no false visual completion')
check(all(not m['video_reviewed'] and not m['tactical_review_complete'] for m in matches),'visual flags')
check(sum(bool(m.get('commentary_timeline')) for m in matches)==6,'detailed match accounts')
for m in matches:
 for c in m.get('commentary_timeline',[]):
  check(c['match_clock_alignment'] is None and not c['independently_visually_verified'],'source clock not match clock')
 for a in ['red','blue']:
  if m['year']==2026:
   p=m['phase_detail'];total=sum(p[f'{a}_{x}'] for x in ['auto_fuel','auto_tower','transition_fuel','first_shift_fuel','second_shift_fuel','endgame_fuel','endgame_tower'])
   check(total==m[a+'_no_foul'],'2026 component sum')
m={m['key']:m for m in matches}
check(m['2026cmptx_sf3m1']['phase_detail']['red_auto_fuel']==188 and m['2026cmptx_sf3m1']['phase_detail']['blue_auto_fuel']==118,'match-3 auto figures')
check(m['2026cmptx_sf3m1']['red_no_foul']-188==529 and m['2026cmptx_sf3m1']['blue_no_foul']-118==509,'match-3 post-auto figures')
check((m['2026cmptx_sf6m1']['red_no_foul'],m['2026cmptx_sf6m1']['blue_no_foul'])==(678,691),'match-6 clean figures')
check(m['2022cmptx_sf1m2']['video_url'].endswith('-HI1RpdORwI'),'recovered match-2 link')

# Every original normalized table remains exactly reproducible.
con=sqlite3.connect(ROOT/'frc_strategy.sqlite');differences=[];counts={}
for p in sorted((ROOT/'tables').glob('*.jsonl')):
 rows=[json.loads(l) for l in p.read_text().splitlines() if l.strip()]
 cols=[r[1] for r in con.execute('PRAGMA table_info('+p.stem+')')]
 stored=con.execute('SELECT '+','.join(cols)+' FROM '+p.stem).fetchall()
 expected=[tuple(r.get(c) for c in cols) for r in rows]
 counts[p.stem]=len(stored)
 if collections.Counter(stored)!=collections.Counter(expected):differences.append(p.stem)
 check(collections.Counter(stored)==collections.Counter(expected),'normalized table '+p.stem)
check(con.execute('PRAGMA integrity_check').fetchone()[0]=='ok','main SQL integrity');con.close()
wj('REBUILD_VALIDATION.json',{'status':'passed','equal_tables':len(counts),'differences':differences,'row_counts':counts})

baseline=ROOT.parent/'FRC_Strategy_2022_2026.zip'
with zipfile.ZipFile(baseline) as z:
 for file in ['AGENT_VALIDATION.json','READER_VALIDATION.json','BROWSER_VALIDATION.json','REBUILD_VALIDATION.json','VALIDATION.json']:
  (ROOT/'validation'/('pre_research7_'+file)).write_bytes(z.read('FRC_Strategy_2022_2026/'+file))
 for file in ['data/robot_dossiers.jsonl','data/technical_mechanisms.jsonl','data/mechanism_images.jsonl','data/technical_parameters.jsonl']:
  check(z.read('FRC_Strategy_2022_2026/'+file)==(ROOT/file).read_bytes(),'preserved original robot/technical data '+file)
 for im in rj('data/mechanism_images.jsonl'):
  check(z.read('FRC_Strategy_2022_2026/'+im['path'])==(ROOT/im['path']).read_bytes(),'preserved source image '+im['id'])

for kind,query in [('match_commentary','6324'),('visual_audit_status','2026cmptx_f1m3')]:
 r=subprocess.run([sys.executable,str(ROOT/'scripts/query_agent.py'),'search',query,'--year','2026','--kind',kind],capture_output=True,text=True,check=True)
 check(json.loads(r.stdout)['matches']>0,'typed search '+kind)
summary={'status':'passed','scope':'Data, provenance boundaries and reproducibility; visual match audit is blocked and incomplete',
 'checks':checks,'new_transcripts_recovered':11,'new_complete_available_caption_reviews':2,'recovered_awaiting_full_review':9,'new_detailed_sections':27,'total_expanded_sections':132,
 'detailed_match_accounts':6,'candidate_match_recordings':80,'match_recording_pages_tested':6,'visual_audits_complete':0,'all_channel_inventory_complete':False,
 'original_image_bytes_preserved':504,'original_125_dossiers_preserved':True,'normalized_tables_equal':len(counts),'typed_match_commentary_and_audit_search':'passed'}
wj('RESEARCH7_VALIDATION.json',summary);print(json.dumps(summary,indent=2))
