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

    def test_active_turn_has_bounded_liveness_and_duplicate_progress_cannot_extend_it(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app",generation=110)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=110,holder="lane-a",reservation_id="r")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=111,holder="lane-a",fresh_main_sha="main-a",observed_at="2026-09-19T00:00:00Z",max_idle_seconds=900)
        state=MERGE_LEASE.record_turn_progress(state,expected_generation=112,holder="lane-a",phase="prepared",evidence="candidate head abc",observed_at="2026-09-19T00:05:00Z")
        with self.assertRaises(MERGE_LEASE.LeaseConflict):
            MERGE_LEASE.record_turn_progress(state,expected_generation=113,holder="lane-a",phase="prepared",evidence="candidate head abc",observed_at="2026-09-19T00:06:00Z")
        self.assertIn(MERGE_LEASE.ACTIVE_TURN_STALLED,MERGE_LEASE.validate_turn_liveness(state,now="2026-09-19T00:21:00Z"))

    def test_stale_unmerged_turn_cannot_merge_and_can_be_recovered_without_reordering_fifo(self) -> None:
        state=MERGE_LEASE.free_lease("cybalicistjt-stack/Multiversal-app",generation=120)
        state=MERGE_LEASE.reserve_turn(state,expected_generation=120,holder="stalled",reservation_id="a")
        state=MERGE_LEASE.reserve_turn(state,expected_generation=121,holder="next",reservation_id="b")
        state=MERGE_LEASE.activate_next_turn(state,expected_generation=122,holder="stalled",fresh_main_sha="main-a",observed_at="2026-09-19T00:00:00Z",max_idle_seconds=900)
        state=MERGE_LEASE.bind_validated_candidate(state,expected_generation=123,holder="stalled",validated_head="head-a",validated_base="main-a",observed_at="2026-09-19T00:01:00Z")
        errors=MERGE_LEASE.validate_merge_authorization(state,fresh_main_sha="main-a",pr_head_sha="head-a",holder="stalled",now="2026-09-19T00:17:00Z")
        self.assertIn(MERGE_LEASE.ACTIVE_TURN_STALLED,errors)
        recovered=MERGE_LEASE.recover_stalled_turn(state,expected_generation=124,stalled_holder="stalled",fresh_main_sha="main-a",recovery_location="governance/ai/work-state/W.json",recovery_executor="replacement",reason="idle deadline exceeded",now="2026-09-19T00:17:00Z")
        self.assertEqual(recovered["status"],"free")
        self.assertEqual([x["holder"] for x in recovered["queue"]],["next"])

    def test_ready_candidates_enter_publication_order_only_after_green_prequeue_validation(self) -> None:
        state=MERGE_LEASE.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=10)
        candidate={"candidate_id":"a","lane":"msas","work_item_id":"MSAS-X","pr_number":1,"head_sha":"head-a","prequeue_validation":{"status":"green","head_sha":"head-a","run_id":"run-a"}}
        state=MERGE_LEASE.submit_ready_candidate(state,expected_generation=10,candidate=candidate)
        self.assertEqual([x["candidate_id"] for x in state["ready"]],["a"])
        self.assertNotIn("holder",state)
        self.assertNotIn("turn_base",state)
        self.assertFalse(hasattr(MERGE_LEASE,"release_lease"))

    def test_non_green_candidate_cannot_enter_ready_queue(self) -> None:
        state=MERGE_LEASE.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=20)
        candidate={"candidate_id":"a","lane":"mrcs","work_item_id":"MRCS-X","pr_number":2,"head_sha":"head-a","prequeue_validation":{"status":"pending","head_sha":"head-a","run_id":"run-a"}}
        with self.assertRaises(MERGE_LEASE.PublicationConflict):
            MERGE_LEASE.submit_ready_candidate(state,expected_generation=20,candidate=candidate)

    def test_ready_queue_is_fifo_without_reserving_future_work(self) -> None:
        state=MERGE_LEASE.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=30)
        for cid,lane in (("a","msas"),("b","mrcs"),("c","mvps")):
            candidate={"candidate_id":cid,"lane":lane,"work_item_id":lane.upper()+"-X","pr_number":30+len(state["ready"]),"head_sha":"head-"+cid,"prequeue_validation":{"status":"green","head_sha":"head-"+cid,"run_id":"run-"+cid}}
            state=MERGE_LEASE.submit_ready_candidate(state,expected_generation=state["generation"],candidate=candidate)
        self.assertEqual([x["candidate_id"] for x in state["ready"]],["a","b","c"])

    def test_integration_gate_binds_only_ready_head_to_fresh_main(self) -> None:
        state=MERGE_LEASE.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=40)
        candidate={"candidate_id":"a","lane":"msas","work_item_id":"MSAS-X","pr_number":4,"head_sha":"head-a","prequeue_validation":{"status":"green","head_sha":"head-a","run_id":"pre-a"}}
        state=MERGE_LEASE.submit_ready_candidate(state,expected_generation=40,candidate=candidate)
        receipt={"candidate_id":"a","candidate_head":"head-a","base_sha":"main-now","status":"green","run_id":"integration-a"}
        self.assertEqual(MERGE_LEASE.validate_integration_authorization(state,candidate_id="a",fresh_main_sha="main-now",pr_head_sha="head-a",integration_receipt=receipt),[])
        errors=MERGE_LEASE.validate_integration_authorization(state,candidate_id="a",fresh_main_sha="main-moved",pr_head_sha="head-a",integration_receipt=receipt)
        self.assertIn(MERGE_LEASE.STALE_INTEGRATION,errors)

    def test_failed_ready_candidate_does_not_strand_following_candidates(self) -> None:
        state=MERGE_LEASE.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=50)
        for cid in ("a","b"):
            candidate={"candidate_id":cid,"lane":"msas","work_item_id":"MSAS-X","pr_number":5,"head_sha":"head-"+cid,"prequeue_validation":{"status":"green","head_sha":"head-"+cid,"run_id":"run-"+cid}}
            state=MERGE_LEASE.submit_ready_candidate(state,expected_generation=state["generation"],candidate=candidate)
        state=MERGE_LEASE.fail_ready_candidate(state,expected_generation=state["generation"],candidate_id="a",reason="integration test failed")
        self.assertEqual([x["candidate_id"] for x in state["ready"]],["b"])
        self.assertEqual(state["history"][-1]["status"],"failed")

    def test_durable_merge_reconciliation_consumes_candidate_without_release_step(self) -> None:
        state=MERGE_LEASE.free_publication_queue("cybalicistjt-stack/multiversal-aioc",generation=60)
        candidate={"candidate_id":"a","lane":"mvps","work_item_id":"MVPS-X","pr_number":6,"head_sha":"head-a","prequeue_validation":{"status":"green","head_sha":"head-a","run_id":"run-a"}}
        state=MERGE_LEASE.submit_ready_candidate(state,expected_generation=60,candidate=candidate)
        state=MERGE_LEASE.reconcile_durable_publication(state,expected_generation=61,candidate_id="a",observed_head_sha="head-a",merge_sha="merge-a")
        self.assertEqual(state["ready"],[])
        self.assertEqual(state["history"][-1]["status"],"published")
        self.assertEqual(state["history"][-1]["merge_sha"],"merge-a")
        self.assertFalse(hasattr(MERGE_LEASE,"recover_completed_turn"))

    def test_lane_state_transport_is_sharded_by_lane(self) -> None:
        path=ROOT / "scripts/ops3_lane_state.py"
        self.assertTrue(path.is_file())
        lane_state=_load("ops3_lane_state", "scripts/ops3_lane_state.py")
        self.assertEqual(lane_state.coordination_branch("msas"),"ops3-lane-state/msas")
        self.assertEqual(lane_state.coordination_branch("mrcs"),"ops3-lane-state/mrcs")
        a=lane_state.initial_state("msas",revision=1,selected_work_item="MSAS-X",attempt_id="MSAS-X-attempt-001")
        b=lane_state.initial_state("mrcs",revision=1,selected_work_item="MRCS-X",attempt_id="MRCS-X-attempt-001")
        a2=lane_state.record_progress(a,expected_revision=1,lane="msas",kind="implementation",evidence="head-a")
        self.assertEqual(a2["revision"],2)
        self.assertEqual(b["revision"],1)
        with self.assertRaises(lane_state.LaneStateConflict):
            lane_state.record_progress(a2,expected_revision=2,lane="mrcs",kind="wrong-lane",evidence="no")

    def test_owner_continue_without_material_progress_enters_visible_stall_recovery(self) -> None:
        checkpoint={"status":"in_progress","execution_guard":{"continue_turns":1,"stall_nudges":0,"material_progress_seq":2,"progress_at_last_owner_command":2,"no_progress_cycles":0,"last_material_progress":{"seq":2,"kind":"validation","evidence":"run 7 failed"},"active_stall":False,"terminal_response_allowed":False,"stop_reason":None},"execution_conformance":{"status":"in_progress","policy_violations":[]}}
        updated=EXECUTION_GUARD.observe_owner_execution_command(checkpoint)
        self.assertTrue(updated["execution_guard"]["active_stall"])
        self.assertIn(EXECUTION_GUARD.NO_MATERIAL_PROGRESS,updated["execution_conformance"]["policy_violations"])
        progressed=EXECUTION_GUARD.record_material_progress(updated,kind="repair",evidence="changed failing signature")
        self.assertFalse(progressed["execution_guard"]["active_stall"])

if __name__ == "__main__":
    unittest.main()
