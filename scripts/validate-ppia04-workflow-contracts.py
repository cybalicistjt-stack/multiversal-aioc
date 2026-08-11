#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
WORKFLOWS = BASE / "PPIA-04_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
MATRIX = BASE / "PPIA-04_VEHICLE_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-04_REFERENCE_CASES_v0.1.0.json"
TAXONOMY = BASE / "PPIA-04_VEHICLE_EXPERIENCE_TAXONOMY_v0.1.0.json"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-04 WORKFLOW CONTRACTS: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def main() -> None:
    for path in (WORKFLOWS, MATRIX, CASES, TAXONOMY):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    doc = json.loads(WORKFLOWS.read_text(encoding="utf-8"))
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    cases = json.loads(CASES.read_text(encoding="utf-8"))

    require(doc.get("format") == "multiversal-ppia04-vehicle-workflow-authoring-contract-matrix", "wrong workflow format")
    require(doc.get("inherits") == [TAXONOMY.name, MATRIX.name, CASES.name], "workflow inheritance changed")

    workflows = doc.get("workflows", [])
    require(len(workflows) == 15, f"expected 15 workflows, got {len(workflows)}")
    require([w.get("workflow_id") for w in workflows] == [f"VS-WF-{n:03d}" for n in range(1, 16)], "workflow IDs must be continuous VS-WF-001..015")

    for workflow in workflows:
        for key in ("primary_personas", "entry_points", "preconditions", "steps", "outputs", "mutation_owner", "privacy_requirements", "recovery_requirements", "accessibility_requirements", "reference_cases", "forbidden_mutations"):
            require(workflow.get(key), f"{workflow['workflow_id']} missing {key}")

    mutation_workflows = [w for w in workflows if w.get("authoritative_mutation_performed") is True]
    require(len(mutation_workflows) == 13, f"expected 13 authoritative mutation workflows, got {len(mutation_workflows)}")
    for workflow in mutation_workflows:
        joined = json.dumps(workflow, ensure_ascii=False).lower()
        require(workflow.get("revalidation_points"), f"{workflow['workflow_id']} missing revalidation points")
        require("version" in joined or "revalid" in joined, f"{workflow['workflow_id']} missing version/revalidation boundary")
        require("operation id" in joined or "idempot" in joined or "event" in joined, f"{workflow['workflow_id']} missing idempotency/event recovery boundary")

    handoffs = doc.get("handoff_contracts", [])
    require(len(handoffs) == 10, f"expected 10 handoffs, got {len(handoffs)}")
    require([h.get("handoff_id") for h in handoffs] == [f"VS-HO-{n:03d}" for n in range(1, 11)], "handoff IDs must be continuous VS-HO-001..010")
    for handoff in handoffs:
        require(handoff.get("payload"), f"{handoff['handoff_id']} missing payload")
        require(handoff.get("rule"), f"{handoff['handoff_id']} missing rule")

    expected_cases = [f"PPIA04-RC-{n:03d}" for n in range(1, 21)]
    require([case.get("case_id") for case in cases.get("cases", [])] == expected_cases, "reference case source set changed")
    coverage = doc.get("reference_case_coverage", {})
    require(list(coverage) == expected_cases, "reference-case coverage keys changed")
    require(all(coverage[case_id] for case_id in expected_cases), "one or more reference cases lack workflow coverage")

    matrix_actions = {item.get("id") for item in matrix.get("action_contracts", [])}
    require(len(matrix_actions) == 14, "expected 14 inspector action contracts")
    full = json.dumps(doc, ensure_ascii=False).lower()
    for phrase in (
        "ownership", "custody", "station authority", "name similarity", "source-unspecified",
        "semantic position", "canvas", "operation id", "hidden", "carried craft", "damage",
        "dock", "board", "launch", "capture", "salvage", "ppia-03", "mv-ia-f007",
        "mv-ia-f013", "mv-ia-f014", "mv-ia-f020", "mv-ia-f021", "screen-reader",
        "newtonian", "programmable vehicle ai", "stage-a-a2"
    ):
        require(phrase in full, f"missing required workflow boundary {phrase!r}")

    boundaries = " ".join(doc.get("authoring_boundaries", {}).get("not_allowed_here", []))
    for phrase in ("R1", "source-unspecified", "PPIA-03", "F007", "F013", "F014", "F020/F021", "IA-D08-003", "STAGE-A-A2"):
        require(phrase in boundaries, f"authoring boundary missing {phrase!r}")

    invariants = doc.get("completion_invariants", [])
    require(len(invariants) == 8, "expected eight completion invariants")
    require(any("accessible nonvisual" in item.lower() for item in invariants), "accessible nonvisual invariant missing")
    require(any("20 ppia-04 reference cases" in item.lower() for item in invariants), "20-case coverage invariant missing")
    require(any("13 authoritative" in item.lower() for item in invariants), "mutation workflow invariant missing")

    print("PPIA-04 WORKFLOW CONTRACTS: PASS")
    print("workflows=15")
    print("authoritative_mutation_workflows=13")
    print("handoffs=10")
    print("reference_cases_covered=20")
    print("completion_invariants=8")


if __name__ == "__main__":
    main()
