import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
MODEL = ENV_DIR / "ENV-16_CREATURE_DISCOVERY_PROJECTION_MODEL_v1.0.0.json"
CONTRACT = ENV_DIR / "ENV-16_ENVIRONMENT_CREATURE_DISCOVERY_CONTRACT.md"
EXAMPLES = ENV_DIR / "ENV-16_DISCOVERY_PROJECTION_EXAMPLES_v1.0.0.json"
REPORT = ENV_DIR / "ENV-16_COMPLETION_REPORT.md"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"
CEW_BACKLOG = ROOT / "governance/application-planning/creature-ecology-wildlife/CEW_PROGRAM_BACKLOG.json"


class Env16CreatureDiscoveryProjectionTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_contract_has_stable_identity_and_no_runtime_authority(self):
        model = self.load_json(MODEL)
        self.assertEqual(model["contract_id"], "ENV-CD-1.0")
        self.assertEqual(model["required_inputs"]["environment_context"]["habitat_signature_version"], "ENV-HS-1.0")
        self.assertTrue(model["projection_is_read_only"])
        self.assertFalse(model["projection_creates_canonical_creature_state"])
        self.assertFalse(model["projection_creates_canonical_distribution_state"])
        self.assertFalse(model["numeric_discovery_score_authorized"])
        self.assertFalse(model["hidden_priority_numbers_authorized"])
        self.assertFalse(model["application_implementation_authority"])
        self.assertFalse(model["runtime_schema_mutation_authorized"])

    def test_projection_facets_cover_required_gm_discovery_classes(self):
        facets = set(self.load_json(MODEL)["gm_projection_facets"])
        required = {
            "native_common",
            "possible_tolerated",
            "migratory_seasonal",
            "introduced_invasive",
            "rare_exceptional",
            "overlay_enabled",
            "canonical_presence_conflict",
            "excluded_or_blocked",
            "unresolved",
        }
        self.assertTrue(required.issubset(facets))

    def test_authority_gates_keep_distribution_visibility_and_ecology_separate(self):
        model = self.load_json(MODEL)
        boundary = model["authority_boundary"]
        self.assertEqual(boundary["environment_composition_and_habitat_signature_owner"], "ENV")
        self.assertEqual(boundary["creature_habitat_profile_owner"], "CEW")
        self.assertEqual(boundary["creature_distribution_owner"], "CEW")
        self.assertEqual(boundary["world_reality_setting_place_owner"], "existing World/Reality/Setting/Place authorities")
        self.assertEqual(boundary["campaign_placement_visibility_owner"], "existing Campaign/GM/visibility authorities")
        self.assertEqual(model["gate_order"], [
            "identity_and_authority_gate",
            "campaign_visibility_gate",
            "canonical_distribution_gate",
            "ecological_fit_gate",
            "overlay_condition_gate",
            "season_activity_gate",
            "projection_facet_derivation",
            "stable_grouping_and_trace",
        ])

    def test_distribution_absence_blocks_habitat_fit_and_unknown_fails_closed(self):
        gates = self.load_json(MODEL)["gate_rules"]
        dist = gates["canonical_distribution_gate"]
        self.assertIn("excluded", dist["explicitly_absent"])
        self.assertEqual(dist["not_established_or_unknown"], "unresolved_not_present_by_default")
        self.assertIn("Habitat fit cannot manufacture range", dist["rule"])

    def test_explicit_canonical_presence_is_preserved_on_ecological_conflict(self):
        eco = self.load_json(MODEL)["gate_rules"]["ecological_fit_gate"]
        self.assertIn("canonical_presence_conflict", eco["canonical_presence_conflict_rule"])
        self.assertIn("discoverable_with_warning", eco["canonical_presence_conflict_rule"])
        text = CONTRACT.read_text(encoding="utf-8")
        self.assertIn("canonical presence conflict", text)
        self.assertIn("does **not** silently delete the creature", text)

    def test_overlay_and_temporal_rules_do_not_rewrite_baseline_authority(self):
        gates = self.load_json(MODEL)["gate_rules"]
        self.assertTrue(gates["overlay_condition_gate"]["interaction_is_not_causation"])
        self.assertIn("without rewriting canonical range", gates["season_activity_gate"]["rule"])
        text = CONTRACT.read_text(encoding="utf-8")
        self.assertIn("current occurrence", text)
        self.assertIn("baseline range", text)

    def test_visibility_is_a_hard_information_boundary(self):
        visibility = self.load_json(MODEL)["gate_rules"]["campaign_visibility_gate"]
        self.assertEqual(visibility["campaign_suppressed"], "excluded")
        self.assertEqual(visibility["gm_only"], "discoverable_to_authorized_gm_only")
        self.assertEqual(visibility["unknown_or_conflict"], "unresolved")
        self.assertIn("never leaks", visibility["rule"])

    def test_examples_cover_presence_absence_temporal_overlay_conflict_unknown_and_hidden(self):
        examples = self.load_json(EXAMPLES)["examples"]
        ids = {e["example_id"] for e in examples}
        self.assertEqual(ids, {
            "EX-CD-NATIVE-COMMON-RIVER",
            "EX-CD-SUITABLE-BUT-ABSENT",
            "EX-CD-SEASONAL-MIGRANT",
            "EX-CD-OVERLAY-ENABLED",
            "EX-CD-CANONICAL-PRESENCE-CONFLICT",
            "EX-CD-UNKNOWN-DISTRIBUTION",
            "EX-CD-HIDDEN-CAMPAIGN-CREATURE",
        })
        self.assertTrue(all(e["illustrative_not_canonical"] for e in examples))
        absent = next(e for e in examples if e["example_id"] == "EX-CD-SUITABLE-BUT-ABSENT")
        self.assertEqual(absent["ecological_fit"], "compatible")
        self.assertEqual(absent["expected_outcome"], "excluded")
        conflict = next(e for e in examples if e["example_id"] == "EX-CD-CANONICAL-PRESENCE-CONFLICT")
        self.assertEqual(conflict["ecological_fit"], "incompatible")
        self.assertEqual(conflict["expected_outcome"], "discoverable_with_warning")
        hidden = next(e for e in examples if e["example_id"] == "EX-CD-HIDDEN-CAMPAIGN-CREATURE")
        self.assertEqual(hidden["expected_outcome"], "excluded")

    def test_result_contract_keeps_blocked_and_unresolved_available_for_authorized_diagnostics(self):
        result = self.load_json(MODEL)["gm_result_contract"]
        self.assertTrue(result["blocked_results_retained_for_authorized_gm_diagnostics"])
        self.assertTrue(result["silent_drop_of_material_conflict_forbidden"])
        self.assertIn("do not sort by an invented ecological/discovery score", result["stable_grouping_rule"])
        modes = self.load_json(MODEL)["query_modes"]
        self.assertIn("include_blocked", modes)
        self.assertIn("include_unresolved", modes)

    def test_cew_handoff_selects_cew01_without_preempting_source_recovery(self):
        model = self.load_json(MODEL)
        self.assertEqual(model["cew_handoff"]["strict_successor"], "CEW-01")
        self.assertTrue(model["cew_handoff"]["contract_can_exist_before_full_cew_population"])
        self.assertTrue(model["cew_handoff"]["missing_cew_facts_fail_closed_as_unresolved"])
        cew = self.load_json(CEW_BACKLOG)
        order = cew["strict_order"]
        statuses = {item["id"]: item["status"] for item in cew["tranches"]}
        self.assertIn(cew["current_item"], order)
        current_index = order.index(cew["current_item"])
        self.assertGreaterEqual(current_index, order.index("CEW-01"))
        if cew["current_item"] == "CEW-01":
            self.assertEqual(statuses["CEW-01"], "selected_not_started")
        else:
            self.assertEqual(statuses["CEW-01"], "completed_verified")
            self.assertIn(cew.get("completed_through"), order)
            self.assertGreaterEqual(
                order.index(cew["completed_through"]),
                order.index("CEW-01"),
            )

    def test_closeout_marks_env16_complete_and_cew01_selected(self):
        backlog = self.load_json(BACKLOG)
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        self.assertEqual(backlog["completed_through"], "ENV-16")
        self.assertEqual(backlog["current_item"], "ENV-16")
        self.assertEqual(statuses["ENV-16"], "completed_verified")
        decisions = backlog["env16_decisions"]
        self.assertEqual(decisions["contract_id"], "ENV-CD-1.0")
        self.assertTrue(decisions["ecological_suitability_separate_from_distribution"])
        self.assertTrue(decisions["visibility_is_explicit_gate"])
        self.assertTrue(decisions["blocked_and_unresolved_diagnostic_projection"])
        self.assertTrue(decisions["canonical_presence_conflict_preserved"])
        self.assertEqual(decisions["strict_successor"], "CEW-01")
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
