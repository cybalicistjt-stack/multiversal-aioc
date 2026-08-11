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
CHECKPOINT_PATH = ROOT / "governance" / "ai" / "work-state" / "PPIA-01-attempt-001.json"

EXPECTED_IDS = [f"PPIA-{index:02d}" for index in range(1, 17)]
EXPECTED_ORDER = [
    "PPIA-01", "PPIA-02", "PPIA-03", "PPIA-04", "PPIA-05", "PPIA-12",
    "PPIA-07", "PPIA-08", "PPIA-09", "PPIA-10", "PPIA-11", "PPIA-06",
    "PPIA-13", "PPIA-14", "PPIA-15", "PPIA-16",
]
ACTIVE_STATUSES = {"started", "in_progress"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    backlog = load_json(BACKLOG_PATH)
    index = load_json(INDEX_PATH)
    pointer = load_json(POINTER_PATH)
    status = load_json(STATUS_PATH)
    checkpoint = load_json(CHECKPOINT_PATH)
    program = PROGRAM_PATH.read_text(encoding="utf-8")
    roadmap = ROADMAP_PATH.read_text(encoding="utf-8")

    assert backlog["program_id"] == "PPIA"
    assert backlog["version"] == "1.0.0"
    assert backlog["current_work_item_id"] == "PPIA-01"
    assert backlog["execution_order"] == EXPECTED_ORDER
    tranche_ids = [item["work_item_id"] for item in backlog["tranches"]]
    assert tranche_ids == EXPECTED_IDS
    assert len(set(tranche_ids)) == 16
    current_tranche = backlog["tranches"][0]
    assert current_tranche["status"] in ACTIVE_STATUSES
    assert all(item["status"] == "planned" for item in backlog["tranches"][1:])

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

    assert pointer["primary_attempt_id"] == "PPIA-01-attempt-001"
    selected = [item for item in pointer["active_attempts"] if item["owner_selected"]]
    assert len(selected) == 1
    assert selected[0]["work_item_id"] == "PPIA-01"
    assert selected[0]["checkpoint_path"].endswith("PPIA-01-attempt-001.json")

    app_tracks = [item for item in pointer["deferred_tracks"] if item["track"] == "application-implementation"]
    assert len(app_tracks) == 1
    assert app_tracks[0]["next_work_item_id"] == "STAGE-A-A2"
    assert "checkout_runner_blocked" in app_tracks[0]["state"]

    assert status["primary"]["work_item_id"] == "PPIA-01"
    assert checkpoint["work_item_id"] == "PPIA-01"
    assert checkpoint["attempt_id"] == "PPIA-01-attempt-001"
    assert checkpoint["owner_decision_required"] is False
    assert checkpoint["status"] in ACTIVE_STATUSES
    assert status["primary"]["status"] == checkpoint["status"] == selected[0]["status"] == current_tranche["status"]
    assert status["primary"]["active_substep"] == checkpoint["active_substep"]
    assert status["primary"]["next_action"] == checkpoint["next_action"]
    assert status["primary"]["pull_request"] == checkpoint["pull_request"]
    assert status["primary"]["latest_pushed_commit"] == checkpoint["latest_pushed_commit"]

    assert "**Program ID:** PPIA" in program
    for work_item_id in EXPECTED_IDS:
        assert work_item_id in program
        assert work_item_id in roadmap
    assert "**Version:** 2.3.0" in roadmap
    assert "DT-001 through DT-010 Developer Toolbelt is complete" in roadmap
    assert "A2_CHANGED_PATH_SCOPE_v1.0.0.csv" in roadmap
    assert "A2 is not activated" in roadmap

    print("PPIA program validation: PASS")
    print("tranches: 16")
    print("current: PPIA-01")
    print(f"current_status: {current_tranche['status']}")
    print("a2_activation_authorized: false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
