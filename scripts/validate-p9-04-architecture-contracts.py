#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = (ROOT / "governance/phase9/P9-04_POSTGRES_CENTERED_ARCHITECTURE_CONTRACT.md").read_text()
registry = json.loads((ROOT / "governance/phase9/P9-04_IMPLEMENTATION_READINESS_REGISTRY.json").read_text())

assert registry["selectedArchitectureClass"] == "Postgres-centered managed backend"
assert len(registry["contracts"]) == 14
assert len(registry["servicePorts"]) == 8
assert len(registry["requiredTables"]) >= 17
assert all(registry["invariants"].values())
allowed = registry["authorization"]
assert allowed["architecturePlanningAllowed"] is True
assert allowed["contractAndTestAuthoringAllowed"] is True
for key in [
    "vendorAccountCreationAllowed", "paidPlanAllowed", "credentialProvisioningAllowed",
    "liveSchemaApplicationAllowed", "productionDeploymentAllowed", "applicationImplementationAllowed"
]:
    assert allowed[key] is False

for phrase in [
    "server is authoritative", "Provider-neutral service boundaries", "Entitlements are derived",
    "Commands are idempotent", "Hidden data is excluded before publication",
    "expand–migrate–contract", "Backup and restore", "Provider exit",
    "does not authorize vendor account creation"
]:
    assert phrase in contract, phrase

payload = {
    "format": "multiversal-p9-04-architecture-contract-validation",
    "version": "0.1.0",
    "status": "PASS",
    "contractCount": len(registry["contracts"]),
    "servicePortCount": len(registry["servicePorts"]),
    "requiredTableCount": len(registry["requiredTables"]),
    "invariantCount": len(registry["invariants"]),
    "implementationAuthorized": False,
    "nextHandoff": registry["nextHandoff"]
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["artifactSha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "out/p9-04-architecture-contracts"
out.mkdir(parents=True, exist_ok=True)
(out / "P9-04_ARCHITECTURE_CONTRACT_VALIDATION.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps(payload, sort_keys=True))
