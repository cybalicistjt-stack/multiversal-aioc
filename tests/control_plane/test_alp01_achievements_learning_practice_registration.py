import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp01AchievementsLearningPracticeRegistrationTests(unittest.TestCase):
    def test_alp01_completion_and_alp02_selection_are_registered_across_control_plane(self):
        merge = "c3ff8adb2311d1c59f3288a82593b358e3d47960"
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        checkpoint = load_json("governance/ai/work-state/ALP-01-attempt-001.json")
        successor = load_json("governance/ai/work-state/ALP-02-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")

        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["authority_retired"])
        self.assertEqual(checkpoint["application_merge_sha"], merge)
        self.assertEqual(checkpoint["application_pr"], 407)
        self.assertTrue(checkpoint["convergence_control"]["same_cycle_completed"])
        self.assertEqual(checkpoint["convergence_control"]["application_feature_repair_cycles"], 0)
        self.assertEqual(checkpoint["validation"]["final_green"]["historical_profile_fanout"], 0)

        self.assertEqual(successor["status"], "selected_not_started")
        self.assertFalse(successor["implementation_authority"])
        self.assertIsNone(successor["implementation_branch"])
        self.assertEqual(successor["application_baseline_sha"], merge)

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-02")
        self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
        self.assertFalse(pointer["active_attempt"]["implementation_authority"])
        self.assertIsNone(pointer["active_attempt"]["implementation_branch"])
        self.assertEqual(pointer["active_attempt"]["application_baseline_sha"], merge)

        self.assertEqual(index["current"]["work_item_id"], "ALP-02")
        self.assertEqual(index["current"]["status"], "selected_not_started")
        self.assertFalse(index["current"]["implementation_authority"])

        self.assertEqual(backlog["completed_through"], "ALP-01")
        self.assertEqual(backlog["tranches"][0]["status"], "completed_verified")
        self.assertFalse(backlog["tranches"][0]["implementation_authority"])
        self.assertEqual(backlog["tranches"][1]["status"], "selected_not_started")
        self.assertFalse(backlog["tranches"][1]["implementation_authority"])
        self.assertIsNone(backlog["tranches"][1]["implementation_branch"])

        self.assertFalse(registry["alp_01_authority"]["implementation_authority"])
        self.assertTrue(registry["alp_01_authority"]["retired"])
        self.assertFalse(registry["alp_02_authority"]["implementation_authority"])
        self.assertTrue(registry["alp_02_authority"]["selected_not_started"])

        self.assertEqual(runtime["active_work"]["work_item"], "ALP-02")
        self.assertEqual(runtime["active_work"]["role"], "selected_not_started")
        self.assertFalse(runtime["active_work"]["implementation_authority"])
        self.assertEqual(runtime["application_repository"]["canonical_main"], merge)
        self.assertEqual(runtime["application_repository"]["active_validation_family"], "ALP")
        self.assertEqual(runtime["application_repository"]["active_validation_family_state"], "ALP02_selected_not_started")

    def test_alp01_taxonomy_boundaries_and_validation_evidence_are_preserved(self):
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")
        checkpoint = load_json("governance/ai/work-state/ALP-01-attempt-001.json")
        closeout = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ALP01_CLOSEOUT_2026-09-04.md")

        expected_families = [
            "platform_learning_milestone",
            "campaign_achievement",
            "practice_training_marker",
            "project_learning_evidence",
            "recognition_record",
            "mechanical_reward_reference",
        ]
        self.assertEqual(checkpoint["completed_contract"]["taxonomy_families"], expected_families)
        for family in expected_families:
            self.assertIn(family, program)

        for phrase in (
            "not universal permission",
            "Reward/Progression/Reputation/Faction",
            "hidden completion",
            "Diegetic practice remains optional",
            "no durable persistence",
        ):
            self.assertIn(phrase, program)

        for value in (
            "bf331f7c02e097306bf8a7e6704bcea2b4dd184d",
            "edfc93fe2e4ff5e5598099683975d1c2378ea2614995b919f4b0fcc5c6e5490b",
            "ea637d3e84d0722c4a190f4d12b856c8891a6e07",
            "81509fda2166f4c34058a14184dadc661fc531e6a92f4dbc3f717ae4af3cf9de",
            "c3ff8adb2311d1c59f3288a82593b358e3d47960",
        ):
            self.assertIn(value, closeout)


if __name__ == "__main__":
    unittest.main()
