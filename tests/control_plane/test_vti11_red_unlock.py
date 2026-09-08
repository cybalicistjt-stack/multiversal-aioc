import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Vti11RedUnlockTests(unittest.TestCase):
    def test_matching_red_opens_only_bounded_vti11_production(self):
        cp = load_json("governance/ai/work-state/VTI-11-attempt-001.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        roadmap = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        red = cp["validation"]["acceptance_red"]
        self.assertIn(cp["status"], {"in_progress", "completed_verified"})
        self.assertEqual(cp["application_pr"], 440)
        self.assertEqual(red["head_sha"], "8c2f75144404d4fef558a4383b081621282a9a55")
        self.assertEqual(red["run_id"], 34206133589)
        self.assertEqual(red["repository_health_job"], 101995926174)
        self.assertEqual(red["linux_job"], 101995973396)
        self.assertEqual(red["windows_job"], 101995973371)
        self.assertEqual(red["deterministic_compare_job"], 101996191118)
        self.assertEqual(red["deterministic_receipt_sha256"], "ac550c382fa35df15d600a938f65228078c706a33592200320b19cd1952709b3")
        self.assertEqual(red["failure_stage"], "vti11-invariants")
        self.assertEqual(red["failure_reason"], "production contract intentionally absent")
        self.assertTrue(red["matching_red_observed"])
        self.assertTrue(red["raw_evidence_confirmed"])
        self.assertEqual(red["historical_profile_fanout"], 0)

        if cp["status"] == "in_progress":
            self.assertTrue(cp["production_mutation_authorized"])
            self.assertTrue(pointer["bounded_authority"]["production_mutation_authorized"])
            self.assertTrue(pointer["bounded_authority"]["matching_red_observed"])
            self.assertTrue(roadmap["current"]["production_mutation_authorized"])
            self.assertTrue(roadmap["current"]["matching_red_observed"])
            self.assertTrue(authority["vti_11_authority"]["production_mutation_authorized"])
            self.assertTrue(authority["vti_11_authority"]["matching_red_observed"])
            self.assertTrue(backlog["active_contract"]["production_mutation_authorized"])
            self.assertTrue(backlog["active_contract"]["matching_red_observed"])
            self.assertTrue(runtime["active_work"]["production_mutation_authorized"])
            self.assertTrue(runtime["active_work"]["matching_red_observed"])
        else:
            self.assertTrue(cp["completed"])
            self.assertTrue(cp["authority_retired"])
            self.assertFalse(cp["production_mutation_authorized"])
            self.assertTrue(authority["vti_11_authority"]["retired"])
            self.assertFalse(authority["vti_11_authority"]["production_mutation_authorized"])
            self.assertTrue(authority["vti_11_authority"]["matching_red_observed"])

        for key in ("vti12_plus_authorized", "sgc01_plus_authorized", "provider_activation_authorized", "tester_distribution_authorized", "release_or_deployment_authorized"):
            self.assertFalse(cp["authority_boundary"][key])
        for planned in roadmap["planned_programs"]:
            self.assertFalse(planned["implementation_authority"])
        for deferred in roadmap["deferred_future_projects"]:
            self.assertFalse(deferred["implementation_authority"])
            self.assertFalse(deferred["automatic_activation"])

if __name__ == "__main__":
    unittest.main()
