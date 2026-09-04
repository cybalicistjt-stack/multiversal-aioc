import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp02AchievementDefinitionsRegistrationTests(unittest.TestCase):
    def test_alp02_is_completed_and_alp03_is_selected_only(self):
        merge = "050356f7578856de5931917a60efe8af91def1bd"
        checkpoint = load_json("governance/ai/work-state/ALP-02-attempt-001.json")
        successor = load_json("governance/ai/work-state/ALP-03-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        closeout = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ALP02_CLOSEOUT_2026-09-04.md")

        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["authority_retired"])
        self.assertEqual(checkpoint["application_pr"], 408)
        self.assertEqual(checkpoint["application_merge_sha"], merge)
        self.assertTrue(checkpoint["convergence_control"]["same_cycle_completed"])
        self.assertEqual(checkpoint["convergence_control"]["application_feature_repair_cycles"], 0)
        self.assertEqual(checkpoint["validation"]["final_green"]["historical_profile_fanout"], 0)

        self.assertEqual(successor["status"], "selected_not_started")
        self.assertFalse(successor["implementation_authority"])
        self.assertIsNone(successor["implementation_branch"])
        self.assertEqual(successor["application_baseline_sha"], merge)

        self.assertEqual(backlog["completed_through"], "ALP-02")
        self.assertEqual(backlog["current_item"], "ALP-03")
        alp02 = next(item for item in backlog["tranches"] if item["id"] == "ALP-02")
        alp03 = next(item for item in backlog["tranches"] if item["id"] == "ALP-03")
        self.assertEqual(alp02["status"], "completed_verified")
        self.assertFalse(alp02["implementation_authority"])
        self.assertEqual(alp03["status"], "selected_not_started")
        self.assertFalse(alp03["implementation_authority"])
        self.assertIsNone(alp03["implementation_branch"])

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-03")
        self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
        self.assertFalse(pointer["active_attempt"]["implementation_authority"])
        self.assertIsNone(pointer["active_attempt"]["implementation_branch"])
        self.assertFalse(pointer["bounded_authority"]["alp_implementation"])

        self.assertEqual(index["current"]["work_item_id"], "ALP-03")
        self.assertEqual(index["current"]["status"], "selected_not_started")
        self.assertFalse(index["current"]["implementation_authority"])

        self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-03")
        self.assertEqual(registry["active_planning_work"]["state"], "selected_not_started")
        self.assertFalse(registry["alp_02_authority"]["implementation_authority"])
        self.assertTrue(registry["alp_02_authority"]["retired"])
        self.assertTrue(registry["alp_03_authority"]["selected_not_started"])
        self.assertFalse(registry["alp_03_authority"]["implementation_authority"])

        self.assertEqual(runtime["application_repository"]["canonical_main"], merge)
        self.assertEqual(runtime["active_work"]["work_item"], "ALP-03")
        self.assertEqual(runtime["active_work"]["state"], "selected_not_started")
        self.assertFalse(runtime["active_work"]["implementation_authority"])

        for phrase in (
            "ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance — **COMPLETED_VERIFIED**",
            "ALP-03 — Platform Onboarding & Mastery Milestones — **SELECTED_NOT_STARTED**",
            "unknown",
            "does **not** award achievements",
            "migration `0022`",
        ):
            self.assertIn(phrase, program)

        for value in (
            "f86c09aae3af19e7063bc6d0b41f45f6d95c1b45",
            "f4404793c098b1e382916fc414dcbc47a30f72a2c3922e78b6c9fccd0493015b",
            "3e5d47edda7a28f25f6f282a0a4d770570d46280",
            "84d6bfd06ce885887e06bcae1b057ac2ee6dc0a4865941956a2fdf1c5bfac97c",
            merge,
        ):
            self.assertIn(value, closeout)

    def test_alp01_remains_frozen_predecessor(self):
        checkpoint = load_json("governance/ai/work-state/ALP-01-attempt-001.json")
        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertEqual(checkpoint["application_merge_sha"], "c3ff8adb2311d1c59f3288a82593b358e3d47960")


if __name__ == "__main__":
    unittest.main()
