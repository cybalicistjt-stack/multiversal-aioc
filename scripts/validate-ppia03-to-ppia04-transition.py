#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
REPORT = BASE / "PPIA-03_COMPLETION_REPORT.md"
P3 = ROOT / "governance/ai/work-state/PPIA-03-attempt-001.json"
P4 = ROOT / "governance/ai/work-state/PPIA-04-attempt-001.json"
ROADMAP = ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md"
PROGRAM = BASE / "PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md"

P3_COMPLETION_MERGE = "ea08234b9d6bcd4cb942c2de964639b330d9511e"
P3_TO_P4_TRANSITION_MERGE = "aee4b5d99f3163454da931a939b142048cea11c5"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-03→PPIA-04 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p3 = load(P3)
    p4 = load(P4)
    report = REPORT.read_text(encoding="utf-8")
    roadmap = ROADMAP.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")
    tranches = {item["work_item_id"]: item for item in backlog["tranches"]}

    require(tranches["PPIA-03"]["status"] == "completed_verified", "PPIA-03 backlog state must stay completed_verified")
    require(tranches["PPIA-04"]["status"] in {"started", "in_progress", "completed_verified"}, "PPIA-04 backlog state invalid")
    require(p3["status"] == "completed_verified" and p3.get("merge_commit") == P3_COMPLETION_MERGE, "PPIA-03 verified completion evidence changed")
    require(p3["pull_request"] == 224 and p3["latest_pushed_commit"] == "c1e00ebf67fe4c78af2ce6e1dd483bb699706047", "PPIA-03 exact completion identity changed")

    require(p4["work_item_id"] == "PPIA-04" and p4["attempt_id"] == "PPIA-04-attempt-001", "PPIA-04 checkpoint identity mismatch")
    require(p4["branch"] == "governance/ppia-04-vehicle-mecha-starship", "PPIA-04 branch mismatch")
    require(p4["base_commit"] == P3_TO_P4_TRANSITION_MERGE, "PPIA-04 must preserve validated transition merge as branch base")
    require(any(P3_TO_P4_TRANSITION_MERGE in item.get("value", "") for item in p4.get("evidence", [])), "PPIA-04 must preserve transition merge evidence")
    require(p4["roadmap_projection_pending"] is True, "PPIA-04 roadmap projection policy changed")
    require(not p4["unresolved_failures"] and p4["owner_decision_required"] is False, "PPIA-04 has unresolved transition state")

    for value in (P3_COMPLETION_MERGE, "31518534709", "40 acceptance requirements across 15 categories", "PPIA-04 — Vehicle, Mecha & Starship Experience"):
        require(value in report, f"PPIA-03 completion report missing {value!r}")
    for value in ("PPIA-03 — Items, Equipment & Inventory Experience", "PPIA-04 — Vehicle, Mecha & Starship Experience"):
        require(value in roadmap and value in program, f"roadmap/program lost {value}")

    print("PPIA-03→PPIA-04 TRANSITION: PASS")
    print(f"ppia04_status={p4['status']}")
    print(f"ppia04_branch_base={P3_TO_P4_TRANSITION_MERGE}")


if __name__ == "__main__":
    main()
