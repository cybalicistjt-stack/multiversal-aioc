#!/usr/bin/env python3
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PKT = ROOT / "feature-packets"
SPEC = PKT / "MV-IA-F014_VEHICLE_MECHA_STARSHIP_OPERATIONS_DESIGN.md"
MATRIX = PKT / "MV-IA-F014_VEHICLE_OPERATIONS_MATRIX.json"
TRACE = PKT / "IA-D06-004_IMPLEMENTATION_TRACEABILITY.json"
REVIEW = PKT / "IA-D06-004_REVIEW_RECEIPT.md"
READY = PKT / "IA-D06-004_READINESS_RECORD.md"
COMPLETE = PKT / "IA-D06-004_COMPLETION_RECORD.json"
BACKLOG = ROOT / "INTERNAL_ALPHA_DESIGN_BACKLOG.md"


def main() -> int:
    errors: list[str] = []
    for p in [SPEC, MATRIX, TRACE, REVIEW, READY, COMPLETE, BACKLOG]:
        if not p.exists(): errors.append(f"missing {p.name}")
    if errors:
        print("IA-D06-004 VEHICLE OPERATIONS VALIDATION: FAIL")
        print("\n".join(f"- {e}" for e in errors)); return 1
    spec = SPEC.read_text(encoding="utf-8")
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    trace = json.loads(TRACE.read_text(encoding="utf-8"))
    completion = json.loads(COMPLETE.read_text(encoding="utf-8"))
    backlog = BACKLOG.read_text(encoding="utf-8")
    checks = [
        ("Vehicle, Mecha, and Starship Operations" in spec, "title"),
        (len(matrix.get("operationalClasses", [])) == 10, "operationalClasses count"),
        (len(matrix.get("stations", [])) == 12, "stations count"),
        (len(matrix.get("states", [])) == 13, "states count"),
        (len(matrix.get("fixtures", [])) == 24, "fixtures count"),
        (len(matrix.get("implementationSlices", [])) == 8, "slices count"),
        (len(matrix.get("acceptanceCriteria", [])) == 28, "criteria count"),
        (matrix.get("blockingFindings") == [], "blocking findings"),
        (len(trace.get("acceptanceTraceability", [])) == 28, "traceability count"),
        (completion.get("status") == "complete-design-implementation-ready", "completion status"),
        (completion.get("nextWorkItemId") == "IA-D06-005", "completion next"),
        ("IA-D06-004 — basic MV-IA-F014 Vehicle, Mecha, and Starship Operations — complete" in backlog, "backlog complete"),
        ("IA-D06-005 — combat/Asset integrity matrix — next" in backlog, "backlog next"),
        ("P9-06-008-attempt-002" in spec and "P9-06-008-attempt-002" in backlog, "parallel work preservation")
    ]
    errors.extend(name for ok, name in checks if not ok)
    if errors:
        print("IA-D06-004 VEHICLE OPERATIONS VALIDATION: FAIL")
        print("\n".join(f"- {e}" for e in errors)); return 1
    print("IA-D06-004 VEHICLE OPERATIONS VALIDATION: PASS")
    print("Fixtures: 24\nImplementation slices: 8\nAcceptance criteria: 28\nBlocking findings: 0")
    return 0

if __name__ == "__main__": sys.exit(main())
