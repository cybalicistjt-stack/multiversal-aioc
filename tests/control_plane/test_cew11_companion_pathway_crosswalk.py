import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
MODEL = CEW / "CEW-11_COMPANION_RELATIONSHIP_PATHWAY_CROSSWALK_v1.0.0.json"
EVIDENCE = CEW / "CEW-11_RELATIONSHIP_PATHWAY_SOURCE_EVIDENCE_v1.0.0.json"
CONTRACT = CEW / "CEW-11_COMPANION_RELATIONSHIP_PATHWAY_CONTRACT.md"
REPORT = CEW / "CEW-11_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew11CompanionPathwayCrosswalkTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_contract_and_authority_boundaries(self):
        model = self.load(MODEL)
        self.assertEqual(model["contract_id"], "CEW-REL-PATH-1.0")
        self.assertEqual(model["work_item"], "CEW-11")
        self.assertEqual(model["identity_authority"], "CEW-ID-1.0")
        self.assertEqual(model["cognition_personhood_authority"], "CEW-COG-PART-1.0")
        self.assertEqual(model["havalaea_lineage_authority"], "CEW-HAV-LIN-1.0")
        self.assertEqual(model["ccp_mount_authority"], "CCP-06")
        self.assertEqual(model["ccp_familiar_authority"], "CCP-07")
        self.assertFalse(model["application_implementation_authority"])
        self.assertFalse(model["live_relationship_state_mutation_authorized"])
        self.assertEqual(model["strict_successor"], "CEW-12")

    def test_pathway_roles_remain_independent_relationship_capabilities(self):
        model = self.load(MODEL)
        roles = model["relationship_pathway_model"]["pathway_roles"]
        for role in [
            "pet_or_companion",
            "mount",
            "pack",
            "service",
            "work",
            "travel_support",
            "combat_participation",
            "combat_support",
            "familiar",
            "supernatural_bond",
        ]:
            self.assertIn(role, roles)
        self.assertTrue(model["relationship_pathway_model"]["multi_pathway_eligibility_allowed"])
        self.assertFalse(model["relationship_pathway_model"]["pathway_role_is_base_creature_type"])
        self.assertFalse(model["relationship_pathway_model"]["eligibility_creates_current_relationship"])

    def test_crosswalk_reuses_completed_ccp_owners(self):
        model = self.load(MODEL)
        owners = model["ccp_crosswalk"]
        self.assertEqual(owners["bond_formation"], "CCP-03")
        self.assertEqual(owners["training_behavior"], "CCP-04")
        self.assertEqual(owners["care_welfare"], "CCP-05")
        self.assertEqual(owners["mount_pack_service_work_travel"], "CCP-06")
        self.assertEqual(owners["combat_familiar_supernatural_bond"], "CCP-07")
        self.assertEqual(owners["breeding_lineage"], "CCP-08")
        self.assertEqual(owners["habitats_facilities"], "CCP-09")
        self.assertEqual(owners["ecology_world"], "CCP-10")
        self.assertFalse(owners["duplicate_relationship_system_created"])

    def test_eligibility_states_preserve_unknown_and_consent(self):
        model = self.load(MODEL)
        states = model["relationship_pathway_model"]["eligibility_states"]
        self.assertEqual(
            states,
            [
                "asserted_eligible",
                "conditional_profile_scoped",
                "sapient_voluntary_partnership_only",
                "asserted_not_normally_bondable",
                "explicitly_ineligible",
                "unknown",
                "not_applicable",
            ],
        )
        consent = model["sapient_partnership_rules"]
        self.assertTrue(consent["sapient_relationship_requires_explicit_voluntary_consent"])
        self.assertTrue(consent["consent_applies_to_mount_pet_companion_familiar_work_service_and_combat_roles"])
        self.assertFalse(consent["physical_capability_overrides_consent"])
        self.assertFalse(consent["npc_projection_overrides_consent"])

    def test_non_inference_rules_block_apparent_fit(self):
        model = self.load(MODEL)
        rules = model["non_inference_rules"]
        for key in [
            "size_or_strength_implies_mount",
            "locomotion_implies_mount",
            "trainability_implies_pet_or_companion",
            "domestication_implies_current_pet_status",
            "magical_or_supernatural_type_implies_familiar",
            "high_intelligence_implies_companion_or_familiar",
            "animal_or_beast_type_implies_pet",
            "ecological_role_implies_relationship_pathway",
            "havalaea_lineage_implies_relationship_pathway",
            "npc_projection_implies_relationship_pathway",
            "source_collection_membership_implies_pathway",
            "display_name_similarity_creates_binding",
        ]:
            self.assertFalse(rules[key])

    def test_source_evidence_recovers_mount_and_familiar_pet_material_without_stable_id_binding(self):
        evidence = self.load(EVIDENCE)
        docs = {row["source_document"]: row for row in evidence["source_documents"]}
        self.assertEqual(docs["Mounts.PDF"]["sha256"], "90061aefaa7a0a1c8503be207099123948605f967987ac777847d19857eb6593")
        self.assertEqual(docs["Familiars and pets.PDF"]["sha256"], "02129e10f40a815480b47c14f26e14620777eb0370ef2b7fd3d998b3a1760b32")
        self.assertEqual(docs["Animal training.PDF"]["sha256"], "917e9e326e50b0f7db8d4ce5c03d191c595342950b54c86a904667392db03287")
        self.assertEqual(evidence["mount_source_designation_count"], 60)
        self.assertEqual(len(evidence["mount_source_designations"]), 60)
        self.assertTrue(all(row["canonical_stable_id_binding"] is None for row in evidence["mount_source_designations"]))
        familiar = evidence["familiar_pet_source_semantics"]
        self.assertTrue(familiar["sentient_familiars_may_willingly_enter_bond_for_mutual_benefit"])
        self.assertTrue(familiar["familiar_bond_described_as_mutual_agreement"])
        self.assertTrue(familiar["pet_and_familiar_are_distinct_source_roles"])

    def test_legacy_mechanics_do_not_override_completed_ccp_authority(self):
        model = self.load(MODEL)
        precedence = model["legacy_source_precedence"]
        self.assertFalse(precedence["mounts_pdf_universal_speed_capacity_endurance_formulas_promoted"])
        self.assertFalse(precedence["mounts_pdf_training_dcs_promoted_as_universal_ccp_rules"])
        self.assertFalse(precedence["familiars_pdf_universal_abilities_promoted_from_creature_eligibility"])
        self.assertFalse(precedence["familiars_pdf_bond_tiers_promoted_as_universal_ccp_rules"])
        self.assertEqual(precedence["mount_system_authority"], "CCP-06")
        self.assertEqual(precedence["familiar_supernatural_bond_authority"], "CCP-07")

    def test_current_canonical_definitions_remain_pathway_unknown_without_explicit_binding(self):
        model = self.load(MODEL)
        cov = model["canonical_stable_id_coverage"]
        self.assertEqual(cov["canonical_creature_definition_count"], 27)
        self.assertEqual(cov["explicit_relationship_pathway_binding_count"], 0)
        self.assertEqual(cov["unknown_relationship_pathway_binding_count"], 27)
        self.assertEqual(cov["canonical_havalaea_creature_definition_count"], 5)
        self.assertEqual(cov["havalaea_explicit_relationship_pathway_binding_count"], 0)
        self.assertEqual(cov["havalaea_unknown_relationship_pathway_binding_count"], 5)
        self.assertFalse(cov["source_label_used_as_canonical_binding"])

    def test_contract_text_states_core_relationship_rules(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "Mount, pet/companion, familiar, work, service, and combat-partner status are relationship pathways, not creature types.",
            "Eligibility does not create ownership, bonding, taming, training, obedience, or placement state.",
            "Physical capability is not consent.",
            "A magical creature is not automatically familiar-compatible.",
            "A trainable or domesticated creature is not automatically a pet or companion.",
            "Completed CCP-06 and CCP-07 authority takes precedence over legacy universal formulas in retained Mounts and Familiars source material.",
            "CEW-12 is the strict successor.",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_is_monotonic_and_selects_cew12(self):
        backlog = self.load(BACKLOG)
        strict_order = backlog["strict_order"]
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-11"))
        self.assertEqual(status["CEW-11"], "completed_verified")
        if backlog["completed_through"] == "CEW-11":
            self.assertEqual(backlog["current_item"], "CEW-12")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(status["CEW-12"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-11"))
        decisions = backlog["cew11_decisions"]
        self.assertEqual(decisions["contract_id"], "CEW-REL-PATH-1.0")
        self.assertEqual(decisions["mount_source_designation_count"], 60)
        self.assertEqual(decisions["canonical_creature_definition_count"], 27)
        self.assertEqual(decisions["explicit_relationship_pathway_binding_count"], 0)
        self.assertTrue(decisions["sapient_voluntary_consent_required"])
        self.assertFalse(decisions["legacy_universal_formula_promotion_authorized"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertIn("CEW-12", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
