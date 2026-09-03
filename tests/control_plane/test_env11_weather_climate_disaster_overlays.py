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
        self.assertEqual(len(set(ids)), 22)
        self.assertEqual(set(ids), {
            "OVL-WTH-HEAVY-RAIN", "OVL-WTH-MONSOON", "OVL-WTH-FOG",
            "OVL-WTH-THUNDERSTORM", "OVL-WTH-HEAVY-SNOW", "OVL-WTH-BLIZZARD",
            "OVL-WTH-WINDSTORM", "OVL-WTH-HURRICANE", "OVL-WTH-TORNADO",
            "OVL-WTH-SANDSTORM", "OVL-WTH-HAIL", "OVL-HYD-FLOOD",
            "OVL-HYD-FLASH-FLOOD", "OVL-HYD-DROUGHT", "OVL-HYD-STORM-SURGE",
            "OVL-HYD-TSUNAMI-SEICHE", "OVL-ECO-WILDFIRE", "OVL-GEO-VOLCANIC-ASH",
            "OVL-GEO-VOLCANIC-ERUPTION", "OVL-GEO-EARTHQUAKE",
            "OVL-GEO-AVALANCHE", "OVL-GEO-LANDSLIDE",
        })

    def test_every_definition_satisfies_env04_contract(self):
        model = self.load_json(MODEL)
        library = self.load_json(LIBRARY)
        contract = model["overlay_definition_contract"]
        families = {f["id"] for f in model["overlay_families"]}
        operations = set(contract["allowed_delta_operations"])
        stack_modes = set(contract["stack_modes"])
        required = set(contract["required_fields"])
        delta_required = set(contract["delta_requirements"])
        for overlay in library["overlays"]:
            self.assertTrue(required.issubset(overlay), overlay["overlay_id"])
            self.assertIn(overlay["family_id"], families)
            self.assertEqual(overlay["provenance"]["classification"], "owner_authored")
            self.assertFalse(overlay["provenance"]["source_text_claimed"])
            for delta in overlay["deltas"]:
                self.assertTrue(delta_required.issubset(delta), overlay["overlay_id"])
                self.assertIn(delta["operation"], operations)
                self.assertIn(delta["stack_mode"], stack_modes)

    def test_interactions_never_auto_activate_conditions(self):
        rows = self.load_csv(MATRIX)
        self.assertGreaterEqual(len(rows), 16)
        self.assertTrue(all(r["Automatic_Activation"] == "NO" for r in rows))
        actual = {(r["Source_Overlay_ID"], r["Relation"], r["Target_Overlay_ID"]) for r in rows}
        self.assertIn(("OVL-WTH-HEAVY-RAIN", "amplifies", "OVL-HYD-FLOOD"), actual)
        self.assertIn(("OVL-HYD-DROUGHT", "amplifies", "OVL-ECO-WILDFIRE"), actual)
        self.assertIn(("OVL-WTH-BLIZZARD", "supersedes", "OVL-WTH-HEAVY-SNOW"), actual)

    def test_no_hidden_event_engine(self):
        library = self.load_json(LIBRARY)
        self.assertFalse(library["authority_boundary"]["automatic_event_causation_authorized"])
        guide = GUIDE.read_text(encoding="utf-8")
        for phrase in [
            "Heavy Rain does not automatically create Flood",
            "Drought does not automatically create Wildfire",
            "Earthquake does not automatically create Landslide or Tsunami",
            "Hurricane does not automatically create Storm Surge or Tornado",
        ]:
            self.assertIn(phrase, guide)

    def test_env11_boundaries_remain_permanent(self):
        library = self.load_json(LIBRARY)
        boundary = library["authority_boundary"]
        self.assertFalse(boundary["application_implementation_authority"])
        self.assertFalse(boundary["runtime_schema_mutation_authorized"])
        self.assertEqual(boundary["planetary_physical_condition_overlays_deferred_to"], "ENV-12")
        self.assertEqual(boundary["supernatural_multiversal_overlays_deferred_to"], "ENV-13")
        self.assertEqual(boundary["habitat_signature_vocabulary_deferred_to"], "ENV-15")
        self.assertEqual(boundary["creature_distribution_owned_by"], "CEW")

    def test_effect_key_deduplication_examples_exist(self):
        overlays = {o["overlay_id"]: o for o in self.load_json(LIBRARY)["overlays"]}
        def keys(oid):
            return {d["effect_key"] for d in overlays[oid]["deltas"]}
        self.assertIn("visibility.precipitation_obscuration", keys("OVL-WTH-HEAVY-RAIN") & keys("OVL-WTH-HURRICANE"))
        self.assertIn("movement.high_wind_complication", keys("OVL-WTH-WINDSTORM") & keys("OVL-WTH-HURRICANE") & keys("OVL-WTH-TORNADO") & keys("OVL-WTH-BLIZZARD"))
        self.assertIn("atmosphere.particulate_load", keys("OVL-WTH-SANDSTORM") & keys("OVL-GEO-VOLCANIC-ASH"))

    def test_env11_remains_completed_as_program_advances(self):
        backlog = self.load_json(BACKLOG)
        order = backlog["strict_order"]
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        completed = [item["id"] for item in backlog["tranches"] if item["status"] == "completed_verified"]
        self.assertEqual(completed[:11], order[:11])
        self.assertGreaterEqual(order.index(backlog["completed_through"]), order.index("ENV-11"))
        self.assertGreaterEqual(order.index(backlog["current_item"]), order.index("ENV-12"))
        self.assertEqual(statuses["ENV-11"], "completed_verified")
        decisions = backlog["env11_decisions"]
        self.assertEqual(decisions["weather_climate_disaster_overlays_added"], 22)
        self.assertEqual(len(decisions["overlay_ids"]), 22)
        self.assertEqual(decisions["current_preset_count"], 76)
        self.assertEqual(decisions["current_composed_archetype_count"], 19)
        self.assertFalse(decisions["automatic_event_causation_authorized"])
        self.assertTrue(decisions["effect_key_deduplication_preserved"])
        self.assertFalse(decisions["universal_numeric_formulas_authored"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])


if __name__ == "__main__":
    unittest.main()
