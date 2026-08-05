#!/usr/bin/env python3
import hashlib
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'governance/balance/8D-007_GOLDEN_CORPUS_MANIFEST.json').read_text())
thresholds = json.loads((ROOT / 'governance/balance/8D-007_PEER_GROUP_TARGET_BAND_CONTRACT.json').read_text())
limits = thresholds['regressionThresholds']

baseline = {
    'fixtureFingerprintChanges': 0,
    'scenarioExecutionFailures': 0,
    'sourceTruthChanges': 0,
    'residueCount': 0,
    'blockingObservations': 0,
    'materialObservationRate': 0.0,
    'domainCoverage': len({f['domain'] for f in manifest['fixtures']}),
}

def detect(candidate):
    failures = []
    if candidate['fixtureFingerprintChanges'] > limits['fixtureFingerprintChanges']:
        failures.append('fingerprint-drift')
    if candidate['scenarioExecutionFailures'] > limits['scenarioExecutionFailures']:
        failures.append('scenario-failure')
    if candidate['sourceTruthChanges'] > limits['sourceTruthChanges']:
        failures.append('source-truth-change')
    if candidate['residueCount'] > limits['residueCount']:
        failures.append('residue')
    if candidate['blockingObservations'] > limits['blockingObservations']:
        failures.append('blocking-observation')
    if candidate['materialObservationRate'] > limits['materialObservationRateMaximum']:
        failures.append('material-observation-rate')
    if candidate['domainCoverage'] < limits['domainCoverageMinimum']:
        failures.append('domain-coverage')
    return failures

mutations = {
    'fingerprint-drift': {'fixtureFingerprintChanges': 1},
    'scenario-failure': {'scenarioExecutionFailures': 1},
    'source-truth-change': {'sourceTruthChanges': 1},
    'residue': {'residueCount': 1},
    'blocking-observation': {'blockingObservations': 1},
    'material-observation-rate': {'materialObservationRate': limits['materialObservationRateMaximum'] + 0.01},
    'domain-coverage': {'domainCoverage': limits['domainCoverageMinimum'] - 1},
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
