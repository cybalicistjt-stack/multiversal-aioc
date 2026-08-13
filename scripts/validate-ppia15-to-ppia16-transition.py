#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
PROGRAM = BASE / "PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md"
ROADMAP = ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md"
P15 = ROOT / "governance/ai/work-state/PPIA-15-attempt-001.json"
P16 = ROOT / "governance/ai/work-state/PPIA-16-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
P15_PACKAGE = BASE / "PPIA-15_COMPLETION_PACKAGE_INDEX_v0.1.0.json"
P15_REPORT = BASE / "PPIA-15_COMPLETION_REPORT.md"

EXPECTED_ORDER = ["PPIA-01","PPIA-02","PPIA-03","PPIA-04","PPIA-05","PPIA-12","PPIA-07","PPIA-08","PPIA-09","PPIA-10","PPIA-11","PPIA-06","PPIA-13","PPIA-14","PPIA-15","PPIA-16"]
P16_BRANCH = "governance/ppia-16-developer-console-ai-team-control-surface"
P15_EVIDENCE = {
    "head": "6480e22d142e018fb1722570411baa8cd29a41ea",
    "run": "31679948031",
    "pr": 289,
    "merge": "1ec15976e662de466ec301caa20462640138bc13",
    "hosted": "65/65",
}
DT_FINAL = "354e24007d2c453d090a2a6cdb31d3e3333c84c1"
P16_GATE = "Implementation-ready Development Console information architecture and screen/workflow package over DT-001 through DT-010, preserving non-authoritative tooling boundaries."


def fail(message: str) -> None:
    text = "PPIA-15→PPIA-16 TRANSITION: FAIL — " + message
    print("::error title=PPIA-15 to PPIA-16 Transition Validator::" + text.replace("\n", "%0A").replace("\r", "%0D"))
    raise SystemExit(text)


def req(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog, p15, p16, pointer, status, p15_package = map(load, (BACKLOG, P15, P16, POINTER, STATUS, P15_PACKAGE))
    program = PROGRAM.read_text(encoding="utf-8").lower()
    roadmap = ROADMAP.read_text(encoding="utf-8").lower()
    report = P15_REPORT.read_text(encoding="utf-8").lower()

    req(backlog.get("execution_order") == EXPECTED_ORDER, "PPIA execution order changed")
    req(backlog.get("current_work_item_id") == "PPIA-16", "PPIA-16 is not current")
    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    req(set(tranches) == {f"PPIA-{i:02d}" for i in range(1, 17)}, "PPIA tranche set changed")
    for wid in EXPECTED_ORDER[:-1]:
        req(tranches[wid].get("status") in {"complete","completed","completed_verified"}, f"{wid} must be complete before PPIA-16")
    req(tranches["PPIA-15"].get("status") == "completed_verified", "PPIA-15 backlog must be completed_verified")
    req(tranches["PPIA-16"].get("status") == "started", "PPIA-16 backlog must be started")
    req(tranches["PPIA-16"].get("dependencies") == [], "PPIA-16 explicit dependency set changed")
    req(tranches["PPIA-16"].get("completion_gate") == P16_GATE, "PPIA-16 completion gate changed")
    req(EXPECTED_ORDER[-2:] == ["PPIA-15", "PPIA-16"], "PPIA-16 must directly follow PPIA-15")

    req(p15.get("work_item_id") == "PPIA-15" and p15.get("attempt_id") == "PPIA-15-attempt-001", "PPIA-15 checkpoint identity changed")
    req(p15.get("status") == "completed_verified" and p15.get("active_substep") is None and p15.get("completed_at"), "PPIA-15 checkpoint not completed_verified")
    req(p15.get("latest_pushed_commit") == P15_EVIDENCE["head"], "PPIA-15 exact completion head changed")
    req(p15.get("pull_request") == P15_EVIDENCE["pr"], "PPIA-15 completion PR changed")
    req(p15.get("merge_commit") == P15_EVIDENCE["merge"], "PPIA-15 completion merge changed")
    req(p15.get("unresolved_failures") == [] and p15.get("owner_decision_required") is False, "PPIA-15 completion has unresolved state")
    p15_blob = json.dumps(p15, ensure_ascii=False).lower()
    for token in (P15_EVIDENCE["head"], P15_EVIDENCE["run"], P15_EVIDENCE["merge"], "#289", P15_EVIDENCE["hosted"], "signature verified valid"):
        req(token.lower() in p15_blob, f"PPIA-15 immutable completion evidence missing {token}")
    req(p15_package.get("transition_after_completion") == "PPIA-15 -> PPIA-16 separate governed operation", "PPIA-15 completion transition boundary changed")
    for phrase in ("effective authored ppia-15 regression corpus to **90 cases**", "ordinary gm modification is not duplicated as a standalone", "p15-gap-001", "f024", "separate governed operation"):
        req(phrase in report, f"PPIA-15 completion report missing {phrase!r}")

    req(p16.get("work_item_id") == "PPIA-16" and p16.get("attempt_id") == "PPIA-16-attempt-001", "PPIA-16 checkpoint identity changed")
    req(p16.get("branch") == P16_BRANCH, "PPIA-16 governed branch changed")
    req(p16.get("base_commit") == P15_EVIDENCE["merge"], "PPIA-16 base must be PPIA-15 completion merge")
    req(p16.get("status") == "started" and p16.get("completed_at") is None, "PPIA-16 must be active, not completed")
    req(p16.get("owner_decision_required") is False and p16.get("unresolved_failures") == [], "PPIA-16 must be unblocked")
    req(p16.get("roadmap_projection_pending") is True, "PPIA-16 roadmap projection must remain batched/pending")
    req("Foundation / Existing Developer Toolbelt and Control-Surface Authority Inventory" in (p16.get("active_substep") or ""), "PPIA-16 initial bounded substep changed")
    scope = json.dumps({
        "objective": p16.get("objective"),
        "active_substep": p16.get("active_substep"),
        "next_action": p16.get("next_action"),
        "notes": p16.get("notes", []),
        "evidence": p16.get("evidence", []),
        "last_verified_action": p16.get("last_verified_action", ""),
    }, ensure_ascii=False).lower()
    for term in (
        "developer console", "ai-team control surface", "dt-001", "dt-010", "current work/slice", "scope authority", "stop conditions",
        "repository health", "fixtures", "scenarios", "privacy scanning", "ui evidence", "design lint", "traceability",
        "recovery/performance", "ci/evidence receipts", "findings", "codex task capsules", "proof exploration", "interruption recovery",
        "non-authoritative", "mv-dev v0.10.0", DT_FINAL,
    ):
        req(term in scope, f"PPIA-16 governed scope missing {term!r}")
    for dt in range(1, 11):
        req(f"dt-{dt:03d}" in scope, f"PPIA-16 scope missing DT-{dt:03d}")

    req(pointer.get("primary_attempt_id") == "PPIA-16-attempt-001", "runtime pointer does not select PPIA-16")
    selected = [x for x in pointer.get("active_attempts", []) if x.get("owner_selected")]
    req(len(selected) == 1 and selected[0].get("work_item_id") == "PPIA-16", "exactly one owner-selected PPIA-16 attempt required")
    entry = selected[0]
    req(entry.get("checkpoint_path") == "governance/ai/work-state/PPIA-16-attempt-001.json", "PPIA-16 checkpoint path changed")
    for field in ("attempt_id","branch","status","updated_at","roadmap_projection_pending"):
        req(entry.get(field) == p16.get(field), f"pointer/PPIA-16 mismatch: {field}")
    primary = status.get("primary", {})
    for field in ("work_item_id","attempt_id","branch","status","active_substep","next_action","latest_pushed_commit","pull_request","owner_decision_required","unresolved_failures","roadmap_projection_pending"):
        req(primary.get(field) == p16.get(field), f"compact status/PPIA-16 mismatch: {field}")
    req(status.get("active_attempt_count") == len(pointer.get("active_attempts", [])), "active attempt count mismatch")
    req(status.get("deferred_track_count") == len(pointer.get("deferred_tracks", [])), "deferred track count mismatch")
    reason = pointer.get("selection_reason", "").lower()
    for token in (P15_EVIDENCE["head"], P15_EVIDENCE["run"], P15_EVIDENCE["merge"], "65/65", DT_FINAL, "roadmap", "pending"):
        req(token.lower() in reason, f"pointer lost transition/source evidence {token}")

    for phrase in ("ppia-16 — developer console / ai-team control surface", "dt-001 through dt-010", "current work/slice", "scope authority", "stop conditions", "proof exploration", "interruption recovery"):
        req(phrase in program, f"PPIA governing program missing {phrase!r}")
    for dt in range(1, 11):
        req(f"dt-{dt:03d}" in roadmap, f"roadmap missing DT-{dt:03d}")
    req("mv-dev` version `0.10.0" in roadmap or "mv-dev v0.10.0" in roadmap, "roadmap missing mv-dev v0.10.0 anchor")
    req(DT_FINAL in roadmap, "roadmap missing final DT support-series merge")

    app_tracks = [x for x in pointer.get("deferred_tracks", []) if x.get("track") == "application-implementation"]
    req(len(app_tracks) == 1 and app_tracks[0].get("next_work_item_id") == "STAGE-A-A2", "A2 deferred track changed")
    req("checkout_runner_blocked" in app_tracks[0].get("state", ""), "A2 must remain checkout-runner blocked")
    boundaries = backlog.get("boundaries", {})
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(boundaries.get(key) is False, f"transition may not enable {key}")
    req(boundaries.get("requires_codex") is False, "PPIA-16 design transition must not require Codex")

    print("PPIA-15→PPIA-16 TRANSITION: PASS")
    print(f"ppia15_head={P15_EVIDENCE['head']} ppia15_run={P15_EVIDENCE['run']} ppia15_pr={P15_EVIDENCE['pr']} ppia15_merge={P15_EVIDENCE['merge']}")
    print("ppia15_hosted=65/65 status=completed_verified")
    print(f"ppia16_branch={P16_BRANCH} ppia16_status=started dependencies=none")
    print(f"developer_toolbelt_anchor={DT_FINAL} mv_dev=0.10.0 dt_range=DT-001..DT-010")
    print("runtime_activation=false a2_activation=false tester_access=false release=false deployment=false")


if __name__ == "__main__":
    main()
