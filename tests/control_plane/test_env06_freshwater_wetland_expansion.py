import csv
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
BASE_ARCH = ENV_DIR / "ENV-03_ARCHETYPE_LIBRARY_v1.0.0.json"
EXT = ENV_DIR / "ENV-06_ARCHETYPE_EXTENSION_v1.0.0.json"
REGISTRY = ENV_DIR / "ENV-06_FRESHWATER_WETLAND_PRESET_REGISTRY_v1.0.0.csv"
CONTENT = ENV_DIR / "ENV-06_FRESHWATER_WETLAND_CONTENT_v1.0.0.md"
REPORT = ENV_DIR / "ENV-06_FRESHWATER_WETLAND_EXPANSION_REPORT.md"
OVERLAY_MODEL = ENV_DIR / "ENV-04_OVERLAY_MODEL_v1.0.0.json"
ENV05 = ENV_DIR / "ENV-05_PRESET_REGISTRY_v1.0.0.csv"


class Env06FreshwaterWetlandExpansionTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_flowing_water_is_the_only_archetype_extension(self):
        base = self.load_json(BASE_ARCH)
        ext = self.load_json(EXT)
        self.assertEqual(base["archetype_count"], 15)
        self.assertEqual(ext["authority_boundary"]["extension_archetype_count"], 1)
        self.assertEqual(ext["authority_boundary"]["current_composed_archetype_count"], 16)
        self.assertEqual([a["id"] for a in ext["archetypes"]], ["ARCH-FLOWING-WATER"])
        self.assertEqual(ext["decision"]["watch_item"], "flowing-water/channel behavior")
        self.assertEqual(ext["decision"]["result"], "promote_new_archetype")
        self.assertFalse(ext["authority_boundary"]["application_implementation_authority"])
        self.assertEqual(ext["authority_boundary"]["habitat_signature_vocabulary_deferred_to"], "ENV-15")
        self.assertEqual(ext["authority_boundary"]["creature_distribution_owned_by"], "CEW")

    def test_exact_six_freshwater_wetland_presets_are_added(self):
        rows = self.load_csv(REGISTRY)
        expected = {
            "River / Stream", "Lake / Pond", "Floodplain", "River Delta / Estuary",
            "Marsh / Bog / Fen", "Flooded Forest",
        }
        self.assertEqual(len(rows), 6)
        self.assertEqual({r["Preset_Name"] for r in rows}, expected)
        self.assertEqual(len({r["Preset_ID"] for r in rows}), 6)
        self.assertTrue(all(r["Authored_Expansion"] == "YES" for r in rows))
        self.assertTrue(all(r["Application_Implementation_Authority"] == "NO" for r in rows))
        self.assertTrue(all(r["Habitat_Signature_State"] == "deferred_to_ENV-15" for r in rows))
        self.assertTrue(all(r["Creature_Distribution_State"] == "deferred_to_CEW" for r in rows))

    def test_archetype_composition_uses_existing_library_plus_flowing_water(self):
        base_ids = {a["id"] for a in self.load_json(BASE_ARCH)["archetypes"]}
        ext_ids = {a["id"] for a in self.load_json(EXT)["archetypes"]}
        valid = base_ids | ext_ids
        rows = {r["Preset_Name"]: r for r in self.load_csv(REGISTRY)}
        for row in rows.values():
            self.assertIn(row["Primary_Archetype_ID"], valid)
            for secondary in filter(None, row["Secondary_Archetype_IDs"].split("|")):
                self.assertIn(secondary, valid)
        self.assertEqual(rows["River / Stream"]["Primary_Archetype_ID"], "ARCH-FLOWING-WATER")
        self.assertEqual(rows["Lake / Pond"]["Primary_Archetype_ID"], "ARCH-OPEN-WATER")
        self.assertEqual(set(rows["Floodplain"]["Secondary_Archetype_IDs"].split("|")), {"ARCH-OPEN-COUNTRY", "ARCH-FLOWING-WATER"})
        self.assertEqual(set(rows["River Delta / Estuary"]["Secondary_Archetype_IDs"].split("|")), {"ARCH-WETLAND", "ARCH-COASTAL"})
        self.assertEqual(rows["Marsh / Bog / Fen"]["Primary_Archetype_ID"], "ARCH-WETLAND")
        self.assertEqual(rows["Flooded Forest"]["Primary_Archetype_ID"], "ARCH-FOREST")
        self.assertEqual(rows["Flooded Forest"]["Secondary_Archetype_IDs"], "ARCH-WETLAND")

    def test_overlay_hooks_are_family_only_and_content_libraries_remain_deferred(self):
        rows = self.load_csv(REGISTRY)
        families = {f["id"] for f in self.load_json(OVERLAY_MODEL)["overlay_families"]}
        for row in rows:
            hints = {x for x in row["Overlay_Family_Hints"].split("|") if x}
            self.assertTrue(hints.issubset(families), row["Preset_Name"])
            self.assertFalse(any(x.startswith("OVL-") for x in hints), row["Preset_Name"])
        report = REPORT.read_text(encoding="utf-8")
        self.assertIn("does not author executable Heavy Rain, Flood, Extreme Cold, Toxic Water, Magical Saturation", report)
        self.assertIn("remain in ENV-11/12/13", report)

    def test_each_preset_has_all_minimum_content_classes_and_d12_table(self):
        text = CONTENT.read_text(encoding="utf-8")
        sections = re.split(r"\n## (?=\d+\.)", text)[1:]
        self.assertEqual(len(sections), 6)
        required = [
            "### Overview", "### Environmental features", "### Movement and navigation",
            "### Hazards", "### Encounters and challenges", "### Rest and shelter",
            "### Random encounters (d12)",
        ]
        for section in sections:
            for heading in required:
                self.assertIn(heading, section)
            random_part = section.split("### Random encounters (d12)", 1)[1]
            entries = re.findall(r"(?m)^(\d+)\. ", random_part)
            self.assertEqual(entries[:12], [str(i) for i in range(1, 13)])

    def test_distinctions_prevent_preset_overlay_and_marine_scope_collapse(self):
        report = REPORT.read_text(encoding="utf-8")
        self.assertIn("Floodplain versus Flood overlay", report)
        self.assertIn("Flooded Forest versus flooded ordinary forest", report)
        self.assertIn("Detailed tidal flats, marine ecology, surf/coastal behavior", report)
        self.assertIn("remain ENV-07", report)
        rows = {r["Preset_Name"]: r for r in self.load_csv(REGISTRY)}
        self.assertIn("ENV-07", rows["River Delta / Estuary"]["Downstream_Refinement_Tranches"])

    def test_total_governed_preset_count_becomes_46_without_touching_old_40(self):
        old_rows = self.load_csv(ENV05)
        new_rows = self.load_csv(REGISTRY)
        self.assertEqual(len(old_rows), 40)
        self.assertEqual(len(new_rows), 6)
        self.assertEqual(len({r["Preset_ID"] for r in old_rows + new_rows}), 46)
        text = CONTENT.read_text(encoding="utf-8")
        self.assertIn("not recovered source text", text)
        self.assertIn("does not rewrite the forty retained source profiles", text)


if __name__ == "__main__":
    unittest.main()
