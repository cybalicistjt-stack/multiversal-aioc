import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp02AchievementDefinitionsRegistrationTests(unittest.TestCase):
    def test_alp02_remains_completed_while_successor_may_advance(self):
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
        self.assertEqual(checkpoint["convergence_control"]["owner_continue_count"], 2)
        self.assertEqual(checkpoint["convergence_control"]["execution_cycles"], 2)
        self.assertFalse(checkpoint["convergence_control"]["same_cycle_completed"])
        self.assertTrue(checkpoint["convergence_control"]["completed_within_two_cycles"])
        self.assertTrue(checkpoint["convergence_control"]["control_plane_incident"])
        self.assertEqual(checkpoint["convergence_control"]["application_feature_repair_cycles"], 0)
        self.assertEqual(checkpoint["convergence_control"]["repository_state_repair_cycles"], 3)
        self.assertEqual(checkpoint["convergence_control"]["validation_contract_repair_cycles"], 2)
        self.assertEqual(checkpoint["validation"]["final_green"]["historical_profile_fanout"], 0)

        self.assertIn(successor["status"], {"selected_not_started", "in_progress", "completed_verified"})
        self.assertEqual(successor["application_baseline_sha"], merge)

        completed_number = int(backlog["completed_through"].split("-")[1])
        self.assertGreaterEqual(completed_number, 2)
        alp02 = next(item for item in backlog["tranches"] if item["id"] == "ALP-02")
        alp03 = next(item for item in backlog["tranches"] if item["id"] == "ALP-03")
        self.assertEqual(alp02["status"], "completed_verified")
        self.assertFalse(alp02["implementation_authority"])
        self.assertEqual(alp03["status"], successor["status"])
        self.assertEqual(alp03["implementation_authority"], successor["implementation_authority"])

        if successor["status"] in {"selected_not_started", "in_progress"}:
            self.assertEqual(backlog["completed_through"], "ALP-02")
            self.assertEqual(backlog["current_item"], "ALP-03")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-03")
            self.assertEqual(pointer["active_attempt"]["status"], successor["status"])
            self.assertEqual(index["current"]["work_item_id"], "ALP-03")
            self.assertEqual(index["current"]["status"], successor["status"])
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-03")
            self.assertEqual(registry["active_planning_work"]["state"], successor["status"])
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-03")
            self.assertEqual(runtime["active_work"]["state"], successor["status"])
            self.assertEqual(runtime["application_repository"]["canonical_main"], merge)
        else:
            self.assertGreaterEqual(completed_number, 3)
            self.assertFalse(successor["implementation_authority"])
            self.assertTrue(successor.get("authority_retired", True))
            self.assertTrue(pointer["active_attempt"]["work_item_id"].startswith("ALP-"))
            self.assertTrue(index["current"]["work_item_id"].startswith("ALP-"))
            self.assertTrue(registry["active_planning_work"]["work_item"].startswith("ALP-"))
            self.assertTrue(runtime["active_work"]["work_item"].startswith("ALP-"))
            self.assertEqual(runtime["application_repository"]["canonical_main"], backlog["application_baseline_sha"])

        self.assertFalse(registry["alp_02_authority"]["implementation_authority"])
        self.assertTrue(registry["alp_02_authority"]["retired"])
        alp02_registry = next(item for item in registry["recently_completed_implementation_work"] if item["work_item_id"] == "ALP-02")
        self.assertEqual(alp02_registry["application_feature_repair_cycles"], 0)
        self.assertEqual(alp02_registry["repository_state_repair_cycles"], 3)
        self.assertEqual(alp02_registry["validation_contract_repair_cycles"], 2)

        for phrase in (
            "ALP-02 — Achievement Definitions, Criteria, Evidence, Scope & Provenance",
            "ALP-03 — Platform Onboarding & Mastery Milestones",
            "**COMPLETED_VERIFIED**",
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
