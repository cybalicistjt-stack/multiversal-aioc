#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P8_REPORT = BASE / "PPIA-08_COMPLETION_REPORT.md"
P8 = ROOT / "governance/ai/work-state/PPIA-08-attempt-001.json"
P9 = ROOT / "governance/ai/work-state/PPIA-09-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
F011 = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F011_INVESTIGATION_AND_CLUE_BOARD.md"
F011_MATRIX = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F011_INVESTIGATION_CLUE_MATRIX.json"

P8_FINAL_HEAD = "1a2a8590730a905cf4bba84abd59d0a8f00de89c"
P8_COMPLETION_PR = 251
P8_COMPLETION_MERGE = "09f9df2607398010097e834e8ad7b129cd10645f"
P9_BRANCH = "governance/ppia-09-investigation-mystery-authoring"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-08→PPIA-09 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p8 = load(P8)
    p9 = load(P9)
    pointer = load(POINTER)
    status = load(STATUS)
    report = P8_REPORT.read_text(encoding="utf-8")
    f011 = F011.read_text(encoding="utf-8")
    require(F011_MATRIX.exists(), "MV-IA-F011 companion clue matrix missing")

    tranches = {x["work_item_id"]: x for x in backlog["tranches"]}
    require(tranches["PPIA-08"]["status"] == "completed_verified", "PPIA-08 backlog must be completed_verified")
    require(tranches["PPIA-09"]["status"] == "started", "PPIA-09 backlog must be started")
    require("PPIA-08" in tranches["PPIA-09"].get("dependencies", []), "PPIA-09 dependency on PPIA-08 missing")
    require(backlog["current_work_item_id"] == "PPIA-09", "backlog must select PPIA-09")
    order = backlog["execution_order"]
    require(order.index("PPIA-08") + 1 == order.index("PPIA-09"), "dependency-optimized order must place PPIA-09 after PPIA-08")

    require(p8["status"] == "completed_verified", "PPIA-08 checkpoint must be completed_verified")
    require(p8["active_substep"] is None and p8.get("completed_at"), "PPIA-08 completion timestamp/substep invalid")
    require(p8["latest_pushed_commit"] == P8_FINAL_HEAD, "PPIA-08 exact validated completion head mismatch")
    require(p8["pull_request"] == P8_COMPLETION_PR, "PPIA-08 completion PR mismatch")
    require(p8["merge_commit"] == P8_COMPLETION_MERGE, "PPIA-08 completion merge mismatch")
    require(not p8["unresolved_failures"] and p8["owner_decision_required"] is False, "PPIA-08 completion has unresolved state")
    require(any(v.get("command", "").startswith("Validate PPIA-08 Completion Contract") and v.get("status") == "passed" for v in p8["validation"]), "PPIA-08 completion-gate evidence missing")
    evidence_text = json.dumps(p8.get("evidence", []), ensure_ascii=False)
    for value in (P8_FINAL_HEAD, "PR #251", P8_COMPLETION_MERGE):
        require(value in evidence_text, f"PPIA-08 immutable completion evidence missing {value}")

    # The completion report is a pre-merge candidate artifact; immutable final head/PR/merge
    # evidence belongs to the completed checkpoint above, not to the historical report.
    for value in ("48 blocking acceptance requirements", "PPIA-09"):
        require(value.lower() in report.lower(), f"PPIA-08 completion report missing {value!r}")

    require(p9["work_item_id"] == "PPIA-09" and p9["attempt_id"] == "PPIA-09-attempt-001", "PPIA-09 checkpoint identity mismatch")
    require(p9["status"] == "started", "PPIA-09 checkpoint must be started")
    require(p9["branch"] == P9_BRANCH, "PPIA-09 governed branch mismatch")
    require(p9["base_commit"] == P8_COMPLETION_MERGE, "PPIA-09 base must be PPIA-08 completion merge")
    require(p9["latest_pushed_commit"] is None and p9["pull_request"] is None and p9["merge_commit"] is None, "transition may not fabricate PPIA-09 implementation evidence")
    require(p9["owner_decision_required"] is False and p9["unresolved_failures"] == [], "PPIA-09 transition must be unblocked")
    require(p9["active_substep"] and "source/design foundation" in p9["active_substep"].lower(), "PPIA-09 must start at source/design foundation")
    scope = (p9.get("objective", "") + " " + p9["active_substep"] + " " + p9["next_action"] + " " + " ".join(p9.get("notes", []))).lower()
    for phrase in ("objective truth", "gm conclusion", "clue", "evidence", "hypothesis", "false lead", "contradiction", "reveal", "uncertainty", "provenance", "nonvisual"):
        require(phrase in scope, f"PPIA-09 starting scope missing {phrase!r}")

    f011_low = f011.lower()
    for phrase in ("objective truth", "gm conclusion", "clue definition", "campaign clue", "observation", "claim", "evidence item", "hypothesis", "connection", "question", "conclusion", "false lead", "private clue", "idempotency", "nonvisual"):
        require(phrase in f011_low, f"MV-IA-F011 starting contract missing {phrase!r}")
    require("player deductions are not auto-promoted to fact" in f011_low, "MV-IA-F011 truth/belief guardrail missing")
    require("spatial placement is presentation state" in f011_low, "MV-IA-F011 graph-position guardrail missing")

    require(pointer["primary_attempt_id"] == "PPIA-09-attempt-001", "pointer must select PPIA-09")
    selected = [x for x in pointer["active_attempts"] if x.get("owner_selected")]
    require(len(selected) == 1 and selected[0]["work_item_id"] == "PPIA-09", "exactly one owner-selected PPIA-09 attempt required")
    current = selected[0]
    for field in ("attempt_id", "branch", "status", "updated_at", "roadmap_projection_pending"):
        require(current[field] == p9[field], f"pointer/PPIA-09 checkpoint mismatch: {field}")
    require(current["checkpoint_path"] == "governance/ai/work-state/PPIA-09-attempt-001.json", "PPIA-09 checkpoint path mismatch")

    primary = status["primary"]
    for field in ("work_item_id", "attempt_id", "branch", "status", "active_substep", "next_action", "latest_pushed_commit", "pull_request", "owner_decision_required", "unresolved_failures", "roadmap_projection_pending"):
        require(primary[field] == p9[field], f"compact status/PPIA-09 checkpoint mismatch: {field}")
    require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "pointer must explain batched roadmap projection")

    boundaries = backlog["boundaries"]
    for key in ("application_runtime_mutation_authorized", "a2_activation_authorized", "release_authorized", "deployment_authorized", "tester_access_authorized", "canonical_promotion_without_source_evidence_authorized"):
        require(boundaries[key] is False, f"transition may not enable {key}")

    print("PPIA-08→PPIA-09 TRANSITION: PASS")
    print(f"ppia08_final_head={P8_FINAL_HEAD}")
    print(f"ppia08_final_merge={P8_COMPLETION_MERGE}")
    print("ppia08_status=completed_verified")
    print("ppia09_status=started")
    print(f"ppia09_branch={P9_BRANCH}")
    print("starting_contract=MV-IA-F011 + PPIA-08 + permissions/recovery/accessibility")
    print("truth_belief_separation=required hidden_information_filtering=required nonvisual=required")
    print("roadmap_projection_pending=true runtime_activation=false")


if __name__ == "__main__":
    main()
