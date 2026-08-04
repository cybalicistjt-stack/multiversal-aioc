import csv
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/P0_ROW_PAGE_MATCH_BATCH_1_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
out_dir.mkdir(parents=True, exist_ok=True)
archive = ROOT / 'Csv.zip'

with zipfile.ZipFile(archive) as zf:
    members = {Path(name).name: name for name in zf.namelist() if not name.endswith('/')}
    member = members.get(contract['dataset'])
    if not member:
        raise SystemExit(f"missing {contract['dataset']}")
    with zf.open(member) as raw:
        reader = csv.DictReader(line.decode('utf-8-sig') for line in raw)
        source_field = next((f for f in (reader.fieldnames or []) if f.strip().lower() in {'source_pdf', 'source pdf'}), None)
        if not source_field:
            raise SystemExit('source field not found')
        records = []
        for row_number, row in enumerate(reader, start=2):
            claim = (row.get(source_field) or '').strip()
            if claim != contract['exactSourceClaim']:
                continue
            records.append({
                'dataset': contract['dataset'],
                'rowNumber': row_number,
                'sourceClaim': claim,
                'governedSourcePath': contract['governedSourcePath'],
                'documentScopeVerified': True,
                'pageCitation': None,
                'candidatePageRange': [1, contract['sourcePageCount']],
                'matchState': 'quarantined-ambiguous-no-row-specific-locator',
                'canonicalId': None,
                'promotionReady': False
            })

if len(records) != contract['expectedRows']:
    raise SystemExit(f"matched rows {len(records)} != {contract['expectedRows']}")

with (out_dir / 'ROW_PAGE_MATCH_RESULTS.jsonl').open('w', encoding='utf-8') as f:
    for record in records:
        f.write(json.dumps(record, sort_keys=True) + '\n')
summary = {
    'format': 'multiversal-p0-row-page-match-batch-summary',
    'workstream': contract['workstream'],
    'rowsAttempted': len(records),
    'uniquePageCitationsAssigned': 0,
    'ambiguousRowsQuarantined': len(records),
    'visualUnreadableRowsQuarantined': 0,
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0
}
(out_dir / 'SUMMARY.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary, sort_keys=True))
