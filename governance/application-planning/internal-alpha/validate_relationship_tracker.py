from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
P = ROOT / "feature-packets"

def load(name: str):
    return json.loads((P / name).read_text(encoding="utf-8"))

matrix = load("MV-IA-F009_RELATIONSHIP_TRACKER_MATRIX.json")
coverage = load("MV-IA-F009_SOURCE_COVERAGE_AND_PROVENANCE.json")
trace = load("MV-IA-F009_IMPLEMENTATION_TRACEABILITY.json")
completion = load("MV-IA-F009_COMPLETION_RECORD.json")
packet = (P / "MV-IA-F009_RELATIONSHIP_TRACKER.md").read_text(encoding="utf-8")
assert matrix["featureId"] == "MV-IA-F009" and matrix["workItemId"] == "IA-D05-001"
assert matrix["relationshipDimensions"] == ["trust", "respect", "affection", "attraction", "loyalty", "fear", "suspicion", "hostility", "admiration", "dependence", "obligation", "rivalry", "familiarity", "ideological-alignment"]
assert len(matrix["revealLayers"]) == 7
assert len(matrix["domainCommands"]) == 12 and len(matrix["domainEvents"]) == 11
assert len(matrix["fixtures"]) == len({x["fixtureId"] for x in matrix["fixtures"]}) == 24
assert len(matrix["implementationSlices"]) == 8 and len(matrix["acceptanceCriteria"]) == 28
assert len(matrix["deniedCases"]) >= 28 and matrix["blockingFindings"] == []
assert matrix["nextWorkItemId"] == "IA-D05-002"
assert matrix["sourceCoverage"]["relationshipRegister"] == {"rows": 154, "sourceExplicitRelationshipFacts": 4, "relationshipNotProvided": 150}
assert sum(x.get("rows", 0) for x in coverage["sources"]) == 516
assert trace["unresolvedFindings"] == [] and trace["blockingFindings"] == []
assert completion["result"]["blockingFindings"] == 0
for required in ["does not use one universal attitude score", "Relationships are directional unless explicitly paired as mutual", "status lookup before retry", "Mobile provides a complete list/tree fallback", "IA-D05-002", "Silence is not approval.", "implementation remains dependency-gated"]:
    assert required in packet, required
sections=[int(line.split()[1].rstrip(".")) for line in packet.splitlines() if line.startswith("## ") and line.split()[1].rstrip(".").isdigit()]
assert sections == list(range(1,25)), sections
assert packet.startswith("# MV-IA-F009 — Relationship Tracker")
assert "**Feature ID:** MV-IA-F009" in packet and "**Design status:** implementation-ready" in packet and "**Owner:** John Brandon Turner" in packet
print("MV-IA-F009 VALIDATION: PASS")
print("Dimensions: 14; reveal layers: 7; fixtures: 24; criteria: 28; blocking findings: 0")
