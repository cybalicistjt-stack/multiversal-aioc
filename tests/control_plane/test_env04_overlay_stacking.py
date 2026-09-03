import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
MODEL = ENV_DIR / "ENV-04_OVERLAY_MODEL_v1.0.0.json"
CONTRACT = ENV_DIR / "ENV-04_OVERLAY_TAXONOMY_STACKING_CONTRACT_v1.0.0.md"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env04OverlayStackingTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_overlay_model_is_bounded_and_nonimplementation(self):
        model = self.load_json(MODEL)
        self.assertEqual(model["tranche"], "ENV-04")
        self.assertFalse(model["authority_boundary"]["application_implementation_authority"])
        self.assertFalse(model["authority_boundary"]["runtime_schema_mutation_authorized"])
        self.assertFalse(model["authority_boundary"]["source_profiles_mutated"])
        self.assertEqual(model["authority_boundary"]["preset_conversion_owned_by"], "ENV-05")
        self.assertEqual(model["authority_boundary"]["habitat_signature_vocabulary_owned_by"], "ENV-15")

    def test_overlay_family_taxonomy_is_complete_and_nonprecedential(self):
        model = self.load_json(MODEL)
        families = {item["id"] for item in model["overlay_families"]}
        expected = {
            "OVF-WEATHER", "OVF-THERMAL", "OVF-HYDROLOGY", "OVF-ATMOSPHERE",
            "OVF-LIGHT", "OVF-GRAVITY", "OVF-PRESSURE", "OVF-CONTAMINATION",
            "OVF-GEOLOGIC", "OVF-ECOLOGICAL", "OVF-INFRASTRUCTURE", "OVF-SUPERNATURAL",
        }
        self.assertEqual(families, expected)
        self.assertIn("Overlay family is classification, not implicit precedence.", model["principles"])
        self.assertTrue(model["determinism_rules"]["hidden_priority_numbers_forbidden"])
        self.assertTrue(model["determinism_rules"]["last_write_wins_forbidden"])
        self.assertTrue(model["determinism_rules"]["input_order_must_not_change_result"])

    def test_delta_stack_and_relation_vocabularies_are_explicit(self):
        model = self.load_json(MODEL)
        contract = model["overlay_definition_contract"]
        self.assertEqual(
            set(contract["allowed_delta_operations"]),
            {"set", "add", "remove", "constrain", "expand", "multiply", "replace_reference", "merge_unique"},
        )
        self.assertEqual(
            set(contract["stack_modes"]),
            {"nonstacking", "additive", "multiplicative", "strongest", "weakest", "replace", "merge_unique"},
        )
        self.assertEqual(
            set(model["relation_types"]),
            {"requires", "excludes", "supersedes", "transforms_with", "amplifies", "dampens"},
        )
        self.assertEqual(contract["intensity_contract"]["canonical_band_order"], ["trace", "mild", "moderate", "severe", "extreme"])
        self.assertTrue(contract["intensity_contract"]["cross_scale_comparison_forbidden_unless_declared"])

    def test_stacking_pipeline_is_deterministic_and_deduplicates_effects(self):
        model = self.load_json(MODEL)
        pipeline = model["stacking_pipeline"]
        self.assertEqual([item["order"] for item in pipeline], list(range(1, 10)))
        self.assertEqual(pipeline[5]["step"], "deduplicate_equivalent_effects")
        self.assertIn("effect_key", pipeline[5]["rule"])
        self.assertTrue(model["determinism_rules"]["contribution_trace_required"])
        joined = " ".join(model["deduplication_rules"])
        self.assertIn("stable effect_key", joined)
        self.assertIn("unresolved_conflict", joined)

    def test_broad_styles_are_not_reintroduced_as_monolithic_overlays(self):
        model = self.load_json(MODEL)
        guidance = model["non_overlay_guidance"]
        self.assertIn("narrower conditions", guidance["post_apocalyptic"])
        self.assertIn("not automatically an environmental condition overlay", guidance["cyberpunk"])
        self.assertIn("Stable climate", guidance["climate_band"])

    def test_contract_records_key_examples_and_visible_conflict_behavior(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "Heavy Rain + Flooded",
            "Radiation + Toxic Atmosphere",
            "Low Gravity + Zero Gravity",
            "Wildfire + Heavy Rain",
            "Abandoned + Blackout",
            "Magical Saturation + Reality Instability",
            "input-order-independent",
            "unresolved_conflict",
        ]:
            self.assertIn(phrase, text)

    def test_env04_remains_completed_after_later_env_progression(self):
        backlog = self.load_json(BACKLOG)
        order = backlog["strict_order"]
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        self.assertEqual(statuses["ENV-04"], "completed_verified")
        self.assertGreaterEqual(order.index(backlog["completed_through"]), order.index("ENV-04"))
        self.assertNotEqual(backlog["current_item"], "ENV-04")
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
