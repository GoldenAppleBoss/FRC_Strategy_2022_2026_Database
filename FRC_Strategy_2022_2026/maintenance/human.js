// The reader starts in the design workspace. Detailed research has its own entry point.
WB.mode = 'human';
WB.libraryView = 'robots';
WB.benchmarkPage = 0;
WB.eventType = '';
WB.eventWeek = '';
WB.eventQuery = '';
WB.benchmarkYear = '';
WB.lessonYear = '';
WB.lessonQuery = '';
WB.lessonPage = 0;
state.year = '';
state.robot = '';
const dossierReviews = Object.fromEntries((DB.dossierReviews || []).map(r => [r.robot_id, r]));

function asText(value) {
  if (value == null) return '';
  if (Array.isArray(value)) return value.map(asText).join('\n\n');
  if (typeof value === 'object') return Object.entries(value).map(([k,v]) => k.replaceAll('_',' ') + ': ' + asText(v)).join('\n\n');
  return String(value);
}
function prose(value) {
  return asText(value).split(/\n\n/).filter(Boolean).map(t => `<p>${esc(t)}</p>`).join('');
}
function bullets(value) {
  if (!value || !value.length) return '';
  return '<ul>' + (Array.isArray(value) ? value : [value]).map(v => `<li>${esc(asText(v))}</li>`).join('') + '</ul>';
}
function audience(mode) {
  WB.mode = mode;
  tab(mode === 'agent' ? 'agent' : 'home');
}
function librarySection(name) {
  WB.libraryView = name;
  tab({robots:'robots',lessons:'architectures',benchmarks:'bench'}[name]);
}
tabs = function() {
  const human = [['home','Start here'],['robots','Robot library'],['create','Create recommendation'],['runs','Your recommendations']];
  const agent = [['agent','Agent entry point'],['robots','Robot library'],['architectures','Architecture studies'],['bench','Benchmarks'],['games','Game & meta'],['context','Context documents'],['replay','Video research'],['einstein','Match records'],['sources','Sources'],['audit','Coverage & methods']];
  const active = WB.mode === 'human' && ['architectures','bench'].includes(state.tab) ? 'robots' : state.tab;
  const modes = ['human','agent'].map(m => `<button class="${WB.mode===m?'active':''}" aria-pressed="${WB.mode===m}" onclick="audience('${m}')">${m==='human'?'For people':'For agents'}</button>`).join('');
  const links = (WB.mode === 'human' ? human : agent).map(([k,label]) => `<button class="${k===active?'active':''}" onclick="tab('${k}')" ${k===active?'aria-current="page"':''}><span class="nav-icon">${icon(k)}</span><span class="nav-text">${label}</span></button>`).join('');
  $('#tabs').innerHTML = `<div class="entry-switch">${modes}</div><div class="nav-label">${WB.mode==='human'?'DESIGN WORKSPACE':'RESEARCH INTERFACE'}</div>${links}`;
};
const renderWorkspace = render;
render = function() {
  if (state.tab === 'binders') state.tab = 'robots';
  renderWorkspace();
  if (WB.mode === 'human' && ['robots','architectures','bench'].includes(state.tab)) {
    const nav = [['robots','Robot dossiers'],['architectures','Design lessons'],['bench','Performance benchmarks']];
    $('#view').insertAdjacentHTML('afterbegin', '<div class="library-nav">' + nav.map(([k,l]) => `<button class="btn ${state.tab===k?'teal':''}" onclick="tab('${k}')">${l}</button>`).join('') + '</div>');
  }
};
home = function() {
  $('#view').innerHTML = heading('A strategic design assistant.','Study proven robots and turn a game manual into one coherent robot concept.') +
    `<section class="hero-workbench"><div class="hero-copy"><div class="eyebrow">TEAM BEAN · 1833</div><h2>From game manual<br>to robot concept.</h2><p>See how real robots collect, move and score game pieces. Then give the design agent your manual, goals and build constraints.</p><div class="actions"><button class="btn primary" onclick="tab('create')">Create a recommendation</button><button class="btn ghost" onclick="tab('robots')">Browse robots</button></div></div><div class="hero-image"><img src="${WORKBENCH_HERO}" alt="Fuel in flight during an IRI match"><span>2026 IRI · Photo by Team BEAN</span></div></section>
    <div class="entry-cards"><section class="panel"><div class="eyebrow">HUMAN ENTRY POINT</div><h2>Find a design worth studying.</h2><p>Read robot dossiers, compare design decisions and ground your performance goals in event data.</p><button class="btn teal" onclick="tab('robots')">Explore ${DB.robots.length} robot dossiers</button></section><section class="panel"><div class="eyebrow">AGENT ENTRY POINT</div><h2>Retrieve the evidence you need.</h2><p>Open the full robot packets, game context, mechanism versions and indexed research. The local runner retrieves relevant evidence during each pass.</p><button class="btn" onclick="audience('agent')">Open agent instructions</button></section></div>`;
};
const sourceDossier = robotDetail;
robotDetail = function(a) {
  if (!a) return '<p>Select a robot dossier.</p>';
  const review = dossierReviews[a.id];
  const original = DB.technicalNotes.filter(n => n.robot_id === a.id);
  const pictures = (a.images || []).filter(i => !i.human_hidden);
  const sections = [['overview','Whole robot'],['flow','Piece flow'],['mechanisms','Mechanisms'],['versions','Versions'],['sources','Sources']];
  const mechanisms = (review?.subsystems || original.map(n=>({name:n.title,construction:n.construction,team_rationale:n.team_stated_reason,engineering_analysis:n.engineering_analysis,unknowns:n.limitations,source_urls:[n.source_url]})));
  return `<div class="dossier-title"><div class="eyebrow">${a.year} · ${esc(a.game)}</div><h2>${a.team} · ${esc(a.team_name)}</h2><p class="lede">${esc(a.robot||a.architecture)}</p></div><nav class="dossier-jumps" aria-label="Dossier sections">${sections.map(([k,l])=>`<a href="#dossier-${k}" onclick="event.preventDefault();this.closest('article, #research-drawer-body').querySelector('#dossier-${k}').scrollIntoView({behavior:'smooth'})">${l}</a>`).join('')}</nav>
    <section id="dossier-overview"><h3>The whole robot</h3>${prose(review?.whole_robot_explanation||a.architecture)}${pictures.length?'<div class="gallery">'+pictures.slice(0,2).map(figure).join('')+'</div>':''}</section>
    <section id="dossier-flow"><h3>Follow the game piece</h3>${review?prose(review.piece_flow):Object.entries(a.subsystems).map(([k,v])=>`<p><b>${esc(k)}</b> ${esc(v)}</p>`).join('')}<h3>Packaging and movement</h3>${prose(review?.packaging_and_motion||a.analysis)}</section>
    <section id="dossier-mechanisms"><h3>How the mechanisms work</h3>${mechanisms.map((m,i)=>`<div class="mechanism-chapter"><h4>${i+1} · ${esc(m.name)}</h4>${prose(m.construction)}${prose(m.operation)}${m.team_rationale?'<h5>Team rationale</h5>'+prose(m.team_rationale):''}${m.engineering_analysis?'<div class="inference"><h5>Engineering interpretation</h5>'+prose(m.engineering_analysis)+'</div>':''}${m.interfaces?'<h5>Interfaces</h5>'+prose(m.interfaces):''}${m.service_and_failure_modes?'<h5>Service and failure modes</h5>'+prose(m.service_and_failure_modes):''}${m.unknowns?'<details><summary>Evidence limits</summary>'+bullets(m.unknowns)+'</details>':''}<p class="small">${(m.source_urls||[]).map(u=>link(u,'Primary source')).join(' · ')}</p></div>`).join('')}</section>
    <section id="dossier-versions"><h3>Changes and versions</h3>${bullets(review?.revisions||a.versions)}${revisionDetails(a)}</section>
    <section><h3>Design lessons</h3>${bullets(review?.transferable_principles||[a.analysis])}${bullets(review?.disconfirming_conditions)}${architectureDetails(a)}</section>
    ${pictures.length>2?'<section><h3>Mechanism references</h3><div class="gallery">'+pictures.slice(2).map(figure).join('')+'</div></section>':''}
    <section id="dossier-sources"><h3>Evidence and sources</h3><p class="small">${review?'Expanded source review':'Existing source study · deeper review still pending'}</p>${(review?.source_reviews||[]).map(s=>`<details><summary>${esc(s.title)}</summary><p>${link(s.url)}</p>${prose(s.locator)}${prose(s.review_basis)}${prose(s.facts)}${prose(s.limitations)}</details>`).join('')}${bullets(review?.remaining_gaps||a.limits)}${a.primary.map(u=>`<p class="small">${link(u)}</p>`).join('')}${review?'<details><summary>Earlier technical notes</summary>'+original.map(n=>`<h4>${esc(n.title)}</h4>${prose(n.construction)}${prose(n.engineering_analysis)}`).join('')+'</details>':''}</section>`;
};
robotList = function() {
  const words = state.query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  const found = DB.robots.filter(a => (!state.year||a.year==state.year) && (!state.family||a.tags.includes(state.family)) && words.every(w => robotSearchText(a).includes(w)||JSON.stringify(dossierReviews[a.id]||{}).toLowerCase().includes(w))).sort((a,b)=>b.year-a.year||a.team-b.team);
  if (found.length && !found.some(a=>a.id===state.robot)) state.robot = found[0].id;
  $('#count').textContent = `${found.length} robot dossiers · team-number order`;
  $('#robot-list').innerHTML = found.map(a=>`<button class="row ${a.id===state.robot?'chosen':''}" data-robot="${a.id}" aria-pressed="${a.id===state.robot}"><span class="small">${a.year} · ${esc(a.robot||a.game)}</span><strong>${a.team} ${esc(a.team_name)}</strong><span class="subtitle">${esc(a.architecture)}</span></button>`).join('') || '<p>No dossiers match these filters.</p>';
  document.querySelectorAll('[data-robot]').forEach(b=>b.onclick=()=>{state.robot=b.dataset.robot;robotList();if(innerWidth<900)$('#detail').scrollIntoView({behavior:'smooth'});});
  $('#detail').innerHTML = found.length ? robotDetail(found.find(a=>a.id===state.robot)) : '<p>Clear the filters to see more robots.</p>';
};
const browseRobots = robots;
robots = function() {
  browseRobots();
  const filter = $('#family');
  if (filter?.options) for (const option of [...filter.options]) if (/supplement|historical|curated primary/i.test(option.value)) option.remove();
  $('#view').insertAdjacentHTML('afterbegin',heading('Robot library.','Find a robot by season, team or mechanism. Each dossier follows the complete piece path and links to the evidence.'));
};
function openDossier(id) {
  state.year=id.slice(0,4);
  state.robot=id;
  state.family='';
  tab('robots');
}
architectures = function() {
  const query = WB.lessonQuery.toLowerCase().trim();
  const rows = (DB.dossierReviews || []).filter(r => {
    if (WB.lessonYear && !r.robot_id.startsWith(WB.lessonYear+'-')) return false;
    return !query || asText([r.robot_id, r.whole_robot_explanation, r.transferable_principles, r.disconfirming_conditions]).toLowerCase().includes(query);
  });
  const pageSize = 20;
  const pages = Math.max(1, Math.ceil(rows.length/pageSize));
  WB.lessonPage = Math.max(0, Math.min(WB.lessonPage, pages-1));
  const cards = rows.slice(WB.lessonPage*pageSize, (WB.lessonPage+1)*pageSize).map(r => {
    const robot = DB.robots.find(a => a.id === r.robot_id);
    const principles = Array.isArray(r.transferable_principles) ? r.transferable_principles.slice(0,2) : r.transferable_principles;
    return `<section class="panel"><div class="eyebrow">${r.robot_id}</div><h2>${esc(robot?.robot||r.robot_id)}</h2>${bullets(principles)}<details><summary>When the trade reverses</summary>${bullets(r.disconfirming_conditions)}</details><button class="btn soft" onclick="openDossier('${r.robot_id}')">Read the whole robot</button></section>`;
  }).join('');
  const comparisons = (DB.designComparisons||[]).map(c =>
    `<details><summary>${esc(c.title)}</summary><p><strong>Decision.</strong> ${esc(c.decision)}</p><p>${esc(c.analysis)}</p><p><strong>How to compare.</strong> ${esc(c.check)}</p><div class="actions">${c.robots.map(id=>`<button class="btn soft" onclick="openDossier('${id}')">${id}</button>`).join('')}</div></details>`
  ).join('');
  $('#view').innerHTML = heading('Design lessons.','Compare decisions across teams and see when each one stops paying off.')+
    `<form id="lesson-filters" class="toolbar"><select id="lesson-year" aria-label="Lesson season">${years()}</select><input id="lesson-query" aria-label="Find a design lesson" placeholder="Try transfer, service access, or defense" value="${esc(WB.lessonQuery)}"><button class="btn">Apply</button></form>
    <section class="panel"><h2>Architecture comparisons</h2>${comparisons}${(DB.architectureCases||[]).map(c=>`<details><summary>${esc(c.robot_id+' · '+c.title)}</summary>${architectureCase(c)}</details>`).join('')}</section>
    <p>${rows.length} robot studies · Page ${WB.lessonPage+1} of ${pages}</p>
    <div class="lesson-grid">${cards||'<p>No design lessons match these filters.</p>'}</div>
    <div class="actions"><button class="btn" ${WB.lessonPage===0?'disabled':''} onclick="WB.lessonPage--;render()">Previous</button><button class="btn" ${WB.lessonPage===pages-1?'disabled':''} onclick="WB.lessonPage++;render()">Next</button></div>
`;
  $('#lesson-year').value = WB.lessonYear;
  $('#lesson-filters').onsubmit = event => {
    event.preventDefault();
    WB.lessonYear = $('#lesson-year').value;
    WB.lessonQuery = $('#lesson-query').value;
    WB.lessonPage = 0;
    render();
  };
};
function benchmarkValue(b,stage,k) { return b.alliance_populations?.[stage]?.metrics?.no_foul?.[k] ?? null; }
function distributionTable(data) {
  return `<div class="tablewrap"><table class="data-table"><thead><tr><th>Metric</th><th>Sample</th><th>P25</th><th>Median</th><th>P75</th><th>P90</th><th>Range</th></tr></thead><tbody>${Object.entries(data||{}).map(([k,d])=>`<tr><td>${esc(k.replaceAll('_',' '))}</td><td>${num(d.n)}</td><td>${num(d.p25)}</td><td>${num(d.median)}</td><td>${num(d.p75)}</td><td>${num(d.p90)}</td><td>${num(d.min)}–${num(d.max)}</td></tr>`).join('')}</tbody></table></div>`;
}
function showBenchmark(id) {
  const b=DB.benchmarks.find(x=>x.event===id);
  $('#benchmark-detail').innerHTML=`<section class="panel"><h2>${b.year} · ${esc(b.name)}</h2><p>${link(b.tba_url,'Match results')} · ${link(b.data_url,'Source bundle')}</p><p>${esc(b.notes)}</p>${Object.entries(b.alliance_populations||{}).map(([k,p])=>`<h3>${esc(k)} alliance scoring</h3><p>${p.completed_matches} matches · ${p.alliance_observations} alliance rows · ${p.excluded_dq} DQ rows excluded · ${p.missing_score} missing clean scores</p>${distributionTable(Object.fromEntries(Object.entries(p.metrics).filter(([key])=>['no_foul','score','auto_points','teleop_points','endgame_points','endgame_tower','barge_points','total_coral_points','total_algae_points'].includes(key))))}<details><summary>All scoring components</summary>${distributionTable(p.metrics)}</details>${k==='qualification'&&Object.keys(p.ranking_points).length?'<details><summary>Qualification bonus RP rates</summary><ul>'+Object.entries(p.ranking_points).map(([name,d])=>`<li>${esc(name)} · ${d.achieved} of ${d.observed} recorded alliance outcomes</li>`).join('')+'</ul></details>':''}`).join('')}${b.individual_epa?'<h3>Individual EPA</h3>'+distributionTable(b.individual_epa):'<p>This earlier event record has a narrower scoring sample.</p>'}</section>`;
  $('#benchmark-detail').scrollIntoView({behavior:'smooth'});
}
bench = function() {
  const values = DB.benchmarks;
  const rows = values.filter(b=>(!WB.benchmarkYear||WB.benchmarkYear==b.year)&&(!WB.eventType||WB.eventType===b.type)&&(!WB.eventWeek||WB.eventWeek==b.week)&&(!WB.eventQuery||(b.name+' '+b.event).toLowerCase().includes(WB.eventQuery.toLowerCase()))).sort((a,b)=>b.year-a.year||(a.week||0)-(b.week||0)||a.name.localeCompare(b.name));
  const maxPage=Math.max(0,Math.ceil(rows.length/30)-1);
  WB.benchmarkPage=Math.min(maxPage,Math.max(0,WB.benchmarkPage));
  const view=rows.slice(30*WB.benchmarkPage,30*(WB.benchmarkPage+1));
  $('#view').innerHTML=heading('Performance benchmarks.','Compare alliance output by event stage and individual EPA in separate columns.')+
    `<form id="benchmark-filters" class="toolbar"><select id="benchmark-year" aria-label="Season">${years()}</select><select id="benchmark-type" aria-label="Event type"><option value="">All event types</option>${[...new Set(values.map(b=>b.type))].sort().map(t=>`<option value="${esc(t)}">${esc(t.replaceAll('_',' '))}</option>`).join('')}</select><select id="benchmark-week" aria-label="Week"><option value="">All weeks</option>${[...new Set(values.map(b=>b.week))].filter(v=>v!=null).sort((a,b)=>a-b).map(w=>`<option>${w}</option>`).join('')}</select><input id="benchmark-search" aria-label="Find an event" placeholder="Find an event" value="${esc(WB.eventQuery)}"><button class="btn">Apply</button></form>
    <p class="notice">${values.length} event records. The expanded sample includes the first and last event key for each season, event type and week, plus available PCH and Worlds events. These distributions describe the observed sample.</p><section class="panel"><p>${rows.length} events match · Page ${WB.benchmarkPage+1} of ${maxPage+1}</p><div class="tablewrap"><table class="data-table"><thead><tr><th>Event</th><th>Stage</th><th>Qual clean median</th><th>Qual clean P90</th><th>Playoff clean median</th><th>8th pre-elim EPA</th></tr></thead><tbody>${view.map(b=>`<tr><td><button type="button" class="text-button" data-benchmark="${b.event}">${b.year} · ${esc(b.name)}</button></td><td>${esc(b.type.replaceAll('_',' '))} · Week ${num(b.week)}</td><td>${num(benchmarkValue(b,'qualification','median'))}</td><td>${num(benchmarkValue(b,'qualification','p90'))}</td><td>${num(benchmarkValue(b,'playoff','median'))}</td><td>${num(b.pre_elim_epa_8th)}</td></tr>`).join('')}</tbody></table></div><div class="actions"><button class="btn" ${WB.benchmarkPage===0?'disabled':''} onclick="WB.benchmarkPage--;render()">Previous</button><button class="btn" ${WB.benchmarkPage===maxPage?'disabled':''} onclick="WB.benchmarkPage++;render()">Next</button></div></section><div id="benchmark-detail"></div>`;
  $('#benchmark-year').value=WB.benchmarkYear;
  $('#benchmark-type').value=WB.eventType;
  $('#benchmark-week').value=WB.eventWeek;
  $('#benchmark-filters').onsubmit=e=>{e.preventDefault();WB.benchmarkYear=$('#benchmark-year').value;WB.eventType=$('#benchmark-type').value;WB.eventWeek=$('#benchmark-week').value;WB.eventQuery=$('#benchmark-search').value;WB.benchmarkPage=0;render();};
  document.querySelectorAll('[data-benchmark]').forEach(e=>e.onclick=()=>showBenchmark(e.dataset.benchmark));
};
agent = function() {
  const m=DB.agentManifest;
  $('#view').innerHTML=heading('Agent entry point.','Retrieve full robot packets and carry their source limits into the recommendation.')+`<section class="panel"><h2>Run the design investigation.</h2><p>Use the local launcher to restore the embedded corpus. Give it the actual manual and a design brief. It runs six research passes and produces recommendation.md.</p><div class="actions"><button class="btn primary" onclick="showSetup()">Set up the local workspace</button><button class="btn" onclick="tab('create')">Prepare the design brief</button></div></section><div class="entry-cards"><section class="panel"><h2>Read the full packet.</h2><pre>python scripts/query_agent.py packet 2018-254\npython scripts/query_agent.py search Lockdown --kind dossier_review\npython scripts/query_agent.py images --robot 2026-4414</pre><p>Read AGENTS.md, the game chapter and the team design doctrine first. Open source images at the correct robot version and compare complete architectures.</p></section><section class="panel"><h2>Research coverage</h2><p>${m.counts.robot_packets} robot packets · ${m.counts.deep_dossier_reviews||0} expanded reviews · ${DB.benchmarks.length} event benchmarks.</p><details><summary>Machine-readable manifest</summary><pre style="overflow:auto;max-height:420px">${esc(JSON.stringify(m,null,2))}</pre></details></section></div>`;
};
