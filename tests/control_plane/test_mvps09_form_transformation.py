from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/player-species/contracts"
FORM = D / "MVPS-09_FORM_DEFINITION_CONTRACT.json"
TRANSFORM = D / "MVPS-09_TRANSFORMATION_SEMANTICS_CONTRACT.json"
FIXTURES = D / "MVPS-09_TRANSFORMATION_FIXTURES.json"
INVARIANTS = D / "MVPS-09_INVARIANTS.json"


class MVPS09FormTransformationTests(unittest.TestCase):
    def _j(self, p: Path) -> dict:
        return json.loads(p.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self):
        for p in (FORM, TRANSFORM, FIXTURES, INVARIANTS):
            with self.subTest(path=p):
                self.assertTrue(p.is_file(), p)

    def test_form_identity_is_distinct_and_reference_based(self):
        c = self._j(FORM)
        self.assertEqual(c["contract_id"], "MVPS.FormDefinition")
        self.assertTrue(c["identity_policy"]["form_identity_distinct_from_species"])
        self.assertFalse(c["identity_policy"]["form_replaces_base_species_identity"])
        self.assertFalse(c["inline_shared_mechanics_allowed"])
        self.assertTrue({"morphology_profile_ref","scale_profile_ref","movement_grants","sense_grants","capability_grants","resource_refs","compatibility_profile_ref","presentation_ref"} <= set(c["reference_surfaces"]))

    def test_transformation_contract_is_explicit_and_reversible(self):
        c = self._j(TRANSFORM)
        self.assertEqual(c["contract_id"], "MVPS.TransformationSemantics")
        required=set(c["transformation_record"]["required"])
        self.assertTrue({"transformation_id","source_form_ref","target_form_ref","entry_trigger_ref","retention_policy","equipment_policy_ref","exit_policy","visibility","provenance"} <= required)
        self.assertTrue(c["base_selection_history_preserved"])
        self.assertTrue(c["reversal"]["provenance_safe"])
        self.assertFalse(c["runtime_projection_created"])
        self.assertEqual(c["runtime_projection_owner"], "MVPS-13")

    def test_equipment_policy_is_explicit_without_mutation_ownership(self):
        c = self._j(TRANSFORM)
        p=c["equipment_handling"]
        self.assertEqual(set(p["policy_kinds"]), {"retain","drop","suppress","resize","replace","adapt","owner_defined"})
        self.assertFalse(p["inventory_mutation_owned_by_mvps09"])
        self.assertFalse(p["equipment_assignment_mutation_owned_by_mvps09"])
        self.assertEqual(p["mutation_owner"], "PPIA-03 / Item-Equipment owner workflow")

    def test_resource_and_shared_mechanics_defer_to_owners(self):
        c = self._j(TRANSFORM)
        self.assertFalse(c["resource_handling"]["resource_engine_created"])
        self.assertEqual(c["resource_handling"]["policy"], "reference_and_handoff_only")
        self.assertEqual(c["unknown_or_conflict_policy"], "surface_unresolved_not_guess")

    def test_fixtures_prove_retention_equipment_reversal_and_history(self):
        f=self._j(FIXTURES)["cases"]
        self.assertTrue({"temporary_form_round_trip","equipment_suppression","equipment_adaptation","resource_owner_handoff","unresolved_missing_exit"} <= set(f))
        self.assertTrue(f["temporary_form_round_trip"]["expected"]["base_selection_history_preserved"])
        self.assertTrue(f["temporary_form_round_trip"]["expected"]["reversal_provenance_preserved"])
        self.assertEqual(f["equipment_suppression"]["expected"]["equipment_policy"], "suppress")
        self.assertEqual(f["equipment_adaptation"]["expected"]["equipment_policy"], "adapt")
        self.assertEqual(f["resource_owner_handoff"]["expected"]["status"], "owner_deferred")
        self.assertEqual(f["unresolved_missing_exit"]["expected"]["status"], "unresolved")

    def test_invariants_cover_acceptance_and_boundaries(self):
        ids={x["id"] for x in self._j(INVARIANTS)["invariants"]}
        self.assertTrue({
            "MVPS09-I01-form-not-species",
            "MVPS09-I02-base-history-preserved",
            "MVPS09-I03-explicit-retention",
            "MVPS09-I04-explicit-equipment-policy",
            "MVPS09-I05-provenance-safe-reversal",
            "MVPS09-I06-shared-owner-delegation",
            "MVPS09-I07-no-progression-or-runtime-projection-leakage"
        } <= ids)


if __name__ == "__main__":
    unittest.main()
