#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/internal-alpha/tester-access"
CANDIDATE = "de4ead1a93fa19daae3e3e5149c50139abc50f14"
APP_MERGE = "ebdb1fdaf05eb535a70255a41f76b66987a8f17a"
PACKAGE_SHA = "d3d6e223245b71bc7f6265025168d61d5eb9b39447d662233584395ff0f73983"
PREDECESSOR = "56b127f1fc01eebe5c73ba0472a5b6496fe92b5e"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def req(ok: bool, message: str, errors: list[str]) -> None:
    if not ok:
        errors.append(message)


def main() -> int:
    errors: list[str] = []
    required = [
        BASE / "INTERNAL_ALPHA_TESTER_ACCOUNT_ROSTER_v0.1.0.json",
        BASE / "INTERNAL_ALPHA_TESTER_ACCESS_EXECUTION_PLAN_v0.1.0.md",
        BASE / "IA_D09_TA_001_SUCCESSOR_VALIDATION_RECEIPT.json",
        BASE / "IA_D09_TA_001_OWNER_DISTRIBUTION_DECISION_TEMPLATE.json",
        ROOT / "governance/ai/work-state/IA-D09-TA-001-attempt-001.json",
        ROOT / "governance/ai/runtime/BOOTSTRAP_CURRENT_STATE_AMENDMENT_IA_D09_TA_001_SUCCESSOR_PENDING_OWNER.md",
    ]
    for path in required:
        req(path.is_file(), f"missing required file: {path.relative_to(ROOT)}", errors)

    roster = load(BASE / "INTERNAL_ALPHA_TESTER_ACCOUNT_ROSTER_v0.1.0.json")
    receipt = load(BASE / "IA_D09_TA_001_SUCCESSOR_VALIDATION_RECEIPT.json")
    decision = load(BASE / "IA_D09_TA_001_OWNER_DISTRIBUTION_DECISION_TEMPLATE.json")
    work = load(ROOT / "governance/ai/work-state/IA-D09-TA-001-attempt-001.json")
    pointer = load(ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json")
    status = load(ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json")
    roadmap = load(ROOT / "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A12_SUPPLEMENT.json")

    accounts = roster.get("accounts", [])
    req(roster.get("roster_id") == "IA-D09-TESTER-ROSTER-20-001", "roster id mismatch", errors)
    req(roster.get("successor_candidate_sha") == CANDIDATE, "roster successor candidate mismatch", errors)
    req(roster.get("successor_application_merge") == APP_MERGE, "roster app merge mismatch", errors)
    req(roster.get("successor_package_zip_sha256") == PACKAGE_SHA, "roster package SHA mismatch", errors)
    req(len(accounts) == 20, "roster must contain exactly 20 accounts", errors)
    req(sum(1 for row in accounts if row.get("campaign_role") == "game-master") == 10, "roster GM count mismatch", errors)
    req(sum(1 for row in accounts if row.get("campaign_role") == "player") == 10, "roster Player count mismatch", errors)
    req(all(row.get("provisioning_state") == "validated-pending-owner-approval" for row in accounts), "all accounts must remain pending owner approval", errors)
    by_id = {row.get("account_id"): row for row in accounts}
    req(by_id.get("john-gm", {}).get("campaign_role") == "game-master", "John GM role mismatch", errors)
    req(by_id.get("john-player", {}).get("campaign_role") == "player", "John Player role mismatch", errors)
    req(by_id.get("john-gm", {}).get("subject_id") != by_id.get("john-player", {}).get("subject_id"), "John identities must remain separate", errors)
    for index in range(1, 19):
        expected = "game-master" if index % 2 else "player"
        req(by_id.get(f"tester{index}", {}).get("campaign_role") == expected, f"tester{index} role mismatch", errors)

    invariants = roster.get("invariants", {})
    for field in [
        "github_account_required_for_tester",
        "production_identity_provider_selected",
        "real_user_data_authorized",
        "production_credentials_authorized",
        "public_release_or_deployment_authorized",
        "native_android_package_included",
        "shared_live_campaign_session_authority",
        "successor_distribution_owner_approved",
    ]:
        req(invariants.get(field) is False, f"roster invariant opened: {field}", errors)

    req(receipt.get("state") == "validated_pending_owner_distribution_approval", "receipt lifecycle mismatch", errors)
    req(receipt.get("successor_candidate_sha") == CANDIDATE, "receipt candidate mismatch", errors)
    req(receipt.get("successor_application_merge") == APP_MERGE and receipt.get("successor_application_merge_verified") is True, "receipt merge evidence mismatch", errors)
    package = receipt.get("package", {})
    req(package.get("inner_zip_sha256") == PACKAGE_SHA, "receipt package SHA mismatch", errors)
    req(package.get("workflow_artifact_id") == 9263895118, "package artifact id mismatch", errors)
    req(package.get("workflow_run") == 31948141484 and package.get("workflow_job") == 95167328126, "package validation run mismatch", errors)
    browser = receipt.get("browser_evidence", {})
    req(browser.get("workflow_run") == 31948141491 and browser.get("workflow_job") == 95167328143, "browser validation run mismatch", errors)
    req(browser.get("scenario_count") == 6 and browser.get("all_passed") is True, "headed browser evidence mismatch", errors)
    windows = receipt.get("windows_evidence", {})
    req(windows.get("workflow_job") == 95167328019 and windows.get("actual_packaged_powershell_runner") == "passed", "Windows package evidence mismatch", errors)
    scope = receipt.get("distribution_scope", {})
    req(scope.get("tester_github_required") is False, "tester GitHub requirement opened", errors)
    req(scope.get("android_apk") is False, "Android APK incorrectly claimed", errors)
    req(scope.get("data_classification") == "synthetic-test-only", "receipt data boundary mismatch", errors)
    req(scope.get("browser_state_scope") == "local-per-browser-instance", "browser state boundary mismatch", errors)
    req(scope.get("shared_live_campaign_session_authority") is False, "shared live authority incorrectly opened", errors)
    owner = receipt.get("owner_decision", {})
    req(owner.get("required") is True and owner.get("made") is False and owner.get("successor_distribution_approved") is False, "successor owner hold must remain closed", errors)

    req(decision.get("candidate_sha") == CANDIDATE and decision.get("package_sha256") == PACKAGE_SHA, "decision template candidate/package mismatch", errors)
    req(decision.get("decision") == "not-decided", "decision template must remain not-decided", errors)
    req(decision.get("if_approved_scope", {}).get("shared_live_campaign_session_authority") is False, "decision template may not open shared live authority", errors)

    req(work.get("status") == "blocked_owner", "checkpoint must be blocked_owner", errors)
    req(work.get("owner_decision_required") is True and work.get("owner_decision_made") is False, "checkpoint owner hold mismatch", errors)
    req(work.get("predecessor_owner_approved_candidate") == PREDECESSOR, "predecessor approval identity mismatch", errors)
    req(work.get("successor_candidate_sha") == CANDIDATE, "checkpoint successor candidate mismatch", errors)
    req(work.get("successor_distribution_approved") is False, "checkpoint must not approve distribution", errors)
    req(work.get("shared_live_campaign_session_authority") is False, "checkpoint shared live authority must remain false", errors)
    req(work.get("unresolved_failures") == [], "checkpoint has unresolved failures", errors)

    req(pointer.get("primary_attempt_id") == "IA-D09-TA-001-attempt-001", "pointer primary attempt mismatch", errors)
    primary = pointer.get("active_attempts", [None])[0]
    req(isinstance(primary, dict) and primary.get("work_item_id") == "IA-D09-TA-001" and primary.get("status") == "blocked_owner", "pointer primary work mismatch", errors)
    req(pointer.get("deferred_tracks") == [], "pointer may not auto-activate future shared runtime", errors)
    req(status.get("primary", {}).get("work_item_id") == "IA-D09-TA-001", "compact status work item mismatch", errors)
    req(status.get("primary", {}).get("status") == "blocked_owner" and status.get("primary", {}).get("owner_decision_required") is True, "compact status owner hold mismatch", errors)

    entry = next((row for row in roadmap.get("entries", []) if row.get("work_item_id") == "IA-D09-TA-001"), None)
    req(bool(entry), "roadmap supplement missing IA-D09-TA-001", errors)
    if entry:
        req(entry.get("validation_state") == "validated" and entry.get("state") == "blocked_owner", "roadmap lifecycle mismatch", errors)
        req(entry.get("successor_candidate_sha") == CANDIDATE and entry.get("package_zip_sha256") == PACKAGE_SHA, "roadmap candidate/package mismatch", errors)
        req(entry.get("successor_distribution_approved") is False and entry.get("owner_decision_required") is True, "roadmap owner hold mismatch", errors)
        req(entry.get("shared_live_campaign_session_authority") is False, "roadmap shared live authority opened", errors)

    bootstrap = (ROOT / "governance/ai/runtime/BOOTSTRAP_CURRENT_STATE_AMENDMENT_IA_D09_TA_001_SUCCESSOR_PENDING_OWNER.md").read_text(encoding="utf-8")
    for phrase in [
        "validated but not yet approved for distribution",
        "Testers do not need GitHub accounts",
        "no APK is included or approved",
        "does **not** synchronize live Campaign/session actions",
        "There is no automatic A13",
    ]:
        req(phrase in bootstrap, f"bootstrap missing boundary: {phrase}", errors)

    if errors:
        print("IA-D09-TA-001 SUCCESSOR PACKET: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("IA-D09-TA-001 SUCCESSOR PACKET: PASS")
    print("candidate=de4ead1a package=d3d6e223 accounts=20 gm=10 player=10 owner_approval=false shared_live=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
