import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
MODEL = CEW / "CEW-13_ENVIRONMENT_WILDLIFE_GAP_MODEL_v1.0.0.json"
LIBRARY = CEW / "CEW-13_ENVIRONMENT_DRIVEN_WILDLIFE_EXPANSION_v1.0.0.json"
CONTRACT = CEW / "CEW-13_ENVIRONMENT_WILDLIFE_GAP_CONTRACT.md"
REPORT = CEW / "CEW-13_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew13EnvironmentDrivenWildlifeGapExpansionTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_cew13_acceptance_boundary(self):
        self.assertTrue(MODEL.exists(), "CEW-13 gap model is missing")
        self.assertTrue(LIBRARY.exists(), "CEW-13 expansion library is missing")
        self.assertTrue(CONTRACT.exists(), "CEW-13 contract is missing")
        self.assertTrue(REPORT.exists(), "CEW-13 completion report is missing")

        model = self.load(MODEL)
        library = self.load(LIBRARY)
        backlog = self.load(BACKLOG)
        contract = CONTRACT.read_text(encoding="utf-8")
        report = REPORT.read_text(encoding="utf-8")

        self.assertEqual(model["contract_id"], "CEW-ENV-GAP-1.0")
        self.assertEqual(model["work_item"], "CEW-13")
        self.assertEqual(model["environment_inputs"]["preset_count"], 76)
        self.assertEqual(model["environment_inputs"]["archetype_count"], 19)
        self.assertEqual(model["environment_inputs"]["overlay_count"], 47)
        self.assertEqual(model["cew12_input"]["baseline_profile_count"], 100)
        self.assertEqual(model["cew12_input"]["habitat_family_count"], 11)
        self.assertFalse(model["policy"]["species_quota_authorized"])
        self.assertFalse(model["policy"]["numeric_gap_score_authorized"])
        self.assertFalse(model["policy"]["habitat_fit_creates_distribution"])
        self.assertFalse(model["policy"]["environment_similarity_creates_canonical_identity"])
        self.assertFalse(model["policy"]["environment_selection_creates_encounter_placement"])
        self.assertEqual(model["strict_successor"], "CEW-14")

        audit = model["preset_audit"]
        self.assertEqual(len(audit), 76)
        self.assertEqual(len({row["preset_id"] for row in audit}), 76)
        status_values = {row["coverage_status"] for row in audit}
        self.assertIn("cew13_gap_expansion_authored", status_values)
        self.assertIn("cew12_baseline_reuse_sufficient", status_values)
        self.assertIn("deferred_nonordinary_cew14", status_values)
        self.assertIn("deferred_extraordinary_cew15", status_values)
        self.assertIn("distribution_dependent_no_auto_expansion", status_values)

        gaps = model["gap_anchors"]
        self.assertGreaterEqual(len(gaps), 20)
        gap_ids = {row["gap_id"] for row in gaps}
        required_gap_ids = {
            "GAP-FW-FLOWING",
            "GAP-FW-FLOODPLAIN",
            "GAP-FW-ESTUARY",
            "GAP-FW-PEAT-WETLAND",
            "GAP-FW-FLOODED-FOREST",
            "GAP-MAR-TIDAL-FLATS",
            "GAP-MAR-CORAL-REEF",
            "GAP-MAR-KELP-FOREST",
            "GAP-MAR-DEEP-OCEAN",
            "GAP-MAR-HADAL-TRENCH",
            "GAP-OC-SAVANNA",
            "GAP-OC-STEPPE",
            "GAP-OC-SCRUB",
            "GAP-DL-CANYON",
            "GAP-DL-ROCKY-DESERT",
            "GAP-DL-SALT-FLATS",
            "GAP-CP-TAIGA",
            "GAP-CP-GLACIER",
            "GAP-CP-SEA-ICE",
            "GAP-SI-FARMLAND",
            "GAP-SI-ROAD-TRAIL",
            "GAP-SI-MINE-QUARRY",
            "GAP-SI-TRANSIT-HUB",
            "GAP-SI-HARBOR-DOCKS",
        }
        self.assertTrue(required_gap_ids.issubset(gap_ids))

        self.assertEqual(library["contract_id"], "CEW-ENV-GAP-1.0")
        self.assertEqual(library["profile_count"], len(library["profiles"]))
        self.assertGreater(library["profile_count"], 0)
        self.assertFalse(library["profile_count_is_target_or_quota"])
        profile_ids = {row["gap_profile_id"] for row in library["profiles"]}
        self.assertEqual(len(profile_ids), library["profile_count"])

        covered_gap_ids = set()
        allowed_predicates = {"requires", "prefers", "tolerates", "excludes", "depends_on", "unknown"}
        for row in library["profiles"]:
            self.assertEqual(row["identity_kind"], "noncanonical_environment_gap_profile")
            self.assertEqual(row["provenance_kind"], "governed_first_party_environment_gap_expansion")
            self.assertIsNone(row["canonical_stable_id_binding"])
            self.assertIsNone(row["canonical_distribution_binding"])
            self.assertEqual(row["relationship_pathway_state"], "unknown")
            self.assertEqual(row["cognition_personhood_state"], "unknown")
            self.assertFalse(row["statblock_authored"])
            self.assertFalse(row["encounter_placement_authored"])
            self.assertTrue(row["environment_gap_ids"])
            self.assertTrue(row["habitat_predicates"])
            covered_gap_ids.update(row["environment_gap_ids"])
            for fact in row["habitat_predicates"]:
                self.assertIn(fact["predicate"], allowed_predicates)
                self.assertEqual(fact["authority"], "CEW-13 governed first-party")

        authored_gap_ids = {row["gap_id"] for row in gaps if row["resolution"] == "cew13_profiles_authored"}
        self.assertTrue(authored_gap_ids.issubset(covered_gap_ids))

        self.assertFalse(library["mutation_boundary"]["canonical_creature_definitions_created"])
        self.assertFalse(library["mutation_boundary"]["canonical_distribution_authored"])
        self.assertFalse(library["mutation_boundary"]["multiversal_app_runtime_mutation"])
        self.assertFalse(library["mutation_boundary"]["relationship_state_created"])
        self.assertFalse(library["mutation_boundary"]["campaign_or_encounter_placement_created"])

        strict_order = backlog["strict_order"]
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-13"))
        cew13 = next(row for row in backlog["tranches"] if row["id"] == "CEW-13")
        self.assertEqual(cew13["status"], "completed_verified")
        self.assertIn(backlog["current_item"], strict_order)
        self.assertGreaterEqual(strict_order.index(backlog["current_item"]), strict_order.index("CEW-14"))
        if backlog["current_item"] == "CEW-14":
            self.assertEqual(backlog["current_item_state"], "selected_not_started")

        self.assertIn("Habitat suitability is not canonical distribution", contract)
        self.assertIn("No numeric gap score", contract)
        self.assertIn("CEW-14", contract)
        self.assertIn("CEW-15", contract)
        self.assertIn("CEW-14 — Multiversal & Alien Wildlife Expansion", report)


if __name__ == "__main__":
    unittest.main()
