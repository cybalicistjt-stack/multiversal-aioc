import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_SOURCE_DOCUMENT_VERIFICATION_PLAN_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
summary = json.loads((out_dir / 'SUMMARY.json').read_text())
queue = out_dir / 'VERIFICATION_QUEUE.jsonl'

assert summary['workstream'] == '8E-009L30'
assert len(summary['datasets']) == contract['expectedDatasets'] == 20
assert summary['totalRows'] == contract['expectedRows'] == 19199
assert sum(summary['priorityRows'].values()) == summary['totalRows']
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0
assert queue.exists()
lines = queue.read_text().splitlines()
assert len(lines) == summary['totalRows']
for line in lines:
    record = json.loads(line)
    assert record['priority'] in contract['priorityOrder']
    assert record['sourceVerificationState'] == 'unverified'
    assert record['canonicalId'] is None
    assert record['promotionReady'] is False
print(json.dumps(summary, sort_keys=True))
