import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_ABILITY_RELATIONSHIP_RECONCILIATION_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
summary = json.loads((out_dir / 'SUMMARY.json').read_text())

assert summary['workstream'] == '8E-009L27'
assert summary['rows'] == contract['expectedRows'] == 4816
assert summary['treeRecords'] + summary['abilityRecords'] == summary['rows']
assert sum(summary['treeLinks'].values()) == summary['rows']
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0
assert (out_dir / 'RESOLVED_RELATIONSHIPS.jsonl').exists()
assert (out_dir / 'UNRESOLVED_RELATIONSHIPS.jsonl').exists()

for path in (out_dir / 'RESOLVED_RELATIONSHIPS.jsonl', out_dir / 'UNRESOLVED_RELATIONSHIPS.jsonl'):
    for line in path.read_text().splitlines():
        record = json.loads(line)
        assert record['canonicalId'] is None
        assert record['promotionReady'] is False
        assert record['treeResolution']['state'] in {'resolved', 'missing', 'ambiguous', 'not-applicable'}

print(json.dumps(summary, sort_keys=True))
