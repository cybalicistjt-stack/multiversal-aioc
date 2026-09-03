import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
MODEL = CEW / "CEW-10_HAVALAEA_NATIVE_FAUNA_TIME_OF_TROUBLES_v1.0.0.json"
EVIDENCE = CEW / "CEW-10_HAVALAEA_LINEAGE_SOURCE_EVIDENCE_v1.0.0.json"
CONTRACT = CEW / "CEW-10_HAVALAEA_NATIVE_LINEAGE_CONTRACT.md"
REPORT = CEW / "CEW-10_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew10HavalaeaNativeFaunaTimeTroublesTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_contract_and_authority_boundaries(self):
        model = self.load(MODEL)
        self.assertEqual(model["contract_id"], "CEW-HAV-LIN-1.0")
        self.assertEqual(model["work_item"], "CEW-10")
        self.assertEqual(model["identity_authority"], "CEW-ID-1.0")
        self.assertEqual(model["distribution_authority"], "CEW-DIST-1.0")
        self.assertEqual(model["cognition_personhood_authority"], "CEW-COG-PART-1.0")
        self.assertFalse(model["application_implementation_authority"])
        self.assertFalse(model["canonical_stable_id_lineage_population_authorized"])
        self.assertFalse(model["relationship_pathway_population_authorized"])
        self.assertEqual(model["strict_successor"], "CEW-11")

    def test_lineage_states_distinguish_native_from_other_havalaea_presence(self):
        model = self.load(MODEL)
        states = model["lineage_origin_model"]["lineage_states"]
        self.assertEqual(
            states,
            [
                "time_of_troubles_native_lineage",
                "later_imported_lineage",
                "relocated_returned_or_reintroduced_lineage",
                "warden_bred_or_engineered_lineage",
                "rift_displaced_hybridized_or_conceptual_lineage",
                "unknown",
            ],
        )
        rules = model["lineage_origin_model"]["non_inference_rules"]
        self.assertFalse(rules["born_on_havalaea_alone_proves_time_of_troubles_lineage"])
        self.assertFalse(rules["present_on_havalaea_proves_native_lineage"])
        self.assertFalse(rules["havalaea_source_collection_proves_native_lineage"])
        self.assertFalse(rules["warden_bred_or_seeded_proves_time_of_troubles_lineage"])
        self.assertFalse(rules["wild_or_feral_status_proves_native_lineage"])
        self.assertFalse(rules["cultural_or_character_native_proves_ecological_lineage"])

    def test_owner_authority_defines_time_of_troubles_native_lineage(self):
        model = self.load(MODEL)
        owner = model["owner_program_authority"]
        self.assertEqual(owner["authority_kind"], "owner_approved_program_invariant")
        self.assertTrue(owner["time_of_troubles_native_requires_lineage_descent"])
        self.assertTrue(owner["later_imported_animals_remain_distinguishable"])
        self.assertTrue(owner["native_born_wording_alone_is_insufficient_without_lineage_descent"])
        self.assertTrue(owner["native_human_level_animals_preserve_animal_ecological_identity"])
        self.assertTrue(owner["native_human_level_animals_may_project_through_npc_system"])

    def test_source_evidence_is_bounded_and_provenanced(self):
        evidence = self.load(EVIDENCE)
        docs = {row["source_document"]: row for row in evidence["source_documents"]}
        self.assertEqual(docs["Havalaea.PDF"]["sha256"], "b0333b511479a3434e65e7c6812dd8f26bd5de91e838d0da663e564a391f4180")
        self.assertEqual(docs["Havalaea Creatures.PDF"]["sha256"], "78bc18c5026c623261ccd312c4fbae8b015f8c2d42d212904b7dfeb5b20afeab")
        self.assertEqual(docs["Player Creatures.PDF"]["sha256"], "b6626049ddab2cc30295602fa03581a7d66b4352dc4e0cdc30fd1dc5929613f3")
        self.assertEqual(evidence["havalaea_creatures_source_profile_count"], 46)
        self.assertTrue(all(row["canonical_stable_id_binding"] is None for row in evidence["evidence_records"]))

    def test_world_source_preserves_multiple_non_native_or_non_lineage_equivalent_paths(self):
        model = self.load(MODEL)
        source = model["havalaea_world_ecology_source_semantics"]
        self.assertTrue(source["world_was_created_as_multiversal_convergence_ark"])
        self.assertTrue(source["green_wardens_balanced_thousands_of_species"])
        self.assertTrue(source["low_cr_creatures_were_relocated_from_nursery"])
        self.assertTrue(source["reintroduced_or_returning_species_exist"])
        self.assertTrue(source["warden_bred_creatures_can_reproduce_wild"])
        self.assertTrue(source["once_domesticated_creatures_can_be_feral"])
        self.assertTrue(source["riftfall_creatures_are_often_non_native_displaced_hybridized_or_conceptual"])

    def test_current_havalaea_canonical_definitions_remain_lineage_unknown(self):
        model = self.load(MODEL)
        cov = model["canonical_havalaea_definition_coverage"]
        self.assertEqual(cov["canonical_havalaea_creature_definition_count"], 5)
        self.assertEqual(cov["explicit_time_of_troubles_native_lineage_binding_count"], 0)
        self.assertEqual(cov["explicit_later_imported_lineage_binding_count"], 0)
        self.assertEqual(cov["unknown_lineage_binding_count"], 5)
        self.assertFalse(cov["namespace_membership_used_as_native_lineage_proof"])
        self.assertFalse(cov["display_name_used_as_source_binding"])
        self.assertFalse(cov["source_collection_membership_used_as_native_lineage_proof"])

    def test_cultural_native_and_sapient_conversion_do_not_rewrite_ecological_lineage(self):
        model = self.load(MODEL)
        sap = model["sapient_animal_integration"]
        self.assertTrue(sap["player_creatures_template_describes_a_culturally_aware_native_of_havalaea"])
        self.assertFalse(sap["template_native_wording_proves_time_of_troubles_lineage"])
        self.assertFalse(sap["sapience_erases_animal_ecological_identity"])
        self.assertTrue(sap["source_or_owner_confirmed_native_human_level_animals_may_project_as_npcs"])
        self.assertFalse(sap["npc_projection_implies_humanoid_identity"])
        self.assertFalse(sap["npc_projection_implies_ownership_or_tamability"])
        self.assertTrue(sap["sapient_person_level_relationships_require_voluntary_consent"])

    def test_relationship_roles_remain_cew11_owned(self):
        model = self.load(MODEL)
        rel = model["relationship_pathway_boundary"]
        self.assertFalse(rel["mount_role_assigned"])
        self.assertFalse(rel["pet_or_companion_role_assigned"])
        self.assertFalse(rel["familiar_role_assigned"])
        self.assertEqual(rel["mount_pet_familiar_companion_crosswalk_owner"], "CEW-11")
        self.assertFalse(rel["lineage_status_creates_bond_ownership_or_training_state"])

    def test_contract_text_states_core_lineage_rules(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "Presence on Havalaea is not native-lineage proof.",
            "Birth on Havalaea alone is not Time-of-Troubles lineage proof.",
            "Cultural or character nativeness is not ecological lineage.",
            "Warden-bred, engineered, seeded, wild, feral, relocated, returned, or reintroduced status does not silently become Time-of-Troubles native lineage.",
            "Sapience does not erase animal ecological identity.",
            "NPC projection does not imply humanoid identity, ownership, tamability, or loss of autonomy.",
            "CEW-11 is the strict successor.",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_is_monotonic_and_selects_cew11(self):
        backlog = self.load(BACKLOG)
        strict_order = backlog["strict_order"]
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-10"))
        self.assertEqual(status["CEW-10"], "completed_verified")
        if backlog["completed_through"] == "CEW-10":
            self.assertEqual(backlog["current_item"], "CEW-11")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(status["CEW-11"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-10"))
        decisions = backlog["cew10_decisions"]
        self.assertEqual(decisions["contract_id"], "CEW-HAV-LIN-1.0")
        self.assertEqual(decisions["havalaea_creatures_source_profile_count"], 46)
        self.assertEqual(decisions["canonical_havalaea_creature_definition_count"], 5)
        self.assertEqual(decisions["explicit_time_of_troubles_native_lineage_binding_count"], 0)
        self.assertEqual(decisions["unknown_lineage_binding_count"], 5)
        self.assertTrue(decisions["native_human_level_animals_preserve_animal_ecological_identity"])
        self.assertTrue(decisions["native_human_level_animals_npc_projection_supported"])
        self.assertFalse(decisions["relationship_pathway_population_authorized"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertIn("CEW-11", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
