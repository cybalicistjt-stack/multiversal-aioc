import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_VEHICLE_DOMAIN_BATCH_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
summary = json.loads((out_dir / 'SUMMARY.json').read_text())

assert summary['workstream'] == contract['workstream']
assert summary['totalRows'] == contract['expectedRows'] == 5628
assert len(summary['datasets']) == len(contract['datasets']) == 3
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0

expected = {d['file']: d['rows'] for d in contract['datasets']}
seen_ids = set()
validated = 0
for dataset in summary['datasets']:
    assert dataset['file'] in expected
    assert dataset['rows'] == expected[dataset['file']]
    path = ROOT / dataset['output']
    assert path.exists()
    count = 0
    with path.open(encoding='utf-8') as handle:
        for line in handle:
            record = json.loads(line)
            count += 1
            validated += 1
            assert record['dataset'] == dataset['file']
            assert record['domain'] == 'vehicles'
            assert record['routingEvidence'] == 'inferred-classification'
            assert record['recordRouting'].startswith(('vehicle.', 'vehicle-component.'))
            assert record['identity']['canonicalId'] is None
            assert record['rawSource']
            assert record['unmappedColumns']
            assert record['unresolvedManifest']
            assert 'component-parent-reconciliation' in record['unresolvedManifest']
            assert record['promotionReady'] is False
            assert record['stagingId'] not in seen_ids
            seen_ids.add(record['stagingId'])
    assert count == expected[dataset['file']]

assert validated == 5628
print('Vehicle-domain staging validated: 5628 rows across 3 datasets; 0 canonical IDs; 0 promotion-ready rows.')
