#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/internal-alpha/owner-decision"
CANDIDATE = "56b127f1fc01eebe5c73ba0472a5b6496fe92b5e"
BUILD = "5033f55d3344209c1719d6003d1369b4bc201c74ba9d64f046767263daee5a45"
APPROVED = {"authorize Internal Alpha tester access", "approve Internal Alpha release"}
ALL = [
    "authorize Internal Alpha tester access",
    "authorize real-user data collection",
    "authorize production credentials",
    "authorize paid provider commitment",
    "approve Internal Alpha release",
    "approve public release or deployment",
    "promote AI/automation authority",
    "promote working/noncanonical design standards",
]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    def req(ok: bool, msg: str):
        if not ok: errors.append(msg)

    record = load(BASE / "IA_D09_OWNER_DECISION_RECORD_20260816.json")
    gates = load(BASE / "IA_D09_OWNER_GATE_READINESS.json")
    tester = load(BASE / "IA_D09_TESTER_ENTRY_DECISION_PACKAGE.json")
    receipt = load(BASE / "IA_D09_OWNER_DECISION_PREPARATION_RECEIPT.json")
    completion = BASE / "IA_D09_OWNER_DECISION_COMPLETION_RECEIPT.json"
    work = load(ROOT / "governance/ai/work-state/IA-D09-owner-decision-evidence-preparation-attempt-001.json")
    pointer = load(ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json")
    status = load(ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json")
    roadmap = load(ROOT / "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A12_SUPPLEMENT.json")

    req(record.get("owner_subject") == "John Brandon Turner", "owner mismatch")
    req(record.get("candidate_sha") == CANDIDATE and record.get("build_id") == BUILD, "candidate/build mismatch")
    req(record.get("decision_source") == "Owner explicit instruction in Multiversal project conversation: Approve both", "decision source mismatch")
    rows = record.get("decisions", [])
    req([r.get("gate_id") for r in rows] == ALL, "decision gate identity/order mismatch")
    dmap = {r.get("gate_id"): r.get("decision") for r in rows}
    req({g for g, state in dmap.items() if state == "approved"} == APPROVED, "approved gate set mismatch")
    req(all(dmap[g] == "not-decided" for g in set(ALL) - APPROVED), "non-ready gate changed")

    auth = record.get("authorization_projection", {})
    req(auth.get("tester_access_authorized") is True and auth.get("internal_alpha_release_approved") is True, "approved authorization projection mismatch")
    for field in ["real_user_data_authorized", "production_credentials_authorized", "paid_provider_authorized", "public_release_or_deployment_authorized", "broader_ai_automation_authority_authorized", "working_design_standards_promoted"]:
        req(auth.get(field) is False, f"broader authorization opened: {field}")

    grows = {r.get("gate_id"): r for r in gates.get("gates", [])}
    req(gates.get("release_approved") is True, "gate matrix release projection mismatch")
    req(grows.get("authorize Internal Alpha tester access", {}).get("decision") == "approved", "gate matrix tester decision mismatch")
    req(grows.get("approve Internal Alpha release", {}).get("decision") == "approved", "gate matrix release decision mismatch")
    req(all(grows[g].get("decision") == "not-decided" for g in set(ALL) - APPROVED), "gate matrix broader decision changed")

    req(tester.get("owner_access_decision") == "approved" and tester.get("tester_access_authorized") is True, "tester package did not project approval")
    req(tester.get("data_classification") == "synthetic-test-only", "tester data classification broadened")
    req(tester.get("supported_profiles") == ["browser", "local-runner"], "tester profile scope broadened")

    req(receipt.get("owner_decisions_made") == 2 and receipt.get("release_approved") is True and receipt.get("tester_access_authorized") is True, "receipt approval projection mismatch")
    for field in ["real_user_data_authorized", "production_credentials_authorized", "paid_provider_authorized", "public_release_or_deployment_authorized", "broader_ai_automation_authority_authorized", "working_design_standards_promoted"]:
        req(receipt.get(field) is False, f"receipt broader authorization opened: {field}")

    req(work.get("owner_decision_made") is True and work.get("owner_decision_required") is False, "checkpoint owner decision state mismatch")
    req(work.get("release_approved") is True and work.get("tester_access_authorized") is True, "checkpoint approved gate projection mismatch")
    req(work.get("status") in {"ready_for_review", "completed_verified"}, "owner decision lifecycle mismatch")
    req(pointer.get("primary_attempt_id") == work.get("attempt_id"), "pointer primary mismatch")
    req(status.get("primary", {}).get("status") == work.get("status"), "compact status mismatch")

    entry = next((e for e in roadmap.get("entries", []) if e.get("work_item_id") == "IA-D09-OWNER-DECISION"), None)
    req(bool(entry), "roadmap owner-decision entry missing")
    if entry:
        req(set(entry.get("approved_gates", [])) == APPROVED, "roadmap approved gates mismatch")
        req(entry.get("release_approved") is True and entry.get("tester_access_authorized") is True, "roadmap approval projection mismatch")
        req(entry.get("automatic_a13") is False, "automatic A13 must remain false")

    if work.get("status") == "completed_verified":
        req(completion.is_file(), "completion receipt missing")
        if completion.is_file():
            c = load(completion)
            req(c.get("state") == "completed_verified", "completion receipt state mismatch")
            req(c.get("approval_merge_commit") == "437250843ce3a366111cf16af40e60465d009dfc", "approval merge mismatch")
            req(c.get("tester_access_authorized") is True and c.get("internal_alpha_release_approved") is True, "completion approved gates mismatch")

    bootstrap = (ROOT / "governance/ai/runtime/BOOTSTRAP_CURRENT_STATE_AMENDMENT_IA_D09_OWNER_DECISION_APPROVED.md").read_text(encoding="utf-8")
    req("Internal Alpha tester access — approved" in bootstrap, "bootstrap tester approval missing")
    req("Internal Alpha release — approved" in bootstrap, "bootstrap release approval missing")
    req("There is no automatic A13" in bootstrap, "bootstrap automatic-A13 boundary missing")

    if errors:
        print("IA-D09 OWNER DECISION RECORD: FAIL")
        for error in errors: print(f"- {error}")
        return 1
    print("IA-D09 OWNER DECISION RECORD: PASS")
    print(f"status={work.get('status')} approved=2 undecided=6 broader_authority=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
