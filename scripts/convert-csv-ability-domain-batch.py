import csv
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_ABILITY_DOMAIN_BATCH_CONTRACT.json').read_text())
archive = ROOT / 'Csv.zip'
out_dir = ROOT / contract['outputDirectory']
out_dir.mkdir(parents=True, exist_ok=True)


def slug(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-') or 'unnamed'


def classify(row: dict) -> tuple[str, str]:
    record_type = (row.get('Record_Type') or '').strip().lower()
    if 'tree' in record_type:
        return 'ability.tree', 'inferred-classification'
    return 'ability.definition', 'inferred-classification'

summary = {
    'format': 'multiversal-csv-domain-batch-summary',
    'workstream': contract['workstream'],
    'datasets': [],
    'totalRows': 0,
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0,
}

with zipfile.ZipFile(archive) as zf:
    members = {Path(name).name: name for name in zf.namelist() if not name.endswith('/')}
    for spec in contract['datasets']:
        filename = spec['file']
        member = members.get(filename)
        if not member:
            raise SystemExit(f'missing {filename} in Csv.zip')
        output_path = out_dir / f'{Path(filename).stem}.jsonl'
        count = 0
        routes = {}
        with zf.open(member) as raw, output_path.open('w', encoding='utf-8') as output:
            reader = csv.DictReader(line.decode('utf-8-sig') for line in raw)
            fields = reader.fieldnames or []
            if spec['identityColumn'] not in fields:
                raise SystemExit(f'{filename} missing identity column {spec["identityColumn"]}')
            for row_number, row in enumerate(reader, start=2):
                count += 1
                identity = (row.get(spec['identityColumn']) or '').strip()
                route, evidence = classify(row)
                routes[route] = routes.get(route, 0) + 1
                tree_id = (row.get('Tree_ID') or '').strip() or None
                record = {
                    'stagingId': f'mvstg:{slug(Path(filename).stem)}:{row_number}:{slug(identity)}',
                    'dataset': filename,
                    'rowNumber': row_number,
                    'domain': 'abilities',
                    'recordRouting': route,
                    'routingEvidence': evidence,
                    'identity': {'sourceIdentity': identity or None, 'canonicalId': None},
                    'relationships': {'treeIdSource': tree_id, 'resolvedTreeCanonicalId': None},
                    'rawSource': row,
                    'unmappedColumns': fields,
                    'provenance': {'archive': 'Csv.zip', 'dataset': filename, 'rowNumber': row_number},
                    'unresolvedManifest': [
                        'source-document-page-verification',
                        'field-level-provenance',
                        'tree-and-parent-relationship-reconciliation',
                        'cross-file-identity-reconciliation',
                        'ability-domain-validation',
                        'owner-promotion-approval'
                    ],
                    'validationState': 'domain-staged-unverified',
                    'promotionReady': False
                }
                output.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n')
        if count != spec['rows']:
            raise SystemExit(f'{filename}: {count} rows != {spec["rows"]}')
        summary['datasets'].append({'file': filename, 'rows': count, 'routes': routes, 'output': str(output_path.relative_to(ROOT))})
        summary['totalRows'] += count

if summary['totalRows'] != contract['expectedRows']:
    raise SystemExit(f'total rows {summary["totalRows"]} != {contract["expectedRows"]}')
(out_dir / 'SUMMARY.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary, sort_keys=True))
