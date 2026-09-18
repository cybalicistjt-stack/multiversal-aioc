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
        checkpoint={"status":"in_progress","execution_guard":{"continue_turns":1,"stall_nudges":0,"terminal_response_allowed":False,"stop_reason":None},"execution_conformance":{"status":"in_progress","policy_violations":[]}}
        self.assertIn("OPS3.NONTERMINAL_RESPONSE", EXECUTION_GUARD.validate_terminal_response(checkpoint))

    def test_multi_continue_must_be_recorded_as_process_violation(self) -> None:
        checkpoint={"status":"completed_verified","execution_guard":{"continue_turns":4,"stall_nudges":2,"terminal_response_allowed":True,"stop_reason":{"kind":"completed","evidence":"verified closeout"}},"execution_conformance":{"status":"conforming","policy_violations":[]}}
        errors=EXECUTION_GUARD.validate_execution_conformance(checkpoint)
        self.assertIn("OPS3.MULTI_CONTINUE_UNRECORDED", errors)
        self.assertIn("OPS3.STALL_NUDGE_UNRECORDED", errors)

    def test_reservations_are_fifo_and_carry_no_prepared_candidate(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app",generation=10)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=10,holder="lane-a",reservation_id="a")
        state=MERGE_LEASE.reserve_turn(state,expected_generation=11,holder="lane-b",reservation_id="b")
        self.assertEqual([e["holder"] for e in state["queue"]],["lane-a","lane-b"])
        self.assertIsNone(state["validated_head"])
        self.assertIsNone(state["validated_base"])

    def test_only_queue_head_can_activate(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicjt-stack/Multiversal-app",generation=3)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=3,holder="first",reservation_id="r1")
        state=MERGE_LEASE.reserve_turn(state,expected_generation=4,holder="second",reservation_id="r2")
        with self.assertRaises(MERGE_LEASE.LeaseConflict):
            MERGE_LEASE.activate_next_turn(state,expected_generation=5,holder="second",fresh_main_sha="main-a")
        active=MERGE_LEASE.activate_next_turn(state,expected_generation=5,holder="first",fresh_main_sha="main-a")
        self.assertEqual(active["turn_base"],"main-a")
        self.assertEqual([e["holder"] for e in active["queue"]],["second"])

    def test_validation_is_bound_only_after_turn_activation_and_to_turn_base(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app",generation=20)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=20,holder="lane-a",reservation_id="r")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=21,holder="lane-a",fresh_main_sha="main-current")
        with self.assertRaises(MERGE_LEASE.LeaseConflict):
            MERGE_LEASE.bind_validated_candidate(state,expected_generation=22,holder="lane-a",validated_head="head",validated_base="old-main")
        bound=MERGE_LEASE.bind_validated_candidate(state,expected_generation=22,holder="lane-a",validated_head="head",validated_base="main-current")
        self.assertEqual(MERGE_LEASE.validate_merge_authorization(bound,fresh_main_sha="main-current",pr_head_sha="head",holder="lane-a"),[])

    def test_release_preserves_fifo_and_next_turn_uses_new_main_without_rebase_race(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app",generation=30)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=30,holder="lane-a",reservation_id="a")
        state=MERGE_LEASE.reserve_turn(state,expected_generation=31,holder="lane-b",reservation_id="b")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=32,holder="lane-a",fresh_main_sha="main-a")
        state=MERGE_LEASE.bind_validated_candidate(state,expected_generation=33,holder="lane-a",validated_head="head-a",validated_base="main-a")
        state=MERGE_LEASE.release_lease(state,holder="lane-a",merged_sha="merge-a")
        self.assertEqual([e["holder"] for e in state["queue"]],["lane-b"])
        next_state=MERGE_LEASE.activate_next_turn(state,expected_generation=35,holder="lane-b",fresh_main_sha="merge-a")
        self.assertEqual(next_state["turn_base"],"merge-a")
        self.assertIsNone(next_state["validated_head"])

    def test_stale_main_still_fails_closed_inside_active_turn(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app",generation=40)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=40,holder="lane-a",reservation_id="a")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=41,holder="lane-a",fresh_main_sha="main-a")
        state=MERGE_LEASE.bind_validated_candidate(state,expected_generation=42,holder="lane-a",validated_head="head-a",validated_base="main-a")
        errors=MERGE_LEASE.validate_merge_authorization(state,fresh_main_sha="main-b",pr_head_sha="head-a",holder="lane-a")
        self.assertIn("OPS3.STALE_MAIN",errors)


    def test_stalled_completed_turn_can_be_recovery_released_and_fifo_continues(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app",generation=50)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=50,holder="stalled",reservation_id="a")
        state=MERGE_LEASE.reserve_turn(state,expected_generation=51,holder="next",reservation_id="b")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=52,holder="stalled",fresh_main_sha="main-a")
        state=MERGE_LEASE.bind_validated_candidate(state,expected_generation=53,holder="stalled",validated_head="head-a",validated_base="main-a")
        recovered=MERGE_LEASE.recover_completed_turn(
            state,
            expected_generation=54,
            stalled_holder="stalled",
            fresh_main_sha="merge-a",
            merged_sha="merge-a",
            recovery_location="governance/ai/work-state/W-attempt-001.json",
            recovery_executor="replacement-chat",
        )
        self.assertEqual(recovered["status"],"free")
        self.assertEqual(recovered["last_merge_sha"],"merge-a")
        self.assertEqual(recovered["last_recovery_handoff"]["recovery_location"],"governance/ai/work-state/W-attempt-001.json")
        self.assertEqual([e["holder"] for e in recovered["queue"]],["next"])
        next_state=MERGE_LEASE.activate_next_turn(recovered,expected_generation=55,holder="next",fresh_main_sha="merge-a")
        self.assertEqual(next_state["holder"],"next")

    def test_recovery_release_fails_if_main_does_not_match_verified_merge(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app",generation=60)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=60,holder="stalled",reservation_id="a")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=61,holder="stalled",fresh_main_sha="main-a")
        with self.assertRaises(MERGE_LEASE.LeaseConflict):
            MERGE_LEASE.recover_completed_turn(
                state,
                expected_generation=62,
                stalled_holder="stalled",
                fresh_main_sha="other-main",
                merged_sha="merge-a",
                recovery_location="governance/ai/work-state/W-attempt-001.json",
                recovery_executor="replacement-chat",
            )

    def test_recovery_release_requires_durable_recovery_location(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app",generation=70)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=70,holder="stalled",reservation_id="a")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=71,holder="stalled",fresh_main_sha="main-a")
        with self.assertRaises(MERGE_LEASE.LeaseConflict):
            MERGE_LEASE.recover_completed_turn(
                state,
                expected_generation=72,
                stalled_holder="stalled",
                fresh_main_sha="merge-a",
                merged_sha="merge-a",
                recovery_location="",
                recovery_executor="replacement-chat",
            )

    def test_direct_protected_main_write_is_rejected_even_for_active_holder(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/multiversal-aioc",generation=80)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=80,holder="ops",reservation_id="r")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=81,holder="ops",fresh_main_sha="main-a")
        errors=MERGE_LEASE.validate_protected_main_write(
            state,
            target_repo="cybalicistjt-stack/multiversal-aioc",
            fresh_main_sha="main-a",
            holder="ops",
            mutation_kind="contents_api",
        )
        self.assertIn(MERGE_LEASE.DIRECT_MAIN_MUTATION,errors)

    def test_held_turn_detects_protected_main_bypass_instead_of_normalizing_rebase(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/multiversal-aioc",generation=90)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=90,holder="lane-a",reservation_id="r")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=91,holder="lane-a",fresh_main_sha="main-a")
        errors=MERGE_LEASE.validate_protected_main_write(
            state,
            target_repo="cybalicistjt-stack/multiversal-aioc",
            fresh_main_sha="main-b",
            holder="other-writer",
            mutation_kind="contents_api",
        )
        self.assertIn(MERGE_LEASE.PROTECTED_MAIN_BYPASS,errors)
        self.assertIn(MERGE_LEASE.DIRECT_MAIN_MUTATION,errors)

    def test_exact_queue_bound_merge_is_the_only_protected_main_write_path(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app",generation=100)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=100,holder="lane-a",reservation_id="r")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=101,holder="lane-a",fresh_main_sha="main-a")
        state=MERGE_LEASE.bind_validated_candidate(state,expected_generation=102,holder="lane-a",validated_head="head-a",validated_base="main-a")
        errors=MERGE_LEASE.validate_protected_main_write(
            state,
            target_repo="cybalicistjt-stack/Multiversal-app",
            fresh_main_sha="main-a",
            holder="lane-a",
            mutation_kind="pull_request_merge",
            pr_head_sha="head-a",
        )
        self.assertEqual(errors,[])

    def test_direct_acquire_is_retired(self) -> None:
        with self.assertRaises(MERGE_LEASE.LeaseConflict):
            MERGE_LEASE.acquire_lease()

if __name__ == "__main__":
    unittest.main()
