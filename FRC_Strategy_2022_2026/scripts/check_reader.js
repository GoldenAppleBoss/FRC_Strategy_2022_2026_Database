const fs = require('fs'),vm=require('vm'),zlib=require('zlib');
const path=require('path');
const root=path.resolve(__dirname,'..');
const s=fs.readFileSync(process.argv[2]||path.join(root,'index.html'),'utf8');
function tag(k) {return s.match(new RegExp('<script id="'+k+'"[^>]*>([\\s\\S]*?)</script>'))[1];}
const value=JSON.parse(tag('database'));
const data=value.encoding==='gzip'?zlib.gunzipSync(Buffer.from(value.base64,'base64')).toString('utf8'):JSON.stringify(value);
const images=tag('image-assets');
const els=new Map();
const get=id=>{if(!els.has(id))els.set(id,{value:'',textContent:'',innerHTML:'',dataset:{},addEventListener(){},scrollIntoView(){},insertAdjacentHTML(_,h){this.innerHTML=h+this.innerHTML;}});return els.get(id);};
const ctx={document:{body:null,getElementById:id=>id==='database'?{textContent:data}:id==='image-assets'?{textContent:images}:get('#'+id),querySelector:get,querySelectorAll:()=>[],addEventListener(){}},window:{__beanAssetsComplete:true,scrollTo(){},addEventListener(){}},location:{hash:'',protocol:'file:',hostname:''},URLSearchParams,console,setTimeout(){return 0},clearTimeout(){},innerWidth:1280};
vm.createContext(ctx);vm.runInContext(tag('application-source'),ctx);
vm.runInContext(`if(!$('#view').innerHTML.includes('strategic design assistant'))throw Error('Home');if($('#tabs').innerHTML.includes('Binders & mechanics'))throw Error('Duplicate nav');audience('agent');if(!$('#tabs').innerHTML.includes('Video research'))throw Error('Agent nav');audience('human');tab('robots');for(const a of DB.robots)robotDetail(a);if(!robotDetail(DB.robots.find(a=>a.id==='2018-254')).includes('53–0–0'))throw Error('Lockdown');if((robotDetail(DB.robots.find(a=>a.id==='2026-4414')).match(/data-revision-id=/g)||[]).length!==21)throw Error('4414 revisions');if(IMAGE_ASSETS['7bc3e516e03f77f970'])throw Error('Coprocessor');tab('architectures');tab('bench');for(const b of DB.benchmarks)showBenchmark(b.event);tab('create');`,ctx);
vm.runInContext(`
const counts=DB.agentManifest.counts;
if(DB.robots.length!==143||DB.robots.length!==counts.robot_packets)throw Error('Roster count');
if(DB.technicalNotes.length!==counts.technical_notes||DB.technicalNotes.length!==353)throw Error('Technical note count');
if(DB.architectureCases.length!==5||DB.physicalStudies.length!==7||DB.mechanismInterfaces.length!==20)throw Error('Expanded research');
if(DB.benchmarks.length!==292)throw Error('Expanded benchmarks');
if(Object.keys(IMAGE_ASSETS).length!==625||Object.keys(IMAGE_ASSETS).length!==counts.images)throw Error('Image count');
for(const im of Object.values(IMAGE_ASSETS))if(!im.base64||!im.mime.startsWith('image/'))throw Error('Embedded image');
for(const year of [2018,2019])for(const r of DB.robots.filter(r=>r.year===year))if(r.epa!==null||r.epa_rank!==null)throw Error('Historical EPA');
for(const r of DB.robots)if(!robotDetail(r).includes(String(r.team)))throw Error('Dossier render '+r.id);
`,ctx);
console.log('PASS: navigation, 143 dossier renders, 353 notes, 625 embedded images, 21 revisions, 292 benchmarks and recommendation form. Browser layout not tested.');
