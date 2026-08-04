import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_P0_SOURCE_VERIFICATION_BATCH_1_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
summary = json.loads((out_dir / 'SUMMARY.json').read_text())
blocked = out_dir / 'P0_VERIFICATION_QUEUE.jsonl'
ready = out_dir / 'PAGE_VERIFICATION_READY.jsonl'

assert summary['workstream'] == '8E-009L31'
assert len(summary['datasets']) == 3
assert summary['totalRows'] == contract['expectedRows'] == 5508
assert sum(summary['sourceAccess'].values()) == summary['totalRows']
assert sum(summary['relationshipEvidence'].values()) == 4428
assert sum(summary['routingEvidence'].values()) == 1080
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0
assert blocked.exists() and ready.exists()
assert len(blocked.read_text().splitlines()) + len(ready.read_text().splitlines()) == summary['totalRows']
for path in (blocked, ready):
    for line in path.read_text().splitlines():
        record = json.loads(line)
        assert record['canonicalId'] is None
        assert record['promotionReady'] is False
        assert record['sourceAccessState'] in {'available', 'claim-present-document-unavailable', 'claim-missing'}
        if record['pageVerificationState'] == 'ready':
            assert record['availableSourcePaths']
        else:
            assert not record['availableSourcePaths']
print(json.dumps(summary, sort_keys=True))
