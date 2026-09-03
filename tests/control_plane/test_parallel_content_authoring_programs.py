import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "governance/application-planning/PARALLEL_CONTENT_AUTHORING_PROGRAMS.json"
ENV_BACKLOG = ROOT / "governance/application-planning/environment-preset-overlay/ENV_PROGRAM_BACKLOG.json"
CEW_BACKLOG = ROOT / "governance/application-planning/creature-ecology-wildlife/CEW_PROGRAM_BACKLOG.json"
CEW_PROGRAM = ROOT / "governance/application-planning/creature-ecology-wildlife/CEW_CREATURE_ECOLOGY_WILDLIFE_PROGRAM.md"


class ParallelContentAuthoringProgramsTest(unittest.TestCase):
    def load_json(self, path: Path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_registry_preserves_nonimplementation_boundary(self):
        registry = self.load_json(REGISTRY)
        self.assertEqual(registry["registry_id"], "PARALLEL-CONTENT-01")
        programs = {item["program_id"]: item for item in registry["programs"]}
        self.assertEqual(set(programs), {"ENV", "CEW"})
        for item in programs.values():
            self.assertFalse(item["application_implementation_authority"])
            self.assertTrue(item["parallel_with_software"])
            self.assertEqual(item["tranche_count"], 16)
        joined = "\n".join(registry["execution_rules"])
        self.assertIn("active software pointer remains authoritative", joined)
        self.assertIn("Havalaea native-born Time-of-Troubles-descended fauna", joined)
        self.assertIn("eligible for existing NPC-system projection", joined)
        self.assertIn("Mount, pet/companion and familiar are pathway/relationship capabilities", joined)

    def test_env_order_and_boundary_are_stable(self):
        backlog = self.load_json(ENV_BACKLOG)
        self.assertEqual(backlog["strict_order"], [f"ENV-{i:02d}" for i in range(1, 17)])
        self.assertFalse(backlog["application_implementation_authority"])
        self.assertTrue(backlog["parallel_with_software"])
        self.assertEqual(backlog["current_item"], "ENV-01")
        self.assertTrue(any("must not mutate Multiversal-app" in item for item in backlog["boundaries"]))

    def test_cew_order_havalaea_npc_and_partnership_invariants_are_stable(self):
        backlog = self.load_json(CEW_BACKLOG)
        self.assertEqual(backlog["strict_order"], [f"CEW-{i:02d}" for i in range(1, 17)])
        self.assertFalse(backlog["application_implementation_authority"])
        self.assertTrue(backlog["parallel_with_software"])
        self.assertEqual(backlog["current_item"], "CEW-01")
        havalaea = "\n".join(backlog["havalaea_invariants"])
        self.assertIn("Time-of-Troubles", havalaea)
        self.assertIn("NPC-system projection", havalaea)
        self.assertIn("animal ecological identity", havalaea)
        self.assertIn("voluntary-partnership/consent", havalaea)
        partnership = "\n".join(backlog["partnership_invariants"])
        self.assertIn("mount, pet/companion and familiar are relationship/pathway capabilities", partnership)
        self.assertIn("CCP-06", partnership)
        self.assertIn("CCP-07", partnership)

    def test_cew_program_requires_npc_capable_havalaea_fauna_without_identity_collapse(self):
        text = CEW_PROGRAM.read_text(encoding="utf-8")
        self.assertIn("eligible for **NPC-system projection**", text)
        self.assertIn("NPC presentation does not convert them into humanoids", text)
        self.assertIn("Mount, pet/companion and familiar are **relationship/pathway capabilities or roles**, not base creature types", text)


if __name__ == "__main__":
    unittest.main()
