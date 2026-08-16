#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKPOINT = ROOT / "governance/ai/work-state/STAGE-A-A11-current-revalidation-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
RECEIPT = ROOT / "governance/application-planning/stage-a-a11/current-revalidation/STAGE_A_A11_REVALIDATION_COMPLETION_RECEIPT.json"

EXACT_HEAD = "a1b969af8520f6db8bb9dde7a0379a021877ac0b"
MERGE = "79d7ee4076ffdd6c2599d07879da515b4c0869ff"
RUN = 31919318218
JOB = 95096456952


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    cp = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)
    receipt = load(RECEIPT)

    assert cp["work_item_id"] == "STAGE-A-A11"
    assert cp["attempt_id"] == "STAGE-A-A11-current-revalidation-attempt-001"
    assert cp["status"] == "completed_verified"
    assert cp["completed_at"]
    assert cp["active_substep"] is None
    assert cp["latest_pushed_commit"] == EXACT_HEAD
    assert cp["expected_remote_head"] == MERGE
    assert cp["pull_request"] == 330
    assert cp["merge_commit"] == MERGE
    assert cp["unresolved_failures"] == []
    assert cp["owner_decision_required"] is False
    assert cp["roadmap_projection_pending"] is False
    assert cp["revalidation_verdict"] == "PASS_READY_FOR_BOUNDED_A11_ACTIVATION"
    validation = {row["command"]: row for row in cp["validation"]}
    row = validation["python tools/validate_stage_a_a11_revalidation.py"]
    assert row["status"] == "passed"
    assert str(RUN) in row["evidence"] and EXACT_HEAD in row["evidence"]

    scoped = [row for row in cp["evidence"] if "STAGE-A-A11" in row["value"]]
    kinds = {row["kind"] for row in scoped}
    assert {"commit", "pull_request", "ci_run", "merge"}.issubset(kinds)
    evidence_text = json.dumps(scoped)
    for marker in (EXACT_HEAD, str(RUN), str(JOB), MERGE, "#330"):
        assert marker in evidence_text

    for flag in (
        "a11_activated", "a11_application_branch_created", "a12_activated", "provider_selected",
        "provider_credentials_authorized", "paid_execution_authorized", "billing_integration_authorized",
        "budget_commitment_authorized", "real_user_prompt_collection_authorized",
        "real_user_transcript_retention_authorized", "real_user_evaluation_corpus_authorized",
        "semantic_vector_remote_ai_search_baseline_authorized", "autonomous_mutation_authorized",
        "autonomous_approval_authorized", "autonomous_publication_authorized", "hidden_reveal_authorized",
        "combat_resolution_authorized", "release_authorized", "deployment_authorized",
        "canonical_promotion_authorized",
    ):
        assert cp["restrictions"][flag] is False, flag

    assert pointer["primary_attempt_id"] == cp["attempt_id"]
    selected = [row for row in pointer["active_attempts"] if row.get("owner_selected")]
    assert len(selected) == 1
    assert selected[0]["attempt_id"] == cp["attempt_id"]
    assert selected[0]["status"] == "completed_verified"
    app = next(row for row in pointer["deferred_tracks"] if row["track"] == "application-implementation")
    assert app["next_work_item_id"] == "STAGE-A-A11"
    assert app["state"] == "authorized_not_activated"
    assert MERGE in app["evidence"]

    primary = status["primary"]
    assert primary["attempt_id"] == cp["attempt_id"]
    assert primary["status"] == "completed_verified"
    assert primary["active_substep"] is None
    assert primary["latest_pushed_commit"] == EXACT_HEAD
    assert primary["pull_request"] == 330
    assert status["active_attempt_count"] == 1

    assert receipt["state"] == "completed_verified"
    assert receipt["revalidation_exact_head"] == EXACT_HEAD
    assert receipt["revalidation_pull_request"] == 330
    assert receipt["focused_ci"]["run_id"] == RUN
    assert receipt["focused_ci"]["job_id"] == JOB
    assert receipt["focused_ci"]["conclusion"] == "success"
    assert receipt["revalidation_merge"]["sha"] == MERGE
    assert receipt["revalidation_merge"]["signature_verified"] is True
    assert receipt["verdict"] == "PASS_READY_FOR_BOUNDED_A11_ACTIVATION"
    assert receipt["source_accounting"] == {
        "slices": 24,
        "fixtures": 72,
        "blocking_acceptance_keys": 76,
        "planned_provider_neutral_contracts": 26,
        "historical_gap_records": 24,
        "gap_dispositions": {"still_valid": 18, "changed": 4, "superseded": 2, "newly_blocked": 0},
    }
    assert receipt["authority_outcome"]["a11_revalidation_completed_verified"] is True
    assert receipt["authority_outcome"]["a11_implementation_authorized_for_bounded_activation_setup"] is True
    assert receipt["authority_outcome"]["a11_activated"] is False

    print("STAGE-A-A11 REVALIDATION CLOSURE: PASS")
    print(f"exact_head={EXACT_HEAD} run={RUN} merge={MERGE}")
    print("state=completed_verified implementation=authorized_not_activated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
