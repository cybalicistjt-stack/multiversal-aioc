from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROGRAM_DIR = ROOT / "governance" / "application-planning" / "parallel-preimplementation"
BACKLOG_PATH = PROGRAM_DIR / "PPIA_PROGRAM_BACKLOG.json"
PROGRAM_PATH = PROGRAM_DIR / "PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md"
ROADMAP_PATH = ROOT / "governance" / "application-planning" / "APPLICATION_IMPLEMENTATION_ROADMAP.md"
INDEX_PATH = ROOT / "governance" / "ai" / "runtime" / "ROADMAP_INDEX.json"
POINTER_PATH = ROOT / "governance" / "ai" / "runtime" / "CURRENT_WORK_POINTER.json"
STATUS_PATH = ROOT / "governance" / "ai" / "runtime" / "CURRENT_IMPLEMENTATION_STATUS.json"
WORK_STATE_DIR = ROOT / "governance" / "ai" / "work-state"

EXPECTED_IDS = [f"PPIA-{index:02d}" for index in range(1, 17)]
EXPECTED_ORDER = [
    "PPIA-01", "PPIA-02", "PPIA-03", "PPIA-04", "PPIA-05", "PPIA-12",
    "PPIA-07", "PPIA-08", "PPIA-09", "PPIA-10", "PPIA-11", "PPIA-06",
    "PPIA-13", "PPIA-14", "PPIA-15", "PPIA-16",
]
ACTIVE_STATUSES = {"started", "in_progress"}
COMPLETE_STATUSES = {"complete", "completed", "completed_verified"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def checkpoint_for_pointer_entry(entry: dict) -> dict:
    return load_json(ROOT / entry["checkpoint_path"])


def historical_completion_checks() -> None:
    ppia01 = load_json(WORK_STATE_DIR / "PPIA-01-attempt-001.json")
    ppia02 = load_json(WORK_STATE_DIR / "PPIA-02-attempt-001.json")
    ppia03 = load_json(WORK_STATE_DIR / "PPIA-03-attempt-001.json")

    assert ppia01["work_item_id"] == "PPIA-01"
    assert ppia01["attempt_id"] == "PPIA-01-attempt-001"
    assert ppia01["status"] in COMPLETE_STATUSES
    assert ppia01["completed_at"]
    assert ppia01.get("merge_commit") == "f9e2b1fb7c340d27813b09c180b60d34d5fb6f92"
    assert ppia01["owner_decision_required"] is False

    assert ppia02["work_item_id"] == "PPIA-02"
    assert ppia02["attempt_id"] == "PPIA-02-attempt-001"
    assert ppia02["status"] == "completed_verified"
    assert ppia02["completed_at"]
    assert ppia02.get("merge_commit") == "f768345a44a662a5a1981f4cb35d218c926a5cb6"
    assert ppia02["latest_pushed_commit"] == "1909a607bbb3ff57a959ae8cc47058ad2882a4e3"
    assert ppia02["pull_request"] == 219
    assert ppia02["owner_decision_required"] is False
    assert not ppia02["unresolved_failures"]
    assert any("31506614994" in item.get("command", "") and item.get("status") == "passed" for item in ppia02["validation"])

    assert ppia03["work_item_id"] == "PPIA-03"
    assert ppia03["attempt_id"] == "PPIA-03-attempt-001"
    assert ppia03["status"] == "completed_verified"
    assert ppia03["completed_at"] == "2026-08-11T17:38:18+00:00"
    assert ppia03.get("merge_commit") == "ea08234b9d6bcd4cb942c2de964639b330d9511e"
    assert ppia03["latest_pushed_commit"] == "c1e00ebf67fe4c78af2ce6e1dd483bb699706047"
    assert ppia03["pull_request"] == 224
    assert ppia03["owner_decision_required"] is False
    assert not ppia03["unresolved_failures"]
    assert ppia03["active_substep"] is None
    assert any("31518534709" in item.get("command", "") and item.get("status") == "passed" for item in ppia03["validation"])
    assert any("ea08234b9d6bcd4cb942c2de964639b330d9511e" in item.get("value", "") for item in ppia03["evidence"])


def main() -> int:
    backlog = load_json(BACKLOG_PATH)
    index = load_json(INDEX_PATH)
    pointer = load_json(POINTER_PATH)
    status = load_json(STATUS_PATH)
    program = PROGRAM_PATH.read_text(encoding="utf-8")
    roadmap = ROADMAP_PATH.read_text(encoding="utf-8")

    assert backlog["program_id"] == "PPIA"
    assert backlog["version"] == "1.0.0"
    assert backlog["execution_order"] == EXPECTED_ORDER
    tranche_ids = [item["work_item_id"] for item in backlog["tranches"]]
    assert tranche_ids == EXPECTED_IDS
    assert len(set(tranche_ids)) == 16

    current_id = backlog["current_work_item_id"]
    assert current_id in EXPECTED_ORDER
    current_index = EXPECTED_ORDER.index(current_id)
    tranche_by_id = {item["work_item_id"]: item for item in backlog["tranches"]}
    for work_item_id in EXPECTED_ORDER[:current_index]:
        assert tranche_by_id[work_item_id]["status"] in COMPLETE_STATUSES
    current_tranche = tranche_by_id[current_id]
    assert current_tranche["status"] in ACTIVE_STATUSES
    for work_item_id in EXPECTED_ORDER[current_index + 1:]:
        assert tranche_by_id[work_item_id]["status"] == "planned"

    boundaries = backlog["boundaries"]
    assert boundaries["requires_codex"] is False
    assert boundaries["application_runtime_mutation_authorized"] is False
    assert boundaries["a2_activation_authorized"] is False
    assert boundaries["release_authorized"] is False
    assert boundaries["deployment_authorized"] is False
    assert boundaries["tester_access_authorized"] is False
    assert boundaries["canonical_promotion_without_source_evidence_authorized"] is False

    index_ids = {entry["work_item_id"] for entry in index["entries"]}
    assert set(EXPECTED_IDS).issubset(index_ids)
    assert "STAGE-A-A2" in index_ids
    assert "DS-008-working-series" in index_ids

    historical_completion_checks()

    selected = [item for item in pointer["active_attempts"] if item["owner_selected"]]
    assert len(selected) == 1
    selected_entry = selected[0]
    assert pointer["primary_attempt_id"] == selected_entry["attempt_id"]
    assert selected_entry["work_item_id"] == current_id
    checkpoint = checkpoint_for_pointer_entry(selected_entry)
    assert checkpoint["work_item_id"] == current_id
    assert checkpoint["attempt_id"] == selected_entry["attempt_id"]
    assert checkpoint["owner_decision_required"] is False
    assert checkpoint["status"] in ACTIVE_STATUSES

    app_tracks = [item for item in pointer["deferred_tracks"] if item["track"] == "application-implementation"]
    assert len(app_tracks) == 1
    assert app_tracks[0]["next_work_item_id"] == "STAGE-A-A2"
    assert "checkout_runner_blocked" in app_tracks[0]["state"]

    assert status["primary"]["work_item_id"] == current_id
    assert status["primary"]["attempt_id"] == checkpoint["attempt_id"]
    assert status["primary"]["status"] == checkpoint["status"] == selected_entry["status"] == current_tranche["status"]
    assert status["primary"]["active_substep"] == checkpoint["active_substep"]
    assert status["primary"]["next_action"] == checkpoint["next_action"]
    assert status["primary"]["pull_request"] == checkpoint.get("pull_request")
    assert status["primary"]["latest_pushed_commit"] == checkpoint.get("latest_pushed_commit")
    assert status["primary"]["roadmap_projection_pending"] == checkpoint["roadmap_projection_pending"] == selected_entry["roadmap_projection_pending"]

    assert "**Program ID:** PPIA" in program
    for work_item_id in EXPECTED_IDS:
        assert work_item_id in program
        assert work_item_id in roadmap
    assert "**Version:**" in roadmap
    assert "DT-001 through DT-010 Developer Toolbelt is complete" in roadmap
    assert "A2_CHANGED_PATH_SCOPE_v1.0.0.csv" in roadmap
    assert "A2 is not activated" in roadmap

    if checkpoint["roadmap_projection_pending"] is False:
        assert f"**{current_id} — {current_tranche['title']}** is the current owner-approved tranche" in program
        assert f"**{current_id} — {current_tranche['title']}**" in roadmap
    else:
        assert "roadmap" in pointer["selection_reason"].lower()
        assert "pending" in pointer["selection_reason"].lower()

    print("PPIA program validation: PASS")
    print("tranches: 16")
    print(f"completed_before_current: {current_index}")
    print(f"current: {current_id}")
    print(f"current_status: {current_tranche['status']}")
    print(f"roadmap_projection_pending: {str(checkpoint['roadmap_projection_pending']).lower()}")
    print("p3_verified_completion_merge: ea08234b9d6bcd4cb942c2de964639b330d9511e")
    print("a2_activation_authorized: false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
