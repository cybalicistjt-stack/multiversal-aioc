#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/internal-alpha/tester-access"
CANDIDATE = "de4ead1a93fa19daae3e3e5149c50139abc50f14"
BASE_APP_MERGE = "ebdb1fdaf05eb535a70255a41f76b66987a8f17a"
REPAIR_APP_MERGE = "7cc9fa4a042a461d03c88d69c2b18ed18c0f9e21"
BASE_PACKAGE_SHA = "d3d6e223245b71bc7f6265025168d61d5eb9b39447d662233584395ff0f73983"
HOTFIX_PACKAGE_SHA = "5c9f31c96a3373f927f8d3a7ee6ee821aafeda8d0ae26a0c6cecf94ca129e0de"


def load(path: Path): return json.loads(path.read_text(encoding="utf-8"))
def req(ok: bool, message: str, errors: list[str]) -> None:
    if not ok: errors.append(message)


def main() -> int:
    errors: list[str] = []
    roster = load(BASE / "INTERNAL_ALPHA_TESTER_ACCOUNT_ROSTER_v0.1.0.json")
    base_receipt = load(BASE / "IA_D09_TA_001_SUCCESSOR_VALIDATION_RECEIPT.json")
    decision = load(BASE / "IA_D09_TA_001_HOTFIX2_OWNER_DISTRIBUTION_DECISION_20260816.json")
    work = load(ROOT / "governance/ai/work-state/IA-D09-TA-001-attempt-001.json")
    pointer = load(ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json")
    status = load(ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json")
    roadmap = load(ROOT / "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A12_SUPPLEMENT.json")

    accounts = roster.get("accounts", [])
    req(roster.get("roster_id") == "IA-D09-TESTER-ROSTER-20-001", "roster id mismatch", errors)
    req(roster.get("successor_candidate_sha") == CANDIDATE, "roster candidate mismatch", errors)
    req(roster.get("successor_application_merge") == BASE_APP_MERGE, "roster base app merge mismatch", errors)
    req(roster.get("replacement_application_repair_merge") == REPAIR_APP_MERGE, "roster repair app merge mismatch", errors)
    req(roster.get("approved_distribution_package_sha256") == HOTFIX_PACKAGE_SHA, "roster approved Hotfix 2 SHA mismatch", errors)
    req(roster.get("withdrawn_distribution_package_sha256") == BASE_PACKAGE_SHA, "roster withdrawn base SHA mismatch", errors)
    req(len(accounts) == 20, "roster must contain exactly 20 accounts", errors)
    req(sum(1 for x in accounts if x.get("campaign_role") == "game-master") == 10, "roster GM count mismatch", errors)
    req(sum(1 for x in accounts if x.get("campaign_role") == "player") == 10, "roster Player count mismatch", errors)
    req(all(x.get("provisioning_state") == "approved-for-distribution-hotfix2" for x in accounts), "roster provisioning state mismatch", errors)
    for index in range(1, 19):
        expected = "game-master" if index % 2 else "player"
        row = next((x for x in accounts if x.get("account_id") == f"tester{index}"), {})
        req(row.get("campaign_role") == expected, f"tester{index} role mismatch", errors)

    package = base_receipt.get("package", {})
    browser = base_receipt.get("browser_evidence", {})
    windows = base_receipt.get("windows_evidence", {})
    scope = base_receipt.get("distribution_scope", {})
    req(base_receipt.get("successor_candidate_sha") == CANDIDATE, "base receipt candidate mismatch", errors)
    req(base_receipt.get("successor_application_merge") == BASE_APP_MERGE and base_receipt.get("successor_application_merge_verified") is True, "base receipt merge mismatch", errors)
    req(package.get("inner_zip_sha256") == BASE_PACKAGE_SHA and package.get("workflow_artifact_id") == 9263895118, "base receipt package evidence mismatch", errors)
    req(browser.get("scenario_count") == 6 and browser.get("all_passed") is True, "base browser evidence mismatch", errors)
    req(windows.get("actual_packaged_powershell_runner") == "passed", "base Windows evidence mismatch", errors)
    req(scope.get("tester_github_required") is False and scope.get("android_apk") is False, "base distribution boundary mismatch", errors)
    req(scope.get("shared_live_campaign_session_authority") is False, "base shared-live authority opened", errors)

    replacement = decision.get("replacement_package", {})
    routing = replacement.get("physical_role_routing", {})
    req(decision.get("decision") == "approved", "Hotfix 2 decision not approved", errors)
    req(replacement.get("sha256") == HOTFIX_PACKAGE_SHA, "Hotfix 2 decision SHA mismatch", errors)
    req(replacement.get("application_repair_merge") == REPAIR_APP_MERGE, "Hotfix 2 repair merge mismatch", errors)
    req(routing.get("accounts_tested") == 20 and routing.get("gm_correct") == 10 and routing.get("player_correct") == 10 and routing.get("incorrect_role_routing") == 0 and routing.get("result") == "PASS", "Hotfix 2 physical role-routing evidence mismatch", errors)
    req(decision.get("supersedes_distribution_approval_for_package", {}).get("sha256") == BASE_PACKAGE_SHA, "withdrawn package decision mismatch", errors)

    req(work.get("successor_candidate_sha") == CANDIDATE and work.get("package_zip_sha256") == HOTFIX_PACKAGE_SHA, "checkpoint exact replacement identity mismatch", errors)
    req(work.get("replacement_application_merge") == REPAIR_APP_MERGE, "checkpoint repair merge mismatch", errors)
    req(work.get("successor_distribution_approved") is True and work.get("owner_decision_required") is False, "checkpoint approval mismatch", errors)
    req(work.get("physical_windows_role_routing", {}).get("result") == "PASS", "checkpoint physical routing missing", errors)
    req(work.get("unresolved_failures") == [], "checkpoint has unresolved failures", errors)
    for field in ("shared_live_campaign_session_authority", "real_user_data_authorized", "production_credentials_authorized", "paid_provider_authorized", "public_release_or_deployment_authorized", "broader_ai_automation_authority_authorized", "working_design_standards_promoted"):
        req(work.get(field) is False, f"closed authority opened: {field}", errors)

    req(pointer.get("primary_attempt_id") == "IA-D09-TA-001-attempt-001", "pointer primary mismatch", errors)
    req(status.get("primary", {}).get("work_item_id") == "IA-D09-TA-001", "compact status work item mismatch", errors)
    entry = next((x for x in roadmap.get("entries", []) if x.get("work_item_id") == "IA-D09-TA-001"), None)
    req(bool(entry), "roadmap missing IA-D09-TA-001", errors)
    if entry:
        req(entry.get("successor_candidate_sha") == CANDIDATE, "roadmap candidate mismatch", errors)
        req(entry.get("repair_application_merge") == REPAIR_APP_MERGE, "roadmap repair merge mismatch", errors)
        req(entry.get("approved_package_sha256") == HOTFIX_PACKAGE_SHA, "roadmap Hotfix 2 SHA mismatch", errors)
        req(entry.get("withdrawn_package_sha256") == BASE_PACKAGE_SHA, "roadmap withdrawn SHA mismatch", errors)
        req(entry.get("replacement_distribution_approved") is True and entry.get("owner_decision_required") is False, "roadmap approval mismatch", errors)
        req(entry.get("shared_live_campaign_session_authority") is False, "roadmap shared-live authority opened", errors)

    if errors:
        print("IA-D09-TA-001 SUCCESSOR PACKET: FAIL")
        for error in errors: print(f"- {error}")
        return 1
    print("IA-D09-TA-001 SUCCESSOR PACKET: PASS")
    print("candidate=de4ead1a hotfix2=5c9f31c9 accounts=20 gm=10 player=10 physical=20/20 approved=true shared_live=false")
    return 0


if __name__ == "__main__": raise SystemExit(main())
