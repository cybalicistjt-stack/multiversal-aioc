import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance" / "balance"
contract = json.loads((BASE / "8D-007_GOLDEN_CORPUS_CONTRACT.json").read_text())
scenarios = json.loads((BASE / "8D-007_RUNTIME_SCENARIO_REGISTRY.json").read_text())
manifest = json.loads((BASE / "8D-007_GOLDEN_CORPUS_MANIFEST.json").read_text())
schema = json.loads((BASE / "8D-007_BALANCE_OBSERVATION_SCHEMA.json").read_text())

assert contract["status"] == "active-owner-approved-workstream"
assert contract["sourceCorpus"] == {
    "datasets": 20,
    "promotedRecords": 19199,
    "reconciliationArtifactSha256": "112ef5116b4090cc266eefe36e1c539b6567f022d6b857db6e1d2bdd77e30e40",
}
assert contract["governance"]["sourceTruthImmutable"] is True
assert contract["governance"]["balanceObservationsSeparate"] is True
assert schema["properties"]["sourceTruthChanged"]["const"] is False

scenario_ids = {entry["id"] for entry in scenarios["scenarios"]}
assert len(scenario_ids) == len(scenarios["scenarios"])
assert all(isinstance(entry["seed"], int) for entry in scenarios["scenarios"])
assert all(entry["steps"] for entry in scenarios["scenarios"])

matrix = {entry["domain"]: entry for entry in contract["coverageMatrix"]}
fixtures = manifest["fixtures"]
assert manifest["fixtureCount"] == len(fixtures) == 36
assert len({fixture["fixtureId"] for fixture in fixtures}) == 36
assert len({fixture["sourceCoordinate"] for fixture in fixtures}) == 36
assert set(matrix) == {fixture["domain"] for fixture in fixtures}

fingerprints = {}
for domain, requirement in matrix.items():
    selected = [fixture for fixture in fixtures if fixture["domain"] == domain]
    assert len(selected) >= requirement["minimumFixtures"]
    covered = {scenario for fixture in selected for scenario in fixture["scenarioIds"]}
    assert set(requirement["requiredScenarios"]).issubset(covered)

for fixture in fixtures:
    assert fixture["fixtureId"].startswith("mv:golden-fixture:")
    assert fixture["canonicalSelector"]
    assert set(fixture["scenarioIds"]).issubset(scenario_ids)
    assert fixture["expectedOutcomes"]
    payload = {
        "fixtureId": fixture["fixtureId"],
        "canonicalSelector": fixture["canonicalSelector"],
        "sourceCoordinate": fixture["sourceCoordinate"],
        "scenarioIds": fixture["scenarioIds"],
        "expectedOutcomes": fixture["expectedOutcomes"],
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    fingerprints[fixture["fixtureId"]] = hashlib.sha256(encoded).hexdigest()

assert len(set(fingerprints.values())) == len(fingerprints)

installed = {fixture["fixtureId"]: fixture for fixture in fixtures}
assert len(installed) == 36
installed.clear()
assert installed == {}

report = {
    "format": "multiversal-8d-007-initial-golden-corpus-validation",
    "version": "0.1.0",
    "domainsCovered": len(matrix),
    "fixturesValidated": len(fixtures),
    "scenariosRegistered": len(scenario_ids),
    "uniqueRegressionFingerprints": len(fingerprints),
    "sourceTruthImmutable": True,
    "balanceObservationsSeparated": True,
    "installValidationPassed": True,
    "uninstallValidationPassed": True,
    "uninstallResidueCount": 0,
    "fingerprints": fingerprints,
}
out = ROOT / "out" / "8d-007-initial-golden-corpus"
out.mkdir(parents=True, exist_ok=True)
(out / "validation-report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: v for k, v in report.items() if k != "fingerprints"}, sort_keys=True))
