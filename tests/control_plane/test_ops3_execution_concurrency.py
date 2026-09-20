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
PUBLICATION = _load("ops3_merge_lease", "scripts/ops3_merge_lease.py")
LANE_STATE = _load("ops3_lane_state", "scripts/ops3_lane_state.py")

class Ops3ExecutionConcurrencyTests(unittest.TestCase):
    def test_terminal_response_fails_while_bounded_continue_is_in_progress(self) -> None:
        checkpoint={"status":"in_progress","execution_guard":{"continue_turns":1,"stall_nudges":0,"terminal_response_allowed":False,"stop_reason":None},"execution_conformance":{"status":"in_progress","policy_violations":[]}}
        self.assertIn("OPS3.NONTERMINAL_RESPONSE", EXECUTION_GUARD.validate_terminal_response(checkpoint))

    def test_multi_continue_must_be_recorded_as_process_violation(self) -> None:
        checkpoint={"status":"completed_verified","execution_guard":{"continue_turns":4,"stall_nudges":2,"terminal_response_allowed":True,"stop_reason":{"kind":"completed","evidence":"verified closeout"}},"execution_conformance":{"status":"conforming","policy_violations":[]}}
        errors=EXECUTION_GUARD.validate_execution_conformance(checkpoint)
        self.assertIn("OPS3.MULTI_CONTINUE_UNRECORDED", errors)
        self.assertIn("OPS3.STALL_NUDGE_UNRECORDED", errors)

    def candidate(self, cid: str, lane: str = "msas") -> dict:
        return {
            "candidate_id":cid,
            "lane":lane,
            "work_item_id":lane.upper()+"-X",
            "pr_number":10,
            "head_sha":"head-"+cid,
            "prequeue_validation":{"status":"green","head_sha":"head-"+cid,"run_id":"pre-"+cid},
        }

    def test_ready_candidates_enter_order_only_after_green_prequeue_validation(self) -> None:
        state=PUBLICATION.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=10)
        state=PUBLICATION.submit_ready_candidate(state,expected_generation=10,candidate=self.candidate("a"))
        self.assertEqual([x["candidate_id"] for x in state["ready"]],["a"])
        self.assertNotIn("holder",state)
        self.assertNotIn("turn_base",state)
        self.assertFalse(hasattr(PUBLICATION,"release_lease"))

    def test_non_green_candidate_cannot_enter_ready_queue(self) -> None:
        state=PUBLICATION.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=20)
        candidate=self.candidate("a")
        candidate["prequeue_validation"]["status"]="pending"
        with self.assertRaises(PUBLICATION.PublicationConflict):
            PUBLICATION.submit_ready_candidate(state,expected_generation=20,candidate=candidate)

    def test_ready_queue_is_fifo_without_reserving_future_work(self) -> None:
        state=PUBLICATION.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=30)
        for cid,lane in (("a","gpr"),("b","mrcs"),("c","oarc")):
            state=PUBLICATION.submit_ready_candidate(state,expected_generation=state["generation"],candidate=self.candidate(cid,lane))
        self.assertEqual([x["candidate_id"] for x in state["ready"]],["a","b","c"])

    def test_integration_gate_binds_ready_head_to_fresh_main(self) -> None:
        state=PUBLICATION.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=40)
        state=PUBLICATION.submit_ready_candidate(state,expected_generation=40,candidate=self.candidate("a"))
        receipt={"candidate_id":"a","candidate_head":"head-a","base_sha":"main-now","status":"green","run_id":"integration-a"}
        self.assertEqual(PUBLICATION.validate_integration_authorization(state,candidate_id="a",fresh_main_sha="main-now",pr_head_sha="head-a",integration_receipt=receipt),[])
        errors=PUBLICATION.validate_integration_authorization(state,candidate_id="a",fresh_main_sha="main-moved",pr_head_sha="head-a",integration_receipt=receipt)
        self.assertIn(PUBLICATION.STALE_INTEGRATION,errors)

    def test_only_ready_head_can_merge(self) -> None:
        state=PUBLICATION.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=45)
        state=PUBLICATION.submit_ready_candidate(state,expected_generation=45,candidate=self.candidate("a"))
        state=PUBLICATION.submit_ready_candidate(state,expected_generation=46,candidate=self.candidate("b","mrcs"))
        receipt={"candidate_id":"b","candidate_head":"head-b","base_sha":"main-now","status":"green","run_id":"integration-b"}
        errors=PUBLICATION.validate_integration_authorization(state,candidate_id="b",fresh_main_sha="main-now",pr_head_sha="head-b",integration_receipt=receipt)
        self.assertIn(PUBLICATION.QUEUE_ORDER,errors)

    def test_failed_ready_candidate_does_not_strand_followers(self) -> None:
        state=PUBLICATION.free_publication_queue("cybalicistjt-stack/Multiversal-app",generation=50)
        state=PUBLICATION.submit_ready_candidate(state,expected_generation=50,candidate=self.candidate("a"))
        state=PUBLICATION.submit_ready_candidate(state,expected_generation=51,candidate=self.candidate("b","mrcs"))
        state=PUBLICATION.fail_ready_candidate(state,expected_generation=52,candidate_id="a",reason="integration test failed")
        self.assertEqual([x["candidate_id"] for x in state["ready"]],["b"])
        self.assertEqual(state["history"][-1]["status"],"failed")

    def test_durable_merge_consumes_candidate_without_release_or_recovery(self) -> None:
        state=PUBLICATION.free_publication_queue("cybalicistjt-stack/multiversal-aioc",generation=60)
        state=PUBLICATION.submit_ready_candidate(state,expected_generation=60,candidate=self.candidate("a","oarc"))
        state=PUBLICATION.reconcile_durable_publication(state,expected_generation=61,candidate_id="a",observed_head_sha="head-a",merge_sha="merge-a")
        self.assertEqual(state["ready"],[])
        self.assertEqual(state["history"][-1]["status"],"published")
        self.assertEqual(state["history"][-1]["merge_sha"],"merge-a")
        self.assertFalse(hasattr(PUBLICATION,"recover_completed_turn"))

    def test_direct_protected_main_write_is_rejected(self) -> None:
        state=PUBLICATION.free_publication_queue("cybalicistjt-stack/multiversal-aioc",generation=70)
        self.assertEqual(
            PUBLICATION.validate_protected_main_write(state,target_repo="cybalicistjt-stack/multiversal-aioc",fresh_main_sha="main",mutation_kind="contents_api"),
            [PUBLICATION.DIRECT_MAIN_MUTATION],
        )

    def test_lane_state_transport_is_sharded_by_lane(self) -> None:
        self.assertEqual(LANE_STATE.coordination_branch("gpr"),"ops3-lane-state/gpr")
        self.assertEqual(LANE_STATE.coordination_branch("mrcs"),"ops3-lane-state/mrcs")
        a=LANE_STATE.initial_state("gpr",revision=1,selected_work_item="GPR-X",attempt_id="GPR-X-attempt-001")
        b=LANE_STATE.initial_state("mrcs",revision=1,selected_work_item="MRCS-X",attempt_id="MRCS-X-attempt-001")
        a2=LANE_STATE.start_execution(a,expected_revision=1,lane="gpr",implementation_branch="work/gpr-x",evidence="owner Continue")
        self.assertEqual(a2["revision"],2)
        self.assertEqual(b["revision"],1)
        with self.assertRaises(LANE_STATE.LaneStateConflict):
            LANE_STATE.mark_prequeue_green(a2,expected_revision=2,lane="mrcs",candidate_head="head-a",validation_run="run-a")

    def test_lane_can_start_without_mutating_global_selector(self) -> None:
        state=LANE_STATE.initial_state("oarc",revision=5,selected_work_item="OARC-12",attempt_id="OARC-12-attempt-001")
        started=LANE_STATE.start_execution(state,expected_revision=5,lane="oarc",implementation_branch="work/oarc-12",evidence="owner Continue")
        self.assertEqual(started["execution_status"],"in_progress")
        self.assertEqual(started["implementation_branch"],"work/oarc-12")
        self.assertEqual(started["selected_work_item"],"OARC-12")

    def test_execution_guard_rejects_instrumentation_only_progress_receipts(self) -> None:
        checkpoint={"status":"in_progress","execution_guard":{"material_progress_seq":1,"progress_at_last_owner_command":0,"no_progress_cycles":0,"last_material_progress":{"seq":1,"kind":"started","evidence":"started"},"active_stall":False},"execution_conformance":{"status":"in_progress","policy_violations":[]}}
        for kind in ("status_check","linux_green","windows_green","artifact_inspected","queue_submitted","merge_verified","queue_reconciled","closeout_pr_opened"):
            with self.subTest(kind=kind):
                with self.assertRaisesRegex(ValueError, EXECUTION_GUARD.OVERINSTRUMENTATION):
                    EXECUTION_GUARD.record_material_progress(checkpoint,kind=kind,evidence="mechanical transition")
        updated=EXECUTION_GUARD.record_material_progress(checkpoint,kind="causal_repair",evidence="failure signature changed after bounded repair")
        self.assertEqual(updated["execution_guard"]["material_progress_seq"],2)

    def test_owner_continue_without_material_progress_enters_visible_stall_recovery(self) -> None:
        checkpoint={"status":"in_progress","execution_guard":{"continue_turns":1,"stall_nudges":0,"material_progress_seq":2,"progress_at_last_owner_command":2,"no_progress_cycles":0,"last_material_progress":{"seq":2,"kind":"validation","evidence":"run 7 failed"},"active_stall":False,"terminal_response_allowed":False,"stop_reason":None},"execution_conformance":{"status":"in_progress","policy_violations":[]}}
        updated=EXECUTION_GUARD.observe_owner_execution_command(checkpoint)
        self.assertTrue(updated["execution_guard"]["active_stall"])
        self.assertIn(EXECUTION_GUARD.NO_MATERIAL_PROGRESS,updated["execution_conformance"]["policy_violations"])
        progressed=EXECUTION_GUARD.record_material_progress(updated,kind="repair",evidence="changed failing signature")
        self.assertFalse(progressed["execution_guard"]["active_stall"])

    def test_lane_state_has_no_generic_activity_log_writer(self) -> None:
        self.assertFalse(hasattr(LANE_STATE, "record_progress"))
        self.assertFalse(hasattr(LANE_STATE, "complete_execution"))

    def test_lane_state_uses_three_ordinary_attempt_milestones_only(self) -> None:
        state=LANE_STATE.initial_state("mrcs",revision=10,selected_work_item="MRCS-04",attempt_id="MRCS-04-attempt-001")
        state=LANE_STATE.start_execution(state,expected_revision=10,lane="mrcs",implementation_branch="work/mrcs-04",evidence="owner Continue")
        self.assertEqual(state["execution_status"],"in_progress")
        self.assertEqual(state["progress_seq"],1)

        state=LANE_STATE.mark_prequeue_green(
            state,expected_revision=11,lane="mrcs",
            candidate_head="head-green",validation_run="run-green",
        )
        self.assertEqual(state["execution_status"],"prequeue_green")
        self.assertEqual(state["progress_seq"],2)
        self.assertEqual(state["prequeue_green"],{"candidate_head":"head-green","validation_run":"run-green"})

        state=LANE_STATE.mark_published(
            state,expected_revision=12,lane="mrcs",
            candidate_head="head-green",merge_sha="merge-app",ready_candidate_id="MRCS-04-app-001",
        )
        self.assertEqual(state["execution_status"],"published")
        self.assertEqual(state["progress_seq"],3)
        self.assertEqual(state["publication"]["merge_sha"],"merge-app")

    def test_successor_reseed_is_deterministic_and_resets_progress(self) -> None:
        state=LANE_STATE.initial_state("oarc",revision=20,selected_work_item="OARC-13",attempt_id="OARC-13-attempt-001")
        state=LANE_STATE.start_execution(state,expected_revision=20,lane="oarc",implementation_branch="work/oarc-13",evidence="owner Continue")
        state=LANE_STATE.mark_prequeue_green(state,expected_revision=21,lane="oarc",candidate_head="h",validation_run="r")
        state=LANE_STATE.mark_published(state,expected_revision=22,lane="oarc",candidate_head="h",merge_sha="m",ready_candidate_id="OARC-13-app-001")
        next_state=LANE_STATE.reseed_successor(
            state,
            expected_revision=23,
            lane="oarc",
            successor_work_item="OARC-14",
            successor_attempt_id="OARC-14-attempt-001",
            closeout_merge_sha="closeout",
            closeout_validation_run="closeout-run",
            closeout_ready_candidate_id="OARC-13-closeout-001",
        )
        self.assertEqual(next_state["selected_work_item"],"OARC-14")
        self.assertEqual(next_state["attempt_id"],"OARC-14-attempt-001")
        self.assertEqual(next_state["execution_status"],"selected_not_started")
        self.assertEqual(next_state["implementation_branch"],None)
        self.assertEqual(next_state["progress_seq"],0)
        self.assertEqual(next_state["last_progress"],None)
        self.assertEqual(next_state["last_completed"]["work_item_id"],"OARC-13")
        self.assertEqual(next_state["last_completed"]["application_merge_sha"],"m")
        self.assertEqual(next_state["last_completed"]["closeout_merge_sha"],"closeout")

    def test_micro_transition_kinds_are_not_lane_state_api(self) -> None:
        forbidden={
            "linux_green","windows_green","cross_platform_green","pr_opened","ci_queued",
            "ci_running","artifact_inspected","queue_submitted","fresh_main_read",
            "merge_prepared","merge_verified","queue_reconciled","closeout_pr_opened",
            "closeout_prequeue_green",
        }
        public={name for name in dir(LANE_STATE) if not name.startswith("_")}
        self.assertTrue(forbidden.isdisjoint(public))


if __name__ == "__main__":
    unittest.main()
