"""Meaningful runner tests with an explicit deterministic CLI double.

No claims of LLM design quality; production CLI flags and actual HTTP paths are
exercised without consuming a six-pass recommendation run.
"""
import base64,copy,http.client,importlib.util,json,pathlib,sys,tempfile,threading,time,unittest
P=pathlib.Path(__file__).resolve();ROOT=P.parents[1]
spec=importlib.util.spec_from_file_location('bean_workbench',P.parent/'workbench.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class RunnerTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.tmp=tempfile.TemporaryDirectory();cls.directory=pathlib.Path(cls.tmp.name)
  cls.app=mod.Workbench(ROOT,ROOT/'index.html',store=cls.directory/'runs');cls.fake=cls.directory/'fake_cli.py'
  cls.fake.write_text('''import json,sys,time,pathlib
# Consume the prompt just as the real CLI does, including on Windows pipes.
sys.stdin.buffer.read()
args=sys.argv[1:];p=pathlib.Path(args[args.index('-C')+1]);output=pathlib.Path(args[args.index('--output-last-message')+1]);brief=json.loads((p/'brief.json').read_text());job=json.loads((p/'job.json').read_text());stage=int(output.name[:2])-1
if brief['title']=='Slow':time.sleep(8)
questions=[]
if brief['title']=='Question' and stage==0 and not job['answers']:questions=[{'id':'angle','question':'Which angle convention applies?','decision_affected':'Reach geometry'}]
result={'summary':'A test-double pass, not a model design.','notebook':'Pinned test evidence and explicit limits.','recommendation_markdown':('# Test-double concept\\n\\n'+'A complete placeholder paragraph for runner verification. '*30) if stage in [3,5] else '', 'selected_robots':['2023-1746'],'source_ids':['architecture-2023-1746-owner'],'manual_pages':[{'page':1,'status':'read','notes':'Text test manual'}],'image_observations':[{'image_id':'architecture-1746-overview','observation':'Test-double observation, not real image inspection.','limitation':'This is a test.'}],'questions':questions,'findings':[]}
if brief['title']=='Repair' and stage==2 and job['attempts']['evidence']==1:result['source_ids']=['invalid-test-source']
output.write_text(json.dumps(result));print(json.dumps({'type':'item.completed','item':{'type':'agent_message','text':'Test pass completed'}}));print(json.dumps({'type':'turn.completed'}))
''',encoding='utf-8')
  cls.app.cli=[sys.executable,str(cls.fake)]
 @classmethod
 def tearDownClass(cls):cls.tmp.cleanup()
 def new(self,title='Test'):
  return self.app.create({'brief':{'title':title,'effort':'high','model':''},'manual':{'name':'game.txt','base64':base64.b64encode(b'Complete fictional test manual.').decode()}})
 def wait(self,id,expected):
  until=time.monotonic()+15
  while time.monotonic()<until:
   j=self.app.get(id)
   if j['status'] in expected and id not in self.app.active:return j
   time.sleep(.03)
  self.fail(str(self.app.get(id)))
 def test_01_pipeline_and_saved_final(self):
  j=self.new();self.app.start(j['id']);j=self.wait(j['id'],['complete','failed']);self.assertEqual(j['status'],'complete',j.get('error'));self.assertEqual(len(j['results']),6);self.assertTrue(j['has_recommendation']);self.assertTrue((self.app.folder(j['id'])/'NOTEBOOK.md').is_file())
  prompt=(self.app.folder(j['id'])/'06-final-prompt.txt').read_text();self.assertIn('OWNER ANSWERS',prompt);self.assertIn('critique',prompt)
 def test_02_questions_pause_and_resume(self):
  j=self.new('Question');self.app.start(j['id']);j=self.wait(j['id'],['needs_input','failed']);self.assertEqual(j['status'],'needs_input');self.assertEqual(j['stage'],0)
  with self.assertRaises(ValueError):self.app.start(j['id'],{})
  self.app.start(j['id'],{'angle':'Angle above horizontal.'});j=self.wait(j['id'],['complete','failed']);self.assertEqual(j['status'],'complete',j.get('error'));self.assertEqual(j['answers'][0]['answer'],'Angle above horizontal.');self.assertEqual(j['attempts']['manual'],2)
 def test_03_cancel_keeps_files(self):
  j=self.new('Slow');self.app.start(j['id']);time.sleep(.15);self.app.stop(j['id']);j=self.wait(j['id'],['stopped']);self.assertTrue((self.app.folder(j['id'])/'manual.txt').is_file());self.assertEqual(j['stage'],0)
 def test_04_coverage_and_reference_gates(self):
  j=self.new();r={k:[] for k in mod.SCHEMA['required']};r.update(summary='x',notebook='x',recommendation_markdown='x')
  with self.assertRaisesRegex(ValueError,'coverage'):self.app.validate_result(j,r,0)
  r['selected_robots']=['2023-999999'];self.assertRaises(ValueError,self.app.validate_result,j,r,1)
  r['selected_robots']=[];r['findings']=[{'severity':'blocking','issue':'Impossible transfer','evidence':'x','resolution':'Unresolved'}];r['recommendation_markdown']='x'*600
  with self.assertRaisesRegex(ValueError,'blocking'):self.app.validate_result(j,r,5)
 def test_05_upload_limits_and_path_safety(self):
  with self.assertRaises(ValueError):self.app.create({'brief':{'title':'x'},'manual':{'name':'x.pdf','base64':base64.b64encode(b'Not a PDF').decode()}})
  with self.assertRaises(ValueError):self.app.create({'brief':{'title':'x','model':'model; shell'},'manual':{'name':'x.txt','base64':'eA=='}})
  with self.assertRaises(ValueError):self.app.folder('../../etc')
  with self.assertRaises(ValueError):mod.inside(ROOT/'images','../AGENTS.md')
 def test_06_automatic_contract_repair(self):
  j=self.new('Repair');self.app.start(j['id']);j=self.wait(j['id'],['complete','failed']);self.assertEqual(j['status'],'complete',j.get('error'));self.assertEqual(j['attempts']['evidence'],2);self.assertTrue(any(e['kind']=='validation' for e in j['events']))
 def test_07_snapshot_mismatch_is_blocked(self):
  j=self.new();original=mod.corpus_fingerprint
  try:
   mod.corpus_fingerprint=lambda root:{'different':'snapshot'}
   with self.assertRaisesRegex(ValueError,'different research snapshot'):self.app.start(j['id'])
  finally:mod.corpus_fingerprint=original
 def test_08_http_loopback_csrf_and_artifact(self):
  mod.Handler.app=self.app;server=mod.ThreadingHTTPServer(('127.0.0.1',0),mod.Handler);threading.Thread(target=server.serve_forever,daemon=True).start();port=server.server_port
  try:
   c=http.client.HTTPConnection('127.0.0.1',port);c.request('POST','/api/runs',body='{}',headers={'Content-Type':'application/json'});r=c.getresponse();r.read();self.assertEqual(r.status,403)
   c.request('GET','/api/runs',headers={'Host':'evil.example'});r=c.getresponse();r.read();self.assertEqual(r.status,403)
   payload=json.dumps({'brief':{'title':'HTTP brief'},'manual':{'name':'game.txt','base64':'eA=='}})
   c.request('POST','/api/runs',body=payload,headers={'Content-Type':'application/json','Origin':f'http://127.0.0.1:{port}','X-Bean-Token':self.app.token});r=c.getresponse();j=json.loads(r.read());self.assertEqual(r.status,201,j)
   c.request('GET','/api/runs/'+j['id']);r=c.getresponse();self.assertEqual(r.status,200);self.assertEqual(json.loads(r.read())['title'],'HTTP brief')
   c.request('GET','/images/../AGENTS.md');r=c.getresponse();r.read();self.assertEqual(r.status,404)
  finally:server.shutdown();server.server_close()
if __name__=='__main__':unittest.main(verbosity=2)
