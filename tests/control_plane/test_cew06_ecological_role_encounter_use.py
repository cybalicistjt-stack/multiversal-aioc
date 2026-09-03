import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
MODEL = CEW / "CEW-06_ECOLOGICAL_ROLE_ENCOUNTER_USE_v1.0.0.json"
EVIDENCE = CEW / "CEW-06_ECOLOGICAL_ROLE_SOURCE_EVIDENCE_v1.0.0.json"
CONTRACT = CEW / "CEW-06_ECOLOGICAL_ROLE_ENCOUNTER_USE_CONTRACT.md"
REPORT = CEW / "CEW-06_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew06EcologicalRoleEncounterUseTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_model_preserves_independent_axes_and_unknown_state(self):
        model = self.load(MODEL)
        self.assertEqual(model["contract_id"], "CEW-ECO-1.0")
        self.assertEqual(model["work_item"], "CEW-06")
        self.assertEqual(model["classification_authority"], "CEW-CLASS-1.0")
        self.assertEqual(model["habitat_authority"], "CEW-HAB-1.0")
        self.assertEqual(model["distribution_authority"], "CEW-DIST-1.0")
        self.assertFalse(model["application_implementation_authority"])
        self.assertTrue(model["unknown_is_first_class"])
        self.assertFalse(model["ecological_role_implies_distribution"])
        self.assertFalse(model["encounter_use_changes_definition_identity"])
        self.assertFalse(model["encounter_use_implies_campaign_placement"])
        self.assertFalse(model["numeric_encounter_score_authorized"])
        self.assertEqual(
            set(model["role_dimensions"]),
            {"trophic_resource_role", "social_aggregation", "ecosystem_interaction", "encounter_use_facet"},
        )

    def test_controlled_vocabulary_is_multiversal_and_nonexclusive(self):
        model = self.load(MODEL)
        vocab = model["controlled_vocabulary"]
        self.assertEqual(
            set(vocab["trophic_resource_role"]),
            {"predator", "scavenger", "herbivore", "sap_feeder", "parasite", "resource_feeder", "unknown"},
        )
        self.assertEqual(
            set(vocab["social_aggregation"]),
            {"solitary", "pair", "pack", "herd", "swarm", "colony", "unknown"},
        )
        self.assertEqual(
            set(vocab["ecosystem_interaction"]),
            {"territorial_defender", "guardian", "ecosystem_engineer", "symbiont", "resource_source", "unknown"},
        )
        self.assertEqual(
            set(vocab["encounter_use_facet"]),
            {"ambusher", "lure_trapper", "pack_pressure", "swarm_pressure", "lookout_alarm", "sentinel_guardian", "terrain_controller", "area_denial", "pursuit_stalker", "hit_and_run", "noncombat_or_negotiable", "unknown"},
        )
        self.assertTrue(model["multi_value_facts_allowed"])
        self.assertFalse(model["role_values_mutually_exclusive"])
        self.assertEqual(model["unmapped_source_term_rule"], "preserve_raw_source_term_as_unresolved; do_not_force_nearest_controlled_value")

    def test_direct_source_evidence_covers_core_role_families(self):
        evidence = self.load(EVIDENCE)
        rows = {row["evidence_id"]: row for row in evidence["direct_evidence_records"]}
        expected = {
            "havalaea-sapcrawl-varnet",
            "havalaea-rootstalker",
            "havalaea-echojaw-crocodile",
            "havalaea-cradleroot-golem",
            "beast1-compsognathus",
            "beast1-hypsilophodon",
            "beast1-dilophosaurus",
            "aberration-timevine",
            "aberration-tesseravore",
        }
        self.assertTrue(expected <= set(rows))
        for row in rows.values():
            self.assertTrue(row["source_locator"]["source_document"].endswith(".PDF"))
            self.assertGreaterEqual(row["source_locator"]["page"], 1)
            self.assertTrue(row["source_excerpt"])
            self.assertFalse(row["canonical_distribution_assertion"])
            self.assertFalse(row["campaign_placement_assertion"])
            self.assertTrue(row["classification_facts"])

        varnet = rows["havalaea-sapcrawl-varnet"]
        facts = {(f["dimension"], f["value"]) for f in varnet["classification_facts"]}
        self.assertIn(("trophic_resource_role", "sap_feeder"), facts)
        self.assertIn(("social_aggregation", "swarm"), facts)
        self.assertIn(("encounter_use_facet", "swarm_pressure"), facts)

        timevine = rows["aberration-timevine"]
        self.assertIn(
            ("trophic_resource_role", "parasite"),
            {(f["dimension"], f["value"]) for f in timevine["classification_facts"]},
        )
        tess = rows["aberration-tesseravore"]
        self.assertIn(
            ("trophic_resource_role", "resource_feeder"),
            {(f["dimension"], f["value"]) for f in tess["classification_facts"]},
        )
        self.assertEqual(tess["raw_resource_target"], "volume and spatial structure")

    def test_plant_category_profiles_are_scoped_not_bulk_identity_bindings(self):
        evidence = self.load(EVIDENCE)
        profiles = {row["profile_id"]: row for row in evidence["source_category_profiles"]}
        self.assertEqual(set(profiles), {"plant-immobile", "plant-creeping", "plant-spreading"})
        for row in profiles.values():
            self.assertEqual(row["source_document"], "Plant Creatures.PDF")
            self.assertEqual(row["application_scope"], "explicit_source_category_members_only")
            self.assertFalse(row["automatic_identity_binding"])
            self.assertFalse(row["automatic_distribution_binding"])
            self.assertTrue(row["encounter_use_facets"])
        self.assertEqual(
            set(profiles["plant-immobile"]["encounter_use_facets"]),
            {"sentinel_guardian", "lure_trapper", "area_denial", "noncombat_or_negotiable"},
        )
        self.assertEqual(
            set(profiles["plant-creeping"]["encounter_use_facets"]),
            {"ambusher", "swarm_pressure", "terrain_controller"},
        )
        self.assertEqual(
            set(profiles["plant-spreading"]["encounter_use_facets"]),
            {"area_denial", "terrain_controller"},
        )

    def test_encounter_facets_do_not_become_runtime_or_balance_truth(self):
        model = self.load(MODEL)
        rules = model["encounter_projection_rules"]
        self.assertFalse(rules["facet_creates_participant_role"])
        self.assertFalse(rules["facet_creates_quantity"])
        self.assertFalse(rules["facet_creates_wave"])
        self.assertFalse(rules["facet_creates_starting_position"])
        self.assertFalse(rules["facet_creates_hidden_tactics"])
        self.assertFalse(rules["facet_guarantees_difficulty"])
        self.assertTrue(rules["permission_filter_before_faceting"])
        self.assertTrue(rules["source_provenance_required_in_gm_diagnostics"])

    def test_contract_states_noninference_and_cew07_boundary(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "Ecological role is not creature identity, habitat, or geographic distribution.",
            "Encounter-use facets are reusable search and preparation hints, not Campaign placement state.",
            "A predator label does not imply a specific prey species.",
            "A guardian label does not imply ownership, faction allegiance, personhood, or domestication.",
            "Plant category profiles apply only where the source explicitly establishes that category.",
            "Exotic resource feeding remains source-specific rather than being forced into Earth trophic vocabulary.",
            "CEW-07 owns the existing-creature coverage audit.",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_is_monotonic_and_selects_cew07(self):
        backlog = self.load(BACKLOG)
        strict_order = backlog["strict_order"]
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-06"))
        self.assertEqual(status["CEW-06"], "completed_verified")
        if backlog["completed_through"] == "CEW-06":
            self.assertEqual(backlog["current_item"], "CEW-07")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(status["CEW-07"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-06"))
        decisions = backlog["cew06_decisions"]
        self.assertEqual(decisions["contract_id"], "CEW-ECO-1.0")
        self.assertFalse(decisions["bulk_corpus_role_population_authorized"])
        self.assertFalse(decisions["numeric_encounter_score_authorized"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertIn("CEW-07", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
