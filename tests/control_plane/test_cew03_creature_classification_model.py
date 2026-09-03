import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW_DIR = ROOT / "governance/application-planning/creature-ecology-wildlife"
MODEL = CEW_DIR / "CEW-03_CREATURE_CLASSIFICATION_MODEL_v1.0.0.json"
CONTRACT = CEW_DIR / "CEW-03_CLASSIFICATION_CONTRACT.md"
REPORT = CEW_DIR / "CEW-03_COMPLETION_REPORT.md"
BACKLOG = CEW_DIR / "CEW_PROGRAM_BACKLOG.json"


class Cew03CreatureClassificationModelTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_model_is_multidimensional_and_open_world(self):
        model = self.load_json(MODEL)
        self.assertEqual(model["model_id"], "CEW-CLASS-1.0")
        self.assertEqual(model["identity_authority"], "CEW-ID-1.0")
        self.assertEqual(model["taxonomy_authority"], "CEW-TAX-1.0")
        self.assertFalse(model["application_implementation_authority"])
        self.assertTrue(model["open_world_semantics"]["unknown_is_first_class"])
        self.assertFalse(model["open_world_semantics"]["source_silence_means_false"])
        self.assertFalse(model["open_world_semantics"]["single_axis_collapse_authorized"])

        axes = {axis["axis_id"]: axis for axis in model["classification_axes"]}
        expected = {
            "biological_ecological_identity",
            "game_creature_type",
            "nested_subtype_category",
            "body_plan_manifestation",
            "origin_affinity",
            "template_modifier_transformation",
            "condition_state",
            "intelligence_cognition",
            "personhood_sapience",
            "habitat_ecology",
            "distribution_scope",
            "ecological_role",
            "domestication_training",
            "relationship_pathways",
            "npc_presentation",
            "encounter_runtime_role",
        }
        self.assertEqual(set(axes), expected)
        for axis in axes.values():
            self.assertEqual(axis["default_state"], "unknown")
            self.assertIn(axis["cardinality"], {"zero_or_one", "zero_or_many"})
            self.assertTrue(axis["provenance_required_for_assertion"])

    def test_cross_axis_non_inference_boundaries_are_explicit(self):
        model = self.load_json(MODEL)
        rules = model["cross_axis_rules"]
        for key in [
            "classification_does_not_change_identity",
            "game_type_does_not_define_biological_identity",
            "biological_identity_does_not_define_game_type",
            "sapience_does_not_change_species_or_ecological_identity",
            "npc_projection_does_not_define_personhood",
            "relationship_eligibility_does_not_create_bond_or_ownership",
            "habitat_suitability_does_not_create_distribution",
            "template_does_not_replace_base_type_without_explicit_source_rule",
            "source_conflicts_remain_visible",
            "no_last_write_wins_conflict_resolution",
        ]:
            self.assertTrue(rules[key])

    def test_later_cew_tranches_own_population_not_cew03_invention(self):
        model = self.load_json(MODEL)
        owners = {axis["axis_id"]: axis["population_owner"] for axis in model["classification_axes"]}
        self.assertEqual(owners["habitat_ecology"], "CEW-04")
        self.assertEqual(owners["distribution_scope"], "CEW-05")
        self.assertEqual(owners["ecological_role"], "CEW-06")
        self.assertEqual(owners["intelligence_cognition"], "CEW-09")
        self.assertEqual(owners["personhood_sapience"], "CEW-09")
        self.assertEqual(owners["domestication_training"], "CEW-09")
        self.assertEqual(owners["relationship_pathways"], "CEW-11")
        self.assertEqual(model["future_population_rules"]["habitat_predicate_vocabulary"], "ENV-HS-1.0 / CEW-04")
        self.assertFalse(model["future_population_rules"]["cew03_bulk_classification_authorized"])

    def test_cew02_source_disagreements_are_not_flattened(self):
        model = self.load_json(MODEL)
        queue = {row["conflict_id"]: row for row in model["preserved_unresolved_queue"]}
        self.assertGreaterEqual(len(queue), 7)
        for conflict_id in [
            "CEW02-CONFLICT-005",
            "CEW02-CONFLICT-006",
            "CEW02-CONFLICT-007",
            "CEW02-CONFLICT-008",
            "CEW02-CONFLICT-009",
            "CEW02-CONFLICT-010",
            "CEW02-CONFLICT-011",
        ]:
            self.assertIn(conflict_id, queue)
            self.assertEqual(queue[conflict_id]["state"], "unresolved_conflict")
            self.assertFalse(queue[conflict_id]["auto_resolve"])

    def test_reference_cases_demonstrate_axis_independence(self):
        model = self.load_json(MODEL)
        cases = {row["case_id"]: row for row in model["reference_cases"]}
        for case_id in [
            "fire_type_animal",
            "undead_type_animal",
            "creeping_plant",
            "incorporeal_mirage",
            "divinetech_overlap",
            "vampire_conflict",
            "havalaea_sapient_animal",
        ]:
            self.assertIn(case_id, cases)

        fire = cases["fire_type_animal"]
        self.assertEqual(fire["classification"]["biological_ecological_identity"], ["Animal"])
        self.assertEqual(fire["classification"]["origin_affinity"], ["Fire"])
        self.assertFalse(fire["effects"]["base_type_replacement"])

        undead = cases["undead_type_animal"]
        self.assertEqual(undead["classification"]["game_creature_type"], ["Undead"])
        self.assertTrue(undead["effects"]["explicit_source_type_replacement"])

        plant = cases["creeping_plant"]
        self.assertEqual(plant["classification"]["biological_ecological_identity"], ["Plant"])
        self.assertEqual(plant["classification"]["body_plan_manifestation"], ["Creeping movement category"])
        self.assertNotIn("Creeping", plant["classification"]["game_creature_type"])

        havalaea = cases["havalaea_sapient_animal"]
        self.assertEqual(havalaea["classification"]["biological_ecological_identity"], ["Animal"])
        self.assertEqual(havalaea["classification"]["npc_presentation"], ["eligible_when source/owner-supported"])
        self.assertEqual(havalaea["classification"]["relationship_pathways"], ["not inferred"])

    def test_contract_preserves_identity_provenance_and_permission_boundaries(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "No axis is allowed to infer another axis merely from category similarity.",
            "Classification never changes reusable Definition identity.",
            "Unknown is not false, absent, incompatible, nonsapient, nonnative, or ineligible.",
            "Habitat suitability is not canonical distribution.",
            "Mount, pet/companion and familiar remain relationship/pathway roles, not creature types.",
            "NPC presentation is a projection choice, not a biological or personhood reclassification.",
            "CEW-03 does not bulk-populate later-tranche classifications.",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_is_monotonic_and_selects_cew04(self):
        backlog = self.load_json(BACKLOG)
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        strict_order = backlog["strict_order"]
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-03"))
        self.assertEqual(status["CEW-03"], "completed_verified")
        if backlog["completed_through"] == "CEW-03":
            self.assertEqual(backlog["current_item"], "CEW-04")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(status["CEW-04"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-03"))
        decisions = backlog["cew03_decisions"]
        self.assertEqual(decisions["contract_id"], "CEW-CLASS-1.0")
        self.assertEqual(decisions["classification_axis_count"], 16)
        self.assertFalse(decisions["single_axis_collapse_authorized"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertIn("CEW-04", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
