import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Eci01EnvCewRoadmapRegistrationTests(unittest.TestCase):
    def test_eci01_is_durable_required_successor_before_alp_across_lifecycle(self):
        program = load_text("governance/application-planning/environment-creature-integration/ECI_ENVIRONMENT_CREATURE_INTEGRATION_PROGRAM.md")
        backlog = load_json("governance/application-planning/environment-creature-integration/ECI_PROGRAM_BACKLOG.json")
        amendment_path = "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_MAL10_ECI_INSERTION_CLOSEOUT_2026-09-04.md"
        amendment = load_text(amendment_path)
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        checkpoint = load_json("governance/ai/work-state/ECI-01-attempt-001.json")
        mal = load_json("governance/application-planning/microgames-ambient-loops/MAL_MICROGAMES_AMBIENT_LOOPS_PROGRAM.md")
        alp = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")

        self.assertEqual(backlog["program_id"], "ECI")
        self.assertEqual(backlog["activation_after"], "MAL-10")
        self.assertEqual(backlog["successor"], "ALP-01")
        self.assertEqual(backlog["required_contracts"], ["ENV-HS-1.0", "ENV-CD-1.0", "CEW-GM-DISC-1.0"])
        self.assertIn(checkpoint["status"], {"selected_not_started", "in_progress", "completed_verified"})
        self.assertEqual(backlog["tranches"][0]["status"], checkpoint["status"])
        self.assertIn("MAL-01..10 → ECI-01 → ALP-01..08", amendment)
        self.assertIn("ready_for_separately_governed_software_selection", amendment)
        self.assertIn("no later roadmap edit may silently drop", amendment)

        self.assertEqual(mal["successor"], "ECI-01")
        self.assertEqual(alp["activation_after"], "ECI-01")
        self.assertEqual(alp.get("deferred_by_owner_insertion", {}).get("inserted_work_item"), "ECI-01")

        if checkpoint["status"] == "completed_verified":
            # ECI's durable invariant is that ALP became its successor family. Do not
            # pin this historical regression to whichever ALP tranche is currently
            # selected; later ALP closeouts must be allowed to advance normally.
            self.assertEqual(alp["tranches"][0]["id"], "ALP-01")
            self.assertNotEqual(alp["tranches"][0]["status"], "planned")
            if pointer.get("active_attempt", {}).get("source_program") == "ALP":
                active_id = pointer["active_attempt"]["work_item_id"]
                active_tranche = next((row for row in alp["tranches"] if row["id"] == active_id), None)
                self.assertIsNotNone(active_tranche)
                self.assertEqual(pointer["active_attempt"]["status"], active_tranche["status"])
                self.assertEqual(index["current"]["work_item_id"], active_id)
                self.assertEqual(index["current"]["status"], pointer["active_attempt"]["status"])
        else:
            self.assertEqual(pointer["active_attempt"]["work_item_id"], "ECI-01")
            self.assertEqual(pointer["active_attempt"]["status"], checkpoint["status"])
            self.assertEqual(index["current"]["work_item_id"], "ECI-01")
            self.assertEqual(index["current"]["status"], checkpoint["status"])
            self.assertTrue(index["effective_forward_order"].startswith("ECI-01 → ALP-01..08"))
            self.assertEqual(alp["tranches"][0]["status"], "planned")
            self.assertFalse(alp["tranches"][0].get("implementation_authority", False))

        for phrase in (
            "ENV-HS-1.0",
            "ENV-CD-1.0",
            "CEW-GM-DISC-1.0",
            "can occur here",
            "normally occurs here",
            "does not create encounter placement",
        ):
            self.assertIn(phrase, program)

    def test_dominix_owner_clarification_is_preserved_as_setting_authority(self):
        note = load_text("governance/application-planning/parallel-preimplementation/PPIA-12_DOMINIX_ESCALATION_OWNER_CLARIFICATION_2026-09-04.md")
        for phrase in (
            "FMR",
            "crazy and loud",
            "spiral out",
            "everyone has the potential",
            "story can escalate",
            "abilities can escalate alongside it",
            "great majority",
            "trying to live around that",
            "avoid that",
            "not the universal everyday presentation of Dominix",
        ):
            self.assertIn(phrase, note)
        self.assertIn("does not invent a universal escalation formula", note)


if __name__ == "__main__":
    unittest.main()
