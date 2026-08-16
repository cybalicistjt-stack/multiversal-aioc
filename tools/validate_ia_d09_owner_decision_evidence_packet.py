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
READY_GATES = {"authorize Internal Alpha tester access", "approve Internal Alpha release"}
CANDIDATE = "56b127f1fc01eebe5c73ba0472a5b6496fe92b5e"
BUILD = "5033f55d3344209c1719d6003d1369b4bc201c74ba9d64f046767263daee5a45"
DECISION_RECORD = PACKET_DIR / "IA_D09_OWNER_DECISION_RECORD_20260816.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    for name in [
        "IA_D09_OWNER_DECISION_EVIDENCE_PACKET.md",
        "IA_D09_CANDIDATE_KNOWN_LIMITATIONS.json",
        "IA_D09_CANDIDATE_DATA_PRIVACY_BOUNDARY.md",
        "IA_D09_TESTER_RECOVERY_SUPPORT_PROCEDURE.md",
        "IA_D09_UNRESOLVED_RISK_REGISTER.json",
        "IA_D09_TESTER_ENTRY_DECISION_PACKAGE.json",
        "IA_D09_OWNER_GATE_READINESS.json",
        "IA_D09_OWNER_DECISION_RECORD_TEMPLATE.json",
        "IA_D09_OWNER_DECISION_PREPARATION_RECEIPT.json",
    ]:
        require((PACKET_DIR / name).is_file(), f"missing packet file: {name}", errors)

    gates = load(PACKET_DIR / "IA_D09_OWNER_GATE_READINESS.json")
    template = load(PACKET_DIR / "IA_D09_OWNER_DECISION_RECORD_TEMPLATE.json")
    limitations = load(PACKET_DIR / "IA_D09_CANDIDATE_KNOWN_LIMITATIONS.json")
    risks = load(PACKET_DIR / "IA_D09_UNRESOLVED_RISK_REGISTER.json")
    tester = load(PACKET_DIR / "IA_D09_TESTER_ENTRY_DECISION_PACKAGE.json")
    work = load(ROOT / "governance/ai/work-state/IA-D09-owner-decision-evidence-preparation-attempt-001.json")
    pointer = load(ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json")
    status = load(ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json")
    roadmap = load(ROOT / "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A12_SUPPLEMENT.json")

    require(gates.get("candidate_sha") == CANDIDATE, "gate matrix candidate mismatch", errors)
    require(gates.get("candidate_state") == "candidate-validated", "candidate must remain candidate-validated", errors)
    rows = gates.get("gates", [])
    require([row.get("gate_id") for row in rows] == EXPECTED_GATES, "owner gate ordering/identity mismatch", errors)
    require({row["gate_id"] for row in rows if row.get("decision_ready") is True} == READY_GATES, "decision-ready gate set changed", errors)

    template_rows = template.get("decisions", [])
    require(template.get("owner_subject") == "John Brandon Turner", "template owner mismatch", errors)
    require(template.get("candidate_sha") == CANDIDATE and template.get("build_id") == BUILD, "template candidate/build mismatch", errors)
    require([row.get("gate_id") for row in template_rows] == EXPECTED_GATES, "template gate identity mismatch", errors)
    require(all(row.get("decision") == "not-decided" for row in template_rows), "historical decision template must remain untouched", errors)
    require(all(value is False for value in template.get("default_without_owner_decision", {}).values()), "historical template defaults changed", errors)

    require(limitations.get("candidate_sha") == CANDIDATE and limitations.get("blocking_limitation_count") == 0, "limitation registry mismatch", errors)
    require(len(limitations.get("items", [])) == 5 and all(item.get("blocking") is False for item in limitations.get("items", [])), "expected five nonblocking limitations", errors)
    require(risks.get("candidate_sha") == CANDIDATE and risks.get("blocking_risk_count") == 0, "risk register mismatch", errors)
    require(risks.get("unresolved_high_critical_security_count") == 0, "unresolved HIGH/CRITICAL security findings", errors)
    require(tester.get("candidate_sha") == CANDIDATE and tester.get("build_id") == BUILD, "tester package candidate/build mismatch", errors)
    require(tester.get("data_classification") == "synthetic-test-only", "tester data boundary changed", errors)
    require(tester.get("supported_profiles") == ["browser", "local-runner"], "tester profiles changed", errors)

    if DECISION_RECORD.is_file():
        decision = load(DECISION_RECORD)
        drows = decision.get("decisions", [])
        dmap = {row.get("gate_id"): row.get("decision") for row in drows}
        require(decision.get("owner_subject") == "John Brandon Turner", "decision owner mismatch", errors)
        require(decision.get("candidate_sha") == CANDIDATE and decision.get("build_id") == BUILD, "decision candidate/build mismatch", errors)
        require([row.get("gate_id") for row in drows] == EXPECTED_GATES, "decision record gate identity mismatch", errors)
        require({gate for gate, state in dmap.items() if state == "approved"} == READY_GATES, "only the two decision-ready gates may be approved", errors)
        require(all(dmap[g] == "not-decided" for g in set(EXPECTED_GATES) - READY_GATES), "non-ready owner gate changed", errors)
        auth = decision.get("authorization_projection", {})
        require(auth.get("tester_access_authorized") is True and auth.get("internal_alpha_release_approved") is True, "approved gate projection mismatch", errors)
        for field in ["real_user_data_authorized", "production_credentials_authorized", "paid_provider_authorized", "public_release_or_deployment_authorized", "broader_ai_automation_authority_authorized", "working_design_standards_promoted"]:
            require(auth.get(field) is False, f"unauthorized broader gate opened: {field}", errors)
        require(gates.get("release_approved") is True, "release approval not projected to gate matrix", errors)
        require(work.get("owner_decision_made") is True and work.get("owner_decision_required") is False, "work state did not record owner decision", errors)
        require(work.get("release_approved") is True and work.get("tester_access_authorized") is True, "work state approved gate projection mismatch", errors)
    else:
        require(gates.get("release_approved") is False, "pre-decision packet must not approve release", errors)
        require(all(row.get("decision") == "not-decided" for row in rows), "pre-decision gate matrix may not make owner decisions", errors)
        require(work.get("owner_decision_required") is True and work.get("owner_decision_made") is False, "pre-decision work state mismatch", errors)

    require(pointer.get("primary_attempt_id") == "IA-D09-owner-decision-evidence-preparation-attempt-001", "current pointer mismatch", errors)
    require(status.get("primary", {}).get("work_item_id") == "IA-D09-OWNER-DECISION", "implementation status primary mismatch", errors)
    require(status.get("primary", {}).get("status") == work.get("status"), "implementation status lifecycle mismatch", errors)
    require(any(row.get("work_item_id") == "IA-D09-OWNER-DECISION" for row in roadmap.get("entries", [])), "roadmap supplement missing IA-D09 owner-decision entry", errors)
    require("does not approve any owner-only gate" in (PACKET_DIR / "IA_D09_OWNER_DECISION_EVIDENCE_PACKET.md").read_text(encoding="utf-8"), "historical packet non-approval boundary changed", errors)

    if errors:
        print("IA-D09 OWNER-DECISION EVIDENCE PACKET: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("IA-D09 OWNER-DECISION EVIDENCE PACKET: PASS")
    print("phase=post-owner-decision" if DECISION_RECORD.is_file() else "phase=pre-owner-decision")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
