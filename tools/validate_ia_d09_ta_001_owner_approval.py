#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/internal-alpha/tester-access"
HOTFIX_SHA = "5c9f31c96a3373f927f8d3a7ee6ee821aafeda8d0ae26a0c6cecf94ca129e0de"
REPAIR_MERGE = "7cc9fa4a042a461d03c88d69c2b18ed18c0f9e21"
WITHDRAWN_SHA = "d3d6e223245b71bc7f6265025168d61d5eb9b39447d662233584395ff0f73983"


def load(path: Path): return json.loads(path.read_text(encoding="utf-8"))
def req(ok: bool, message: str, errors: list[str]) -> None:
    if not ok: errors.append(message)


def main() -> int:
    errors: list[str] = []
    decision_path = BASE / "IA_D09_TA_001_HOTFIX2_OWNER_DISTRIBUTION_DECISION_20260816.json"
    roster_path = BASE / "INTERNAL_ALPHA_TESTER_ACCOUNT_ROSTER_v0.1.0.json"
    work_path = ROOT / "governance/ai/work-state/IA-D09-TA-001-attempt-001.json"
    bootstrap_path = ROOT / "governance/ai/runtime/BOOTSTRAP_CURRENT_STATE_AMENDMENT_IA_D09_TA_001_HOTFIX2_OWNER_APPROVED.md"
    for path in (decision_path, roster_path, work_path, bootstrap_path):
        req(path.is_file(), f"missing required file: {path.relative_to(ROOT)}", errors)

    decision = load(decision_path)
    roster = load(roster_path)
    work = load(work_path)
    pointer = load(ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json")
    status = load(ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json")
    roadmap = load(ROOT / "governance/ai/runtime/ROADMAP_INDEX_STAGE_A_A12_SUPPLEMENT.json")

    replacement = decision.get("replacement_package", {})
    routing = replacement.get("physical_role_routing", {})
    req(decision.get("owner") == "John Brandon Turner", "owner mismatch", errors)
    req(decision.get("decision") == "approved", "owner decision must be approved", errors)
    req(decision.get("scope") == "bounded 20-account Internal Alpha distribution only", "approval scope mismatch", errors)
    req(replacement.get("file_name") == "Multiversal-Internal-Alpha-Windows-HOTFIX2-a4e262167aa9.zip", "approved file mismatch", errors)
    req(replacement.get("sha256") == HOTFIX_SHA, "approved SHA mismatch", errors)
    req(replacement.get("application_repair_merge") == REPAIR_MERGE, "repair merge mismatch", errors)
    req(replacement.get("marker") == "IA-HOTFIX-ACCOUNT-DISPATCH-2" and replacement.get("default_port") == 8877, "Hotfix marker/port mismatch", errors)
    req(routing.get("accounts_tested") == 20 and routing.get("gm_correct") == 10 and routing.get("player_correct") == 10 and routing.get("incorrect_role_routing") == 0 and routing.get("result") == "PASS", "physical role matrix mismatch", errors)
    req(decision.get("supersedes_distribution_approval_for_package", {}).get("sha256") == WITHDRAWN_SHA, "withdrawn approved package mismatch", errors)
    req(decision.get("owner_only_scope_expansion_inferred") is False, "scope expansion was inferred", errors)
    for field in ("shared_live_campaign_session_authority", "real_user_data_authorized", "production_credentials_authorized", "paid_provider_authorized", "public_release_or_deployment_authorized", "broader_ai_automation_authority_authorized", "working_design_standards_promoted", "android_apk_authorized"):
        req(decision.get("preserved_boundaries", {}).get(field) is False, f"closed decision authority opened: {field}", errors)

    accounts = roster.get("accounts", [])
    req(roster.get("approved_distribution_package_sha256") == HOTFIX_SHA, "roster approved SHA mismatch", errors)
    req(roster.get("replacement_application_repair_merge") == REPAIR_MERGE, "roster repair merge mismatch", errors)
    req(roster.get("withdrawn_distribution_package_sha256") == WITHDRAWN_SHA, "roster withdrawn SHA mismatch", errors)
    req(len(accounts) == 20, "roster account count mismatch", errors)
    req(all(row.get("provisioning_state") == "approved-for-distribution-hotfix2" for row in accounts), "roster distribution state mismatch", errors)
    req(sum(1 for row in accounts if row.get("campaign_role") == "game-master") == 10, "GM count mismatch", errors)
    req(sum(1 for row in accounts if row.get("campaign_role") == "player") == 10, "Player count mismatch", errors)
    req(roster.get("physical_windows_role_routing", {}).get("result") == "PASS", "roster physical evidence missing", errors)

    req(work.get("status") == "completed_verified", "checkpoint lifecycle mismatch", errors)
    req(work.get("owner_decision_required") is False and work.get("owner_decision_made") is True, "checkpoint owner decision mismatch", errors)
    req(work.get("successor_distribution_approved") is True, "checkpoint distribution approval missing", errors)
    req(work.get("package_zip_sha256") == HOTFIX_SHA and work.get("replacement_application_merge") == REPAIR_MERGE, "checkpoint exact replacement identity mismatch", errors)
    for field in ("shared_live_campaign_session_authority", "real_user_data_authorized", "production_credentials_authorized", "paid_provider_authorized", "public_release_or_deployment_authorized", "broader_ai_automation_authority_authorized", "working_design_standards_promoted"):
        req(work.get(field) is False, f"closed checkpoint authority opened: {field}", errors)

    req(pointer.get("primary_attempt_id") == "IA-D09-TA-001-attempt-001", "pointer primary mismatch", errors)
    req(pointer.get("bootstrap_current_state_amendment") == "governance/ai/runtime/BOOTSTRAP_CURRENT_STATE_AMENDMENT_IA_D09_TA_001_HOTFIX2_OWNER_APPROVED.md", "pointer bootstrap amendment mismatch", errors)
    req(status.get("primary", {}).get("owner_decision_required") is False, "compact status still requires owner decision", errors)

    entry = next((x for x in roadmap.get("entries", []) if x.get("work_item_id") == "IA-D09-TA-001"), None)
    req(bool(entry), "roadmap missing IA-D09-TA-001", errors)
    if entry:
        req(entry.get("approved_package_sha256") == HOTFIX_SHA and entry.get("repair_application_merge") == REPAIR_MERGE, "roadmap exact replacement identity mismatch", errors)
        req(entry.get("replacement_distribution_approved") is True and entry.get("owner_decision_required") is False, "roadmap approval mismatch", errors)
        req(entry.get("shared_live_campaign_session_authority") is False, "roadmap shared-live authority opened", errors)

    bootstrap = bootstrap_path.read_text(encoding="utf-8")
    for phrase in ("explicitly approved", "20 accounts were physically exercised", "Testers do not need GitHub accounts", "no APK is approved", "does **not** authorize synchronized live GM/Player Campaign/session authority", "There is no automatic A13"):
        req(phrase in bootstrap, f"bootstrap missing boundary: {phrase}", errors)

    if errors:
        print("IA-D09-TA-001 HOTFIX2 OWNER APPROVAL: FAIL")
        for error in errors: print(f"- {error}")
        return 1
    print("IA-D09-TA-001 HOTFIX2 OWNER APPROVAL: PASS")
    print("package=5c9f31c9 accounts=20 gm=10 player=10 physical=20/20 approved=true shared_live=false")
    return 0


if __name__ == "__main__": raise SystemExit(main())
