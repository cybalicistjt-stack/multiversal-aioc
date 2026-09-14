from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import execution_transaction_preflight as preflight


def _load_reconciler():
    path = SCRIPTS / "execution_state_reconciler.py"
    spec = importlib.util.spec_from_file_location("execution_state_reconciler_capsule", path)
    if spec is None or spec.loader is None:
        raise AssertionError("unable to load execution_state_reconciler.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExecutionCapsuleTests(unittest.TestCase):
    def test_execution_route_requires_compiled_capsule_before_red_dispatch(self) -> None:
        route = preflight.decide_execution_route({
            "capsule_ready": False,
            "focused_test_exists": True,
            "required_context_resolved": True,
            "red_validation_dispatched": False,
            "red_result_observed": False,
            "diagnostic_mode": False,
            "failure_signature": None,
        })
        self.assertEqual(route["decision"], "COMPILE_EXECUTION_CAPSULE")
        self.assertFalse(route["repository_search_authorized"])

    def test_capsule_compiles_context_validation_merge_and_closeout_into_one_packet(self) -> None:
        reconciler = _load_reconciler()
        compile_capsule = getattr(reconciler, "compile_execution_capsule", None)
        self.assertTrue(callable(compile_capsule), "execution capsule compiler is missing")
        if not callable(compile_capsule):
            return

        capsule = compile_capsule({
            "work_item_id": "ARI-22C",
            "attempt_id": "ARI-22C-attempt-001",
            "application_repository": "cybalicistjt-stack/Multiversal-app",
            "application_base_sha": "8" * 40,
            "implementation_branch": "implementation/ari-22c-recovery-deterministic-receipt-final-ari-closure-proof",
            "allowed_context_paths": [
                "packages/contracts/src/asset-resource-ingestion-reuse/missing-source-relink-derivative-rebuild-recovery.ts",
                "packages/contracts/src/asset-resource-ingestion-reuse/cross-system-reuse-rights-scale-proof.ts",
            ],
            "application_mutation_allowlist": [
                "apps/client-ui/src/ari/ari-22c.recovery-deterministic-receipt-final-closure.test.ts",
                "packages/contracts/src/asset-resource-ingestion-reuse/cross-system-reuse-rights-scale-proof.ts",
                "governance/application-planning/validation-core/profiles/ARI-22C.json",
            ],
            "validation_profile_id": "ARI-22C",
            "focused_test_path": "src/ari/ari-22c.recovery-deterministic-receipt-final-closure.test.ts",
            "repository_capabilities": {
                "allow_squash_merge": True,
                "allow_merge_commit": False,
                "allow_rebase_merge": False,
            },
            "closeout_projection_paths": [
                "governance/ai/work-state/ARI-22C-attempt-001.json",
                "governance/ai/runtime/CURRENT_WORK_POINTER.json",
                "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json",
                "governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json",
                "governance/ai/runtime/ROADMAP_COMPILED_PROJECTION.json",
                "governance/application-planning/asset-resource-ingestion-reuse/ARI_PROGRAM_BACKLOG.json",
            ],
            "strict_successor": {
                "work_item_id": "MIB-16",
                "attempt_id": "MIB-16-attempt-001",
                "selection_state": "selected_not_started",
                "implementation_authority": False,
                "implementation_branch": None,
            },
        })

        self.assertEqual(capsule["schema_version"], "1.0.0")
        self.assertEqual(capsule["work_item_id"], "ARI-22C")
        self.assertEqual(capsule["merge_plan"]["method"], "squash")
        self.assertEqual(capsule["validation"]["profile_id"], "ARI-22C")
        self.assertEqual(capsule["strict_successor"]["work_item_id"], "MIB-16")
        self.assertEqual(capsule["post_start_discovery_policy"], "DENY_UNLESS_DIAGNOSTIC_FAILURE_SIGNATURE")
        self.assertEqual(len(capsule["capsule_digest"]), 64)

    def test_transition_bundle_is_derived_from_one_canonical_closeout_record(self) -> None:
        reconciler = _load_reconciler()
        materialize = getattr(reconciler, "materialize_transition_bundle", None)
        self.assertTrue(callable(materialize), "deterministic transition materializer is missing")
        if not callable(materialize):
            return

        bundle = materialize({
            "work_item_id": "ARI-22C",
            "attempt_id": "ARI-22C-attempt-001",
            "status": "completed_verified",
            "implementation_authority": False,
            "implementation_branch": None,
            "strict_successor": "MIB-16",
            "successor_attempt_id": "MIB-16-attempt-001",
            "successor_title": "Release Readiness, Diagnostics & Portability",
            "application_pr": 470,
            "validated_head": "6" * 40,
            "validation_run": 34874955597,
            "deterministic_receipt_sha256": "1" * 64,
            "merge_sha": "7" * 40,
        })

        self.assertEqual(bundle["completed"]["work_item_id"], "ARI-22C")
        self.assertEqual(bundle["completed"]["status"], "completed_verified")
        self.assertFalse(bundle["completed"]["implementation_authority"])
        self.assertEqual(bundle["successor"]["work_item_id"], "MIB-16")
        self.assertEqual(bundle["successor"]["status"], "selected_not_started")
        self.assertFalse(bundle["successor"]["implementation_authority"])
        self.assertIsNone(bundle["successor"]["implementation_branch"])
        self.assertEqual(bundle["evidence"]["application_pr"], 470)
        self.assertEqual(bundle["evidence"]["validation_run"], 34874955597)


if __name__ == "__main__":
    unittest.main()
