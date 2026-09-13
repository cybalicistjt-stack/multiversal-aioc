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

import execution_transaction_preflight as preflight


def _load_module(filename: str, module_name: str):
    path = SCRIPTS / filename
    if not path.exists():
        raise AssertionError(f"missing production control: {path.relative_to(ROOT)}")
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"unable to load production control: {path.relative_to(ROOT)}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExecutionRoutingGateTests(unittest.TestCase):
    def test_merged_start_with_test_derives_red_phase_not_stale_governed_start(self) -> None:
        reconciler = _load_module("execution_state_reconciler.py", "execution_state_reconciler")
        record = {
            "work_item_id": "ARI-20",
            "attempt_id": "ARI-20-attempt-001",
            "status": "in_progress",
            "implementation_branch": "implementation/ari-20-resource-pack-intake-ux",
            "implementation_authority": True,
            "strict_successor": "ARI-21",
        }
        observed = {
            "start_pr_state": "merged",
            "implementation_branch_exists": True,
            "focused_test_exists": True,
            "application_pr_state": "absent",
            "validation_state": "not_dispatched",
            "application_merge_sha": None,
            "closeout_state": "not_started",
        }
        state = reconciler.reconcile_execution_state(record, observed)
        self.assertEqual(state["phase"], "implementation_red")
        self.assertEqual(state["next_action"], "dispatch_focused_red_validation")

    def test_projection_bundle_is_derived_from_one_canonical_record(self) -> None:
        reconciler = _load_module("execution_state_reconciler.py", "execution_state_reconciler_projection")
        record = {
            "work_item_id": "ARI-20",
            "attempt_id": "ARI-20-attempt-001",
            "status": "in_progress",
            "implementation_branch": "implementation/ari-20-resource-pack-intake-ux",
            "implementation_authority": True,
            "strict_successor": "ARI-21",
        }
        bundle = reconciler.materialize_selector_rows(record)
        for label in ("checkpoint", "pointer", "authority", "runtime", "compiled"):
            row = bundle[label]
            self.assertEqual(row["work_item_id"], "ARI-20")
            self.assertEqual(row["attempt_id"], "ARI-20-attempt-001")
            self.assertEqual(row["status"], "in_progress")
            self.assertTrue(row["implementation_authority"])
        for label in ("checkpoint", "pointer", "authority", "runtime", "compiled"):
            self.assertEqual(bundle[label]["implementation_branch"], record["implementation_branch"])

    def test_context_guard_is_hermetic_until_diagnostic_failure_expands_it(self) -> None:
        guard = _load_module("execution_context_guard.py", "execution_context_guard")
        manifest = {
            "work_item_id": "ARI-20",
            "phase": "implementation_red",
            "allowed_paths": [
                "packages/contracts/src/asset-resource-ingestion-reuse/recursive-discovery-media-classification.ts",
                "packages/contracts/src/asset-resource-ingestion-reuse/content-addressed-byte-identity-deduplication.ts",
                "packages/contracts/src/asset-resource-ingestion-reuse/semantic-tags-collections-family-grouping.ts",
                "packages/contracts/src/asset-resource-ingestion-reuse/rights-license-use-capability-matrix.ts",
                "apps/client-ui/src/ari/ari-20.resource-pack-intake-ux.test.ts",
            ],
            "diagnostic_mode": False,
            "failure_signature": None,
        }
        allowed = guard.authorize_context_access(manifest, path=manifest["allowed_paths"][0], operation="read")
        self.assertEqual(allowed["decision"], "ALLOW_DECLARED_INPUT")
        denied = guard.authorize_context_access(manifest, path="README.md", operation="read")
        self.assertEqual(denied["decision"], "DENY_UNDECLARED_INPUT")
        search = guard.authorize_context_access(manifest, path=None, operation="repository_search")
        self.assertEqual(search["decision"], "DENY_UNDECLARED_INPUT")
        diagnostic = {**manifest, "diagnostic_mode": True, "failure_signature": "TS2307:missing-module"}
        expanded = guard.authorize_context_access(
            diagnostic,
            path="packages/contracts/src/new-required-interface.ts",
            operation="read",
        )
        self.assertEqual(expanded["decision"], "ALLOW_DIAGNOSTIC_EXPANSION")

    def test_focused_test_plus_resolved_context_requires_red_dispatch(self) -> None:
        route = preflight.decide_execution_route({
            "focused_test_exists": True,
            "required_context_resolved": True,
            "red_validation_dispatched": False,
            "red_result_observed": False,
            "diagnostic_mode": False,
            "failure_signature": None,
        })
        self.assertEqual(route["decision"], "DISPATCH_RED_NOW")
        self.assertFalse(route["repository_search_authorized"])

    def test_red_wait_and_implementation_routes_do_not_reopen_search(self) -> None:
        waiting = preflight.decide_execution_route({
            "focused_test_exists": True,
            "required_context_resolved": True,
            "red_validation_dispatched": True,
            "red_result_observed": False,
            "diagnostic_mode": False,
        })
        self.assertEqual(waiting["decision"], "WAIT_FOR_RED_RESULT")
        self.assertFalse(waiting["repository_search_authorized"])
        implement = preflight.decide_execution_route({
            "focused_test_exists": True,
            "required_context_resolved": True,
            "red_validation_dispatched": True,
            "red_result_observed": True,
            "diagnostic_mode": False,
        })
        self.assertEqual(implement["decision"], "IMPLEMENT_FROM_RED")
        self.assertFalse(implement["repository_search_authorized"])

    def test_diagnostic_expansion_requires_concrete_failure_signature(self) -> None:
        blocked = preflight.decide_execution_route({"diagnostic_mode": True, "failure_signature": None})
        self.assertEqual(blocked["decision"], "CONTINUE_CONTEXT_RESOLUTION")
        self.assertFalse(blocked["repository_search_authorized"])
        allowed = preflight.decide_execution_route({
            "diagnostic_mode": True,
            "failure_signature": "TS2307:missing-module",
        })
        self.assertEqual(allowed["decision"], "DIAGNOSTIC_EXPANSION_ALLOWED")
        self.assertTrue(allowed["repository_search_authorized"])

    def test_focused_validation_profile_is_generated_from_small_data_record(self) -> None:
        generator = _load_module("generate_focused_validation_profile.py", "generate_focused_validation_profile")
        profile = generator.build_profile({
            "work_item": "ARI-20",
            "artifact_prefix": "ari-20-resource-pack-intake-ux",
            "description": "Resource Pack Intake UX focused regression.",
            "test_path": "src/ari/ari-20.resource-pack-intake-ux.test.ts",
            "boundary": "ARI-20 only; do not begin ARI-21.",
        })
        self.assertEqual(profile["profile_id"], "ARI-20")
        self.assertEqual(
            [step["id"] for step in profile["steps"]],
            ["workspace-install", "client-typecheck", "ari20-focused-regression"],
        )
        self.assertIn("src/ari/ari-20.resource-pack-intake-ux.test.ts", profile["steps"][2]["commands"]["linux"])
        self.assertIn("src/ari/ari-20.resource-pack-intake-ux.test.ts", profile["steps"][2]["commands"]["windows"][-1])
        required_failure_fields = {"layer", "reason_code", "feature_blame", "responsibility", "blame_rationale", "remediation"}
        self.assertEqual([step["failure"]["reason_code"] for step in profile["steps"]], [
            "TOOLCHAIN.DEPENDENCY_INSTALL_FAILURE",
            "BUILD.COMPILE_FAILURE",
            "TEST_UNIT.ASSERTION_FAILURE",
        ])
        for step in profile["steps"]:
            self.assertEqual(set(step["failure"]), required_failure_fields)

    def test_bootstrap_and_profile_persist_execution_routing_controls(self) -> None:
        bootstrap = (ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md").read_text(encoding="utf-8")
        profile = json.loads((ROOT / "governance/ai/runtime/EXECUTION_PROFILE.json").read_text(encoding="utf-8"))
        for marker in (
            "execution_state_reconciler.py",
            "execution_context_guard.py",
            "DISPATCH_RED_NOW",
            "hermetic tranche context",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, bootstrap)
        routing = profile["execution_hardening"]["execution_routing"]
        self.assertEqual(routing["state_reconciler"], "scripts/execution_state_reconciler.py")
        self.assertEqual(routing["context_guard"], "scripts/execution_context_guard.py")
        self.assertEqual(routing["validation_profile_generator"], "scripts/generate_focused_validation_profile.py")
        self.assertEqual(routing["red_dispatch_decision"], "DISPATCH_RED_NOW")

    def test_atomic_projection_uses_direct_git_objects_without_one_shot_workflows(self) -> None:
        profile = json.loads((ROOT / "governance/ai/runtime/EXECUTION_PROFILE.json").read_text(encoding="utf-8"))
        critical = profile["execution_hardening"].get("critical_path_optimization", {})
        atomic = critical.get("atomic_projection", {})
        self.assertTrue(atomic.get("git_object_mutation_preferred"))
        self.assertEqual(atomic.get("commit_shape"), "one_tree_one_commit_one_ref_update")
        self.assertTrue(atomic.get("temporary_workflow_generation_prohibited_when_git_objects_available"))
        self.assertEqual(atomic.get("planner"), "scripts/execution_atomic_projection.py")
        planner = _load_module("execution_atomic_projection.py", "execution_atomic_projection")
        plan = planner.build_projection_plan({
            "operation_id": "ari22a-start",
            "idempotency_key": "ari22a:start:001",
            "base_sha": "a" * 40,
            "branch": "governance/ari-22a-start",
            "paths": ["a.json", "b.json", "c.json"],
        })
        self.assertEqual(plan["decision"], "ATOMIC_GIT_OBJECT_PROJECTION")
        self.assertEqual(plan["mutation_sequence"], ["create_blob", "create_tree", "create_commit", "update_ref"])
        self.assertEqual(plan["paths"], ["a.json", "b.json", "c.json"])

    def test_terminal_proof_is_embedded_in_canonical_main_health(self) -> None:
        workflow = (ROOT / ".github/workflows/validate-repository-health.yml").read_text(encoding="utf-8")
        self.assertIn("execution_terminal_auto_proof.py", workflow)
        self.assertIn("terminal-reconciliation-result.json", workflow)
        proof = _load_module("execution_terminal_auto_proof.py", "execution_terminal_auto_proof")
        checkpoint = {
            "work_item_id": "ARI-22A",
            "status": "completed_verified",
            "strict_successor": "ARI-22B",
            "completion_evidence": {"application_validation_run": 12345},
            "terminal_reconciliation_seed": {
                "cycle_id": "ari22a-cycle-001",
                "trace_id": "ari22a-trace-001",
                "resume_generation": 0,
                "resumed_from_cycle_id": None,
                "elapsed_active_minutes": 12.0,
                "dynamic_fill_attempted": True,
                "safe_same_lane_work_available": False,
                "fill_exit_reason": "safe_work_exhausted",
                "operation_ledger": [{
                    "operation_id": "ari22a-op-01",
                    "idempotency_key": "ari22a:op:01",
                    "status": "completed",
                    "attempts": 1,
                    "trace_id": "ari22a-trace-001",
                }],
                "side_effect_ledger": [{
                    "effect_id": "ari22a-effect-01",
                    "idempotency_key": "ari22a:effect:01",
                    "status": "verified",
                    "trace_id": "ari22a-trace-001",
                }],
            },
        }
        state = proof.build_terminal_state(checkpoint)
        self.assertEqual(state["work_item_status"], "completed_verified")
        self.assertEqual(state["execution_reconciliation"]["desired_state"], "terminal_verified")
        self.assertEqual(state["execution_reconciliation"]["verification_evidence"][0]["evidence_id"], "application-validation-12345")

    def test_ari22a_terminal_identity_is_stable_across_lifecycle_transitions(self) -> None:
        checkpoint = json.loads((ROOT / "governance/ai/work-state/ARI-22A-attempt-001.json").read_text(encoding="utf-8"))
        self.assertIn(checkpoint["status"], {"selected_not_started", "in_progress", "completed_verified"})
        if checkpoint["status"] == "selected_not_started":
            self.assertFalse(checkpoint["implementation_authority"])
            self.assertIsNone(checkpoint["implementation_branch"])
        elif checkpoint["status"] == "in_progress":
            self.assertTrue(checkpoint["implementation_authority"])
            self.assertEqual(
                checkpoint["implementation_branch"],
                "implementation/ari-22a-golden-fixture-intake-unified-catalog-proof",
            )
        else:
            self.assertFalse(checkpoint["implementation_authority"])
        seed = checkpoint.get("terminal_reconciliation_seed", {})
        self.assertEqual(seed.get("cycle_id"), "ari22a-cycle-001")
        self.assertEqual(seed.get("trace_id"), "ari22a-trace-001")
        self.assertTrue(seed.get("operation_ledger"))
        self.assertTrue(seed.get("side_effect_ledger"))


if __name__ == "__main__":
    unittest.main()
