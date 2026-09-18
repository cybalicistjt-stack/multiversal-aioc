from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/player-species/contracts"
LINEAGE = D / "MVPS-08_LINEAGE_DEFINITION_CONTRACT.json"
COMPOSE = D / "MVPS-08_LINEAGE_COMPOSITION_CONTRACT.json"
FIXTURES = D / "MVPS-08_LINEAGE_COMPOSITION_FIXTURES.json"
INVARIANTS = D / "MVPS-08_INVARIANTS.json"


class MVPS08LineageCompositionTests(unittest.TestCase):
    def _j(self, p: Path) -> dict:
        return json.loads(p.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self):
        for p in (LINEAGE, COMPOSE, FIXTURES, INVARIANTS):
            with self.subTest(path=p):
                self.assertTrue(p.is_file(), p)

    def test_lineage_references_exact_parent_without_copying_it(self):
        c = self._j(LINEAGE)
        self.assertEqual(c["contract_id"], "MVPS.LineageDefinition")
        self.assertFalse(c["full_parent_definition_copy_allowed"])
        self.assertTrue(c["parent_species_ref"]["exact_version_required"])
        self.assertEqual(set(c["parent_species_ref"]["required"]), {"species_id", "record_version"})
        self.assertTrue(c["relationship_evidence"]["source_backed_required"])
        self.assertFalse(c["relationship_evidence"]["same_name_or_visual_similarity_sufficient"])
        self.assertTrue({"lineage_id", "lineage_version", "parent_species_ref", "relationship_evidence_refs", "delta_operations", "provenance"} <= set(c["required_top_level_fields"]))

    def test_deltas_are_typed_reference_level_operations(self):
        c = self._j(LINEAGE)
        kinds = set(c["delta_operation_kinds"])
        self.assertTrue({"add_reference", "exclude_reference", "remove_reference", "replace_reference", "override_descriptive_value"} <= kinds)
        required = set(c["delta_operation_contract"]["required"])
        self.assertTrue({"operation_id", "operation_kind", "target_path", "source_ref", "provenance_ref", "order"} <= required)
        self.assertFalse(c["delta_operation_contract"]["inline_shared_mechanics_allowed"])
        self.assertFalse(c["delta_operation_contract"]["runtime_state_mutation_allowed"])

    def test_composition_is_deterministic_but_order_does_not_guess_conflicts(self):
        c = self._j(COMPOSE)
        self.assertEqual(c["contract_id"], "MVPS.LineageComposition")
        self.assertTrue(c["deterministic_replay"])
        self.assertEqual(c["stable_order"], ["base_species", "lineage.layer_order", "lineage.lineage_id", "lineage.lineage_version", "operation.order", "operation.operation_id"])
        self.assertFalse(c["semantic_conflict_resolution_by_order_allowed"])
        self.assertEqual(c["unknown_or_conflict_policy"], "surface_unresolved_not_guess")
        self.assertTrue({"unresolved", "resolved_by_explicit_rule"} <= set(c["conflict_statuses"]))

    def test_duplicate_and_stacking_semantics_remain_shared_owner(self):
        c = self._j(COMPOSE)
        self.assertEqual(c["duplicate_grant_policy"], "defer_to_shared_owner_stacking_and_duplicate_rules")
        self.assertFalse(c["lineage_local_stacking_engine_created"])
        self.assertFalse(c["runtime_projection_created"])
        self.assertEqual(c["runtime_projection_owner"], "MVPS-13")

    def test_fixtures_prove_add_replace_shared_owner_and_conflict_paths(self):
        f = self._j(FIXTURES)
        cases = f["cases"]
        self.assertTrue({"reference_addition", "explicit_replacement", "duplicate_shared_owner", "conflict_same_target", "parent_version_mismatch"} <= set(cases))
        self.assertEqual(cases["reference_addition"]["expected"]["status"], "composed")
        self.assertEqual(cases["explicit_replacement"]["expected"]["status"], "composed")
        self.assertEqual(cases["duplicate_shared_owner"]["expected"]["status"], "owner_deferred")
        self.assertEqual(cases["conflict_same_target"]["expected"]["status"], "unresolved")
        self.assertEqual(cases["parent_version_mismatch"]["expected"]["status"], "unresolved")
        for case in cases.values():
            self.assertNotIn("copied_parent_definition", case)
            self.assertFalse(case["runtime_mutation"])

    def test_invariants_cover_core_acceptance(self):
        i = self._j(INVARIANTS)
        ids = {x["id"] for x in i["invariants"]}
        self.assertTrue({
            "MVPS08-I01-parent-reference-not-copy",
            "MVPS08-I02-source-backed-lineage-relationship",
            "MVPS08-I03-deterministic-replay",
            "MVPS08-I04-order-does-not-resolve-semantic-conflict",
            "MVPS08-I05-conflicts-remain-explicit",
            "MVPS08-I06-shared-owner-stacking",
            "MVPS08-I07-base-species-identity-preserved",
            "MVPS08-I08-no-form-or-runtime-projection-leakage"
        } <= ids)
        self.assertFalse(i["lineage_specific_runtime_engine_created"])


if __name__ == "__main__":
    unittest.main()
