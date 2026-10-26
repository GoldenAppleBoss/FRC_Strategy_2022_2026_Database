"""Integrate the recovered-caption checkpoint without certifying visual review.

Run from this directory with the browser exports in /workspace/scratch, or pass
their directory as argv[1]. Raw captions stay outside the distributable corpus.
"""
from pathlib import Path
import csv, hashlib, json, re, sys
from studies import STUDIES

ROOT=Path(__file__).resolve().parents[2]
EXPORTS=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/workspace/scratch')
DATE='2026-10-25'
def readj(p): return [json.loads(l) for l in (ROOT/p).read_text().splitlines() if l.strip()]
def writej(p,rows): (ROOT/p).write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows))
def writejson(p,obj): (ROOT/p).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def stamp(t): return f'{int(t)//60}:{int(t)%60:02d}'

ledger=readj('data/roboreplay_review_ledger.jsonl')
contexts=[r for r in readj('data/context_documents.jsonl') if r['id'] not in ['roboreplay--Cm-RuiSNlU','roboreplay-Oo5nP00wVBM','einstein-visual-audit-protocol']]
inventory=[]
for v in ledger:
 p=EXPORTS/f'roboreplay-{v["video_id"]}.txt'
 if not p.exists(): continue
 raw=p.read_bytes(); text=raw.decode('utf-8')
 assert f'Video ID: {v["video_id"]}' in text
 rows=[]
 for l in text.splitlines():
  m=re.match(r'\[(\d+):(\d+)\]\s*(.*)',l)
  if m: rows.append({'start_seconds':int(m[1])*60+int(m[2]),'text':m[3]})
 assert rows and all(a['start_seconds']<=b['start_seconds'] for a,b in zip(rows,rows[1:]))
 meta={'video_id':v['video_id'],'url':v['url'],'retrieved_on':DATE,'method':'Normal YouTube watch page / Show transcript / browser transcript export',
  'language':'en','captions':'auto-generated','sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),
  'timestamped_segments':len(rows),'first_caption_start_seconds':rows[0]['start_seconds'],'last_caption_start_seconds':rows[-1]['start_seconds'],
  'duration_boundary':'Last caption start is not media duration. Export does not contain segment durations.',
  'raw_transcript_redistributed':False,'visual_review':False,'new_full_caption_review':v['video_id'] in STUDIES}
 inventory.append(meta)
 v['transcript_status']='downloaded'
 v['latest_access_status']='Recovered through the normal YouTube transcript interface. The current session did not present a CAPTCHA. Video playback remained unavailable in tested match recordings.'
 v['retrieval_record']=meta
 if v['video_id'] not in STUDIES:
  v['review_status']='unreviewed'
  v['reviewed_ranges_seconds']=[]
  v['title']=v['title'].replace('· unreviewed','· transcript recovered; review pending')
  continue
 s=STUDIES[v['video_id']]
 v.update(title=s['title'],title_type='YouTube title observed in normal watch page',published_date=s['published_date'],review_status='full_transcript_review',
  source_summary=s['summary'],transfer_analysis=s['transfer'],reviewed_on=DATE,reviewed_ranges_seconds=[[rows[0]['start_seconds'],rows[-1]['start_seconds']]],visual_review=False)
 sections=[]
 for start,end,title,account,analysis in s['sections']:
  if v['video_id']=='Oo5nP00wVBM' and end==2047: end=2046
  if v['video_id']=='-Cm-RuiSNlU' and end==2778: end=2779
  sections.append({'start_seconds':start,'end_seconds':end,'title':title,'source_account':account,'engineering_or_strategy_analysis':analysis,'url':v['url']+f'&t={start}s'})
 v['navigation_windows']=[{'start_seconds':a['start_seconds'],'end_seconds':a['end_seconds'],'topics':[a['title']],'url':a['url']} for a in sections]
 v['expanded_review']={'sections':sections,'quiz_questions':s['questions'],'remaining_uncertainties':s['uncertainties'],
  'enrichment_scope':'New complete read of every available timestamped caption in the browser export, including non-match intervals. Detailed paraphrase and conditional analysis; no visual footage audit. Timestamp coverage ends at the last caption start, not certified media duration.',
  'visual_review':False,'source_fingerprint':meta['sha256'],'source_caption_segments':len(rows),
  'newly_selected_passages_seconds':[],'full_caption_review_status_inherited':False,
  'expanded_document':f'docs/roboreplay/{v["video_id"]}.md','raw_transcript_redistributed':False,
  'caption_review_start_seconds':rows[0]['start_seconds'],'last_available_caption_start_seconds':rows[-1]['start_seconds']}
 body=f'# {s["title"]}\n\nSource: {v["url"]}\n\nPublished: {s["published_date"]}. Review: {DATE}. Automatic English captions; {len(rows)} timestamped segments. Every exported caption was read. The final caption begins at {stamp(rows[-1]["start_seconds"])}; this is not a video-duration measurement. No raw transcript is redistributed. No visual audit was possible.\n\n{s["summary"]}\n\n{s["transfer"]}\n'
 for a in sections:
  body+=f'\n## {stamp(a["start_seconds"])}–{stamp(a["end_seconds"])} · {a["title"]}\n\n[Source navigation]({a["url"]}). These are commentary-video times, not match-clock times.\n\n### Attributed source account\n\n{a["source_account"]}\n\n### Conditional engineering or strategy interpretation\n\n{a["engineering_or_strategy_analysis"]}\n'
 body+='\n## Questions for verification\n\n'+'\n'.join('- '+q for q in s['questions'])+'\n\n## Remaining uncertainties\n\n'+'\n'.join('- '+q for q in s['uncertainties'])+'\n'
 (ROOT/v['expanded_review']['expanded_document']).write_text(body)
 contexts.append({'id':'roboreplay-'+v['video_id'],'title':s['title'],'year':2026,'robot_id':None,'kind':'roboreplay_deep_study','body':body,'source_urls':[v['url']],'review_scope':v['expanded_review']['enrichment_scope']})
writej('data/roboreplay_review_ledger.jsonl',ledger)
writej('data/transcript_recovery_ledger.jsonl',inventory)

matches=readj('data/einstein_reviews.jsonl')
matchmap={m['key']:m for m in matches}
recovered=matchmap['2022cmptx_sf1m2']
recovered['video_url']='https://www.youtube.com/watch?v=-HI1RpdORwI'
recovered['source_issue']='Prior mirror association was rejected because it showed match 15. A different recording is now verified at the page-metadata level: official FIRST title Einstein 2, red 1619/6672/254 164, blue 3534/5940/6328 122. Footage did not render; no visual review certified.'
recovered['video_identity_verification']={'basis':'Visible official YouTube title, channel and description, matched against the stored roster and scores','date':DATE,'title':'Einstein 2 - 2022 FIRST Championship','channel':'FIRSTRoboticsCompetition','url':recovered['video_url'],'roster_and_final_score_match':True,'visual_match_identity_verified':False}

# Match-specific claims remain explicitly attributed to the commentator.
match_sections={
 '2026cmptx_sf11m1':('-Cm-RuiSNlU',list(range(1,7))),
 '2026cmptx_f1m1':('-Cm-RuiSNlU',[8,9]),
 '2026cmptx_f1m2':('-Cm-RuiSNlU',[10,11,12]),
 '2026cmptx_f1m3':('-Cm-RuiSNlU',[13,14]),
 '2026cmptx_sf3m1':('Oo5nP00wVBM',list(range(1,7))),
 '2026cmptx_sf6m1':('Oo5nP00wVBM',list(range(7,13)))
}
for key,(vid,indices) in match_sections.items():
 m=matchmap[key];v=next(v for v in ledger if v['video_id']==vid)
 m['strategic_notes']=[n for n in m['strategic_notes'] if n.get('research_pass')!='recovered-caption-pass']
 m['commentary_timeline']=[]
 for i in indices:
  s=v['expanded_review']['sections'][i-1]
  m['commentary_timeline'].append({'source_video_id':vid,'source_start_seconds':s['start_seconds'],'source_end_seconds':s['end_seconds'],
   'title':s['title'],'account':s['source_account'],'conditional_analysis':s['engineering_or_strategy_analysis'],
   'source_url':s['url'],'match_clock_alignment':None,'evidence_type':'attributed_commentary_not_visual_observation',
   'independently_visually_verified':False})
  m['strategic_notes'].append({'kind':'broadcast_report','text':s['source_account'],'source_url':s['url'],'source_video_seconds':[s['start_seconds'],s['end_seconds']],'research_pass':'recovered-caption-pass'})
  m['strategic_notes'].append({'kind':'analyst_inference','text':s['engineering_or_strategy_analysis'],'source_url':s['url'],'research_pass':'recovered-caption-pass'})
 m['evidence']=[e for e in m['evidence'] if e.get('research_pass')!='recovered-caption-pass']
 m['evidence'].append({'url':v['url'],'basis':'Complete available-caption review of edited RoboReplay commentary. Specific windows are in commentary_timeline. Not direct visual match observation.','research_pass':'recovered-caption-pass'})
 m['review_status']='Detailed attributed commentary + official phase analysis; visual audit pending'

attempts={
 '2022cmptx_sf1m1':{'tested_video_url':'https://www.youtube.com/watch?v=Tta2G4YpDes','media_duration_seconds_observed':190,'browser_ready_state':0,'decoded_video_width':0,'rendered_match_frames':0,
  'recovery_attempts':['Normal watch-page navigation','One normal reload','Pause and play','Normal player quality set to 360p'],
  'outcome':'Player remained black and buffering at 0:00. No match action observed.'},
 '2022cmptx_sf1m2':{'tested_video_url':'https://www.youtube.com/watch?v=-HI1RpdORwI','media_duration_seconds_observed':191,'rendered_match_frames':0,
  'recovery_attempts':['Normal watch-page navigation','Verified title, creator, roster and scores from visible description'],
  'outcome':'Page-level match identity verified; no rendered match footage observed.'},
 '2026cmptx_f1m3':{'tested_video_url':'https://www.youtube.com/watch?v=2kJRSXaYX04','media_duration_seconds_observed':216,'browser_ready_state':0,'decoded_video_width':0,'rendered_match_frames':0,
  'recovery_attempts':['Normal watch-page navigation','Seek forward using the visible seek control','Documented browser media-download action'],
  'outcome':'Black buffering player; seek did not yield a decoded frame and media download was canceled. No match action observed.'}
}
for key,url,duration in [
 ('2023cmptx_sf1m1','https://www.youtube.com/watch?v=2WFNp-NAz-8',170),
 ('2024cmptx_sf1m1','https://www.youtube.com/watch?v=KVctfYIb47I',185),
 ('2025cmptx_sf1m1','https://www.youtube.com/watch?v=TuWMGQ74kNI',191)]:
 attempts[key]={'tested_video_url':url,'media_duration_seconds_observed':duration,'browser_ready_state':0,'decoded_video_width':0,'rendered_match_frames':0,'recovery_attempts':['Normal watch-page navigation','Playback state and fresh screenshot inspected after loading'],'outcome':'Player remained black and buffering at 0:00 with playback requested and no decoded video frame. No match action observed.'}
auditrows=[]
for m in matches:
 a={'match_key':m['key'],'year':m['year'],'canonical_video_url':m.get('video_url'),'review_status':'blocked_before_footage' if m['key'] in attempts else 'pending_not_attempted_this_pass',
  'complete':False,'visual_review':False,'review_date':DATE if m['key'] in attempts else None,
  'observed_intervals_video_seconds':[],'match_clock_alignment':None,'observed_events':[],'robot_role_intervals':[],
  'blind_intervals':'All match action; no decoded footage inspected in this pass.',
  'completion_boundary':'Empty event lists mean unreviewed, not no events. Captions, thumbnails and official scores do not satisfy visual review.',
  'access_attempt':attempts.get(m['key']),
  'required_checks':['Confirm actual recording against roster, scores and bracket position','Establish video-to-match-clock alignment','Inspect full autonomous, teleop and endgame','Follow each of six robots across changing roles and health','Mark camera cuts and occlusion','Separate observable behavior, commentary, intent and causal inference','Check claims against official score components','List remaining ambiguities and obtain alternate angles where needed'],
  'replay_attempt_inventory_verified':False}
 m['visual_audit']=a;m['video_reviewed']=False;m['tactical_review_complete']=False
 auditrows.append(a)
writej('data/einstein_visual_audit.jsonl',auditrows)
writej('data/einstein_reviews.jsonl',matches)

protocol='''# Einstein visual-audit protocol and current checkpoint

## What this edition actually establishes

The corpus contains 80 canonical Einstein match records across 2022–2026: 18, 15, 15, 16 and 16 respectively. All 80 have a candidate recording link after recovery of the official 2022 match-2 page. A canonical TBA match row is not a verified inventory of every played/replayed attempt or every camera angle. That additional completeness check remains open.

Zero visual match audits are complete. Six recording pages were opened for access/identity checks; the rest were not individually tested in this pass. Representative recordings from all five seasons supplied metadata but no decoded match frame, remaining black and buffering. Normal reload, playback controls, a lower quality on the 2022 player, seeking on the 2026 player and documented media export did not produce footage. The failure is specific to these tested sessions; it does not prove all videos are unavailable or identify a network cause. It was not a visible bot challenge in this session.

The user authorized solving the prior CAPTCHA. On opening the normal watch page there was no CAPTCHA to solve. The transcript interface worked. All eleven previously pending exports were recovered. Two new available-caption reads cover six canonical 2026 matches, with detailed attributed accounts and conditional analysis. Nine recovered exports still await full content review. The prior 33 caption studies retain their inherited review scope. Nothing in this checkpoint is represented as permanent internal model memory or as visual watching.

## Identity before tactics

Compare the title, year, teams, alliance colors, bracket position and final score. A similar title or a mirror association is insufficient. The rejected 2022 match-2 link previously pointed to match 15. The replacement is the official FIRST recording titled “Einstein 2 - 2022 FIRST Championship”; its visible description exactly matches red 1619/6672/254 scoring 164 and blue 3534/5940/6328 scoring 122. This establishes page identity, not independent visual identity. Keep that distinction if the video is mislabeled or contains a replay later in the file.

For each recording, preserve its exact URL, creator, available duration and any alternate-angle relation. Record whether a replay is the final scored attempt or an abandoned/no-score attempt. Do not silently overwrite the original evidence when substituting a better angle. In 2022 the semifinal stage is round-robin-style Einstein play; later double-elimination set/match keys use different conventions. Do not infer bracket order by sorting all seasons with the same filename heuristic.

## A continuous first pass plus six robot-follow passes

View the full match from prestart through the final action at a speed that preserves the interactions being asserted. Establish where autonomous starts, teleop starts and the match ends in the source video. Link every event to both source time and the visible match clock when available. For edited analysis with pauses, rewinds or slow motion, use a piecewise mapping rather than assuming source seconds equal elapsed match seconds. A caption timestamp is a navigation pointer until aligned visually.

Then follow each of the six robots through the full sequence. Record acquisition source, held inventory only when countable, scoring location and configuration, crossing choice, passing destination, screen/defense target and changes of job. For 2026, identify the actual hub state and the robot’s preparation for its next active window. For 2025, record concurrent L1, algae and branch work rather than imposing a serial “finish high branches, then do L1” story. For earlier seasons, preserve their own field geometry, scoring constraints and endgame incentives; do not import the 2026 supply model automatically.

A role is an interval, not a permanent label for a team or a robot. The same robot can score, pass, screen, steal, defend and recover in one match. A stopped robot can affect a route while providing no intended defensive action. A robot with a loaded hopper can influence supply without scoring. A defender may change targets to protect a crossing instead of following its original mark. Keep those possibilities distinguishable in the log.

## What an individual event needs

Store event ID, match key, recording ID, source start/end, match-clock start/end, actors, current configuration, field location, directly visible action, visible outcome, uncertainty and evidence links. Distinguish “robot contacts opponent,” “opponent changes route,” “shots fall short” and “robot stops moving.” Those observations do not by themselves mean “intentional pick,” “successful defense worth one hopper,” “battery sag” or “radio failure.” Put those interpretations in separate fields with their supporting or missing evidence.

For a screen or defensive handoff, observe all participants before and after the interaction. A five-second delay may save another defender’s travel, but it may also cost the screening scorer an equally valuable cycle. Track the alternative route actually available and the time remaining in the scoring window. Do not turn a rough hopper capacity into denied points. For a steal, distinguish fuel removed from an opponent’s reserve, fuel retained, fuel passed, fuel later scored and fuel lost back to the opponent. Avoid counting a transfer twice.

Leave unknown counts null. An empty event list means footage unreviewed, not that the match contained no relevant event. A camera cut creates a blind interval even if broadcast commentary continues. Multiple robots near a pile do not reveal their exact pickup share. Hub counts cannot generally assign individual scoring when streams overlap. Use the official score only at its actual alliance/phase resolution.

## Geometry and failures need more than a plausible story

Record the deployed envelope as seen at the interaction: extension can change a trench-capable robot into a bump-only robot. When a defender constrains rotation, identify the bumper contact and nearby hub, trench bar, wall or bump separately. Do not infer exact clearance, mass, traction, moment of inertia or motor current from a camera image. A rounded perimeter changes the contact problem but cannot guarantee escape under every friction and obstacle condition.

For an operational interruption, mark the last unambiguous functioning action, the first abnormal action, any recovery, and which capabilities remain. “Collects but shoots short” differs from “entire robot dead.” A mechanism appearing damaged is not a diagnosis of root cause. Electrical logs, operator testimony or a technical publication may explain a symptom later; preserve the chronology and attribution of that new explanation. Do not label an unobserved problem a brownout because the score dropped.

## Reconcile with official components without inventing individual output

Keep final score, clean score, penalties received and each relevant official phase or component. Reconcile arithmetic and identify which alliance had each active shift. Own first/second active-shift totals in 2026 occur at different wall-clock times for opponents. The final-period fuel component is not climb output. The stored 2026 finals all record zero tower points for both alliances; fuel and access remain the useful questions in this series.

For 2026 match 3, official auto fuel is 188–118; post-auto fuel is 529–509; final is 717–632 because Milstein receives five penalty points. The commentator’s post-auto numbers are alliance quantities. For match 6, clean output is 678–691 and final is 688–691, with ten penalty points received by Milstein. A three-point final is not a three-point clean result. Preserve this distinction in quizzes and causal explanations.

In the upper-bracket final, Daly wins auto 186–83 and transition 65–30 but does not win every subsequent fuel component. In finals 2 it does lead every recorded fuel component, with the final period only 169–165. In finals 3 the own active-shift totals are 311–79, while final-period fuel is 154–161. Those patterns guide what footage to investigate; they cannot identify how many fuel a defender individually denied.

## Completion and verification

Do not set complete=true until full interval coverage, all-six-robot follow checks, identity and clock alignment, camera blind spots, score reconciliation and explicit unresolved claims are present. It is acceptable for a completed viewing to leave a particular action unresolved because it is occluded. That uncertainty must remain visible; viewing completion is not omniscience. A user correction should identify the event/claim, the better source or timestamp, the revised interpretation and which downstream design conclusions need reconsideration.

The intended next step is playable match footage or an authorized usable video source. Until it exists, the six expanded 2026 narratives remain commentary evidence, and all eighty visual records remain pending. The JSONL ledger is the durable queue; it is not a certification of work that could not be performed.
'''
(ROOT/'docs/EINSTEIN_VISUAL_AUDIT.md').write_text(protocol)
contexts.append({'id':'einstein-visual-audit-protocol','title':'Einstein visual-audit protocol and current checkpoint','year':None,'robot_id':None,'kind':'audit_method','body':protocol,'source_urls':[]})
writej('data/context_documents.jsonl',contexts)

# Keep all public views and exact normalized table exports in sync.
payload=json.loads((ROOT/'data/reader_payload.json').read_text());payload.update(einstein=matches,videoReviews=ledger,contextDocs=contexts)
audit=json.loads((ROOT/'data/audit.json').read_text())
audit.update(edition='Recovered transcripts and detailed 2026 Einstein commentary checkpoint',
 roboreplay_full_transcript_reviews=sum(v['review_status']=='full_transcript_review' for v in ledger),
 roboreplay_pending=sum(v['review_status']!='full_transcript_review' for v in ledger),
 roboreplay_pending_retrieval=sum(v['transcript_status']!='downloaded' for v in ledger),
 recovered_transcripts_this_pass=len(inventory),expanded_video_reviews=sum(bool(v.get('expanded_review')) for v in ledger),
 expanded_video_sections=sum(len(v.get('expanded_review',{}).get('sections',[])) for v in ledger),
 einstein_with_reported_tactics=sum(any(n['kind'] in ['broadcast_report','team_report'] for n in m['strategic_notes']) for m in matches),
 einstein_recording_links=sum(bool(m.get('video_url')) for m in matches),einstein_visual_reviews=0,
 einstein_recording_pages_tested_this_pass=len(attempts),context_documents=len(contexts),
 context_words=sum(len(re.findall(r'\b\w+\b',c['body'])) for c in contexts),agent_typed_claims=1256)
prompts=[]
for v in ledger:
 for i,q in enumerate(v.get('expanded_review',{}).get('quiz_questions',[]),1):
  prompts.append({'id':v['video_id']+':quiz:'+str(i),'video_id':v['video_id'],'season':v.get('season'),'question':q,'study':v['expanded_review']['expanded_document'],
   'answer_evidence':'Read the full study and cited source windows; distinguish source account, inference and unresolved evidence.','visual_evidence_required_for_match_observation':True})
audit['video_quiz_prompts']=len(prompts)
writej('data/roboreplay_quiz_prompts.jsonl',prompts)
writejson('data/audit.json',audit);payload['audit']=audit;writejson('data/reader_payload.json',payload)
writej('tables/einstein_reviews.jsonl',[{'key':m['key'],'year':m['year'],'review_status':m['review_status'],'video_reviewed':0,'tactical_review_complete':0,'data_json':json.dumps(m,ensure_ascii=False,separators=(',',':'))} for m in matches])
writej('tables/video_reviews.jsonl',[{'video_id':v['video_id'],'url':v['url'],'title':v['title'],'season':v.get('season'),'discovery_url':v.get('discovery_url'),'source_post_date':v.get('source_post_date'),'published_date':v.get('published_date'),
 'transcript_status':v['transcript_status'],'review_status':v['review_status'],'source_summary':v['source_summary'],'transfer_analysis':v['transfer_analysis'],
 'reviewed_ranges_json':json.dumps(v.get('reviewed_ranges_seconds',[])),'visual_review':0,'metadata_json':json.dumps(v,ensure_ascii=False)} for v in ledger])
writej('tables/context_documents.jsonl',[{'id':c['id'],'title':c['title'],'year':c.get('year'),'robot_id':c.get('robot_id'),'kind':c['kind'],'body_markdown':c['body'],'source_urls_json':json.dumps(c.get('source_urls',[]),ensure_ascii=False)} for c in contexts])
for file,rows in [('data/einstein.csv',matches),('data/roboreplay_review_ledger.csv',ledger)]:
 with (ROOT/file).open() as f: fields=next(csv.reader(f))
 with (ROOT/file).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader()
  for row in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()})
writejson('data/video_access_audit.json',{'date':DATE,'prior_block':'Prior session presented a Google unusual-traffic CAPTCHA. User explicitly approved an attempt.','current_captcha_status':'No CAPTCHA presented in current normal watch-page session; no CAPTCHA solved or bypassed.',
 'transcript_access':'All eleven previously pending videos exported through normal YouTube transcript UI. Opening Show transcript and allowing panel content to load resolved initial export-unavailable responses.',
 'recovered_inventory':'data/transcript_recovery_ledger.jsonl','new_full_caption_reviews':list(STUDIES),'recovered_awaiting_full_review':[r['video_id'] for r in inventory if not r['new_full_caption_review']],
 'visual_access':'Tested players remained black/buffering; no decoded match frames inspected. Documented media download attempts were canceled.',
 'visual_attempts':attempts,'site_bot_block_observed_this_session':False,'network_cause_diagnosed':False,'channel_inventory_complete':False,
 'additional_discovery_candidates':[{'video_id':'qjj32YCsh3U','title':'How 1690 used Defense AGAIN to take down 254 | FRC Strategy Analysis','creator':'RoboReplay','basis':'Visible recommendation on the recovered Einstein-analysis page','content_reviewed':False},
 {'video_id':'JoeJ1bhKlm0','title':'How to beat 254 at Their HOME EVENT! | FRC Strategy Analysis','creator':'RoboReplay','basis':'Visible recommendation on the recovered Einstein-analysis page','content_reviewed':False}],
 'scope':'Current recovered set is the eleven pending items from the prior 44-video ledger, not an exhaustive channel certification. Newly noticed candidates require inventory and review.'})
writejson('RESEARCH7_SUMMARY.json',{'date':DATE,'new_transcripts_recovered':len(inventory),'new_complete_available_caption_reads':len(STUDIES),'new_detailed_video_sections':sum(len(s['sections']) for s in STUDIES.values()),
 'new_detailed_commentary_matches':list(match_sections),'new_study_words':sum(len((ROOT/f'docs/roboreplay/{vid}.md').read_text().split()) for vid in STUDIES),
 'recovered_awaiting_full_read':audit['roboreplay_pending'],'prior_caption_reviews':33,'total_caption_reviews':audit['roboreplay_full_transcript_reviews'],
 'canonical_einstein_matches':80,'candidate_recording_links':80,'visual_audits_completed':0,'visual_recording_pages_tested':len(attempts),
 'channel_inventory_complete':False,'all_replay_attempts_inventoried':False,'robot_dossiers':125,'technical_notes':227,'embedded_images':504})
print(json.dumps(json.loads((ROOT/'RESEARCH7_SUMMARY.json').read_text()),indent=2))
