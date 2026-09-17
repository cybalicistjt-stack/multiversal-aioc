from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _load(name: str, relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {relative}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EXECUTION_GUARD = _load("ops3_execution_guard", "scripts/ops3_execution_guard.py")
MERGE_LEASE = _load("ops3_merge_lease", "scripts/ops3_merge_lease.py")


class Ops3ExecutionConcurrencyTests(unittest.TestCase):
    def test_terminal_response_fails_while_bounded_continue_is_in_progress(self) -> None:
        checkpoint = {
            "status": "in_progress",
            "execution_guard": {
                "continue_turns": 1,
                "stall_nudges": 0,
                "terminal_response_allowed": False,
                "stop_reason": None,
            },
            "execution_conformance": {"status": "in_progress", "policy_violations": []},
        }
        errors = EXECUTION_GUARD.validate_terminal_response(checkpoint)
        self.assertIn("OPS3.NONTERMINAL_RESPONSE", errors)

    def test_owner_or_external_blocker_can_end_a_continue_truthfully(self) -> None:
        checkpoint = {
            "status": "in_progress",
            "execution_guard": {
                "continue_turns": 1,
                "stall_nudges": 0,
                "terminal_response_allowed": True,
                "stop_reason": {
                    "kind": "external_blocker",
                    "evidence": "target service unavailable after verified check",
                },
            },
            "execution_conformance": {"status": "blocked", "policy_violations": []},
        }
        self.assertEqual(EXECUTION_GUARD.validate_terminal_response(checkpoint), [])

    def test_multi_continue_cannot_be_certified_clean(self) -> None:
        checkpoint = {
            "status": "completed_verified",
            "execution_guard": {
                "continue_turns": 3,
                "stall_nudges": 0,
                "terminal_response_allowed": True,
                "stop_reason": {"kind": "completed", "evidence": "verified closeout"},
            },
            "execution_conformance": {"status": "completed_verified", "policy_violations": []},
        }
        errors = EXECUTION_GUARD.validate_execution_conformance(checkpoint)
        self.assertIn("OPS3.MULTI_CONTINUE_UNRECORDED", errors)

    def test_stall_nudge_cannot_be_certified_clean(self) -> None:
        checkpoint = {
            "status": "completed_verified",
            "execution_guard": {
                "continue_turns": 1,
                "stall_nudges": 1,
                "terminal_response_allowed": True,
                "stop_reason": {"kind": "completed", "evidence": "verified closeout"},
            },
            "execution_conformance": {"status": "completed_verified", "policy_violations": []},
        }
        errors = EXECUTION_GUARD.validate_execution_conformance(checkpoint)
        self.assertIn("OPS3.STALL_NUDGE_UNRECORDED", errors)

    def test_merge_authorization_fails_if_main_advanced_after_validation(self) -> None:
        lease = MERGE_LEASE.acquire_lease(
            MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app", generation=7),
            expected_generation=7,
            holder="PCA-13-attempt-001",
            validated_head="feature-head",
            validated_base="main-a",
        )
        errors = MERGE_LEASE.validate_merge_authorization(
            lease,
            fresh_main_sha="main-b",
            pr_head_sha="feature-head",
            holder="PCA-13-attempt-001",
        )
        self.assertIn("OPS3.STALE_MAIN", errors)

    def test_competing_acquisitions_from_same_generation_cannot_both_apply(self) -> None:
        free = MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app", generation=11)
        first = MERGE_LEASE.acquire_lease(
            free,
            expected_generation=11,
            holder="attempt-a",
            validated_head="head-a",
            validated_base="main-a",
        )
        with self.assertRaises(MERGE_LEASE.LeaseConflict):
            MERGE_LEASE.acquire_lease(
                first,
                expected_generation=11,
                holder="attempt-b",
                validated_head="head-b",
                validated_base="main-a",
            )

    def test_release_requires_same_holder_and_verified_merge(self) -> None:
        held = MERGE_LEASE.acquire_lease(
            MERGE_LEASE.free_lease("cybalicistjt-stack/multiversal-aioc", generation=3),
            expected_generation=3,
            holder="OPS3-02",
            validated_head="head",
            validated_base="base",
        )
        with self.assertRaises(MERGE_LEASE.LeaseConflict):
            MERGE_LEASE.release_lease(held, holder="other", merged_sha="merge")
        released = MERGE_LEASE.release_lease(held, holder="OPS3-02", merged_sha="merge")
        self.assertEqual(released["status"], "free")
        self.assertEqual(released["generation"], 5)
        self.assertEqual(released["last_merge_sha"], "merge")


if __name__ == "__main__":
    unittest.main()
