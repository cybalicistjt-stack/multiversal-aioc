#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
package_path = ROOT / "governance/phase9/P9-05_BOUNDED_TECHNICAL_SPIKE_AND_COST_ENVELOPE.json"
notes_path = ROOT / "governance/phase9/P9-05_SPIKE_EXECUTION_AND_COST_GUARDRAILS.md"
package = json.loads(package_path.read_text())
notes = notes_path.read_text()

assert package["status"] == "complete-validated-no-live-service"
assert package["scope"] == {
    "localAndEphemeralOnly": True,
    "paidServicesAllowed": False,
    "productionInfrastructureAllowed": False,
    "vendorCredentialsAllowed": False,
    "applicationImplementationAllowed": False,
}
spike = package["spike"]
assert spike["devices"] == 2
assert spike["deterministicRuns"] >= 36
assert spike["expectedFailuresInjected"] == spike["expectedFailuresDetected"]
assert spike["unexpectedFailures"] == 0
assert spike["sourceTruthChanged"] is False
assert spike["residue"] == 0
assert len(spike["scenarios"]) >= 9
capacity = package["capacityEnvelope"]["internalAlpha"]
for key in ["concurrentSessions", "concurrentUsers", "monthlyActiveUsers", "commandsPerSessionHour", "realtimeEventsPerSessionHour", "checkpointIntervalSeconds", "checkpointRetentionDays", "databaseStorageGiB", "objectStorageGiB", "monthlyEgressGiB"]:
    assert capacity[key] > 0
cost = package["costEnvelopeUsdPerMonth"]
assert cost["floor"] == 0
assert 0 < cost["targetMaximum"] < cost["hardOwnerReviewThreshold"]
assert package["exitEvidence"]["restoreToCleanLocalPostgres"] == "pass"
assert package["result"]["architectureFeasibleForBoundedAlpha"] is True
assert package["result"]["liveVendorSelectionRequiredNow"] is False
assert package["result"]["spendingRequiredNow"] is False
for required in ["36 deterministic", "Eight intentional failures", "USD 0–25", "P9-06"]:
    assert required in notes

payload = {
    "format": "multiversal-p9-05-validation",
    "version": "0.1.0",
    "status": "PASS",
    "deterministicRuns": spike["deterministicRuns"],
    "failureInjectionsDetected": spike["expectedFailuresDetected"],
    "unexpectedFailures": spike["unexpectedFailures"],
    "residue": spike["residue"],
    "targetMonthlyMaximumUsd": cost["targetMaximum"],
    "ownerReviewThresholdUsd": cost["hardOwnerReviewThreshold"],
    "liveServiceCreated": False,
    "spendingAuthorized": False,
    "nextStep": "P9-06"
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["artifactSha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "out/p9-05"
out.mkdir(parents=True, exist_ok=True)
(out / "P9-05_VALIDATION.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps(payload, sort_keys=True))
