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
ENV09_ARCH = ENV_DIR / "ENV-09_ARCHETYPE_EXTENSION_v1.0.0.json"
EXT = ENV_DIR / "ENV-10_ARCHETYPE_EXTENSION_v1.0.0.json"
REGISTRY = ENV_DIR / "ENV-10_SETTLED_INDUSTRIAL_INFRASTRUCTURE_PRESET_REGISTRY_v1.0.0.csv"
CONTENT = ENV_DIR / "ENV-10_SETTLED_INDUSTRIAL_INFRASTRUCTURE_CONTENT_v1.0.0.md"
REPORT = ENV_DIR / "ENV-10_SETTLED_INDUSTRIAL_INFRASTRUCTURE_EXPANSION_REPORT.md"
OVERLAYS = ENV_DIR / "ENV-04_OVERLAY_MODEL_v1.0.0.json"
ENV05 = ENV_DIR / "ENV-05_PRESET_REGISTRY_v1.0.0.csv"
ENV06 = ENV_DIR / "ENV-06_FRESHWATER_WETLAND_PRESET_REGISTRY_v1.0.0.csv"
ENV07 = ENV_DIR / "ENV-07_COASTAL_MARINE_PRESET_REGISTRY_v1.0.0.csv"
ENV08 = ENV_DIR / "ENV-08_OPEN_COUNTRY_DRY_LANDFORMS_PRESET_REGISTRY_v1.0.0.csv"
ENV09 = ENV_DIR / "ENV-09_COLD_ALPINE_POLAR_PRESET_REGISTRY_v1.0.0.csv"


class Env10SettledIndustrialInfrastructureTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_transport_corridor_is_only_env10_archetype_extension(self):
        base = self.load_json(BASE_ARCH)
        env06 = self.load_json(ENV06_ARCH)
        env07 = self.load_json(ENV07_ARCH)
        env09 = self.load_json(ENV09_ARCH)
        ext = self.load_json(EXT)
        self.assertEqual(base["archetype_count"], 15)
        self.assertEqual(env06["authority_boundary"]["current_composed_archetype_count"], 16)
        self.assertEqual(env07["authority_boundary"]["current_composed_archetype_count"], 17)
        self.assertEqual(env09["authority_boundary"]["current_composed_archetype_count"], 18)
        self.assertEqual(ext["authority_boundary"]["extension_archetype_count"], 1)
        self.assertEqual(ext["authority_boundary"]["current_composed_archetype_count"], 19)
        self.assertEqual([a["id"] for a in ext["archetypes"]], ["ARCH-TRANSPORT-CORRIDOR"])
        self.assertEqual(ext["decision"]["watch_item"], "road/trail corridor behavior")
        self.assertEqual(ext["decision"]["result"], "promote_new_archetype")
        self.assertFalse(ext["authority_boundary"]["application_implementation_authority"])
        self.assertEqual(ext["authority_boundary"]["habitat_signature_vocabulary_deferred_to"], "ENV-15")
        self.assertEqual(ext["authority_boundary"]["creature_distribution_owned_by"], "CEW")

    def test_exact_ten_presets_are_added(self):
        rows = self.load_csv(REGISTRY)
        expected = {
            "Farmland / Agricultural Countryside", "Suburb / Residential District",
            "Frontier Outpost", "Road / Wilderness Trail", "Mine / Quarry",
            "Factory / Refinery", "Power Plant / Utility Complex",
            "Fortress / Military Base", "Transit Hub / Terminal", "Harbor / Dockyards",
        }
        self.assertEqual(len(rows), 10)
        self.assertEqual({r["Preset_Name"] for r in rows}, expected)
        self.assertEqual(len({r["Preset_ID"] for r in rows}), 10)
        self.assertTrue(all(r["Minimum_Profile_Complete"] == "YES" for r in rows))
        self.assertTrue(all(r["Authored_Expansion"] == "YES" for r in rows))
        self.assertTrue(all(r["Application_Implementation_Authority"] == "NO" for r in rows))
        self.assertTrue(all(r["Habitat_Signature_State"] == "deferred_to_ENV-15" for r in rows))
        self.assertTrue(all(r["Creature_Distribution_State"] == "deferred_to_CEW" for r in rows))

    def test_archetype_composition_uses_existing_semantics_plus_transport_corridor(self):
        valid = {a["id"] for a in self.load_json(BASE_ARCH)["archetypes"]}
        valid |= {a["id"] for a in self.load_json(ENV06_ARCH)["archetypes"]}
        valid |= {a["id"] for a in self.load_json(ENV07_ARCH)["archetypes"]}
        valid |= {a["id"] for a in self.load_json(ENV09_ARCH)["archetypes"]}
        valid |= {a["id"] for a in self.load_json(EXT)["archetypes"]}
        rows = {r["Preset_Name"]: r for r in self.load_csv(REGISTRY)}
        for row in rows.values():
            self.assertIn(row["Primary_Archetype_ID"], valid)
            for secondary in filter(None, row["Secondary_Archetype_IDs"].split("|")):
                self.assertIn(secondary, valid)
        self.assertEqual(rows["Road / Wilderness Trail"]["Primary_Archetype_ID"], "ARCH-TRANSPORT-CORRIDOR")
        self.assertEqual(rows["Farmland / Agricultural Countryside"]["Primary_Archetype_ID"], "ARCH-OPEN-COUNTRY")
        self.assertEqual(rows["Suburb / Residential District"]["Primary_Archetype_ID"], "ARCH-SETTLEMENT")
        self.assertEqual(rows["Mine / Quarry"]["Primary_Archetype_ID"], "ARCH-INFRASTRUCTURE")
        self.assertIn("ARCH-TRANSPORT-CORRIDOR", rows["Transit Hub / Terminal"]["Secondary_Archetype_IDs"])
        self.assertIn("ARCH-COASTAL", rows["Harbor / Dockyards"]["Secondary_Archetype_IDs"])

    def test_overlay_hooks_are_family_only(self):
        rows = self.load_csv(REGISTRY)
        families = {f["id"] for f in self.load_json(OVERLAYS)["overlay_families"]}
        for row in rows:
            hints = {x for x in row["Overlay_Family_Hints"].split("|") if x}
            self.assertTrue(hints.issubset(families), row["Preset_Name"])
            self.assertFalse(any(x.startswith("OVL-") for x in hints), row["Preset_Name"])
        report = REPORT.read_text(encoding="utf-8")
        for phrase in ["Flood", "Wildfire", "Landslide", "Toxic Release", "Radiation"]:
            self.assertIn(phrase, report)

    def test_each_preset_has_minimum_content_and_d12_table(self):
        text = CONTENT.read_text(encoding="utf-8")
        sections = re.split(r"\n## (?=\d+\.)", text)[1:]
        self.assertEqual(len(sections), 10)
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

    def test_existing_source_preset_boundaries_are_explicit(self):
        report = REPORT.read_text(encoding="utf-8")
        for phrase in [
            "Suburb / Residential District is not the existing Flooded Suburbs source preset",
            "Road / Wilderness Trail is not Skeletons of Highways",
            "Factory / Refinery and Power Plant / Utility Complex remain distinct from generic Industrial Zones",
            "Harbor / Dockyards is not Port City",
        ]:
            self.assertIn(phrase, report)
        content = CONTENT.read_text(encoding="utf-8")
        self.assertIn("not recovered source text", content)
        self.assertIn("CEW owns canonical creature identities", content)

    def test_total_governed_preset_count_becomes_76(self):
        rows = self.load_csv(ENV05) + self.load_csv(ENV06) + self.load_csv(ENV07) + self.load_csv(ENV08) + self.load_csv(ENV09) + self.load_csv(REGISTRY)
        self.assertEqual(len(rows), 76)
        self.assertEqual(len({r["Preset_ID"] for r in rows}), 76)


if __name__ == "__main__":
    unittest.main()
