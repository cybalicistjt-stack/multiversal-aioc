import json,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class ExecutionProfileAuthorityTests(unittest.TestCase):
 def test_profile_is_canonical_and_current(self):
  p=json.loads((ROOT/"governance/ai/runtime/EXECUTION_PROFILE.json").read_text());self.assertEqual(p["status"],"CURRENT");self.assertEqual(p["service_objective"]["ordinary_tranche_single_continue_target_percent"],100);self.assertEqual(p["service_objective"]["max_execution_cycles_without_genuine_blocker"],1);self.assertEqual(p["service_objective"]["unrelated_historical_validation_jobs_target"],0)
 def test_health_validator_projection_matches_profile(self):
  r=subprocess.run([sys.executable,"scripts/sync_execution_profile.py","--root",str(ROOT),"--check"],cwd=ROOT,text=True,capture_output=True);self.assertEqual(r.returncode,0,r.stdout+r.stderr)
 def test_convergence_validator_reads_profile(self):
  t=(ROOT/"scripts/validate_execution_convergence.py").read_text();self.assertIn('PROFILE_PATH="governance/ai/runtime/EXECUTION_PROFILE.json"',t);self.assertNotIn('single-continue target must remain 100',t)
 def test_preflight_references_profile(self):self.assertEqual(json.loads((ROOT/"governance/ai/runtime/FAMILY_EXECUTION_PREFLIGHT.json").read_text())["execution_profile"],"governance/ai/runtime/EXECUTION_PROFILE.json")
 def test_expired_or_trial_limited_tools_cannot_be_required(self):
  p=json.loads((ROOT/"governance/ai/runtime/EXECUTION_PROFILE.json").read_text());guard=p["external_tool_access"];self.assertEqual(guard["required_dependency_status"],"verified_current_for_intended_workflow");self.assertFalse(guard["trial_expired_or_inaccessible_tools_may_be_required"]);self.assertEqual(set(guard["known_not_allowed_as_required_development_dependencies"]),{"YepCode","Basic Memory"});self.assertIn("Do not silently assume access",guard["fallback_rule"])
if __name__=="__main__":unittest.main()
