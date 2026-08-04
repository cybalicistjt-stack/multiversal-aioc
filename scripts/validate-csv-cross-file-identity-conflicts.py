import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'governance/object-system/csv-intake/CSV_CROSS_FILE_IDENTITY_CONFLICT_RECONCILIATION_CONTRACT.json').read_text())
out=ROOT/c['outputDirectory']; s=json.loads((out/'SUMMARY.json').read_text())
assert s['workstream']=='8E-009L29'
assert s['datasets']==c['expectedDatasets']==20
assert s['rows']==c['expectedRows']==19199
assert s['canonicalIdsAssigned']==0 and s['promotionReadyRows']==0 and s['automaticMerges']==0
for p in (out/'REVIEW_CLUSTERS.jsonl',out/'SOURCE_ID_CONFLICTS.jsonl'):
    assert p.exists()
    for line in p.read_text().splitlines():
        r=json.loads(line)
        assert r.get('automaticMerge') is False
        if 'canonicalId' in r: assert r['canonicalId'] is None
print(json.dumps(s,sort_keys=True))
