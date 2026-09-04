import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
RECOVERY = CEW / "CEW-14_SETTING_FAUNA_RECOVERY_v1.0.0.json"
EXPANSION = CEW / "CEW-14_MULTIVERSAL_ALIEN_WILDLIFE_EXPANSION_v1.0.0.json"
CONTRACT = CEW / "CEW-14_MULTIVERSAL_ALIEN_WILDLIFE_CONTRACT.md"
REPORT = CEW / "CEW-14_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew14MultiversalAlienWildlifeExpansionTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_cew14_acceptance_boundary(self):
        self.assertTrue(RECOVERY.exists(), "CEW-14 setting fauna recovery is missing")
        self.assertTrue(EXPANSION.exists(), "CEW-14 multiversal/alien wildlife expansion is missing")
        self.assertTrue(CONTRACT.exists(), "CEW-14 contract is missing")
        self.assertTrue(REPORT.exists(), "CEW-14 completion report is missing")

        recovery = self.load(RECOVERY)
        expansion = self.load(EXPANSION)
        backlog = self.load(BACKLOG)
        contract = CONTRACT.read_text(encoding="utf-8")
        report = REPORT.read_text(encoding="utf-8")

        self.assertEqual(recovery["contract_id"], "CEW-ALIEN-WILD-1.0")
        self.assertEqual(recovery["work_item"], "CEW-14")
        self.assertEqual(recovery["source_first_policy"]["havalaea_source_profile_count_carried_forward"], 46)
        self.assertEqual(recovery["source_first_policy"]["skoaltarran_safe_statblock_record_count"], 39)
        self.assertFalse(recovery["source_first_policy"]["setting_collection_membership_proves_native_status"])
        self.assertFalse(recovery["source_first_policy"]["source_recovery_creates_canonical_identity"])
        self.assertEqual(len(recovery["skoaltarran_setting_fauna_records"]), 39)
        for row in recovery["skoaltarran_setting_fauna_records"]:
            self.assertEqual(row["identity_state"], "recoverable_source_record")
            self.assertEqual(row["setting_scope"], "Skoaltarran")
            self.assertEqual(row["native_status"], "unknown")
            self.assertIsNone(row["canonical_stable_id_binding"])
            self.assertEqual(row["personhood_state"], "unknown")

        self.assertEqual(expansion["contract_id"], "CEW-ALIEN-WILD-1.0")
        self.assertEqual(expansion["work_item"], "CEW-14")
        self.assertEqual(expansion["cew13_nonordinary_input"]["deferred_preset_count"], 10)
        self.assertEqual(len(expansion["cew13_nonordinary_input"]["presets"]), 10)
        self.assertEqual(len({row["preset_id"] for row in expansion["cew13_nonordinary_input"]["presets"]}), 10)
        self.assertFalse(expansion["policy"]["species_quota_authorized"])
        self.assertFalse(expansion["policy"]["numeric_ecological_score_authorized"])
        self.assertFalse(expansion["policy"]["habitat_fit_creates_distribution"])
        self.assertFalse(expansion["policy"]["environment_similarity_creates_identity"])
        self.assertFalse(expansion["policy"]["cew15_monster_or_type_gap_expansion_authored"])
        self.assertEqual(expansion["strict_successor"], "CEW-15")

        gaps = expansion["gap_anchors"]
        self.assertGreaterEqual(len(gaps), 10)
        gap_ids = {row["gap_id"] for row in gaps}
        required = {
            "CEW14-GAP-STATION-LIVING",
            "CEW14-GAP-STATION-DERELICT",
            "CEW14-GAP-VOID",
            "CEW14-GAP-ASTEROID",
            "CEW14-GAP-GAS-GIANT",
            "CEW14-GAP-WRECKFIELD",
            "CEW14-GAP-FLOATING-MEGACITY",
            "CEW14-GAP-BLACK-HOLE",
            "CEW14-GAP-WORMHOLE",
            "CEW14-GAP-NEBULA",
        }
        self.assertTrue(required.issubset(gap_ids))

        profiles = expansion["profiles"]
        self.assertEqual(expansion["profile_count"], len(profiles))
        self.assertGreater(expansion["profile_count"], 0)
        self.assertFalse(expansion["profile_count_is_target_or_quota"])
        covered = set()
        ids = set()
        allowed_predicates = {"requires", "prefers", "tolerates", "excludes", "depends_on", "unknown"}
        for row in profiles:
            self.assertEqual(row["identity_kind"], "noncanonical_nonsapient_alien_wildlife_profile")
            self.assertEqual(row["provenance_kind"], "governed_first_party_cew14_design")
            self.assertIsNone(row["canonical_stable_id_binding"])
            self.assertIsNone(row["canonical_distribution_binding"])
            self.assertEqual(row["sapience_state"], "explicitly_absent")
            self.assertEqual(row["personhood_state"], "explicitly_absent")
            self.assertEqual(row["relationship_pathway_state"], "unknown")
            self.assertFalse(row["statblock_authored"])
            self.assertFalse(row["encounter_placement_authored"])
            self.assertTrue(row["environment_gap_ids"])
            self.assertTrue(row["habitat_predicates"])
            self.assertNotIn(row["profile_id"], ids)
            ids.add(row["profile_id"])
            covered.update(row["environment_gap_ids"])
            for fact in row["habitat_predicates"]:
                self.assertIn(fact["predicate"], allowed_predicates)
                self.assertEqual(fact["authority"], "CEW-14 governed first-party")
        self.assertTrue(required.issubset(covered))

        boundary = expansion["mutation_boundary"]
        self.assertFalse(boundary["canonical_creature_definitions_created"])
        self.assertFalse(boundary["canonical_distribution_authored"])
        self.assertFalse(boundary["multiversal_app_runtime_mutation"])
        self.assertFalse(boundary["relationship_state_created"])
        self.assertFalse(boundary["campaign_or_encounter_placement_created"])
        self.assertFalse(boundary["cew15_type_taxonomy_mutation"])

        strict_order = backlog["strict_order"]
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-14"))
        cew14 = next(row for row in backlog["tranches"] if row["id"] == "CEW-14")
        self.assertEqual(cew14["status"], "completed_verified")
        self.assertEqual(backlog["current_item"], "CEW-15")
        self.assertEqual(backlog["current_item_state"], "selected_not_started")

        self.assertIn("source recovery precedes new invention", contract.lower())
        self.assertIn("setting-collection membership does not prove native status", contract.lower())
        self.assertIn("CEW-15", contract)
        self.assertIn("CEW-15 — Monster, Extraordinary Creature & Creature-Type Gap Expansion", report)


if __name__ == "__main__":
    unittest.main()
