from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
P = ROOT / "feature-packets"

def load(name: str):
    return json.loads((P / name).read_text(encoding="utf-8"))

matrix = load("MV-IA-F010_SOCIAL_INTERACTION_MATRIX.json")
coverage = load("MV-IA-F010_SOURCE_COVERAGE_AND_PROVENANCE.json")
trace = load("MV-IA-F010_IMPLEMENTATION_TRACEABILITY.json")
completion = load("MV-IA-F010_COMPLETION_RECORD.json")
packet = (P / "MV-IA-F010_SOCIAL_INTERACTION_MODE.md").read_text(encoding="utf-8")
assert matrix["featureId"] == "MV-IA-F010" and matrix["workItemId"] == "IA-D05-003"
assert len(matrix["interactionModes"]) == 3 and len(matrix["actionCategories"]) == 14
assert matrix["sourceActionForms"] == 49 and len(matrix["alphaActions"]) == 7
assert len(matrix["resolutionMethods"]) == 6 and len(matrix["degreeOutcomes"]) == 7
assert len(matrix["sharedEffectProcessors"]) == 18 and len(matrix["outcomeEventDraftTypes"]) == 29
assert len(matrix["fixtures"]) == len({x["fixtureId"] for x in matrix["fixtures"]}) == 24
assert len(matrix["implementationSlices"]) == 8 and len(matrix["acceptanceCriteria"]) == 28
assert len(matrix["deniedCases"]) >= 30 and matrix["blockingFindings"] == []
assert matrix["nextWorkItemId"] == "IA-D05-004"
assert coverage["sources"][3]["rows"] == 209 and coverage["sources"][3]["unmatchedLocalWrapper"] == 196
assert trace["unresolvedFindings"] == [] and trace["blockingFindings"] == []
assert completion["result"]["blockingFindings"] == 0
for required in ["Persuasion is not mind control", "full dialogue is optional", "status lookup before retry", "atomic Event group", "compensating undo", "IA-D05-004", "Silence is not approval.", "implementation remains dependency-gated"]:
    assert required in packet, required
sections=[int(line.split()[1].rstrip(".")) for line in packet.splitlines() if line.startswith("## ") and line.split()[1].rstrip(".").isdigit()]
assert sections == list(range(1,25)), sections
assert packet.startswith("# MV-IA-F010 — Social Interaction Mode")
assert "**Feature ID:** MV-IA-F010" in packet and "**Design status:** implementation-ready" in packet and "**Owner:** John Brandon Turner" in packet
for n in range(1,29): assert f"SOC-AC-{n:03d}" in packet
print("MV-IA-F010 VALIDATION: PASS")
print("Modes: 3; action forms: 49; alpha actions: 7; fixtures: 24; criteria: 28; blocking findings: 0")
