import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class Eci01EnvCewRoadmapRegistrationTests(unittest.TestCase):
    def test_eci01_is_durable_required_successor_before_alp(self):
        program = load_text("governance/application-planning/environment-creature-integration/ECI_ENVIRONMENT_CREATURE_INTEGRATION_PROGRAM.md")
        backlog = load_json("governance/application-planning/environment-creature-integration/ECI_PROGRAM_BACKLOG.json")
        roadmap = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md")
        amendment = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_ECI_INSERTION_2026-09-04.md")
        index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
        pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
        checkpoint = load_json("governance/ai/work-state/ECI-01-attempt-001.json")
        mal = load_json("governance/application-planning/microgames-ambient-loops/MAL_MICROGAMES_AMBIENT_LOOPS_PROGRAM.md")
        alp = load_json("governance/application-planning/achievements-learning-practice/ALP_PROGRAM_BACKLOG.json")

        self.assertEqual(backlog["program_id"], "ECI")
        self.assertEqual(backlog["activation_after"], "MAL-10")
        self.assertEqual(backlog["successor"], "ALP-01")
        self.assertEqual(backlog["current_item"], "ECI-01")
        self.assertEqual(backlog["tranches"][0]["status"], "selected_not_started")
        self.assertFalse(backlog["tranches"][0]["implementation_authority"])
        self.assertEqual(
            backlog["required_contracts"],
            ["ENV-HS-1.0", "ENV-CD-1.0", "CEW-GM-DISC-1.0"],
        )
        self.assertIn("MAL-01..10 → ECI-01 → ALP-01..08", roadmap)
        self.assertIn("ECI-01", amendment)
        self.assertIn("ready_for_separately_governed_software_selection", amendment)
        self.assertIn("no later roadmap edit may silently drop", amendment)

        self.assertEqual(index["current"]["work_item_id"], "ECI-01")
        self.assertEqual(index["current"]["status"], "selected_not_started")
        self.assertTrue(index["effective_forward_order"].startswith("ECI-01 → ALP-01..08"))
        self.assertEqual(pointer["active_attempt"]["work_item_id"], "ECI-01")
        self.assertFalse(pointer["active_attempt"]["implementation_authority"])
        self.assertEqual(checkpoint["work_item_id"], "ECI-01")
        self.assertEqual(checkpoint["status"], "selected_not_started")
        self.assertFalse(checkpoint["implementation_authority"])

        self.assertEqual(mal["successor"], "ECI-01")
        self.assertEqual(alp["activation_after"], "ECI-01")
        self.assertEqual(alp["tranches"][0]["status"], "planned")
        self.assertEqual(alp["deferred_by_owner_insertion"]["inserted_work_item"], "ECI-01")

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
