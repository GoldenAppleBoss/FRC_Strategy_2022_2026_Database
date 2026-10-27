"""Read-only XLSX structure/content audit. Standard library; no physics certification."""
import collections,json,pathlib,re,sys,zipfile,xml.etree.ElementTree as E,posixpath
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/package/2006/relationships'}
def audit(path):
 errors=[];warnings=[]
 with zipfile.ZipFile(path) as z:
  wb=E.fromstring(z.read('xl/workbook.xml'));sheets=wb.findall('s:sheets/s:sheet',NS)
  if len(sheets)!=1:errors.append('Exactly one worksheet required')
  if not sheets:return {'errors':errors,'warnings':warnings}
  if sheets[0].get('name')!='Task List':errors.append('Worksheet must be named Task List')
  rid=sheets[0].get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
  rels=E.fromstring(z.read('xl/_rels/workbook.xml.rels'));target=next(x.get('Target') for x in rels if x.get('Id')==rid)
  file=target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/'+target)
  ss=[]
  if 'xl/sharedStrings.xml' in z.namelist():
   ss=[''.join(x.itertext()) for x in E.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',NS)]
  ws=E.fromstring(z.read(file));cells={};formulas={};cache={}
  for c in ws.findall('.//s:sheetData/s:row/s:c',NS):
   ref=c.get('r');typ=c.get('t');v=c.find('s:v',NS);txt=v.text if v is not None else None
   if typ=='s':txt=ss[int(txt)] if txt is not None else ''
   elif typ=='inlineStr':txt=''.join(c.find('s:is',NS).itertext())
   cells[ref]=txt
   if c.find('s:f',NS) is not None:formulas[ref]=c.find('s:f',NS).text;cache[ref]=txt
   if typ=='e':errors.append('Excel error at '+ref+': '+str(txt))
  # Locate the filter/table task range so appended calculations are not mistaken for tasks.
  af=ws.find('s:autoFilter',NS);end=92
  if af is not None and af.get('ref'):end=int(re.search(r'(\d+)$',af.get('ref')).group(1))
  relfile=posixpath.dirname(file)+'/_rels/'+posixpath.basename(file)+'.rels'
  if relfile in z.namelist():
   for rel in E.fromstring(z.read(relfile)):
    if rel.get('Type','').endswith('/table'):
     tf=rel.get('Target');tf=tf.lstrip('/') if tf.startswith('/') else posixpath.normpath(posixpath.dirname(file)+'/'+tf)
     table=E.fromstring(z.read(tf))
     if table.get('name')=='RobotTasks':end=int(re.search(r'(\d+)$',table.get('ref')).group(1))
  tasks=[i for i in range(13,end+1) if str(cells.get('B'+str(i)) or '').strip()]
  for row in range(2,8):
   if not str(cells.get('C'+str(row)) or '').strip():errors.append('Missing metadata C'+str(row))
  for i in tasks:
   for col in 'ABCDEFHIJKLM':
    if not str(cells.get(col+str(i)) or '').strip():errors.append('Missing task value '+col+str(i))
   if cells.get('E'+str(i)) not in ['1','2','3']:warnings.append('Priority needs review E'+str(i))
   if cells.get('F'+str(i)) not in ['1','2','3','5','8','13','21']:warnings.append('Difficulty needs review F'+str(i))
   if 'G'+str(i) not in formulas:errors.append('Missing priority/difficulty formula G'+str(i))
  for col in ['I','J','M']:
   groups=collections.defaultdict(list)
   for i in tasks:
    txt=re.sub(r'\s+',' ',str(cells.get(col+str(i)) or '').strip().lower())
    if txt:groups[txt].append(i)
   for text,rows in groups.items():
    if len(rows)>=5 and len(rows)>=len(tasks)/2:warnings.append({'kind':'repeated_content_requires_review','column':col,'rows':rows,'count':len(rows),'text':text})
  counts=collections.Counter(cells.get('H'+str(i)) for i in tasks)
  expected={'B10':len(tasks),'E10':counts['Must do'],'H10':counts['Might do'],'K10':counts['Won’t do']}
  for ref,value in expected.items():
   try:ok=float(cache.get(ref))==value
   except (ValueError,TypeError):ok=False
   if not ok:warnings.append('Missing/stale summary cache '+ref+'; expected '+str(value))
  for row in range(13,end+1):
   if row not in tasks and str(cells.get('H'+str(row)) or '').strip():warnings.append('Recommendation on unused task row '+str(row))
 return {'scope':'Structure, nonblank fields, formula presence, summary caches and exact duplicate text; semantic/physical quality requires human review','worksheet_count':len(sheets),'task_count':len(tasks),'recommendation_counts':dict(counts),'errors':errors,'warnings':warnings,'structural_pass':not errors,'ready_for_architecture_selection':'not established by this audit'}
if __name__=='__main__':
 result=audit(pathlib.Path(sys.argv[1]));print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(1 if result['errors'] else 0)
