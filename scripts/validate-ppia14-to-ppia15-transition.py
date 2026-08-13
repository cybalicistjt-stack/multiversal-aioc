#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P14 = ROOT / "governance/ai/work-state/PPIA-14-attempt-001.json"
P15 = ROOT / "governance/ai/work-state/PPIA-15-attempt-001.json"
P9 = ROOT / "governance/ai/work-state/PPIA-09-attempt-001.json"
P10 = ROOT / "governance/ai/work-state/PPIA-10-attempt-001.json"
P11 = ROOT / "governance/ai/work-state/PPIA-11-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
PACKAGE = BASE / "PPIA-14_COMPLETION_PACKAGE_INDEX_v0.1.0.json"
REPORT = BASE / "PPIA-14_COMPLETION_REPORT.md"

EXPECTED_ORDER = ["PPIA-01","PPIA-02","PPIA-03","PPIA-04","PPIA-05","PPIA-12","PPIA-07","PPIA-08","PPIA-09","PPIA-10","PPIA-11","PPIA-06","PPIA-13","PPIA-14","PPIA-15","PPIA-16"]
P15_BRANCH = "governance/ppia-15-internal-alpha-test-content-expansion"
COMPLETE = {"complete", "completed", "completed_verified"}
ACTIVE = {"started", "in_progress", "ready_for_review"}

DEPENDENCIES = {
    "PPIA-09": {"head":"7393eac19d88eb5b2c58e44b51c1c3a2f3e2b968", "run":"31558007822", "pr":256, "merge":"3996ca97a2e31fa89ce5c9d4101c96affb83ea71"},
    "PPIA-10": {"head":"507c9da21dd74d771f910861323693e2d7193bfa", "run":"31585946135", "pr":261, "merge":"b4ac8c080af7055e2d150ab6d37de41e9cc2a68f"},
    "PPIA-11": {"head":"9bf4627f9e8e4a4c21dcc2614dcb74d54d62d724", "run":"31595927902", "pr":267, "merge":"f2274707b1337425f0bc9ac8d1dd5ebb08d9f883"},
    "PPIA-14": {"head":"34c4575ad4ec7dad705b5e292b11c94699a648ac", "run":"31646879101", "pr":284, "merge":"2bebbfcfeac78081ab942be1a15eab1745d35c3a"},
}
FOUNDATION = {
    "head":"d876093989e656d3cf8366c19755295ef0f785e8",
    "run":"31652241636",
    "pr":286,
    "merge":"a1f6b7380a07e65469ba8072e8aa4135d7b1e42f",
}


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-14→PPIA-15 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def verify_completed_checkpoint(work_item: str, checkpoint: dict) -> None:
    expected = DEPENDENCIES[work_item]
    require(checkpoint.get("work_item_id") == work_item, f"{work_item} checkpoint identity mismatch")
    require(checkpoint.get("status") == "completed_verified", f"{work_item} checkpoint must be completed_verified")
    require(checkpoint.get("active_substep") is None and checkpoint.get("completed_at"), f"{work_item} completion timestamp/substep invalid")
    require(checkpoint.get("latest_pushed_commit") == expected["head"], f"{work_item} exact validated completion head mismatch")
    require(checkpoint.get("pull_request") == expected["pr"], f"{work_item} completion PR mismatch")
    require(checkpoint.get("merge_commit") == expected["merge"], f"{work_item} completion merge mismatch")
    require(checkpoint.get("owner_decision_required") is False and checkpoint.get("unresolved_failures") == [], f"{work_item} completion has unresolved state")
    require(any(expected["run"] in (x.get("command", "") + " " + str(x.get("evidence", ""))) and x.get("status") == "passed" for x in checkpoint.get("validation", [])), f"{work_item} completion run evidence missing")
    evidence_text = json.dumps(checkpoint.get("evidence", []), ensure_ascii=False) + checkpoint.get("last_verified_action", "")
    for value in (expected["head"], expected["merge"], str(expected["pr"]), expected["run"]):
        require(value in evidence_text, f"{work_item} immutable evidence missing {value}")


def main() -> None:
    backlog = load(BACKLOG)
    p14 = load(P14)
    p15 = load(P15)
    p9 = load(P9)
    p10 = load(P10)
    p11 = load(P11)
    pointer = load(POINTER)
    status = load(STATUS)
    package = load(PACKAGE)
    report = REPORT.read_text(encoding="utf-8").lower()

    tranches = {x["work_item_id"]: x for x in backlog["tranches"]}
    require(backlog["execution_order"] == EXPECTED_ORDER, "dependency-optimized PPIA order changed")
    require(EXPECTED_ORDER.index("PPIA-14") + 1 == EXPECTED_ORDER.index("PPIA-15"), "PPIA-15 must directly follow PPIA-14")
    require(tranches["PPIA-15"].get("dependencies") == ["PPIA-09","PPIA-10","PPIA-11","PPIA-14"], "PPIA-15 dependency set changed")

    for wid, checkpoint in (("PPIA-09", p9), ("PPIA-10", p10), ("PPIA-11", p11), ("PPIA-14", p14)):
        require(tranches[wid]["status"] == "completed_verified", f"{wid} backlog must be completed_verified")
        verify_completed_checkpoint(wid, checkpoint)

    for wid in EXPECTED_ORDER[:EXPECTED_ORDER.index("PPIA-15")]:
        require(tranches[wid]["status"] in COMPLETE, f"{wid} must be complete before PPIA-15")

    require(package.get("transition_after_completion") == "PPIA-14 -> PPIA-15 separate governed operation", "PPIA-14 completion transition boundary changed")
    for phrase in ("complete permission-safe error/recovery microcopy library", "108 effective deterministic cases", "p14-gap-001", "f024", "ppia-13 retains concept-teaching ownership", "no application runtime", "ppia-14 → ppia-15 transition"):
        require(phrase in report, f"PPIA-14 completion report lost {phrase!r}")

    require(p15.get("work_item_id") == "PPIA-15" and p15.get("attempt_id") == "PPIA-15-attempt-001", "PPIA-15 checkpoint identity mismatch")
    require(p15.get("branch") == P15_BRANCH, "PPIA-15 governed branch mismatch")
    require(p15.get("base_commit") == DEPENDENCIES["PPIA-14"]["merge"], "PPIA-15 base must be PPIA-14 completion merge")
    require(p15.get("owner_decision_required") is False and p15.get("unresolved_failures") == [], "PPIA-15 transition must be unblocked")
    require(p15.get("roadmap_projection_pending") is True, "PPIA-15 roadmap projection must remain batched/pending")
    require(p15.get("status") in ACTIVE | {"completed_verified"}, f"unexpected PPIA-15 status {p15.get('status')!r}")

    scope = json.dumps({
        "objective": p15.get("objective"),
        "active_substep": p15.get("active_substep"),
        "next_action": p15.get("next_action"),
        "notes": p15.get("notes", []),
        "completed_substeps": p15.get("completed_substeps", []),
        "validation": p15.get("validation", []),
        "evidence": p15.get("evidence", []),
        "last_verified_action": p15.get("last_verified_action", ""),
    }, ensure_ascii=False).lower()
    for phrase in ("expand", "not duplicate", "internal alpha", "regression", "permission", "conflict", "recovery", "scale", "accessibility", "mobile", "object-edge", "synthetic/noncanonical", "p14-gap-001", "f024"):
        require(phrase in scope, f"PPIA-15 governed scope missing {phrase!r}")

    foundation_evidence = " ".join((FOUNDATION["head"], FOUNDATION["run"], str(FOUNDATION["pr"]), FOUNDATION["merge"]))
    foundation_verified = all(value in scope for value in (FOUNDATION["head"], FOUNDATION["run"], FOUNDATION["merge"])) and ("pr #286" in scope or '"pull_request", "value": "PPIA-15 Foundation PR #286"'.lower() in scope or str(FOUNDATION["pr"]) in scope)
    if foundation_verified:
        # Once PPIA-15 has advanced beyond its first Foundation milestone, the transition
        # validator becomes historical/successor-safe. Preserve the immutable Foundation
        # evidence instead of requiring the initial Foundation next_action wording forever.
        require("62/62" in scope, "verified Foundation hosted-workflow evidence missing")
        require("foundation" in scope and "coverage-gap" in scope, "verified Foundation milestone evidence missing")
        require("p15-gap-001" in scope or "p14-gap-001" in scope, "verified Foundation F024 provenance missing")
        scope_mode = "successor_after_verified_foundation"
    else:
        # During the initial transition/activation state, require the complete owner-approved
        # awkward-case scope explicitly before any Foundation package has been verified.
        for phrase in (
            "simultaneous selection", "mid-session reveals", "entitlement loss", "gm modifications", "duplicate-name objects", "version conflict", "campaign-local override",
            "source-only objects", "vehicle transfer", "relationship secret reveal", "interrupted crafting", "reconnect during approval", "large inventories", "dense creatures",
            "unusual species", "mobile-only", "keyboard/accessibility", "offline/read-only"
        ):
            require(phrase in scope, f"PPIA-15 governed scope missing {phrase!r}")
        scope_mode = "initial_foundation_scope"

    current_id = backlog["current_work_item_id"]
    if current_id == "PPIA-15":
        require(tranches["PPIA-15"]["status"] in ACTIVE, "active PPIA-15 backlog tranche must be started/in_progress")
        require(p15["status"] in ACTIVE and p15.get("active_substep") and p15.get("next_action"), "active PPIA-15 checkpoint must be on a bounded step")
        require(tranches["PPIA-16"]["status"] == "planned", "PPIA-16 must remain planned during PPIA-15 activation")
        require(pointer["primary_attempt_id"] == "PPIA-15-attempt-001", "pointer must select PPIA-15")
        selected = [x for x in pointer["active_attempts"] if x.get("owner_selected")]
        require(len(selected) == 1 and selected[0]["work_item_id"] == "PPIA-15", "exactly one owner-selected PPIA-15 attempt required")
        current = selected[0]
        require(current.get("checkpoint_path") == "governance/ai/work-state/PPIA-15-attempt-001.json", "PPIA-15 checkpoint path mismatch")
        for field in ("attempt_id", "branch", "status", "updated_at", "roadmap_projection_pending"):
            require(current[field] == p15[field], f"pointer/PPIA-15 checkpoint mismatch: {field}")
        primary = status["primary"]
        for field in ("work_item_id", "attempt_id", "branch", "status", "active_substep", "next_action", "latest_pushed_commit", "pull_request", "owner_decision_required", "unresolved_failures", "roadmap_projection_pending"):
            require(primary[field] == p15.get(field), f"compact status/PPIA-15 checkpoint mismatch: {field}")
        require(status["active_attempt_count"] == len(pointer["active_attempts"]) and status["deferred_track_count"] == len(pointer["deferred_tracks"]), "compact runtime counts mismatch")
        transition_mode = "active_ppia15"
    else:
        require(EXPECTED_ORDER.index(current_id) > EXPECTED_ORDER.index("PPIA-15"), "historical transition may only validate after PPIA-15")
        require(tranches["PPIA-15"]["status"] in COMPLETE, "historical PPIA-15 backlog must be complete")
        require(p15["status"] == "completed_verified", "historical PPIA-15 checkpoint must be completed_verified")
        transition_mode = "historical_after_ppia15"

    reason = pointer["selection_reason"]
    for value in (DEPENDENCIES["PPIA-14"]["head"], DEPENDENCIES["PPIA-14"]["run"], DEPENDENCIES["PPIA-14"]["merge"]):
        require(value in reason, f"pointer must preserve PPIA-14 completion evidence {value}")
    require("roadmap" in reason.lower() and "pending" in reason.lower(), "pointer must explain batched roadmap projection")

    boundaries = backlog["boundaries"]
    for key in ("application_runtime_mutation_authorized", "a2_activation_authorized", "release_authorized", "deployment_authorized", "tester_access_authorized", "canonical_promotion_without_source_evidence_authorized"):
        require(boundaries[key] is False, f"transition may not enable {key}")
    require(boundaries["requires_codex"] is False, "PPIA transition must not require Codex")

    print("PPIA-14→PPIA-15 TRANSITION: PASS")
    print(f"ppia14_final_head={DEPENDENCIES['PPIA-14']['head']}")
    print(f"ppia14_final_merge={DEPENDENCIES['PPIA-14']['merge']}")
    print(f"ppia14_completion_run={DEPENDENCIES['PPIA-14']['run']}")
    print("dependencies=PPIA-09,PPIA-10,PPIA-11,PPIA-14 completed_verified")
    print(f"ppia15_status={p15['status']}")
    print(f"ppia15_branch={P15_BRANCH}")
    print(f"transition_mode={transition_mode}")
    print(f"scope_mode={scope_mode}")
    print("roadmap_projection_pending=true runtime_activation=false")


if __name__ == "__main__":
    main()
