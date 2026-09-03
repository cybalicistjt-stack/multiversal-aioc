import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
MODEL = CEW / "CEW-12_EARTHLIKE_ANIMAL_WILDLIFE_BASELINE_v1.0.0.json"
LIBRARY = CEW / "CEW-12_EARTHLIKE_WILDLIFE_LIBRARY_v1.0.0.json"
EVIDENCE = CEW / "CEW-12_EARTHLIKE_SOURCE_EVIDENCE_v1.0.0.json"
CONTRACT = CEW / "CEW-12_EARTHLIKE_WILDLIFE_BASELINE_CONTRACT.md"
REPORT = CEW / "CEW-12_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew12EarthlikeWildlifeBaselineTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_contract_and_authority_boundaries(self):
        model = self.load(MODEL)
        self.assertEqual(model["contract_id"], "CEW-EARTHLIKE-BASE-1.0")
        self.assertEqual(model["work_item"], "CEW-12")
        self.assertEqual(model["identity_authority"], "CEW-ID-1.0")
        self.assertEqual(model["classification_authority"], "CEW-CLASS-1.0")
        self.assertEqual(model["habitat_authority"], "CEW-HAB-1.0")
        self.assertEqual(model["distribution_authority"], "CEW-DIST-1.0")
        self.assertEqual(model["ecological_role_authority"], "CEW-ECO-1.0")
        self.assertEqual(model["relationship_pathway_authority"], "CEW-REL-PATH-1.0")
        self.assertFalse(model["application_implementation_authority"])
        self.assertFalse(model["canonical_creature_definition_mutation_authorized"])
        self.assertEqual(model["strict_successor"], "CEW-13")

    def test_library_is_broad_but_not_an_exhaustive_species_encyclopedia(self):
        model = self.load(MODEL)
        library = self.load(LIBRARY)
        self.assertEqual(library["profile_count"], 100)
        self.assertEqual(len(library["profiles"]), 100)
        self.assertFalse(model["baseline_policy"]["exhaustive_earth_species_encyclopedia_target"])
        self.assertFalse(model["baseline_policy"]["profile_count_is_completeness_or_quality_score"])
        self.assertFalse(model["baseline_policy"]["quota_driven_cew13_gap_expansion_authorized"])

    def test_required_ordinary_taxonomic_groups_are_represented(self):
        library = self.load(LIBRARY)
        required = {
            "mammal",
            "bird",
            "reptile",
            "amphibian",
            "bony_fish",
            "cartilaginous_fish",
            "insect",
            "arachnid",
            "crustacean",
            "mollusk",
            "other_invertebrate",
        }
        self.assertEqual(set(library["controlled_taxonomy_groups"]), required)
        counts = Counter(row["taxonomy_group"] for row in library["profiles"])
        self.assertEqual(set(counts), required)
        self.assertTrue(all(counts[group] >= 4 for group in required))
        self.assertEqual(library["taxonomy_group_counts"], dict(sorted(counts.items())))

    def test_profiles_are_noncanonical_content_profiles_with_no_statblock_promotion(self):
        library = self.load(LIBRARY)
        ids = [row["baseline_profile_id"] for row in library["profiles"]]
        names = [row["display_name"] for row in library["profiles"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(names), len(set(names)))
        forbidden = {"ac", "hp", "damage", "speed", "cr", "attack_bonus", "saving_throw_dc"}
        for row in library["profiles"]:
            self.assertTrue(row["baseline_profile_id"].startswith("cew12.earthlike."))
            self.assertIsNone(row["canonical_stable_id_binding"])
            self.assertIsNone(row["canonical_distribution_binding"])
            self.assertEqual(row["relationship_pathway_state"], "unknown")
            self.assertEqual(row["cognition_personhood_state"], "unknown")
            self.assertFalse(forbidden.intersection(row))
            self.assertGreaterEqual(len(row["habitat_families"]), 1)
            self.assertGreaterEqual(len(row["ecological_roles"]), 1)

    def test_source_recovery_preserves_animals_pdf_without_promoting_unsafe_statblocks(self):
        evidence = self.load(EVIDENCE)
        docs = {row["source_document"]: row for row in evidence["source_documents"]}
        self.assertEqual(docs["animals 11-16-24.PDF"]["sha256"], "6b9e8a4b1e30001f38bf2012933a7ec5704a02b6177dbc38b0707d6f44545f3e")
        self.assertEqual(docs["animals 11-16-24.PDF"]["page_count"], 3)
        self.assertEqual(evidence["animals_source_label_count"], 33)
        self.assertEqual(len(evidence["animals_source_labels"]), 33)
        self.assertEqual(evidence["animals_source_safe_statblock_record_count"], 0)
        self.assertTrue(evidence["animals_source_evidence_absence_is_not_inferred"])
        self.assertFalse(evidence["animals_table_mechanics_promoted_to_canonical_statblocks"])
        self.assertEqual(evidence["ordinary_baseline_seed_count_from_animals_pdf"], 32)
        self.assertEqual(evidence["source_labels_excluded_from_ordinary_baseline"], ["Spider (Giant)"])

    def test_retained_beast_collections_are_context_not_ordinary_identity_conversion(self):
        evidence = self.load(EVIDENCE)
        docs = {row["source_document"]: row for row in evidence["source_documents"]}
        self.assertEqual(docs["Beast Creatures 1.PDF"]["sha256"], "3b7a1b666e142cf0dd4bf74449855cd1fc5abccd881cec64c0c0e095faaa8b4b")
        self.assertEqual(docs["Beasts 2.PDF"]["sha256"], "e595d7b6738316e5858c1688f16758d00edbffd60904f4ab2aeabac31d873c26")
        self.assertEqual(evidence["beast_creatures_1_thematic_profile_count"], 120)
        self.assertEqual(evidence["beasts_2_candidate_start_count"], 81)
        self.assertEqual(evidence["beasts_2_safe_statblock_record_count"], 80)
        self.assertFalse(evidence["beast_collection_membership_means_ordinary_earthlike"])
        self.assertFalse(evidence["beast_source_label_means_canonical_definition"])

    def test_source_and_first_party_authoring_are_explicitly_distinguished(self):
        library = self.load(LIBRARY)
        counts = Counter(row["provenance_kind"] for row in library["profiles"])
        self.assertEqual(counts["source_recovered_seed"], 32)
        self.assertEqual(counts["governed_first_party_baseline"], 68)
        self.assertEqual(library["provenance_kind_counts"], dict(sorted(counts.items())))
        for row in library["profiles"]:
            if row["provenance_kind"] == "source_recovered_seed":
                self.assertEqual(row["source_document"], "animals 11-16-24.PDF")
                self.assertEqual(row["source_fact_scope"], "identity_label_and_ordinary_animal_profile_seed_only")
            else:
                self.assertIsNone(row["source_document"])
                self.assertEqual(row["source_fact_scope"], "governed_first_party_ecological_baseline_authoring")

    def test_habitat_and_ecology_are_useful_without_becoming_distribution(self):
        model = self.load(MODEL)
        library = self.load(LIBRARY)
        habitat_counts = Counter(h for row in library["profiles"] for h in row["habitat_families"])
        role_counts = Counter(r for row in library["profiles"] for r in row["ecological_roles"])
        for required_habitat in [
            "forest_woodland",
            "grassland_open_country",
            "desert_scrub",
            "freshwater_river_lake",
            "wetland_marsh",
            "coastal_intertidal",
            "marine_open_water",
            "alpine_mountain",
            "polar_tundra",
            "subterranean_cave",
            "settled_rural_urban",
        ]:
            self.assertIn(required_habitat, habitat_counts)
        for required_role in [
            "predator",
            "prey",
            "grazer",
            "browser",
            "scavenger",
            "decomposer",
            "pollinator",
            "parasite",
            "detritivore",
            "filter_feeder",
        ]:
            self.assertIn(required_role, role_counts)
        self.assertFalse(model["non_inference_rules"]["earthlike_baseline_implies_earth_canonical_range"])
        self.assertFalse(model["non_inference_rules"]["habitat_fit_implies_canonical_presence"])
        self.assertFalse(model["non_inference_rules"]["ordinary_baseline_implies_common_or_visible"])
        self.assertFalse(model["non_inference_rules"]["ecological_role_implies_encounter_placement"])

    def test_personhood_relationship_and_havalaea_boundaries_survive_baseline_authoring(self):
        model = self.load(MODEL)
        rules = model["non_inference_rules"]
        self.assertFalse(rules["ordinary_earthlike_implies_nonsapient"])
        self.assertFalse(rules["domestic_species_implies_pet_or_companion"])
        self.assertFalse(rules["large_species_implies_mount"])
        self.assertFalse(rules["small_species_implies_familiar"])
        self.assertFalse(rules["baseline_profile_implies_havalaea_native_lineage"])
        self.assertFalse(rules["baseline_profile_implies_npc_projection"])
        self.assertTrue(model["consent_boundary"]["sapient_person_level_relationships_require_voluntary_consent"])

    def test_contract_text_states_core_baseline_rules(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "Earthlike baseline is an ecological content library, not a canonical Earth distribution claim.",
            "Source recovery and governed first-party baseline authoring remain distinguishable.",
            "The retained animals table is evidence, not a canonical statblock registry.",
            "Ordinary does not mean nonsapient.",
            "Domestic does not mean pet, companion, mount, familiar, owned, bonded, or trained.",
            "CEW-13 owns environment-driven wildlife gap expansion.",
            "CEW-13 is the strict successor.",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_is_monotonic_and_selects_cew13(self):
        backlog = self.load(BACKLOG)
        strict_order = backlog["strict_order"]
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-12"))
        self.assertEqual(status["CEW-12"], "completed_verified")
        if backlog["completed_through"] == "CEW-12":
            self.assertEqual(backlog["current_item"], "CEW-13")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(status["CEW-13"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-12"))
        decisions = backlog["cew12_decisions"]
        self.assertEqual(decisions["contract_id"], "CEW-EARTHLIKE-BASE-1.0")
        self.assertEqual(decisions["baseline_profile_count"], 100)
        self.assertEqual(decisions["taxonomy_group_count"], 11)
        self.assertEqual(decisions["animals_source_label_count"], 33)
        self.assertEqual(decisions["ordinary_source_seed_count"], 32)
        self.assertEqual(decisions["canonical_creature_definition_bindings_created"], 0)
        self.assertFalse(decisions["canonical_distribution_authored"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertIn("CEW-13", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
