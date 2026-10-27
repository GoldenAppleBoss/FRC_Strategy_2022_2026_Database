"""Synthetic structural checks, not robot simulations or measured agent results."""
import copy,unittest
from validate_design_review import validate
def fixture():
 ids=['A','B']
 return {'team':1833,'manual_revision':'SYNTHETIC TEST ONLY','manual_source':'synthetic fixture','constraints':{'primary_contributor':True,'turret_allowed':False,'pneumatics_allowed':False},'selected_architecture':{'candidate_id':'A','role':'primary_contributor','has_turret':False,'has_pneumatics':False},'task_workbook':{'path':'synthetic.xlsx','worksheet_count':1},'candidates':[{'id':i,'role':'primary_contributor','has_turret':False,'has_pneumatics':False,'interfaces':['synthetic'],'physical_envelope':{'test':True},'complexity_drivers':['synthetic'],'failure_modes':['synthetic']} for i in ids],'scenarios':[{'kind':s,'common_assumptions':['synthetic'],'inputs':[{'name':'synthetic time','value':1,'units':'s','provenance':'synthetic test'}],'candidate_results':[{'candidate_id':i,'timeline':[{'test':True}],'score_accounting':{'test':True},'calculation_locator':'synthetic'} for i in ids]} for s in ['ordinary_partners','strong_partners','elite_defended']],'capacity_trade_study':{'options':[1,2,3]},'sensitivity_analysis':['synthetic'],'acceptance_requirements':['synthetic'],'decision_tests':['synthetic'],'corrections_and_open_questions':['synthetic'],'human_review_status':'synthetic','solo_rp_analysis':{k:'synthetic' for k in ['governing_rp_rules','objective_classification','owned_prerequisites','required_individual_output','margin_and_uncertainty','passive_partner_case','seeding_and_playoff_implications']},'validation_economics':{k:'synthetic' for k in ['decision_uncertainty','cheapest_adequate_evidence','estimated_cost_and_schedule','result_that_changes_choice','stopping_rule']}}
class ReviewTests(unittest.TestCase):
 def test_complete_structure(self):self.assertTrue(validate(fixture())['structural_pass'])
 def test_support_rejected(self):
  a=fixture();a['selected_architecture']['role']='support';self.assertFalse(validate(a)['structural_pass'])
 def test_turret_rejected(self):
  a=fixture();a['selected_architecture']['has_turret']=True;self.assertFalse(validate(a)['structural_pass'])
 def test_candidate_turret_rejected(self):
  a=fixture();a['candidates'][1]['has_turret']=True;self.assertFalse(validate(a)['structural_pass'])
 def test_missing_scenario_rejected(self):
  a=fixture();a['scenarios'].pop();self.assertFalse(validate(a)['structural_pass'])
 def test_unfair_candidate_coverage_rejected(self):
  a=fixture();a['scenarios'][0]['candidate_results'].pop();self.assertFalse(validate(a)['structural_pass'])
 def test_missing_input_provenance_rejected(self):
  a=fixture();a['scenarios'][0]['inputs'][0].pop('provenance');self.assertFalse(validate(a)['structural_pass'])
 def test_capacity_threshold_not_enough(self):
  a=fixture();a['capacity_trade_study']['options']=[100];self.assertFalse(validate(a)['structural_pass'])
 def test_second_sheet_rejected(self):
  a=fixture();a['task_workbook']['worksheet_count']=2;self.assertFalse(validate(a)['structural_pass'])
 def test_empty_rejected(self):self.assertFalse(validate({})['structural_pass'])
 def test_solo_rp_analysis_required(self):
  a=fixture();a.pop('solo_rp_analysis');self.assertFalse(validate(a)['structural_pass'])
 def test_validation_cost_required(self):
  a=fixture();a['validation_economics'].pop('estimated_cost_and_schedule');self.assertFalse(validate(a)['structural_pass'])
 def test_pneumatics_rejected(self):
  a=fixture();a['selected_architecture']['has_pneumatics']=True;self.assertFalse(validate(a)['structural_pass'])
if __name__=='__main__':unittest.main()
