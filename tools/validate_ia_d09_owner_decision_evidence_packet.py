#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_DIR = ROOT / "governance/application-planning/internal-alpha/owner-decision"

EXPECTED_GATES = [
    "authorize Internal Alpha tester access",
    "authorize real-user data collection",
    "authorize production credentials",
    "authorize paid provider commitment",
    "approve Internal Alpha release",
    "approve public release or deployment",
    "promote AI/automation authority",
    "promote working/noncanonical design standards",
]
READY_GATES = {
    "authorize Internal Alpha tester access",
    "approve Internal Alpha release",
}
CANDIDATE = "56b127f1fc01eebe5c73ba0472a5b6496fe92b5e"
BUILD = "5033f55d3344209c1719d6003d1369b4bc201c74ba9d64f046767263daee5a45"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    required_files = [
        "IA_D09_OWNER_DECISION_EVIDENCE_PACKET.md",
        "IA_D09_CANDIDATE_KNOWN_LIMITATIONS.json",
        "IA_D09_CANDIDATE_DATA_PRIVACY_BOUNDARY.md",
        "IA_D09_TESTER_RECOVERY_SUPPORT_PROCEDURE.md",
        "IA_D09_UNRESOLVED_RISK_REGISTER.json",
        "IA_D09_TESTER_ENTRY_DECISION_PACKAGE.json",
        "IA_D09_OWNER_GATE_READINESS.json",
        "IA_D09_OWNER_DECISION_RECORD_TEMPLATE.json",
        "IA_D09_OWNER_DECISION_PREPARATION_RECEIPT.json",
    ]
    for name in required_files:
        require((PACKET_DIR / name).is_file(), f"missing packet file: {name}", errors)

    gates = load(PACKET_DIR / "IA_D09_OWNER_GATE_READINESS.json")
    decisions = load(PACKET_DIR / "IA_D09_OWNER_DECISION_RECORD_TEMPLATE.json")
    limitations = load(PACKET_DIR / "IA_D09_CANDIDATE_KNOWN_LIMITATIONS.json")
    risks = load(PACKET_DIR / "IA_D09_UNRESOLVED_RISK_REGISTER.json")
    tester = load(PACKET_DIR / "IA_D09_TESTER_ENTRY_DECISION_PACKAGE.json")
    receipt = load(PACKET_DIR / "IA_D09_OWNER_DECISION_PREPARATION_RECEIPT.json")
    work = load(ROOT / "governance/ai/work-state/IA-D09-owner-decision-evidence-preparation-attempt-001.json")
    pointer = load(ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json")
    status = load(ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json")
    roadmap = load(ROOT / "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A12_SUPPLEMENT.json")

    require(gates.get("candidate_sha") == CANDIDATE, "gate matrix candidate mismatch", errors)
    require(gates.get("candidate_state") == "candidate-validated", "candidate must remain candidate-validated", errors)
    require(gates.get("release_approved") is False, "packet must not approve release", errors)
    gate_rows = gates.get("gates", [])
    require([row.get("gate_id") for row in gate_rows] == EXPECTED_GATES, "owner gate ordering/identity mismatch", errors)
    require({row["gate_id"] for row in gate_rows if row.get("decision_ready") is True} == READY_GATES, "only bounded tester-access and Internal Alpha release may be decision-ready", errors)
    require(all(row.get("decision") == "not-decided" for row in gate_rows), "gate matrix may not make owner decisions", errors)

    decision_rows = decisions.get("decisions", [])
    require(decisions.get("owner_subject") == "John Brandon Turner", "owner subject mismatch", errors)
    require(decisions.get("candidate_sha") == CANDIDATE and decisions.get("build_id") == BUILD, "decision template candidate/build mismatch", errors)
    require([row.get("gate_id") for row in decision_rows] == EXPECTED_GATES, "decision template gate identity mismatch", errors)
    require(all(row.get("decision") == "not-decided" for row in decision_rows), "decision template must remain not-decided", errors)
    require(all(value is False for value in decisions.get("default_without_owner_decision", {}).values()), "all default authorization values must remain false", errors)

    items = limitations.get("items", [])
    require(limitations.get("candidate_sha") == CANDIDATE, "limitation registry candidate mismatch", errors)
    require(limitations.get("blocking_limitation_count") == 0, "blocking limitations cannot be present", errors)
    require(len(items) == 5 and all(item.get("blocking") is False for item in items), "expected five nonblocking candidate limitations", errors)

    require(risks.get("candidate_sha") == CANDIDATE, "risk register candidate mismatch", errors)
    require(risks.get("blocking_risk_count") == 0, "blocking risk count must remain zero", errors)
    require(risks.get("unresolved_high_critical_security_count") == 0, "unresolved HIGH/CRITICAL security count must remain zero", errors)

    require(tester.get("candidate_sha") == CANDIDATE and tester.get("build_id") == BUILD, "tester package candidate/build mismatch", errors)
    require(tester.get("data_classification") == "synthetic-test-only", "tester data boundary must remain synthetic-test-only", errors)
    require(tester.get("supported_profiles") == ["browser", "local-runner"], "tester profiles must remain browser/local-runner", errors)
    require(tester.get("owner_access_decision") == "not-decided" and tester.get("tester_access_authorized") is False, "tester access must remain closed", errors)

    require(work.get("status") in {"ready_for_review", "blocked_owner"}, "work-state status mismatch", errors)
    require(work.get("owner_decision_required") is True and work.get("owner_decision_made") is False, "work-state must require an undecided owner decision", errors)
    require(work.get("release_approved") is False and work.get("tester_access_authorized") is False, "work-state must keep release/tester gates closed", errors)

    require(pointer.get("primary_attempt_id") == "IA-D09-owner-decision-evidence-preparation-attempt-001", "current pointer must select IA-D09 owner decision", errors)
    require(status.get("primary", {}).get("work_item_id") == "IA-D09-OWNER-DECISION", "implementation status primary mismatch", errors)
    require(status.get("primary", {}).get("status") == work.get("status"), "implementation status lifecycle mismatch", errors)
    require(status.get("primary", {}).get("owner_decision_required") is True, "implementation status must require owner decision", errors)
    require(any(row.get("work_item_id") == "IA-D09-OWNER-DECISION" for row in roadmap.get("entries", [])), "roadmap supplement missing IA-D09 owner-decision entry", errors)

    if work.get("status") == "blocked_owner":
        require(receipt.get("state") == "prepared_verified_owner_decision_pending", "post-merge preparation receipt mismatch", errors)
        require(receipt.get("preparation_merge_commit") == "3a6f75bff961b5a5ff15392e97cb3bc106c8b939", "preparation merge evidence mismatch", errors)
        require(receipt.get("owner_decisions_made") == 0, "post-merge receipt may not make an owner decision", errors)

    packet_text = (PACKET_DIR / "IA_D09_OWNER_DECISION_EVIDENCE_PACKET.md").read_text(encoding="utf-8")
    require("does not approve any owner-only gate" in packet_text, "packet must state non-approval boundary", errors)
    require("There is no automatic A13" in (ROOT / "governance/ai/runtime/BOOTSTRAP_CURRENT_STATE_AMENDMENT_IA_D09_OWNER_DECISION_PENDING.md").read_text(encoding="utf-8"), "bootstrap amendment must prevent automatic A13", errors)

    if errors:
        print("IA-D09 OWNER-DECISION EVIDENCE PACKET: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("IA-D09 OWNER-DECISION EVIDENCE PACKET: PASS")
    print("decision_ready=2 not_decision_ready=6 owner_decisions=0 release_approved=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
