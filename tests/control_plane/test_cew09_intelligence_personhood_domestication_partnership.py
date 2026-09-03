import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
MODEL = CEW / "CEW-09_INTELLIGENCE_PERSONHOOD_DOMESTICATION_PARTNERSHIP_v1.0.0.json"
EVIDENCE = CEW / "CEW-09_SOURCE_EVIDENCE_v1.0.0.json"
CONTRACT = CEW / "CEW-09_COGNITION_PERSONHOOD_PARTNERSHIP_CONTRACT.md"
REPORT = CEW / "CEW-09_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew09IntelligencePersonhoodDomesticationPartnershipTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_contract_and_authority_boundaries(self):
        model = self.load(MODEL)
        self.assertEqual(model["contract_id"], "CEW-COG-PART-1.0")
        self.assertEqual(model["work_item"], "CEW-09")
        self.assertEqual(model["classification_authority"], "CEW-CLASS-1.0")
        self.assertEqual(model["identity_authority"], "CEW-ID-1.0")
        self.assertEqual(model["companion_profile_authority"], "CCP-02")
        self.assertEqual(model["relationship_pathway_authority"], "CCP-03")
        self.assertFalse(model["application_implementation_authority"])
        self.assertFalse(model["canonical_stable_id_population_authorized"])
        self.assertFalse(model["relationship_pathway_population_authorized"])
        self.assertFalse(model["havalaea_native_lineage_population_authorized"])
        self.assertEqual(model["strict_successor"], "CEW-10")

    def test_animal_training_intelligence_tiers_are_recovered_exactly(self):
        model = self.load(MODEL)
        rows = model["intelligence_cognition_model"]["animal_training_tiers"]
        self.assertEqual(len(rows), 5)
        expected = [
            (1, "1-2", "instinctual_simple_commands"),
            (2, "3-4", "basic_behavioral_commands_with_repetition"),
            (3, "5-6", "tactical_and_multistep_tasks"),
            (4, "7-8", "complex_instructions_and_teamwork"),
            (5, "9+", "reason_improvise_and_dialogue"),
        ]
        observed = [(row["tier"], row["intelligence_score"], row["training_implication_id"]) for row in rows]
        self.assertEqual(observed, expected)
        self.assertEqual(model["intelligence_cognition_model"]["source_document"], "Animal training.PDF")

    def test_cognition_evidence_never_auto_creates_personhood(self):
        model = self.load(MODEL)
        rules = model["cross_axis_non_inference_rules"]
        self.assertFalse(rules["tier5_or_int9plus_implies_personhood"])
        self.assertFalse(rules["speech_or_dialogue_capability_implies_personhood_without_authority"])
        self.assertFalse(rules["high_intelligence_descriptor_implies_sapience"])
        self.assertFalse(rules["npc_presentation_implies_personhood"])
        self.assertFalse(rules["animal_or_beast_implies_nonsapient"])
        self.assertFalse(rules["sapience_erases_animal_ecological_identity"])

    def test_source_evidence_is_bounded_and_provenanced(self):
        evidence = self.load(EVIDENCE)
        docs = {row["source_document"]: row for row in evidence["source_documents"]}
        self.assertEqual(evidence["direct_evidence_record_count"], 12)
        self.assertEqual(docs["Animal training.PDF"]["sha256"], "917e9e326e50b0f7db8d4ce5c03d191c595342950b54c86a904667392db03287")
        self.assertEqual(docs["Player Creatures.PDF"]["sha256"], "b6626049ddab2cc30295602fa03581a7d66b4352dc4e0cdc30fd1dc5929613f3")
        self.assertEqual(docs["animals 11-16-24.PDF"]["sha256"], "6b9e8a4b1e30001f38bf2012933a7ec5704a02b6177dbc38b0707d6f44545f3e")
        self.assertEqual(docs["Beast Creatures 1.PDF"]["sha256"], "3b7a1b666e142cf0dd4bf74449855cd1fc5abccd881cec64c0c0e095faaa8b4b")
        self.assertEqual(docs["Havalaea Creatures.PDF"]["sha256"], "78bc18c5026c623261ccd312c4fbae8b015f8c2d42d212904b7dfeb5b20afeab")
        self.assertTrue(all(row["canonical_stable_id_binding"] is None for row in evidence["evidence_records"]))

    def test_player_creature_sapience_rules_remain_conversion_scoped(self):
        model = self.load(MODEL)
        pc = model["personhood_sapience_model"]["player_creature_conversion_rules"]
        self.assertTrue(pc["normally_nonsapient_species_may_gain_full_sentience_and_language_via_conversion"])
        self.assertTrue(pc["havalaea_sapient_animal_template_is_fully_sentient_speaking_culturally_aware"])
        self.assertEqual(pc["havalaea_template_minimum_intelligence"], 8)
        self.assertTrue(pc["havalaea_template_pc_or_npc_capable"])
        self.assertFalse(pc["conversion_rule_is_base_species_fact"])
        self.assertFalse(pc["template_applies_to_all_current_havalaea_creature_definitions"])
        self.assertEqual(pc["native_lineage_application_owner"], "CEW-10")

    def test_domestication_training_classification_preserves_state_boundaries(self):
        model = self.load(MODEL)
        d = model["domestication_training_model"]
        self.assertEqual(
            set(d["definition_level_fact_kinds"]),
            {"source_asserted_wild", "source_asserted_domesticated", "source_asserted_trainable", "source_asserted_generally_untrainable", "unknown"},
        )
        self.assertFalse(d["temperament_implies_domestication"])
        self.assertFalse(d["loyal_trait_implies_ownership"])
        self.assertFalse(d["docile_trait_implies_tamed"])
        self.assertFalse(d["trainable_implies_current_training_state"])
        self.assertEqual(d["individual_taming_training_bond_state_owner"], "CCP-03/04 plus runtime relationship state")

    def test_sapient_partnership_requires_voluntary_consent_without_assigning_roles(self):
        model = self.load(MODEL)
        p = model["partnership_consent_model"]
        self.assertTrue(p["source_confirmed_sapient_taming_forbidden"])
        self.assertTrue(p["sapient_relationship_requires_explicit_voluntary_consent"])
        self.assertTrue(p["rescue_is_nonbonding"])
        self.assertFalse(p["automatic_ownership_created"])
        self.assertFalse(p["automatic_obedience_created"])
        self.assertFalse(p["mount_pet_familiar_roles_assigned"])
        self.assertEqual(p["mount_pet_familiar_crosswalk_owner"], "CEW-11")

    def test_canonical_stable_id_population_remains_unknown(self):
        model = self.load(MODEL)
        cov = model["canonical_stable_id_coverage"]
        self.assertEqual(cov["canonical_creature_definition_count"], 27)
        self.assertEqual(cov["explicit_intelligence_cognition_binding_count"], 0)
        self.assertEqual(cov["explicit_personhood_sapience_binding_count"], 0)
        self.assertEqual(cov["explicit_domestication_training_binding_count"], 0)
        self.assertEqual(cov["unknown_intelligence_cognition_binding_count"], 27)
        self.assertEqual(cov["unknown_personhood_sapience_binding_count"], 27)
        self.assertEqual(cov["unknown_domestication_training_binding_count"], 27)
        self.assertFalse(cov["display_name_or_source_label_used_as_binding"])
        self.assertFalse(cov["type_or_ecology_used_as_personhood_binding"])

    def test_npc_projection_is_independent_of_personhood_and_identity(self):
        model = self.load(MODEL)
        npc = model["npc_presentation_model"]
        self.assertTrue(npc["source_or_owner_backing_required"])
        self.assertFalse(npc["npc_projection_changes_creature_identity"])
        self.assertFalse(npc["npc_projection_erases_animal_ecological_identity"])
        self.assertFalse(npc["npc_projection_creates_personhood"])
        self.assertFalse(npc["npc_projection_creates_ownership_or_tamability"])

    def test_contract_text_states_core_non_inference_rules(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "Intelligence is not personhood.",
            "Sapience does not erase animal ecological identity.",
            "Trainability is not current training state, ownership, or obedience.",
            "Source-confirmed sapient beings cannot enter through taming.",
            "Sapient relationship formation requires explicit voluntary consent.",
            "Mount, pet/companion, and familiar pathway roles remain CEW-11-owned.",
            "CEW-10 is the strict successor.",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_is_monotonic_and_selects_cew10(self):
        backlog = self.load(BACKLOG)
        strict_order = backlog["strict_order"]
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-09"))
        self.assertEqual(status["CEW-09"], "completed_verified")
        if backlog["completed_through"] == "CEW-09":
            self.assertEqual(backlog["current_item"], "CEW-10")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(status["CEW-10"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-09"))
        decisions = backlog["cew09_decisions"]
        self.assertEqual(decisions["contract_id"], "CEW-COG-PART-1.0")
        self.assertEqual(decisions["animal_training_intelligence_tier_count"], 5)
        self.assertEqual(decisions["direct_source_evidence_record_count"], 12)
        self.assertEqual(decisions["canonical_creature_definition_count"], 27)
        self.assertEqual(decisions["explicit_stable_id_personhood_binding_count"], 0)
        self.assertTrue(decisions["sapient_taming_forbidden"])
        self.assertTrue(decisions["sapient_voluntary_consent_required"])
        self.assertFalse(decisions["relationship_pathway_population_authorized"])
        self.assertFalse(decisions["havalaea_native_lineage_population_authorized"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertIn("CEW-10", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
