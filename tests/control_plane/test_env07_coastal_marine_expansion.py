import csv
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
BASE_ARCH = ENV_DIR / "ENV-03_ARCHETYPE_LIBRARY_v1.0.0.json"
ENV06_ARCH = ENV_DIR / "ENV-06_ARCHETYPE_EXTENSION_v1.0.0.json"
EXT = ENV_DIR / "ENV-07_ARCHETYPE_EXTENSION_v1.0.0.json"
REGISTRY = ENV_DIR / "ENV-07_COASTAL_MARINE_PRESET_REGISTRY_v1.0.0.csv"
CONTENT = ENV_DIR / "ENV-07_COASTAL_MARINE_CONTENT_v1.0.0.md"
REPORT = ENV_DIR / "ENV-07_COASTAL_MARINE_EXPANSION_REPORT.md"
OVERLAYS = ENV_DIR / "ENV-04_OVERLAY_MODEL_v1.0.0.json"
ENV05 = ENV_DIR / "ENV-05_PRESET_REGISTRY_v1.0.0.csv"
ENV06 = ENV_DIR / "ENV-06_FRESHWATER_WETLAND_PRESET_REGISTRY_v1.0.0.csv"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env07CoastalMarineExpansionTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_aquatic_structure_is_the_only_env07_archetype_extension(self):
        base = self.load_json(BASE_ARCH)
        prior = self.load_json(ENV06_ARCH)
        ext = self.load_json(EXT)
        self.assertEqual(base["archetype_count"], 15)
        self.assertEqual(prior["authority_boundary"]["current_composed_archetype_count"], 16)
        self.assertEqual(ext["authority_boundary"]["extension_archetype_count"], 1)
        self.assertEqual(ext["authority_boundary"]["current_composed_archetype_count"], 17)
        self.assertEqual([a["id"] for a in ext["archetypes"]], ["ARCH-AQUATIC-STRUCTURE"])
        self.assertEqual(ext["decision"]["watch_item"], "reef/kelp dense aquatic structure")
        self.assertEqual(ext["decision"]["result"], "promote_new_archetype")
        self.assertFalse(ext["authority_boundary"]["application_implementation_authority"])
        self.assertEqual(ext["authority_boundary"]["habitat_signature_vocabulary_deferred_to"], "ENV-15")
        self.assertEqual(ext["authority_boundary"]["creature_distribution_owned_by"], "CEW")

    def test_exact_six_coastal_marine_presets_are_added(self):
        rows = self.load_csv(REGISTRY)
        expected = {
            "Coast / Shoreline / Beach", "Tidal Flats", "Coral Reef",
            "Kelp Forest", "Deep Ocean / Abyssal", "Ocean Trench",
        }
        self.assertEqual(len(rows), 6)
        self.assertEqual({r["Preset_Name"] for r in rows}, expected)
        self.assertEqual(len({r["Preset_ID"] for r in rows}), 6)
        self.assertTrue(all(r["Minimum_Profile_Complete"] == "YES" for r in rows))
        self.assertTrue(all(r["Authored_Expansion"] == "YES" for r in rows))
        self.assertTrue(all(r["Application_Implementation_Authority"] == "NO" for r in rows))
        self.assertTrue(all(r["Habitat_Signature_State"] == "deferred_to_ENV-15" for r in rows))
        self.assertTrue(all(r["Creature_Distribution_State"] == "deferred_to_CEW" for r in rows))

    def test_archetype_composition_reuses_existing_semantics(self):
        base_ids = {a["id"] for a in self.load_json(BASE_ARCH)["archetypes"]}
        prior_ids = {a["id"] for a in self.load_json(ENV06_ARCH)["archetypes"]}
        ext_ids = {a["id"] for a in self.load_json(EXT)["archetypes"]}
        valid = base_ids | prior_ids | ext_ids
        rows = {r["Preset_Name"]: r for r in self.load_csv(REGISTRY)}
        for row in rows.values():
            self.assertIn(row["Primary_Archetype_ID"], valid)
            for secondary in filter(None, row["Secondary_Archetype_IDs"].split("|")):
                self.assertIn(secondary, valid)
        self.assertEqual(rows["Coast / Shoreline / Beach"]["Primary_Archetype_ID"], "ARCH-COASTAL")
        self.assertEqual(rows["Coast / Shoreline / Beach"]["Secondary_Archetype_IDs"], "ARCH-OPEN-COUNTRY")
        self.assertEqual(rows["Tidal Flats"]["Secondary_Archetype_IDs"], "ARCH-WETLAND")
        self.assertEqual(rows["Coral Reef"]["Primary_Archetype_ID"], "ARCH-AQUATIC-STRUCTURE")
        self.assertEqual(rows["Coral Reef"]["Secondary_Archetype_IDs"], "ARCH-SUBMERGED")
        self.assertEqual(rows["Kelp Forest"]["Primary_Archetype_ID"], "ARCH-AQUATIC-STRUCTURE")
        self.assertEqual(rows["Deep Ocean / Abyssal"]["Primary_Archetype_ID"], "ARCH-SUBMERGED")
        self.assertEqual(rows["Ocean Trench"]["Primary_Archetype_ID"], "ARCH-SUBMERGED")

    def test_overlay_hooks_are_family_only_and_concrete_conditions_remain_deferred(self):
        rows = self.load_csv(REGISTRY)
        families = {f["id"] for f in self.load_json(OVERLAYS)["overlay_families"]}
        for row in rows:
            hints = {x for x in row["Overlay_Family_Hints"].split("|") if x}
            self.assertTrue(hints.issubset(families), row["Preset_Name"])
            self.assertFalse(any(x.startswith("OVL-") for x in hints), row["Preset_Name"])
        report = REPORT.read_text(encoding="utf-8")
        self.assertIn("does not author executable Tide, Storm Surge, Hurricane, Extreme Pressure", report)
        self.assertIn("Overlay-family hints remain nonexecuting", report)

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

    def test_key_boundaries_remain_distinct(self):
        report = REPORT.read_text(encoding="utf-8")
        for phrase in [
            "Tidal Flats versus a high-tide/flood condition",
            "Deep Ocean versus Extreme Pressure",
            "Ocean Trench versus geologic disaster",
            "River Delta / Estuary remains its own freshwater/brackish river-mouth preset",
        ]:
            self.assertIn(phrase, report)
        self.assertIn("CEW owns canonical creature identities and world distribution", CONTENT.read_text(encoding="utf-8"))

    def test_total_governed_preset_count_becomes_52(self):
        rows = self.load_csv(ENV05) + self.load_csv(ENV06) + self.load_csv(REGISTRY)
        self.assertEqual(len(rows), 52)
        self.assertEqual(len({r["Preset_ID"] for r in rows}), 52)
        text = CONTENT.read_text(encoding="utf-8")
        self.assertIn("not recovered source text", text)
        self.assertIn("does not rewrite the forty retained source profiles", text)

    def test_env07_remains_completed_after_later_progression(self):
        backlog = self.load_json(BACKLOG)
        order = backlog["strict_order"]
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        completed = [item["id"] for item in backlog["tranches"] if item["status"] == "completed_verified"]
        self.assertEqual(completed[:7], order[:7])
        self.assertEqual(statuses["ENV-07"], "completed_verified")
        self.assertGreaterEqual(order.index(backlog["completed_through"]), order.index("ENV-07"))
        self.assertGreaterEqual(order.index(backlog["current_item"]), order.index("ENV-08"))
        self.assertEqual(backlog["env07_decisions"]["current_preset_count"], 52)
        self.assertEqual(backlog["env07_decisions"]["current_composed_archetype_count"], 17)
        self.assertEqual(backlog["env07_decisions"]["new_archetype_ids"], ["ARCH-AQUATIC-STRUCTURE"])
        self.assertTrue(backlog["env07_decisions"]["river_delta_estuary_preserved"])
        self.assertFalse(backlog["env07_decisions"]["application_runtime_mutation_authorized"])
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
