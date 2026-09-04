import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp03PlatformOnboardingMasteryRegistrationTests(unittest.TestCase):
    def test_alp03_remains_completed_while_successor_may_advance(self):
        merge = "025f653f65be5ea8ccae1d04f9591e146c3d8797"
        alp04_merge = "788a8025caf8046edfeddcbf238cce972a4c5378"
        alp05_merge = "402aa6d91795d6e75be64c106aa122b0b79cb872"
        checkpoint = load_json("governance/ai/work-state/ALP-03-attempt-001.json")
        successor = load_json("governance/ai/work-state/ALP-04-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")
        closeout = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ALP03_CLOSEOUT_2026-09-04.md")

        self.assertEqual(checkpoint["status"], "completed_verified")
        self.assertFalse(checkpoint["implementation_authority"])
        self.assertTrue(checkpoint["authority_retired"])
        self.assertEqual(checkpoint["application_pr"], 409)
        self.assertEqual(checkpoint["application_merge_sha"], merge)
        self.assertEqual(checkpoint["convergence_control"]["owner_continue_count"], 2)
        self.assertEqual(checkpoint["convergence_control"]["execution_cycles"], 2)
        self.assertEqual(checkpoint["convergence_control"]["repair_cycles"], 6)
        self.assertFalse(checkpoint["convergence_control"]["same_cycle_completed"])
        self.assertTrue(checkpoint["convergence_control"]["completed_within_two_cycles"])
        self.assertFalse(checkpoint["convergence_control"]["control_plane_incident"])
        self.assertEqual(checkpoint["convergence_control"]["application_feature_repair_cycles"], 0)
        self.assertEqual(checkpoint["convergence_control"]["repository_state_repair_cycles"], 2)
        self.assertEqual(checkpoint["convergence_control"]["validation_contract_repair_cycles"], 4)
        self.assertEqual(checkpoint["validation"]["final_green"]["historical_profile_fanout"], 0)

        self.assertIn(successor["status"], {"selected_not_started", "in_progress", "completed_verified"})
        self.assertEqual(successor["application_baseline_sha"], merge)
        alp03 = next(item for item in backlog["tranches"] if item["id"] == "ALP-03")
        alp04 = next(item for item in backlog["tranches"] if item["id"] == "ALP-04")
        self.assertEqual(alp03["status"], "completed_verified")
        self.assertFalse(alp03["implementation_authority"])
        self.assertEqual(alp04["status"], successor["status"])
        self.assertEqual(alp04["implementation_authority"], successor["implementation_authority"])

        if successor["status"] != "completed_verified":
            self.assertEqual(backlog["completed_through"], "ALP-03")
            self.assertEqual(backlog["current_item"], "ALP-04")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-04")
            self.assertEqual(pointer["active_attempt"]["status"], successor["status"])
            self.assertEqual(index["current"]["work_item_id"], "ALP-04")
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-04")
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-04")
            self.assertEqual(pointer["roadmap_supplements"], ["governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ALP03_CLOSEOUT_2026-09-04.md"])
        else:
            self.assertEqual(successor["application_merge_sha"], alp04_merge)
            self.assertFalse(successor["implementation_authority"])
            alp05 = load_json("governance/ai/work-state/ALP-05-attempt-001.json")
            self.assertIn(alp05["status"], {"selected_not_started", "in_progress", "completed_verified"})
            self.assertEqual(alp05["application_baseline_sha"], alp04_merge)

            if alp05["status"] != "completed_verified":
                self.assertEqual(backlog["completed_through"], "ALP-04")
                self.assertEqual(backlog["current_item"], "ALP-05")
                if alp05["status"] == "selected_not_started":
                    self.assertIsNone(alp05["implementation_branch"])
                    self.assertFalse(alp05["implementation_authority"])
                else:
                    self.assertEqual(alp05["implementation_branch"], "integration/alp-05-diegetic-practice-spaces-training-scenes-simulations")
                    self.assertTrue(alp05["implementation_authority"])
                self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-05")
                self.assertEqual(pointer["active_attempt"]["status"], alp05["status"])
                self.assertEqual(index["current"]["work_item_id"], "ALP-05")
                self.assertEqual(index["current"]["status"], alp05["status"])
                self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-05")
                self.assertEqual(registry["active_planning_work"]["state"], alp05["status"])
                self.assertEqual(runtime["application_repository"]["canonical_main"], alp04_merge)
                self.assertEqual(runtime["active_work"]["work_item"], "ALP-05")
                self.assertEqual(runtime["active_work"]["state"], alp05["status"])
                self.assertEqual(pointer["roadmap_supplements"], ["governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ALP04_CLOSEOUT_2026-09-04.md"])
            else:
                self.assertEqual(alp05["application_merge_sha"], alp05_merge)
                self.assertFalse(alp05["implementation_authority"])
                alp06 = load_json("governance/ai/work-state/ALP-06-attempt-001.json")
                self.assertIn(alp06["status"], {"selected_not_started", "in_progress", "completed_verified"})
                self.assertEqual(alp06["application_baseline_sha"], alp05_merge)
                self.assertEqual(backlog["completed_through"], "ALP-05")
                self.assertEqual(backlog["current_item"], "ALP-06")
                self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-06")
                self.assertEqual(pointer["active_attempt"]["status"], alp06["status"])
                self.assertEqual(index["current"]["work_item_id"], "ALP-06")
                self.assertEqual(index["current"]["status"], alp06["status"])
                self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-06")
                self.assertEqual(registry["active_planning_work"]["state"], alp06["status"])
                self.assertEqual(runtime["application_repository"]["canonical_main"], alp05_merge)
                self.assertEqual(runtime["active_work"]["work_item"], "ALP-06")
                self.assertEqual(runtime["active_work"]["state"], alp06["status"])
                self.assertEqual(pointer["roadmap_supplements"], ["governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ALP05_CLOSEOUT_2026-09-04.md"])
                if alp06["status"] == "selected_not_started":
                    self.assertIsNone(alp06["implementation_branch"])
                    self.assertFalse(alp06["implementation_authority"])

        self.assertFalse(registry["alp_03_authority"]["implementation_authority"])
        self.assertTrue(registry["alp_03_authority"]["retired"])
        alp03_registry = next(item for item in registry["recently_completed_implementation_work"] if item["work_item_id"] == "ALP-03")
        self.assertEqual(alp03_registry["application_feature_repair_cycles"], 0)
        self.assertEqual(alp03_registry["repository_state_repair_cycles"], 2)
        self.assertEqual(alp03_registry["validation_contract_repair_cycles"], 4)

        for phrase in (
            "ALP-03 — Platform Onboarding & Mastery Milestones",
            "ALP-04 — GM-Authored Campaign Achievements, Titles, Reputation & Reward Links",
            "**COMPLETED_VERIFIED**",
            "Diegetic practice remains optional",
            "migration `0022`",
        ):
            self.assertIn(phrase, program)

        for value in (
            "a71cc81b6b815b39c90159d13ae43d4b33d5f359",
            "17f107d0fb2886f6805b57e32282d670046396e96a10f3576c19869162585303",
            "a8243e69e5c3831b858e11a87e1dd270865261ab",
            "a0f75ca0b9ff585dc00dab4ba684abf8b26c412becc53f1026fd8e659c081d1d",
            merge,
        ):
            self.assertIn(value, closeout)

    def test_alp03_completed_scope_keeps_later_authorities_closed(self):
        checkpoint = load_json("governance/ai/work-state/ALP-03-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        boundary = checkpoint["authority_boundary"]
        self.assertIn("platform-owned onboarding milestone definitions", scope["authorized"])
        self.assertIn("platform-owned mastery milestone definitions", scope["authorized"])
        self.assertIn("GM-authored campaign achievements, titles, reputation or reward links", scope["not_authorized"])
        self.assertIn("achievement awarding or completion mutation", scope["not_authorized"])
        self.assertFalse(boundary["alp04_plus_authorized"])
        self.assertFalse(boundary["tester_distribution_authorized"])
        self.assertFalse(boundary["release_or_deployment_authorized"])


if __name__ == "__main__":
    unittest.main()
