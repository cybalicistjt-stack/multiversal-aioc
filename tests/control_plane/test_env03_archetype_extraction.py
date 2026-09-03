import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
LIBRARY = ENV_DIR / "ENV-03_ARCHETYPE_LIBRARY_v1.0.0.json"
CROSSWALK = ENV_DIR / "ENV-03_PROFILE_ARCHETYPE_CROSSWALK_v1.0.0.csv"
ENV02 = ENV_DIR / "ENV-02_EFFECTIVE_COMPLETENESS_MATRIX_v1.0.0.csv"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env03ArchetypeExtractionTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_archetype_library_is_bounded_and_nonimplementation(self):
        library = self.load_json(LIBRARY)
        self.assertEqual(library["tranche"], "ENV-03")
        self.assertEqual(library["archetype_count"], 15)
        self.assertFalse(library["authority_boundary"]["application_implementation_authority"])
        self.assertFalse(library["authority_boundary"]["source_profiles_mutated"])
        self.assertEqual(library["authority_boundary"]["overlay_conflict_and_stacking_owned_by"], "ENV-04")
        self.assertEqual(library["authority_boundary"]["preset_conversion_owned_by"], "ENV-05")
        self.assertEqual(library["authority_boundary"]["habitat_signature_vocabulary_owned_by"], "ENV-15")

    def test_all_env02_profiles_map_once_to_valid_primary_archetypes(self):
        library = self.load_json(LIBRARY)
        archetype_ids = {item["id"] for item in library["archetypes"]}
        crosswalk = self.load_csv(CROSSWALK)
        env02 = self.load_csv(ENV02)
        self.assertEqual(len(crosswalk), 40)
        self.assertEqual(len(env02), 40)
        self.assertEqual({row["Environment_Definition_ID"] for row in crosswalk}, {row["Environment_Definition_ID"] for row in env02})
        self.assertEqual(len({row["Environment_Definition_ID"] for row in crosswalk}), 40)
        for row in crosswalk:
            self.assertIn(row["Primary_Archetype_ID"], archetype_ids)
            for secondary in filter(None, row["Secondary_Archetype_IDs"].split("|")):
                self.assertIn(secondary, archetype_ids)
                self.assertNotEqual(secondary, row["Primary_Archetype_ID"])
        self.assertEqual(sum(int(row["Compound_Archetype_Count"]) > 1 for row in crosswalk), 12)

    def test_state_and_condition_families_are_not_archetype_identity(self):
        ids = {item["id"] for item in self.load_json(LIBRARY)["archetypes"]}
        forbidden = {"ARCH-POST-APOCALYPTIC", "ARCH-RADIOACTIVE", "ARCH-OVERGROWN", "ARCH-FLOODED", "ARCH-ABANDONED", "ARCH-VOLCANIC", "ARCH-NEBULA", "ARCH-BLACK-HOLE", "ARCH-WORMHOLE", "ARCH-CYBERPUNK"}
        self.assertTrue(ids.isdisjoint(forbidden))

    def test_key_compound_profiles_preserve_multiple_baselines(self):
        rows = {row["Environment_Name"]: row for row in self.load_csv(CROSSWALK)}
        self.assertEqual(rows["Mangrove Swamp"]["Primary_Archetype_ID"], "ARCH-WETLAND")
        self.assertEqual(set(rows["Mangrove Swamp"]["Secondary_Archetype_IDs"].split("|")), {"ARCH-FOREST", "ARCH-COASTAL"})
        self.assertEqual(rows["Sunken City"]["Primary_Archetype_ID"], "ARCH-SUBMERGED")
        self.assertIn("ARCH-URBAN", rows["Sunken City"]["Secondary_Archetype_IDs"])
        self.assertEqual(rows["Underground Bunker Network"]["Primary_Archetype_ID"], "ARCH-CONSTRUCTED-HABITAT")
        self.assertEqual(rows["Port City"]["Secondary_Archetype_IDs"], "ARCH-COASTAL")
        self.assertIn("ENV-09", rows["Arctic Tundra and Taiga"]["Deferred_Preset_Or_Overlay_Traits"])

    def test_backlog_preserves_env03_completion_after_progression(self):
        backlog = self.load_json(BACKLOG)
        order = backlog["strict_order"]
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        self.assertEqual(statuses["ENV-03"], "completed_verified")
        self.assertGreaterEqual(order.index(backlog["completed_through"]), order.index("ENV-03"))
        self.assertGreater(order.index(backlog["current_item"]), order.index("ENV-03"))
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
