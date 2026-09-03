import csv
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
BASE_ARCH = ENV_DIR / "ENV-03_ARCHETYPE_LIBRARY_v1.0.0.json"
ENV06_ARCH = ENV_DIR / "ENV-06_ARCHETYPE_EXTENSION_v1.0.0.json"
ENV07_ARCH = ENV_DIR / "ENV-07_ARCHETYPE_EXTENSION_v1.0.0.json"
EVAL = ENV_DIR / "ENV-08_ARCHETYPE_EVALUATION_v1.0.0.json"
REGISTRY = ENV_DIR / "ENV-08_OPEN_COUNTRY_DRY_LANDFORMS_PRESET_REGISTRY_v1.0.0.csv"
CONTENT = ENV_DIR / "ENV-08_OPEN_COUNTRY_DRY_LANDFORMS_CONTENT_v1.0.0.md"
REPORT = ENV_DIR / "ENV-08_OPEN_COUNTRY_DRY_LANDFORMS_EXPANSION_REPORT.md"
OVERLAYS = ENV_DIR / "ENV-04_OVERLAY_MODEL_v1.0.0.json"
ENV05 = ENV_DIR / "ENV-05_PRESET_REGISTRY_v1.0.0.csv"
ENV06 = ENV_DIR / "ENV-06_FRESHWATER_WETLAND_PRESET_REGISTRY_v1.0.0.csv"
ENV07 = ENV_DIR / "ENV-07_COASTAL_MARINE_PRESET_REGISTRY_v1.0.0.csv"


class Env08OpenCountryDryLandformsTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_env08_adds_no_archetype_and_keeps_composed_count_17(self):
        base = self.load_json(BASE_ARCH)
        env06 = self.load_json(ENV06_ARCH)
        env07 = self.load_json(ENV07_ARCH)
        evaluation = self.load_json(EVAL)
        self.assertEqual(base["archetype_count"], 15)
        self.assertEqual(env06["authority_boundary"]["current_composed_archetype_count"], 16)
        self.assertEqual(env07["authority_boundary"]["current_composed_archetype_count"], 17)
        self.assertEqual(evaluation["authority_boundary"]["new_archetype_count"], 0)
        self.assertEqual(evaluation["authority_boundary"]["current_composed_archetype_count"], 17)
        self.assertEqual(evaluation["decision"]["result"], "reuse_existing_archetypes_only")
        self.assertFalse(evaluation["authority_boundary"]["application_implementation_authority"])
        self.assertEqual(evaluation["authority_boundary"]["habitat_signature_vocabulary_deferred_to"], "ENV-15")
        self.assertEqual(evaluation["authority_boundary"]["creature_distribution_owned_by"], "CEW")

    def test_exact_eight_presets_are_added(self):
        rows = self.load_csv(REGISTRY)
        expected = {
            "Grassland / Prairie", "Savanna", "Steppe", "Scrubland / Chaparral",
            "Hills / Uplands", "Canyon / Badlands", "Rocky Desert", "Salt Flats",
        }
        self.assertEqual(len(rows), 8)
        self.assertEqual({r["Preset_Name"] for r in rows}, expected)
        self.assertEqual(len({r["Preset_ID"] for r in rows}), 8)
        self.assertTrue(all(r["Minimum_Profile_Complete"] == "YES" for r in rows))
        self.assertTrue(all(r["Authored_Expansion"] == "YES" for r in rows))
        self.assertTrue(all(r["Application_Implementation_Authority"] == "NO" for r in rows))
        self.assertTrue(all(r["Habitat_Signature_State"] == "deferred_to_ENV-15" for r in rows))
        self.assertTrue(all(r["Creature_Distribution_State"] == "deferred_to_CEW" for r in rows))

    def test_archetype_composition_uses_only_existing_ids(self):
        valid = {a["id"] for a in self.load_json(BASE_ARCH)["archetypes"]}
        valid |= {a["id"] for a in self.load_json(ENV06_ARCH)["archetypes"]}
        valid |= {a["id"] for a in self.load_json(ENV07_ARCH)["archetypes"]}
        rows = {r["Preset_Name"]: r for r in self.load_csv(REGISTRY)}
        for row in rows.values():
            self.assertIn(row["Primary_Archetype_ID"], valid)
            for secondary in filter(None, row["Secondary_Archetype_IDs"].split("|")):
                self.assertIn(secondary, valid)
        for name in ["Grassland / Prairie", "Savanna", "Steppe", "Scrubland / Chaparral", "Salt Flats"]:
            self.assertEqual(rows[name]["Primary_Archetype_ID"], "ARCH-OPEN-COUNTRY")
        self.assertEqual(rows["Hills / Uplands"]["Primary_Archetype_ID"], "ARCH-HIGHLAND")
        self.assertEqual(rows["Hills / Uplands"]["Secondary_Archetype_IDs"], "ARCH-OPEN-COUNTRY")
        self.assertEqual(rows["Canyon / Badlands"]["Primary_Archetype_ID"], "ARCH-HIGHLAND")
        self.assertEqual(rows["Rocky Desert"]["Secondary_Archetype_IDs"], "ARCH-HIGHLAND")

    def test_overlay_hooks_are_family_only(self):
        rows = self.load_csv(REGISTRY)
        families = {f["id"] for f in self.load_json(OVERLAYS)["overlay_families"]}
        for row in rows:
            hints = {x for x in row["Overlay_Family_Hints"].split("|") if x}
            self.assertTrue(hints.issubset(families), row["Preset_Name"])
            self.assertFalse(any(x.startswith("OVL-") for x in hints), row["Preset_Name"])
        report = REPORT.read_text(encoding="utf-8")
        for phrase in ["Extreme Heat", "Drought", "Wildfire", "Sandstorm/Dust Storm"]:
            self.assertIn(phrase, report)

    def test_each_preset_has_minimum_content_and_d12_table(self):
        text = CONTENT.read_text(encoding="utf-8")
        sections = re.split(r"\n## (?=\d+\.)", text)[1:]
        self.assertEqual(len(sections), 8)
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

    def test_key_preset_overlay_and_existing_preset_boundaries_are_explicit(self):
        report = REPORT.read_text(encoding="utf-8")
        for phrase in [
            "Grassland/Prairie does not imply Wildfire",
            "Savanna does not imply Drought or Extreme Heat",
            "Canyon/Badlands do not imply active Flash Flood",
            "Rocky Desert is distinct from the existing Sandy Desert",
            "Salt Flats do not universally imply caustic chemistry",
        ]:
            self.assertIn(phrase, report)
        content = CONTENT.read_text(encoding="utf-8")
        self.assertIn("CEW owns those mappings", content)
        self.assertIn("not recovered source text", content)

    def test_total_governed_preset_count_becomes_60(self):
        rows = self.load_csv(ENV05) + self.load_csv(ENV06) + self.load_csv(ENV07) + self.load_csv(REGISTRY)
        self.assertEqual(len(rows), 60)
        self.assertEqual(len({r["Preset_ID"] for r in rows}), 60)


if __name__ == "__main__":
    unittest.main()
