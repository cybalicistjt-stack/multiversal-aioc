import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp02AchievementDefinitionsRegistrationTests(unittest.TestCase):
    def test_alp02_governed_start_is_current_and_red_gated(self):
        checkpoint = load_json("governance/ai/work-state/ALP-02-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")

        branch = "integration/alp-02-achievement-definitions-criteria-evidence-scope-provenance"
        baseline = "c3ff8adb2311d1c59f3288a82593b358e3d47960"

        self.assertEqual(checkpoint["status"], "in_progress")
        self.assertTrue(checkpoint["implementation_authority"])
        self.assertEqual(checkpoint["implementation_branch"], branch)
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertFalse(checkpoint["acceptance_gate"]["production_mutation_authorized"])
        self.assertFalse(checkpoint["acceptance_gate"]["red_observed"])

        alp02 = next(item for item in backlog["tranches"] if item["id"] == "ALP-02")
        self.assertEqual(alp02["status"], "in_progress")
        self.assertTrue(alp02["implementation_authority"])
        self.assertEqual(alp02["implementation_branch"], branch)
        self.assertEqual(backlog["completed_through"], "ALP-01")

        self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-02")
        self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
        self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
        self.assertTrue(pointer["active_attempt"]["implementation_authority"])
        self.assertFalse(pointer["bounded_authority"]["production_mutation_authorized"])

        self.assertEqual(index["current"]["work_item_id"], "ALP-02")
        self.assertEqual(index["current"]["status"], "in_progress")
        self.assertTrue(index["current"]["implementation_authority"])
        self.assertFalse(index["current"]["production_mutation_authorized"])

        self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-02")
        self.assertEqual(registry["active_planning_work"]["state"], "in_progress")
        self.assertTrue(registry["alp_02_authority"]["implementation_authority"])
        self.assertFalse(registry["alp_02_authority"]["production_mutation_authorized"])
        self.assertFalse(registry["alp_02_authority"]["achievement_award_authorized"])
        self.assertFalse(registry["alp_02_authority"]["hidden_evidence_inference_authorized"])

        self.assertEqual(runtime["active_work"]["work_item"], "ALP-02")
        self.assertEqual(runtime["active_work"]["state"], "in_progress")
        self.assertFalse(runtime["active_work"]["production_mutation_authorized"])

        for phrase in (
            "Achievement Definitions, Criteria, Evidence, Scope & Provenance",
            "unknown",
            "does **not** award achievements",
            "migration `0022`",
            "ALP-03+",
        ):
            self.assertIn(phrase, program)

    def test_alp01_remains_frozen_predecessor(self):
        checkpoint = load_json("governance/ai/work-state/ALP-01-attempt-001.json")
        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertEqual(checkpoint["application_merge_sha"], "c3ff8adb2311d1c59f3288a82593b358e3d47960")


if __name__ == "__main__":
    unittest.main()
