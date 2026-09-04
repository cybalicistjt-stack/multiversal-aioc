import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp01AchievementsLearningPracticeRegistrationTests(unittest.TestCase):
    def test_alp01_governed_start_is_registered_across_current_control_plane(self):
        baseline = "94b8dde9afdce249c873b22f0509406d77fdf099"
        branch = "integration/alp-01-authority-taxonomy"
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        checkpoint = load_json("governance/ai/work-state/ALP-01-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")

        self.assertEqual(checkpoint["status"], "in_progress")
        self.assertTrue(checkpoint["implementation_authority"])
        self.assertEqual(checkpoint["implementation_branch"], branch)
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-01")
        self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
        self.assertTrue(pointer["active_attempt"]["implementation_authority"])
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
        self.assertEqual(pointer["active_attempt"]["application_baseline_sha"], baseline)

        self.assertEqual(index["current"]["work_item_id"], "ALP-01")
        self.assertEqual(index["current"]["status"], "in_progress")
        self.assertTrue(index["current"]["implementation_authority"])
        self.assertEqual(index["current"]["implementation_branch"], branch)

        self.assertEqual(backlog["tranches"][0]["status"], "in_progress")
        self.assertTrue(backlog["tranches"][0]["implementation_authority"])
        self.assertEqual(backlog["tranches"][0]["implementation_branch"], branch)

        alp_authority = registry["alp_01_authority"]
        self.assertTrue(alp_authority["authority_crosswalk_authorized"])
        self.assertTrue(alp_authority["taxonomy_authorized"])
        self.assertTrue(alp_authority["classification_projection_authorized"])
        self.assertFalse(alp_authority["achievement_award_authorized"])
        self.assertFalse(alp_authority["reward_commit_authorized"])
        self.assertFalse(alp_authority["hidden_completion_inference_authorized"])
        self.assertFalse(alp_authority["universal_permission_gate_authorized"])
        self.assertFalse(alp_authority["durable_persistence_authorized"])
        self.assertFalse(alp_authority["migration_reserved"])

        self.assertEqual(runtime["active_work"]["work_item"], "ALP-01")
        self.assertEqual(runtime["active_work"]["role"], "active_implementation")
        self.assertEqual(runtime["application_repository"]["active_validation_family"], "ALP")
        self.assertEqual(runtime["application_repository"]["active_validation_family_state"], "ALP01_in_progress")

    def test_alp01_taxonomy_and_owner_boundaries_are_explicit(self):
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")
        checkpoint = load_json("governance/ai/work-state/ALP-01-attempt-001.json")

        expected_families = [
            "platform_learning_milestone",
            "campaign_achievement",
            "practice_training_marker",
            "project_learning_evidence",
            "recognition_record",
            "mechanical_reward_reference",
        ]
        self.assertEqual(checkpoint["governed_contract"]["taxonomy_families"], expected_families)
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


if __name__ == "__main__":
    unittest.main()
