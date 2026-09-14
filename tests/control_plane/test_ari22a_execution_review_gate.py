from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import execution_atomic_projection as atomic
import execution_environment_admission as environment
import execution_integrity_gate as integrity
import execution_merge_authorization as merge_authorization
import execution_state_reconciler as reconciler
import execution_transaction_preflight as preflight


class Ari22AExecutionReviewGateTests(unittest.TestCase):
    def test_repository_capability_preflight_selects_only_supported_merge_method(self) -> None:
        capabilities = {
            "allow_merge_commit": False,
            "allow_rebase_merge": False,
            "allow_squash_merge": True,
        }
        selected = preflight.select_merge_method(capabilities)
        self.assertEqual(selected["decision"], "USE_MERGE_METHOD")
        self.assertEqual(selected["merge_method"], "squash")

        rejected = preflight.select_merge_method(capabilities, requested_method="merge")
        self.assertEqual(rejected["decision"], "STOP_UNSUPPORTED_MERGE_METHOD")
        self.assertEqual(rejected["supported_methods"], ["squash"])

    def test_precloseout_blocks_below_target_without_safe_work_exhaustion(self) -> None:
        decision = preflight.assess_precloseout_readiness({
            "elapsed_active_minutes": 22.0,
            "target_cycle_minutes": 24.0,
            "safe_same_lane_work_available": False,
            "dynamic_fill_attempted": True,
            "fill_exit_reason": "closeout_switch_reached",
        })
        self.assertEqual(decision["decision"], "CONTINUE_SAME_CYCLE")
        self.assertEqual(decision["reason_code"], "MVEXEC-ENVELOPE-TARGET-PENDING")
        self.assertEqual(decision["remaining_active_minutes"], 2.0)

    def test_precloseout_allows_target_reached(self) -> None:
        decision = preflight.assess_precloseout_readiness({
            "elapsed_active_minutes": 24.0,
            "target_cycle_minutes": 24.0,
            "safe_same_lane_work_available": False,
            "dynamic_fill_attempted": True,
            "fill_exit_reason": "closeout_switch_reached",
        })
        self.assertEqual(decision["decision"], "READY_FOR_CLOSEOUT")
        self.assertEqual(decision["reason_code"], "MVEXEC-ENVELOPE-READY")

    def test_multifile_projection_rejects_contents_api_transport(self) -> None:
        with self.assertRaises(atomic.AtomicProjectionError):
            atomic.build_projection_plan({
                "operation_id": "closeout-op",
                "idempotency_key": "closeout:001",
                "base_sha": "a" * 40,
                "branch": "governance/example-closeout",
                "paths": ["a.json", "b.json"],
                "mutation_transport": "contents_api",
            })

        plan = atomic.build_projection_plan({
            "operation_id": "closeout-op",
            "idempotency_key": "closeout:001",
            "base_sha": "a" * 40,
            "branch": "governance/example-closeout",
            "paths": ["a.json", "b.json"],
            "mutation_transport": "git_data_api",
        })
        self.assertEqual(plan["mutation_transport"], "git_data_api")
        self.assertEqual(plan["mutation_sequence"], ["create_blob", "create_tree", "create_commit", "update_ref"])

    def test_green_execution_state_is_explicitly_nonterminal(self) -> None:
        state = reconciler.reconcile_execution_state(
            {
                "status": "in_progress",
                "implementation_authority": True,
                "implementation_branch": "implementation/ari-22b-example",
            },
            {
                "start_pr_state": "merged",
                "implementation_branch_exists": True,
                "focused_test_exists": True,
                "application_pr_state": "open",
                "validation_state": "success",
                "application_merge_sha": None,
                "closeout_state": "not_started",
            },
        )
        self.assertEqual(state["phase"], "integration")
        self.assertEqual(state["next_action"], "merge_exact_validated_head")
        self.assertEqual(state["response_gate"], "CONTINUE_EXECUTION")

    def test_closed_execution_state_still_requires_terminal_preflight(self) -> None:
        state = reconciler.reconcile_execution_state(
            {"status": "completed_verified"},
            {},
        )
        self.assertEqual(state["phase"], "closed")
        self.assertEqual(state["response_gate"], "TERMINATION_PREFLIGHT_REQUIRED")

    def test_human_ai_team_contract_is_machine_readable(self) -> None:
        profile = json.loads((ROOT / "governance/ai/runtime/EXECUTION_PROFILE.json").read_text(encoding="utf-8"))
        contract = profile["execution_hardening"]["human_ai_team_contract"]
        self.assertEqual(contract["agent_execution_role"], "execute_authorized_unit_to_terminal_boundary")
        self.assertEqual(contract["owner_role"], "set_priority_and_resolve_explicit_owner_decisions")
        self.assertFalse(contract["progress_update_is_terminal"])
        self.assertTrue(contract["discover_repository_capabilities_before_side_effects"])
        self.assertEqual(
            contract["interrupt_only_for"],
            ["genuine_blocker", "owner_decision_required", "out_of_scope_high_risk_action"],
        )
        self.assertTrue(contract["retry_threshold_exceeded_requires_escalation"])

    def test_ari22b_owner_observation_cannot_be_rewritten_as_single_continue(self) -> None:
        checkpoint = integrity.load_effective_checkpoint(
            ROOT,
            "governance/ai/work-state/ARI-22B-attempt-001.json",
        )
        observation = checkpoint["owner_interaction_observation"]
        self.assertEqual(observation["continue_turns"], 2)
        self.assertEqual(observation["stall_nudges"], 1)
        self.assertEqual(checkpoint["convergence_control"]["owner_continue_count"], 2)
        self.assertFalse(checkpoint["convergence_control"]["single_continue_achieved"])
        integrity.validate_completed_attempt_integrity(
            checkpoint,
            context="ARI-22B-attempt-001",
            service_objective=checkpoint["convergence_control"]["service_objective"],
        )

    def test_ari22b_preserves_historical_nonconformance_instead_of_fabricating_diagnostics(self) -> None:
        checkpoint = integrity.load_effective_checkpoint(
            ROOT,
            "governance/ai/work-state/ARI-22B-attempt-001.json",
        )
        conformance = checkpoint["execution_conformance"]
        self.assertEqual(conformance["status"], "historical_nonconforming")
        self.assertFalse(checkpoint["convergence_control"]["diagnostic_mode"])
        self.assertIn("diagnostic_threshold_missed", conformance["policy_violations"])
        self.assertIn("merge_capability_preflight_bypassed", conformance["policy_violations"])
        self.assertIn("single_continue_misreported", conformance["policy_violations"])
        self.assertIn("owner_visible_timing_target_missed", conformance["policy_violations"])

    def test_owner_visible_timing_uses_real_timestamps_not_synthetic_active_minutes(self) -> None:
        checkpoint = integrity.load_effective_checkpoint(
            ROOT,
            "governance/ai/work-state/ARI-22B-attempt-001.json",
        )
        timing = integrity.measure_owner_visible_timing(checkpoint)
        self.assertAlmostEqual(timing["wall_elapsed_minutes"], 58.1167, places=3)
        self.assertEqual(timing["target_minutes"], 24.0)
        self.assertFalse(timing["target_met"])
        self.assertEqual(timing["measurement_basis"], "checkpoint_started_at_to_completed_at")
        self.assertFalse(timing["synthetic_active_minutes_substitute"])

    def test_merge_authorization_receipt_binds_repository_head_and_permitted_method(self) -> None:
        receipt = merge_authorization.authorize_merge_effect(
            {
                "repository": "cybalicistjt-stack/Multiversal-app",
                "head_sha": "2" * 40,
                "allow_merge_commit": False,
                "allow_rebase_merge": False,
                "allow_squash_merge": True,
            }
        )
        self.assertEqual(receipt["decision"], "MERGE_AUTHORIZED")
        self.assertEqual(receipt["repository"], "cybalicistjt-stack/Multiversal-app")
        self.assertEqual(receipt["expected_head_sha"], "2" * 40)
        self.assertEqual(receipt["merge_method"], "squash")
        self.assertEqual(len(receipt["authorization_digest"]), 64)
        verified = merge_authorization.validate_merge_invocation(
            receipt,
            {
                "repository": "cybalicistjt-stack/Multiversal-app",
                "expected_head_sha": "2" * 40,
                "merge_method": "squash",
            },
        )
        self.assertEqual(verified["status"], "PASS")
        with self.assertRaises(merge_authorization.MergeAuthorizationError):
            merge_authorization.validate_merge_invocation(
                receipt,
                {
                    "repository": "cybalicistjt-stack/Multiversal-app",
                    "expected_head_sha": "2" * 40,
                    "merge_method": "merge",
                },
            )
        with self.assertRaises(preflight.TransactionPreflightError):
            merge_authorization.authorize_merge_effect(
                {
                    "repository": "cybalicistjt-stack/Multiversal-app",
                    "head_sha": "stale-or-unknown",
                    "allow_merge_commit": False,
                    "allow_rebase_merge": False,
                    "allow_squash_merge": True,
                }
            )

    def test_environment_admission_blocks_harness_defects_before_product_mutation(self) -> None:
        base = {
            "repository": "cybalicistjt-stack/Multiversal-app",
            "head_sha": "3" * 40,
            "clean_worktree": True,
            "tracked_executable_line_endings_normalized": True,
            "validation_harness_ready": True,
            "validation_cache_policy_ready": True,
            "required_runner_lanes_available": True,
        }
        admitted = environment.assess_environment(base)
        self.assertEqual(admitted["decision"], "ADMIT_PRODUCT_MUTATION")
        self.assertEqual(environment.validate_admission_receipt(admitted)["status"], "PASS")
        blocked = environment.assess_environment({**base, "validation_cache_policy_ready": False})
        self.assertEqual(blocked["decision"], "STOP_ENVIRONMENT_NOT_READY")
        self.assertEqual(blocked["failed_checks"], ["validation_cache_policy_ready"])
        self.assertEqual(blocked["repair_lane"], "separate_or_explicitly_classified_validation_harness_repair")

    def test_integrity_gate_audits_recent_completed_even_after_successor_selection(self) -> None:
        result = integrity.check(ROOT)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["active_attempt"]["attempt_id"], "ARI-22C-attempt-001")
        self.assertEqual(result["active_attempt"]["status"], "selected_not_started")
        recent = {row["attempt_id"]: row for row in result["recent_completed"]}
        self.assertIn("ARI-22B-attempt-001", recent)
        self.assertEqual(recent["ARI-22B-attempt-001"]["execution_conformance"], "historical_nonconforming")
        self.assertEqual(recent["ARI-22B-attempt-001"]["owner_continue_turns"], 2)

    def test_execution_integrity_policy_is_current_and_small_scope(self) -> None:
        policy = (ROOT / "governance/ai/MULTIVERSAL_EXECUTION_INTEGRITY_POLICY.md").read_text(encoding="utf-8")
        self.assertIn("**Status:** CURRENT", policy)
        self.assertIn("small executable seams", policy)
        self.assertIn("harness complexity budget", policy.lower())
        self.assertIn("scripts/execution_integrity_gate.py", policy)
        self.assertIn("scripts/execution_environment_admission.py", policy)
        self.assertIn("scripts/execution_merge_authorization.py", policy)


if __name__ == "__main__":
    unittest.main()
