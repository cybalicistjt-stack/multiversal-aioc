#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
P = ROOT / "feature-packets"
CONTRACT = P / "IA-D04-002_PROPOSAL_APPROVAL_SHARED_COMPONENT_CONTRACT.md"
MATRIX = P / "IA-D04-002_PROPOSAL_APPROVAL_COMPONENT_MATRIX.json"
TRACE = P / "IA-D04-002_IMPLEMENTATION_TRACEABILITY.json"
REVIEW = P / "IA-D04-002_REVIEW_RECEIPT.md"
READINESS = P / "IA-D04-002_READINESS_RECORD.md"
COMPLETION = P / "IA-D04-002_COMPLETION_RECORD.json"
F006 = P / "MV-IA-F006_ACTION_APPROVAL_MATRIX.json"
BACKLOG = ROOT / "INTERNAL_ALPHA_DESIGN_BACKLOG.md"
PROGRAM = ROOT / "README.md"
INDEX = P / "README.md"
ROADMAP = ROOT.parents[2] / "governance/ai/runtime/ROADMAP_INDEX.json"

CRITERIA = [f"PAC-AC-{i:03d}" for i in range(1, 21)]
FIXTURES = [f"PAC-FX-{i:03d}" for i in range(1, 17)]
SLICES = [f"PAC-S{i:02d}" for i in range(1, 9)]


def load(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"cannot parse {path}: {exc}")
        return {}


def need(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def phrases(text: str, required: list[str], label: str, errors: list[str]) -> None:
    lower = text.lower()
    for phrase in required:
        need(phrase.lower() in lower, f"{label} missing {phrase!r}", errors)


def version(text: str) -> tuple[int, ...]:
    match = re.search(r"\*\*Version:\*\* ([0-9]+(?:\.[0-9]+)+)", text)
    return tuple(int(part) for part in match.group(1).split(".")) if match else ()


def main() -> int:
    errors: list[str] = []
    required = [CONTRACT, MATRIX, TRACE, REVIEW, READINESS, COMPLETION, F006, BACKLOG, PROGRAM, INDEX, ROADMAP]
    for path in required:
        need(path.is_file(), f"missing required file {path}", errors)
    if errors:
        print("\n".join(errors))
        return 1

    contract = CONTRACT.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")
    readiness = READINESS.read_text(encoding="utf-8")
    backlog = BACKLOG.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")
    index = INDEX.read_text(encoding="utf-8")
    matrix = load(MATRIX, errors)
    trace = load(TRACE, errors)
    completion = load(COMPLETION, errors)
    f006 = load(F006, errors)
    roadmap = load(ROADMAP, errors)

    need(contract.startswith("# IA-D04-002 — Proposal and Approval Shared-Component Contract"), "contract title mismatch", errors)
    sections = [int(match.group(1)) for line in contract.splitlines() if (match := re.match(r"^## (\d+)\. ", line))]
    need(sections == list(range(1, 25)), f"contract sections must be 1-24 exactly; got {sections}", errors)
    phrases(contract, [
        "IA-D02-006", "IA-D03-005", "MV-IA-F006", "approve, deny, and modify-and-approve",
        "Silence is not approval", "review claim is advisory", "original accepted proposal is immutable",
        "server-side projection", "status lookup", "atomic", "zero paid services and zero AI", "IA-D04-003"
    ], "contract", errors)
    for criterion in CRITERIA:
        need(criterion in contract, f"contract missing {criterion}", errors)

    identity = (matrix.get("programId"), matrix.get("workItemId"), matrix.get("contractId"), matrix.get("owner"), matrix.get("status"))
    need(identity == ("MV-IA-001", "IA-D04-002", "MV-IA-SS06-PROPOSAL-APPROVAL", "John Brandon Turner", "implementation-ready-design"), "matrix identity/status mismatch", errors)
    counts = {
        "consumerProfiles": 7,
        "componentSurfaces": 12,
        "stateVocabulary": 15,
        "proposalRequiredFields": 24,
        "decisionReceiptRequiredFields": 20,
        "validationClasses": 24,
        "operationTypes": 22,
        "eventTypes": 22,
        "deniedCases": 32,
        "deterministicFixtures": 16,
        "implementationSlices": 8,
        "acceptanceCriteria": 20,
    }
    for key, expected in counts.items():
        need(len(matrix.get(key, [])) == expected, f"matrix {key} must contain {expected}", errors)
    need([item.get("fixtureId") for item in matrix.get("deterministicFixtures", [])] == FIXTURES, "fixture IDs mismatch", errors)
    need([item.get("sliceId") for item in matrix.get("implementationSlices", [])] == SLICES, "slice IDs mismatch", errors)
    need([item.get("criterionId") for item in matrix.get("acceptanceCriteria", [])] == CRITERIA, "acceptance IDs mismatch", errors)
    need(all(item.get("blocking") is True for item in matrix.get("acceptanceCriteria", [])), "all acceptance criteria must be blocking", errors)
    need(matrix.get("blockingFindings") == [], "matrix retains blocking findings", errors)
    need(matrix.get("nextWorkItemId") == "IA-D04-003", "matrix next item mismatch", errors)
    for flag in ["implementationAuthorized", "paidServicesAuthorized", "productionCredentialsAuthorized", "realUserDataCollectionAuthorized", "internalAlphaReleaseAuthorized", "productionAuthorized", "publicReleaseAuthorized", "canonicalPromotionAuthorized"]:
        need(matrix.get("authorizations", {}).get(flag) is False, f"matrix {flag} must be false", errors)

    need(f006.get("nextWorkItemId") == "IA-D04-002", "F006 handoff to IA-D04-002 not preserved", errors)
    need(trace.get("workItemId") == "IA-D04-002" and trace.get("status") == "complete", "traceability identity mismatch", errors)
    need([item.get("criterionId") for item in trace.get("acceptanceTraceability", [])] == CRITERIA, "traceability criteria mismatch", errors)
    need([item.get("fixtureId") for item in trace.get("fixtureTraceability", [])] == FIXTURES, "traceability fixtures mismatch", errors)
    need([item.get("sliceId") for item in trace.get("implementationSlices", [])] == SLICES, "traceability slices mismatch", errors)
    need(trace.get("untracedAcceptanceCriteria") == [] and trace.get("blockingFindings") == [], "traceability gaps or blocking findings", errors)

    metrics = completion.get("metrics", {})
    need((completion.get("workItemId"), completion.get("status"), completion.get("owner")) == ("IA-D04-002", "complete-design-implementation-ready", "John Brandon Turner"), "completion identity/status mismatch", errors)
    expected_metrics = {"packetSections":24,"consumerProfiles":7,"componentSurfaces":12,"stateVocabulary":15,"proposalRequiredFields":24,"decisionReceiptFields":20,"validationClasses":24,"operationTypes":22,"eventTypes":22,"deniedCases":32,"fixtures":16,"implementationSlices":8,"acceptanceCriteria":20,"blockingFindings":0}
    for key, expected in expected_metrics.items():
        need(metrics.get(key) == expected, f"completion {key} must be {expected}", errors)
    need(completion.get("nextDesignAction", {}).get("workItemId") == "IA-D04-003", "completion next action mismatch", errors)

    phrases(review, ["PASS — IMPLEMENTATION-READY DESIGN", "seven governed consumer profiles", "sixteen deterministic fixtures", "zero blocking findings", "Silence is not approval", "IA-D04-003"], "review", errors)
    phrases(readiness, ["READY FOR IMPLEMENTATION HANDOFF — DEPENDENCY GATED", "versioned consumer profiles", "atomic Event-backed commit adapters", "zero-service operation", "IA-D04-003"], "readiness", errors)
    need(version(backlog) >= (0, 14, 0), "backlog version must be at least 0.14.0", errors)
    phrases(backlog, ["IA-D04-002 — proposal and approval shared-component contract — complete", "IA-D04-003 — two-device interruption and reconnect matrix — next"], "backlog", errors)
    need(version(program) >= (0, 14, 0), "program version must be at least 0.14.0", errors)
    phrases(program, ["IA-D04-002 — Proposal and Approval Shared-Component Contract", "IA-D04-003 — Two-Device Interruption and Reconnect Matrix"], "program", errors)
    phrases(index, ["IA-D04-002_PROPOSAL_APPROVAL_SHARED_COMPONENT_CONTRACT.md", "IA-D04-002_PROPOSAL_APPROVAL_COMPONENT_MATRIX.json", "IA-D04-003"], "packet index", errors)
    roadmap_ids = {item.get("work_item_id") for item in roadmap.get("entries", [])}
    need({"IA-D04-002", "IA-D04-003"} <= roadmap_ids, "roadmap missing IA-D04-002 or IA-D04-003", errors)

    if errors:
        print("IA-D04-002 PROPOSAL/APPROVAL SHARED COMPONENT VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("IA-D04-002 PROPOSAL/APPROVAL SHARED COMPONENT VALIDATION: PASS")
    print("Consumer profiles: 7")
    print("Component surfaces: 12")
    print("States: 15")
    print("Proposal fields: 24")
    print("Decision receipt fields: 20")
    print("Validation classes: 24")
    print("Operations: 22")
    print("Events: 22")
    print("Denied cases: 32")
    print("Fixtures: 16")
    print("Implementation slices: 8")
    print("Acceptance criteria: 20")
    print("Blocking findings: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
