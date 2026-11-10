"""Add the branded local-agent workflow without discarding the research reader."""
from pathlib import Path
import base64,hashlib,io,json,re,zipfile
ROOT=Path(__file__).resolve().parents[1]

def package():
 out=io.BytesIO()
 selected=[ROOT/'AGENTS.md',ROOT/'schema.sql',ROOT/'scripts/query_agent.py',ROOT/'scripts/interface_compatibility.py',ROOT/'agent/manifest.json',ROOT/'agent/retrieval_units.jsonl',ROOT/'agent/image_catalog.jsonl',ROOT/'agent/design_rubric.json',ROOT/'agent/evaluation_cases.jsonl',ROOT/'agent/architecture_evaluation_cases.jsonl',ROOT/'agent/README.md']
 selected+=list((ROOT/'docs').rglob('*.md'))
 selected+=list((ROOT/'data').glob('*.jsonl'))
 selected+=[p for p in (ROOT/'data').glob('*.json') if p.name!='reader_payload.json']
 selected+=list((ROOT/'agent/robot_packets').glob('*.json'))
 selected+=list((ROOT/'agent').glob('*.jsonl'))
 selected+=list((ROOT/'scripts').glob('*.py'))
 selected+=list((ROOT/'team1833').glob('*.json'))+list((ROOT/'team1833').glob('*.md'))
 selected+=[ROOT/'data/cohort_coverage.jsonl',ROOT/'data/cohort_research_attempts.jsonl',ROOT/'data/architecture_owner_accounts.jsonl',ROOT/'data/architecture_research_ledger.jsonl']
 selected+=list((ROOT/'workbench').glob('*.py'))+list((ROOT/'workbench').glob('*.md'))+list((ROOT/'workbench').glob('*.json'))
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in sorted(set(selected)):
   if p.is_file():z.writestr(str(p.relative_to(ROOT)),p.read_bytes())
 raw=out.getvalue();fingerprints={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n')).hexdigest() for p in [ROOT/'agent/retrieval_units.jsonl',ROOT/'data/robot_dossiers.jsonl',ROOT/'data/mechanism_revisions.jsonl',ROOT/'data/architecture_cases.jsonl',ROOT/'workbench/RUN_CONTRACT.md',ROOT/'workbench/manual.py',ROOT/'workbench/research.py']}
 return dict(corpus_files=fingerprints,format='zip',sha256=hashlib.sha256(raw).hexdigest(),base64=base64.b64encode(raw).decode(),scope='Complete reader research plus original text guides, retrieval units and runner. Git history, XLSX task template and original-resolution image bytes are not required for recommendation runs; the task explicitly waives worksheets.')

def enhance(html):
 fontcss=''
 for name,f,weight in [('Chewy','chewy.ttf','400'),('Manrope','manrope.ttf','100 900')]:
  fontcss+="@font-face{font-family:'"+name+"';font-style:normal;font-weight:"+weight+";font-display:swap;src:url(data:font/ttf;base64,"+base64.b64encode((ROOT/'workbench'/f).read_bytes()).decode()+") format('truetype');}\n"
 css=fontcss+(ROOT/'workbench/workbench.css').read_text();html=html.replace('</style>',css+'\n</style>',1)
 logo='data:image/png;base64,'+base64.b64encode((ROOT/'workbench/bean-logo.png').read_bytes()).decode()
 chrome=f'''<aside class="bean-sidebar"><a class="bean-brand" href="#" onclick="tab('home');return false"><img src="{logo}" alt="Team BEAN 1833"><div><b>BEAN 1833</b><span>Design workbench</span></div></a><nav id="tabs" aria-label="Main navigation"></nav><div class="sidebar-bottom"><strong>Simple. Effective. Competitive.</strong>Research the whole robot.<br>Keep the useful complexity.<br><button class="text-link" style="font-size:9px;padding:12px 0 0" onclick="showSetup()">Local runner setup ↗</button></div></aside><div class="bean-shell"><div class="bean-topbar"><div class="crumb">Workspace <span aria-hidden="true"> / </span> <strong id="bean-page-name">Overview</strong></div><div class="topbar-right"><button id="runner-badge" class="runner-badge" onclick="showSetup()"><i class="status-dot"></i>Reader mode</button><button class="text-link" onclick="tab('create')">New brief +</button><span class="avatar" aria-label="Team 1833">18</span></div></div><main class="bean-main"><section id="view" aria-live="polite"><div class="panel"><h1 class="bean-display">Opening your research workspace…</h1><p>The complete research library is loading. Opening a local copy is fastest.</p></div></section><div class="workbench-footer"><span>BEAN Design Workbench · Research snapshot 7 November 2026</span><span>Provisional evidence · Source facts and engineering inference stay distinct</span></div></main></div><div id="toast" role="status"></div>
<dialog id="setup-dialog" class="setup-dialog" aria-labelledby="setup-title"><button class="setup-close" onclick="closeSetup()" aria-label="Close setup">×</button><div class="eyebrow" style="color:var(--green)">ONE-TIME SETUP</div><h2 id="setup-title">Give the agent its workspace.</h2><p>Browse this file anywhere. To run a real investigation, use the local launcher with Python 3.10+ and the official Codex CLI.</p><ol><li><b>Keep this file named index.html.</b> Download the launcher into the same folder.<div class="actions" style="margin-top:10px"><button class="btn primary" onclick="downloadRunner()">Download workbench.py</button></div></li><li><b>Set up Codex once.</b> If it is not already installed, install Node.js LTS first, then:<code>npm install -g @openai/codex<br>codex login</code>Uses your existing Codex sign-in and available account usage. No API key goes into this page.</li><li><b>Start the workbench from that folder.</b><code>python workbench.py</code>On macOS/Linux use <b>python3</b> if needed. On Windows, <b>py workbench.py</b> also works. For complete PDF text and diagram support, run <b>python -m pip install pymupdf</b> once. Keep the terminal open.</li><li><b>Use the local page that opens.</b> The launcher restores the embedded research workspace when needed, then opens <a href="http://127.0.0.1:1833" target="_blank" rel="noopener">http://127.0.0.1:1833</a>. Add your manual and start the investigation. If you prepared a brief here first, export it below, then choose <b>Import brief</b> on the local page.</li></ol><p id="setup-status" class="callout">Checking local connection…</p><div class="actions"><button class="btn teal" onclick="refreshConnection()">Refresh connection</button><button class="btn" onclick="exportBriefBundle()">Export this brief</button><button class="btn" onclick="closeSetup()">Back to workspace</button></div><p style="font-size:10px;color:var(--muted)">The agent researches inside an isolated run folder. Source material stays available on disk. Six passes and validation improve consistency; they do not certify physical feasibility. If your CLI or sandbox is unavailable, use Export agent task with the full repository instead.</p></dialog>
<dialog class="research-drawer" id="research-drawer" aria-label="Complete robot research"><button class="btn small" onclick="document.getElementById('research-drawer').close()">Close</button><div id="research-drawer-body"></div></dialog>'''
 start=html.index('<body>')+len('<body>');end=html.index('<script id="database"')
 old=html[start:end];dialog=old[old.index('<dialog id="image-dialog"'):]
 html=html[:start]+chrome+dialog+html[end:]
 html=html.replace('<title>FRC Strategy Atlas · 2018–2019 / 2022–2026</title>','<title>BEAN 1833 · Design Workbench</title>')
 bundle=package();runner=dict(filename='workbench.py',base64=base64.b64encode((ROOT/'workbench/workbench.py').read_bytes()).decode())
 tags='<script id="workbench-package" type="application/json">'+json.dumps(bundle,separators=(',',':'))+'</script>\n<script id="workbench-runner" type="application/json">'+json.dumps(runner,separators=(',',':'))+'</script>\n'
 html=html.replace('<script id="database"',tags+'<script id="database"',1)
 anchor='tabs();render();\nhandleImageHash();'
 assert anchor in html,'Expected reader initialization anchor'
 hero='data:image/jpeg;base64,'+base64.b64encode((ROOT/'workbench/clover-iri-match.jpg').read_bytes()).decode()
 html=html.replace(anchor,'const WORKBENCH_HERO='+json.dumps(hero)+';\n'+(ROOT/'workbench/workbench.js').read_text()+'\n'+anchor,1)
 # Start the interface before the large image/package streams finish parsing.
 delayed=[]
 for tag_id in ['image-assets','workbench-package']:
  pattern=r'<script id="'+tag_id+r'" type="application/json">.*?</script>'
  match=re.search(pattern,html,re.S);assert match,tag_id
  delayed.append(match[0]);html=html[:match.start()]+html[match.end():]
 html=html.replace("const IMAGE_ASSETS=JSON.parse(document.getElementById('image-assets').textContent);", "const IMAGE_ASSETS=window.__beanAssetsComplete?JSON.parse(document.getElementById('image-assets')?.textContent||'{}'):{};")
 hydration="""<script>(window.__beanAppReady||Promise.resolve()).then(()=>{window.__beanAssetsComplete=true;Object.assign(IMAGE_ASSETS,JSON.parse(document.getElementById('image-assets').textContent));if(typeof state!=='undefined'&&!['home','create','runs','run'].includes(state.tab)){const y=window.scrollY;render();window.scrollTo({top:y,behavior:'auto'});}});</script>"""
 html=html.replace('</body>',delayed[0]+hydration+delayed[1]+'</body>',1)
 return html
