from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import execution_atomic_projection as atomic
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


if __name__ == "__main__":
    unittest.main()
