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
EXPECTED_ORDER = ["PPIA-01","PPIA-02","PPIA-03","PPIA-04","PPIA-05","PPIA-12","PPIA-07","PPIA-08","PPIA-09","PPIA-10","PPIA-11","PPIA-06","PPIA-13","PPIA-14","PPIA-15","PPIA-16"]
ACTIVE_STATUSES = {"started", "in_progress"}
COMPLETE_STATUSES = {"complete", "completed", "completed_verified"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def checkpoint_for_pointer_entry(entry: dict) -> dict:
    return load_json(ROOT / entry["checkpoint_path"])


def historical_completion_checks() -> None:
    p1 = load_json(WORK_STATE_DIR / "PPIA-01-attempt-001.json")
    p2 = load_json(WORK_STATE_DIR / "PPIA-02-attempt-001.json")
    p3 = load_json(WORK_STATE_DIR / "PPIA-03-attempt-001.json")
    p4 = load_json(WORK_STATE_DIR / "PPIA-04-attempt-001.json")
    p5 = load_json(WORK_STATE_DIR / "PPIA-05-attempt-001.json")

    assert p1["status"] in COMPLETE_STATUSES and p1.get("merge_commit") == "f9e2b1fb7c340d27813b09c180b60d34d5fb6f92"
    assert p2["status"] == "completed_verified" and p2.get("merge_commit") == "f768345a44a662a5a1981f4cb35d218c926a5cb6"
    assert p2["latest_pushed_commit"] == "1909a607bbb3ff57a959ae8cc47058ad2882a4e3" and p2["pull_request"] == 219
    assert p3["status"] == "completed_verified" and p3.get("merge_commit") == "ea08234b9d6bcd4cb942c2de964639b330d9511e"
    assert p3["latest_pushed_commit"] == "c1e00ebf67fe4c78af2ce6e1dd483bb699706047" and p3["pull_request"] == 224
    assert p4["status"] == "completed_verified" and p4.get("merge_commit") == "e8ec662534820e53fcb8a7d958c0946f494faefd"
    assert p4["latest_pushed_commit"] == "a821f53794d675e73ae71d6c02d577141981ba22" and p4["pull_request"] == 229
    assert p5["status"] == "completed_verified" and p5.get("merge_commit") == "0ffaa34ef15f9a7e4b77776688c6be3fc3047446"
    assert p5["latest_pushed_commit"] == "e6e2bcfd0f22f537a73721dfd8069531bd1af24c" and p5["pull_request"] == 234
    assert p5["active_substep"] is None and not p5["unresolved_failures"] and p5["owner_decision_required"] is False
    assert any("31529821441" in item.get("command", "") and item.get("status") == "passed" for item in p5["validation"])
    assert any("0ffaa34ef15f9a7e4b77776688c6be3fc3047446" in item.get("value", "") for item in p5["evidence"])


def main() -> int:
    backlog = load_json(BACKLOG_PATH)
    index = load_json(INDEX_PATH)
    pointer = load_json(POINTER_PATH)
    status = load_json(STATUS_PATH)
    program = PROGRAM_PATH.read_text(encoding="utf-8")
    roadmap = ROADMAP_PATH.read_text(encoding="utf-8")

    assert backlog["program_id"] == "PPIA" and backlog["version"] == "1.0.0"
    assert backlog["execution_order"] == EXPECTED_ORDER
    tranche_ids = [item["work_item_id"] for item in backlog["tranches"]]
    assert tranche_ids == EXPECTED_IDS and len(set(tranche_ids)) == 16

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
    for flag in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        assert boundaries[flag] is False
    assert boundaries["requires_codex"] is False

    index_ids = {entry["work_item_id"] for entry in index["entries"]}
    assert set(EXPECTED_IDS).issubset(index_ids) and "STAGE-A-A2" in index_ids and "DS-008-working-series" in index_ids
    historical_completion_checks()

    selected = [item for item in pointer["active_attempts"] if item["owner_selected"]]
    assert len(selected) == 1
    selected_entry = selected[0]
    assert pointer["primary_attempt_id"] == selected_entry["attempt_id"]
    assert selected_entry["work_item_id"] == current_id
    checkpoint = checkpoint_for_pointer_entry(selected_entry)
    assert checkpoint["work_item_id"] == current_id and checkpoint["attempt_id"] == selected_entry["attempt_id"]
    assert checkpoint["owner_decision_required"] is False and checkpoint["status"] in ACTIVE_STATUSES

    app_tracks = [item for item in pointer["deferred_tracks"] if item["track"] == "application-implementation"]
    assert len(app_tracks) == 1 and app_tracks[0]["next_work_item_id"] == "STAGE-A-A2" and "checkout_runner_blocked" in app_tracks[0]["state"]

    primary = status["primary"]
    assert primary["work_item_id"] == current_id and primary["attempt_id"] == checkpoint["attempt_id"]
    assert primary["status"] == checkpoint["status"] == selected_entry["status"] == current_tranche["status"]
    for field in ("active_substep","next_action","pull_request","latest_pushed_commit","roadmap_projection_pending"):
        assert primary[field] == checkpoint.get(field)
    assert primary["roadmap_projection_pending"] == selected_entry["roadmap_projection_pending"]

    assert "**Program ID:** PPIA" in program
    for work_item_id in EXPECTED_IDS:
        assert work_item_id in program and work_item_id in roadmap
    assert "DT-001 through DT-010 Developer Toolbelt is complete" in roadmap
    assert "A2_CHANGED_PATH_SCOPE_v1.0.0.csv" in roadmap and "A2 is not activated" in roadmap
    if checkpoint["roadmap_projection_pending"]:
        assert "roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower()

    print("PPIA program validation: PASS")
    print(f"current: {current_id}")
    print(f"completed_before_current: {current_index}")
    print("p5_verified_completion_merge: 0ffaa34ef15f9a7e4b77776688c6be3fc3047446")
    print("a2_activation_authorized: false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
