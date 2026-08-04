import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_MIXED_DOMAIN_ROUTING_RECONCILIATION_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
summary = json.loads((out_dir / 'SUMMARY.json').read_text())

assert summary['workstream'] == '8E-009L28'
assert summary['rows'] == contract['expectedRows'] == 1080
assert summary['resolvedRows'] + summary['unresolvedRows'] == summary['rows']
assert set(summary['routes']).issubset(set(contract['rules']['allowedRoutes']))
assert sum(summary['routes'].values()) == summary['resolvedRows']
assert sum(summary['sourceValueCensus'].values()) == summary['rows']
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0

resolved = out_dir / 'RESOLVED_ROUTING.jsonl'
unresolved = out_dir / 'UNRESOLVED_ROUTING.jsonl'
assert resolved.exists() and unresolved.exists()

resolved_count = 0
for line in resolved.read_text().splitlines():
    record = json.loads(line)
    resolved_count += 1
    assert record['routingState'] == 'resolved'
    assert record['resolvedRoute'] in contract['rules']['allowedRoutes']
    assert record['routingEvidence'] == 'exact-controlled-source-value'
    assert record['canonicalId'] is None
    assert record['promotionReady'] is False

unresolved_count = 0
for line in unresolved.read_text().splitlines():
    record = json.loads(line)
    unresolved_count += 1
    assert record['routingState'] in {'blank', 'unsupported-source-value'}
    assert record['resolvedRoute'] is None
    assert record['canonicalId'] is None
    assert record['promotionReady'] is False

assert resolved_count == summary['resolvedRows']
assert unresolved_count == summary['unresolvedRows']
print(json.dumps(summary, sort_keys=True))
