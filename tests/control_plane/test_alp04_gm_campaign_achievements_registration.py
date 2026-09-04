import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp04GmCampaignAchievementsRegistrationTests(unittest.TestCase):
    def test_alp04_governed_lifecycle_is_consistent(self):
        baseline = "025f653f65be5ea8ccae1d04f9591e146c3d8797"
        branch = "integration/alp-04-gm-campaign-achievements-titles-reputation-reward-links"
        checkpoint = load_json("governance/ai/work-state/ALP-04-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")

        self.assertIn(checkpoint["status"], {"in_progress", "completed_verified"})
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["predecessor"]["work_item_id"], "ALP-03")
        self.assertEqual(checkpoint["predecessor"]["status"], "completed_verified")
        self.assertEqual(checkpoint["predecessor"]["merge_sha"], baseline)

        if checkpoint["status"] == "in_progress":
            self.assertTrue(checkpoint["implementation_authority"])
            self.assertEqual(checkpoint["implementation_branch"], branch)
            gate = checkpoint["acceptance_gate"]
            self.assertTrue(gate["acceptance_package_authorized"])
            self.assertEqual(gate["production_mutation_authorized"], gate["red_observed"])
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-04")
            self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
            self.assertTrue(pointer["active_attempt"]["implementation_authority"])
            self.assertEqual(index["current"]["work_item_id"], "ALP-04")
            self.assertEqual(index["current"]["status"], "in_progress")
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-04")
            self.assertEqual(registry["active_planning_work"]["state"], "in_progress")
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-04")
            self.assertEqual(runtime["active_work"]["state"], "in_progress")
        else:
            self.assertFalse(checkpoint["implementation_authority"])
            self.assertTrue(checkpoint["authority_retired"])

        alp04 = next(item for item in backlog["tranches"] if item["id"] == "ALP-04")
        self.assertEqual(alp04["status"], checkpoint["status"])
        self.assertEqual(alp04["implementation_authority"], checkpoint["implementation_authority"])
        self.assertEqual(backlog["completed_through"], "ALP-03" if checkpoint["status"] == "in_progress" else "ALP-04")

        for phrase in (
            "ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links",
            "GM-authored campaign achievement",
            "Reputation/Relationship/Faction",
            "mechanical reward",
            "Diegetic practice remains optional",
            "migration `0022`",
        ):
            self.assertIn(phrase, program)

    def test_alp04_scope_preserves_owner_system_boundaries(self):
        checkpoint = load_json("governance/ai/work-state/ALP-04-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        boundary = checkpoint["authority_boundary"]
        self.assertIn("GM-authored campaign achievement definitions over ALP-02 campaign_achievement definitions", scope["authorized"])
        self.assertIn("campaign title and recognition reference projection", scope["authorized"])
        self.assertIn("explicit Reputation/Relationship/Faction owner-system references without mutation", scope["authorized"])
        self.assertIn("explicit mechanical reward owner-system references without reward commit", scope["authorized"])
        self.assertIn("achievement awarding or completion mutation", scope["not_authorized"])
        self.assertIn("mechanical reward commit", scope["not_authorized"])
        self.assertIn("durable ALP persistence or migration 0022", scope["not_authorized"])
        self.assertFalse(boundary["alp05_plus_authorized"])
        self.assertFalse(boundary["tester_distribution_authorized"])
        self.assertFalse(boundary["release_or_deployment_authorized"])


if __name__ == "__main__":
    unittest.main()
