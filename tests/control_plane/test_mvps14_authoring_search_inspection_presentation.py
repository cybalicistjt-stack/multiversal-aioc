from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/player-species/contracts"
AUTHORING = D / "MVPS-14_AUTHORING_CONTRACT.json"
SEARCH = D / "MVPS-14_SEARCH_INSPECTION_CONTRACT.json"
PRESENTATION = D / "MVPS-14_PRESENTATION_PROJECTION_CONTRACT.json"
FIXTURES = D / "MVPS-14_AUTHORING_SEARCH_PRESENTATION_FIXTURES.json"
INVARIANTS = D / "MVPS-14_INVARIANTS.json"


class MVPS14AuthoringSearchInspectionPresentationTests(unittest.TestCase):
    def _j(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_artifacts_exist(self):
        for path in (AUTHORING, SEARCH, PRESENTATION, FIXTURES, INVARIANTS):
            with self.subTest(path=path):
                self.assertTrue(path.is_file(), path)

    def test_authoring_composes_intent_but_does_not_own_canonical_write(self):
        c = self._j(AUTHORING)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesAuthoring")
        self.assertTrue(c["authority"]["authoring_decision_required"])
        self.assertTrue(c["draft_workflow"]["validation_preview_required_before_submit"])
        self.assertFalse(c["authority"]["canonical_write_executed_by_mvps14"])
        self.assertFalse(c["authority"]["publication_performed_by_mvps14"])
        self.assertFalse(c["authority"]["permission_escalation_allowed"])
        self.assertEqual(c["shared_owner_handoff"]["visibility_projection"], "AuthoringProjectionPort")

    def test_search_and_inspection_filter_before_derived_outputs(self):
        c = self._j(SEARCH)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesSearchInspection")
        p = c["permission_filtering"]
        self.assertTrue(p["filter_before_search"])
        self.assertTrue(p["filter_before_count"])
        self.assertTrue(p["filter_before_autocomplete"])
        self.assertTrue(p["filter_before_preview"])
        self.assertTrue(p["filter_before_ai_context"])
        self.assertFalse(p["hidden_cardinality_included"])
        fields = set(c["inspection_projection"]["required_fields"])
        self.assertTrue({
            "species_id", "record_version", "lifecycle_state", "validation_state",
            "provenance_refs", "source_refs", "cross_links"
        } <= fields)
        self.assertTrue(c["inspection_projection"]["migration_state_inspectable"])
        self.assertTrue(c["inspection_projection"]["missing_or_conflicted_provenance_explicit"])

    def test_presentation_is_projection_not_rules_authority(self):
        c = self._j(PRESENTATION)
        self.assertEqual(c["contract_id"], "MVPS.SpeciesPresentationProjection")
        self.assertEqual(c["runtime_source"], "MVPS.SpeciesRuntimeProjection")
        self.assertFalse(c["rules_authority"]["ui_executes_species_rules"])
        self.assertFalse(c["rules_authority"]["presentation_mutates_runtime_projection"])
        self.assertFalse(c["rules_authority"]["hidden_canon_inferred"])
        self.assertTrue(c["mechanical_separation"]["presentation_assets_non_executable"])
        self.assertTrue(c["mechanical_separation"]["labels_layout_visualization_non_authoritative"])
        self.assertTrue({"character_builder", "gm_inspector", "species_reference"} <= set(c["surface_kinds"]))

    def test_builder_and_gm_views_keep_provenance_validation_and_receipts_inspectable(self):
        c = self._j(PRESENTATION)
        fields = set(c["projection_fields"])
        self.assertTrue({
            "species_identity", "exact_version_ref", "validation_state",
            "provenance_refs", "grant_receipt_refs", "runtime_contribution_refs"
        } <= fields)
        self.assertTrue(c["gm_inspection"]["can_show_source_trace_when_authorized"])
        self.assertTrue(c["builder_projection"]["unresolved_choices_remain_visible"])
        self.assertTrue(c["builder_projection"]["migration_required_not_presented_as_playable"])

    def test_fixtures_cover_hidden_search_authoring_and_runtime_projection_boundaries(self):
        cases = self._j(FIXTURES)["cases"]
        required = {
            "hidden_species_search",
            "inspect_provenance_validation",
            "authoring_draft_no_publish",
            "builder_runtime_projection",
            "gm_inspector_source_trace",
            "presentation_asset_nonmechanical",
        }
        self.assertTrue(required <= set(cases))
        self.assertEqual(cases["hidden_species_search"]["expected"]["hidden_result_count"], 0)
        self.assertFalse(cases["hidden_species_search"]["expected"]["hidden_cardinality_included"])
        self.assertFalse(cases["authoring_draft_no_publish"]["expected"]["canonical_write_performed"])
        self.assertFalse(cases["authoring_draft_no_publish"]["expected"]["publication_performed"])
        self.assertTrue(cases["builder_runtime_projection"]["expected"]["runtime_projection_read_only"])
        self.assertTrue(cases["gm_inspector_source_trace"]["expected"]["provenance_visible_when_authorized"])
        self.assertFalse(cases["presentation_asset_nonmechanical"]["expected"]["mechanics_changed"])

    def test_invariants_lock_mvps14_scope(self):
        ids = {x["id"] for x in self._j(INVARIANTS)["invariants"]}
        self.assertTrue({
            "MVPS14-I01-ui-is-projection",
            "MVPS14-I02-authoring-no-direct-canonical-write",
            "MVPS14-I03-permission-filter-before-derived-output",
            "MVPS14-I04-provenance-validation-inspectable",
            "MVPS14-I05-presentation-mechanically-separate",
            "MVPS14-I06-runtime-projection-read-only",
            "MVPS14-I07-hidden-canon-not-inferred",
            "MVPS14-I08-stable-versioned-cross-links",
        } <= ids)


if __name__ == "__main__":
    unittest.main()
