import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
MODEL = ENV_DIR / "ENV-04_OVERLAY_MODEL_v1.0.0.json"
LIBRARY = ENV_DIR / "ENV-11_WEATHER_CLIMATE_DISASTER_OVERLAY_LIBRARY_v1.0.0.json"
MATRIX = ENV_DIR / "ENV-11_OVERLAY_INTERACTION_MATRIX_v1.0.0.csv"
GUIDE = ENV_DIR / "ENV-11_WEATHER_CLIMATE_DISASTER_OVERLAY_GUIDE.md"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"
PRESET_FILES = [
    ENV_DIR / "ENV-05_PRESET_REGISTRY_v1.0.0.csv",
    ENV_DIR / "ENV-06_FRESHWATER_WETLAND_PRESET_REGISTRY_v1.0.0.csv",
    ENV_DIR / "ENV-07_COASTAL_MARINE_PRESET_REGISTRY_v1.0.0.csv",
    ENV_DIR / "ENV-08_OPEN_COUNTRY_DRY_LANDFORMS_PRESET_REGISTRY_v1.0.0.csv",
    ENV_DIR / "ENV-09_COLD_ALPINE_POLAR_PRESET_REGISTRY_v1.0.0.csv",
    ENV_DIR / "ENV-10_SETTLED_INDUSTRIAL_INFRASTRUCTURE_PRESET_REGISTRY_v1.0.0.csv",
]


class Env11WeatherClimateDisasterOverlayTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_exact_22_unique_overlay_identities(self):
        library = self.load_json(LIBRARY)
        overlays = library["overlays"]
        self.assertEqual(library["overlay_count"], 22)
        self.assertEqual(len(overlays), 22)
        ids = [o["overlay_id"] for o in overlays]
        names = [o["name"] for o in overlays]
        self.assertEqual(len(set(ids)), 22)
        self.assertEqual(len(set(names)), 22)
        expected = {
            "OVL-WTH-HEAVY-RAIN", "OVL-WTH-MONSOON", "OVL-WTH-FOG",
            "OVL-WTH-THUNDERSTORM", "OVL-WTH-HEAVY-SNOW", "OVL-WTH-BLIZZARD",
            "OVL-WTH-WINDSTORM", "OVL-WTH-HURRICANE", "OVL-WTH-TORNADO",
            "OVL-WTH-SANDSTORM", "OVL-WTH-HAIL", "OVL-HYD-FLOOD",
            "OVL-HYD-FLASH-FLOOD", "OVL-HYD-DROUGHT", "OVL-HYD-STORM-SURGE",
            "OVL-HYD-TSUNAMI-SEICHE", "OVL-ECO-WILDFIRE", "OVL-GEO-VOLCANIC-ASH",
            "OVL-GEO-VOLCANIC-ERUPTION", "OVL-GEO-EARTHQUAKE",
            "OVL-GEO-AVALANCHE", "OVL-GEO-LANDSLIDE",
        }
        self.assertEqual(set(ids), expected)

    def test_every_definition_satisfies_env04_contract(self):
        model = self.load_json(MODEL)
        library = self.load_json(LIBRARY)
        contract = model["overlay_definition_contract"]
        families = {f["id"] for f in model["overlay_families"]}
        operations = set(contract["allowed_delta_operations"])
        stack_modes = set(contract["stack_modes"])
        relation_types = set(model["relation_types"])
        required = set(contract["required_fields"])
        delta_required = set(contract["delta_requirements"])
        ids = {o["overlay_id"] for o in library["overlays"]}

        for overlay in library["overlays"]:
            self.assertTrue(required.issubset(overlay), overlay["overlay_id"])
            self.assertIn(overlay["family_id"], families)
            self.assertTrue(overlay["target_domains"])
            self.assertTrue(overlay["applicability"])
            self.assertTrue(overlay["deltas"])
            self.assertEqual(overlay["provenance"]["classification"], "owner_authored")
            self.assertFalse(overlay["provenance"]["source_text_claimed"])
            for delta in overlay["deltas"]:
                self.assertTrue(delta_required.issubset(delta), overlay["overlay_id"])
                self.assertIn(delta["operation"], operations)
                self.assertIn(delta["stack_mode"], stack_modes)
                self.assertTrue(delta["effect_key"])
            for relation in overlay.get("relations", []):
                self.assertIn(relation["type"], relation_types)
                self.assertIn(relation["target"], ids)

        for relation in library["authored_cross_overlay_relations"]:
            self.assertIn(relation["type"], relation_types)
            self.assertIn(relation["source"], ids)
            self.assertIn(relation["target"], ids)

    def test_interaction_matrix_forbids_automatic_activation(self):
        rows = self.load_csv(MATRIX)
        self.assertGreaterEqual(len(rows), 16)
        self.assertTrue(all(r["Automatic_Activation"] == "NO" for r in rows))
        expected_edges = {
            ("OVL-WTH-HEAVY-RAIN", "amplifies", "OVL-HYD-FLOOD"),
            ("OVL-HYD-DROUGHT", "amplifies", "OVL-ECO-WILDFIRE"),
            ("OVL-GEO-EARTHQUAKE", "amplifies", "OVL-GEO-LANDSLIDE"),
            ("OVL-WTH-HURRICANE", "amplifies", "OVL-HYD-STORM-SURGE"),
            ("OVL-WTH-BLIZZARD", "supersedes", "OVL-WTH-HEAVY-SNOW"),
            ("OVL-HYD-FLASH-FLOOD", "transforms_with", "OVL-HYD-FLOOD"),
        }
        actual = {(r["Source_Overlay_ID"], r["Relation"], r["Target_Overlay_ID"]) for r in rows}
        self.assertTrue(expected_edges.issubset(actual))

    def test_no_hidden_event_engine_and_preset_boundaries_are_explicit(self):
        library = self.load_json(LIBRARY)
        self.assertFalse(library["authority_boundary"]["automatic_event_causation_authorized"])
        self.assertGreaterEqual(len(library["explicit_non_causation_examples"]), 8)
        guide = GUIDE.read_text(encoding="utf-8")
        for phrase in [
            "does **not** turn plausible physical causation into automatic overlay activation",
            "Heavy Rain does not automatically create Flood",
            "Drought does not automatically create Wildfire",
            "Earthquake does not automatically create Landslide or Tsunami",
            "Hurricane does not automatically create Storm Surge or Tornado",
            "Volcano does not imply Volcanic Eruption or Volcanic Ash",
            "Alpine/High Mountain does not imply Avalanche",
        ]:
            self.assertIn(phrase, guide)

    def test_env12_env13_env15_and_cew_boundaries_remain_intact(self):
        library = self.load_json(LIBRARY)
        boundary = library["authority_boundary"]
        self.assertFalse(boundary["application_implementation_authority"])
        self.assertFalse(boundary["runtime_schema_mutation_authorized"])
        self.assertEqual(boundary["planetary_physical_condition_overlays_deferred_to"], "ENV-12")
        self.assertEqual(boundary["supernatural_multiversal_overlays_deferred_to"], "ENV-13")
        self.assertEqual(boundary["habitat_signature_vocabulary_deferred_to"], "ENV-15")
        self.assertEqual(boundary["creature_distribution_owned_by"], "CEW")
        names = {o["name"] for o in library["overlays"]}
        for forbidden in [
            "Extreme Heat", "Extreme Cold", "Low Oxygen", "Radiation", "Vacuum",
            "Low Gravity", "High Gravity", "Zero Gravity", "Magical Saturation",
            "Magical Dead Zone", "Reality Instability", "Dimensional Bleed",
            "Psychic Influence", "Temporal Instability", "Chaos/Foam Influence",
        ]:
            self.assertNotIn(forbidden, names)

    def test_env11_changes_no_preset_or_archetype_count(self):
        preset_rows = []
        for path in PRESET_FILES:
            preset_rows.extend(self.load_csv(path))
        self.assertEqual(len(preset_rows), 76)
        self.assertEqual(len({r["Preset_ID"] for r in preset_rows}), 76)
        backlog = self.load_json(BACKLOG)
        self.assertEqual(backlog["env10_decisions"]["current_preset_count"], 76)
        self.assertEqual(backlog["env10_decisions"]["current_composed_archetype_count"], 19)
        self.assertFalse(backlog["application_implementation_authority"])

    def test_effect_key_deduplication_examples_exist(self):
        overlays = {o["overlay_id"]: o for o in self.load_json(LIBRARY)["overlays"]}
        def keys(oid):
            return {d["effect_key"] for d in overlays[oid]["deltas"]}
        self.assertIn("visibility.precipitation_obscuration", keys("OVL-WTH-HEAVY-RAIN") & keys("OVL-WTH-HURRICANE"))
        self.assertIn("movement.high_wind_complication", keys("OVL-WTH-WINDSTORM") & keys("OVL-WTH-HURRICANE") & keys("OVL-WTH-TORNADO") & keys("OVL-WTH-BLIZZARD"))
        self.assertIn("atmosphere.particulate_load", keys("OVL-WTH-SANDSTORM") & keys("OVL-GEO-VOLCANIC-ASH"))
        self.assertIn("hazard.mass_movement_burial", keys("OVL-GEO-AVALANCHE") & keys("OVL-GEO-LANDSLIDE"))


if __name__ == "__main__":
    unittest.main()
