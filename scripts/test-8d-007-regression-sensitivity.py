#!/usr/bin/env python3
import hashlib
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'governance/balance/8D-007_GOLDEN_CORPUS_MANIFEST.json').read_text())
thresholds = json.loads((ROOT / 'governance/balance/8D-007_PEER_TARGET_THRESHOLD_REGISTRY.json').read_text())

baseline = {
    'fixtureCount': len(manifest['fixtures']),
    'scenarioFailureCount': 0,
    'sourceTruthChangeCount': 0,
    'residueCount': 0,
    'blockingObservationCount': 0,
    'materialObservationRate': 0.0,
    'domainCoverageCount': len({f['domain'] for f in manifest['fixtures']}),
    'fingerprintChanged': False,
}

def detect(candidate):
    failures = []
    limits = thresholds['regressionThresholds']
    if candidate['scenarioFailureCount'] > limits['maxScenarioFailures']:
        failures.append('scenario-failure')
    if candidate['sourceTruthChangeCount'] > limits['maxSourceTruthChanges']:
        failures.append('source-truth-change')
    if candidate['residueCount'] > limits['maxResidueCount']:
        failures.append('residue')
    if candidate['blockingObservationCount'] > limits['maxBlockingObservations']:
        failures.append('blocking-observation')
    if candidate['materialObservationRate'] > limits['maxMaterialObservationRate']:
        failures.append('material-observation-rate')
    if candidate['domainCoverageCount'] < limits['minimumDomainCoverage']:
        failures.append('domain-coverage')
    if candidate['fingerprintChanged'] and limits['fingerprintPolicy'] == 'exact-match':
        failures.append('fingerprint-drift')
    return failures

mutations = {
    'scenario-failure': {'scenarioFailureCount': 1},
    'source-truth-change': {'sourceTruthChangeCount': 1},
    'residue': {'residueCount': 1},
    'blocking-observation': {'blockingObservationCount': 1},
    'material-observation-rate': {'materialObservationRate': 1.0},
    'domain-coverage': {'domainCoverageCount': baseline['domainCoverageCount'] - 1},
    'fingerprint-drift': {'fingerprintChanged': True},
}

results = []
for expected, patch in mutations.items():
    candidate = deepcopy(baseline)
    candidate.update(patch)
    detected = detect(candidate)
    assert expected in detected, (expected, detected)
    results.append({'mutation': expected, 'detected': True, 'detectors': detected})

assert detect(baseline) == []
payload = {
    'format': 'multiversal-8d-007-regression-sensitivity',
    'version': '0.1.0',
    'baselinePasses': True,
    'mutationCount': len(results),
    'detectedMutationCount': sum(1 for r in results if r['detected']),
    'allIntentionalFailuresDetected': all(r['detected'] for r in results),
    'sourceTruthChanged': False,
    'results': results,
}
canonical = json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()
payload['artifactSha256'] = hashlib.sha256(canonical).hexdigest()
out = ROOT / 'out/8d-007-regression-sensitivity'
out.mkdir(parents=True, exist_ok=True)
(out / 'REGRESSION_SENSITIVITY_REPORT.json').write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')
print(json.dumps({k: payload[k] for k in ['mutationCount', 'detectedMutationCount', 'allIntentionalFailuresDetected', 'artifactSha256']}))
