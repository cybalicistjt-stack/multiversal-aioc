from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_DIR = ROOT / "governance/application-planning/player-species/contracts"
MORPH = CONTRACT_DIR / "MVPS-03_MORPHOLOGY_PROFILE_CONTRACT.json"
QUERY = CONTRACT_DIR / "MVPS-03_BODY_STRUCTURE_QUERY_CONTRACT.json"
FIXTURES = CONTRACT_DIR / "MVPS-03_MORPHOLOGY_FIXTURES.json"


class MVPS03MorphologyBodyPlanTests(unittest.TestCase):
    def _json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_contract_artifacts_exist(self) -> None:
        for path in (MORPH, QUERY, FIXTURES):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_morphology_profile_is_size_independent_and_species_agnostic(self) -> None:
        morph = self._json(MORPH)
        self.assertEqual(morph["contract_id"], "MVPS.MorphologyProfile")
        self.assertEqual(morph["record_type"], "MorphologyProfile")
        self.assertEqual(morph["scale_policy"], "external_reference_only")
        self.assertFalse(morph["species_name_branching_allowed"])
        required = set(morph["required_top_level_fields"])
        self.assertTrue({
            "morphology_id", "body_regions", "limbs", "manipulators",
            "worn_regions", "attachment_points", "natural_appendages",
            "structural_relations", "query_tags"
        } <= required)
        self.assertEqual(morph["body_region_contract"]["inline_scale"], False)
        self.assertEqual(morph["limb_contract"]["inline_scale"], False)

    def test_query_contract_exposes_structure_without_equipment_policy(self) -> None:
        query = self._json(QUERY)
        self.assertEqual(query["contract_id"], "MVPS.BodyStructureQuery")
        self.assertFalse(query["species_name_input_allowed"])
        self.assertFalse(query["owns_equipment_compatibility_policy"])
        ops = set(query["operations"])
        self.assertTrue({
            "list_regions", "list_limbs", "list_manipulators",
            "list_worn_regions", "list_attachment_points",
            "list_natural_appendages", "match_structural_requirements"
        } <= ops)
        self.assertTrue(query["match_result_contract"]["reason_required"])

    def test_humanoid_and_nonhumanoid_fixtures_share_one_interface(self) -> None:
        fixtures = self._json(FIXTURES)
        humanoid = fixtures["humanoid_fixture"]
        nonhumanoid = fixtures["nonhumanoid_fixture"]
        fields = set(self._json(MORPH)["required_top_level_fields"])
        self.assertTrue(fields <= set(humanoid))
        self.assertTrue(fields <= set(nonhumanoid))
        self.assertNotEqual(humanoid["body_plan_family"], nonhumanoid["body_plan_family"])
        self.assertNotIn("species_name", humanoid)
        self.assertNotIn("species_name", nonhumanoid)

        query_examples = fixtures["query_examples"]
        self.assertTrue(query_examples["humanoid_two_hand_requirement"]["matched"])
        self.assertFalse(query_examples["nonhumanoid_two_hand_requirement"]["matched"])
        self.assertTrue(query_examples["nonhumanoid_two_hand_requirement"]["reason"])

    def test_structural_contract_does_not_smuggle_later_mvps_ownership(self) -> None:
        morph = self._json(MORPH)
        forbidden = {
            "movement_speed", "sense_range", "equipment_fit_formula",
            "transformation_rules", "species_progression", "environment_tolerance"
        }
        self.assertTrue(forbidden.isdisjoint(morph.keys()))


if __name__ == "__main__":
    unittest.main()
