#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
registry_path = ROOT / "governance/phase9/PHASE_9_SOURCE_PACKAGE_REGISTRY.json"
standard_path = ROOT / "governance/phase9/PHASE_9_RECONCILIATION_AND_NAMING_STANDARD.md"
registry = json.loads(registry_path.read_text())
standard = standard_path.read_text()

assert registry["sourcePackage"]["archiveSha256"] == "5535acb24c804161b7484b77682dc3cb14231236f912e10931f6ba0dab870d37"
assert registry["sourcePackage"]["structuredPackageSha256"] == "6554b8f524e4b295e52c835058a66256fa9dbd0319d138719e2146faacc9af88"
assert registry["sourcePackage"]["structuredPackageFileCount"] == 135
assert {c["id"] for c in registry["components"]} == {"P9-01", "P9-01-SPONSORED-MONTH", "P9-02"}
assert registry["handoff"]["state"] == "READY_FOR_P9-03_TECHNOLOGY_AND_SERVICE_DECISION_PACKAGE"
assert registry["handoff"]["technologyComparisonAllowed"] is True
for forbidden in ["architectureSelectionAllowed", "vendorCommitmentAllowed", "spendingAllowed", "implementationAllowed"]:
    assert registry["handoff"][forbidden] is False
assert registry["nonDuplication"]["recreateP901"] is False
assert registry["nonDuplication"]["recreateP902"] is False
for required in ["Phase 9R", "P9-03", "Do not recreate P9-01 or P9-02", "$4.99/month"]:
    assert required in standard

payload = {
    "format": "multiversal-phase9-reconciliation-validation",
    "version": "0.1.0",
    "status": "PASS",
    "registeredComponents": len(registry["components"]),
    "structuredPackageFileCount": registry["sourcePackage"]["structuredPackageFileCount"],
    "canonicalContinuation": "P9-03",
    "roadmapAlias": registry["nonDuplication"]["roadmapAlias"],
    "duplicateRecreationAllowed": False,
    "implementationAuthorized": False
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["artifactSha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "out/phase9-reconciliation"
out.mkdir(parents=True, exist_ok=True)
(out / "PHASE_9_RECONCILIATION_VALIDATION.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps(payload, sort_keys=True))
