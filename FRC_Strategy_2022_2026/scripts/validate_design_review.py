"""Structural gate for an 1833 design-review JSON. Human review remains essential."""
import json,pathlib,sys
def validate(a):
 errors=[]
 def require(ok,msg):
  if not ok:errors.append(msg)
 require(a.get('team')==1833,'Team must be 1833')
 c=a.get('constraints',{});require(c.get('primary_contributor') is True,'Primary contributor constraint required');require(c.get('turret_allowed') is False,'Turrets are prohibited')
 require(c.get('pneumatics_allowed') is False,'Pneumatics are prohibited')
 selected=a.get('selected_architecture',{});require(selected.get('role')=='primary_contributor','Support-only selected architecture prohibited');require(selected.get('has_turret') is False,'Selected architecture must be non-turret')
 require(selected.get('has_pneumatics') is False,'Selected architecture must be non-pneumatic')
 require(bool(a.get('manual_revision')) and bool(a.get('manual_source')),'Manual revision/source required')
 require(a.get('task_workbook',{}).get('worksheet_count')==1,'One-sheet task workbook required')
 require(bool(a.get('task_workbook',{}).get('path')),'Task workbook path required')
 candidates=a.get('candidates',[]);require(len(candidates)>=2,'At least two candidates required')
 ids=[x.get('id') for x in candidates];require(all(ids) and len(set(ids))==len(ids),'Unique candidate IDs required')
 require(selected.get('candidate_id') in ids,'Selected candidate must exist')
 for x in candidates:
  require(x.get('role')=='primary_contributor' and x.get('has_turret') is False,'All compared 1833 candidates must respect primary/non-turret constraints')
  require(x.get('has_pneumatics') is False,'Candidate must be non-pneumatic')
  for field in ['interfaces','physical_envelope','complexity_drivers','failure_modes']:require(bool(x.get(field)),x.get('id','?')+': missing '+field)
 scenarios=a.get('scenarios',[]);names={s.get('kind') for s in scenarios}
 require({'ordinary_partners','strong_partners','elite_defended'}<=names,'Ordinary, strong and elite defended scenarios required')
 for s in scenarios:
  require(bool(s.get('common_assumptions')),str(s.get('kind'))+': common assumptions required')
  inputs=s.get('inputs',[]);require(bool(inputs),str(s.get('kind'))+': model inputs required')
  for x in inputs:
   require(isinstance(x.get('value'),(int,float)) or isinstance(x.get('range'),list),str(s.get('kind'))+': numeric value or range required')
   require(bool(x.get('units')) and bool(x.get('provenance')),str(s.get('kind'))+': input units/provenance required')
  results=s.get('candidate_results',[]);require({x.get('candidate_id') for x in results}==set(ids),str(s.get('kind'))+': every candidate needs a result')
  for x in results:
   require(bool(x.get('timeline')) and bool(x.get('score_accounting')),str(s.get('kind'))+': timeline and score accounting required')
   require(bool(x.get('calculation_locator')),str(s.get('kind'))+': reproducible calculation locator required')
 require(len(a.get('capacity_trade_study',{}).get('options',[]))>=3,'At least three capacity/storage options required')
 for field in ['sensitivity_analysis','acceptance_requirements','decision_tests','corrections_and_open_questions','human_review_status']:require(bool(a.get(field)),'Missing '+field)
 for section,fields in {'solo_rp_analysis':['governing_rp_rules','objective_classification','owned_prerequisites','required_individual_output','margin_and_uncertainty','passive_partner_case','seeding_and_playoff_implications'],'validation_economics':['decision_uncertainty','cheapest_adequate_evidence','estimated_cost_and_schedule','result_that_changes_choice','stopping_rule']}.items():
  record=a.get(section,{})
  require(isinstance(record,dict),section+': structured record required')
  if isinstance(record,dict):
   for field in fields:require(bool(record.get(field)),section+': missing '+field)
 return {'structural_pass':not errors,'errors':errors,'scope':'Presence and explicit profile constraints only; quantities, simulations, sources and engineering credibility still require review'}
if __name__=='__main__':
 result=validate(json.loads(pathlib.Path(sys.argv[1]).read_text()));print(json.dumps(result,indent=2));sys.exit(1 if result['errors'] else 0)
