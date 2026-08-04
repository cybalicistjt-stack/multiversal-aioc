import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_P0_SOURCE_PACKAGE_REQUIREMENTS_CONTRACT.json').read_text())
out = ROOT / contract['outputDirectory']
summary = json.loads((out / 'SUMMARY.json').read_text())
requirements = json.loads((out / 'REQUIRED_SOURCE_FILES.json').read_text())
aliases = json.loads((out / 'SOURCE_CLAIM_ALIASES.json').read_text())

assert summary['workstream'] == '8E-009L32'
assert summary['rowsAudited'] == contract['expectedRows'] == 5508
assert summary['exactSourceFilenames'] == len(requirements)
assert summary['narrativeOrAliasClaims'] == len(aliases)
assert summary['presentExactSourceFilenames'] + summary['missingExactSourceFilenames'] == len(requirements)
assert summary['canonicalIdsAssigned'] == 0
assert summary['promotionReadyRows'] == 0
for item in requirements:
    assert item['claimedFilename'].lower().endswith('.pdf')
    assert item['status'] in {'present', 'missing'}
    assert bool(item['repositoryMatches']) == (item['status'] == 'present')
for item in aliases:
    assert item['status'] == 'requires-claim-resolution'
if summary['missingExactSourceFilenames'] or aliases:
    assert summary['pageLevelVerificationReady'] is False
print(json.dumps(summary, sort_keys=True))
