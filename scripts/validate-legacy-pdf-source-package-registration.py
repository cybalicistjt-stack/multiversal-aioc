import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
base = ROOT / 'governance/object-system/csv-intake'
contract = json.loads((base / 'LEGACY_PDF_SOURCE_PACKAGE_CONTRACT.json').read_text())
manifest = json.loads((ROOT / contract['manifest']).read_text())
aliases = json.loads((ROOT / contract['aliases']).read_text())

assert contract['workstream'] == '8E-009L33'
assert contract['archive']['sha256'] == '60a81e247f203fa8b52eb8cd7a95d1e2039c48aacc5c29d5c7f63bef6a573183'
assert contract['archive']['sizeBytes'] == 59134328
assert manifest['archive'] == contract['archive']
assert len(manifest['pdfPaths']) == 218
assert len(set(manifest['pdfPaths'])) == 218
assert all(path.lower().endswith('.pdf') for path in manifest['pdfPaths'])
assert len(manifest['p0RequiredEntries']) == 22
assert all(entry['path'] in manifest['pdfPaths'] for entry in manifest['p0RequiredEntries'])
assert all(len(entry['sha256']) == 64 and entry['sizeBytes'] > 0 for entry in manifest['p0RequiredEntries'])
assert aliases['archiveSha256'] == contract['archive']['sha256']
assert len(aliases['aliases']) == 22
assert aliases['resolvedExactClaims'] == 22
assert aliases['unresolvedExactClaims'] == 0
assert all(path in manifest['pdfPaths'] for path in aliases['aliases'].values())
assert aliases['canonicalIdsAssigned'] == 0
assert aliases['promotionReadyRows'] == 0
print(json.dumps({'workstream':'8E-009L33','pdfs':218,'p0RequiredFiles':22,'aliasesResolved':22,'canonicalIdsAssigned':0,'promotionReadyRows':0}, sort_keys=True))
