#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
REPORT = BASE / "PPIA-04_COMPLETION_REPORT.md"
P4 = ROOT / "governance/ai/work-state/PPIA-04-attempt-001.json"
P5 = ROOT / "governance/ai/work-state/PPIA-05-attempt-001.json"
ROADMAP = ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md"
PROGRAM = BASE / "PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md"

P4_FINAL_HEAD = "a821f53794d675e73ae71d6c02d577141981ba22"
P4_COMPLETION_MERGE = "e8ec662534820e53fcb8a7d958c0946f494faefd"
P4_TO_P5_TRANSITION_MERGE = "6e9e82252d389f1360e7f1b1191afe5e8c336aa0"
P5_FINAL_HEAD = "e6e2bcfd0f22f537a73721dfd8069531bd1af24c"
P5_COMPLETION_MERGE = "0ffaa34ef15f9a7e4b77776688c6be3fc3047446"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-04→PPIA-05 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p4 = load(P4)
    p5 = load(P5)
    report = REPORT.read_text(encoding="utf-8")
    roadmap = ROADMAP.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")
    tranches = {item["work_item_id"]: item for item in backlog["tranches"]}

    require(tranches["PPIA-04"]["status"] == "completed_verified", "PPIA-04 backlog state must remain completed_verified")
    require(tranches["PPIA-05"]["status"] == "completed_verified", "PPIA-05 backlog state must remain completed_verified after its completion")

    require(p4["status"] == "completed_verified" and p4["active_substep"] is None, "PPIA-04 checkpoint must remain completed_verified")
    require(p4["latest_pushed_commit"] == P4_FINAL_HEAD and p4["pull_request"] == 229 and p4.get("merge_commit") == P4_COMPLETION_MERGE, "PPIA-04 exact completion evidence changed")
    require(any("31524517244" in item.get("command", "") and item.get("status") == "passed" for item in p4["validation"]), "PPIA-04 completion gate evidence missing")

    require(p5["work_item_id"] == "PPIA-05" and p5["attempt_id"] == "PPIA-05-attempt-001", "PPIA-05 checkpoint identity mismatch")
    require(p5["status"] == "completed_verified" and p5["active_substep"] is None, "PPIA-05 checkpoint must now be completed_verified")
    require(p5["base_commit"] == P4_TO_P5_TRANSITION_MERGE, "PPIA-05 governed work must preserve canonical transition base")
    require(p5["latest_pushed_commit"] == P5_FINAL_HEAD and p5["pull_request"] == 234 and p5.get("merge_commit") == P5_COMPLETION_MERGE, "PPIA-05 exact completion evidence changed")
    require(any("31529821441" in item.get("command", "") and item.get("status") == "passed" for item in p5["validation"]), "PPIA-05 completion gate evidence missing")
    require(any(P5_COMPLETION_MERGE in item.get("value", "") for item in p5.get("evidence", [])), "PPIA-05 completion merge evidence missing")

    for value in ("24 retained Vehicle/Mecha/Spacecraft/Operations PDFs / 608 pages", "42 acceptance requirements across 14 categories", P4_FINAL_HEAD, P4_COMPLETION_MERGE, "PPIA-05 — Species, Forms & Character Biology"):
        require(value in report, f"PPIA-04 completion report missing {value!r}")
    for value in ("PPIA-04 — Vehicle, Mecha & Starship Experience", "PPIA-05 — Species, Forms & Character Biology"):
        require(value in roadmap and value in program, f"roadmap/program lost {value}")

    print("PPIA-04→PPIA-05 TRANSITION: PASS")
    print("ppia04_status=completed_verified")
    print(f"ppia04_final_merge={P4_COMPLETION_MERGE}")
    print("ppia05_status=completed_verified")
    print(f"ppia05_transition_merge={P4_TO_P5_TRANSITION_MERGE}")
    print(f"ppia05_final_merge={P5_COMPLETION_MERGE}")
    print("historical_transition_integrity=preserved")


if __name__ == "__main__":
    main()
