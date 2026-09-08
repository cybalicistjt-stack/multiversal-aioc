import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Vti10LifecycleTests(unittest.TestCase):
    def test_vti10_governed_start_or_later_lifecycle(self):
        cp = load_json("governance/ai/work-state/VTI-10-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")

        self.assertIn(cp["status"], {"in_progress", "completed_verified"})
        self.assertEqual(cp["application_baseline_sha"], "9bed9b190b1d78bbbce9e208c2daa792c9109466")

        if cp["status"] == "in_progress":
            self.assertEqual(backlog["current_item"], "VTI-10")
            self.assertEqual(cp["implementation_branch"], "integration/vti-10-additional-vtt-adapters-compatibility-matrix")
            self.assertTrue(cp["implementation_authority"])
            self.assertTrue(cp["branch_creation_authorized"])
            self.assertTrue(cp["acceptance_package_authorized"])
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-10")
            self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
            self.assertTrue(pointer["active_attempt"]["implementation_authority"])
            self.assertEqual(runtime["active_work"]["work_item"], "VTI-10")
            self.assertTrue(runtime["active_work"]["implementation_authority"])
            auth = authority["vti_10_authority"]
            self.assertTrue(auth["implementation_authority"])
            self.assertTrue(auth["branch_creation_authorized"])
            self.assertTrue(auth["acceptance_package_authorized"])
            if not cp["validation"]["acceptance_red"]:
                self.assertFalse(cp["production_mutation_authorized"])
                self.assertFalse(pointer["bounded_authority"]["production_mutation_authorized"])
                self.assertFalse(runtime["active_work"]["production_mutation_authorized"])
                self.assertFalse(auth["production_mutation_authorized"])
        else:
            self.assertTrue(cp["completed"])
            self.assertTrue(cp["authority_retired"])
            self.assertFalse(cp["implementation_authority"])
            self.assertFalse(cp["production_mutation_authorized"])
            self.assertTrue(authority["vti_10_authority"]["retired"])
            self.assertFalse(authority["vti_10_authority"]["implementation_authority"])

        for key in ("provider_activation_authorized", "tester_distribution_authorized", "release_or_deployment_authorized", "vti11_plus_authorized", "sgc01_plus_authorized"):
            self.assertFalse(cp["authority_boundary"][key])

if __name__ == "__main__":
    unittest.main()
