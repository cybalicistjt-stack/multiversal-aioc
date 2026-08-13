#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
P = lambda name: BASE / name

FILES = {
    "scope": P("PPIA-15_COMPLETION_SCOPE_LOCK_v0.1.0.json"),
    "acceptance": P("PPIA-15_COMPLETION_ACCEPTANCE_MATRIX_v0.1.0.json"),
    "package": P("PPIA-15_COMPLETION_PACKAGE_INDEX_v0.1.0.json"),
    "foundation_package": P("PPIA-15_FOUNDATION_PACKAGE_INDEX_v0.1.0.json"),
    "iar_package": P("PPIA-15_IAR_PACKAGE_INDEX_v0.1.0.json"),
    "integrated_package": P("PPIA-15_INTEGRATED_EXPANDED_REGRESSION_PACKAGE_INDEX_v0.1.0.json"),
    "foundation_cases": P("PPIA-15_FOUNDATION_REFERENCE_CASES_v0.1.0.json"),
    "scenarios": P("PPIA-15_EXPANDED_REGRESSION_SCENARIO_LIBRARY_v0.1.0.json"),
    "projections": P("PPIA-15_INSPECTOR_PROJECTION_CONTRACTS_v0.1.0.json"),
    "actions": P("PPIA-15_ACTION_AND_REFERENCE_CONTRACTS_v0.1.0.json"),
    "iar_cases": P("PPIA-15_IAR_REFERENCE_CASES_v0.1.0.json"),
    "workflows": P("PPIA-15_INTEGRATED_EXPANDED_REGRESSION_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json"),
    "integrated_cases": P("PPIA-15_INTEGRATED_EXPANDED_REGRESSION_REFERENCE_CASES_v0.1.0.json"),
    "trace": P("PPIA-15_INTEGRATED_EXPANDED_REGRESSION_TRACEABILITY_MATRIX_v0.1.0.json"),
}
REPORT = P("PPIA-15_COMPLETION_REPORT.md")
README = P("PPIA-15_COMPLETION_README.md")
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-15-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BACKLOG = P("PPIA_PROGRAM_BACKLOG.json")
WORKFLOW = ROOT / ".github/workflows/validate-ppia-15-completion-contracts.yml"


def fail(message: str) -> None:
    text = "PPIA-15 COMPLETION CONTRACT: FAIL — " + message
    print("::error title=PPIA-15 Completion Contract Validator::" + text.replace("\n", "%0A").replace("\r", "%0D"))
    raise SystemExit(text)


def req(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path):
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def exact_once(actual, expected, label):
    counts = Counter(actual)
    req(set(counts) == set(expected), f"{label} coverage set mismatch")
    req(all(v == 1 for v in counts.values()), f"{label} must be assigned exactly once")


def main() -> None:
    d = {k: load(v) for k, v in FILES.items()}
    checkpoint, pointer, status, backlog = map(load, (CHECKPOINT, POINTER, STATUS, BACKLOG))
    for p in (REPORT, README, WORKFLOW):
        req(p.exists(), f"missing {p.relative_to(ROOT)}")

    gate = "Expanded nonduplicative Internal Alpha regression scenario set covering awkward permission, conflict, recovery, scale, accessibility, mobile and object-edge cases."
    req(d["scope"].get("work_item") == "PPIA-15" and d["scope"].get("scope_locked") is True, "completion scope identity changed")
    req(d["scope"].get("completion_gate") == gate, "completion gate changed")
    req(d["scope"].get("completion_requires") == "exact_head_all_green_hosted_validation_and_merge", "completion evidence rule changed")
    req(d["scope"].get("transition_after_completion") == "PPIA-15 -> PPIA-16 separate governed operation", "transition boundary changed")
    req(len(d["scope"].get("required_categories", [])) == 18, "completion scope must retain 18 categories")
    req("invented_F024_pack_lifecycle_behavior" in d["scope"].get("prohibited_shortcuts", []), "F024 no-invention shortcut guard missing")
    req("adding_duplicate_scenarios_merely_to_increase_counts" in d["scope"].get("prohibited_shortcuts", []), "nonduplication shortcut guard missing")

    acc = d["acceptance"]
    req(acc.get("work_item") == "PPIA-15" and acc.get("classification") == "completion_acceptance_matrix", "acceptance identity changed")
    req(acc.get("completion_gate") == gate, "acceptance gate changed")
    expected_counts = {"acceptance_categories":18,"primary_inherited_case_records_after_exact_alias_collapse":300,"awkward_families":18,"stable_scenarios":24,"foundation_cases":32,"projection_groups":12,"actions":20,"iar_cases":40,"workflows":18,"handoffs":12,"integrated_cases":18,"effective_authored_cases":90,"ordinary_gm_modification_clones":0,"open_f024_source_gaps":1}
    req(acc.get("counts") == expected_counts, "completion acceptance counts changed")
    cats = acc.get("categories", [])
    req([x.get("id") for x in cats] == [f"P15-CG-{i:02d}" for i in range(1, 19)], "completion category IDs changed")
    req(len({x.get("name") for x in cats}) == 18 and all(x.get("proof") for x in cats), "completion category proof/name integrity changed")

    pkg = d["package"]
    req(pkg.get("work_item") == "PPIA-15" and pkg.get("milestone") == "final_completion_gate", "completion package identity changed")
    req(pkg.get("completion_surface", {}) == {"acceptance_categories":18,"primary_inherited_case_records_after_exact_alias_collapse":300,"awkward_families":18,"direct_gaps":7,"partial_awkward_variants":10,"baseline_covered_no_clone":1,"stable_scenarios":24,"foundation_cases":32,"projection_groups":12,"actions":20,"iar_cases":40,"workflows":18,"handoffs":12,"integrated_cases":18,"effective_authored_cases":90,"ordinary_gm_modification_clones":0,"open_f024_source_gaps":1}, "completion package surface changed")
    milestones = pkg.get("verified_milestones", [])
    expected_milestones = [
        ("foundation_existing_test_corpus_and_coverage_gap_inventory", "d876093989e656d3cf8366c19755295ef0f785e8", "a1f6b7380a07e65469ba8072e8aa4135d7b1e42f", 62, 286, "31652241636"),
        ("expanded_regression_scenario_library_inspector_action_reference", "94029c704fa097f99440a58a64c4293d52b4ad36", "740683e33ff6e3a0b1a8672c06fbbf9d87fa3bf5", 63, 287, "31653764114"),
        ("integrated_expanded_regression_workflows_traceability", "8e02c87504555ce8fc27b902a68cae8384f4ab25", "d98a2fc6fc31c62b91d7c11a92b8242469965b7d", 64, 288, "31656064001"),
    ]
    req(len(milestones) == 3, "completion package predecessor milestone count changed")
    for row, exp in zip(milestones, expected_milestones):
        req((row.get("milestone"), row.get("validated_head"), row.get("merge"), row.get("hosted_workflows"), row.get("pull_request"), row.get("dedicated_run")) == exp, f"immutable milestone evidence changed: {exp[0]}")
    req(pkg.get("state") == "completion_candidate_only_until_exact_head_all_green_and_merge", "completion candidate state changed")
    req(pkg.get("transition_after_completion") == "PPIA-15 -> PPIA-16 separate governed operation", "completion transition boundary changed")

    fnd = d["foundation_package"].get("locked_counts", {})
    req((fnd.get("primary_inherited_case_records_after_exact_alias_collapse"), fnd.get("required_awkward_families"), fnd.get("direct_gaps"), fnd.get("partial_awkward_variants"), fnd.get("baseline_covered_no_clone"), fnd.get("foundation_reference_cases")) == (300,18,7,10,1,32), "verified Foundation accounting changed")
    iar = d["iar_package"].get("locked_counts", {})
    req((iar.get("foundation_cases"), iar.get("stable_scenario_contracts"), iar.get("required_awkward_families"), iar.get("projection_groups"), iar.get("action_contracts"), iar.get("new_iar_cases"), iar.get("effective_cases"), iar.get("ordinary_gm_modification_clones"), iar.get("open_f024_source_gaps")) == (32,24,18,12,20,40,72,0,1), "verified IAR accounting changed")
    integ = d["integrated_package"].get("locked_counts", {})
    req((integ.get("workflows"), integ.get("required_awkward_families"), integ.get("stable_scenario_contracts"), integ.get("projection_groups"), integ.get("action_contracts"), integ.get("handoffs"), integ.get("foundation_cases"), integ.get("iar_cases"), integ.get("new_integrated_cases"), integ.get("effective_cases"), integ.get("ordinary_gm_modification_clones"), integ.get("open_f024_source_gaps")) == (18,18,24,12,20,12,32,40,18,90,0,1), "verified integrated accounting changed")

    fc = d["foundation_cases"].get("cases", [])
    sr = d["scenarios"].get("scenario_contracts", [])
    pg = d["projections"].get("projection_groups", [])
    ac = d["actions"].get("actions", [])
    ic = d["iar_cases"].get("cases", [])
    wf = d["workflows"].get("workflows", [])
    iw = d["integrated_cases"].get("cases", [])
    req([x.get("id") for x in fc] == [f"PPIA15-FC-{i:03d}" for i in range(1,33)], "Foundation case IDs changed")
    req([x.get("id") for x in sr] == [f"P15-SCN-{i:03d}" for i in range(1,25)], "scenario IDs changed")
    req([x.get("id") for x in pg] == [f"P15-PG-{i:03d}" for i in range(1,13)], "projection IDs changed")
    req([x.get("id") for x in ac] == [f"P15-ACT-{i:03d}" for i in range(1,21)], "action IDs changed")
    req([x.get("id") for x in ic] == [f"P15-IAR-{i:03d}" for i in range(1,41)], "IAR case IDs changed")
    req([x.get("id") for x in wf] == [f"P15-WF-{i:03d}" for i in range(1,19)], "workflow IDs changed")
    req([x.get("id") for x in iw] == [f"P15-IW-{i:03d}" for i in range(1,19)], "integrated case IDs changed")

    exact_once([cid for w in wf for cid in w.get("foundation_case_ids", [])], [x["id"] for x in fc], "Foundation cases")
    exact_once([cid for w in wf for cid in w.get("iar_case_ids", [])], [x["id"] for x in ic], "IAR cases")
    exact_once([cid for w in wf for cid in w.get("integrated_case_ids", [])], [x["id"] for x in iw], "Integrated cases")
    req({f"P15-AWK-{i:03d}" for i in range(1,19)} == {w.get("awkward_family_id") for w in wf}, "workflow awkward-family coverage changed")
    req({x.get("id") for x in sr} == {sid for w in wf for sid in w.get("scenario_ids", [])}, "workflow scenario coverage changed")
    req({x.get("id") for x in pg} == {pid for w in wf for pid in w.get("projection_group_ids", [])}, "workflow projection coverage changed")
    req({x.get("id") for x in ac} == {aid for w in wf for aid in w.get("action_ids", [])}, "workflow action coverage changed")
    req(all(x.get("ppia15_mutates_authoritative_state") is False for x in ac), "PPIA-15 action gained mutation authority")

    txt = (REPORT.read_text(encoding="utf-8") + "\n" + README.read_text(encoding="utf-8")).lower()
    for phrase in ("90 effective authored ppia-15 cases","zero ordinary-gm-modification standalone clones","p15-gap-001","f024","status unknown is not failure","offline/local/read-only state","512 inventory","128 creature/npc","separate governed operation"):
        req(phrase in txt, f"completion narrative missing {phrase!r}")

    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    for dep in ("PPIA-09","PPIA-10","PPIA-11","PPIA-14"):
        req(tranches.get(dep, {}).get("status") == "completed_verified", f"{dep} dependency changed")
    req(tranches.get("PPIA-15", {}).get("completion_gate") == gate, "backlog PPIA-15 gate changed")
    current = backlog.get("current_work_item_id")
    if current == "PPIA-15":
        req(tranches.get("PPIA-15", {}).get("status") in {"started","ready_for_review"}, "completion candidate must not transition PPIA-15 before merge")
        req(checkpoint.get("status") in {"started","ready_for_review"} and checkpoint.get("completed_at") is None, "completion candidate checkpoint cannot be completed before merge")
        req("Completion Contract / Evidence Closure" in (checkpoint.get("active_substep") or ""), "checkpoint not on completion milestone")
        req(pointer.get("primary_attempt_id") == "PPIA-15-attempt-001", "pointer does not select PPIA-15")
        req(status.get("primary", {}).get("work_item_id") == "PPIA-15", "compact status does not select PPIA-15")
        continuity_mode = "active_completion_candidate"
    else:
        order = backlog.get("execution_order", [])
        req(current in order and order.index(current) > order.index("PPIA-15"), "historical completion validation only allowed after PPIA-15")
        req(tranches.get("PPIA-15", {}).get("status") == "completed_verified", "historical PPIA-15 backlog must be completed_verified")
        req(checkpoint.get("status") == "completed_verified" and checkpoint.get("completed_at"), "historical checkpoint must be completed_verified")
        continuity_mode = "historical_after_ppia15"
    req(checkpoint.get("owner_decision_required") is False and checkpoint.get("unresolved_failures") == [], "PPIA-15 unresolved blocker exists")
    bounds = backlog.get("boundaries", {})
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(bounds.get(key) is False, f"program boundary changed: {key}")

    print("PPIA-15 COMPLETION CONTRACT: PASS")
    print("inherited_primary=300 awkward_families=18 scenarios=24 foundation=32 iar=40 integrated=18 effective_authored=90")
    print("projection_groups=12 actions=20 workflows=18 handoffs=12 gm_baseline_clones=0 f024_gap=open-not-invented")
    print(f"continuity_mode={continuity_mode} runtime_activation=false a2_activation=false tester_access=false release=false deployment=false ppia16_transition=false")


if __name__ == "__main__":
    main()
