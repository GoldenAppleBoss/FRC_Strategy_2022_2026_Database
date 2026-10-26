from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[2]
def readj(p):return [json.loads(l) for l in (ROOT/p).read_text().splitlines() if l.strip()]
def writej(p,rows):(ROOT/p).write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows))
def wj(p,obj):(ROOT/p).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

old='All 33 accessible RoboReplay records have expanded studies: 105 sections and 100 quiz questions, with attributed source accounts, conditional analysis and unresolved details. The written video studies total about 14,000 words, with more space allocated to the season recap. The new enrichment revisits selected timestamped passages over the inherited full-caption reviews; it is not a second complete rewatch or a visual audit. Eleven pending videos remain unreviewed. Normal YouTube browser access encountered an unusual-traffic verification challenge. No bypass was attempted and no creator-published transcript archive was located.'
new='The current checkpoint recovers all eleven previously pending transcripts through the normal YouTube transcript interface. No CAPTCHA appeared in this session. The 44-video ledger now has 35 complete available-caption reviews: 33 inherited reviews with selected-passage enrichment, plus two new complete caption reads. Those two studies add 27 sections and about 6,900 written words covering six 2026 Einstein matches. Nine recovered transcripts still await full content review. Across all 35 studies there are 132 sections and 114 quiz prompts. Full channel enumeration remains unverified. Tested match players stayed black and buffering, so zero visual Einstein audits are complete. Read `docs/EINSTEIN_VISUAL_AUDIT.md` and `data/einstein_visual_audit.jsonl` before using a match account as observation.'
paths=['README.md','AGENTS.md','docs/AGENT_GUIDE.md','docs/context/AGENT_CONTEXT.md','agent/README.md']
replacements={}
for path in paths:
 p=ROOT/path;s=p.read_text();before=s
 s=s.replace(old,new).replace('Fifty-one Einstein records have reviewed reported tactics','Fifty-four Einstein records have reviewed reported tactics').replace('Fifty-seven Einstein records have reviewed reported tactics','Fifty-four Einstein records have reviewed reported tactics').replace('of which 51 have reviewed reported tactics','of which 54 have reviewed reported tactics').replace('of which 57 have reviewed reported tactics','of which 54 have reviewed reported tactics')
 s=s.replace('RoboReplay: **33 full available transcript reviews**, 44 discovered videos, 11 pending after access was blocked.','RoboReplay: **35 full available transcript reviews** among the prior 44-video inventory; all eleven previously pending transcripts recovered, nine of those awaiting full content review.')
 s=s.replace('RoboReplay coverage remains 33 available full-caption reviews among 44 discovered videos, with 11 pending and complete channel enumeration unverified. No visual watching is claimed.','RoboReplay coverage is 35 available full-caption reviews among the prior 44-video inventory. All eleven previously pending exports were recovered; nine still await full review. Full channel enumeration is unverified. No visual watching is claimed.')
 s=s.replace('RoboReplay state is unchanged: 44 discovered videos, 33 full available caption reviews, 11 pending, full channel inventory unverified. No new transcript access or visual watching occurred in this technical-binder pass. Keep previous review ledgers and pending access limits.','RoboReplay state: all eleven previously pending exports recovered; 35 complete available-caption reviews in the prior 44-video ledger, with nine recovered exports awaiting full review. The two new studies cover six 2026 Einstein matches in detail. Full channel inventory is unverified, with additional discovery candidates recorded in data/video_access_audit.json. Tested match footage did not render, so no visual audit is complete. Keep source commentary distinct from direct observation.')
 p.write_text(s);replacements[before]=s

p=ROOT/'docs/roboreplay/README.md';s=p.read_text();before=s
s=s.replace('33 previously available caption reviews now have 105 authored sections and explicit limits. The 11 pending videos remain unreviewed because normal access encountered a verification challenge. New enrichment uses selected passages, not a new complete visual watch. Full raw transcripts are not redistributed.',new)
for vid in ['-Cm-RuiSNlU','Oo5nP00wVBM']:
 if f']({vid}.md)' not in s:s+='\n- ['+('2026 upper-bracket final and finals 1–3: supply control, defense and failures' if vid.startswith('-') else '2026 Einstein matches 3 and 6: crossing geometry, steals and rounded bumpers')+f']({vid}.md)'
s+='\n';p.write_text(s);replacements[before]=s
p=ROOT/'docs/context/NEXT_RESEARCH_QUEUE.md';before=p.read_text()
s='''# Current research queue

The 125 robot-year sample, 227 technical notes, 27 publication-review robot-years and 98 focused studies remain unchanged. Complete mechanism/version histories, remaining binder discovery, CAD interpretation and exact event installations remain open.

## Recovered transcript queue

All eleven pending exports from the prior 44-video inventory were recovered through normal YouTube access. Full available-caption reads and long studies were completed for -Cm-RuiSNlU and Oo5nP00wVBM. The other nine exports are recovered but not reviewed: MVBEPikDEGY, UByANktu2ck, RKWm1abo8hk, BT2P26TOLwo, lA4LkvZ8vNk, 0H69SR-ylZg, LPALB1UmPhY, fHAHlAcGqoA and zVLcKw8r4Q0. Do not summarize their content from the title or convert retrieval into review. The access procedure is recorded in data/video_access_audit.json; export fingerprints and coverage endpoints are in data/transcript_recovery_ledger.jsonl.

The channel remains incompletely enumerated. Two further creator videos were noticed in recommendations, qjj32YCsh3U and JoeJ1bhKlm0, and are recorded as unreviewed discovery candidates in the access audit. Inventory and review them rather than certifying all-channel coverage from the earlier 44-video set.

## Einstein visual audit

The user explicitly requests every match’s visual audit. All 80 canonical records now have candidate links. Zero visual audits are complete. Six pages were inspected for access/identity. Representative recordings from all five seasons remained black with no decoded footage; normal recovery on the 2022/2026 tests did not resolve it and media export failed. Other recordings were not individually tested. No CAPTCHA appeared in this session, so none was solved. Do not infer a universal site failure or diagnose the network cause.

The next dependent step needs playable footage. Follow docs/EINSTEIN_VISUAL_AUDIT.md and data/einstein_visual_audit.jsonl: verify recording identity, align clocks, view the full action, follow six changing robot roles, mark camera blind intervals, reconcile official phase scores and preserve causal uncertainty. Inventory any replayed attempts and alternate angles separately from canonical TBA match rows. Current long narratives for 2026 matches 3, 6, 11 and finals 1–3 are attributed commentary, not visual observation.

## Agent verification

Quiz against the complete written studies. Record the source window for each answer, distinguish construction from role and observed behavior from inferred intent, and leave unresolved counts null. A wrong answer should produce a specific claim correction and a downstream reasoning review. Do not promote a plausible engineering explanation into a team-stated reason. Verify rule-dependent statements against the dated official manual.
'''
p.write_text(s);replacements[before]=s

p=ROOT/'docs/game_2026.md';before=p.read_text();s=before
s=s.replace('The available RoboReplay caption review reaches the week-2 viewer analysis; later 2026 video announcements are inventoried but their transcripts were blocked. Therefore this is not a RoboReplay-backed account of every late-season match. The existing Einstein ledger remains explicit about reported tactics and absent visual audits.','The earlier checkpoint reached the week-2 viewer analysis. The current checkpoint adds complete available-caption reads of the upper-bracket final, finals 1–3 and Einstein matches 3 and 6. Nine more late-season exports have been recovered but are not yet reviewed. This is still not a visual audit or an account of every late-season match. The detailed source accounts and uncertainties are in docs/roboreplay/-Cm-RuiSNlU.md and docs/roboreplay/Oo5nP00wVBM.md.')
extra='''

## Six late-season match accounts: architecture changes the next supply state

The recovered [May finals analysis](https://www.youtube.com/watch?v=-Cm-RuiSNlU) and [August retrospective](https://www.youtube.com/watch?v=Oo5nP00wVBM) provide a more detailed account of the fuel-control problem. Both sources were read through their complete available captions. The match players did not render, so the actions below remain the commentator’s account. The distinction matters: a creator can accurately describe a movement while speculating about its intent or the cause of a failure. The long studies retain those separate layers and timestamp every explanation.

In the upper-bracket Daly–Newton meeting, the source connects 1323’s angled autonomous entry, 2910’s disrupted route, 4065’s midfield endpoint and the dual moving cleanup of 1323/4414. Its central argument is a chain: early possession changes neutral-zone availability; scarcity forces an opponent to collect in a less convenient location; that departure location makes its next steal later; the delay gives the prepared scorer more uncontested time. The chain is useful as an audit hypothesis. It is not established by one score difference and does not mean every link was deliberately planned. The official table also records Newton winning its second own active shift and final-period fuel; do not rewrite Daly’s overall win as winning every window.

The first final offers a different state. The source reports 1323’s interruption and praises 4414 for collecting through the transition instead of matching immediate scoring. Daly’s recorded transition fuel is zero against Newton’s 57. The purpose in the creator’s account is to change the next supply state, not to score in that interval. Whether that choice would win with six healthy robots remains a counterfactual. The relevant architecture question is whether a robot can preserve enough inventory and route flexibility to turn deferred scoring into useful output before its next window ends.

The second final adds a defensive geometry account. The source describes 4065 keeping 2910 near a bump, hub and trench bar where the deployed collector limits rotations, then using a blocker even after a crossing succeeds. Newton also changes tactics: a successful early fuel contest, a delayed 4414 escape, holding fuel out of the shared pool and passing instead of taking another heavily defended cycle. The creator considers some of those adaptations valuable even though Newton loses. The audit must measure opportunity cost and actual outcomes before turning them into a universal policy. A pin described as worth its penalties is a commentary judgment, not permission to ignore the governing rules.

The third final changes autonomous matchups and includes reported 2046 shooting trouble and 868 damage. Those failure states prevent treating the 306-point result as a pure turret-versus-drum experiment. Official own-active-shift fuel totals are 311–79, while final-period fuel is 154–161 and tower points are zero for both sides. The source’s account directs attention to access, supply, blocked approaches and operational symptoms. It cannot diagnose current draw, voltage sag or the exact fuel denied by a defender.

The August examples add a configuration-specific mobility distinction. A robot may be trench-capable when compact but bump-only with an extended hopper. A steal can be attractive on the way in yet poor if the exit crosses a defended bottleneck after the hopper expands. The source describes 254 briefly giving up its own scoring to let 8613 reach 2481’s return, and 6324 sacrificing its next collection to delay a loaded 1678. Those are partner timing trades, not evidence that scorers should generically stop scoring to defend. The same account highlights 4946’s curved bumper perimeter as an escape hypothesis and 6324’s picks as changing the defender’s problem. Exact geometry, friction and intent remain unverified.

Finally, the retrospective argues that losing autonomous narrowly may improve later opportunities. That does not erase the earlier example of Daly compounding an auto win. The conditions differ: who retains the neutral zone, who can stage fuel, how loaded robots cross and whether the next scorer has to search. The agent should model both possible autonomous outcomes and the resulting inventories and routes. It should not optimize toward deliberately losing auto from one close match, or optimize toward winning auto while ignoring the terminal positions that determine the next minute.
'''
if '## Six late-season match accounts: architecture changes the next supply state' not in s:s+=extra
p.write_text(s);replacements[before]=s

contexts=readj('data/context_documents.jsonl')
for c in contexts:c['body']=replacements.get(c['body'],c['body'])
writej('data/context_documents.jsonl',contexts)
writej('tables/context_documents.jsonl',[{'id':c['id'],'title':c['title'],'year':c.get('year'),'robot_id':c.get('robot_id'),'kind':c['kind'],'body_markdown':c['body'],'source_urls_json':json.dumps(c.get('source_urls',[]),ensure_ascii=False)} for c in contexts])
payload=json.loads((ROOT/'data/reader_payload.json').read_text());payload['contextDocs']=contexts
for g in payload['games']:
 if g['year']==2026:g['analysis']=(ROOT/'docs/game_2026.md').read_text()
audit=json.loads((ROOT/'data/audit.json').read_text());audit['context_words']=sum(len(re.findall(r'\b\w+\b',c['body'])) for c in contexts)
audit['roboreplay_reviewed_caption_hours']=round(14.12+(2779+2046)/3600,2)
payload['audit']=audit;wj('data/audit.json',audit);wj('data/reader_payload.json',payload)
# The normalized season chapter follows the same current text.
rows=readj('tables/seasons.jsonl')
for r in rows:
 if r['year']==2026:
  for k in list(r):
   if isinstance(r[k],str) and r[k].startswith('# 2026'):r[k]=(ROOT/'docs/game_2026.md').read_text()
writej('tables/seasons.jsonl',rows)
print('Updated entry-point scope, next queue, chapter and contextual mirrors.')
