import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
MODEL = ENV_DIR / "ENV-04_OVERLAY_MODEL_v1.0.0.json"
LIBRARY = ENV_DIR / "ENV-12_PLANETARY_PHYSICAL_OVERLAY_LIBRARY_v1.0.0.json"
MATRIX = ENV_DIR / "ENV-12_PHYSICAL_OVERLAY_INTERACTION_MATRIX_v1.0.0.csv"
GUIDE = ENV_DIR / "ENV-12_PLANETARY_PHYSICAL_OVERLAY_GUIDE.md"
SOURCE_NOTES = ENV_DIR / "ENV-12_PHYSICAL_OVERLAY_SOURCE_NOTES.md"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env12PlanetaryPhysicalOverlayTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_exact_15_unique_overlay_identities(self):
        library = self.load_json(LIBRARY)
        overlays = library["overlays"]
        self.assertEqual(library["overlay_count"], 15)
        self.assertEqual(len(overlays), 15)
        ids = [o["overlay_id"] for o in overlays]
        names = [o["name"] for o in overlays]
        self.assertEqual(len(set(ids)), 15)
        self.assertEqual(len(set(names)), 15)
        self.assertEqual(set(ids), {
            "OVL-THR-EXTREME-HEAT", "OVL-THR-EXTREME-COLD",
            "OVL-ATM-TOXIC", "OVL-ATM-CORROSIVE", "OVL-ATM-LOW-OXYGEN",
            "OVL-PRS-HIGH", "OVL-PRS-LOW", "OVL-CON-RADIATION",
            "OVL-LGT-DARKNESS", "OVL-LGT-GLARE",
            "OVL-GRV-LOW", "OVL-GRV-HIGH", "OVL-GRV-ZERO", "OVL-GRV-VARIABLE",
            "OVL-ATM-VACUUM",
        })

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

    def test_interaction_matrix_has_no_automatic_activation(self):
        rows = self.load_csv(MATRIX)
        ids = {o["overlay_id"] for o in self.load_json(LIBRARY)["overlays"]}
        self.assertGreaterEqual(len(rows), 17)
        self.assertTrue(all(r["Automatic_Activation"] == "NO" for r in rows))
        self.assertTrue(all(r["Source_Overlay_ID"] in ids and r["Target_Overlay_ID"] in ids for r in rows))
        actual = {(r["Source_Overlay_ID"], r["Relation"], r["Target_Overlay_ID"]) for r in rows}
        for edge in {
            ("OVL-ATM-VACUUM", "supersedes", "OVL-PRS-LOW"),
            ("OVL-ATM-VACUUM", "supersedes", "OVL-ATM-LOW-OXYGEN"),
            ("OVL-THR-EXTREME-HEAT", "excludes", "OVL-THR-EXTREME-COLD"),
            ("OVL-LGT-DARKNESS", "excludes", "OVL-LGT-GLARE"),
            ("OVL-GRV-ZERO", "excludes", "OVL-GRV-VARIABLE"),
        }:
            self.assertIn(edge, actual)

    def test_physical_domains_remain_modular(self):
        overlays = {o["overlay_id"]: o for o in self.load_json(LIBRARY)["overlays"]}
        self.assertIn("atmosphere_air_quality", overlays["OVL-ATM-LOW-OXYGEN"]["target_domains"])
        self.assertNotIn("pressure", overlays["OVL-ATM-LOW-OXYGEN"]["target_domains"])
        self.assertIn("pressure", overlays["OVL-PRS-LOW"]["target_domains"])
        self.assertIn("atmosphere_air_quality", overlays["OVL-ATM-VACUUM"]["target_domains"])
        self.assertIn("pressure", overlays["OVL-ATM-VACUUM"]["target_domains"])
        vacuum_keys = {d["effect_key"] for d in overlays["OVL-ATM-VACUUM"]["deltas"]}
        self.assertIn("atmosphere.medium_presence", vacuum_keys)
        self.assertIn("pressure.low_regime", vacuum_keys)

    def test_gravity_regimes_share_one_resolution_seam(self):
        overlays = {o["overlay_id"]: o for o in self.load_json(LIBRARY)["overlays"]}
        for oid in ["OVL-GRV-LOW", "OVL-GRV-HIGH", "OVL-GRV-ZERO", "OVL-GRV-VARIABLE"]:
            self.assertEqual(overlays[oid]["family_id"], "OVF-GRAVITY")
            self.assertIn("gravity_regime", overlays[oid]["exclusive_groups"])
            keys = {d["effect_key"] for d in overlays[oid]["deltas"]}
            self.assertIn("gravity.regime", keys)
            self.assertIn("movement.gravity_context", keys)

    def test_no_universal_participant_or_equipment_formulas_are_invented(self):
        library = self.load_json(LIBRARY)
        rules = " ".join(library["library_rules"])
        for phrase in ["No universal damage", "radiation-dose", "carrying-capacity", "owning systems", "equipment", "adaptations"]:
            self.assertIn(phrase, rules)
        guide = GUIDE.read_text(encoding="utf-8")
        for phrase in [
            "does not invent universal damage",
            "Vacuum is intentionally not implemented as automatic activation",
            "Low Pressure does not automatically create Low Oxygen",
            "Radiation does not automatically create mutations",
            "Vacuum does not automatically create Zero Gravity",
            "Zero Gravity does not automatically create Vacuum",
        ]:
            self.assertIn(phrase, guide)
        notes = SOURCE_NOTES.read_text(encoding="utf-8")
        self.assertIn("does not promote its particular die sizes", notes)
        self.assertIn("not invented universal numeric standards", notes)

    def test_env13_env14_env15_and_cew_boundaries_remain_intact(self):
        boundary = self.load_json(LIBRARY)["authority_boundary"]
        self.assertFalse(boundary["application_implementation_authority"])
        self.assertFalse(boundary["runtime_schema_mutation_authorized"])
        self.assertFalse(boundary["automatic_event_causation_authorized"])
        self.assertEqual(boundary["supernatural_multiversal_overlays_deferred_to"], "ENV-13")
        self.assertEqual(boundary["ability_adaptation_reconciliation_deferred_to"], "ENV-14")
        self.assertEqual(boundary["habitat_signature_vocabulary_deferred_to"], "ENV-15")
        self.assertEqual(boundary["creature_distribution_owned_by"], "CEW")

    def test_backlog_closes_env12_and_selects_env13(self):
        backlog = self.load_json(BACKLOG)
        order = backlog["strict_order"]
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        completed = [item["id"] for item in backlog["tranches"] if item["status"] == "completed_verified"]
        self.assertEqual(completed, order[:12])
        self.assertEqual(backlog["completed_through"], "ENV-12")
        self.assertEqual(backlog["current_item"], "ENV-13")
        self.assertEqual(statuses["ENV-12"], "completed_verified")
        self.assertEqual(statuses["ENV-13"], "selected_not_started")
        decisions = backlog["env12_decisions"]
        self.assertEqual(decisions["planetary_physical_overlays_added"], 15)
        self.assertEqual(len(decisions["overlay_ids"]), 15)
        self.assertEqual(decisions["current_preset_count"], 76)
        self.assertEqual(decisions["current_composed_archetype_count"], 19)
        self.assertEqual(decisions["weather_climate_disaster_overlay_count"], 22)
        self.assertEqual(decisions["current_total_concrete_overlay_count"], 37)
        self.assertTrue(decisions["physical_domains_kept_modular"])
        self.assertTrue(decisions["vacuum_directly_owns_atmosphere_and_pressure"])
        self.assertTrue(decisions["gravity_regimes_share_single_resolution_seam"])
        self.assertFalse(decisions["universal_numeric_formulas_authored"])
        self.assertFalse(decisions["source_specific_gravity_shift_formula_promoted"])
        self.assertEqual(decisions["supernatural_multiversal_overlays_deferred_to"], "ENV-13")
        self.assertEqual(decisions["ability_adaptation_reconciliation_deferred_to"], "ENV-14")
        self.assertEqual(decisions["habitat_vocabulary_deferred_to"], "ENV-15")
        self.assertEqual(decisions["creature_distribution_owned_by"], "CEW")
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
