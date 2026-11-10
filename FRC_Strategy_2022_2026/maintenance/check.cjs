const fs = require('fs'),vm=require('vm'),zlib=require('zlib');
const s=fs.readFileSync('delivery/index.html','utf8');
function tag(k) {return s.match(new RegExp('<script id="'+k+'"[^>]*>([\\s\\S]*?)</script>'))[1];}
const value=JSON.parse(tag('database'));
const data=zlib.gunzipSync(Buffer.from(value.base64,'base64')).toString();
const images=tag('image-assets');
const els=new Map();
const get=id=>{if(!els.has(id))els.set(id,{value:'',textContent:'',innerHTML:'',dataset:{},addEventListener(){},scrollIntoView(){},insertAdjacentHTML(_,h){this.innerHTML=h+this.innerHTML;}});return els.get(id);};
const ctx={document:{body:null,getElementById:id=>id==='database'?{textContent:data}:id==='image-assets'?{textContent:images}:get('#'+id),querySelector:get,querySelectorAll:()=>[],addEventListener(){}},window:{__beanAssetsComplete:true,scrollTo(){},addEventListener(){}},location:{hash:'',protocol:'file:',hostname:''},URLSearchParams,console,setTimeout(){return 0},clearTimeout(){},innerWidth:1280};
vm.createContext(ctx);vm.runInContext(tag('application-source'),ctx);
vm.runInContext(`if(!$('#view').innerHTML.includes('strategic design assistant'))throw Error('Home');if($('#tabs').innerHTML.includes('Binders & mechanics'))throw Error('Duplicate nav');audience('agent');if(!$('#tabs').innerHTML.includes('Video research'))throw Error('Agent nav');audience('human');tab('robots');for(const a of DB.robots)robotDetail(a);if(!robotDetail(DB.robots.find(a=>a.id==='2018-254')).includes('53–0–0'))throw Error('Lockdown');if((robotDetail(DB.robots.find(a=>a.id==='2026-4414')).match(/data-revision-id=/g)||[]).length!==21)throw Error('4414 revisions');if(IMAGE_ASSETS['7bc3e516e03f77f970'])throw Error('Coprocessor');tab('architectures');tab('bench');for(const b of DB.benchmarks)showBenchmark(b.event);tab('create');`,ctx);
console.log('PASS: navigation, 143 dossier renders, 21 individual revisions, benchmark details and recommendation form');
