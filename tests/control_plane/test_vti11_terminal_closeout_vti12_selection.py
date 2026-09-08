import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Vti11TerminalCloseoutTests(unittest.TestCase):
    def test_vti11_terminal_evidence_and_vti12_successor_lifecycle(self):
        vti11 = load_json("governance/ai/work-state/VTI-11-attempt-001.json")
        vti12 = load_json("governance/ai/work-state/VTI-12-attempt-001.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")

        self.assertEqual(vti11["status"], "completed_verified")
        self.assertTrue(vti11["completed"])
        self.assertTrue(vti11["authority_retired"])
        self.assertEqual(vti11["application_pr"], 440)
        self.assertEqual(vti11["application_merge_sha"], "1c092252aedbc274058222451fad2401e1a3aa39")
        green = vti11["validation"]["final_green"]
        self.assertEqual(green["head_sha"], "ebc5f0265799788ce2f3c5b2b9da5da1b2da3d90")
        self.assertEqual(green["run_id"], 34213605901)
        self.assertEqual(green["repository_health_job"], 102020072033)
        self.assertEqual(green["linux_job"], 102020117401)
        self.assertEqual(green["windows_job"], 102020117411)
        self.assertEqual(green["deterministic_compare_job"], 102020518385)
        self.assertEqual(green["deterministic_receipt_sha256"], "07fc593e61d3c4f8e327fcda4549bbfafa3fa78cae8830bd24c9fa64889ec40b")
        self.assertEqual(green["historical_profile_fanout"], 0)
        for key in ("implementation_authority", "branch_creation_authorized", "acceptance_package_authorized", "production_mutation_authorized"):
            self.assertFalse(vti11[key])

        self.assertEqual(vti12["work_item_id"], "VTI-12")
        self.assertEqual(vti12["title"], "Integrated Cross-VTT Golden Proof")
        self.assertIn(vti12["status"], {"selected_not_started", "in_progress", "completed_verified"})
        self.assertEqual(vti12["application_baseline_sha"], "1c092252aedbc274058222451fad2401e1a3aa39")
        self.assertTrue(authority["vti_11_authority"]["retired"])
        self.assertFalse(authority["vti_11_authority"]["implementation_authority"])
        self.assertFalse(authority["vti_11_authority"]["production_mutation_authorized"])

        if vti12["status"] == "selected_not_started":
            self.assertIsNone(vti12["implementation_branch"])
            for key in ("implementation_authority", "branch_creation_authorized", "acceptance_package_authorized", "production_mutation_authorized"):
                self.assertFalse(vti12[key])
            self.assertEqual(pointer["primary_attempt_id"], "VTI-12-attempt-001")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-12")
            self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
            self.assertFalse(pointer["bounded_authority"]["vti_implementation"])
            self.assertEqual(backlog["completed_through"], "VTI-11")
            self.assertEqual(backlog["current_item"], "VTI-12")
            self.assertEqual(runtime["active_work"]["work_item"], "VTI-12")
            self.assertEqual(index["current"]["work_item_id"], "VTI-12")
            self.assertEqual(index["current"]["status"], "selected_not_started")
            self.assertTrue(authority["vti_12_authority"]["selected_not_started"])
            self.assertFalse(authority["vti_12_authority"]["implementation_authority"])
        elif vti12["status"] == "in_progress":
            self.assertTrue(vti12["implementation_authority"])
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-12")
            self.assertEqual(backlog["current_item"], "VTI-12")
            self.assertEqual(runtime["active_work"]["work_item"], "VTI-12")
            self.assertEqual(index["current"]["work_item_id"], "VTI-12")
        else:
            self.assertTrue(vti12["completed"])
            self.assertTrue(vti12["authority_retired"])

        planned = {row["program_id"]: row for row in index["planned_programs"]}
        self.assertFalse(planned["ARI"]["implementation_authority"])
        self.assertFalse(planned["SAA"]["implementation_authority"])
        deferred = {row["program_id"]: row for row in index["deferred_future_projects"]}
        self.assertFalse(deferred["P3D"]["implementation_authority"])
        self.assertFalse(deferred["P3D"]["automatic_activation"])


if __name__ == "__main__":
    unittest.main()
