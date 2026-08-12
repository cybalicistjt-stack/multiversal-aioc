#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P9_REPORT = BASE / "PPIA-09_COMPLETION_REPORT.md"
P9 = ROOT / "governance/ai/work-state/PPIA-09-attempt-001.json"
P10 = ROOT / "governance/ai/work-state/PPIA-10-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
F009 = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F009_RELATIONSHIP_TRACKER.md"
F010 = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F010_SOCIAL_INTERACTION_MODE.md"
F016 = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F016_FACTIONS_REPUTATION_AND_ORGANIZATIONS.md"

P9_FINAL_HEAD = "7393eac19d88eb5b2c58e44b51c1c3a2f3e2b968"
P9_COMPLETION_PR = 256
P9_COMPLETION_MERGE = "3996ca97a2e31fa89ce5c9d4101c96affb83ea71"
P9_COMPLETION_RUN = "31558007822"
P10_BRANCH = "governance/ppia-10-relationship-social-faction"
COMPLETE = {"complete", "completed", "completed_verified"}
ACTIVE = {"started", "in_progress"}


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-09→PPIA-10 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p9 = load(P9)
    p10 = load(P10)
    pointer = load(POINTER)
    status = load(STATUS)
    report = P9_REPORT.read_text(encoding="utf-8")
    f009 = F009.read_text(encoding="utf-8")
    f010 = F010.read_text(encoding="utf-8")
    f016 = F016.read_text(encoding="utf-8")

    tranches = {x["work_item_id"]: x for x in backlog["tranches"]}
    require(tranches["PPIA-09"]["status"] == "completed_verified", "PPIA-09 backlog must be completed_verified")
    require("PPIA-08" in tranches["PPIA-10"].get("dependencies", []), "PPIA-10 dependency on PPIA-08 missing")
    order = backlog["execution_order"]
    require(order.index("PPIA-09") + 1 == order.index("PPIA-10"), "dependency-optimized order must place PPIA-10 after PPIA-09")

    # Immutable PPIA-09 completion evidence.
    require(p9["status"] == "completed_verified", "PPIA-09 checkpoint must be completed_verified")
    require(p9["active_substep"] is None and p9.get("completed_at"), "PPIA-09 completion timestamp/substep invalid")
    require(p9["latest_pushed_commit"] == P9_FINAL_HEAD, "PPIA-09 exact validated completion head mismatch")
    require(p9["pull_request"] == P9_COMPLETION_PR, "PPIA-09 completion PR mismatch")
    require(p9["merge_commit"] == P9_COMPLETION_MERGE, "PPIA-09 completion merge mismatch")
    require(not p9["unresolved_failures"] and p9["owner_decision_required"] is False, "PPIA-09 completion has unresolved state")
    require(any(P9_COMPLETION_RUN in v.get("command", "") and v.get("status") == "passed" for v in p9["validation"]), "PPIA-09 completion-gate evidence missing")
    evidence_text = json.dumps(p9.get("evidence", []), ensure_ascii=False)
    for value in (P9_FINAL_HEAD, "PR #256", P9_COMPLETION_MERGE, P9_COMPLETION_RUN):
        require(value in evidence_text, f"PPIA-09 immutable completion evidence missing {value}")
    for phrase in ("COMPLETED_VERIFIED", P9_FINAL_HEAD, "PR #256", P9_COMPLETION_RUN, P9_COMPLETION_MERGE, "48 blocking acceptance requirements"):
        require(phrase.lower() in report.lower(), f"PPIA-09 completion report missing {phrase!r}")

    # PPIA-10 initialized identity and scope. This remains valid after later PPIA-10 milestones.
    require(p10["work_item_id"] == "PPIA-10" and p10["attempt_id"] == "PPIA-10-attempt-001", "PPIA-10 checkpoint identity mismatch")
    require(p10["branch"] == P10_BRANCH, "PPIA-10 governed branch mismatch")
    require(p10["base_commit"] == P9_COMPLETION_MERGE, "PPIA-10 base must be PPIA-09 completion merge")
    require(p10["owner_decision_required"] is False and p10["unresolved_failures"] == [], "PPIA-10 transition must be unblocked")
    require(p10["status"] in ACTIVE | {"completed_verified"}, f"unexpected PPIA-10 status {p10['status']!r}")

    scope_trace = json.dumps({
        "objective": p10.get("objective"),
        "last_verified_action": p10.get("last_verified_action"),
        "active_substep": p10.get("active_substep"),
        "next_action": p10.get("next_action"),
        "completed_substeps": p10.get("completed_substeps", []),
        "evidence": p10.get("evidence", []),
        "notes": p10.get("notes", []),
    }, ensure_ascii=False).lower()
    for phrase in ("directional", "relationship", "social", "faction", "reputation", "standing", "influence", "membership", "rank", "office", "secret", "reveal", "permission", "history", "nonvisual"):
        require(phrase in scope_trace, f"PPIA-10 governed scope trace missing {phrase!r}")

    # Starting contracts preserve the critical separations PPIA-10 must not collapse.
    f009_low = f009.lower()
    for phrase in ("relationships are directional", "fourteen", "no universal numeric range", "seven independently authorized reveal layers", "relationship, reputation/standing", "nonvisual"):
        require(phrase in f009_low, f"F009 starting contract missing {phrase!r}")
    f010_low = f010.lower()
    for phrase in ("persuasion is not mind control", "npc truth", "player beliefs", "relationship", "faction standing", "influence", "proposal", "noncolor"):
        require(phrase in f010_low, f"F010 starting contract missing {phrase!r}")
    f016_low = f016.lower()
    for phrase in ("membership, rank, office, reputation, influence, ownership, equipment, and permission are separate", "no universal scale", "secret membership", "relationship tracker", "nonvisual parity"):
        require(phrase in f016_low, f"F016 starting contract missing {phrase!r}")

    # Initial-transition mode selects PPIA-10. Later historical validation accepts a completed PPIA-10 after current work advances.
    current_id = backlog["current_work_item_id"]
    if current_id == "PPIA-10":
        require(tranches["PPIA-10"]["status"] in ACTIVE, "active PPIA-10 backlog tranche must be started/in_progress")
        require(p10["status"] in ACTIVE, "active PPIA-10 checkpoint must be started/in_progress")
        require(pointer["primary_attempt_id"] == "PPIA-10-attempt-001", "pointer must select PPIA-10")
        selected = [x for x in pointer["active_attempts"] if x.get("owner_selected")]
        require(len(selected) == 1 and selected[0]["work_item_id"] == "PPIA-10", "exactly one owner-selected PPIA-10 attempt required")
        current = selected[0]
        for field in ("attempt_id", "branch", "status", "updated_at", "roadmap_projection_pending"):
            require(current[field] == p10[field], f"pointer/PPIA-10 checkpoint mismatch: {field}")
        require(current["checkpoint_path"] == "governance/ai/work-state/PPIA-10-attempt-001.json", "PPIA-10 checkpoint path mismatch")
        primary = status["primary"]
        for field in ("work_item_id", "attempt_id", "branch", "status", "active_substep", "next_action", "latest_pushed_commit", "pull_request", "owner_decision_required", "unresolved_failures", "roadmap_projection_pending"):
            require(primary[field] == p10[field], f"compact status/PPIA-10 checkpoint mismatch: {field}")
        transition_mode = "active_ppia10"
    else:
        require(order.index(current_id) > order.index("PPIA-10"), "historical transition may only validate after PPIA-10")
        require(tranches["PPIA-10"]["status"] in COMPLETE, "historical PPIA-10 backlog must be complete")
        require(p10["status"] == "completed_verified", "historical PPIA-10 checkpoint must be completed_verified")
        transition_mode = "historical_after_ppia10"

    require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "pointer must explain batched roadmap projection")
    boundaries = backlog["boundaries"]
    for key in ("application_runtime_mutation_authorized", "a2_activation_authorized", "release_authorized", "deployment_authorized", "tester_access_authorized", "canonical_promotion_without_source_evidence_authorized"):
        require(boundaries[key] is False, f"transition may not enable {key}")

    print("PPIA-09→PPIA-10 TRANSITION: PASS")
    print(f"ppia09_final_head={P9_FINAL_HEAD}")
    print(f"ppia09_final_merge={P9_COMPLETION_MERGE}")
    print("ppia09_status=completed_verified")
    print(f"ppia10_status={p10['status']}")
    print(f"ppia10_branch={P10_BRANCH}")
    print(f"transition_mode={transition_mode}")
    print("starting_contracts=F009+F010+F016+PPIA-08+PPIA-09")
    print("directional_relationships=true universal_social_score=false hidden_information_filtering=required")
    print("roadmap_projection_pending=true runtime_activation=false")


if __name__ == "__main__":
    main()
