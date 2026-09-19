from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/player-species/contracts"
VALIDATION = D / "MVPS-12_VALIDATION_CONTRACT.json"
MIGRATION = D / "MVPS-12_MIGRATION_CONTRACT.json"
IMPORT_EXPORT = D / "MVPS-12_IMPORT_EXPORT_CONTRACT.json"
FIXTURES = D / "MVPS-12_VALIDATION_MIGRATION_IMPORT_EXPORT_FIXTURES.json"
INVARIANTS = D / "MVPS-12_INVARIANTS.json"


class MVPS12ValidationMigrationImportExportTests(unittest.TestCase):
    def _j(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self):
        for path in (VALIDATION, MIGRATION, IMPORT_EXPORT, FIXTURES, INVARIANTS):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_validation_states_are_explicit_and_missing_canon_is_never_fabricated(self):
        c = self._j(VALIDATION)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesValidation")
        self.assertEqual(
            c["validation_states"],
            ["playable", "incomplete", "invalid", "migration_required"],
        )
        self.assertEqual(
            c["validation_layers"],
            ["structural", "behavioral", "integration"],
        )
        self.assertFalse(c["missing_canon_policy"]["fabricate_or_default_missing_canon"])
        self.assertEqual(
            c["missing_canon_policy"]["disposition"],
            "surface_unresolved_or_incomplete_with_source_evidence",
        )
        self.assertTrue(c["findings"]["rule_source_refs_required"])
        self.assertTrue(c["findings"]["provenance_refs_required"])

    def test_migration_preserves_history_and_requires_explicit_replacement(self):
        c = self._j(MIGRATION)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesMigration")
        self.assertTrue(c["historical_selection_policy"]["preserve_character_species_selection_receipt"])
        self.assertTrue(c["historical_selection_policy"]["preserve_exact_species_version_ref"])
        self.assertTrue(c["historical_selection_policy"]["preserve_lineage_form_and_choice_selections"])
        self.assertTrue(c["historical_selection_policy"]["preserve_adjudication_and_provenance"])
        self.assertFalse(c["replacement_policy"]["silent_substitution_allowed"])
        self.assertTrue(c["migration_receipt"]["required"])
        self.assertTrue(c["migration_discrepancy"]["required_when_unresolved_or_incompatible"])

    def test_import_export_preserves_identity_provenance_and_owner_references(self):
        c = self._j(IMPORT_EXPORT)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesImportExport")
        self.assertTrue(c["round_trip_guarantees"]["stable_identity"])
        self.assertTrue(c["round_trip_guarantees"]["exact_version_refs"])
        self.assertTrue(c["round_trip_guarantees"]["provenance"])
        self.assertTrue(c["round_trip_guarantees"]["unresolved_and_conflict_state"])
        self.assertTrue(c["round_trip_guarantees"]["owner_domain_references"])
        self.assertFalse(c["flattening_policy"]["shared_mechanics_copied_into_species_local_data"])
        self.assertTrue(c["permission_filter_before_export"])

    def test_shared_owner_boundaries_remain_explicit(self):
        v = self._j(VALIDATION)
        m = self._j(MIGRATION)
        x = self._j(IMPORT_EXPORT)
        self.assertEqual(v["shared_owner_handoff"]["character_validation"], "A4 CharacterValidationPort")
        self.assertEqual(m["shared_owner_handoff"]["character_migration"], "A4 CharacterMigrationPort")
        self.assertEqual(x["shared_owner_handoff"]["character_export"], "A4 CharacterExportPort")
        self.assertEqual(x["shared_owner_handoff"]["content_import"], "Authoring ImportMappingPort")
        self.assertEqual(x["shared_owner_handoff"]["content_export"], "RoleFilteredContentExportPort")
        self.assertFalse(v["generic_validation_engine_created"])
        self.assertFalse(m["generic_migration_engine_created"])
        self.assertFalse(x["generic_import_export_engine_created"])

    def test_fixtures_cover_acceptance_and_failure_modes(self):
        cases = self._j(FIXTURES)["cases"]
        required = {
            "missing_required_canon",
            "invalid_cross_owner_reference",
            "deprecated_species_historical_selection",
            "explicit_version_replacement",
            "migration_discrepancy",
            "definition_round_trip",
            "character_selection_round_trip",
        }
        self.assertTrue(required <= set(cases))
        self.assertEqual(cases["missing_required_canon"]["expected"]["state"], "incomplete")
        self.assertFalse(cases["missing_required_canon"]["expected"]["canon_fabricated"])
        self.assertTrue(cases["deprecated_species_historical_selection"]["expected"]["historical_receipt_preserved"])
        self.assertTrue(cases["migration_discrepancy"]["expected"]["receipt_or_discrepancy_emitted"])
        self.assertTrue(cases["definition_round_trip"]["expected"]["owner_refs_preserved"])

    def test_invariants_lock_mvps12_scope_and_mvps13_boundary(self):
        c = self._j(INVARIANTS)
        ids = {item["id"] for item in c["invariants"]}
        self.assertTrue(
            {
                "MVPS12-I01-no-missing-canon-fabrication",
                "MVPS12-I02-explicit-validation-state",
                "MVPS12-I03-history-preserved",
                "MVPS12-I04-no-silent-replacement",
                "MVPS12-I05-migration-receipt-or-discrepancy",
                "MVPS12-I06-round-trip-preserves-references",
                "MVPS12-I07-shared-owner-delegation",
                "MVPS12-I08-runtime-projection-remains-mvps13",
            }
            <= ids
        )
        self.assertFalse(c["runtime_projection_created"])
        self.assertEqual(c["runtime_projection_owner"], "MVPS-13")


if __name__ == "__main__":
    unittest.main()
