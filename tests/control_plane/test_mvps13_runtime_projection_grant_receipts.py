from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/player-species/contracts"
PROJECTION = D / "MVPS-13_RUNTIME_PROJECTION_CONTRACT.json"
RECEIPTS = D / "MVPS-13_GRANT_RECEIPT_COMPOSITION_CONTRACT.json"
FIXTURES = D / "MVPS-13_RUNTIME_PROJECTION_FIXTURES.json"
INVARIANTS = D / "MVPS-13_INVARIANTS.json"


class MVPS13RuntimeProjectionGrantReceiptTests(unittest.TestCase):
    def _j(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self):
        for path in (PROJECTION, RECEIPTS, FIXTURES, INVARIANTS):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_projection_is_exact_versioned_deterministic_and_non_mutating(self):
        c = self._j(PROJECTION)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesRuntimeProjection")
        self.assertTrue(c["deterministic"])
        self.assertTrue(c["input_contract"]["exact_version_refs_required"])
        self.assertEqual(
            c["composition_order"],
            ["base_species", "lineages", "adaptations", "campaign_adjudications", "active_form_overlay"],
        )
        self.assertTrue(c["base_selection_history_preserved"])
        self.assertFalse(c["temporary_runtime_state_mutates_base_selection"])
        self.assertFalse(c["canonical_shared_mechanics_copied_into_projection"])

    def test_invalid_or_unresolved_inputs_do_not_silently_project(self):
        c = self._j(PROJECTION)
        p = c["validation_gate"]
        self.assertEqual(p["playable"], "projection_allowed")
        self.assertEqual(p["incomplete"], "projection_blocked")
        self.assertEqual(p["invalid"], "projection_blocked")
        self.assertEqual(p["migration_required"], "projection_blocked_except_explicit_historical_read")
        self.assertFalse(p["missing_or_conflicted_input_defaults_allowed"])

    def test_active_form_is_an_overlay_not_history_rewrite(self):
        c = self._j(PROJECTION)
        f = c["active_form_policy"]
        self.assertTrue(f["overlay_only"])
        self.assertTrue(f["source_form_and_target_form_refs_preserved"])
        self.assertTrue(f["retained_and_replaced_contributions_explicit"])
        self.assertFalse(f["base_species_or_lineage_rewritten"])
        self.assertTrue(f["reversal_uses_recorded_pre_transform_state"])

    def test_every_projected_contribution_and_grant_receipt_is_traceable(self):
        c = self._j(RECEIPTS)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesGrantReceiptComposition")
        required = set(c["projected_contribution"]["required_fields"])
        self.assertTrue({
            "contribution_id", "record_ref", "owner_domain", "source_layer",
            "source_ref", "source_version_ref", "provenance_refs",
            "activation_state", "stacking_replacement_policy_ref"
        } <= required)
        receipt_required = set(c["character_species_grant_receipt"]["required_fields"])
        self.assertTrue({
            "grant_receipt_id", "record_ref", "grant_source_ref", "grant_reason",
            "grant_event_ref", "permanence", "activation_state",
            "stacking_replacement_policy"
        } <= receipt_required)
        self.assertTrue(c["receipt_identity"]["stable_across_replay_for_same_inputs"])
        self.assertTrue(c["receipt_identity"]["input_digest_required"])

    def test_shared_owners_retain_mechanics_and_character_projection_authority(self):
        p = self._j(PROJECTION)
        r = self._j(RECEIPTS)
        self.assertEqual(p["shared_owner_handoff"]["character_projection"], "A4 CharacterProjectionPort")
        self.assertFalse(p["generic_character_projection_engine_created"])
        self.assertFalse(p["shared_mechanic_execution_owned_by_mvps13"])
        self.assertFalse(r["stacking_or_replacement_resolution_owned_by_mvps13"])
        self.assertFalse(r["character_persistence_mutation_owned_by_mvps13"])

    def test_fixtures_cover_replay_form_overlay_and_failure_boundaries(self):
        cases = self._j(FIXTURES)["cases"]
        required = {
            "deterministic_replay",
            "temporary_form_overlay",
            "same_grant_multiple_sources",
            "migration_required_selection",
            "unresolved_lineage_conflict",
            "campaign_adjudication",
        }
        self.assertTrue(required <= set(cases))
        self.assertTrue(cases["deterministic_replay"]["expected"]["same_input_digest_same_projection_digest"])
        self.assertTrue(cases["temporary_form_overlay"]["expected"]["base_selection_history_unchanged"])
        self.assertTrue(cases["temporary_form_overlay"]["expected"]["temporary_contributions_traceable"])
        self.assertEqual(cases["migration_required_selection"]["expected"]["status"], "projection_blocked")
        self.assertEqual(cases["unresolved_lineage_conflict"]["expected"]["status"], "projection_blocked")
        self.assertEqual(cases["same_grant_multiple_sources"]["expected"]["resolution"], "shared_owner_handoff")

    def test_invariants_lock_mvps13_scope(self):
        ids = {x["id"] for x in self._j(INVARIANTS)["invariants"]}
        self.assertTrue({
            "MVPS13-I01-deterministic-replay",
            "MVPS13-I02-exact-version-inputs",
            "MVPS13-I03-base-history-immutable",
            "MVPS13-I04-temporary-form-overlay",
            "MVPS13-I05-source-traceable-contributions",
            "MVPS13-I06-shared-owner-stacking",
            "MVPS13-I07-validation-gated-projection",
            "MVPS13-I08-no-generic-character-engine",
        } <= ids)


if __name__ == "__main__":
    unittest.main()
