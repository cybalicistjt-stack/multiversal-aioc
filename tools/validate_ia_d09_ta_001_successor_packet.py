#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/internal-alpha/tester-access"
CANDIDATE = "de4ead1a93fa19daae3e3e5149c50139abc50f14"
APP_MERGE = "ebdb1fdaf05eb535a70255a41f76b66987a8f17a"
PACKAGE_SHA = "d3d6e223245b71bc7f6265025168d61d5eb9b39447d662233584395ff0f73983"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def req(ok: bool, message: str, errors: list[str]) -> None:
    if not ok:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    roster = load(BASE / "INTERNAL_ALPHA_TESTER_ACCOUNT_ROSTER_v0.1.0.json")
    receipt = load(BASE / "IA_D09_TA_001_SUCCESSOR_VALIDATION_RECEIPT.json")
    work = load(ROOT / "governance/ai/work-state/IA-D09-TA-001-attempt-001.json")
    pointer = load(ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json")
    status = load(ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json")
    roadmap = load(ROOT / "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A12_SUPPLEMENT.json")

    accounts = roster.get("accounts", [])
    req(roster.get("roster_id") == "IA-D09-TESTER-ROSTER-20-001", "roster id mismatch", errors)
    req(roster.get("successor_candidate_sha") == CANDIDATE, "roster candidate mismatch", errors)
    req(roster.get("successor_application_merge") == APP_MERGE, "roster app merge mismatch", errors)
    req(roster.get("successor_package_zip_sha256") == PACKAGE_SHA, "roster package SHA mismatch", errors)
    req(len(accounts) == 20, "roster must contain exactly 20 accounts", errors)
    req(sum(1 for row in accounts if row.get("campaign_role") == "game-master") == 10, "roster GM count mismatch", errors)
    req(sum(1 for row in accounts if row.get("campaign_role") == "player") == 10, "roster Player count mismatch", errors)
    for index in range(1, 19):
        expected = "game-master" if index % 2 else "player"
        row = next((x for x in accounts if x.get("account_id") == f"tester{index}"), {})
        req(row.get("campaign_role") == expected, f"tester{index} role mismatch", errors)

    package = receipt.get("package", {})
    browser = receipt.get("browser_evidence", {})
    windows = receipt.get("windows_evidence", {})
    scope = receipt.get("distribution_scope", {})
    req(receipt.get("successor_candidate_sha") == CANDIDATE, "receipt candidate mismatch", errors)
    req(receipt.get("successor_application_merge") == APP_MERGE and receipt.get("successor_application_merge_verified") is True, "receipt merge mismatch", errors)
    req(package.get("inner_zip_sha256") == PACKAGE_SHA and package.get("workflow_artifact_id") == 9263895118, "receipt package evidence mismatch", errors)
    req(browser.get("scenario_count") == 6 and browser.get("all_passed") is True, "browser evidence mismatch", errors)
    req(windows.get("actual_packaged_powershell_runner") == "passed", "Windows evidence mismatch", errors)
    req(scope.get("tester_github_required") is False, "tester GitHub boundary opened", errors)
    req(scope.get("android_apk") is False, "Android APK incorrectly claimed", errors)
    req(scope.get("data_classification") == "synthetic-test-only", "data boundary mismatch", errors)
    req(scope.get("browser_state_scope") == "local-per-browser-instance", "browser-state boundary mismatch", errors)
    req(scope.get("shared_live_campaign_session_authority") is False, "shared-live authority opened", errors)

    req(work.get("successor_candidate_sha") == CANDIDATE and work.get("package_zip_sha256") == PACKAGE_SHA, "checkpoint exact identity mismatch", errors)
    req(work.get("unresolved_failures") == [], "checkpoint has unresolved failures", errors)
    for field in ("shared_live_campaign_session_authority", "real_user_data_authorized", "production_credentials_authorized", "paid_provider_authorized", "public_release_or_deployment_authorized", "broader_ai_automation_authority_authorized", "working_design_standards_promoted"):
        req(work.get(field) is False, f"closed authority opened: {field}", errors)

    req(pointer.get("primary_attempt_id") == "IA-D09-TA-001-attempt-001", "pointer primary mismatch", errors)
    req(status.get("primary", {}).get("work_item_id") == "IA-D09-TA-001", "compact status work item mismatch", errors)
    entry = next((x for x in roadmap.get("entries", []) if x.get("work_item_id") == "IA-D09-TA-001"), None)
    req(bool(entry), "roadmap missing IA-D09-TA-001", errors)
    if entry:
        req(entry.get("successor_candidate_sha") == CANDIDATE and entry.get("package_zip_sha256") == PACKAGE_SHA, "roadmap exact identity mismatch", errors)
        req(entry.get("shared_live_campaign_session_authority") is False, "roadmap shared-live authority opened", errors)

    approved = bool(work.get("successor_distribution_approved"))
    if approved:
        decision_path = BASE / "IA_D09_TA_001_OWNER_DISTRIBUTION_DECISION_20260816.json"
        req(decision_path.is_file(), "approved lifecycle missing owner decision record", errors)
        if decision_path.is_file():
            decision = load(decision_path)
            req(decision.get("decision") == "approved" and decision.get("distribution_authorized") is True, "approved decision record mismatch", errors)
            req(decision.get("candidate_sha") == CANDIDATE and decision.get("package_sha256") == PACKAGE_SHA, "approved decision exact identity mismatch", errors)
    else:
        req(work.get("owner_decision_required") is True, "pending lifecycle must require owner decision", errors)

    if errors:
        print("IA-D09-TA-001 SUCCESSOR PACKET: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("IA-D09-TA-001 SUCCESSOR PACKET: PASS")
    print(f"candidate=de4ead1a package=d3d6e223 accounts=20 gm=10 player=10 approved={str(approved).lower()} shared_live=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
