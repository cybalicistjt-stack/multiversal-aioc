import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Vti11LifecycleTests(unittest.TestCase):
    def test_vti11_governed_start_or_later_lifecycle(self):
        cp = load_json("governance/ai/work-state/VTI-11-attempt-001.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        roadmap = load_json("governance/ai/runtime/ROADMAP_INDEX.json")

        self.assertIn(cp["status"], {"in_progress", "completed_verified"})
        self.assertEqual(cp["application_baseline_sha"], "145eee04181b9ed66cae887ea6830da111918c25")
        self.assertEqual(backlog["current_item"] if cp["status"] == "in_progress" else backlog["completed_through"], "VTI-11")

        if cp["status"] == "in_progress":
            branch = "integration/vti-11-adventure-campaign-package-export"
            self.assertEqual(cp["implementation_branch"], branch)
            self.assertTrue(cp["implementation_authority"])
            self.assertTrue(cp["branch_creation_authorized"])
            self.assertTrue(cp["acceptance_package_authorized"])

            red = cp.get("validation", {}).get("acceptance_red")
            production_expected = bool(red and red.get("matching_red_observed"))
            self.assertEqual(cp["production_mutation_authorized"], production_expected)

            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-11")
            self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
            self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
            self.assertTrue(pointer["active_attempt"]["implementation_authority"])
            self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], production_expected)

            self.assertEqual(runtime["active_work"]["work_item"], "VTI-11")
            self.assertEqual(runtime["active_work"]["implementation_branch"], branch)
            self.assertTrue(runtime["active_work"]["implementation_authority"])
            self.assertEqual(runtime["active_work"]["production_mutation_authorized"], production_expected)

            self.assertEqual(roadmap["current"]["work_item_id"], "VTI-11")
            self.assertEqual(roadmap["current"]["status"], "in_progress")
            self.assertEqual(roadmap["current"]["implementation_branch"], branch)
            self.assertTrue(roadmap["current"]["implementation_authority"])
            self.assertEqual(roadmap["current"]["production_mutation_authorized"], production_expected)

            auth = authority["vti_11_authority"]
            self.assertTrue(auth["implementation_authority"])
            self.assertTrue(auth["branch_creation_authorized"])
            self.assertTrue(auth["acceptance_package_authorized"])
            self.assertEqual(auth["production_mutation_authorized"], production_expected)

        for key in ("vti12_plus_authorized", "sgc01_plus_authorized", "provider_activation_authorized", "tester_distribution_authorized", "release_or_deployment_authorized"):
            self.assertFalse(cp["authority_boundary"][key])


if __name__ == "__main__":
    unittest.main()
