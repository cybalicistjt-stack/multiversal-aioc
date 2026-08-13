#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
MAN = BASE / "PPIA-10_SOURCE_MANIFEST_v0.1.0.json"
TAX = BASE / "PPIA-10_RELATIONSHIP_SOCIAL_FACTION_TAXONOMY_v0.1.0.json"
AUTH = BASE / "PPIA-10_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
INS = BASE / "PPIA-10_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-10_REFERENCE_CASES_v0.1.0.json"
WF = BASE / "PPIA-10_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
TRACE = BASE / "PPIA-10_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json"
REPORT = BASE / "PPIA-10_COMPLETION_REPORT.md"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
CP = ROOT / "governance/ai/work-state/PPIA-10-attempt-001.json"
PTR = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

FOUNDATION_HEAD = "1c9216cf821a33f0386a0d43ec9290db4b5723fa"
FOUNDATION_MERGE = "0c0b8ce17cd80e47b7b12285a2bd8278e58a732e"
INSPECTOR_HEAD = "9cc894e3544203f42ec23c12efd256041cb630a2"
INSPECTOR_MERGE = "6985dd1e1f6d2e2b696f409cc74ae9e0ad18d728"
WORKFLOW_HEAD = "7e23b04fa920b706278ae0467b022713cc6a9334"
WORKFLOW_MERGE = "36da845855a01da8003b699f8a68478427424d42"
COMPLETE = {"complete", "completed", "completed_verified"}
ACTIVE = {"started", "in_progress"}

def fail(msg):
    raise SystemExit("PPIA-10 COMPLETION CONTRACT: FAIL — " + msg)

def req(cond, msg):
    if not cond:
        fail(msg)

def load(path):
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    for p in (MAN, TAX, AUTH, INS, CASES, WF, TRACE, REPORT, BACKLOG, CP, PTR, STATUS):
        req(p.exists(), f"missing {p.relative_to(ROOT)}")
    man, tax, auth, ins, cases, wf, trace = map(load, (MAN, TAX, AUTH, INS, CASES, WF, TRACE))
    backlog, cp, ptr, status = map(load, (BACKLOG, CP, PTR, STATUS))
    report = REPORT.read_text(encoding="utf-8")

    req(man.get("format") == "multiversal-ppia10-source-manifest", "source manifest identity")
    req(man.get("direct_pdf_totals") == {"files": 5, "pages": 44}, "direct PDF boundary")
    req(all(x.get("visual_review_complete") is True for x in man.get("direct_pdf_sources", [])), "all direct PDFs visually reviewed")
    req(man.get("direct_structured_totals") == {"files": 2, "rows": 1374, "structural_relevant_rows": 94}, "structured source boundary")
    req(len(man.get("source_backed_findings", [])) == 18, "source-backed finding count")
    req(len(man.get("explicit_source_gaps", [])) == 12, "explicit source-gap count")
    req(all(v is False for v in man.get("non_assumptions", {}).values()), "source non-assumptions must remain false")

    layers = tax.get("identity_state_layers", [])
    profiles = tax.get("presentation_profiles", [])
    req([x.get("id") for x in layers] == [f"P10-L{i:02d}" for i in range(1, 19)], "18 semantic layers changed")
    req(len(profiles) == 14 and len(set(profiles)) == 14, "14 presentation profiles changed")
    req(all(v is False for v in tax.get("foundation_non_assumptions", {}).values()), "taxonomy non-assumptions changed")
    handoffs = auth.get("domain_handoffs", [])
    req([x.get("id") for x in handoffs] == [f"P10-HO-{i:03d}" for i in range(1, 16)], "15 domain handoffs changed")
    guard = " ".join(auth.get("blocking_guardrails", [])).lower()
    for phrase in ("directional", "no universal", "membership", "rank", "objective truth", "mind control",
                   "filtered before graph topology", "atomic event group", "information path",
                   "expected_version", "operation_id", "semantic nonvisual", "ai", "no application runtime"):
        req(phrase in guard, f"authority guardrail missing {phrase!r}")

    groups = ins.get("projection_groups", [])
    actions = ins.get("actions", [])
    req([x.get("id") for x in groups] == [f"P10-PG-{i:03d}" for i in range(1, 19)], "18 projection groups changed")
    req([x.get("id") for x in actions] == [f"P10-ACT-{i:03d}" for i in range(1, 35)], "34 governed actions changed")
    writes = [x for x in actions if x.get("kind") == "write"]
    reads = [x for x in actions if x.get("kind") == "read"]
    req(len(writes) == 24 and len(reads) == 10, "24-write / 10-read split changed")
    req(all(x.get("protocol") == "P10-MUT-001" for x in writes), "write mutation protocol changed")
    protocol = ins.get("mutation_protocols", {}).get("P10-MUT-001", {})
    req(protocol.get("required") == ["authorization", "expected_version", "operation_id"], "mutation required protocol changed")
    req(protocol.get("offline_authoritative_mutation") is False, "offline authoritative mutation boundary changed")
    req(ins.get("projection_policy", {}).get("filter_before_derivatives") is True, "permission-before-derivatives changed")
    req(ins.get("projection_policy", {}).get("hidden_derivative_leak") is False, "hidden derivative leak boundary changed")

    req(cases.get("imported_case_count") == 72 and cases.get("local_case_count") == 18 and cases.get("resolved_case_count") == 90, "90-case corpus counts changed")
    req(len(cases.get("local_cases", [])) == 18, "local case count changed")
    req(all(v is False for v in cases.get("policy", {}).values()), "reference-case policy drift")
    titles = {x.get("title") for x in cases.get("local_cases", [])}
    for title in ("Directional relationship source boundary", "Standing requires attributable information path",
                  "Influence remains separate from standing", "Membership rank office service and permission stay separate",
                  "Atomic Social Mode consequences and compensation", "Hidden derivatives do not leak",
                  "Revocation purges two-device protected projections", "AI proposal remains nonauthoritative until acceptance"):
        req(title in titles, f"required completion reference case missing {title}")

    req(wf.get("format") == "multiversal-ppia10-workflow-authoring-contract-matrix", "workflow index identity")
    req(wf.get("policy", {}).get("workflow_count") == 18 and wf.get("policy", {}).get("authoritative_mutation_workflow_count") == 15 and wf.get("policy", {}).get("read_only_workflow_count") == 3, "workflow index counts changed")
    req(trace.get("format") == "multiversal-ppia10-workflow-traceability-matrix", "traceability identity")
    req(trace.get("counts") == {"workflows": 18, "mutation": 15, "read_only": 3}, "trace workflow counts changed")
    req(trace.get("coverage") == {"pg": "18/18", "profiles": "14/14", "actions": "34/34", "cases": "90/90 exactly once", "handoffs": "15/15"}, "workflow traceability coverage changed")
    assertions = " ".join(trace.get("assertions", [])).lower()
    for phrase in ("directional relationships", "hidden filtering before derivatives", "no universal relationship",
                   "standing requires source event", "membership/rank/office/permission separate", "influence separate from standing",
                   "atomic cross-domain event group", "external references do not transfer ownership", "expected_version + operation_id",
                   "semantic nonvisual parity", "ai proposal-only", "no application runtime"):
        req(phrase in assertions, f"workflow assertion missing {phrase!r}")

    lower = report.lower()
    for phrase in ("completion candidate — not complete until this exact head passes required validation and merges",
                   FOUNDATION_HEAD.lower(), FOUNDATION_MERGE.lower(), INSPECTOR_HEAD.lower(), INSPECTOR_MERGE.lower(),
                   WORKFLOW_HEAD.lower(), WORKFLOW_MERGE.lower(), "directional metrics", "secrets and visibility",
                   "reputation / standing", "faction structures", "consequences", "reference fixtures",
                   "90 deterministic reference cases", "18 semantic layers", "14 presentation profiles", "34 governed actions",
                   "24 authoritative mutations / 10 reads", "15 explicit domain handoffs", "expected_version", "operation_id",
                   "semantic nonvisual", "proposal-only", "ppia-10 → ppia-11 transition"):
        req(phrase in lower, f"completion report missing {phrase!r}")

    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    req("PPIA-10" in tranches and "PPIA-11" in tranches, "PPIA-10/PPIA-11 backlog entries missing")
    cp_status = cp.get("status")
    req(cp_status in {"started", "completed_verified"}, f"unexpected PPIA-10 checkpoint status {cp_status!r}")
    req(cp.get("attempt_id") == "PPIA-10-attempt-001" and cp.get("branch") == "governance/ppia-10-relationship-social-faction", "PPIA-10 checkpoint identity changed")
    req(cp.get("unresolved_failures") == [] and cp.get("owner_decision_required") is False, "PPIA-10 unresolved state")
    history = json.dumps({"last_verified_action": cp.get("last_verified_action"), "completed_substeps": cp.get("completed_substeps", []), "validation": cp.get("validation", []), "evidence": cp.get("evidence", [])}, ensure_ascii=False).lower()
    for value in (FOUNDATION_HEAD, FOUNDATION_MERGE, INSPECTOR_HEAD, INSPECTOR_MERGE, WORKFLOW_HEAD, WORKFLOW_MERGE):
        req(value.lower() in history, f"immutable milestone evidence missing {value}")

    order = backlog.get("execution_order", [])
    current_id = backlog.get("current_work_item_id")
    req(current_id in order and "PPIA-10" in order and "PPIA-11" in order, "PPIA execution order/current item invalid")
    if tranches["PPIA-10"].get("status") == "started":
        req(current_id == "PPIA-10", "candidate/pre-transition backlog must keep PPIA-10 current")
        req(tranches["PPIA-11"].get("status") == "planned", "PPIA-11 must remain planned before transition")
        req(ptr.get("primary_attempt_id") == "PPIA-10-attempt-001", "pointer must remain on PPIA-10 before transition")
        req(status.get("primary", {}).get("work_item_id") == "PPIA-10", "compact status must remain on PPIA-10 before transition")
        if cp_status == "started":
            active = ((cp.get("active_substep") or "") + " " + (cp.get("next_action") or "")).lower()
            req("completion" in active and "ppia-10" in active, "started checkpoint must be on PPIA-10 completion gate")
        else:
            req("validate ppia-10 completion contract" in history, "completed checkpoint missing completion validation evidence")
        continuity = "ppia10_completion_pretransition"
    else:
        req(tranches["PPIA-10"].get("status") == "completed_verified", "post-transition PPIA-10 status must be completed_verified")
        req(cp_status == "completed_verified", "post-transition PPIA-10 checkpoint must remain completed_verified")
        req(order.index(current_id) > order.index("PPIA-10"), "post-transition current work must advance beyond PPIA-10")
        if current_id == "PPIA-11":
            req(tranches["PPIA-11"].get("status") in ACTIVE, "PPIA-11 must be active when current")
            req(ptr.get("primary_attempt_id") == "PPIA-11-attempt-001", "post-transition pointer must select PPIA-11")
            req(status.get("primary", {}).get("work_item_id") == "PPIA-11" and status.get("primary", {}).get("status") in ACTIVE, "post-transition compact status must select active PPIA-11")
            continuity = "ppia10_historical_during_ppia11"
        else:
            req(order.index(current_id) > order.index("PPIA-11"), "later historical state must advance beyond PPIA-11")
            req(tranches["PPIA-11"].get("status") in COMPLETE, "later historical state requires PPIA-11 complete")
            req(ptr.get("primary_attempt_id") != "PPIA-10-attempt-001", "historical pointer must not return to PPIA-10")
            req(status.get("primary", {}).get("work_item_id") == current_id, "compact status must match current later PPIA work item")
            continuity = "ppia10_historical_after_ppia11"

    req(backlog.get("boundaries", {}).get("application_runtime_mutation_authorized") is False, "runtime mutation boundary changed")
    req(backlog.get("boundaries", {}).get("a2_activation_authorized") is False, "A2 activation boundary changed")
    req(backlog.get("boundaries", {}).get("release_authorized") is False, "release boundary changed")
    req(backlog.get("boundaries", {}).get("deployment_authorized") is False, "deployment boundary changed")
    req(backlog.get("boundaries", {}).get("tester_access_authorized") is False, "tester boundary changed")

    print("PPIA-10 COMPLETION CONTRACT: PASS")
    print("source=5 PDFs/44 pages + 2 CSVs/1374 rows/94 explicit social-faction rows")
    print("surface=18 layers / 14 profiles / 18 projection groups / 34 actions / 90 cases / 18 workflows / 15 handoffs")
    print("workflow_split=15 mutation / 3 read-only; action_split=24 write / 10 read")
    print("completion_gate=directional metrics + secrets + reputation + faction structures + consequences + visibility + reference fixtures")
    print("traceability_gaps=0 runtime_activation=false")
    print("continuity_mode=" + continuity)

if __name__ == "__main__":
    main()
