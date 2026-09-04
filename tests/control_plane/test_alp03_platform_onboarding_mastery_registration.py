import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Alp03PlatformOnboardingMasteryRegistrationTests(unittest.TestCase):
    def test_alp03_governed_start_and_red_unlock_are_consistent(self):
        baseline = "050356f7578856de5931917a60efe8af91def1bd"
        branch = "integration/alp-03-platform-onboarding-mastery-milestones"
        checkpoint = load_json("governance/ai/work-state/ALP-03-attempt-001.json")
        backlog = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        runtime = load_json("governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json")
        program = load_text("governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md")

        self.assertEqual(checkpoint["status"], "in_progress")
        self.assertTrue(checkpoint["implementation_authority"])
        self.assertEqual(checkpoint["implementation_branch"], branch)
        self.assertEqual(checkpoint["application_baseline_sha"], baseline)
        gate = checkpoint["acceptance_gate"]
        self.assertTrue(gate["acceptance_package_authorized"])
        self.assertTrue(gate["matching_linux_windows_red_required"])
        self.assertEqual(gate["production_mutation_authorized"], gate["red_observed"])
        if gate["red_observed"]:
            red = gate["acceptance_red"]
            self.assertEqual(red["head_sha"], "a71cc81b6b815b39c90159d13ae43d4b33d5f359")
            self.assertEqual(red["run_id"], 33885427744)
            self.assertEqual(red["linux_job"], 101063942140)
            self.assertEqual(red["windows_job"], 101063942161)
            self.assertEqual(red["deterministic_compare_job"], 101064060265)
            self.assertEqual(red["matching_failure_step"], "alp03-invariants")
            self.assertEqual(red["deterministic_receipt_sha256"], "17f107d0fb2886f6805b57e32282d670046396e96a10f3576c19869162585303")
            self.assertTrue(red["production_contract_absent"])

        alp03 = next(item for item in backlog["tranches"] if item["id"] == "ALP-03")
        self.assertEqual(alp03["status"], "in_progress")
        self.assertTrue(alp03["implementation_authority"])
        self.assertEqual(alp03["implementation_branch"], branch)
        self.assertEqual(backlog["completed_through"], "ALP-02")

        for surface in (pointer["active_attempt"], index["current"]):
            self.assertEqual(surface["work_item_id"], "ALP-03")
            self.assertEqual(surface["status"], "in_progress")
            self.assertTrue(surface["implementation_authority"])
            self.assertEqual(surface["implementation_branch"], branch)

        self.assertTrue(pointer["bounded_authority"]["alp_implementation"])
        self.assertEqual(pointer["bounded_authority"]["production_mutation_authorized"], gate["production_mutation_authorized"])
        self.assertEqual(registry["active_planning_work"]["state"], "in_progress")
        self.assertTrue(registry["alp_03_authority"]["implementation_authority"])
        self.assertEqual(registry["alp_03_authority"]["production_mutation_authorized"], gate["production_mutation_authorized"])
        self.assertEqual(runtime["active_work"]["state"], "in_progress")
        self.assertTrue(runtime["active_work"]["implementation_authority"])
        self.assertEqual(runtime["active_work"]["production_mutation_authorized"], gate["production_mutation_authorized"])
        self.assertEqual(runtime["application_repository"]["canonical_main"], baseline)

        self.assertIn("ALP-03 — Platform Onboarding & Mastery Milestones", program)
        self.assertIn("**IN_PROGRESS**", program)
        self.assertIn("Diegetic practice remains optional", program)
        self.assertIn("migration `0022`", program)

    def test_alp03_scope_keeps_later_authorities_closed(self):
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
