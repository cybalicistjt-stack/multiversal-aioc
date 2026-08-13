#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
P = lambda name: BASE / name

FILES = {
    "scope": P("PPIA-16_COMPLETION_SCOPE_LOCK_v0.1.0.json"),
    "acceptance": P("PPIA-16_COMPLETION_ACCEPTANCE_MATRIX_v0.1.0.json"),
    "package": P("PPIA-16_COMPLETION_PACKAGE_INDEX_v0.1.0.json"),
    "foundation_package": P("PPIA-16_FOUNDATION_PACKAGE_INDEX_v0.1.0.json"),
    "screen_package": P("PPIA-16_SCREEN_ACTION_REFERENCE_PACKAGE_INDEX_v0.1.0.json"),
    "integrated_package": P("PPIA-16_INTEGRATED_SCREEN_WORKFLOW_PACKAGE_INDEX_v0.1.0.json"),
}
REPORT = P("PPIA-16_COMPLETION_REPORT.md")
README = P("PPIA-16_COMPLETION_README.md")
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-16-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BACKLOG = P("PPIA_PROGRAM_BACKLOG.json")
WORKFLOW = ROOT / ".github/workflows/validate-ppia-16-completion-contracts.yml"

GATE = "Implementation-ready Development Console information architecture and screen/workflow package over DT-001 through DT-010, preserving non-authoritative tooling boundaries."
EXPECTED_COUNTS = {
    "acceptance_categories":18,
    "dt_tools":10,
    "aioc_control_surfaces":10,
    "program_requirements":16,
    "authority_layers":5,
    "screens":10,
    "shared_states":8,
    "action_classes":8,
    "components":8,
    "workflows":12,
    "handoffs":12,
    "predecessor_reference_cases":48,
    "integrated_cases":12,
    "effective_qa_cases":60,
    "orphaned_coverage":0,
}


def fail(message: str) -> None:
    text = "PPIA-16 COMPLETION CONTRACT: FAIL — " + message
    print("::error title=PPIA-16 Completion Contract Validator::" + text.replace("\n", "%0A").replace("\r", "%0D"))
    raise SystemExit(text)


def req(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path):
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    d = {k: load(v) for k, v in FILES.items()}
    checkpoint, pointer, status, backlog = map(load, (CHECKPOINT, POINTER, STATUS, BACKLOG))
    for path in (REPORT, README, WORKFLOW):
        req(path.exists(), f"missing {path.relative_to(ROOT)}")

    scope = d["scope"]
    req(scope.get("work_item") == "PPIA-16" and scope.get("scope_locked") is True, "completion scope identity changed")
    req(scope.get("completion_gate") == GATE, "completion gate changed")
    req(len(scope.get("required_categories", [])) == 18, "completion scope must retain 18 categories")
    for guard in (
        "tool_pass_implies_authority",
        "candidate_bound_evidence_silently_carries_to_new_candidate",
        "blind_retry_after_ambiguous_mutation",
        "runtime_or_stage_a_a2_activation",
        "ppia_program_completion_before_exact_head_validation_merge_and_recovery",
    ):
        req(guard in scope.get("prohibited_shortcuts", []), f"missing completion shortcut guard: {guard}")
    req(scope.get("completion_requires") == "exact_head_all_green_hosted_validation_signed_merge_and_recovery", "completion evidence rule changed")

    acceptance = d["acceptance"]
    req(acceptance.get("work_item") == "PPIA-16" and acceptance.get("classification") == "completion_acceptance_matrix", "acceptance identity changed")
    req(acceptance.get("completion_gate") == GATE, "acceptance gate changed")
    req(acceptance.get("counts") == EXPECTED_COUNTS, "completion acceptance counts changed")
    categories = acceptance.get("categories", [])
    req([row.get("id") for row in categories] == [f"P16-CG-{i:02d}" for i in range(1, 19)], "completion category IDs changed")
    req(len({row.get("name") for row in categories}) == 18 and all(row.get("proof") for row in categories), "completion category proof/name integrity changed")

    package = d["package"]
    req(package.get("work_item") == "PPIA-16" and package.get("milestone") == "final_completion_gate", "completion package identity changed")
    req(package.get("completion_surface") == EXPECTED_COUNTS, "completion package surface changed")
    expected_milestones = [
        ("ppia15_to_ppia16_transition", "21054af7b372d2216097e91bd32efe9298ec8a9d", "87ee7795de362059d92a76e3923e2a7f8d182124", 66, 290, "31682807809"),
        ("foundation_existing_toolbelt_and_control_surface_authority_inventory", "8e0650fb9ab237ec3f1b1fe9152de42ee6f7c889", "015f200595fd6e8ba5da85a2956ee1c9dc8fb15b", 67, 291, "31685859485"),
        ("screen_states_action_contracts_reference_cases", "45e7e34b6bf7de0ca2ebff4b2818bdb1007f04c5", "be811bd4508954700a83032b285107a8bd0d019a", 68, 292, "31689903909"),
        ("integrated_screen_workflow_traceability", "d9b46fb71bcb71504308429ebf96c6ac5afd1811", "e5253e6cd08c3a053a6b9e8d99592faa652d7798", 69, 293, "31692631899"),
    ]
    milestones = package.get("verified_milestones", [])
    req(len(milestones) == 4, "completion predecessor milestone count changed")
    for row, expected in zip(milestones, expected_milestones):
        actual = (row.get("milestone"), row.get("validated_head"), row.get("merge"), row.get("hosted_workflows"), row.get("pull_request"), row.get("dedicated_run"))
        req(actual == expected, f"immutable predecessor evidence changed: {expected[0]}")
    req(package.get("state") == "completion_candidate_only_until_exact_head_all_green_signed_merge_and_recovery", "completion candidate state changed")

    foundation = d["foundation_package"].get("expected_counts", {})
    req(foundation == {"toolbelt_entries":10,"aioc_control_surfaces":10,"program_requirements":16,"screens":10,"workflows":12,"cross_screen_components":8,"authority_precedence_layers":5,"action_classes":8}, "verified Foundation accounting changed")
    screen = d["screen_package"].get("locked_counts", {})
    req(screen == {"screens":10,"shared_states":8,"action_classes":8,"components":8,"foundation_workflows":12,"reference_cases":48,"reference_cases_per_workflow":4}, "verified Screen/Action accounting changed")
    integrated = d["integrated_package"].get("locked_counts", {})
    req(integrated == {"foundation_workflows":12,"screens":10,"action_classes":8,"components":8,"dt_tools":10,"aioc_control_surfaces":10,"program_requirements":16,"authority_layers":5,"handoffs":12,"predecessor_reference_cases":48,"new_integrated_cases":12,"effective_qa_cases":60}, "verified integrated accounting changed")

    narrative = (REPORT.read_text(encoding="utf-8") + "\n" + README.read_text(encoding="utf-8")).lower()
    for phrase in (
        "60 effective ppia-16 qa cases",
        "zero intended orphaned coverage",
        "only `completed_verified` is complete",
        "ambiguous mutation status forbids blind retry",
        "candidate-bound evidence",
        "stage-a-a2 remains authorized but not activated",
        "design standards attempt-002 remains unfinished",
    ):
        req(phrase in narrative, f"completion narrative missing {phrase!r}")

    tranches = {row.get("work_item_id"): row for row in backlog.get("tranches", [])}
    req(set(tranches) == {f"PPIA-{i:02d}" for i in range(1,17)}, "PPIA tranche set changed")
    for work_item in ["PPIA-01","PPIA-02","PPIA-03","PPIA-04","PPIA-05","PPIA-12","PPIA-07","PPIA-08","PPIA-09","PPIA-10","PPIA-11","PPIA-06","PPIA-13","PPIA-14","PPIA-15"]:
        req(tranches.get(work_item, {}).get("status") in {"complete","completed","completed_verified"}, f"verified predecessor {work_item} no longer complete")
    req(tranches.get("PPIA-16", {}).get("completion_gate") == GATE, "backlog PPIA-16 gate changed")

    p16_status = tranches.get("PPIA-16", {}).get("status")
    if p16_status in {"started", "in_progress"}:
        req(backlog.get("current_work_item_id") == "PPIA-16", "completion candidate must remain current PPIA-16")
        req(checkpoint.get("status") in {"in_progress", "ready_for_review"} and checkpoint.get("completed_at") is None, "completion candidate checkpoint cannot be complete before merge")
        req("Completion Contract / Evidence Closure" in (checkpoint.get("active_substep") or ""), "checkpoint not on PPIA-16 completion milestone")
        req(pointer.get("primary_attempt_id") == "PPIA-16-attempt-001", "pointer does not select PPIA-16 candidate")
        req(status.get("primary", {}).get("work_item_id") == "PPIA-16", "compact status does not select PPIA-16 candidate")
        continuity_mode = "active_completion_candidate"
    elif p16_status == "completed_verified":
        req(checkpoint.get("status") == "completed_verified" and checkpoint.get("completed_at"), "completed PPIA-16 checkpoint missing completion evidence")
        req(checkpoint.get("merge_commit"), "completed PPIA-16 checkpoint missing merge")
        continuity_mode = "completed_verified_final_tranche"
    else:
        fail(f"unsupported PPIA-16 backlog status: {p16_status}")

    req(checkpoint.get("owner_decision_required") is False and checkpoint.get("unresolved_failures") == [], "PPIA-16 unresolved blocker exists")
    bounds = backlog.get("boundaries", {})
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(bounds.get(key) is False, f"program boundary changed: {key}")

    print("PPIA-16 COMPLETION CONTRACT: PASS")
    print("continuity_mode:", continuity_mode)
    print("completion_surface:", EXPECTED_COUNTS)
    print("predecessor_merges: 87ee7795 015f2005 be811bd4 e5253e6c")
    print("nonactivation: runtime=false a2=false release=false deployment=false tester=false paid=false production_credentials=false canonical_promotion=false")


if __name__ == "__main__":
    main()
