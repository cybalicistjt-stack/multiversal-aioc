from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_DIR = ROOT / "governance/application-planning/player-species/contracts"
GRANT = CONTRACT_DIR / "MVPS-06_CAPABILITY_GRANT_CONTRACT.json"
NATURAL = CONTRACT_DIR / "MVPS-06_NATURAL_EQUIPMENT_CONTRACT.json"
FIX = CONTRACT_DIR / "MVPS-06_CAPABILITY_NATURAL_EQUIPMENT_FIXTURES.json"
INV = CONTRACT_DIR / "MVPS-06_INVARIANTS.json"


class MVPS06CapabilityNaturalEquipmentTests(unittest.TestCase):
    def _json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self) -> None:
        for path in (GRANT, NATURAL, FIX, INV):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_capability_grants_are_typed_shared_owner_references(self) -> None:
        contract = self._json(GRANT)
        self.assertEqual(contract["contract_id"], "MVPS.SpeciesCapabilityGrant")
        self.assertEqual(contract["execution_policy"], "shared_owner_reference_only")
        self.assertFalse(contract["inline_mechanics_allowed"])
        self.assertFalse(contract["species_specific_execution_engine_created"])

        kinds = set(contract["capability_kinds"])
        self.assertTrue({
            "ability", "action", "reaction", "resource", "resistance",
            "immunity", "proficiency", "modifier", "effect"
        } <= kinds)

        required = set(contract["grant_declaration_contract"]["required"])
        self.assertTrue({
            "grant_id", "record_ref", "owner_domain", "capability_kind",
            "grant_class", "source_ref", "provenance_ref"
        } <= required)

    def test_biology_or_species_labels_do_not_infer_mechanics(self) -> None:
        contract = self._json(GRANT)
        evidence = contract["biological_binding_evidence"]
        self.assertFalse(evidence["species_prerequisite_is_sufficient"])
        self.assertFalse(evidence["species_perk_label_is_sufficient"])
        self.assertFalse(evidence["innate_label_is_sufficient"])
        self.assertFalse(evidence["biological_looking_name_is_sufficient"])
        self.assertEqual(contract["missing_mechanics_policy"], "unresolved_not_inferred")

    def test_natural_equipment_routes_to_shared_owners_without_inventory_duplication(self) -> None:
        contract = self._json(NATURAL)
        self.assertEqual(contract["contract_id"], "MVPS.SpeciesNaturalEquipmentGrant")
        self.assertFalse(contract["inline_item_or_ability_mechanics_allowed"])
        self.assertFalse(contract["intrinsic_structure_defaults_to_asset_instance"])
        self.assertFalse(contract["intrinsic_structure_defaults_to_inventory_ownership"])

        kinds = set(contract["natural_equipment_kinds"])
        self.assertTrue({"natural_weapon", "natural_armor", "organ"} <= kinds)

        required = set(contract["natural_equipment_declaration"]["required"])
        self.assertTrue({
            "natural_equipment_id", "kind", "body_structure_ref",
            "source_ref", "provenance_ref", "mechanic_refs"
        } <= required)

        owners = set(contract["mechanic_ref_owner_domains"])
        self.assertTrue({
            "Ability", "Action", "Effect", "Condition", "Resource",
            "Modifier", "ItemDefinition", "Equipment"
        } <= owners)

    def test_fixtures_prove_explicit_grant_and_non_grant_paths(self) -> None:
        fixtures = self._json(FIX)
        claw = fixtures["morphology_only_claw_fixture"]
        stinger = fixtures["explicit_stinger_weapon_fixture"]
        armor = fixtures["explicit_natural_armor_fixture"]
        organ = fixtures["explicit_organ_resource_fixture"]

        self.assertEqual(claw["executable_grants"], [])
        self.assertEqual(claw["natural_equipment_grants"], [])
        self.assertTrue(claw["morphology_fact_ref"])

        self.assertTrue(stinger["natural_equipment_grants"])
        self.assertTrue(armor["natural_equipment_grants"])
        self.assertTrue(organ["natural_equipment_grants"])

        for fixture in (stinger, armor, organ):
            self.assertNotIn("species_name", fixture)
            self.assertFalse(fixture["creates_asset_instance"])
            self.assertFalse(fixture["creates_inventory_ownership"])
            for grant in fixture["natural_equipment_grants"]:
                self.assertTrue(grant["body_structure_ref"])
                self.assertTrue(grant["source_ref"])
                self.assertTrue(grant["provenance_ref"])
                self.assertTrue(grant["mechanic_refs"])

    def test_invariants_cover_identity_provenance_and_owner_boundaries(self) -> None:
        invariants = self._json(INV)
        ids = {item["id"] for item in invariants["invariants"]}
        self.assertTrue({
            "MVPS06-I01-every-executable-grant-has-canonical-identity",
            "MVPS06-I02-every-grant-has-provenance",
            "MVPS06-I03-no-inline-shared-mechanics",
            "MVPS06-I04-biological-labels-do-not-create-mechanics",
            "MVPS06-I05-natural-equipment-routes-through-shared-owners",
            "MVPS06-I06-intrinsic-body-structures-do-not-create-owned-assets",
            "MVPS06-I07-missing-mechanics-remain-unresolved"
        } <= ids)
        self.assertFalse(invariants["runtime_capability_engine_created"])
        self.assertFalse(invariants["runtime_inventory_engine_created"])


if __name__ == "__main__":
    unittest.main()
