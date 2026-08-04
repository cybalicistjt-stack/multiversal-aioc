import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
contract=json.loads((ROOT/'governance/object-system/csv-intake/CSV_MIXED_HAZARD_DOMAIN_BATCH_CONTRACT.json').read_text())
out=ROOT/contract['outputDirectory']; summary=json.loads((out/'SUMMARY.json').read_text())
assert summary['totalRows']==contract['expectedRows']==2981
assert len(summary['datasets'])==2
assert summary['canonicalIdsAssigned']==0 and summary['promotionReadyRows']==0
seen=set(); rows=0
for spec in contract['datasets']:
    path=out/f'{Path(spec["file"]).stem}.jsonl'; count=0
    for line in path.read_text(encoding='utf-8').splitlines():
        record=json.loads(line); count+=1; rows+=1
        assert record['stagingId'] not in seen; seen.add(record['stagingId'])
        assert record['rawSource'] and record['unresolvedManifest']
        assert record['identity']['canonicalId'] is None
        assert record['promotionReady'] is False
        assert record['routingEvidence']=='inferred-classification'
    assert count==spec['rows']
assert rows==2981
print('CSV mixed/hazard domain batch validated: 2981 rows across 2 datasets; 0 canonical IDs.')
