import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp07PlayerGmUxAccessibilityNotificationsRecognitionHistoryRegistrationTests(unittest.TestCase):
    def test_alp07_governed_start_or_closeout_is_consistent(self):
        baseline = "b59e47dfe5754ad22cfdbe2082585d265335da51"
        branch = "integration/alp-07-player-gm-ux-accessibility-notifications-recognition-history"
        checkpoint = load_json("governance/ai/work-state/ALP-07-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")

        self.assertEqual(checkpoint["work_item_id"], "ALP-07")
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        self.assertIn(checkpoint["status"], {"in_progress", "completed_verified"})
        alp07 = next(item for item in backlog["tranches"] if item["id"] == "ALP-07")
        self.assertEqual(alp07["status"], checkpoint["status"])

        if checkpoint["status"] == "in_progress":
            production_authorized = checkpoint["production_mutation_authorized"]
            self.assertTrue(checkpoint["implementation_authority"])
            self.assertEqual(checkpoint["implementation_branch"], branch)
            self.assertTrue(checkpoint["branch_creation_authorized"])
            self.assertTrue(checkpoint["acceptance_package_authorized"])
            self.assertEqual(backlog["completed_through"], "ALP-06")
            self.assertEqual(backlog["current_item"], "ALP-07")
            self.assertEqual(backlog["active_contract"]["production_mutation_authorized"], production_authorized)
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-07")
            self.assertEqual(pointer["active_attempt"]["status"], "in_progress")
            self.assertEqual(pointer["active_attempt"]["implementation_branch"], branch)
            self.assertTrue(pointer["active_attempt"]["implementation_authority"])
            self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], production_authorized)
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-07")
            self.assertEqual(registry["active_planning_work"]["state"], "in_progress")
            self.assertEqual(registry["alp_07_authority"]["production_mutation_authorized"], production_authorized)
            self.assertEqual(index["current"]["work_item_id"], "ALP-07")
            self.assertEqual(index["current"]["status"], "in_progress")
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-07")
            self.assertEqual(runtime["active_work"]["state"], "in_progress")
            if production_authorized:
                self.assertIsNotNone(checkpoint["validation"]["acceptance_red"])
                self.assertTrue(backlog["active_contract"]["matching_red_observed"])
                self.assertTrue(registry["alp_07_authority"]["matching_red_observed"])
            else:
                self.assertIsNone(checkpoint["validation"]["acceptance_red"])
                self.assertFalse(backlog["active_contract"]["matching_red_observed"])
                self.assertFalse(registry["alp_07_authority"]["matching_red_observed"])
        else:
            self.assertFalse(checkpoint["implementation_authority"])
            self.assertTrue(checkpoint["authority_retired"])
            self.assertTrue(checkpoint["completed"])
            self.assertEqual(backlog["completed_through"], "ALP-07")
            self.assertEqual(backlog["current_item"], "ALP-08")
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ALP-08")
            self.assertEqual(pointer["active_attempt"]["status"], "selected_not_started")
            self.assertIsNone(pointer["active_attempt"]["implementation_branch"])
            self.assertFalse(pointer["active_attempt"]["implementation_authority"])
            self.assertEqual(registry["active_planning_work"]["work_item"], "ALP-08")
            self.assertEqual(registry["active_planning_work"]["state"], "selected_not_started")
            self.assertEqual(index["current"]["work_item_id"], "ALP-08")
            self.assertEqual(runtime["active_work"]["work_item"], "ALP-08")

        for phrase in (
            "ALP-07 — Player/GM UX, Accessibility, Notifications & Recognition History",
            "viewer role",
            "Accessibility behavior is presentation-only",
            "notification candidates",
            "Recognition history",
            "hidden or unauthorized",
            "migration `0022`",
            "ALP-08",
        ):
            self.assertIn(phrase, program)

    def test_alp07_scope_preserves_read_only_presentation_boundaries(self):
        checkpoint = load_json("governance/ai/work-state/ALP-07-attempt-001.json")
        scope = checkpoint["implementation_scope"]
        boundary = checkpoint["authority_boundary"]
        for item in (
            "explicit viewer role and viewer identity for player-facing versus GM-facing ALP projections",
            "accessibility presentation metadata and caller-supplied display preferences that alter presentation only, not canonical ALP or owner-system state",
            "deterministic notification-candidate projection for authorized ALP events or state changes without delivery, acknowledgement or external messaging side effects",
            "deterministic recognition-history projection with stable record identity, source family, provenance and timestamp/order metadata when explicitly supplied",
        ):
            self.assertIn(item, scope["authorized"])
        for item in (
            "achievement awarding, completion mutation or recognition creation by implication",
            "notification sending, delivery, external messaging, acknowledgement-state mutation or subscription mutation",
            "hidden or unauthorized evidence, event, history or cardinality inference",
            "durable ALP persistence or migration 0022",
            "ALP-08 MAL/ISE/WCI/GCL integration or golden learning/recognition proof behavior",
        ):
            self.assertIn(item, scope["not_authorized"])
        self.assertFalse(boundary["alp08_plus_authorized"])
        self.assertFalse(boundary["provider_activation_authorized"])
        self.assertFalse(boundary["tester_distribution_authorized"])
        self.assertFalse(boundary["release_or_deployment_authorized"])

    def test_alp07_registry_keeps_all_mutating_authorities_closed_across_lifecycle(self):
        checkpoint = load_json("governance/ai/work-state/ALP-07-attempt-001.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        authority = registry["alp_07_authority"]
        if checkpoint["status"] == "in_progress":
            self.assertTrue(authority["implementation_authority"])
            self.assertTrue(authority["acceptance_package_authorized"])
        else:
            self.assertEqual(checkpoint["status"], "completed_verified")
            self.assertFalse(authority["implementation_authority"])
            self.assertTrue(authority["retired"])
            self.assertFalse(authority["acceptance_package_authorized"])
            self.assertFalse(authority["production_mutation_authorized"])
        self.assertFalse(authority["owner_mutation_authorized"])
        self.assertFalse(authority["achievement_award_authorized"])
        self.assertFalse(authority["reward_commit_authorized"])
        self.assertFalse(authority["xp_or_advancement_grant_authorized"])
        self.assertFalse(authority["title_or_reputation_grant_authorized"])
        self.assertFalse(authority["notification_delivery_authorized"])
        self.assertFalse(authority["notification_acknowledgement_mutation_authorized"])
        self.assertFalse(authority["subscription_mutation_authorized"])
        self.assertFalse(authority["hidden_evidence_inference_authorized"])
        self.assertFalse(authority["hidden_history_inference_authorized"])
        self.assertFalse(authority["durable_persistence_authorized"])
        self.assertFalse(authority["migration_0022_authorized"])
        self.assertFalse(authority["alp08_plus_authorized"])


if __name__ == "__main__":
    unittest.main()
