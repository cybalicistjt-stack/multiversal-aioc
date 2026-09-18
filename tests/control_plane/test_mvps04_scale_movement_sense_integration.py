from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_DIR = ROOT / "governance/application-planning/player-species/contracts"
INTEGRATION = CONTRACT_DIR / "MVPS-04_SCALE_MOVEMENT_SENSE_INTEGRATION.json"
FIXTURES = CONTRACT_DIR / "MVPS-04_SCALE_MOVEMENT_SENSE_FIXTURES.json"
INVARIANTS = CONTRACT_DIR / "MVPS-04_INVARIANTS.json"


class MVPS04ScaleMovementSenseIntegrationTests(unittest.TestCase):
    def _json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self) -> None:
        for path in (INTEGRATION, FIXTURES, INVARIANTS):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_integration_contract_references_shared_owners(self) -> None:
        contract = self._json(INTEGRATION)
        self.assertEqual(contract["contract_id"], "MVPS.SpeciesScaleMovementSenseIntegration")
        self.assertEqual(contract["scale"]["policy"], "external_profile_reference")
        self.assertEqual(contract["movement"]["grant_policy"], "typed_shared_record_reference")
        self.assertEqual(contract["senses"]["grant_policy"], "typed_shared_record_reference")
        self.assertEqual(contract["derived_values"]["policy"], "registered_rules_profile_reference_only")
        self.assertFalse(contract["movement"]["species_formula_allowed"])
        self.assertFalse(contract["senses"]["species_formula_allowed"])
        self.assertFalse(contract["duplicate_engine_policy"]["movement_engine_allowed"])
        self.assertFalse(contract["duplicate_engine_policy"]["sense_engine_allowed"])

    def test_typed_movement_and_sense_grants_have_source_and_rules_refs(self) -> None:
        contract = self._json(INTEGRATION)
        movement_required = set(contract["movement"]["grant_contract"]["required"])
        sense_required = set(contract["senses"]["grant_contract"]["required"])
        self.assertTrue({"record_ref", "grant_type", "source_ref", "rules_profile_ref"} <= movement_required)
        self.assertTrue({"record_ref", "grant_type", "source_ref", "rules_profile_ref"} <= sense_required)
        self.assertIn("locomotion_mode", contract["movement"]["grant_types"])
        self.assertIn("sense_mode", contract["senses"]["grant_types"])

    def test_fixture_uses_refs_not_inline_mechanics(self) -> None:
        fixtures = self._json(FIXTURES)
        winged = fixtures["winged_fixture"]
        aquatic = fixtures["aquatic_fixture"]
        for fixture in (winged, aquatic):
            self.assertTrue(fixture["scale_profile_ref"])
            self.assertTrue(fixture["movement_grants"])
            self.assertTrue(fixture["sense_grants"])
            self.assertTrue(fixture["derived_value_rule_refs"])
            self.assertNotIn("movement_speed_formula", fixture)
            self.assertNotIn("vision_range_formula", fixture)
            for grant in fixture["movement_grants"] + fixture["sense_grants"]:
                self.assertTrue(grant["record_ref"])
                self.assertTrue(grant["rules_profile_ref"])
                self.assertTrue(grant["source_ref"])

    def test_invariants_forbid_duplicate_engines_and_inline_derived_rules(self) -> None:
        invariants = self._json(INVARIANTS)
        ids = {item["id"] for item in invariants["invariants"]}
        self.assertTrue({
            "MVPS04-I01-scale-is-profile-reference",
            "MVPS04-I02-movement-is-typed-shared-grant",
            "MVPS04-I03-senses-are-typed-shared-grants",
            "MVPS04-I04-derived-values-use-registered-rules",
            "MVPS04-I05-no-duplicate-movement-or-sense-engine"
        } <= ids)
        self.assertFalse(invariants["runtime_engine_created"])


if __name__ == "__main__":
    unittest.main()
