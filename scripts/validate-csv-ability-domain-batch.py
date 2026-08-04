import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_ABILITY_DOMAIN_BATCH_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
summary = json.loads((out_dir / 'SUMMARY.json').read_text())

assert summary['workstream'] == contract['workstream']
assert summary['totalRows'] == contract['expectedRows']
assert len(summary['datasets']) == len(contract['datasets'])
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0

seen = set()
rows = 0
for spec in contract['datasets']:
    path = out_dir / f"{Path(spec['file']).stem}.jsonl"
    count = 0
    with path.open(encoding='utf-8') as handle:
        for line in handle:
            record = json.loads(line)
            count += 1
            rows += 1
            assert record['dataset'] == spec['file']
            assert record['domain'] == 'abilities'
            assert record['recordRouting'] in {'ability.tree', 'ability.definition'}
            assert record['routingEvidence'] == 'inferred-classification'
            assert record['identity']['canonicalId'] is None
            assert record['relationships']['resolvedTreeCanonicalId'] is None
            assert record['promotionReady'] is False
            assert record['validationState'] == 'domain-staged-unverified'
            assert record['rawSource']
            assert 'tree-and-parent-relationship-reconciliation' in record['unresolvedManifest']
            assert record['stagingId'] not in seen
            seen.add(record['stagingId'])
    assert count == spec['rows'], (spec['file'], count, spec['rows'])
assert rows == contract['expectedRows']
print(json.dumps({'datasetsValidated': len(contract['datasets']), 'rowsValidated': rows, 'uniqueStagingIds': len(seen), 'canonicalIdsAssigned': 0, 'promotionReadyRows': 0}, sort_keys=True))
