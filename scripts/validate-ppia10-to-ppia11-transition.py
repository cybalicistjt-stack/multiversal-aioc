#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P10_REPORT = BASE / "PPIA-10_COMPLETION_REPORT.md"
P10 = ROOT / "governance/ai/work-state/PPIA-10-attempt-001.json"
P11 = ROOT / "governance/ai/work-state/PPIA-11-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BALANCE = ROOT / "governance/balance/8D-007_COMPLETION_GOVERNANCE.json"
CORPUS = ROOT / "governance/balance/8D-007_GOLDEN_CORPUS_CONTRACT.json"

P10_FINAL_HEAD = "507c9da21dd74d771f910861323693e2d7193bfa"
P10_COMPLETION_PR = 261
P10_COMPLETION_MERGE = "b4ac8c080af7055e2d150ab6d37de41e9cc2a68f"
P10_COMPLETION_RUN = "31585946135"
P11_BRANCH = "governance/ppia-11-encounter-balance-laboratory"
P11_FINAL_MERGE = "f2274707b1337425f0bc9ac8d1dd5ebb08d9f883"
COMPLETE = {"complete", "completed", "completed_verified"}
ACTIVE = {"started", "in_progress"}
PPIA_CLOSED = "completed_verified_owner_approved_parallel_work"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-10→PPIA-11 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p10 = load(P10)
    p11 = load(P11)
    pointer = load(POINTER)
    status = load(STATUS)
    balance = load(BALANCE)
    corpus = load(CORPUS)
    report = P10_REPORT.read_text(encoding="utf-8")

    tranches = {x["work_item_id"]: x for x in backlog["tranches"]}
    require(tranches["PPIA-10"]["status"] == "completed_verified", "PPIA-10 backlog must be completed_verified")
    require(tranches["PPIA-11"]["status"] in ACTIVE | COMPLETE, "PPIA-11 backlog must be active or historically complete")
    require(set(tranches["PPIA-11"].get("dependencies", [])) == {"PPIA-02","PPIA-03","PPIA-04","PPIA-05"}, "PPIA-11 declared dependencies changed")
    for dep in tranches["PPIA-11"]["dependencies"]:
        require(tranches[dep]["status"] in COMPLETE, f"PPIA-11 dependency {dep} is not complete")
    order = backlog["execution_order"]
    require(order.index("PPIA-10") + 1 == order.index("PPIA-11"), "dependency-optimized order must place PPIA-11 after PPIA-10")

    require(p10["status"] == "completed_verified", "PPIA-10 checkpoint must be completed_verified")
    require(p10["active_substep"] is None and p10.get("completed_at"), "PPIA-10 completion timestamp/substep invalid")
    require(p10["latest_pushed_commit"] == P10_FINAL_HEAD, "PPIA-10 exact validated completion head mismatch")
    require(p10["pull_request"] == P10_COMPLETION_PR, "PPIA-10 completion PR mismatch")
    require(p10["merge_commit"] == P10_COMPLETION_MERGE, "PPIA-10 completion merge mismatch")
    require(not p10["unresolved_failures"] and p10["owner_decision_required"] is False, "PPIA-10 completion has unresolved state")
    require(any(P10_COMPLETION_RUN in v.get("command", "") and v.get("status") == "passed" for v in p10["validation"]), "PPIA-10 completion-gate evidence missing")
    evidence_text = json.dumps(p10.get("evidence", []), ensure_ascii=False)
    for value in (P10_FINAL_HEAD, "PR #261", P10_COMPLETION_MERGE, P10_COMPLETION_RUN):
        require(value in evidence_text, f"PPIA-10 immutable completion evidence missing {value}")
    for phrase in ("completion candidate", "directional metrics", "secrets", "reputation", "faction structures", "consequences", "visibility", "reference fixtures"):
        require(phrase in report.lower(), f"PPIA-10 completion report missing {phrase!r}")

    require(p11["work_item_id"] == "PPIA-11" and p11["attempt_id"] == "PPIA-11-attempt-001", "PPIA-11 checkpoint identity mismatch")
    require(p11["branch"] == P11_BRANCH, "PPIA-11 governed branch mismatch")
    require(p11["base_commit"] == P10_COMPLETION_MERGE, "PPIA-11 base must be PPIA-10 completion merge")
    require(p11["status"] in ACTIVE | {"completed_verified"}, "PPIA-11 checkpoint must be active or completed_verified")
    require(p11["owner_decision_required"] is False and p11["unresolved_failures"] == [], "PPIA-11 transition must be unblocked")
    scope = json.dumps({
        "objective": p11.get("objective"), "active_substep": p11.get("active_substep"), "next_action": p11.get("next_action"),
        "completed_substeps": p11.get("completed_substeps", []), "evidence": p11.get("evidence", []), "notes": p11.get("notes", [])
    }, ensure_ascii=False).lower()
    for phrase in ("threat", "capability", "environment", "action economy", "resource", "mixed encounter", "boss", "wave", "reinforcement", "retreat", "uncertainty", "benchmark", "calibration", "guaranteed-balance", "source mechanics", "non-destructive"):
        require(phrase in scope, f"PPIA-11 governed scope missing {phrase!r}")

    require(balance.get("workstream") == "8D-007 Golden Test Corpus and Balance Harness", "8D-007 balance governance identity changed")
    criteria = balance["completionCriteria"]
    require(criteria["representativeCoverageDomains"] == 18 and criteria["goldenFixtures"] == 36, "8D-007 coverage/fixture counts changed")
    require(criteria["deterministicScenarios"] == 24 and criteria["scenarioExecutions"] == 72, "8D-007 scenario counts changed")
    require(criteria["nonDestructiveRecommendationsRecorded"] == 36 and criteria["mutationSensitivityCases"] == 7, "8D-007 recommendation/sensitivity counts changed")
    require(criteria["sourceTruthChanged"] is False and criteria["installationResidue"] == 0 and criteria["blockingObservations"] == 0, "8D-007 evidence boundary changed")
    gov = balance["governance"]
    require(gov["canonicalSourceMechanicsImmutable"] is True and gov["recommendationsRemainSeparate"] is True, "8D-007 source/recommendation separation changed")
    require(gov["automaticBalanceRewriteProhibited"] is True and gov["regressionFailuresBlockMerge"] is True, "8D-007 mutation/regression governance changed")
    require(corpus.get("documentId") == "MV-8D-007-CONTRACT-001", "8D-007 corpus contract identity changed")

    current_id = backlog["current_work_item_id"]
    if current_id == "PPIA-11":
        require(tranches["PPIA-11"]["status"] in ACTIVE and p11["status"] in ACTIVE, "active PPIA-11 continuity requires active status")
        require(pointer["primary_attempt_id"] == "PPIA-11-attempt-001", "pointer must select PPIA-11")
        selected = [x for x in pointer["active_attempts"] if x.get("owner_selected")]
        require(len(selected) == 1 and selected[0]["work_item_id"] == "PPIA-11", "exactly one owner-selected PPIA-11 attempt required")
        current = selected[0]
        for field in ("attempt_id", "branch", "status", "updated_at", "roadmap_projection_pending"):
            require(current[field] == p11[field], f"pointer/PPIA-11 checkpoint mismatch: {field}")
        require(current["checkpoint_path"] == "governance/ai/work-state/PPIA-11-attempt-001.json", "PPIA-11 checkpoint path mismatch")
        primary = status["primary"]
        for field in ("work_item_id", "attempt_id", "branch", "status", "active_substep", "next_action", "latest_pushed_commit", "pull_request", "owner_decision_required", "unresolved_failures", "roadmap_projection_pending"):
            require(primary[field] == p11[field], f"compact status/PPIA-11 checkpoint mismatch: {field}")
        require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "active PPIA-11 pointer must explain batched roadmap projection")
        transition_mode = "active_ppia11"
    else:
        require(order.index(current_id) > order.index("PPIA-11"), "historical transition may only validate after PPIA-11")
        require(tranches["PPIA-11"]["status"] in COMPLETE, "historical PPIA-11 backlog must be complete")
        require(p11["status"] == "completed_verified", "historical PPIA-11 checkpoint must be completed_verified")
        require(p11.get("merge_commit") == P11_FINAL_MERGE, "historical PPIA-11 completion merge changed")
        require(pointer["primary_attempt_id"] != "PPIA-11-attempt-001", "historical pointer must advance beyond PPIA-11")
        require(status["primary"]["work_item_id"] != "PPIA-11", "historical compact status must advance beyond PPIA-11")
        if backlog.get("status") == PPIA_CLOSED:
            require(current_id == "PPIA-16", "closed PPIA historical transition must retain PPIA-16 final anchor")
            require(tranches["PPIA-16"]["status"] == "completed_verified", "closed PPIA final tranche must remain completed_verified")
            transition_mode = "historical_after_ppia11_program_closed"
        else:
            require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "in-flight historical pointer must explain batched roadmap projection")
            transition_mode = "historical_after_ppia11"

    boundaries = backlog["boundaries"]
    for key in ("application_runtime_mutation_authorized", "a2_activation_authorized", "release_authorized", "deployment_authorized", "tester_access_authorized", "canonical_promotion_without_source_evidence_authorized"):
        require(boundaries[key] is False, f"transition may not enable {key}")

    print("PPIA-10→PPIA-11 TRANSITION: PASS")
    print(f"ppia10_final_head={P10_FINAL_HEAD}")
    print(f"ppia10_final_merge={P10_COMPLETION_MERGE}")
    print("ppia10_status=completed_verified")
    print(f"ppia11_status={p11['status']}")
    print(f"ppia11_branch={P11_BRANCH}")
    print(f"transition_mode={transition_mode}")
    print("balance_anchor=8D-007 18 domains / 36 fixtures / 24 scenarios / 72 executions")
    print("source_truth_immutable=true automatic_balance_rewrite=false guaranteed_balance_claim=false")
    print("runtime_activation=false")


if __name__ == "__main__":
    main()
