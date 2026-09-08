import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Vti10TerminalCloseoutTests(unittest.TestCase):
    def test_vti10_terminal_evidence_and_vti11_selected_without_authority(self):
        vti10 = load_json("governance/ai/work-state/VTI-10-attempt-001.json")
        vti11 = load_json("governance/ai/work-state/VTI-11-attempt-001.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        authority = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        backlog = load_json("governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")

        self.assertEqual(vti10["status"], "completed_verified")
        self.assertTrue(vti10["completed"])
        self.assertTrue(vti10["authority_retired"])
        self.assertEqual(vti10["application_pr"], 439)
        self.assertEqual(vti10["application_merge_sha"], "145eee04181b9ed66cae887ea6830da111918c25")
        self.assertEqual(vti10["validation"]["final_green"]["head_sha"], "41df73d952bf106b65d260c980c07d8ad877bdab")
        self.assertEqual(vti10["validation"]["final_green"]["run_id"], 34183387667)
        self.assertEqual(vti10["validation"]["final_green"]["deterministic_receipt_sha256"], "08f29cea5babcc93b3f388cb71d99465286b3f720b78d85f340df560c43792ac")
        for key in ("implementation_authority", "branch_creation_authorized", "acceptance_package_authorized", "production_mutation_authorized"):
            self.assertFalse(vti10[key])

        self.assertEqual(vti11["work_item_id"], "VTI-11")
        self.assertEqual(vti11["title"], "Adventure / Campaign Package Export")
        self.assertEqual(vti11["status"], "selected_not_started")
        self.assertEqual(vti11["application_baseline_sha"], "145eee04181b9ed66cae887ea6830da111918c25")
        self.assertIsNone(vti11["implementation_branch"])
        for key in ("implementation_authority", "branch_creation_authorized", "acceptance_package_authorized", "production_mutation_authorized"):
            self.assertFalse(vti11[key])

        self.assertEqual(pointer["primary_attempt_id"], "VTI-11-attempt-001")
        self.assertEqual(pointer["active_attempt"]["work_item_id"], "VTI-11")
        self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
        self.assertFalse(pointer["bounded_authority"]["vti_implementation"])
        self.assertEqual(pointer["bounded_authority"]["vti_work_item"], "VTI-11")
        self.assertFalse(pointer["bounded_authority"]["acceptance_package_authorized"])
        self.assertFalse(pointer["bounded_authority"]["production_mutation_authorized"])

        self.assertEqual(backlog["completed_through"], "VTI-10")
        self.assertEqual(backlog["current_item"], "VTI-11")
        self.assertEqual(backlog["current_attempt"], "VTI-11-attempt-001")
        self.assertEqual(backlog["application_baseline_sha"], "145eee04181b9ed66cae887ea6830da111918c25")
        self.assertEqual(runtime["active_work"]["work_item"], "VTI-11")
        self.assertEqual(index["current"]["work_item_id"], "VTI-11")
        self.assertEqual(index["current"]["status"], "selected_not_started")

        self.assertTrue(authority["vti_10_authority"]["retired"])
        self.assertFalse(authority["vti_10_authority"]["implementation_authority"])
        self.assertTrue(authority["vti_11_authority"]["selected_not_started"])
        self.assertFalse(authority["vti_11_authority"]["implementation_authority"])
        self.assertFalse(authority["vti_11_authority"]["production_mutation_authorized"])

        planned = {row["program_id"]: row for row in index["planned_programs"]}
        self.assertFalse(planned["ARI"]["implementation_authority"])
        self.assertFalse(planned["SAA"]["implementation_authority"])
        deferred = {row["program_id"]: row for row in index["deferred_future_projects"]}
        self.assertFalse(deferred["P3D"]["implementation_authority"])
        self.assertFalse(deferred["P3D"]["automatic_activation"])


if __name__ == "__main__":
    unittest.main()
