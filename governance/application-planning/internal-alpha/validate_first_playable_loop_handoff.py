from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
P = ROOT / "feature-packets"
def load(name: str): return json.loads((P / name).read_text(encoding="utf-8"))
queue = load("IA-D04-005_IMPLEMENTATION_QUEUE.json")
trace = load("IA-D04-005_IMPLEMENTATION_TRACEABILITY.json")
completion = load("IA-D04-005_COMPLETION_RECORD.json")
handoff = (P / "IA-D04-005_FIRST_PLAYABLE_LOOP_IMPLEMENTATION_HANDOFF.md").read_text(encoding="utf-8")
assert queue["workItemId"] == "IA-D04-005"
assert queue["status"] == "implementation-ready-dependency-gated"
assert len(queue["implementationPackages"]) == 12
assert queue["acceptanceScenarioCount"] == 24
assert queue["blockingAcceptanceCriteriaCount"] == 28
assert queue["blockingFindings"] == []
assert queue["nextDesignWorkItemId"] == "IA-D05-001"
ids = [p["id"] for p in queue["implementationPackages"]]
assert len(ids) == len(set(ids))
known = set(ids)
for package in queue["implementationPackages"]:
    assert set(package["dependsOn"]) <= known
    assert package["id"] not in package["dependsOn"]
assert len(trace["packageIds"]) == 12
assert trace["unresolvedGaps"] == []
assert completion["result"] == {"implementationPackages": 12, "acceptanceScenarios": 24, "blockingAcceptanceCriteria": 28, "blockingFindings": 0}
for token in ["P9-06-008-attempt-002", "ActionResultCommitted", "status lookup before retry", "Silent last-write-wins is prohibited", "IA-D05-001"]: assert token in handoff
print("IA-D04-005 validated: 12 packages, 24 scenarios, 28 blocking criteria, 0 blocking findings.")
