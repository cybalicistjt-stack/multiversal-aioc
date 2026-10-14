from __future__ import annotations
import importlib.util, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def _load(n,r):
 p=ROOT/r;s=importlib.util.spec_from_file_location(n,p)
 if s is None or s.loader is None: raise RuntimeError(f"unable to load {r}")
 m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
CI=_load("ops4_ci_guard","scripts/ops4_ci_guard.py");EXEC=_load("ops4_execution_guard","scripts/ops4_execution_guard.py")
class Ops4CiGuardTests(unittest.TestCase):
 def green(self): return {"status":"green","kind":"focused_test","evidence":"changed package test passed"}
 def unavailable(self): return {"status":"unavailable","reason":"repository API available but executable checkout unavailable","attempted_capabilities":["local_checkout","package_test"]}
 def test_green(self): self.assertEqual(CI.validate_remote_request({"candidate_head":"a","preflight":self.green()}),[])
 def test_unavailable(self): self.assertEqual(CI.validate_remote_request({"candidate_head":"a","preflight":self.unavailable()}),[])
 def test_skipped(self): self.assertIn(CI.PREFLIGHT_SKIPPED,CI.validate_remote_request({"candidate_head":"a","preflight":{"status":"skipped"}}))
 def test_unproved_unavailable(self): self.assertIn(CI.PREFLIGHT_UNAVAILABLE_UNPROVED,CI.validate_remote_request({"candidate_head":"a","preflight":{"status":"unavailable","reason":"x"}}))
 def test_product_same_head_retry_blocked(self): self.assertIn(CI.SAME_HEAD_PRODUCT_RETRY,CI.validate_remote_request({"candidate_head":"a","preflight":self.green(),"prior_remote":{"candidate_head":"a","status":"completed","conclusion":"failure","failure_class":"product"}}))
 def test_changed_head_requires_repair(self):
  r={"candidate_head":"b","preflight":self.green(),"prior_remote":{"candidate_head":"a","status":"completed","conclusion":"failure","failure_class":"configuration"}}
  self.assertIn(CI.REPAIR_EVIDENCE_REQUIRED,CI.validate_remote_request(r));self.assertEqual(CI.validate_remote_request({**r,"repair_evidence":"fixed first material failure"}),[])
 def test_duplicate_active(self): self.assertIn(CI.DUPLICATE_REMOTE_VALIDATION,CI.validate_remote_request({"candidate_head":"a","preflight":self.green(),"prior_remote":{"candidate_head":"a","status":"in_progress","conclusion":""}}))
 def test_infra_budget(self):
  r={"candidate_head":"a","preflight":self.green(),"prior_remote":{"candidate_head":"a","status":"completed","conclusion":"failure","failure_class":"infrastructure_transient","same_head_infra_retry_count":0},"infra_retry_evidence":"runner lost connection"}
  self.assertEqual(CI.validate_remote_request(r),[]);r["prior_remote"]["same_head_infra_retry_count"]=1;self.assertIn(CI.INFRA_RETRY_EXHAUSTED,CI.validate_remote_request(r))
 def test_flake_budget(self): self.assertIn(CI.UNRESOLVED_FLAKE,CI.validate_remote_request({"candidate_head":"a","preflight":self.green(),"prior_remote":{"candidate_head":"a","status":"completed","conclusion":"failure","failure_class":"flaky_unknown","same_head_flake_retry_count":1},"flake_classification_evidence":"alternated"}))
 def test_real_boundary_needs_independent_evidence(self):
  self.assertIn(CI.MOCK_ONLY_REAL_BOUNDARY,CI.validate_acceptance_evidence(boundary_kind="network",evidence_kinds=["agent_authored_unit","mock"]));self.assertEqual(CI.validate_acceptance_evidence(boundary_kind="network",evidence_kinds=["real_integration"]),[])
 def test_draft_cannot_admit_full_acceptance(self):
  r={"candidate_head":"new","preflight":self.green(),"pr_draft":True}
  self.assertIn(CI.DRAFT_ACCEPTANCE,CI.validate_remote_request(r))
  self.assertEqual(CI.validate_remote_request({**r,"validation_mode":"preflight"}),[])
 def test_new_head_cannot_supersede_active_validation(self):
  r={"candidate_head":"new","preflight":self.green(),"prior_remote":{"candidate_head":"old","status":"queued","conclusion":""}}
  self.assertIn(CI.ACTIVE_HEAD_SUPERSEDED,CI.validate_remote_request(r))
 def test_two_cycle_selector_drift_and_unpermitted_terminal_response(self):
  current={"lanes":{"mtlc":{"selected_work_item":"MTLC-02","attempt_id":"MTLC-02-attempt-001","state":"selected_not_started","implementation_branch":None,"implementation_authority":False}}}
  work={"work_item_id":"MTLC-02","attempt_id":"MTLC-02-attempt-001","status":"selected_not_started","implementation_branch":None,"implementation_authority":False}
  lane={"selected_work_item":"MTLC-02","attempt_id":"MTLC-02-attempt-001","execution_status":"in_progress","implementation_branch":"work/mtlc-02-private-table-onboarding","terminal":False}
  self.assertIn("OPS4.LANE_PROJECTION_DRIFT",EXEC.validate_lane_projection(current,work,lane,"mtlc"))
  self.assertIn(EXEC.NONTERMINAL,EXEC.validate_lane_terminal_response(lane))
  current["lanes"]["mtlc"].update({"state":"in_progress","implementation_branch":lane["implementation_branch"],"implementation_authority":True})
  work.update({"status":"in_progress","implementation_branch":lane["implementation_branch"],"implementation_authority":True})
  self.assertEqual(EXEC.validate_lane_projection(current,work,lane,"mtlc"),[])
 def test_legacy_violation_codes_normalize(self):
  c={"status":"completed_verified","execution_guard":{"continue_turns":4,"stall_nudges":2,"material_progress_seq":2,"progress_at_last_owner_command":1,"no_progress_cycles":0,"last_material_progress":{"seq":2,"kind":"repair","evidence":"fixed"},"active_stall":False,"terminal_response_allowed":True,"stop_reason":{"kind":"completed","evidence":"verified"}},"execution_conformance":{"status":"conforming","policy_violations":["OPS3.MULTI_CONTINUE_UNRECORDED","OPS3.STALL_NUDGE_UNRECORDED"]}}
  self.assertEqual(EXEC.validate_execution_conformance(c),[])
if __name__=="__main__": unittest.main()
