import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
base = ROOT / 'governance/object-system/csv-intake'
contract = json.loads((base / 'P0_PAGE_LEVEL_SOURCE_INDEX_CONTRACT.json').read_text())
evidence = json.loads((ROOT / contract['evidence']).read_text())
summary = evidence['summary']

assert contract['workstream'] == summary['workstream'] == '8E-009L34'
assert contract['archiveSha256'] == summary['archiveSha256']
assert summary['documents'] == contract['expectedDocuments'] == 22
assert summary['totalPages'] == contract['expectedPages'] == 648
assert summary['extractableTextPages'] == contract['expectedExtractableTextPages'] == 635
assert summary['rowsAuthorizedForPageIndexing'] == contract['expectedRows'] == 5508
assert summary['rowsWithExactSourcePaths'] + summary['rowsWithNarrativeClaims'] == 5508
assert len(evidence['documentIndex']) == 22
assert len({x['claim'] for x in evidence['documentIndex']}) == 22
assert len({x['path'] for x in evidence['documentIndex']}) == 22
assert summary['canonicalIdsAssigned'] == evidence['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == evidence['promotionReadyRows'] == 0
print(json.dumps(summary, sort_keys=True))
