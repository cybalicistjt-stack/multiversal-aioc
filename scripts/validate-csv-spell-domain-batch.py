import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_SPELL_DOMAIN_BATCH_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
summary = json.loads((out_dir / 'SUMMARY.json').read_text())
assert summary['totalRows'] == contract['expectedRows'] == 385
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0
seen = set()
count = 0
for spec in contract['datasets']:
    path = out_dir / f"{Path(spec['file']).stem}.jsonl"
    assert path.exists()
    rows = 0
    for line in path.read_text(encoding='utf-8').splitlines():
        record = json.loads(line)
        rows += 1
        count += 1
        sid = record['stagingId']
        assert sid not in seen
        seen.add(sid)
        assert record['domain'] == 'spells'
        assert record['templateRouting'] == 'spell-system'
        assert record['identity']['canonicalId'] is None
        assert record['promotionReady'] is False
        assert record['rawSource']
        unresolved = set(record['unresolvedManifest'])
        assert 'source-document-page-verification' in unresolved
        assert 'spell-system-runtime-validation' in unresolved
    assert rows == spec['rows']
assert count == 385
print(json.dumps({'datasets':1,'rows':count,'uniqueStagingIds':len(seen),'canonicalIdsAssigned':0,'promotionReadyRows':0}, sort_keys=True))
