from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKETS = ROOT / "feature-packets"

REQUIRED = [
    "MV-IA-F011_INVESTIGATION_AND_CLUE_BOARD.md",
    "MV-IA-F011_INVESTIGATION_CLUE_MATRIX.json",
    "MV-IA-F011_IMPLEMENTATION_TRACEABILITY.json",
    "MV-IA-F011_SOURCE_COVERAGE_AND_PROVENANCE.json",
    "MV-IA-F011_READINESS_RECORD.md",
    "MV-IA-F011_REVIEW_RECEIPT.md",
    "MV-IA-F011_COMPLETION_RECORD.json",
]


def fail(message: str) -> None:
    raise SystemExit(message)


for name in REQUIRED:
    path = PACKETS / name
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        fail(f"missing or empty required artifact: {name}")

matrix = json.loads((PACKETS / REQUIRED[1]).read_text(encoding="utf-8"))
trace = json.loads((PACKETS / REQUIRED[2]).read_text(encoding="utf-8"))
coverage = json.loads((PACKETS / REQUIRED[3]).read_text(encoding="utf-8"))
completion = json.loads((PACKETS / REQUIRED[6]).read_text(encoding="utf-8"))
packet = (PACKETS / REQUIRED[0]).read_text(encoding="utf-8")

if matrix.get("workItemId") != "IA-D05-004" or matrix.get("featureId") != "MV-IA-F011":
    fail("matrix identity mismatch")
if len(matrix.get("records", [])) != 10:
    fail("expected 10 core record types")
if len(matrix.get("connectionTypes", [])) != 15:
    fail("expected 15 connection types")
if len(matrix.get("fixtures", [])) != 24:
    fail("expected 24 deterministic fixtures")
if len(matrix.get("implementationSlices", [])) != 8:
    fail("expected 8 implementation slices")
if matrix.get("blockingAcceptanceCriteria") != 28 or matrix.get("blockingFindings") != 0:
    fail("acceptance or blocking-finding count mismatch")
if len(trace.get("resolvedFindings", [])) != 7 or trace.get("blockingFindings") != []:
    fail("traceability findings mismatch")
if not coverage.get("coverageClaims", {}).get("gmTruthProtectionCovered"):
    fail("GM truth protection coverage missing")
if completion.get("nextWorkItemId") != "IA-D05-005":
    fail("next work item mismatch")
if completion.get("parallelWorkPreserved") != "P9-06-008-attempt-002":
    fail("parallel work preservation missing")

required_phrases = [
    "Hypotheses never become facts",
    "Spatial placement is presentation state",
    "Silent last-write-wins is prohibited",
    "P9-06-008-attempt-002",
]
for phrase in required_phrases:
    if phrase not in packet:
        fail(f"required design principle missing: {phrase}")

print("IA-D05-004 investigation and clue board validation passed")
