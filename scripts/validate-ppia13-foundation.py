#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
FEATURES = ROOT / "governance/application-planning/internal-alpha/feature-packets"

FILES = {
    "manifest": BASE / "PPIA-13_SOURCE_MANIFEST_v0.1.0.json",
    "taxonomy": BASE / "PPIA-13_TEACHING_CONTENT_TAXONOMY_v0.1.0.json",
    "authority": BASE / "PPIA-13_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json",
    "delivery": BASE / "PPIA-13_AUDIENCE_CONTEXT_AND_DELIVERY_MATRIX_v0.1.0.json",
    "cases": BASE / "PPIA-13_FOUNDATION_REFERENCE_CASES_v0.1.0.json",
}
INVENTORY = BASE / "PPIA-13_SOURCE_AND_TEACHING_SURFACE_INVENTORY.md"
CANDIDATE = BASE / "PPIA-13_FOUNDATION_CANDIDATE.md"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-13-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
F025 = FEATURES / "MV-IA-F025_ONBOARDING_HELP_DIAGNOSTICS_AND_ISSUE_REPORTING.md"
F025_MATRIX = FEATURES / "MV-IA-F025_ONBOARDING_SUPPORT_MATRIX.json"
F003 = FEATURES / "MV-IA-F003_IDENTITY_DASHBOARD_AND_WORKSPACE_SELECTION.md"
F004 = FEATURES / "MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md"
F006 = FEATURES / "MV-IA-F006_FIRST_PLAYABLE_ACTION_AND_GM_APPROVAL_LOOP.md"
F020 = FEATURES / "MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md"
F021 = FEATURES / "MV-IA-F021_AUTOSAVE_RECONNECT_RECOVERY_AND_BOUNDED_OFFLINE_USE.md"


def fail(msg: str) -> None:
    raise SystemExit("PPIA-13 FOUNDATION: FAIL — " + msg)


def req(condition: bool, msg: str) -> None:
    if not condition:
        fail(msg)


def load(path: Path):
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    docs = {key: load(path) for key, path in FILES.items()}
    backlog, checkpoint, pointer, status = map(load, (BACKLOG, CHECKPOINT, POINTER, STATUS))
    for path in (INVENTORY, CANDIDATE, F025, F025_MATRIX, F003, F004, F006, F020, F021):
        req(path.exists(), f"missing source/artifact {path.relative_to(ROOT)}")

    manifest = docs["manifest"]
    req(manifest.get("work_item_id") == "PPIA-13", "manifest work item changed")
    req(manifest.get("evidence_classes") == [
        "source_truth", "inherited_contract", "project_source_design_contract",
        "authored_teaching_content", "delivery_context_metadata", "unresolved_gap"
    ], "six evidence/provenance classes changed")
    primary = manifest.get("primary_inherited_contract", {})
    req(primary.get("feature_id") == "MV-IA-F025" and primary.get("version") == "0.1.0", "F025 primary authority changed")
    req(primary.get("default_help_decision") == "deny-unless-topic-is-public-or-context-authorized", "F025 default Help decision changed")
    req(primary.get("default_diagnostic_decision") == "exclude" and primary.get("default_issue_decision") == "deny", "F025 diagnostic/issue defaults changed")
    req(primary.get("inherited_counts") == {
        "roles":9,"onboarding_stages":10,"help_contexts":20,"issue_categories":16,
        "severity_values":5,"protected_diagnostic_surfaces":24,"required_denied_cases":26,"acceptance_criteria":20
    }, "F025 inherited counts changed")
    req([x.get("id") for x in manifest.get("repository_sources", [])] == [f"P13-SRC-{i:03d}" for i in range(1,9)], "repository source manifest IDs changed")
    gaps = {x.get("id"): x for x in manifest.get("explicit_source_gaps", [])}
    req(set(gaps) == {"P13-GAP-001", "P13-GAP-002"}, "explicit source-gap set changed")
    req("F024" in gaps["P13-GAP-001"].get("subject", "") and "Do not invent" in gaps["P13-GAP-001"].get("foundation_rule", ""), "F024 source-gap boundary missing")

    f025_matrix = load(F025_MATRIX)
    req(len(f025_matrix.get("roles", [])) == 9, "canonical F025 role count changed")
    req(len(f025_matrix.get("onboardingStages", [])) == 10, "canonical F025 onboarding stage count changed")
    req(len(f025_matrix.get("helpContexts", [])) == 20, "canonical F025 help-context count changed")
    req(len(f025_matrix.get("protectedDiagnosticSurfaces", [])) == 24, "canonical F025 protected diagnostic count changed")
    req(len(f025_matrix.get("requiredDeniedCases", [])) == 26, "canonical F025 denied-case count changed")
    req(f025_matrix.get("implementationAuthorized") is False and f025_matrix.get("internalAlphaReleaseAuthorized") is False and f025_matrix.get("productionAuthorized") is False and f025_matrix.get("publicReleaseAuthorized") is False, "F025 authorization boundary changed")

    taxonomy = docs["taxonomy"]
    req([x.get("id") for x in taxonomy.get("content_types", [])] == [f"P13-TC-{i:03d}" for i in range(1,13)], "12 teaching-content types changed")
    req([x.get("id") for x in taxonomy.get("trigger_classes", [])] == [f"P13-TR-{i:03d}" for i in range(1,13)], "12 trigger classes changed")
    req([x.get("id") for x in taxonomy.get("teaching_surfaces", [])] == [f"P13-SF-{i:03d}" for i in range(1,19)], "18 teaching surfaces changed")
    req(taxonomy.get("primary_human_teaching_roles") == ["player","game-master","content-creator"], "primary Player/GM/Creator audience changed")
    req(len(taxonomy.get("audience_roles", [])) == 9, "nine-role teaching coverage changed")
    rules = taxonomy.get("delivery_rules", {})
    for key in ("preserve_return_context","contextual_help_replayable","dismissal_must_not_remove_required_access_to_help","permission_filter_before_derivative"):
        req(rules.get(key) is True, f"teaching delivery rule changed: {key}")
    for key in ("forced_modal_chain_default","hidden_state_may_be_used_to_hint_existence","generated_teaching_is_authoritative_game_truth","tutorial_campaign_is_canonical_content","color_only_semantics","hover_only_access"):
        req(rules.get(key) is False, f"teaching prohibition changed: {key}")

    authority = docs["authority"]
    req([x.get("id") for x in authority.get("authority_domains", [])] == [f"P13-AU-{i:03d}" for i in range(1,11)], "10 authority domains changed")
    blocking = " ".join(authority.get("blocking_invariants", [])).lower()
    for phrase in (
        "never creates or modifies gameplay mechanics", "permission filtering occurs before help search",
        "hidden object", "local draft", "offline state never implies authoritative mutation",
        "mobile", "screen-reader", "ai-assisted teaching", "tutorial-campaign", "ppia-14",
        "f024", "no application runtime"
    ):
        req(phrase in blocking, f"blocking invariant missing {phrase!r}")
    pipeline = authority.get("permission_safe_pipeline", [])
    req(len(pipeline) == 8 and pipeline[0] == "resolve subject and active context" and "filter" in pipeline[2] and pipeline[-1].startswith("optional AI"), "permission-safe teaching pipeline changed")
    req(set(authority.get("p14_handoff", {})) >= {"owned_here","owned_by_ppia14","rule"}, "PPIA-14 handoff missing")

    delivery = docs["delivery"]
    req(len(delivery.get("role_profiles", [])) == 9, "nine role profiles changed")
    req([x.get("id") for x in delivery.get("foundation_journeys", [])] == [f"P13-JR-{i:03d}" for i in range(1,6)], "five Foundation journeys changed")
    req(len(delivery.get("context_rules", [])) == 12, "12 context rules changed")
    access = delivery.get("accessibility_delivery", {})
    for key in ("keyboard_complete","touch_complete","screen_reader_complete","mobile_single_focus_supported","high_zoom_supported","reduced_motion_supported","noncolor_equivalent_required"):
        req(access.get(key) is True, f"accessibility requirement changed: {key}")
    req(delivery.get("resume_and_dismissal", {}).get("preserve_return_context") is True, "return-context preservation changed")

    cases = docs["cases"]
    req(cases.get("classification") == "synthetic_qa_foundation_fixture" and cases.get("noncanonical") is True, "Foundation fixture classification changed")
    req(cases.get("case_count") == 30 and len(cases.get("cases", [])) == 30, "30 Foundation cases changed")
    req([x.get("id") for x in cases.get("cases", [])] == [f"PPIA13-FC-{i:03d}" for i in range(1,31)], "Foundation case IDs changed")
    case_text = json.dumps(cases, ensure_ascii=False).lower()
    for phrase in ("player-first-launch","gm-first-launch","creator-first-launch","hidden-object-help-search","first-action-pending-gm","offline-read-only","ambiguous-submit","pack-context-source-gap","mobile-single-focus","keyboard-only-walkthrough","screen-reader-nonvisual","tutorial-campaign-player","help-replay-no-duplicate-effects"):
        req(phrase in case_text, f"reference coverage missing {phrase!r}")
    req(all(value is False for value in cases.get("policy", {}).values()), "Foundation fixture prohibitions changed")

    inventory = INVENTORY.read_text(encoding="utf-8").lower()
    candidate = CANDIDATE.read_text(encoding="utf-8").lower()
    for phrase in ("mv-ia-f025","18 stable teaching surfaces","local draft","accepted durable event","permission filtering occurs before","tutorial-campaign","ppia-14","f024","noncanonical","no application runtime"):
        req(phrase in inventory, f"inventory missing {phrase!r}")
    for phrase in ("12 teaching-content types","12 contextual trigger classes","18 stable teaching surfaces","player, game master and content creator","permission-safe teaching pipeline","ppia-14","f024","30 deterministic","not complete until"):
        req(phrase in candidate, f"candidate missing {phrase!r}")

    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    req(tranches.get("PPIA-06", {}).get("status") == "completed_verified", "PPIA-06 predecessor no longer completed_verified")
    req(tranches.get("PPIA-08", {}).get("status") == "completed_verified", "PPIA-08 dependency no longer completed_verified")
    req(tranches.get("PPIA-13", {}).get("status") in {"started","completed_verified"}, "PPIA-13 backlog state invalid")
    req(tranches.get("PPIA-14", {}).get("status") in {"planned","started","completed_verified"}, "PPIA-14 successor missing")
    req(checkpoint.get("attempt_id") == "PPIA-13-attempt-001" and checkpoint.get("branch") == "governance/ppia-13-onboarding-help-teaching-content", "PPIA-13 checkpoint identity changed")
    req(checkpoint.get("status") in {"started","ready_for_review","completed_verified"}, "PPIA-13 checkpoint state invalid")
    req(checkpoint.get("unresolved_failures") == [] and checkpoint.get("owner_decision_required") is False, "PPIA-13 unresolved state")

    # While PPIA-13 remains current, runtime continuity must select it. Once a later tranche is active,
    # this Foundation remains a historical content regression and must not force the old pointer.
    if backlog.get("current_work_item_id") == "PPIA-13":
        req(pointer.get("primary_attempt_id") == "PPIA-13-attempt-001", "current pointer does not select PPIA-13")
        req(status.get("primary", {}).get("work_item_id") == "PPIA-13", "compact status does not select PPIA-13")
        continuity = "ppia13_current"
    else:
        req(tranches.get("PPIA-13", {}).get("status") == "completed_verified", "historical PPIA-13 must be completed_verified")
        continuity = "ppia13_historical"

    boundaries = backlog.get("boundaries", {})
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(boundaries.get(key) is False, f"program boundary changed: {key}")

    print("PPIA-13 FOUNDATION: PASS")
    print("authority=MV-IA-F025 + F003/F004/F006/F020/F021 + completed PPIA-08")
    print("surface=6 evidence classes / 12 content types / 12 trigger classes / 18 teaching surfaces / 9 roles / 5 journeys")
    print("reference_cases=30 synthetic noncanonical; tutorial_campaign_noncanonical=true")
    print("permission_filter_before_derivatives=true offline_authoritative_mutation=false p14_boundary=true f024_gap_explicit=true")
    print("accessibility=mobile+keyboard+touch+screen-reader+high-zoom+reduced-motion+noncolor")
    print("runtime_activation=false continuity_mode=" + continuity)


if __name__ == "__main__":
    main()
