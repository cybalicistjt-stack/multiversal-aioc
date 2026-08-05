#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "governance/phase9/P9-06_IMPLEMENTATION_BACKLOG_AND_ACCEPTANCE_GATES.json"
data = json.loads(path.read_text())

assert data["status"] == "complete-ready-for-owner-gated-implementation"
assert len(data["workstreams"]) == 7
assert len(data["backlog"]) == 24
assert len(data["acceptanceGates"]) == 8
assert data["scope"]["implementationAllowed"] is False
assert data["scope"]["paidServiceAllowed"] is False
assert data["scope"]["productionDeploymentAllowed"] is False
assert data["nextHandoff"] == "P9-06A_OWNER_IMPLEMENTATION_AUTHORIZATION_GATE"

ids = [x["id"] for x in data["backlog"]]
assert len(ids) == len(set(ids))
assert sorted(x["priority"] for x in data["backlog"]) == list(range(1, 25))
known = set(ids)
for item in data["backlog"]:
    assert set(item["dependencies"]).issubset(known)
    assert all(ids.index(dep) < ids.index(item["id"]) for dep in item["dependencies"])

payload = {
    "format": "multiversal-p9-06-validation",
    "version": "0.1.0",
    "status": "PASS",
    "workstreamCount": len(data["workstreams"]),
    "backlogItemCount": len(data["backlog"]),
    "acceptanceGateCount": len(data["acceptanceGates"]),
    "implementationAuthorized": data["scope"]["implementationAllowed"],
    "paidServiceAuthorized": data["scope"]["paidServiceAllowed"],
    "productionDeploymentAuthorized": data["scope"]["productionDeploymentAllowed"],
    "nextHandoff": data["nextHandoff"]
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["artifactSha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "out/p9-06"
out.mkdir(parents=True, exist_ok=True)
(out / "P9-06_VALIDATION.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps(payload, sort_keys=True))
