import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
MODEL = ENV_DIR / "ENV-05_PRESET_MODEL_v1.0.0.json"
REGISTRY = ENV_DIR / "ENV-05_PRESET_REGISTRY_v1.0.0.csv"
CROSSWALK = ENV_DIR / "ENV-03_PROFILE_ARCHETYPE_CROSSWALK_v1.0.0.csv"
ARCHETYPES = ENV_DIR / "ENV-03_ARCHETYPE_LIBRARY_v1.0.0.json"
OVERLAYS = ENV_DIR / "ENV-04_OVERLAY_MODEL_v1.0.0.json"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env05PresetConversionTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_exactly_40_unique_source_backed_presets_exist(self):
        rows = self.load_csv(REGISTRY)
        self.assertEqual(len(rows), 40)
        self.assertEqual(len({r["Preset_ID"] for r in rows}), 40)
        self.assertEqual(len({r["Source_Environment_Definition_ID"] for r in rows}), 40)
        self.assertTrue(all(r["Minimum_Profile_Complete"] == "YES" for r in rows))
        self.assertTrue(all(r["Source_Profile_Immutable"] == "YES" for r in rows))
        self.assertTrue(all(r["Conversion_State"] == "converted_source_backed_preset" for r in rows))

    def test_preset_archetypes_exactly_preserve_env03_crosswalk(self):
        registry = {r["Source_Environment_Definition_ID"]: r for r in self.load_csv(REGISTRY)}
        crosswalk = {r["Environment_Definition_ID"]: r for r in self.load_csv(CROSSWALK)}
        valid_ids = {a["id"] for a in self.load_json(ARCHETYPES)["archetypes"]}
        self.assertEqual(set(registry), set(crosswalk))
        for source_id, src in crosswalk.items():
            row = registry[source_id]
            self.assertEqual(row["Preset_Name"], src["Environment_Name"])
            self.assertEqual(row["Primary_Archetype_ID"], src["Primary_Archetype_ID"])
            self.assertEqual(row["Secondary_Archetype_IDs"], src["Secondary_Archetype_IDs"])
            self.assertIn(row["Primary_Archetype_ID"], valid_ids)
            for secondary in filter(None, row["Secondary_Archetype_IDs"].split("|")):
                self.assertIn(secondary, valid_ids)
        self.assertEqual(sum(bool(r["Secondary_Archetype_IDs"]) for r in registry.values()), 12)

    def test_overlay_hints_are_family_only_and_do_not_invent_concrete_overlays(self):
        rows = self.load_csv(REGISTRY)
        families = {f["id"] for f in self.load_json(OVERLAYS)["overlay_families"]}
        for row in rows:
            hints = [x for x in row["Deferred_Overlay_Family_Hints"].split("|") if x]
            self.assertTrue(set(hints).issubset(families), row["Preset_Name"])
            self.assertFalse(any(x.startswith("OVL-") for x in hints), row["Preset_Name"])
        model = self.load_json(MODEL)
        self.assertFalse(model["authority_boundary"]["concrete_overlay_library_authored"])
        self.assertTrue(model["authority_boundary"]["overlay_family_hints_are_not_overlay_definitions"])

    def test_broad_style_and_state_context_does_not_become_overlay_identity(self):
        rows = {r["Preset_Name"]: r for r in self.load_csv(REGISTRY)}
        self.assertIn("post_apocalyptic", rows["Post-Apocalyptic Radioactive Zone"]["Preset_Context_Tags"])
        self.assertIn("post_apocalyptic", rows["Post-Apocalyptic Overgrown City"]["Preset_Context_Tags"])
        self.assertIn("cyberpunk", rows["Cyberpunk City"]["Preset_Context_Tags"])
        self.assertNotIn("post_apocalyptic", rows["Post-Apocalyptic Radioactive Zone"]["Deferred_Overlay_Family_Hints"])
        self.assertNotIn("cyberpunk", rows["Cyberpunk City"]["Deferred_Overlay_Family_Hints"])

    def test_model_preserves_source_and_parallel_software_boundaries(self):
        model = self.load_json(MODEL)
        self.assertEqual(model["preset_count"], 40)
        self.assertEqual(model["compound_preset_count"], 12)
        self.assertEqual(model["unmapped_presets"], 0)
        boundary = model["authority_boundary"]
        self.assertFalse(boundary["application_implementation_authority"])
        self.assertFalse(boundary["runtime_schema_mutation_authorized"])
        self.assertFalse(boundary["source_profiles_mutated"])
        self.assertFalse(boundary["source_profile_text_duplicated_into_presets"])
        self.assertEqual(boundary["habitat_signature_vocabulary_deferred_to"], "ENV-15")
        self.assertEqual(boundary["creature_distribution_owned_by"], "CEW")

    def test_backlog_closes_env05_and_selects_env06(self):
        backlog = self.load_json(BACKLOG)
        order = backlog["strict_order"]
        completed = [item["id"] for item in backlog["tranches"] if item["status"] == "completed_verified"]
        self.assertEqual(completed, order[:5])
        self.assertEqual(backlog["completed_through"], "ENV-05")
        self.assertEqual(backlog["current_item"], "ENV-06")
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        self.assertEqual(statuses["ENV-05"], "completed_verified")
        self.assertEqual(statuses["ENV-06"], "selected_not_started")
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
