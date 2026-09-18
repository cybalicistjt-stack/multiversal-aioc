from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT_DIR = ROOT / "governance/application-planning/player-species/contracts"
PHYS = CONTRACT_DIR / "MVPS-05_PHYSIOLOGY_LIFECYCLE_CONTRACT.json"
ENV = CONTRACT_DIR / "MVPS-05_ENVIRONMENT_TOLERANCE_CONTRACT.json"
FIX = CONTRACT_DIR / "MVPS-05_PHYSIOLOGY_ENVIRONMENT_FIXTURES.json"
INV = CONTRACT_DIR / "MVPS-05_INVARIANTS.json"


class MVPS05PhysiologyEnvironmentTests(unittest.TestCase):
    def _json(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self) -> None:
        for path in (PHYS, ENV, FIX, INV):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_descriptive_biology_is_non_executable(self) -> None:
        contract = self._json(PHYS)
        self.assertEqual(contract["contract_id"], "MVPS.SpeciesPhysiologyLifecycle")
        self.assertEqual(contract["biology_descriptor"]["execution_policy"], "non_executable")
        self.assertFalse(contract["biology_descriptor"]["may_infer_mechanics"])
        self.assertFalse(contract["biology_descriptor"]["may_create_conditions_or_resources"])
        self.assertEqual(contract["missing_mechanics_policy"], "unresolved_not_inferred")

    def test_executable_physiology_uses_typed_shared_refs(self) -> None:
        contract = self._json(PHYS)
        hooks = contract["physiology_hooks"]
        self.assertTrue({"respiration", "sustenance", "rest_recovery"} <= set(hooks["hook_types"]))
        required = set(hooks["hook_contract"]["required"])
        self.assertTrue({"record_ref", "hook_type", "source_ref", "rules_profile_ref"} <= required)
        self.assertFalse(hooks["inline_formula_allowed"])
        lifecycle = contract["lifecycle"]
        self.assertEqual(lifecycle["development_metadata_policy"], "descriptive_unless_rule_referenced")
        self.assertEqual(lifecycle["mechanical_transition_policy"], "shared_rule_or_effect_reference_only")

    def test_environment_tolerance_contract_is_capability_based(self) -> None:
        contract = self._json(ENV)
        self.assertEqual(contract["contract_id"], "MVPS.SpeciesEnvironmentTolerance")
        self.assertFalse(contract["species_name_branching_allowed"])
        self.assertEqual(contract["environment_evaluation_policy"], "environment_requires_capabilities_species_exposes_refs")
        self.assertTrue({
            "atmosphere", "pressure", "temperature", "gravity",
            "radiation", "water", "vacuum"
        } <= set(contract["environment_factor_types"]))
        required = set(contract["tolerance_grant_contract"]["required"])
        self.assertTrue({"record_ref", "factor_type", "source_ref", "rules_profile_ref"} <= required)
        self.assertFalse(contract["tolerance_grant_contract"]["inline_resolution_formula_allowed"])

    def test_fixtures_prove_prose_does_not_create_mechanics(self) -> None:
        fixtures = self._json(FIX)
        baseline = fixtures["baseline_biological_fixture"]
        aquatic = fixtures["aquatic_fixture"]
        construct = fixtures["construct_fixture"]

        self.assertTrue(baseline["biology_descriptor"]["summary"])
        self.assertEqual(baseline["biology_descriptor"]["mechanical_effect"], None)
        self.assertTrue(baseline["physiology_hooks"])
        self.assertTrue(aquatic["environment_tolerance_grants"])
        self.assertTrue(construct["environment_tolerance_grants"])
        self.assertEqual(construct["biology_descriptor"]["mechanical_effect"], None)

        for fixture in (baseline, aquatic, construct):
            self.assertNotIn("species_name", fixture)
            self.assertNotIn("survival_formula", fixture)
            self.assertNotIn("aging_formula", fixture)
            for grant in fixture["environment_tolerance_grants"]:
                self.assertTrue(grant["record_ref"])
                self.assertTrue(grant["source_ref"])
                self.assertTrue(grant["rules_profile_ref"])

    def test_invariants_cover_non_inference_and_shared_environment_resolution(self) -> None:
        invariants = self._json(INV)
        ids = {item["id"] for item in invariants["invariants"]}
        self.assertTrue({
            "MVPS05-I01-descriptive-biology-non-executable",
            "MVPS05-I02-physiology-hooks-use-shared-records",
            "MVPS05-I03-lifecycle-mechanics-use-shared-rules",
            "MVPS05-I04-environment-tolerances-are-typed-grants",
            "MVPS05-I05-environment-resolves-required-capabilities",
            "MVPS05-I06-missing-mechanics-are-not-inferred"
        } <= ids)
        self.assertFalse(invariants["runtime_environment_engine_created"])


if __name__ == "__main__":
    unittest.main()
