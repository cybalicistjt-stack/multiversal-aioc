#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
WORKFLOWS = BASE / "PPIA-03_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
MATRIX = BASE / "PPIA-03_ITEM_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-03_REFERENCE_CASES_v0.1.0.json"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-03 WORKFLOW CONTRACTS: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def main() -> None:
    for path in (WORKFLOWS, MATRIX, CASES):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    doc = json.loads(WORKFLOWS.read_text(encoding="utf-8"))
    require(doc.get("format") == "multiversal-ppia03-item-inventory-workflow-authoring-contract-matrix", "wrong workflow format")
    require(doc.get("inherits") == [MATRIX.parent.joinpath("PPIA-03_ITEM_EXPERIENCE_TAXONOMY_v0.1.0.json").name, MATRIX.name, CASES.name], "workflow inheritance changed")

    workflows = doc.get("workflows", [])
    require(len(workflows) == 12, f"expected 12 workflows, got {len(workflows)}")
    expected_ids = [f"IT-WF-{n:03d}" for n in range(1, 13)]
    require([w.get("workflow_id") for w in workflows] == expected_ids, "workflow IDs must be continuous IT-WF-001..012")

    for workflow in workflows:
        require(workflow.get("preconditions"), f"{workflow['workflow_id']} missing preconditions")
        require(workflow.get("steps"), f"{workflow['workflow_id']} missing steps")
        require(workflow.get("outputs"), f"{workflow['workflow_id']} missing outputs")
        require(workflow.get("mutation_owner"), f"{workflow['workflow_id']} missing mutation owner")
        require(workflow.get("privacy_requirements"), f"{workflow['workflow_id']} missing privacy requirements")
        require(workflow.get("recovery_requirements"), f"{workflow['workflow_id']} missing recovery requirements")
        require(workflow.get("accessibility_requirements"), f"{workflow['workflow_id']} missing accessibility requirements")

    mutation_workflows = [w for w in workflows if w.get("authoritative_mutation_performed") is True]
    require(len(mutation_workflows) == 9, f"expected 9 authoritative mutation workflows, got {len(mutation_workflows)}")
    for workflow in mutation_workflows:
        joined = json.dumps(workflow, ensure_ascii=False).lower()
        require("revalid" in joined or "expected version" in joined, f"{workflow['workflow_id']} missing revalidation/version boundary")
        require("idempot" in joined or "operation" in joined or "event" in joined, f"{workflow['workflow_id']} missing idempotency/event recovery boundary")

    handoffs = doc.get("handoff_contracts", [])
    require(len(handoffs) == 10, f"expected 10 handoff contracts, got {len(handoffs)}")
    require([h.get("handoff_id") for h in handoffs] == [f"IT-HO-{n:03d}" for n in range(1, 11)], "handoff IDs must be continuous IT-HO-001..010")
    for handoff in handoffs:
        require(handoff.get("payload"), f"{handoff['handoff_id']} missing payload")
        require(handoff.get("rule"), f"{handoff['handoff_id']} missing rule")

    full = json.dumps(doc, ensure_ascii=False)
    for phrase in (
        "Taser",
        "source-unspecified capacity",
        "reference-only",
        "hidden Asset existence",
        "ownership",
        "custody",
        "containment cycles",
        "split",
        "merge",
        "identify",
        "durability",
        "crafting",
        "ambiguous network",
        "operation ID",
        "PPIA-04",
        "PPIA-05",
        "PPIA-11",
    ):
        require(phrase.lower() in full.lower(), f"missing required cross-workflow boundary {phrase!r}")

    authoring = doc.get("authoring_boundaries", {})
    not_allowed = " ".join(authoring.get("not_allowed_here", []))
    for phrase in ("published Item Definition", "R1 structural headings", "Taser", "reference-only", "PPIA-04", "PPIA-05", "PPIA-11"):
        require(phrase in not_allowed, f"authoring boundary missing {phrase!r}")

    invariants = doc.get("completion_invariants", [])
    require(len(invariants) == 7, "expected seven workflow completion invariants")
    require(any("accessible" in item.lower() for item in invariants), "accessible path invariant missing")
    require(any("hidden" in item.lower() and "aggregates" in item.lower() for item in invariants), "hidden aggregate invariant missing")

    print("PPIA-03 WORKFLOW CONTRACTS: PASS")
    print("workflows=12")
    print("authoritative_mutation_workflows=9")
    print("handoffs=10")
    print("completion_invariants=7")


if __name__ == "__main__":
    main()
