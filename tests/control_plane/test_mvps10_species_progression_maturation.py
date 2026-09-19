from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/player-species/contracts"
PROGRESSION = D / "MVPS-10_SPECIES_PROGRESSION_HOOK_CONTRACT.json"
MATURATION = D / "MVPS-10_MATURATION_EVENT_CONTRACT.json"
FIXTURES = D / "MVPS-10_PROGRESSION_FIXTURES.json"
INVARIANTS = D / "MVPS-10_INVARIANTS.json"


class MVPS10SpeciesProgressionMaturationTests(unittest.TestCase):
    def _j(self, p: Path) -> dict:
        return json.loads(p.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self):
        for p in (PROGRESSION, MATURATION, FIXTURES, INVARIANTS):
            with self.subTest(path=p):
                self.assertTrue(p.is_file(), p)

    def test_species_progression_is_optional_and_shared_owner_backed(self):
        c = self._j(PROGRESSION)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesProgressionHook")
        self.assertFalse(c["species_progression_required"])
        self.assertTrue(c["no_progression_hook_is_valid"])
        self.assertFalse(c["species_specific_progression_engine_created"])
        self.assertEqual(c["acquisition_policy"], "reference_and_handoff_only")
        self.assertEqual(c["unknown_or_conflict_policy"], "surface_unresolved_not_guess")

    def test_advancement_is_event_sourced_and_history_preserving(self):
        c = self._j(PROGRESSION)
        e = c["event_sourcing"]
        self.assertTrue(e["all_permanent_or_conditional_advancement_event_sourced"])
        self.assertTrue(e["durable_event_required_for_acquisition"])
        self.assertTrue(e["historical_event_records_immutable"])
        self.assertFalse(e["silent_character_mutation_allowed"])
        self.assertTrue({"before_state_ref","selected_option_ref","cost_receipt_ref","grant_refs","prerequisite_evidence_refs","rules_source_refs","resulting_state_ref","provenance_ref"} <= set(e["required_event_evidence"]))

    def test_maturation_does_not_turn_age_into_automatic_entitlement(self):
        c = self._j(MATURATION)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesMaturationEventHook")
        self.assertTrue(c["lifecycle_descriptor_non_executable"])
        self.assertFalse(c["chronological_age_is_progression_entitlement"])
        self.assertTrue(c["mechanical_stage_change_requires_explicit_event"])
        self.assertFalse(c["automatic_unlock_from_age_without_authorizing_rule"])
        self.assertTrue(c["base_species_selection_history_preserved"])
        self.assertEqual(c["lifecycle_descriptor_owner"], "MVPS-05")
        self.assertEqual(c["form_transformation_owner"], "MVPS-09")

    def test_duplicate_grants_and_costs_defer_to_shared_owners(self):
        c = self._j(PROGRESSION)
        self.assertEqual(c["duplicate_grant_policy"], "defer_to_shared_owner_stacking_replacement")
        self.assertFalse(c["species_local_duplicate_resolution_allowed"])
        self.assertFalse(c["species_local_xp_or_cost_engine_created"])
        self.assertEqual(c["cab_policy"], "eligibility_acquisition_cost_and_reference_value_owned_by_CAB")
        self.assertFalse(c["runtime_projection_created"])
        self.assertEqual(c["runtime_projection_owner"], "MVPS-13")

    def test_fixtures_cover_optional_event_maturation_duplicates_and_unknowns(self):
        f = self._j(FIXTURES)["cases"]
        self.assertTrue({
            "no_species_progression",
            "explicit_species_unlock_event",
            "maturation_stage_unlock",
            "duplicate_grant_owner_deferred",
            "age_without_authorizing_rule_unresolved",
            "missing_advancement_event_rejected",
        } <= set(f))
        self.assertEqual(f["no_species_progression"]["expected"]["status"], "valid_no_progression")
        self.assertTrue(f["explicit_species_unlock_event"]["expected"]["event_sourced"])
        self.assertTrue(f["maturation_stage_unlock"]["expected"]["base_selection_history_preserved"])
        self.assertEqual(f["duplicate_grant_owner_deferred"]["expected"]["status"], "owner_deferred")
        self.assertEqual(f["age_without_authorizing_rule_unresolved"]["expected"]["status"], "unresolved")
        self.assertEqual(f["missing_advancement_event_rejected"]["expected"]["status"], "invalid")

    def test_invariants_cover_acceptance_and_boundaries(self):
        ids = {x["id"] for x in self._j(INVARIANTS)["invariants"]}
        self.assertTrue({
            "MVPS10-I01-progression-optional",
            "MVPS10-I02-advancement-event-sourced",
            "MVPS10-I03-maturation-explicit-not-age-entitlement",
            "MVPS10-I04-shared-acquisition-eligibility-owners",
            "MVPS10-I05-duplicate-grants-shared-owner",
            "MVPS10-I06-history-and-provenance-preserved",
            "MVPS10-I07-no-species-progression-engine",
            "MVPS10-I08-form-and-runtime-projection-boundaries",
        } <= ids)


if __name__ == "__main__":
    unittest.main()
