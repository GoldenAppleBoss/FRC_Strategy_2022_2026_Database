const fs=require('fs'),vm=require('vm'),assert=require('assert');
const root=require('path').resolve(__dirname,'..')+'/';
const html=fs.readFileSync(root+'index.html','utf8'),payload=html.match(/<script id="database" type="application\/json">([\s\S]*?)<\/script>/)[1];
const script=html.match(/<script>\s*'use strict';([\s\S]*?)<\/script>/)[1];
const assets=html.match(/<script id="image-assets" type="application\/json">([\s\S]*?)<\/script>/)[1];
const els=new Map();function el(s){if(!els.has(s))els.set(s,{innerHTML:'',textContent:'',value:'',dataset:{}});return els.get(s)}
const context={document:{getElementById:id=>id==='database'?{textContent:payload}:id==='image-assets'?{textContent:assets}:el('#'+id),querySelector:el,querySelectorAll:()=>[],addEventListener:()=>{}},window:{scrollTo:()=>{},addEventListener:()=>{}},location:{hash:''},URLSearchParams,console};vm.createContext(context);
vm.runInContext(script,context);let count=0;
function run(code){vm.runInContext('{'+code+'}',context);count++}
run("if(!document.querySelector('#tabs').innerHTML.includes('Binders &amp; mechanics')&&!document.querySelector('#tabs').innerHTML.includes('Binders & mechanics'))throw Error('binder tab missing')");
run("if(DB.robots.length!==141||DB.technicalNotes.length!==303)throw Error('counts')");
run("DB.robots.forEach(a=>{const h=robotDetail(a);if(!h.includes(String(a.team)))throw Error('robot detail')})");
run("DB.robots.forEach(a=>{const h=binderDetail(a);if(!h.includes(a.binder_audit.status.replaceAll('_',' ')))throw Error('binder detail')})");
run("state.year='';state.query='';binders();if(!document.querySelector('#binder-count').textContent.startsWith('141 '))throw Error('all binder audits')");
run("state.binderStatus='reviewed';binderList();if(!document.querySelector('#binder-count').textContent.startsWith('40 '))throw Error('reviewed filter')");
run("state.binderStatus='pending';binderList();if(!document.querySelector('#binder-count').textContent.startsWith('101 '))throw Error('pending filter')");
run("state.binderStatus='';state.query='slapdown';binderList();if(document.querySelector('#binder-count').textContent.startsWith('0 '))throw Error('technical search')");
run("state.query='a-query-that-does-not-exist-0918273';binderList();if(!document.querySelector('#binder-count').textContent.startsWith('0 '))throw Error('no results')");
run("const p=binderDetail(DB.robots.find(a=>a.id==='2026-2910'));if(!p.includes('Original BLITZ')||!p.includes('RE-BLITZ')||!p.includes('Engineering analysis'))throw Error('version and evidence')");
run("const p=binderDetail(DB.robots.find(a=>a.id==='2025-1323'));if(!p.includes('Team explanation')||!p.includes('L1'))throw Error('primary L1 reasoning')");
run("const p=binderDetail(DB.robots.find(a=>a.id==='2024-2910'));if(!p.includes('owner has disabled'))throw Error('download limit')");
run("state.query='';state.year='2026';state.binderStatus='';robots();robotList()");
run("DB.games.forEach(g=>{state.game=g.year;games()})");
run("['pch','champs_div','einstein'].forEach(t=>{state.benchType=t;bench()});DB.benchmarks.forEach(eventDetail)");
run("DB.einstein.forEach(matchDetail);einstein();matchList()");
run("context();DB.contextDocs.forEach(d=>markdown(d.body))");
run("replay();DB.videoReviews.forEach(expandedReplayDetail)");
run("sources();sourceList();auditWithExpansion()");
run("if(DB.videoReviews.filter(v=>v.expanded_review).length!==35)throw Error('expanded review count');const h=expandedReplayDetail(DB.videoReviews.find(v=>v.video_id==='1UsbJD-zRjU'));if(!h.includes('Quiz prompts')||!h.includes('Source account')&&!h.includes('source account'))throw Error('expanded study missing')");
run("agent();if(!document.querySelector('#view').innerHTML.includes('Agent entry point'))throw Error('agent view')");
run("if(Object.keys(IMAGE_ASSETS).length!==569)throw Error('embedded image count');Object.values(IMAGE_BY_ID).forEach(im=>{if(!imageSrc(im).startsWith('data:image/'))throw Error('external image dependency')})");
run("const im=Object.values(IMAGE_BY_ID)[0];const s=markdown('![test](../../'+im.path+')','docs/technical/test.md');if(!s.includes('data:image/')||s.includes('![test]'))throw Error('markdown image')");
run("if(!markdown('[Guide](../AGENTS.md)','docs/AGENT_GUIDE.md').includes('href=\"AGENTS.md\"'))throw Error('relative link')");
run("if(inlineWithImages('[x](javascript:alert)').includes('href='))throw Error('unsafe scheme')");
run("const r=DB.robots.find(a=>a.id==='2026-2910');if(!robotSearchText(r).includes('0.6-inch plates'))throw Error('technical construction missing from robot search')");
run("if(DB.videoReviews.filter(v=>v.transcript_status==='downloaded').length!==44||DB.videoReviews.filter(v=>v.review_status==='unreviewed').length!==9)throw Error('recovery scope')");
run("if(DB.einstein.filter(m=>m.visual_audit).length!==80||DB.einstein.some(m=>m.video_reviewed||m.visual_audit.complete))throw Error('visual scope')");
run("const m=DB.einstein.find(m=>m.key==='2026cmptx_f1m2');const h=matchDetail(m);if(!h.includes('Detailed attributed commentary')||!h.includes('Conditional interpretation')||!h.includes('Visual audit checkpoint'))throw Error('match timeline render')");
run("const v=DB.videoReviews.find(v=>v.video_id==='-Cm-RuiSNlU');if(v.expanded_review.sections.length!==14||!v.navigation_windows.every(w=>w.url))throw Error('new study navigation')");

run("agent();if(!document.querySelector('#view').innerHTML.includes('No support-only architecture')||DB.agentManifest.team_constraints.turret_allowed!==false)throw Error('1833 mandate absent')");

run("if(!years().includes('2018')||!years().includes('2019'))throw Error('historical year filters');state.year='2018';state.query='';state.binderStatus='';binders();if(!document.querySelector('#binder-count').textContent.startsWith('7 '))throw Error('2018 filtered cohort');const h=robotDetail(DB.robots.find(r=>r.id==='2019-1323'));if(h.includes('#null')||!h.includes('unretrieved'))throw Error('null EPA presentation')");

// summary follows all checks
console.log('PASS' ,count,'reader logic checks; all 141 robot and binder details generated. Browser layout not tested.');
fs.writeFileSync(require('path').join(root,'READER_VALIDATION.json'),JSON.stringify({checks:count,status:'passed',all_robot_details:141,all_binder_audits:141,browser_layout:false},null,2));
