import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp05DiegeticPracticeSpacesRegistrationTests(unittest.TestCase):
    def test_alp05_governed_start_or_closeout_is_consistent(self):
        baseline = "788a8025caf8046edfeddcbf238cce972a4c5378"
        checkpoint = load_json("governance/ai/work-state/ALP-05-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "ALP-05")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertIn(checkpoint["status"], {"in_progress", "completed_verified"})
        alp05 = next(item for item in backlog["tranches"] if item["id"] == "ALP-05")
        self.assertEqual(alp05["status"], checkpoint["status"])

        if checkpoint["status"] == "in_progress":
            branch = "integration/alp-05-diegetic-practice-spaces-training-scenes-simulations"
            self.assertTrue(checkpoint["implementation_authority"])
            self.assertEqual(checkpoint["implementation_branch"], branch)
            self.assertTrue(checkpoint["branch_creation_authorized"])
            self.assertTrue(checkpoint["acceptance_package_authorized"])
            self.assertFalse(checkpoint["production_mutation_authorized"])
            self.assertEqual(backlog["completed_through"], "ALP-04")
            self.assertEqual(backlog["current_item"], "ALP-05")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-05")
            self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
            self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
            self.assertTrue(pointer["active_attempt"]["implementation_authority"])
            self.assertFalse(pointer["bounded_authority"]["production_mutation_authorized"])
            self.assertEqual(registry["active_planning_work"]["state"], "in_progress")
            self.assertEqual(index["current"]["status"], "in_progress")
            self.assertEqual(runtime["active_work"]["state"], "in_progress")
        else:
            self.assertFalse(checkpoint["implementation_authority"])
            self.assertTrue(checkpoint["authority_retired"])
            self.assertEqual(backlog["completed_through"], "ALP-05")
            self.assertEqual(backlog["current_item"], "ALP-06")

        for phrase in (
            "ALP-05 — Diegetic Practice Spaces, Training Scenes & Simulations",
            "optional diegetic practice spaces",
            "training scenes",
            "simulations",
            "Practice participation remains optional",
            "Character Progression",
            "Projects",
            "World/Scene",
            "GCL",
            "ISE",
            "MAL",
            "migration `0022`",
        ):
            self.assertIn(phrase, program)

    def test_alp05_scope_keeps_practice_non_mutating_and_optional(self):
        checkpoint = load_json("governance/ai/work-state/ALP-05-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        boundary = checkpoint["authority_boundary"]
        self.assertIn("explicit practice-space identity, kind, scope, author and provenance", scope["authorized"])
        self.assertIn("optional participation policy with no universal gating", scope["authorized"])
        self.assertIn("read-only links to Character Progression, Projects, World/Scene, GCL, ISE and MAL owner objects", scope["authorized"])
        self.assertIn("automatic XP, advancement, capability or reward grants from practice participation", scope["not_authorized"])
        self.assertIn("hidden or unauthorized evidence inference", scope["not_authorized"])
        self.assertIn("durable ALP persistence or migration 0022", scope["not_authorized"])
        self.assertFalse(boundary["alp06_plus_authorized"])
        self.assertFalse(boundary["tester_distribution_authorized"])
        self.assertFalse(boundary["release_or_deployment_authorized"])


if __name__ == "__main__":
    unittest.main()
