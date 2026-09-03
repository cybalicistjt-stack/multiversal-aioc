import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
ENV = ROOT / "governance/application-planning/environment-preset-overlay"
MODEL = CEW / "CEW-04_HABITAT_ENVIRONMENT_CROSSWALK_v1.0.0.json"
EVIDENCE = CEW / "CEW-04_HABITAT_SOURCE_EVIDENCE_v1.0.0.json"
CONTRACT = CEW / "CEW-04_HABITAT_ENVIRONMENT_CROSSWALK_CONTRACT.md"
REPORT = CEW / "CEW-04_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"
ENV_HS = ENV / "ENV-15_HABITAT_SIGNATURE_MODEL_v1.0.0.json"


class Cew04HabitatEnvironmentCrosswalkTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_model_consumes_env_hs_without_distribution_collapse(self):
        model = self.load(MODEL)
        env = self.load(ENV_HS)
        self.assertEqual(model["contract_id"], "CEW-HAB-1.0")
        self.assertEqual(model["work_item"], "CEW-04")
        self.assertEqual(model["habitat_signature_authority"], "ENV-HS-1.0")
        self.assertEqual(model["classification_authority"], "CEW-CLASS-1.0")
        self.assertEqual(model["identity_authority"], "CEW-ID-1.0")
        self.assertFalse(model["application_implementation_authority"])
        self.assertFalse(model["canonical_distribution_authored"])
        self.assertFalse(model["numeric_ecological_score_authorized"])
        self.assertTrue(model["unknown_is_first_class"])
        self.assertFalse(model["source_silence_means_incompatible"])
        self.assertFalse(model["habitat_fit_implies_presence"])
        self.assertFalse(model["habitat_fit_implies_native"])
        self.assertEqual(
            model["predicate_classes"],
            ["requires", "prefers", "tolerates", "excludes", "depends_on", "unknown"],
        )
        env_dims = {row["id"] for row in env["dimensions"]}
        self.assertEqual(set(model["habitat_signature_dimensions"]), env_dims)

    def test_source_section_profiles_bind_only_source_members(self):
        model = self.load(MODEL)
        profiles = {row["profile_id"]: row for row in model["source_section_profiles"]}
        expected = {
            "beast1-swamp",
            "beast1-desert",
            "beast1-aquatic",
            "beast1-mountain",
            "beast1-cold-climate",
            "beasts2-subterranean",
            "beasts2-aerial",
            "beasts2-urban",
            "beasts2-grasslands",
            "havalaea-jungle-forest",
            "havalaea-aquatic",
            "skoal-ice-shelf",
            "skoal-twilight-forest",
            "skoal-necrotic-wetlands",
            "skoal-skeinspire-mountains",
            "skoal-underground-vaults",
        }
        self.assertEqual(set(profiles), expected)
        valid_dims = set(model["habitat_signature_dimensions"])
        for row in profiles.values():
            self.assertEqual(row["application_scope"], "source_section_members_only")
            self.assertFalse(row["identity_binding_created"])
            self.assertFalse(row["canonical_distribution_assertion"])
            self.assertTrue(row["source_scope"]["source_document"].endswith(".PDF"))
            self.assertGreaterEqual(row["source_scope"]["page_start"], 1)
            self.assertGreaterEqual(row["source_scope"]["page_end"], row["source_scope"]["page_start"])
            self.assertTrue(row["predicate_bundle"])
            for fact in row["predicate_bundle"]:
                self.assertIn(fact["predicate"], model["predicate_classes"])
                self.assertIn(fact["dimension_id"], valid_dims)
                self.assertIn("source_basis", fact)

    def test_direct_source_evidence_preserves_predicates_and_temporal_occurrence(self):
        evidence = self.load(EVIDENCE)
        self.assertEqual(evidence["evidence_id"], "CEW-HAB-EVIDENCE-1.0")
        rows = {row["evidence_id"]: row for row in evidence["direct_evidence_records"]}
        for evidence_id in [
            "havalaea-jungle-slip-beetle",
            "fey-sunblight-sprite",
            "beasts2-hurricane-manta-migration",
            "beast1-cave-tusk-mammoth-migration",
            "fey-flicker-stag-seasonal",
            "beast1-tundra-saberfang-activity",
        ]:
            self.assertIn(evidence_id, rows)
            self.assertTrue(rows[evidence_id]["source_locator"]["source_document"].endswith(".PDF"))
            self.assertGreaterEqual(rows[evidence_id]["source_locator"]["page"], 1)
            self.assertTrue(rows[evidence_id]["source_excerpt"])
            self.assertFalse(rows[evidence_id]["canonical_distribution_assertion"])

        beetle = rows["havalaea-jungle-slip-beetle"]
        facts = {(f["predicate"], f["dimension_id"], tuple(f["values"])) for f in beetle["habitat_facts"]}
        self.assertIn(("prefers", "temperature_band", ("warm",)), facts)
        self.assertIn(("prefers", "substrates", ("rock", "metal")), facts)

        manta = rows["beasts2-hurricane-manta-migration"]
        self.assertEqual(manta["temporal_occurrence"]["kind"], "migration")
        self.assertEqual(manta["temporal_occurrence"]["state"], "asserted")
        stag = rows["fey-flicker-stag-seasonal"]
        self.assertEqual(stag["temporal_occurrence"]["kind"], "seasonal_occurrence")
        self.assertEqual(stag["temporal_occurrence"]["state"], "asserted")

    def test_modifier_environment_rules_do_not_auto_bind_creatures(self):
        model = self.load(MODEL)
        modifiers = {row["modifier_id"]: row for row in model["source_modifier_profiles"]}
        self.assertEqual(set(modifiers), {"fire-type-animal", "cold-type-animal"})
        fire = modifiers["fire-type-animal"]
        cold = modifiers["cold-type-animal"]
        self.assertFalse(fire["automatic_creature_binding"])
        self.assertFalse(cold["automatic_creature_binding"])
        self.assertEqual(fire["habitat_facts"][0]["predicate"], "tolerates")
        self.assertEqual(fire["habitat_facts"][0]["dimension_id"], "temperature_band")
        self.assertEqual(fire["habitat_facts"][0]["values"], ["hot"])
        self.assertEqual(cold["habitat_facts"][0]["predicate"], "tolerates")
        self.assertEqual(cold["habitat_facts"][0]["dimension_id"], "temperature_band")
        self.assertEqual(cold["habitat_facts"][0]["values"], ["cold"])

    def test_term_projection_keeps_raw_biomes_when_exact_env_dimension_is_not_supported(self):
        model = self.load(MODEL)
        rules = model["source_term_projection_rules"]
        self.assertEqual(
            rules["biome_label_without_exact_dimension_match"]["dimension_id"],
            "special_environment_contexts",
        )
        self.assertEqual(
            rules["biome_label_without_exact_dimension_match"]["reference_type"],
            "source_context_ref",
        )
        self.assertTrue(rules["biome_label_without_exact_dimension_match"]["preserve_raw_source_term"])
        self.assertFalse(rules["biome_label_without_exact_dimension_match"]["invent_climate_decomposition"])
        self.assertFalse(rules["movement_or_damage_trait_alone"]["creates_habitat_preference"])
        self.assertFalse(rules["game_type_or_affinity_alone"]["creates_habitat_preference"])

    def test_contract_states_noninference_and_cew05_boundary(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "Habitat suitability is not canonical distribution.",
            "Source silence remains unknown.",
            "A source-section habitat heading applies only to the statblocks authored under that heading.",
            "Game type, affinity, damage resistance, movement mode and creature name do not by themselves create habitat facts.",
            "Biome words that do not support an exact ENV-HS-1.0 dimension value remain source_context_ref facts rather than being decomposed by guesswork.",
            "Migration and seasonality are occurrence qualifiers, not geographic range assertions.",
            "CEW-05 owns canonical World, Reality and geographic distribution.",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_is_monotonic_and_selects_cew05(self):
        backlog = self.load(BACKLOG)
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        strict_order = backlog["strict_order"]
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-04"))
        self.assertEqual(status["CEW-04"], "completed_verified")
        if backlog["completed_through"] == "CEW-04":
            self.assertEqual(backlog["current_item"], "CEW-05")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(status["CEW-05"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-04"))
        decisions = backlog["cew04_decisions"]
        self.assertEqual(decisions["contract_id"], "CEW-HAB-1.0")
        self.assertEqual(decisions["source_section_profile_count"], 16)
        self.assertFalse(decisions["canonical_distribution_authored"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertIn("CEW-05", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
