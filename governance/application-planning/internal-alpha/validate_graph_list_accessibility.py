from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKETS = ROOT / "feature-packets"

FILES = {
    "contract": PACKETS / "IA-D05-005_GRAPH_LIST_ACCESSIBILITY_MATRIX.md",
    "matrix": PACKETS / "IA-D05-005_GRAPH_LIST_ACCESSIBILITY_MATRIX.json",
    "trace": PACKETS / "IA-D05-005_IMPLEMENTATION_TRACEABILITY.json",
    "completion": PACKETS / "IA-D05-005_COMPLETION_RECORD.json",
    "backlog": ROOT / "INTERNAL_ALPHA_DESIGN_BACKLOG.md",
}

errors: list[str] = []
for key, path in FILES.items():
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        errors.append(f"missing or empty {key}: {path}")

if not errors:
    contract = FILES["contract"].read_text(encoding="utf-8")
    matrix = json.loads(FILES["matrix"].read_text(encoding="utf-8"))
    trace = json.loads(FILES["trace"].read_text(encoding="utf-8"))
    completion = json.loads(FILES["completion"].read_text(encoding="utf-8"))
    backlog = FILES["backlog"].read_text(encoding="utf-8")

    checks = [
        (matrix.get("workItemId") == "IA-D05-005", "work item identity"),
        (len(matrix.get("coveredFeatures", [])) == 4, "covered feature count"),
        (len(matrix.get("equivalentViews", [])) == 6, "equivalent view count"),
        (len(matrix.get("fixtures", [])) == 24, "fixture count"),
        (len(matrix.get("implementationSlices", [])) == 8, "slice count"),
        (matrix.get("blockingAcceptanceCriteria") == 28, "acceptance count"),
        (matrix.get("blockingFindings") == 0, "blocking findings"),
        (len(trace.get("resolvedFindings", [])) == 7, "resolved findings"),
        (trace.get("blockingFindings") == [], "trace blockers"),
        (completion.get("nextWorkItemId") == "IA-D05-006", "next item"),
        (completion.get("parallelWorkPreserved") == "P9-06-008-attempt-002", "parallel preservation"),
        ("No semantic fact exists only in graph geometry" in contract, "semantic geometry principle"),
        ("filter" in contract.lower() and "topology" in contract.lower(), "hidden topology protection"),
        ("IA-D05-005 — graph/list accessibility matrix — complete" in backlog, "backlog completion"),
        ("IA-D05-006 — noncombat integration review — next" in backlog, "backlog next"),
    ]
    errors.extend(label for passed, label in checks if not passed)

if errors:
    print("IA-D05-005 GRAPH/LIST ACCESSIBILITY VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("IA-D05-005 GRAPH/LIST ACCESSIBILITY VALIDATION: PASS")
print("Covered features: 4")
print("Equivalent views: 6")
print("Fixtures: 24")
print("Acceptance criteria: 28")
print("Blocking findings: 0")
