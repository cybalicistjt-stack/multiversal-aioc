from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
P = ROOT / "feature-packets"

def load(name: str):
    return json.loads((P / name).read_text(encoding="utf-8"))

matrix = load("MV-IA-F016_FACTION_REPUTATION_MATRIX.json")
coverage = load("MV-IA-F016_SOURCE_COVERAGE_AND_PROVENANCE.json")
trace = load("MV-IA-F016_IMPLEMENTATION_TRACEABILITY.json")
completion = load("MV-IA-F016_COMPLETION_RECORD.json")
packet = (P / "MV-IA-F016_FACTIONS_REPUTATION_AND_ORGANIZATIONS.md").read_text(encoding="utf-8")
assert matrix["featureId"] == "MV-IA-F016" and matrix["workItemId"] == "IA-D05-002"
assert len(matrix["contractFamilies"]) == 16
assert len(matrix["membershipStatuses"]) == 9
assert len(matrix["visibilityLayers"]) == 9
assert len(matrix["ownedCommands"]) == 14 and len(matrix["ownedEvents"]) == 14
assert len(matrix["fixtures"]) == len({x["fixtureId"] for x in matrix["fixtures"]}) == 24
assert len(matrix["implementationSlices"]) == 8 and len(matrix["acceptanceCriteria"]) == 28
assert len(matrix["deniedCases"]) >= 30 and matrix["blockingFindings"] == []
assert matrix["nextWorkItemId"] == "IA-D05-003"
assert matrix["sourceProgressionBoundary"]["canonicalRecords"] == 956
assert coverage["sources"][2]["rows"] == 153 and coverage["sources"][2]["stableFactionReferences"] == 0
assert trace["unresolvedFindings"] == [] and trace["blockingFindings"] == []
assert completion["result"]["blockingFindings"] == 0
for required in ["Membership, rank, office, reputation, influence, ownership, equipment, and permission are separate", "Do not create faction IDs", "status lookup before retry", "Mobile", "IA-D05-003", "Silence is not approval.", "implementation remains dependency-gated"]:
    assert required in packet, required
sections = [int(line.split()[1].rstrip(".")) for line in packet.splitlines() if line.startswith("## ") and line.split()[1].rstrip(".").isdigit()]
assert sections == list(range(1, 25)), sections
assert packet.startswith("# MV-IA-F016 — Factions, Reputation, and Organizations")
assert "**Feature ID:** MV-IA-F016" in packet and "**Design status:** implementation-ready" in packet and "**Owner:** John Brandon Turner" in packet
for n in range(1, 29): assert f"FRO-AC-{n:03d}" in packet
print("MV-IA-F016 VALIDATION: PASS")
print("Contracts: 16; fixtures: 24; criteria: 28; resolved findings: 6; blocking findings: 0")
