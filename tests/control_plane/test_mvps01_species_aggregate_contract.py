from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_DIR = ROOT / "governance/application-planning/player-species/contracts"
SPECIES = CONTRACT_DIR / "SPECIES_DEFINITION_CONTRACT.json"
SELECTION = CONTRACT_DIR / "CHARACTER_SPECIES_SELECTION_CONTRACT.json"
INVARIANTS = CONTRACT_DIR / "MVPS-01_INVARIANTS.json"
FIXTURES = CONTRACT_DIR / "MVPS-01_CONTRACT_FIXTURES.json"


class MVPS01SpeciesAggregateContractTests(unittest.TestCase):
    def _json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_contract_artifacts_exist(self) -> None:
        for path in (SPECIES, SELECTION, INVARIANTS, FIXTURES):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_species_definition_contract_has_canonical_aggregate_boundaries(self) -> None:
        species = self._json(SPECIES)
        self.assertEqual(species["contract_id"], "MVPS.SpeciesDefinition")
        self.assertEqual(species["record_type"], "SpeciesDefinition")
        self.assertEqual(species["mechanics_policy"], "references_and_grants_only")
        self.assertEqual(species["descriptive_fields_policy"], "non_executable")
        self.assertEqual(species["extension_policy"]["override_core_fields"], False)
        self.assertEqual(species["extension_policy"]["namespace_required"], True)

        required = set(species["required_top_level_fields"])
        self.assertTrue({
            "identity", "versioning", "provenance", "lifecycle_state",
            "taxonomy", "setting_scope", "biology_descriptor",
            "morphology_profile_ref", "scale_profile_ref", "choice_schema_ref",
            "sense_grants", "movement_grants", "adaptation_grants",
            "capability_grants", "compatibility_profile_ref", "lineage_refs",
            "form_refs", "progression_refs", "lore_culture_links",
            "presentation_assets", "validation_profile_ref", "extension_data"
        } <= required)

        self.assertIn("valid_playable", species["lifecycle_states"])
        self.assertIn("migration_required", species["lifecycle_states"])
        self.assertIn("retired", species["lifecycle_states"])
        self.assertNotIn("active", species["lifecycle_states"])

    def test_character_species_selection_is_receipt_not_species_copy(self) -> None:
        selection = self._json(SELECTION)
        self.assertEqual(selection["contract_id"], "MVPS.CharacterSpeciesSelection")
        self.assertEqual(selection["record_type"], "CharacterSpeciesSelection")
        self.assertEqual(selection["storage_policy"], "references_and_receipts_not_definition_copy")
        self.assertTrue(selection["species_ref"]["exact_version_required"])
        self.assertTrue(selection["grant_receipts"]["source_and_reason_required"])

        forbidden = set(selection["forbidden_definition_copy_fields"])
        self.assertTrue({
            "taxonomy", "biology_descriptor", "morphology_profile_ref",
            "scale_profile_ref", "sense_grants", "movement_grants",
            "capability_grants"
        } <= forbidden)

    def test_invariant_manifest_covers_mvps01_acceptance(self) -> None:
        manifest = self._json(INVARIANTS)
        by_id = {row["id"]: row for row in manifest["invariants"]}
        for invariant_id in {
            "MVPS01-I01", "MVPS01-I02", "MVPS01-I03", "MVPS01-I04",
            "MVPS01-I05", "MVPS01-I06", "MVPS01-I07", "MVPS01-I08",
            "MVPS01-I09", "MVPS01-I10", "MVPS01-I11", "MVPS01-I12"
        }:
            self.assertIn(invariant_id, by_id)

        self.assertEqual(by_id["MVPS01-I03"]["rule"], "executable_mechanics_are_shared_record_references")
        self.assertEqual(by_id["MVPS01-I05"]["rule"], "descriptive_biology_is_non_executable")
        self.assertEqual(by_id["MVPS01-I10"]["rule"], "no_species_specific_runtime_engine")

    def test_fixture_demonstrates_definition_selection_and_receipt_separation(self) -> None:
        fixtures = self._json(FIXTURES)
        species = fixtures["valid_species_definition"]
        selection = fixtures["valid_character_species_selection"]

        self.assertEqual(selection["species_ref"]["species_id"], species["identity"]["species_id"])
        self.assertEqual(selection["species_ref"]["record_version"], species["versioning"]["record_version"])

        for copied_field in self._json(SELECTION)["forbidden_definition_copy_fields"]:
            self.assertNotIn(copied_field, selection)

        grant_refs = {g["record_ref"] for g in species["capability_grants"]}
        receipt_refs = {g["record_ref"] for g in selection["grant_receipts"]["items"]}
        self.assertTrue(receipt_refs <= grant_refs)

        self.assertNotIn("mechanics", species["biology_descriptor"])
        self.assertNotIn("formula", species["biology_descriptor"])


if __name__ == "__main__":
    unittest.main()
