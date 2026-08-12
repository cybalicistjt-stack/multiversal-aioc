#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
FILES = {
    "manifest": BASE / "PPIA-11_SOURCE_MANIFEST_v0.1.0.json",
    "taxonomy": BASE / "PPIA-11_ENCOUNTER_BALANCE_TAXONOMY_v0.1.0.json",
    "authority": BASE / "PPIA-11_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json",
    "methodology": BASE / "PPIA-11_ENCOUNTER_METHODOLOGY_CONTRACT_v0.1.0.json",
    "schema": BASE / "PPIA-11_BENCHMARK_ENCOUNTER_SCHEMA_v0.1.0.json",
    "benchmarks": BASE / "PPIA-11_BENCHMARK_REFERENCE_CASES_v0.1.0.json",
    "inspector": BASE / "PPIA-11_ENCOUNTER_LAB_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json",
    "cases": BASE / "PPIA-11_ENCOUNTER_LAB_REFERENCE_CASES_v0.1.0.json",
    "workflows": BASE / "PPIA-11_ENCOUNTER_LAB_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json",
    "trace": BASE / "PPIA-11_ENCOUNTER_LAB_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json",
}
REPORT = BASE / "PPIA-11_COMPLETION_REPORT.md"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
CP = ROOT / "governance/ai/work-state/PPIA-11-attempt-001.json"
PTR = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

MILESTONES = [
    ("23d1820fa1d047f3677310d8d426f6e9f541e09d", "bcd9464ebbf4be7ce15d1764d74890ef12e831fc"),
    ("963dd13560f22a4835b740c7b454a7c81532e981", "a5556fb3253baae0f302d9ea9b4b5f582fa9e05e"),
    ("fbc11069d2673bc1cb20fad2e1fa0055c318d602", "baa256596260b680ca7749ab14019635bf015fc8"),
    ("91a7880a89c2cb361c827979aad711ad234f62f5", "6ef3347ba061e80f42bb77b88a62af33228af46f"),
]


def fail(msg):
    raise SystemExit("PPIA-11 COMPLETION CONTRACT: FAIL — " + msg)


def req(cond, msg):
    if not cond:
        fail(msg)


def load(path):
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    docs = {k: load(v) for k, v in FILES.items()}
    backlog, cp, ptr, status = map(load, (BACKLOG, CP, PTR, STATUS))
    req(REPORT.exists(), "missing completion report")
    report = REPORT.read_text(encoding="utf-8").lower()

    man = docs["manifest"]
    req([x.get("id") for x in man.get("evidence_classes", [])] == ["source_truth","inherited_contract","observed_benchmark","authored_methodology","unresolved_gap"], "five evidence classes changed")
    anchor = man.get("governed_balance_anchor", {})
    req(anchor.get("source_corpus", {}).get("datasets") == 20 and anchor.get("source_corpus", {}).get("promoted_records") == 19199, "8D source corpus changed")
    req((anchor.get("coverage_domains"), anchor.get("golden_fixtures"), anchor.get("deterministic_scenarios"), anchor.get("scenario_executions"), anchor.get("non_destructive_recommendations"), anchor.get("mutation_sensitivity_cases")) == (18,36,24,72,36,7), "8D anchor counts changed")
    req(anchor.get("source_truth_changed") is False and anchor.get("comparison_scope") == "within-domain deterministic comparison only", "8D source/comparison boundary changed")
    req(len(man.get("inherited_contracts", [])) == 6 and len(man.get("explicit_non_assumptions", [])) >= 10, "source boundary inventory changed")

    tax = docs["taxonomy"]
    req([x.get("id") for x in tax.get("factor_families", [])] == [f"P11-F-{i:03d}" for i in range(1,21)], "20 factor families changed")
    req(len(tax.get("encounter_forms", [])) == 13 and len(set(tax.get("encounter_forms", []))) == 13, "13 encounter forms changed")
    req([x.get("id") for x in tax.get("uncertainty_bands", [])] == ["low","moderate","high","indeterminate"], "uncertainty bands changed")

    meth = docs["methodology"]
    req([x.get("id") for x in meth.get("assessment_steps", [])] == [f"P11-M-{i:03d}" for i in range(1,14)], "13 methodology steps changed")
    req(len(meth.get("pressure_dimension_support", {})) == 12, "12 pressure dimensions changed")
    req(len(meth.get("recommendation_types", [])) == 9, "nine recommendation classes changed")
    blocking = " ".join(meth.get("blocking_invariants", [])).lower()
    for phrase in ("no universal cr", "no weighted sum", "unknown/source-unspecified", "mixed-scale", "simulation", "ai", "no application runtime"):
        req(phrase in blocking, f"methodology invariant missing {phrase!r}")

    schema = docs["schema"]
    req(schema.get("schema_name") == "PPIA-11 Benchmark Encounter", "benchmark schema identity")
    req(len(schema.get("benchmark_classes", [])) == 5, "benchmark class count changed")
    req(len(schema.get("required_fields", [])) >= 20, "benchmark required fields reduced")
    for field in ("evidence_ledger","factor_review","pressure_dimension_review","comparison_scope","deterministic_protocol","uncertainty","calibration_hooks","provenance"):
        req(field in schema.get("required_fields", []), f"benchmark required field missing {field}")
    prohibited = set(schema.get("prohibited_claims", []))
    req({"balanced","fair","safe","winnable","optimal","guaranteed","universal difficulty","actual player prediction"} <= prohibited, "benchmark prohibited claims changed")

    bm = docs["benchmarks"]
    req(bm.get("case_count") == 18 and len(bm.get("cases", [])) == 18, "18 benchmark cases changed")
    req([x.get("id") for x in bm.get("cases", [])] == [f"PPIA11-BM-{i:03d}" for i in range(1,19)], "benchmark IDs changed")
    req(all(x.get("noncanonical") is True for x in bm.get("cases", [])), "benchmark noncanonical boundary changed")
    forms = {f for x in bm.get("cases", []) for f in x.get("encounter_forms", [])}
    req(forms == set(tax.get("encounter_forms", [])), "benchmark encounter-form coverage changed")
    req({x.get("expected_uncertainty") for x in bm.get("cases", [])} == {"low","moderate","high","indeterminate"}, "benchmark uncertainty coverage changed")

    auth = docs["authority"]
    req([x.get("id") for x in auth.get("domain_handoffs", [])] == [f"P11-HO-{i:03d}" for i in range(1,11)], "10 domain handoffs changed")
    guard = " ".join(auth.get("blocking_invariants", [])).lower()
    for phrase in ("no universal cr", "within-domain", "source mechanics", "automatic balance rewrite", "permission filtering", "unknown/source-unspecified", "mixed-scale", "no guaranteed-balance", "no application runtime"):
        req(phrase in guard, f"authority invariant missing {phrase!r}")

    ins = docs["inspector"]
    req([x.get("id") for x in ins.get("projection_groups", [])] == [f"P11-PG-{i:03d}" for i in range(1,17)], "16 projection groups changed")
    req([x.get("id") for x in ins.get("actions", [])] == [f"P11-ACT-{i:03d}" for i in range(1,25)], "24 actions changed")
    kinds = [x.get("kind") for x in ins.get("actions", [])]
    req(kinds.count("read") == 12 and kinds.count("analysis_proposal") == 8 and kinds.count("write") == 4, "12/8/4 action split changed")
    req(all(x.get("protocol") == "P11-MUT-001" for x in ins.get("actions", []) if x.get("kind") == "write"), "write protocol changed")
    mut = ins.get("mutation_protocols", {}).get("P11-MUT-001", {})
    req(mut.get("required") == ["authorization","expected_version","operation_id"], "mutation requirements changed")
    req(mut.get("source_truth_mutation") is False and mut.get("automatic_balance_rewrite") is False and mut.get("ai_authoritative_mutation") is False, "mutation authority boundary changed")

    cases = docs["cases"]
    req((cases.get("imported_case_count"), cases.get("local_case_count"), cases.get("resolved_case_count")) == (18,24,42), "42-case corpus counts changed")
    req([x.get("id") for x in cases.get("local_cases", [])] == [f"PPIA11-IR-{i:03d}" for i in range(19,43)], "local case IDs changed")
    req(all(v is False for v in cases.get("policy", {}).values()), "reference-case prohibitions changed")

    wf, trace = docs["workflows"], docs["trace"]
    expected_counts = {"workflows":14,"mutation_workflows":5,"read_analysis_workflows":9,"projection_groups":16,"actions":24,"reference_cases":42,"factor_families":20,"pressure_dimensions":12,"uncertainty_bands":4,"methodology_steps":13,"domain_handoffs":10}
    req(wf.get("counts") == expected_counts and trace.get("counts") == expected_counts, "workflow/trace counts changed")
    req([x.get("id") for x in wf.get("workflows", [])] == [f"P11-WF-{i:03d}" for i in range(1,15)], "14 workflow IDs changed")
    req(trace.get("coverage") == {"projection_groups":"16/16","actions":"24/24","reference_cases":"42/42 exactly once","factor_families":"20/20","pressure_dimensions":"12/12 independently inspectable","uncertainty_bands":"4/4","methodology_steps":"13/13","domain_handoffs":"10/10"}, "traceability coverage changed")
    assigned = [c for row in trace.get("rows", []) for c in row.get("cases", [])]
    req(assigned == [f"PPIA11-IR-{i:03d}" for i in range(1,43)], "reference cases not assigned exactly once/in order")
    policy = wf.get("workflow_policy", {})
    for key in ("universal_scalar","weighted_pressure_collapse","source_defaulting","automatic_balance_rewrite","automatic_benchmark_canonical_promotion","ai_irreversible_authority","guaranteed_balance_claim","runtime_activation"):
        req(policy.get(key) is False, f"workflow policy {key} changed")

    for head, merge in MILESTONES:
        req(head in report and merge in report, f"completion report missing milestone {head}/{merge}")
    for phrase in ("completion candidate — not complete until this exact head passes required validation and merges", "encounter design handbook", "benchmark corpus", "20 encounter-factor families", "12 independently inspectable pressure dimensions", "4 uncertainty bands", "13 assessment/calibration methodology steps", "18 explicitly noncanonical deterministic benchmark", "16 permission-safe projection groups", "24 governed actions", "42 deterministic reference cases", "14 integrated workflows", "10 explicit authority/domain handoffs", "no universal cr", "no weighted", "indeterminate_blocked", "expected_version", "operation_id", "semantic nonvisual", "ppia-11 → ppia-06 transition"):
        req(phrase in report, f"completion report missing {phrase!r}")

    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    req("PPIA-11" in tranches and "PPIA-06" in tranches, "PPIA-11/PPIA-06 backlog entries missing")
    cp_status = cp.get("status")
    req(cp_status in {"started","completed_verified"}, f"unexpected checkpoint status {cp_status!r}")
    req(cp.get("attempt_id") == "PPIA-11-attempt-001" and cp.get("branch") == "governance/ppia-11-encounter-balance-laboratory", "checkpoint identity changed")
    req(cp.get("unresolved_failures") == [] and cp.get("owner_decision_required") is False, "PPIA-11 unresolved state")
    history = json.dumps({"last_verified_action":cp.get("last_verified_action"),"completed_substeps":cp.get("completed_substeps",[]),"validation":cp.get("validation",[]),"evidence":cp.get("evidence",[])}, ensure_ascii=False).lower()
    for head, merge in MILESTONES:
        req(head in history and merge in history, f"checkpoint missing immutable milestone evidence {head}/{merge}")

    if tranches["PPIA-11"].get("status") == "started":
        req(backlog.get("current_work_item_id") == "PPIA-11" and tranches["PPIA-06"].get("status") == "planned", "pre-transition backlog continuity changed")
        req(ptr.get("primary_attempt_id") == "PPIA-11-attempt-001" and status.get("primary", {}).get("work_item_id") == "PPIA-11", "pre-transition runtime continuity changed")
        if cp_status == "started":
            active = ((cp.get("active_substep") or "") + " " + (cp.get("next_action") or "")).lower()
            req("completion" in active and "ppia-11" in active, "started checkpoint not on completion gate")
        else:
            req("validate ppia-11 completion contract" in history, "completed checkpoint missing completion validation evidence")
        continuity = "ppia11_completion_pretransition"
    else:
        req(tranches["PPIA-11"].get("status") == "completed_verified", "post-transition PPIA-11 must be completed_verified")
        req(cp_status == "completed_verified", "post-transition PPIA-11 checkpoint must remain completed_verified")
        order = backlog.get("execution_order", [])
        current_id = backlog.get("current_work_item_id")
        req("PPIA-11" in order and "PPIA-06" in order and current_id in order, "post-transition execution order/current item invalid")
        req(order.index(current_id) >= order.index("PPIA-06"), "post-transition current item cannot precede PPIA-06")
        if current_id == "PPIA-06":
            req(tranches["PPIA-06"].get("status") == "started", "PPIA-06 must be started immediately after PPIA-11 transition")
            req(status.get("primary", {}).get("work_item_id") == "PPIA-06" and status.get("primary", {}).get("status") == "started", "post-transition compact status must select PPIA-06")
            continuity = "ppia11_historical_after_ppia06_transition"
        else:
            req(order.index(current_id) > order.index("PPIA-06"), "later historical validation must be downstream of PPIA-06")
            req(tranches["PPIA-06"].get("status") == "completed_verified", "later historical validation requires PPIA-06 completed_verified")
            req(status.get("primary", {}).get("work_item_id") == current_id and status.get("primary", {}).get("status") in {"started","in_progress"}, "compact status must select the current downstream PPIA item")
            continuity = "ppia11_historical_after_ppia06_completion"

    bounds = backlog.get("boundaries", {})
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(bounds.get(key) is False, f"program boundary changed: {key}")

    print("PPIA-11 COMPLETION CONTRACT: PASS")
    print("surface=5 evidence classes / 20 factors / 13 forms / 12 pressure dimensions / 4 uncertainty bands / 13 methodology steps")
    print("benchmark=5 classes / 18 noncanonical deterministic QA fixtures")
    print("inspector=16 projections / 24 actions (12 read / 8 analysis-proposal / 4 write) / 42 cases")
    print("workflows=14 (5 mutation / 9 read-analysis) / 10 handoffs / 42 cases exactly once")
    print("completion_gate=encounter handbook + benchmark corpus + methodology + uncertainty + calibration + no guaranteed-balance overclaim")
    print("traceability_gaps=0 runtime_activation=false continuity_mode=" + continuity)

if __name__ == "__main__":
    main()
