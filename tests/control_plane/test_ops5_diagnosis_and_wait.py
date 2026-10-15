"""Regression for MTLC-02 wait/conformance ambiguity; no new lane state."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import ops4_execution_guard as guard


def checkpoint():
    return {
        "work_item_id": "MTLC-02", "attempt_id": "MTLC-02-attempt-001",
        "status": "in_progress", "implementation_authority": True,
        "implementation_branch": "work/mtlc-02",
        "execution_guard": {"continue_turns": 1, "stall_nudges": 0,
                            "terminal_response_allowed": False, "stop_reason": None},
        "execution_conformance": {"status": "in_progress", "policy_violations": []},
    }


def handoff():
    return {
        "candidate_head": "a" * 40,
        "workflow": {"id": 38625520341, "head_sha": "a" * 40,
                     "status": "in_progress", "conclusion": None},
        "independent_work_remaining": False,
        "resume_action": "Read this exact run once; advance on success or diagnose its failure.",
    }


def assessed(classification="legitimate_wait", confidence="confirmed"):
    c = checkpoint()
    c["execution_guard"].update(continue_turns=2, stall_nudges=1)
    c["execution_conformance"].update(status="conforming", reentry_assessment={
        "continue_turns": 2, "stall_nudges": 1,
        "classification": classification, "confidence": confidence,
        "evidence": "Prior response handed off exact run 38625520341 with no independent work left.",
    })
    return c


class DiagnosisAndWaitTests(unittest.TestCase):
    def test_confirmed_wait_reentry_is_not_automatically_assistant_nonconformance(self):
        self.assertEqual(guard.validate_execution_conformance(assessed()), [])

    def test_unassessed_or_stale_counts_cannot_claim_conformance(self):
        for mutate in (lambda c: c["execution_conformance"].pop("reentry_assessment"),
                       lambda c: c["execution_guard"].update(continue_turns=3),
                       lambda c: c["execution_conformance"]["reentry_assessment"].update(evidence="")):
            c = assessed()
            mutate(c)
            with self.subTest(c=c):
                self.assertIn(guard.MULTI_CONTINUE, guard.validate_execution_conformance(c))

    def test_probable_or_unresolved_cause_does_not_certify_conformance(self):
        for kind, confidence in (("legitimate_wait", "probable"),
                                 ("unresolved", "unresolved"),
                                 ("premature_stop", "confirmed"),
                                 ("mixed", "confirmed")):
            with self.subTest(kind=kind, confidence=confidence):
                self.assertIn(guard.MULTI_CONTINUE,
                              guard.validate_execution_conformance(assessed(kind, confidence)))

    def test_unresolved_assessment_stays_unresolved_without_inventing_blame(self):
        c = assessed("unresolved", "unresolved")
        c["execution_conformance"]["status"] = "unresolved"
        before = deepcopy(c)
        self.assertEqual(guard.validate_execution_conformance(c), [])
        self.assertEqual(c, before)
        self.assertEqual(c["execution_conformance"]["policy_violations"], [])

    def test_historical_nonconformance_is_preserved(self):
        c = assessed("premature_stop")
        c["execution_conformance"].update(status="nonconforming_recovered",
            policy_violations=[guard.MULTI_CONTINUE, guard.STALL_NUDGE, guard.NONTERMINAL])
        before = deepcopy(c)
        self.assertEqual(guard.validate_execution_conformance(c), [])
        self.assertEqual(c, before)

    def test_resuming_a_valid_wait_does_not_invent_stall_or_material_progress(self):
        c = checkpoint()
        c["execution_guard"].update(material_progress_seq=2, progress_at_last_owner_command=2,
            no_progress_cycles=0, active_stall=False,
            last_material_progress={"seq": 2, "kind": "candidate", "evidence": "candidate prepared"})
        result = guard.observe_owner_execution_command(c, prior_wait_handoff=handoff())
        self.assertFalse(result["execution_guard"]["active_stall"])
        self.assertEqual(result["execution_guard"]["material_progress_seq"], 2)
        self.assertEqual(result["execution_guard"]["continue_turns"], 2)
        self.assertNotIn(guard.NO_MATERIAL_PROGRESS, result["execution_conformance"]["policy_violations"])
        invalid = handoff()
        invalid["independent_work_remaining"] = True
        result = guard.observe_owner_execution_command(c, prior_wait_handoff=invalid)
        self.assertTrue(result["execution_guard"]["active_stall"])

    def test_wait_handoff_preserves_in_progress_lane_and_is_not_completion(self):
        c = checkpoint()
        lane = {"execution_status": "in_progress", "terminal": False}
        before = deepcopy((c, lane))
        self.assertEqual(guard.validate_checkpoint(c, lane_state=lane, wait_handoff=handoff()), [])
        self.assertIn(guard.NONTERMINAL, guard.validate_checkpoint(c, lane_state=lane, terminal_response=True))
        self.assertEqual((c, lane), before)

    def test_wait_rejects_remaining_work_stale_head_and_terminal_runs(self):
        changes = [
            {"independent_work_remaining": True}, {"resume_action": ""},
            {"candidate_head": "b" * 40},
            {"workflow": {"id": 1, "head_sha": "a" * 40, "status": "completed", "conclusion": "success"}},
            {"workflow": {"id": 1, "head_sha": "a" * 40, "status": "completed", "conclusion": "failure"}},
            {"workflow": {"id": 1, "head_sha": "a" * 40, "status": "completed", "conclusion": "cancelled"}},
            {"workflow": {"id": 1, "head_sha": "a" * 40, "status": "waiting", "conclusion": None}},
        ]
        for change in changes:
            h = handoff()
            h.update(change)
            with self.subTest(change=change):
                self.assertTrue(guard.validate_checkpoint(checkpoint(), wait_handoff=h))

    def test_wait_cannot_bypass_lane_projection_drift(self):
        c = checkpoint()
        lane = {"selected_work_item": "MTLC-02", "attempt_id": c["attempt_id"],
                "execution_status": "in_progress", "implementation_branch": c["implementation_branch"]}
        current = {"lanes": {"mtlc": {"selected_work_item": "MTLC-03"}}}
        self.assertIn("OPS4.LANE_PROJECTION_DRIFT", guard.validate_checkpoint(
            c, lane_state=lane, current=current, lane_id="mtlc", wait_handoff=handoff()))

    def test_cancelled_and_skipped_outcomes_require_inspection_not_failure_attribution(self):
        for conclusion in ("cancelled", "skipped"):
            with self.subTest(conclusion=conclusion):
                self.assertEqual(guard.classify_workflow_observation(None,
                    {"status": "completed", "conclusion": conclusion},
                    independent_work_remaining=False), "inspect_terminal_outcome")
        self.assertEqual(guard.classify_workflow_observation(None,
            {"status": "completed", "conclusion": "failure"},
            independent_work_remaining=False), "diagnose_failure")

    def test_cli_wait_is_distinct_from_terminal_response(self):
        with tempfile.TemporaryDirectory() as folder:
            c, h = Path(folder) / "checkpoint.json", Path(folder) / "handoff.json"
            c.write_text(json.dumps(checkpoint()))
            h.write_text(json.dumps(handoff()))
            command = [sys.executable, str(ROOT / "scripts/ops4_execution_guard.py"), str(c)]
            valid = subprocess.run(command + ["--wait-handoff", str(h)], capture_output=True, text=True)
            self.assertEqual(valid.returncode, 0, valid.stdout + valid.stderr)
            invalid = subprocess.run(command + ["--terminal-response", "--wait-handoff", str(h)], capture_output=True)
            self.assertNotEqual(invalid.returncode, 0)
            h.write_text("null")
            invalid = subprocess.run(command + ["--wait-handoff", str(h)], capture_output=True)
            self.assertNotEqual(invalid.returncode, 0)


if __name__ == "__main__":
    unittest.main()
