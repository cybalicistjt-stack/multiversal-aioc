import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp04GmCampaignAchievementsRegistrationTests(unittest.TestCase):
    def test_alp04_remains_completed_while_successors_may_advance(self):
        baseline = "025f653f65be5ea8ccae1d04f9591e146c3d8797"
        merge = "788a8025caf8046edfeddcbf238cce972a4c5378"
        checkpoint = load_json("governance/ai/work-state/ALP-04-attempt-001.json")
        successor = load_json("governance/ai/work-state/ALP-05-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")
        supplement = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ALP04_CLOSEOUT_2026-09-04.md")

        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertEqual(checkpoint["application_pr"], 410)
        self.assertEqual(checkpoint["application_merge_sha"], merge)
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["authority_retired"])
        self.assertEqual(checkpoint["validation"]["acceptance_red"]["head_sha"], "183581811afa54725c0586225d9a23e733fa5978")
        self.assertEqual(checkpoint["validation"]["final_green"]["head_sha"], "763e9ef8fb925e9188cdc8975600b6c7047fae01")
        self.assertEqual(checkpoint["convergence_control"]["application_feature_repair_cycles"], 0)
        self.assertEqual(checkpoint["validation"]["final_green"]["historical_profile_fanout"], 0)

        allowed_successor_states = {"selected_not_started", "in_progress", "completed_verified"}
        self.assertIn(successor["status"], allowed_successor_states)
        self.assertEqual(successor["application_baseline_sha"], merge)
        alp04 = next(item for item in backlog["tranches"] if item["id"] == "ALP-04")
        alp05 = next(item for item in backlog["tranches"] if item["id"] == "ALP-05")
        self.assertEqual(alp04["status"], "completed_verified")
        self.assertFalse(alp04["implementation_authority"])
        self.assertEqual(alp04["application_merge_sha"], merge)
        self.assertIn(alp05["status"], allowed_successor_states)
        self.assertIn(backlog["completed_through"], {"ALP-04", "ALP-05", "ALP-06"})
        self.assertIn(backlog["current_item"], {"ALP-05", "ALP-06", "ALP-07"})

        if successor["status"] != "completed_verified":
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-05")
            self.assertEqual(pointer["active_attempt"]["status"], successor["status"])
            self.assertEqual(index["current"]["work_item_id"], "ALP-05")
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-05")
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-05")
        elif backlog["completed_through"] == "ALP-05":
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-06")
            self.assertEqual(index["current"]["work_item_id"], "ALP-06")
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-06")
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-06")
        elif backlog["completed_through"] == "ALP-06":
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-07")
            self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
            self.assertEqual(index["current"]["work_item_id"], "ALP-07")
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-07")
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-07")

        for phrase in (
            "ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links",
            "ALP-05 — Diegetic Practice Spaces, Training Scenes & Simulations",
            "GM-authored campaign achievement",
            "Reputation/Relationship/Faction",
            "mechanical reward",
            "Diegetic practice remains optional",
            "migration `0022`",
            merge,
        ):
            self.assertIn(phrase, program)

        for phrase in (
            "COMPLETED_VERIFIED",
            "33891372974",
            "33892290907",
            "c9496258fdde1436b23b3e75d4dbdd0668062cc6daa8aebd2a2fe68a93eb68e7",
            "7c653ffae5b39d734aceacb933622441f6a99290adfc986b2d430c7d889c60b6",
            merge,
            "ALP-05",
            "selected_not_started",
        ):
            self.assertIn(phrase, supplement)

    def test_alp04_scope_preserves_owner_system_boundaries(self):
        checkpoint = load_json("governance/ai/work-state/ALP-04-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        completed = checkpoint["completed_contract"]
        boundary = checkpoint["authority_boundary"]
        self.assertIn("GM-authored campaign achievement definitions over ALP-02 campaign_achievement definitions", scope["authorized"])
        self.assertIn("campaign title and recognition reference projection", scope["authorized"])
        self.assertIn("explicit Reputation/Relationship/Faction owner-system references without mutation", scope["authorized"])
        self.assertIn("explicit mechanical reward owner-system references without reward commit", scope["authorized"])
        self.assertIn("achievement awarding or completion mutation", scope["not_authorized"])
        self.assertIn("mechanical reward commit", scope["not_authorized"])
        self.assertIn("durable ALP persistence or migration 0022", scope["not_authorized"])
        self.assertFalse(completed["achievement_award_performed"])
        self.assertFalse(completed["owner_system_mutation_performed"])
        self.assertFalse(completed["reward_commit_performed"])
        self.assertFalse(completed["durable_alp_persistence_implemented"])
        self.assertFalse(completed["migration_0022_reserved"])
        self.assertFalse(boundary["alp05_plus_authorized"])
        self.assertFalse(boundary["tester_distribution_authorized"])
        self.assertFalse(boundary["release_or_deployment_authorized"])


if __name__ == "__main__":
    unittest.main()
