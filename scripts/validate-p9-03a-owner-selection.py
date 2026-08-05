#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
record = (root / "governance/phase9/P9-03A_OWNER_TECHNOLOGY_SELECTION_RECORD.md").read_text()

required = [
    "John Brandon Turner",
    "Candidate A — Postgres-centered managed backend",
    "APPROVED FOR ARCHITECTURE PLANNING",
    "P9-04",
    "does **not** by itself authorize",
    "paid-plan enrollment or spending",
    "production deployment",
    "server authoritative",
    "replaceable interfaces",
]
for value in required:
    assert value in record, value

payload = {
    "format": "multiversal-p9-03a-owner-selection-validation",
    "version": "0.1.0",
    "status": "PASS",
    "selectedCandidate": "A",
    "architectureClass": "Postgres-centered managed backend",
    "architecturePlanningAuthorized": True,
    "spendingAuthorized": False,
    "productionDeploymentAuthorized": False,
    "applicationImplementationAuthorized": False,
    "nextWorkItem": "P9-04",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["artifactSha256"] = hashlib.sha256(canonical).hexdigest()
out = root / "out/p9-03a-owner-selection"
out.mkdir(parents=True, exist_ok=True)
(out / "P9-03A_OWNER_SELECTION_VALIDATION.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps(payload, sort_keys=True))
