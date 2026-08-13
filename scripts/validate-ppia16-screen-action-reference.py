#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
SCREENS = BASE / "PPIA-16_SCREEN_STATE_CONTRACTS_v0.1.0.json"
ACTIONS = BASE / "PPIA-16_ACTION_CONTRACTS_v0.1.0.json"
COMPONENTS = BASE / "PPIA-16_COMPONENT_INTERACTION_CONTRACTS_v0.1.0.json"
CASES = BASE / "PPIA-16_SCREEN_ACTION_REFERENCE_CASES_v0.1.0.json"
NARRATIVE = BASE / "PPIA-16_SCREEN_ACTION_REFERENCE_CONTRACT.md"
PACKAGE = BASE / "PPIA-16_SCREEN_ACTION_REFERENCE_PACKAGE_INDEX_v0.1.0.json"
FOUNDATION_IA = BASE / "PPIA-16_FOUNDATION_INFORMATION_ARCHITECTURE_v0.1.0.json"
FOUNDATION_AUTH = BASE / "PPIA-16_FOUNDATION_AUTHORITY_AND_STATUS_MODEL_v0.1.0.json"
FOUNDATION_COVERAGE = BASE / "PPIA-16_FOUNDATION_SCREEN_WORKFLOW_COVERAGE_MAP_v0.1.0.json"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-16-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

FOUNDATION_HEAD = "8e0650fb9ab237ec3f1b1fe9152de42ee6f7c889"
FOUNDATION_RUN = "31685859485"
FOUNDATION_MERGE = "015f200595fd6e8ba5da85a2956ee1c9dc8fb15b"
BRANCH = "governance/ppia-16-developer-console-ai-team-control-surface"
SCREEN_IDS = {f"P16-SCR-{i:03d}" for i in range(1, 11)}
WORKFLOW_IDS = {f"P16-WF-{i:03d}" for i in range(1, 13)}
COMPONENT_IDS = {f"P16-CMP-{i:03d}" for i in range(1, 9)}
ACTION_IDS = {
    "ACT-OBSERVE", "ACT-NAVIGATE", "ACT-GENERATE", "ACT-RUN-EVIDENCE",
    "ACT-EXTERNAL-ADAPTER", "ACT-PROPOSE-GOVERNED-MUTATION",
    "ACT-EXECUTE-GOVERNED-MUTATION", "ACT-OWNER-GATED",
}
SHARED_STATES = {"loading", "ready", "empty", "stale", "conflict", "blocked", "error", "recovering"}
PACKAGE_PATHS = {
    "governance/application-planning/parallel-preimplementation/PPIA-16_SCREEN_STATE_CONTRACTS_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-16_ACTION_CONTRACTS_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-16_COMPONENT_INTERACTION_CONTRACTS_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-16_SCREEN_ACTION_REFERENCE_CASES_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-16_SCREEN_ACTION_REFERENCE_CONTRACT.md",
}


def fail(msg: str) -> None:
    text = "PPIA-16 SCREEN/ACTION/REFERENCE: FAIL — " + msg
    print("::error title=PPIA-16 Screen Action Reference Validator::" + text.replace("\n", "%0A"))
    raise SystemExit(text)


def req(cond: bool, msg: str) -> None:
    if not cond:
        fail(msg)


def load(path: Path) -> dict:
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def main() -> None:
    screens = load(SCREENS)
    actions = load(ACTIONS)
    components = load(COMPONENTS)
    cases = load(CASES)
    package = load(PACKAGE)
    foundation_ia = load(FOUNDATION_IA)
    foundation_auth = load(FOUNDATION_AUTH)
    foundation_cov = load(FOUNDATION_COVERAGE)
    backlog = load(BACKLOG)
    checkpoint = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)
    narrative = NARRATIVE.read_text(encoding="utf-8").lower()

    # Governed active state and immutable Foundation evidence.
    req(backlog.get("current_work_item_id") == "PPIA-16", "PPIA-16 is not current")
    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    req(tranches.get("PPIA-16", {}).get("status") in {"started", "in_progress", "ready_for_review"}, "PPIA-16 backlog not active")
    req(checkpoint.get("work_item_id") == "PPIA-16" and checkpoint.get("attempt_id") == "PPIA-16-attempt-001", "checkpoint identity changed")
    req(checkpoint.get("branch") == BRANCH, "checkpoint branch changed")
    req(checkpoint.get("status") in {"started", "in_progress", "ready_for_review"}, "checkpoint must remain unfinished")
    substep = (checkpoint.get("active_substep") or "").lower()
    for phrase in ("screen states", "action contracts", "reference cases"):
        req(phrase in substep, f"active substep missing {phrase}")
    req(checkpoint.get("owner_decision_required") is False and checkpoint.get("unresolved_failures") == [], "unexpected unresolved checkpoint state")
    req(pointer.get("primary_attempt_id") == "PPIA-16-attempt-001", "pointer does not select PPIA-16")
    primary = status.get("primary", {})
    req(primary.get("work_item_id") == "PPIA-16" and primary.get("attempt_id") == "PPIA-16-attempt-001", "compact status does not select PPIA-16")
    history = json.dumps({"completed": checkpoint.get("completed_substeps", []), "validation": checkpoint.get("validation", []), "evidence": checkpoint.get("evidence", [])}).lower()
    for token in (FOUNDATION_HEAD, FOUNDATION_RUN, FOUNDATION_MERGE, "67/67", "verified"):
        req(token.lower() in history, f"immutable Foundation evidence missing {token}")

    # Foundation identities remain the predecessor contract.
    req({x.get("screen_id") for x in foundation_ia.get("screens", [])} == SCREEN_IDS, "Foundation screen set changed")
    req({x.get("id") for x in foundation_ia.get("cross_screen_components", [])} == COMPONENT_IDS, "Foundation component set changed")
    req({x.get("id") for x in foundation_auth.get("action_classes", [])} == ACTION_IDS, "Foundation action set changed")
    req({x.get("workflow_id") for x in foundation_cov.get("workflows", [])} == WORKFLOW_IDS, "Foundation workflow set changed")

    # Screen states.
    req(screens.get("work_item_id") == "PPIA-16" and screens.get("status") == "screen-action-reference-candidate", "screen artifact identity/status")
    shared = {x.get("id") for x in screens.get("global_state_vocabulary", [])}
    req(shared == SHARED_STATES, f"shared state vocabulary changed: {sorted(shared)}")
    req(len(screens.get("transition_invariants", [])) >= 6, "transition invariants too thin")
    rows = screens.get("screens", [])
    req(len(rows) == 10 and {x.get("screen_id") for x in rows} == SCREEN_IDS, "screen contract set must be P16-SCR-001..010")
    for row in rows:
        req(row.get("initial_focus"), f"{row.get('screen_id')} missing initial focus")
        req(row.get("state_oracles"), f"{row.get('screen_id')} missing state oracles")
        req(row.get("mobile"), f"{row.get('screen_id')} missing mobile behavior")
        req(row.get("nonvisual"), f"{row.get('screen_id')} missing nonvisual behavior")
        req(set(row.get("required_states", [])) <= SHARED_STATES, f"{row.get('screen_id')} uses undeclared shared state")
    screen_blob = json.dumps(screens).lower()
    for token in ("scope-gap", "scenario-pass", "privacy-block", "tool-test-only", "undeclared", "declared", "proven", "partial-green", "budget-missing", "continuity-conflict"):
        req(token in screen_blob, f"screen-specific coverage missing {token}")
    modes = screens.get("interaction_modes", {})
    for key in ("keyboard", "screen_reader", "high_zoom", "mobile_touch", "reduced_motion", "noncolor"):
        req(key in modes and modes[key], f"interaction mode missing {key}")

    # Action contracts.
    req(actions.get("work_item_id") == "PPIA-16" and actions.get("status") == "screen-action-reference-candidate", "action artifact identity/status")
    arows = actions.get("actions", [])
    req(len(arows) == 8 and {x.get("id") for x in arows} == ACTION_IDS, "action contracts must cover all eight Foundation classes")
    for row in arows:
        for key in ("enable_when", "disable_when", "confirmation", "execution_contract", "result_contract", "retry", "keyboard", "mobile_touch"):
            req(row.get(key) not in (None, [], {}), f"{row.get('id')} missing {key}")
    ablob = json.dumps(actions).lower()
    for phrase in ("confirmation cannot create authority", "never blind-retry", "never auto-execute", "ppia-16", "owner", "candidate", "stop conditions"):
        req(phrase in ablob, f"action contract missing invariant {phrase}")
    recovery = actions.get("ambiguous_status_recovery", {})
    req("freeze blind retry" in json.dumps(recovery).lower() and "applied/not-applied/unknown" in json.dumps(recovery).lower(), "ambiguous mutation recovery weakened")

    # Component contracts.
    req(components.get("work_item_id") == "PPIA-16" and components.get("status") == "screen-action-reference-candidate", "component artifact identity/status")
    crows = components.get("components", [])
    req(len(crows) == 8 and {x.get("id") for x in crows} == COMPONENT_IDS, "component contracts must cover P16-CMP-001..008")
    cblob = json.dumps(components).lower()
    for phrase in ("candidate identity chip", "raw status pill", "source stack", "finding row", "evidence receipt card", "stop condition panel", "nonactivation strip", "producer-defined digest", "authoritative_mutation_performed"):
        req(phrase in cblob, f"component behavior missing {phrase}")
    receipt = next(x for x in crows if x.get("id") == "P16-CMP-006")
    required_receipt = {"source_tool_or_workflow","source_repository","candidate_or_source_ref","execution_scope","raw_result","generated_at_or_run_identity","inputs_or_source_roots","artifact_or_evidence_digest_when_available","authoritative_mutation_performed","authority_limitations"}
    req(set(receipt.get("required_fields", [])) == required_receipt, "receipt minimum changed")

    # Synthetic noncanonical reference cases and exact workflow distribution.
    req(cases.get("classification") == "synthetic_noncanonical_qa_reference_fixture" and cases.get("canonical") is False, "reference cases must be synthetic noncanonical")
    rcs = cases.get("cases", [])
    req(cases.get("case_count") == 48 and len(rcs) == 48, "expected exactly 48 reference cases")
    req([x.get("id") for x in rcs] == [f"P16-RC-{i:03d}" for i in range(1, 49)], "reference case IDs changed")
    wf_counts = Counter(x.get("workflow_id") for x in rcs)
    req(set(wf_counts) == WORKFLOW_IDS and all(wf_counts[w] == 4 for w in WORKFLOW_IDS), "each Foundation workflow must have exactly four reference cases")
    covered_screens = {s for row in rcs for s in row.get("screens", [])}
    covered_actions = {a for row in rcs for k in ("enabled", "disabled") for a in row.get(k, [])}
    covered_components = {c for row in rcs for c in row.get("components", [])}
    req(covered_screens == SCREEN_IDS, f"reference screen coverage incomplete: {sorted(SCREEN_IDS-covered_screens)}")
    req(covered_actions == ACTION_IDS, f"reference action coverage incomplete: {sorted(ACTION_IDS-covered_actions)}")
    req(covered_components == COMPONENT_IDS, f"reference component coverage incomplete: {sorted(COMPONENT_IDS-covered_components)}")
    modes_blob = " ".join(str(x.get("mode", "")).lower() for x in rcs)
    for term in ("screen-reader", "keyboard", "phone-touch", "200pct"):
        req(term in modes_blob, f"reference corpus missing {term} coverage")
    case_blob = json.dumps(rcs).lower()
    for term in ("stale", "conflict", "blocked", "recovering", "blind retry", "owner", "partial-green", "candidate", "historical", "non-authoritative", "no completion inference"):
        req(term in case_blob, f"reference corpus missing {term}")

    # Package/narrative and nonactivation.
    req(package.get("foundation_merge") == FOUNDATION_MERGE, "package Foundation merge changed")
    req({x.get("path") for x in package.get("artifacts", [])} == PACKAGE_PATHS, "package artifact set changed")
    req(package.get("validator") == "scripts/validate-ppia16-screen-action-reference.py", "package validator path changed")
    req(package.get("hosted_workflow") == ".github/workflows/validate-ppia-16-screen-action-reference.yml", "package workflow path changed")
    req(package.get("locked_counts") == {"screens":10,"shared_states":8,"action_classes":8,"components":8,"foundation_workflows":12,"reference_cases":48,"reference_cases_per_workflow":4}, "package locked counts changed")
    for phrase in ("48 synthetic noncanonical", "confirmation never creates authority", "ambiguous mutation status", "exact-candidate", "screen-reader", "200%", "mobile/touch", "does not mark ppia-16"):
        req(phrase in narrative, f"narrative missing {phrase}")
    for doc in (screens, actions, components, cases, package):
        nonact = doc.get("nonactivation", {})
        req(nonact and all(v is False for v in nonact.values()), f"{doc.get('title','artifact')} nonactivation changed")

    print("PPIA-16 SCREEN/ACTION/REFERENCE: PASS")
    print("screens=10 shared_states=8 actions=8 components=8 workflows=12 reference_cases=48")
    print("workflow_distribution=4_cases_each accessibility=keyboard+screen_reader+200pct+mobile_touch")
    print("candidate_binding=exact stale_visible ambiguous_mutation_retry=false owner_autoexecute=false")
    print("runtime_activation=false stage_a_a2=false release=false deployment=false tester_access=false")


if __name__ == "__main__":
    main()
