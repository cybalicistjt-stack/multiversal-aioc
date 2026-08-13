from __future__ import annotations

import importlib.util
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
LEGACY_VALIDATOR = PROGRAM_DIR / "validate_ppia_program.py"

EXPECTED_IDS = [f"PPIA-{index:02d}" for index in range(1, 17)]
EXPECTED_ORDER = ["PPIA-01","PPIA-02","PPIA-03","PPIA-04","PPIA-05","PPIA-12","PPIA-07","PPIA-08","PPIA-09","PPIA-10","PPIA-11","PPIA-06","PPIA-13","PPIA-14","PPIA-15","PPIA-16"]
ACTIVE_TRANCHE_STATUSES = {"started", "in_progress"}
UNFINISHED_CHECKPOINT_STATUSES = {"started", "in_progress", "validation_failed", "blocked_non_owner", "blocked_owner", "ready_for_review"}
COMPLETE_STATUSES = {"complete", "completed", "completed_verified"}
FINAL_HEAD = "eede4bfb530056963a4a595faac54515ff151c3b"
FINAL_MERGE = "5b87d57d9b06fbb7427b6fae7ca022509f92a5fe"
FINAL_RUN = "31694048323"
FINAL_PR = 294


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def checkpoint_for_pointer_entry(entry: dict) -> dict:
    return load_json(ROOT / entry["checkpoint_path"])


def run_legacy_historical_checks() -> None:
    spec = importlib.util.spec_from_file_location("ppia_legacy_validator", LEGACY_VALIDATOR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.historical_completion_checks()


def validate_common(backlog: dict, index: dict, pointer: dict, status: dict, program: str, roadmap: str) -> tuple[str, dict, dict]:
    assert backlog["program_id"] == "PPIA" and backlog["version"] == "1.0.0"
    assert backlog["execution_order"] == EXPECTED_ORDER
    tranche_ids = [item["work_item_id"] for item in backlog["tranches"]]
    assert tranche_ids == EXPECTED_IDS and len(set(tranche_ids)) == 16
    tranche_by_id = {item["work_item_id"]: item for item in backlog["tranches"]}

    boundaries = backlog["boundaries"]
    for flag in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        assert boundaries[flag] is False
    assert boundaries["requires_codex"] is False

    index_ids = {entry["work_item_id"] for entry in index["entries"]}
    assert set(EXPECTED_IDS).issubset(index_ids)
    assert "STAGE-A-A2" in index_ids and "DS-008-working-series" in index_ids
    run_legacy_historical_checks()

    assert "**Program ID:** PPIA" in program
    for work_item_id in EXPECTED_IDS:
        assert work_item_id in program and work_item_id in roadmap
    assert "DT-001 through DT-010 Developer Toolbelt is complete" in roadmap
    assert "A2_CHANGED_PATH_SCOPE_v1.0.0.csv" in roadmap and "A2 is not activated" in roadmap

    selected = [item for item in pointer["active_attempts"] if item["owner_selected"]]
    assert len(selected) == 1
    selected_entry = selected[0]
    assert pointer["primary_attempt_id"] == selected_entry["attempt_id"]
    checkpoint = checkpoint_for_pointer_entry(selected_entry)
    assert checkpoint["work_item_id"] == selected_entry["work_item_id"]
    assert checkpoint["attempt_id"] == selected_entry["attempt_id"]
    assert checkpoint["owner_decision_required"] is False

    app_tracks = [item for item in pointer["deferred_tracks"] if item["track"] == "application-implementation"]
    assert len(app_tracks) == 1
    assert app_tracks[0]["next_work_item_id"] == "STAGE-A-A2"
    assert "checkout_runner_blocked" in app_tracks[0]["state"]

    primary = status["primary"]
    assert primary["work_item_id"] == checkpoint["work_item_id"]
    assert primary["attempt_id"] == checkpoint["attempt_id"]
    assert primary["status"] == checkpoint["status"] == selected_entry["status"]
    for field in ("active_substep","next_action","pull_request","latest_pushed_commit","roadmap_projection_pending"):
        assert primary[field] == checkpoint.get(field)
    assert primary["roadmap_projection_pending"] == selected_entry["roadmap_projection_pending"]

    return backlog["current_work_item_id"], tranche_by_id, checkpoint


def validate_active_mode(current_id: str, tranche_by_id: dict, checkpoint: dict, pointer: dict) -> None:
    assert current_id in EXPECTED_ORDER
    current_index = EXPECTED_ORDER.index(current_id)
    for work_item_id in EXPECTED_ORDER[:current_index]:
        assert tranche_by_id[work_item_id]["status"] in COMPLETE_STATUSES
    assert tranche_by_id[current_id]["status"] in ACTIVE_TRANCHE_STATUSES
    for work_item_id in EXPECTED_ORDER[current_index + 1:]:
        assert tranche_by_id[work_item_id]["status"] == "planned"
    assert checkpoint["status"] in UNFINISHED_CHECKPOINT_STATUSES
    assert checkpoint["completed_at"] is None
    if checkpoint["roadmap_projection_pending"]:
        assert "roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower()


def validate_final_mode(current_id: str, tranche_by_id: dict, checkpoint: dict, backlog: dict, pointer: dict) -> None:
    assert current_id == "PPIA-16"
    assert all(tranche_by_id[work_item_id]["status"] in COMPLETE_STATUSES for work_item_id in EXPECTED_ORDER)
    assert tranche_by_id["PPIA-16"]["status"] == "completed_verified"
    assert backlog["status"] == "completed_verified_owner_approved_parallel_work"
    evidence = backlog.get("completion_evidence", {})
    assert evidence == {
        "final_tranche":"PPIA-16",
        "exact_validated_head":FINAL_HEAD,
        "hosted_workflows":"70/70",
        "dedicated_run":FINAL_RUN,
        "pull_request":FINAL_PR,
        "merge_commit":FINAL_MERGE,
        "merge_signature":"verified valid",
    }
    assert checkpoint["work_item_id"] == "PPIA-16"
    assert checkpoint["status"] == "completed_verified"
    assert checkpoint["completed_at"]
    assert checkpoint["active_substep"] is None
    assert checkpoint["latest_pushed_commit"] == FINAL_HEAD
    assert checkpoint["pull_request"] == FINAL_PR
    assert checkpoint["merge_commit"] == FINAL_MERGE
    assert checkpoint["expected_remote_head"] == FINAL_MERGE
    assert checkpoint["unresolved_failures"] == []
    assert any(FINAL_RUN in item.get("evidence", "") and item.get("status") == "passed" for item in checkpoint["validation"])
    assert any(FINAL_MERGE in item.get("value", "") for item in checkpoint["evidence"])
    assert "no automatic successor" in checkpoint["next_action"].lower()
    assert "stage-a-a2" in checkpoint["next_action"].lower()
    assert "design standards" in checkpoint["next_action"].lower()
    if checkpoint["roadmap_projection_pending"]:
        assert "roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower()


def main() -> int:
    backlog = load_json(BACKLOG_PATH)
    index = load_json(INDEX_PATH)
    pointer = load_json(POINTER_PATH)
    status = load_json(STATUS_PATH)
    program = PROGRAM_PATH.read_text(encoding="utf-8")
    roadmap = ROADMAP_PATH.read_text(encoding="utf-8")

    current_id, tranche_by_id, checkpoint = validate_common(backlog, index, pointer, status, program, roadmap)
    if tranche_by_id["PPIA-16"]["status"] == "completed_verified":
        validate_final_mode(current_id, tranche_by_id, checkpoint, backlog, pointer)
        mode = "completed_verified_final_program"
        completed_count = 16
    else:
        validate_active_mode(current_id, tranche_by_id, checkpoint, pointer)
        mode = "active_program"
        completed_count = EXPECTED_ORDER.index(current_id)

    print("PPIA program state validation: PASS")
    print(f"mode: {mode}")
    print(f"current_anchor: {current_id}")
    print(f"completed_count: {completed_count}")
    print("a2_activation_authorized: false")
    print("release_authorized: false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
