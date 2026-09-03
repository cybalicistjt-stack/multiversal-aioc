import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
MODEL = ENV_DIR / "ENV-15_HABITAT_SIGNATURE_MODEL_v1.0.0.json"
CONTRACT = ENV_DIR / "ENV-15_ECOLOGICAL_MATCHING_CONTRACT.md"
EXAMPLES = ENV_DIR / "ENV-15_SIGNATURE_EXAMPLES_v1.0.0.json"
REPORT = ENV_DIR / "ENV-15_COMPLETION_REPORT.md"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env15HabitatSignatureContractTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_model_exposes_required_environment_side_dimensions(self):
        model = self.load_json(MODEL)
        dimensions = {d["id"]: d for d in model["dimensions"]}
        required = {
            "habitat_medium",
            "water_salinity",
            "water_permanence",
            "water_flow",
            "temperature_band",
            "moisture_band",
            "vegetation_density",
            "substrates",
            "elevation_band",
            "depth_band",
            "light_regime",
            "atmosphere_regime",
            "pressure_regime",
            "gravity_regime",
            "shelter_availability",
            "food_resource_conditions",
            "settlement_intensity",
            "special_environment_contexts",
        }
        self.assertTrue(required.issubset(dimensions))
        self.assertEqual(model["signature_id"], "ENV-HS-1.0")
        self.assertTrue(model["unknown_is_first_class"])
        self.assertTrue(model["resolved_signature_is_read_only"])
        self.assertTrue(model["contribution_trace_required"])
        self.assertFalse(model["numeric_ecological_score_authorized"])

    def test_core_controlled_vocabularies_cover_program_requirements(self):
        dims = {d["id"]: d for d in self.load_json(MODEL)["dimensions"]}
        self.assertTrue({"terrestrial", "aquatic", "aerial", "subterranean"}.issubset(dims["habitat_medium"]["controlled_values"]))
        self.assertTrue({"freshwater", "brackish", "saltwater"}.issubset(dims["water_salinity"]["controlled_values"]))
        self.assertTrue({"extreme_cold", "cold", "temperate", "hot", "extreme_heat", "variable"}.issubset(dims["temperature_band"]["controlled_values"]))
        self.assertTrue({"arid", "mesic", "wet", "saturated", "submerged", "variable"}.issubset(dims["moisture_band"]["controlled_values"]))
        self.assertTrue({"none", "sparse", "open", "moderate", "dense", "closed", "variable"}.issubset(dims["vegetation_density"]["controlled_values"]))
        self.assertTrue({"darkness", "dim", "normal", "bright", "glare", "variable"}.issubset(dims["light_regime"]["controlled_values"]))
        self.assertTrue({"breathable", "low_oxygen", "toxic", "corrosive", "nonbreathable", "vacuum", "variable"}.issubset(dims["atmosphere_regime"]["controlled_values"]))
        self.assertTrue({"zero", "low", "standard", "high", "variable_directional"}.issubset(dims["gravity_regime"]["controlled_values"]))

    def test_matching_contract_separates_suitability_from_distribution(self):
        model = self.load_json(MODEL)
        match = model["matching_contract"]
        self.assertEqual(match["result_states"], ["preferred", "compatible", "conditional", "incompatible", "indeterminate"])
        self.assertTrue(match["canonical_distribution_is_separate"])
        self.assertTrue(match["world_reality_place_constraints_can_veto_later"])
        self.assertTrue(match["rarity_frequency_are_not_derived"])
        self.assertTrue(match["unknown_environment_fact_yields_indeterminate_when_material"])
        self.assertTrue(match["unknown_creature_fact_yields_indeterminate_when_material"])
        self.assertFalse(match["habitat_fit_implies_native"])
        self.assertFalse(match["habitat_fit_implies_common"])
        self.assertFalse(match["habitat_fit_implies_present"])

    def test_overlay_and_composition_semantics_are_preserved(self):
        model = self.load_json(MODEL)
        resolution = model["signature_resolution"]
        self.assertEqual(resolution["composition_order"], [
            "archetype_baselines",
            "preset_parameterization",
            "local_instance_configuration",
            "active_overlays",
            "current_runtime_scene_state",
            "habitat_signature_projection",
        ])
        self.assertTrue(resolution["overlay_resolution_precedes_ecological_matching"])
        self.assertTrue(resolution["overlay_effect_key_deduplication_preserved"])
        self.assertTrue(resolution["input_order_independent"])
        self.assertTrue(resolution["local_instance_may_refine_signature_without_mutating_source_profile"])
        self.assertTrue(resolution["provenance_and_contribution_trace_survive_projection"])

    def test_environment_and_cew_ownership_boundary_is_explicit(self):
        model = self.load_json(MODEL)
        boundary = model["authority_boundary"]
        self.assertEqual(boundary["environment_signature_owner"], "ENV")
        self.assertEqual(boundary["creature_habitat_profile_owner"], "CEW")
        self.assertEqual(boundary["creature_distribution_owner"], "CEW")
        self.assertEqual(boundary["creature_identity_owner"], "existing governed creature identity")
        self.assertFalse(boundary["application_implementation_authority"])
        self.assertFalse(boundary["runtime_schema_mutation_authorized"])
        self.assertFalse(boundary["creature_records_authored_by_env15"])
        self.assertFalse(boundary["ability_links_inferred_from_habitat"])

    def test_contract_forbids_false_precision_and_unknown_collapse(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "unknown is not a match and not an exclusion",
            "ecological suitability is not canonical distribution",
            "Habitat Signature never proves that a creature is native, common, present, or known to the GM",
            "no universal numeric ecological-fit score",
            "active overlays resolve before ecological comparison",
            "hard incompatibility requires an explicit conflict",
            "preference may improve ordering without creating distribution authority",
            "World/Reality/Place authority remains external",
            "ENV owns the environment-side signature; CEW owns creature-side ecology",
        ]:
            self.assertIn(phrase, text)

    def test_examples_demonstrate_overlay_change_unknown_and_distribution_separation(self):
        examples = self.load_json(EXAMPLES)["examples"]
        ids = {e["example_id"] for e in examples}
        self.assertEqual(ids, {
            "EX-HS-RIVER-FLOOD",
            "EX-HS-VACUUM-ZERO-G",
            "EX-HS-UNKNOWN-DIMENSION",
            "EX-HS-SUITABLE-BUT-NOT-DISTRIBUTED",
        })
        self.assertTrue(all(e["illustrative_not_canonical"] for e in examples))
        river = next(e for e in examples if e["example_id"] == "EX-HS-RIVER-FLOOD")
        self.assertIn("OVL-HYD-FLOOD", river["active_overlays"])
        unknown = next(e for e in examples if e["example_id"] == "EX-HS-UNKNOWN-DIMENSION")
        self.assertEqual(unknown["expected_match_state"], "indeterminate")
        dist = next(e for e in examples if e["example_id"] == "EX-HS-SUITABLE-BUT-NOT-DISTRIBUTED")
        self.assertEqual(dist["ecological_fit"], "compatible")
        self.assertEqual(dist["canonical_distribution"], "absent_or_not_established")

    def test_closeout_completes_env15_and_selects_env16(self):
        backlog = self.load_json(BACKLOG)
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        completed = [item["id"] for item in backlog["tranches"] if item["status"] == "completed_verified"]
        self.assertEqual(completed, backlog["strict_order"][:15])
        self.assertEqual(backlog["completed_through"], "ENV-15")
        self.assertEqual(backlog["current_item"], "ENV-16")
        self.assertEqual(statuses["ENV-15"], "completed_verified")
        self.assertEqual(statuses["ENV-16"], "selected_not_started")
        decisions = backlog["env15_decisions"]
        self.assertEqual(decisions["signature_id"], "ENV-HS-1.0")
        self.assertEqual(decisions["habitat_dimension_count"], 18)
        self.assertEqual(decisions["matching_result_states"], ["preferred", "compatible", "conditional", "incompatible", "indeterminate"])
        self.assertTrue(decisions["unknown_is_first_class"])
        self.assertTrue(decisions["ecological_suitability_separate_from_distribution"])
        self.assertTrue(decisions["overlay_resolution_precedes_matching"])
        self.assertFalse(decisions["numeric_ecological_score_authorized"])
        self.assertEqual(decisions["creature_habitat_profile_owner"], "CEW")
        self.assertEqual(decisions["creature_distribution_owner"], "CEW")
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
