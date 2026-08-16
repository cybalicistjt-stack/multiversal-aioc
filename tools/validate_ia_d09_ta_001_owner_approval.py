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
    decision_path = BASE / "IA_D09_TA_001_OWNER_DISTRIBUTION_DECISION_20260816.json"
    roster_path = BASE / "INTERNAL_ALPHA_TESTER_ACCOUNT_ROSTER_v0.1.0.json"
    work_path = ROOT / "governance/ai/work-state/IA-D09-TA-001-attempt-001.json"
    bootstrap_path = ROOT / "governance/ai/runtime/BOOTSTRAP_CURRENT_STATE_AMENDMENT_IA_D09_TA_001_OWNER_APPROVED.md"
    for path in (decision_path, roster_path, work_path, bootstrap_path):
        req(path.is_file(), f"missing required file: {path.relative_to(ROOT)}", errors)

    decision = load(decision_path)
    roster = load(roster_path)
    work = load(work_path)
    pointer = load(ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json")
    status = load(ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json")
    roadmap = load(ROOT / "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A12_SUPPLEMENT.json")

    req(decision.get("decision") == "approved", "owner decision must be approved", errors)
    req(decision.get("distribution_authorized") is True, "distribution authorization missing", errors)
    req(decision.get("candidate_sha") == CANDIDATE, "decision candidate mismatch", errors)
    req(decision.get("application_merge") == APP_MERGE, "decision app merge mismatch", errors)
    req(decision.get("package_sha256") == PACKAGE_SHA, "decision package SHA mismatch", errors)
    scope = decision.get("approved_scope", {})
    req(scope.get("tester_accounts") == 20 and scope.get("game_master_accounts") == 10 and scope.get("player_accounts") == 10, "approved roster counts mismatch", errors)
    req(scope.get("android_apk") is False, "Android APK authority opened", errors)
    req(scope.get("identity_mode") == "local-test-identity-selector", "identity boundary mismatch", errors)
    req(scope.get("data_classification") == "synthetic-test-only", "data boundary mismatch", errors)
    req(scope.get("browser_state_scope") == "local-per-browser-instance", "browser-state boundary mismatch", errors)
    req(scope.get("shared_live_campaign_session_authority") is False, "shared-live authority opened", errors)

    accounts = roster.get("accounts", [])
    req(roster.get("successor_candidate_sha") == CANDIDATE, "roster candidate mismatch", errors)
    req(roster.get("successor_application_merge") == APP_MERGE, "roster app merge mismatch", errors)
    req(roster.get("successor_package_zip_sha256") == PACKAGE_SHA, "roster package SHA mismatch", errors)
    req(len(accounts) == 20, "roster account count mismatch", errors)
    req(all(row.get("provisioning_state") == "approved-for-distribution" for row in accounts), "all accounts must be approved for distribution", errors)
    req(sum(1 for row in accounts if row.get("campaign_role") == "game-master") == 10, "GM count mismatch", errors)
    req(sum(1 for row in accounts if row.get("campaign_role") == "player") == 10, "Player count mismatch", errors)
    inv = roster.get("invariants", {})
    req(inv.get("successor_distribution_owner_approved") is True, "roster approval invariant missing", errors)
    for field in ("github_account_required_for_tester", "production_identity_provider_selected", "real_user_data_authorized", "production_credentials_authorized", "public_release_or_deployment_authorized", "native_android_package_included", "shared_live_campaign_session_authority"):
        req(inv.get(field) is False, f"closed roster invariant opened: {field}", errors)

    req(work.get("status") in {"ready_for_review", "completed_verified"}, "checkpoint lifecycle mismatch", errors)
    req(work.get("owner_decision_required") is False and work.get("owner_decision_made") is True, "checkpoint owner decision mismatch", errors)
    req(work.get("successor_distribution_approved") is True, "checkpoint distribution approval missing", errors)
    req(work.get("successor_candidate_sha") == CANDIDATE and work.get("package_zip_sha256") == PACKAGE_SHA, "checkpoint exact identity mismatch", errors)
    for field in ("shared_live_campaign_session_authority", "real_user_data_authorized", "production_credentials_authorized", "paid_provider_authorized", "public_release_or_deployment_authorized", "broader_ai_automation_authority_authorized", "working_design_standards_promoted"):
        req(work.get(field) is False, f"closed checkpoint authority opened: {field}", errors)

    req(pointer.get("primary_attempt_id") == "IA-D09-TA-001-attempt-001", "pointer primary mismatch", errors)
    primary = next((x for x in pointer.get("active_attempts", []) if x.get("attempt_id") == "IA-D09-TA-001-attempt-001"), None)
    req(bool(primary) and primary.get("status") in {"ready_for_review", "completed_verified"}, "pointer lifecycle mismatch", errors)
    req(status.get("primary", {}).get("owner_decision_required") is False, "compact status still requires owner decision", errors)

    entry = next((x for x in roadmap.get("entries", []) if x.get("work_item_id") == "IA-D09-TA-001"), None)
    req(bool(entry), "roadmap missing IA-D09-TA-001", errors)
    if entry:
        req(entry.get("successor_candidate_sha") == CANDIDATE and entry.get("package_zip_sha256") == PACKAGE_SHA, "roadmap exact identity mismatch", errors)
        req(entry.get("successor_distribution_approved") is True and entry.get("owner_decision_required") is False, "roadmap approval mismatch", errors)
        req(entry.get("shared_live_campaign_session_authority") is False, "roadmap shared-live authority opened", errors)

    bootstrap = bootstrap_path.read_text(encoding="utf-8")
    for phrase in ("explicitly approved", "Testers do not need GitHub accounts", "No Android APK is included or approved", "does **not** authorize synchronized live GM/Player Campaign/session authority", "There is no automatic A13"):
        req(phrase in bootstrap, f"bootstrap missing boundary: {phrase}", errors)

    if errors:
        print("IA-D09-TA-001 OWNER APPROVAL: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("IA-D09-TA-001 OWNER APPROVAL: PASS")
    print("candidate=de4ead1a package=d3d6e223 accounts=20 gm=10 player=10 approved=true shared_live=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
