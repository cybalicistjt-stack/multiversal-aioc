#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/stage-a-a12/current-revalidation"
RECEIPT = BASE / "STAGE_A_A12_REVALIDATION_COMPLETION_RECEIPT.json"
VERDICT = BASE / "STAGE_A_A12_CURRENT_REPOSITORY_REVALIDATION.md"
CHECKPOINT = ROOT / "governance/ai/work-state/STAGE-A-A12-current-revalidation-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
SUPPLEMENT = ROOT / "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A12_SUPPLEMENT.json"
BOOTSTRAP = ROOT / "governance/ai/runtime/BOOTSTRAP_CURRENT_STATE_AMENDMENT_STAGE_A_A12_REVALIDATION_CLOSURE.md"

APP = "16c8018cc7ae06657cdcd3176d2ee16ad9edb36e"
A11 = "bf54f36737fe02041f02ab44a69f45c3b0b294ac"
HEAD = "4aaea035af7db583ec0f92796c8c0a7305856b32"
RUN = 31935854339
JOB = 95137534214
PR = 333
MERGE = "528b85b469a68b9f7fec7b04a8bcc19cb677abce"
VERDICT_VALUE = "PASS_READY_FOR_BOUNDED_A12_ACTIVATION"


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    receipt = read(RECEIPT)
    cp = read(CHECKPOINT)
    pointer = read(POINTER)
    status = read(STATUS)
    supplement = read(SUPPLEMENT)
    verdict_text = VERDICT.read_text(encoding="utf-8")
    bootstrap_text = BOOTSTRAP.read_text(encoding="utf-8")

    assert receipt["work_item_id"] == "STAGE-A-A12"
    assert receipt["operation"] == "current-repository revalidation"
    assert receipt["state"] == "completed_verified"
    assert receipt["verdict"] == VERDICT_VALUE
    assert receipt["application_baseline"] == APP
    assert receipt["verified_a11_product_merge"] == A11
    assert receipt["validation"]["exact_head"] == HEAD
    assert receipt["validation"]["run_id"] == RUN
    assert receipt["validation"]["job_id"] == JOB
    assert receipt["validation"]["conclusion"] == "success"
    assert receipt["pull_request"] == PR
    assert receipt["merge_commit"] == MERGE
    assert receipt["gap_revalidation"] == {"superseded": 2, "changed": 13, "still_valid": 11, "newly_blocked": 0}
    assert receipt["source_accounting"]["a12_slices"] == 12
    assert receipt["source_accounting"]["blocking_release_gates"] == 22
    assert receipt["source_accounting"]["security_threat_families"] == 30
    assert receipt["source_accounting"]["security_scenarios"] == 90
    assert receipt["source_accounting"]["planned_acceptance_contracts"] == 26
    assert receipt["implementation"]["activated"] is False
    assert receipt["implementation"]["application_branch_created"] is False
    assert receipt["candidate_state"] == {"candidate_built": False, "candidate_validated": False, "release_approved": False}
    assert all(value is False for value in receipt["restrictions"].values())

    assert cp["status"] == "completed_verified"
    assert cp["completed_at"]
    assert cp["active_substep"] is None
    assert cp["latest_pushed_commit"] == HEAD
    assert cp["pull_request"] == PR
    assert cp["roadmap_projection_pending"] is False
    assert cp["revalidation_verdict"] == VERDICT_VALUE
    validation = {row["command"]: row for row in cp["validation"]}
    assert validation["python tools/validate_stage_a_a12_revalidation.py"]["status"] == "passed"
    evidence = {(row["kind"], row["value"]) for row in cp["evidence"]}
    assert ("commit", f"STAGE-A-A12 exact validated commit {HEAD}") in evidence
    assert ("pull_request", "STAGE-A-A12 current-repository revalidation pull request #333") in evidence
    assert any(kind == "ci_run" and str(RUN) in value and str(JOB) in value for kind, value in evidence)
    assert any(kind == "merge" and MERGE in value for kind, value in evidence)
    assert cp["restrictions"]["a12_activated"] is False
    assert cp["restrictions"]["a12_application_branch_created"] is False
    assert cp["restrictions"]["candidate_built_claimed"] is False
    assert cp["restrictions"]["candidate_validated_claimed"] is False
    assert cp["restrictions"]["release_approved"] is False

    assert pointer["primary_attempt_id"] == cp["attempt_id"]
    primary = next(row for row in pointer["active_attempts"] if row["attempt_id"] == cp["attempt_id"])
    assert primary["status"] == "completed_verified"
    assert primary["owner_selected"] is True
    assert primary["roadmap_projection_pending"] is False
    deferred = next(row for row in pointer["deferred_tracks"] if row["track"] == "application-implementation")
    assert deferred["next_work_item_id"] == "STAGE-A-A12"
    assert deferred["state"] == "authorized_not_activated"

    assert status["primary"]["attempt_id"] == cp["attempt_id"]
    assert status["primary"]["status"] == "completed_verified"
    assert status["primary"]["active_substep"] is None
    assert status["primary"]["latest_pushed_commit"] == HEAD
    assert status["primary"]["pull_request"] == PR
    assert status["active_attempt_count"] == 1
    assert status["deferred_track_count"] == 2

    a12 = next(row for row in supplement["entries"] if row["work_item_id"] == "STAGE-A-A12")
    assert a12["revalidation_state"] == "completed_verified"
    assert a12["revalidation_verdict"] == VERDICT_VALUE
    assert a12["revalidation_pull_request"] == PR
    assert a12["revalidation_exact_head"] == HEAD
    assert a12["revalidation_ci_run"] == RUN
    assert a12["revalidation_merge_commit"] == MERGE
    assert a12["implementation_state"] == "authorized_not_activated"

    for marker in (
        "PASS — READY FOR BOUNDED A12 ACTIVATION",
        "Implementation state:** **NOT ACTIVATED",
        "2 superseded, 13 changed, 11 still valid, 0 newly blocked",
        "release_approved",
    ):
        assert marker in verdict_text
    for marker in ("completed_verified", MERGE, "authorized but not activated", "candidate_built", "release_approved"):
        assert marker in bootstrap_text

    print("STAGE-A-A12 REVALIDATION CLOSURE: PASS")
    print(f"exact_head={HEAD} run={RUN} job={JOB} pr={PR} merge={MERGE}")
    print("state=completed_verified implementation=authorized_not_activated candidate_built=false candidate_validated=false release_approved=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
