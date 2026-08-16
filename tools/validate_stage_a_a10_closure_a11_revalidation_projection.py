#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
CHECKPOINT = ROOT / "governance/ai/work-state/STAGE-A-A11-current-revalidation-attempt-001.json"
SUPPLEMENT = ROOT / "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A11_SUPPLEMENT.json"
BOOTSTRAP_AMENDMENT = ROOT / "governance/ai/runtime/BOOTSTRAP_CURRENT_STATE_AMENDMENT_STAGE_A_A11.md"
MILESTONE = ROOT / "governance/application-planning/stage-a-a11/current-revalidation/STAGE_A_A10_CLOSURE_A11_REVALIDATION_MILESTONE.md"
START = ROOT / "governance/application-planning/stage-a-a11/current-revalidation/STAGE_A_A11_CURRENT_REPOSITORY_REVALIDATION_START.md"

A10_IMPLEMENTATION_MERGE = "9744c5223eb41f9cac765f3807a7860ffe0d1143"
A10_CLOSURE_MERGE = "f023c7feab49910b02abccf3ae87fd4b581c64c8"
A11_ATTEMPT = "STAGE-A-A11-current-revalidation-attempt-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require_text(path: Path, *markers: str) -> None:
    text = path.read_text(encoding="utf-8")
    for marker in markers:
        assert marker in text, f"missing marker {marker!r} in {path.relative_to(ROOT)}"


def main() -> int:
    pointer = read_json(POINTER)
    status = read_json(STATUS)
    checkpoint = read_json(CHECKPOINT)
    supplement = read_json(SUPPLEMENT)

    assert pointer["primary_attempt_id"] == A11_ATTEMPT
    selected = [item for item in pointer["active_attempts"] if item.get("owner_selected")]
    assert len(selected) == 1
    assert selected[0]["attempt_id"] == A11_ATTEMPT
    assert selected[0]["status"] == "started"
    assert selected[0]["branch"] == "governance/stage-a-a10-closure-a11-revalidation"
    assert pointer["roadmap_index_supplement"] == "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A11_SUPPLEMENT.json"
    assert pointer["bootstrap_current_state_amendment"] == "governance/ai/runtime/BOOTSTRAP_CURRENT_STATE_AMENDMENT_STAGE_A_A11.md"
    assert pointer["roadmap_milestone_amendment"] == "governance/application-planning/stage-a-a11/current-revalidation/STAGE_A_A10_CLOSURE_A11_REVALIDATION_MILESTONE.md"

    app_track = next(item for item in pointer["deferred_tracks"] if item["track"] == "application-implementation")
    assert app_track["next_work_item_id"] == "STAGE-A-A11"
    assert app_track["state"] == "revalidation_required_not_activated"
    assert A10_IMPLEMENTATION_MERGE in app_track["evidence"]
    assert A10_CLOSURE_MERGE in app_track["evidence"]

    assert status["primary"]["work_item_id"] == "STAGE-A-A11"
    assert status["primary"]["attempt_id"] == A11_ATTEMPT
    assert status["primary"]["status"] == "started"
    assert status["primary"]["owner_decision_required"] is False
    assert status["verified_predecessor"]["work_item_id"] == "STAGE-A-A10"
    assert status["verified_predecessor"]["status"] == "completed_verified"
    assert status["verified_predecessor"]["application_merge_commit"] == A10_IMPLEMENTATION_MERGE
    assert status["verified_predecessor"]["closure_merge_commit"] == A10_CLOSURE_MERGE
    assert status["restrictions"]["a11_activated"] is False

    assert checkpoint["work_item_id"] == "STAGE-A-A11"
    assert checkpoint["attempt_id"] == A11_ATTEMPT
    assert checkpoint["status"] == "started"
    assert checkpoint["application_baseline"] == A10_CLOSURE_MERGE
    assert checkpoint["verified_predecessor"]["implementation_merge_commit"] == A10_IMPLEMENTATION_MERGE
    assert checkpoint["verified_predecessor"]["closure_merge_commit"] == A10_CLOSURE_MERGE
    assert checkpoint["historical_preparation"]["source_slice_count"] == 24
    assert checkpoint["historical_preparation"]["source_fixture_count"] == 72
    assert checkpoint["historical_preparation"]["blocking_source_acceptance_criteria_count"] == 76
    assert checkpoint["historical_preparation"]["preimplementation_handoff"]["blob_sha"] == "fae5f99491012f5272c257d4457535a5a262b7a9"
    assert checkpoint["historical_preparation"]["repository_compatibility_handoff"]["blob_sha"] == "bb35964fd387237b7d342256daa70598afd16bd2"
    assert checkpoint["restrictions"]["a11_activated"] is False
    assert checkpoint["restrictions"]["provider_selected"] is False
    assert checkpoint["restrictions"]["paid_execution_authorized"] is False
    assert checkpoint["restrictions"]["real_user_prompt_collection_authorized"] is False
    assert checkpoint["restrictions"]["autonomous_mutation_authorized"] is False
    assert checkpoint["restrictions"]["release_authorized"] is False
    assert checkpoint["restrictions"]["deployment_authorized"] is False
    assert checkpoint["restrictions"]["canonical_promotion_authorized"] is False

    entries = supplement["entries"]
    assert len(entries) == 1
    a11 = entries[0]
    assert a11["work_item_id"] == "STAGE-A-A11"
    assert a11["dependencies"] == ["STAGE-A-A10"]
    assert a11["track"] == "application-implementation-pre-revalidation"

    require_text(
        START,
        "STARTED — REVALIDATION ONLY / NOT ACTIVATED",
        A10_IMPLEMENTATION_MERGE,
        A10_CLOSURE_MERGE,
        "24 prepared A11 slices",
        "72 prepared deterministic fixtures",
        "76 blocking source acceptance criteria",
        "Do not activate A11",
    )
    require_text(
        MILESTONE,
        "STAGE-A-A10 — World Content Authoring",
        "COMPLETED_VERIFIED",
        A10_IMPLEMENTATION_MERGE,
        A10_CLOSURE_MERGE,
        "STAGE-A-A11 — Contextual AI Interfaces",
        "IMPLEMENTATION NOT ACTIVATED",
    )
    require_text(
        BOOTSTRAP_AMENDMENT,
        "STAGE-A-A10 — World Content Authoring is now `COMPLETED_VERIFIED`",
        A10_IMPLEMENTATION_MERGE,
        A10_CLOSURE_MERGE,
        "STAGE-A-A11 — Contextual AI Interfaces current-repository revalidation",
        "Do not create or activate an A11 application branch",
    )

    print("STAGE-A-A10 CLOSURE / A11 REVALIDATION PROJECTION: PASS")
    print("primary=STAGE-A-A11-current-revalidation-attempt-001 status=started")
    print("a10=completed_verified a11_activated=false provider_selected=false paid_execution=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
