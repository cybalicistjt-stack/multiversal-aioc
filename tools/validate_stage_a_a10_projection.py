#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
INDEX = ROOT / "governance/ai/runtime/ROADMAP_INDEX.json"
CHECKPOINT = ROOT / "governance/ai/work-state/STAGE-A-A10-current-revalidation-attempt-001.json"
BOOTSTRAP = ROOT / "governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md"
ROADMAP = ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    pointer = read_json(POINTER)
    status = read_json(STATUS)
    index = read_json(INDEX)
    checkpoint = read_json(CHECKPOINT)
    assert pointer["primary_attempt_id"] == "STAGE-A-A10-current-revalidation-attempt-001"
    selected = [x for x in pointer["active_attempts"] if x.get("owner_selected")]
    assert len(selected) == 1 and selected[0]["attempt_id"] == pointer["primary_attempt_id"]
    assert selected[0]["status"] == "completed_verified"
    app = next(x for x in pointer["deferred_tracks"] if x["track"] == "application-implementation")
    assert app["next_work_item_id"] == "STAGE-A-A10"
    assert app["state"] == "authorized_not_activated"
    assert checkpoint["status"] == "completed_verified"
    assert checkpoint["merge_commit"] == "9124860691ea208bded3800008a2d92b4b2c2139"
    assert checkpoint["roadmap_projection_pending"] is False
    assert checkpoint["restrictions"]["a10_activated"] is False
    assert checkpoint["restrictions"]["application_mutation_authorized"] is False
    assert status["primary"]["work_item_id"] == "STAGE-A-A10"
    assert status["primary"]["status"] == "completed_verified"
    ids = {x["work_item_id"] for x in index["entries"]}
    assert "STAGE-A-A10" in ids
    a10 = next(x for x in index["entries"] if x["work_item_id"] == "STAGE-A-A10")
    assert a10["dependencies"] == ["STAGE-A-A9"]
    bootstrap = BOOTSTRAP.read_text(encoding="utf-8")
    assert "**Version:** 5.6.3" in bootstrap
    assert "STAGE-A-A10 current-repository revalidation is `COMPLETED_VERIFIED`" in bootstrap
    assert "World Content Authoring activation" in bootstrap
    roadmap = ROADMAP.read_text(encoding="utf-8")
    assert "**Version:** 2.15.0" in roadmap
    assert "STAGE-A-A9 — Investigation and Social Workspaces is `COMPLETED_VERIFIED`" in roadmap
    assert "STAGE-A-A10 — World Content Authoring has completed current-repository revalidation" in roadmap
    assert "0008_a10_world_content_authoring.json" in roadmap
    print("STAGE-A-A10 RECOVERY PROJECTION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
