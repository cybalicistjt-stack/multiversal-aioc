import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
base = ROOT / 'governance/object-system/csv-intake'
contract = json.loads((base / 'P0_NARRATIVE_SOURCE_SET_CONTRACT.json').read_text())
registry = json.loads((ROOT / contract['registry']).read_text())
manifest = json.loads((base / 'LEGACY_PDF_SOURCE_PACKAGE_MANIFEST.json').read_text())
aliases = json.loads((base / 'P0_SOURCE_CLAIM_ALIAS_REGISTRY.json').read_text())

assert contract['workstream'] == registry['workstream'] == '8E-009L35'
assert registry['archiveSha256'] == aliases['archiveSha256'] == manifest['archive']['sha256']
assert len(registry['documentSets']) == contract['expectedDocumentSets'] == 3
assert sum(item['rows'] for item in registry['documentSets']) == contract['expectedNarrativeRows'] == 1602
assert registry['resolvedNarrativeClaims'] == 3
assert registry['resolvedNarrativeRows'] == 1602
assert registry['remainingNarrativeClaims'] == 0
assert registry['rowsWithGovernedSourceScope'] == 5508
assert registry['rowToPageCitationsAssigned'] == 0
assert registry['canonicalIdsAssigned'] == 0
assert registry['promotionReadyRows'] == 0

manifest_paths = set(manifest['pdfPaths'])
claims = {item['claim'] for item in registry['documentSets']}
assert claims == set(aliases['narrativeClaims'])
for item in registry['documentSets']:
    assert item['members']
    assert len(item['members']) == len(set(item['members']))
    assert all(member in manifest_paths for member in item['members'])

print(json.dumps({
    'workstream': '8E-009L35',
    'documentSets': 3,
    'narrativeRowsResolved': 1602,
    'rowsWithGovernedSourceScope': 5508,
    'rowToPageCitationsAssigned': 0,
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0
}, sort_keys=True))
