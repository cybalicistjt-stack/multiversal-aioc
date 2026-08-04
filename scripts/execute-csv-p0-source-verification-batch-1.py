import csv
import json
import re
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_P0_SOURCE_VERIFICATION_BATCH_1_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
out_dir.mkdir(parents=True, exist_ok=True)
archive = ROOT / 'Csv.zip'

SOURCE_COLUMNS = {'source_pdf', 'source pdf', 'source_document', 'source document', 'source', 'source_file', 'source file'}
PARENT_COLUMNS = {'parent_id', 'parent_record_id', 'vehicle_id', 'frame_id', 'compatible_frame', 'compatible_vehicle'}
ROUTING = {
    'material': ('items', 'item.material.crafting-resource'),
    'homestead': ('homestead', 'homestead'),
    'base': ('base', 'base'),
    'facility': ('facility', 'facility')
}

def norm(value):
    return re.sub(r'[^a-z0-9]+', '', (value or '').lower())

available_docs = {}
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.pdf', '.docx', '.txt', '.md'}:
        available_docs.setdefault(norm(path.stem), []).append(str(path.relative_to(ROOT)))

summary = {
    'format': 'multiversal-csv-p0-source-verification-batch-report',
    'workstream': contract['workstream'],
    'datasets': [],
    'totalRows': 0,
    'sourceClaims': Counter(),
    'sourceAccess': Counter(),
    'relationshipEvidence': Counter(),
    'routingEvidence': Counter(),
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0
}
queue_path = out_dir / 'P0_VERIFICATION_QUEUE.jsonl'
ready_path = out_dir / 'PAGE_VERIFICATION_READY.jsonl'
with zipfile.ZipFile(archive) as zf, queue_path.open('w', encoding='utf-8') as blocked, ready_path.open('w', encoding='utf-8') as ready:
    members = {Path(n).name: n for n in zf.namelist() if not n.endswith('/')}
    for spec in contract['datasets']:
        filename = spec['file']
        member = members.get(filename)
        if not member:
            raise SystemExit(f'missing {filename}')
        counts = Counter()
        with zf.open(member) as raw:
            reader = csv.DictReader(line.decode('utf-8-sig') for line in raw)
            fields = reader.fieldnames or []
            source_fields = [f for f in fields if f.strip().lower() in SOURCE_COLUMNS]
            parent_fields = [f for f in fields if f.strip().lower() in PARENT_COLUMNS]
            for row_number, row in enumerate(reader, start=2):
                summary['totalRows'] += 1
                counts['rows'] += 1
                claims = sorted({(row.get(f) or '').strip() for f in source_fields if (row.get(f) or '').strip()})
                summary['sourceClaims']['present' if claims else 'missing'] += 1
                matches = sorted({p for claim in claims for p in available_docs.get(norm(Path(claim).stem), [])})
                access_state = 'available' if matches else ('claim-present-document-unavailable' if claims else 'claim-missing')
                summary['sourceAccess'][access_state] += 1

                evidence = {}
                if spec['blocker'] == 'vehicle-component-parent-link':
                    explicit = [{'column': f, 'value': (row.get(f) or '').strip()} for f in parent_fields if (row.get(f) or '').strip()]
                    evidence = {'type': 'relationship', 'explicitParentReferences': explicit}
                    state = 'explicit-reference-present' if explicit else 'source-document-required'
                    summary['relationshipEvidence'][state] += 1
                else:
                    source_value = (row.get('Record Type') or '').strip()
                    mapped = ROUTING.get(source_value.lower())
                    evidence = {'type': 'routing', 'recordTypeSource': source_value or None, 'exactControlledRoute': {'domain': mapped[0], 'template': mapped[1]} if mapped else None}
                    state = 'exact-controlled-route' if mapped else 'unsupported-or-blank-record-type'
                    summary['routingEvidence'][state] += 1

                record = {
                    'dataset': filename,
                    'rowNumber': row_number,
                    'blocker': spec['blocker'],
                    'sourceDocumentClaims': claims,
                    'availableSourcePaths': matches,
                    'sourceAccessState': access_state,
                    'evidence': evidence,
                    'pageVerificationState': 'ready' if matches else 'blocked-source-document-unavailable',
                    'canonicalId': None,
                    'promotionReady': False
                }
                (ready if matches else blocked).write(json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n')
        if counts['rows'] != spec['rows']:
            raise SystemExit(f'{filename}: {counts["rows"]} != {spec["rows"]}')
        summary['datasets'].append({'file': filename, 'rows': counts['rows'], 'blocker': spec['blocker'], 'sourceColumns': source_fields, 'parentColumns': parent_fields})

if summary['totalRows'] != contract['expectedRows']:
    raise SystemExit(f'total rows {summary["totalRows"]} != {contract["expectedRows"]}')
for key in ('sourceClaims', 'sourceAccess', 'relationshipEvidence', 'routingEvidence'):
    summary[key] = dict(summary[key])
(out_dir / 'SUMMARY.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary, sort_keys=True))
