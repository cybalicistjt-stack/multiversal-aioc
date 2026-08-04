import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_ITEM_DOMAIN_BATCH_1_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
summary = json.loads((out_dir / 'SUMMARY.json').read_text())
assert summary['totalRows'] == contract['expectedRows'] == 568
assert len(summary['datasets']) == len(contract['datasets']) == 2
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0
seen = set()
count = 0
allowed = {'item.weapon.firearm', 'item.ammunition', 'item.magic.implement', 'item.device.computer'}
for spec in contract['datasets']:
    path = out_dir / f"{Path(spec['file']).stem}.jsonl"
    rows = 0
    for line in path.read_text(encoding='utf-8').splitlines():
        record = json.loads(line)
        rows += 1
        count += 1
        sid = record['stagingId']
        assert sid not in seen
        seen.add(sid)
        assert record['dataset'] == spec['file']
        assert record['domain'] == 'items'
        assert record['templateRouting'] in allowed
        assert record['routingEvidence'] == 'inferred-classification'
        assert record['identity']['canonicalId'] is None
        assert record['promotionReady'] is False
        assert record['rawSource']
        assert record['unresolvedManifest']
    assert rows == spec['rows']
assert count == 568
print('CSV item-domain batch 1 validated: 568 rows across 2 datasets; 0 canonical IDs.')
