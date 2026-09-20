from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/player-species/contracts"
MATRIX = D / "MVPS-16_COMMON_CONFORMANCE_MATRIX.json"
FIXTURES = D / "MVPS-16_RADICAL_SPECIES_FIXTURES.json"
PROOF = D / "MVPS-16_GOLDEN_PROOF.json"
INVARIANTS = D / "MVPS-16_INVARIANTS.json"

EXPECTED_FIXTURES = {
    "ordinary_human",
    "winged_humanoid",
    "aquatic_non_humanoid",
    "centaur_like_quadruped",
    "construct_android",
    "multi_form_shapeshifter",
    "incorporeal_being",
    "radically_alien_body_plan",
}

EXPECTED_WORKFLOWS = {
    "creation_selection",
    "validation",
    "runtime_projection",
    "equipment_compatibility",
    "environment_interaction",
    "progression",
    "transformation",
    "serialization_import_export",
    "migration",
    "authoring_inspection_presentation",
    "npc_creature_reuse",
}

MANDATORY_PASS = EXPECTED_WORKFLOWS - {"progression", "transformation"}


class MVPS16RadicalSpeciesGoldenProofTests(unittest.TestCase):
    def _j(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_golden_artifacts_exist(self):
        for path in (MATRIX, FIXTURES, PROOF, INVARIANTS):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_common_matrix_points_to_real_owner_contracts(self):
        matrix = self._j(MATRIX)
        self.assertEqual(matrix["contract_id"], "MVPS.RadicalSpeciesConformance")
        self.assertEqual(set(matrix["workflows"]), EXPECTED_WORKFLOWS)
        self.assertEqual(matrix["dispatch_policy"]["core_dispatch"], "typed_contracts_only")
        self.assertFalse(matrix["dispatch_policy"]["species_name_conditionals_allowed"])

        for workflow_id, row in matrix["workflows"].items():
            with self.subTest(workflow=workflow_id):
                source = D / row["contract_file"]
                self.assertTrue(source.is_file(), source)
                contract = self._j(source)
                self.assertEqual(contract["contract_id"], row["contract_id"])
                self.assertFalse(row["mvps16_becomes_owner"])

    def test_exactly_eight_radically_different_fixtures_use_the_same_workflow_shape(self):
        data = self._j(FIXTURES)
        self.assertTrue(data["non_canon"])
        cases = data["fixtures"]
        self.assertEqual(set(cases), EXPECTED_FIXTURES)
        self.assertEqual(len(cases), 8)

        expected_keys = None
        for fixture_id, fixture in cases.items():
            with self.subTest(fixture=fixture_id):
                keys = set(fixture["workflow_results"])
                if expected_keys is None:
                    expected_keys = keys
                self.assertEqual(keys, expected_keys)
                self.assertEqual(keys, EXPECTED_WORKFLOWS)
                self.assertFalse(fixture["dispatch"]["species_name_conditional_used"])
                self.assertEqual(fixture["dispatch"]["method"], "typed_contract_data")
                self.assertTrue(fixture["exact_version_species_ref"])
                self.assertTrue(fixture["provenance_refs"])
                self.assertTrue(fixture["morphology_ref"])

    def test_common_workflows_pass_or_explicitly_mark_optional_not_applicable(self):
        cases = self._j(FIXTURES)["fixtures"]
        for fixture_id, fixture in cases.items():
            results = fixture["workflow_results"]
            for workflow_id in MANDATORY_PASS:
                with self.subTest(fixture=fixture_id, workflow=workflow_id):
                    self.assertEqual(results[workflow_id]["status"], "pass")
                    self.assertTrue(results[workflow_id]["evidence_refs"])
            for workflow_id in {"progression", "transformation"}:
                with self.subTest(fixture=fixture_id, workflow=workflow_id):
                    self.assertIn(results[workflow_id]["status"], {"pass", "not_applicable"})
                    if results[workflow_id]["status"] == "not_applicable":
                        self.assertTrue(results[workflow_id]["reason"])

    def test_equipment_proof_includes_explicit_rejection_not_species_branching(self):
        cases = self._j(FIXTURES)["fixtures"]
        incorporeal = cases["incorporeal_being"]["workflow_results"]["equipment_compatibility"]
        self.assertEqual(incorporeal["status"], "pass")
        self.assertEqual(incorporeal["outcome"], "explicitly_incompatible")
        self.assertEqual(incorporeal["decision_basis"], "MVPS.SpeciesInterfaceCompatibility")
        self.assertFalse(incorporeal["species_name_branch_used"])

        alien = cases["radically_alien_body_plan"]["workflow_results"]["equipment_compatibility"]
        self.assertEqual(alien["status"], "pass")
        self.assertEqual(alien["decision_basis"], "MVPS.SpeciesInterfaceCompatibility")
        self.assertFalse(alien["species_name_branch_used"])

    def test_fixture_differences_are_expressed_as_typed_data(self):
        cases = self._j(FIXTURES)["fixtures"]
        self.assertIn("flight", cases["winged_humanoid"]["capability_tags"])
        self.assertIn("aquatic", cases["aquatic_non_humanoid"]["capability_tags"])
        self.assertEqual(cases["centaur_like_quadruped"]["body_plan"]["locomotor_limb_count"], 4)
        self.assertEqual(cases["construct_android"]["physiology_mode"], "synthetic")
        self.assertGreater(len(cases["multi_form_shapeshifter"]["form_refs"]), 1)
        self.assertIn("incorporeal", cases["incorporeal_being"]["capability_tags"])
        self.assertEqual(cases["radically_alien_body_plan"]["body_plan"]["symmetry"], "hexaradial")
        self.assertEqual(cases["ordinary_human"]["body_plan"]["family"], "bipedal_humanoid")

    def test_golden_proof_records_full_matrix_without_semantic_gaps(self):
        proof = self._j(PROOF)
        self.assertEqual(proof["proof_id"], "MVPS-16.RadicalSpeciesGoldenProof")
        self.assertEqual(proof["status"], "completed_green")
        self.assertEqual(proof["fixture_count"], 8)
        self.assertEqual(proof["workflow_count"], len(EXPECTED_WORKFLOWS))
        self.assertEqual(set(proof["fixture_ids"]), EXPECTED_FIXTURES)
        self.assertEqual(set(proof["workflow_ids"]), EXPECTED_WORKFLOWS)
        self.assertEqual(proof["semantic_gaps_remaining"], [])
        self.assertEqual(proof["species_name_conditionals_required"], 0)
        self.assertTrue(proof["owner_authority_preserved"])
        self.assertTrue(proof["same_common_contract_for_all_fixtures"])

    def test_invariants_lock_terminal_mvps_scope(self):
        ids = {x["id"] for x in self._j(INVARIANTS)["invariants"]}
        self.assertTrue({
            "MVPS16-I01-eight-required-fixtures",
            "MVPS16-I02-common-contract-shape",
            "MVPS16-I03-no-species-name-dispatch",
            "MVPS16-I04-equipment-explicit-fit-or-rejection",
            "MVPS16-I05-optional-progression-transform-explicit",
            "MVPS16-I06-full-lifecycle-proof",
            "MVPS16-I07-owner-authority-preserved",
            "MVPS16-I08-no-unresolved-semantic-gaps",
        } <= ids)


if __name__ == "__main__":
    unittest.main()
