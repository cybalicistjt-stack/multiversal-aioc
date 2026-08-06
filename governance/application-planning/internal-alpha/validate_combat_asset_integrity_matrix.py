#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
SPEC = ROOT / "IA-D06-005_COMBAT_ASSET_INTEGRITY_MATRIX_SPEC.md"
MATRIX = ROOT / "IA-D06-005_COMBAT_ASSET_INTEGRITY_MATRIX.json"
TRACE = ROOT / "IA-D06-005_IMPLEMENTATION_TRACEABILITY.json"
REVIEW = ROOT / "IA-D06-005_REVIEW_RECEIPT.md"
READINESS = ROOT / "IA-D06-005_READINESS_RECORD.md"
COMPLETION = ROOT / "IA-D06-005_COMPLETION_RECORD.json"
BACKLOG = ROOT / "INTERNAL_ALPHA_DESIGN_BACKLOG.md"


def req(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def load(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"cannot parse {path.name}: {exc}")
        return {}


def main() -> int:
    errors: list[str] = []
    for path in [SPEC, MATRIX, TRACE, REVIEW, READINESS, COMPLETION, BACKLOG]:
        req(path.exists(), f"missing {path.name}", errors)
    if errors:
        print("\n".join(errors)); return 1
    spec = SPEC.read_text(encoding="utf-8")
    backlog = BACKLOG.read_text(encoding="utf-8")
    review = REVIEW.read_text(encoding="utf-8")
    readiness = READINESS.read_text(encoding="utf-8")
    matrix = load(MATRIX, errors)
    trace = load(TRACE, errors)
    completion = load(COMPLETION, errors)
    req(spec.startswith("# IA-D06-005 — Combat/Asset Integrity Matrix"), "spec title", errors)
    for phrase in ["single atomic authoritative result group", "P9-06-008-attempt-002", "IA-D06-006"]:
        req(phrase.lower() in spec.lower(), f"spec missing {phrase}", errors)
    req(matrix.get("workItemId") == "IA-D06-005", "matrix work item", errors)
    req(len(matrix.get("fixtures", [])) == 24, "fixture count", errors)
    req(len(matrix.get("implementationSlices", [])) == 8, "slice count", errors)
    req(len(matrix.get("acceptanceCriteria", [])) == 28, "criteria count", errors)
    req(matrix.get("resolvedFindings") == 7, "resolved findings", errors)
    req(matrix.get("blockingFindings") == [], "blocking findings", errors)
    req(matrix.get("nextWorkItemId") == "IA-D06-006", "matrix next", errors)
    req(trace.get("acceptanceCriteriaCount") == 28 and trace.get("fixtureCount") == 24, "trace metrics", errors)
    req(completion.get("status") == "complete-design-implementation-ready", "completion status", errors)
    req(completion.get("nextWorkItemId") == "IA-D06-006", "completion next", errors)
    req("implementation-ready" in review.lower(), "review readiness", errors)
    req("implementation-ready" in readiness.lower(), "readiness decision", errors)
    req("**Version:** 0.24.0" in backlog, "backlog version", errors)
    req("IA-D06-005 — combat/Asset integrity matrix — complete" in backlog, "backlog completion", errors)
    req("IA-D06-006 — combat and Assets integration review — next" in backlog, "backlog next", errors)
    req("**IA-D06-006 — combat and Assets integration review — next.**" in backlog, "backlog current next", errors)
    if errors:
        print("IA-D06-005 COMBAT/ASSET INTEGRITY VALIDATION: FAIL")
        for e in errors: print(f"- {e}")
        return 1
    print("IA-D06-005 COMBAT/ASSET INTEGRITY VALIDATION: PASS")
    print("Fixtures: 24")
    print("Implementation slices: 8")
    print("Acceptance criteria: 28")
    print("Resolved findings: 7")
    print("Blocking findings: 0")
    return 0

if __name__ == "__main__":
    sys.exit(main())
