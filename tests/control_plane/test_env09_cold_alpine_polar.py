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
EXT = ENV_DIR / "ENV-09_ARCHETYPE_EXTENSION_v1.0.0.json"
REGISTRY = ENV_DIR / "ENV-09_COLD_ALPINE_POLAR_PRESET_REGISTRY_v1.0.0.csv"
CONTENT = ENV_DIR / "ENV-09_COLD_ALPINE_POLAR_CONTENT_v1.0.0.md"
REPORT = ENV_DIR / "ENV-09_COLD_ALPINE_POLAR_EXPANSION_REPORT.md"
OVERLAYS = ENV_DIR / "ENV-04_OVERLAY_MODEL_v1.0.0.json"
ENV05 = ENV_DIR / "ENV-05_PRESET_REGISTRY_v1.0.0.csv"
ENV06 = ENV_DIR / "ENV-06_FRESHWATER_WETLAND_PRESET_REGISTRY_v1.0.0.csv"
ENV07 = ENV_DIR / "ENV-07_COASTAL_MARINE_PRESET_REGISTRY_v1.0.0.csv"
ENV08 = ENV_DIR / "ENV-08_OPEN_COUNTRY_DRY_LANDFORMS_PRESET_REGISTRY_v1.0.0.csv"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env09ColdAlpinePolarTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_persistent_ice_is_only_env09_archetype_extension(self):
        base = self.load_json(BASE_ARCH)
        env06 = self.load_json(ENV06_ARCH)
        env07 = self.load_json(ENV07_ARCH)
        ext = self.load_json(EXT)
        self.assertEqual(base["archetype_count"], 15)
        self.assertEqual(env06["authority_boundary"]["current_composed_archetype_count"], 16)
        self.assertEqual(env07["authority_boundary"]["current_composed_archetype_count"], 17)
        self.assertEqual(ext["authority_boundary"]["extension_archetype_count"], 1)
        self.assertEqual(ext["authority_boundary"]["current_composed_archetype_count"], 18)
        self.assertEqual([a["id"] for a in ext["archetypes"]], ["ARCH-ICE-MASS"])
        self.assertEqual(ext["decision"]["watch_item"], "ice/glacier traversal behavior")
        self.assertEqual(ext["decision"]["result"], "promote_new_archetype")
        self.assertFalse(ext["authority_boundary"]["application_implementation_authority"])

    def test_exact_six_cold_alpine_polar_presets_are_added(self):
        rows = self.load_csv(REGISTRY)
        expected = {
            "Taiga / Boreal Forest", "Tundra", "Alpine / High Mountain",
            "Glacier / Icefield", "Polar Ice", "Sea Ice",
        }
        self.assertEqual(len(rows), 6)
        self.assertEqual({r["Preset_Name"] for r in rows}, expected)
        self.assertEqual(len({r["Preset_ID"] for r in rows}), 6)
        self.assertTrue(all(r["Minimum_Profile_Complete"] == "YES" for r in rows))
        self.assertTrue(all(r["Authored_Expansion"] == "YES" for r in rows))
        self.assertTrue(all(r["Application_Implementation_Authority"] == "NO" for r in rows))
        self.assertTrue(all(r["Habitat_Signature_State"] == "deferred_to_ENV-15" for r in rows))
        self.assertTrue(all(r["Creature_Distribution_State"] == "deferred_to_CEW" for r in rows))

    def test_archetype_composition_uses_expected_existing_and_ice_ids(self):
        valid = {a["id"] for a in self.load_json(BASE_ARCH)["archetypes"]}
        valid |= {a["id"] for a in self.load_json(ENV06_ARCH)["archetypes"]}
        valid |= {a["id"] for a in self.load_json(ENV07_ARCH)["archetypes"]}
        valid |= {a["id"] for a in self.load_json(EXT)["archetypes"]}
        rows = {r["Preset_Name"]: r for r in self.load_csv(REGISTRY)}
        for row in rows.values():
            self.assertIn(row["Primary_Archetype_ID"], valid)
            for secondary in filter(None, row["Secondary_Archetype_IDs"].split("|")):
                self.assertIn(secondary, valid)
        self.assertEqual(rows["Taiga / Boreal Forest"]["Primary_Archetype_ID"], "ARCH-FOREST")
        self.assertEqual(rows["Tundra"]["Primary_Archetype_ID"], "ARCH-OPEN-COUNTRY")
        self.assertEqual(rows["Alpine / High Mountain"]["Primary_Archetype_ID"], "ARCH-HIGHLAND")
        self.assertEqual(rows["Glacier / Icefield"]["Primary_Archetype_ID"], "ARCH-ICE-MASS")
        self.assertEqual(rows["Glacier / Icefield"]["Secondary_Archetype_IDs"], "ARCH-HIGHLAND")
        self.assertEqual(rows["Polar Ice"]["Secondary_Archetype_IDs"], "ARCH-OPEN-COUNTRY")
        self.assertEqual(rows["Sea Ice"]["Secondary_Archetype_IDs"], "ARCH-OPEN-WATER")

    def test_overlay_hooks_are_family_only_and_cold_is_not_hard_coded(self):
        rows = self.load_csv(REGISTRY)
        families = {f["id"] for f in self.load_json(OVERLAYS)["overlay_families"]}
        for row in rows:
            hints = {x for x in row["Overlay_Family_Hints"].split("|") if x}
            self.assertTrue(hints.issubset(families), row["Preset_Name"])
            self.assertFalse(any(x.startswith("OVL-") for x in hints), row["Preset_Name"])
        report = REPORT.read_text(encoding="utf-8")
        for phrase in ["Extreme Cold", "Blizzard", "Low Oxygen", "Active Avalanche"]:
            self.assertIn(phrase, report)

    def test_each_preset_has_minimum_content_and_d12_table(self):
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

    def test_existing_combined_source_preset_is_preserved(self):
        old_rows = {r["Preset_Name"]: r for r in self.load_csv(ENV05)}
        self.assertIn("Arctic Tundra and Taiga", old_rows)
        row = old_rows["Arctic Tundra and Taiga"]
        self.assertEqual(row["Source_Profile_Immutable"], "YES")
        self.assertIn("compound profile split deferred to ENV-09", row["Source_Trait_Notes"])
        report = REPORT.read_text(encoding="utf-8")
        self.assertIn("preserved unchanged as historical/source provenance", report)

    def test_total_governed_preset_count_becomes_66(self):
        rows = self.load_csv(ENV05) + self.load_csv(ENV06) + self.load_csv(ENV07) + self.load_csv(ENV08) + self.load_csv(REGISTRY)
        self.assertEqual(len(rows), 66)
        self.assertEqual(len({r["Preset_ID"] for r in rows}), 66)
        content = CONTENT.read_text(encoding="utf-8")
        self.assertIn("not recovered source text", content)
        self.assertIn("CEW owns those mappings", content)

    def test_backlog_closes_env09_and_selects_env10(self):
        backlog = self.load_json(BACKLOG)
        order = backlog["strict_order"]
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        completed = [item["id"] for item in backlog["tranches"] if item["status"] == "completed_verified"]
        self.assertEqual(completed, order[:9])
        self.assertEqual(backlog["completed_through"], "ENV-09")
        self.assertEqual(backlog["current_item"], "ENV-10")
        self.assertEqual(statuses["ENV-09"], "completed_verified")
        self.assertEqual(statuses["ENV-10"], "selected_not_started")
        decisions = backlog["env09_decisions"]
        self.assertEqual(decisions["current_preset_count"], 66)
        self.assertEqual(decisions["new_archetypes_added"], 1)
        self.assertEqual(decisions["new_archetype_ids"], ["ARCH-ICE-MASS"])
        self.assertEqual(decisions["current_composed_archetype_count"], 18)
        self.assertTrue(decisions["legacy_arctic_tundra_taiga_source_preset_preserved"])
        self.assertTrue(decisions["extreme_cold_blizzard_low_oxygen_deferred"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
