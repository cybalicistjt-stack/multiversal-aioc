import csv
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_VEHICLE_DOMAIN_BATCH_CONTRACT.json').read_text())
archive = ROOT / 'Csv.zip'
out_dir = ROOT / contract['outputDirectory']
out_dir.mkdir(parents=True, exist_ok=True)


def slug(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-') or 'unnamed'


def classify(filename: str, row: dict) -> tuple[str, str]:
    if filename == 'expanded_land_sea_air_vehicles_all_genres.csv':
        domain = (row.get('Domain') or '').strip().lower()
        vehicle_class = (row.get('Vehicle_Class') or '').strip().lower()
        suffix = slug(domain or vehicle_class or 'general')
        return f'vehicle.{suffix}', 'inferred-classification'

    record_type = (row.get('Record_Type') or '').strip().lower()
    text = ' '.join(str(v or '') for v in row.values()).lower()
    is_component = 'component' in record_type or any(term in record_type for term in ('module', 'system', 'weapon', 'engine', 'armor'))
    if not record_type:
        is_component = any(term in text for term in (' component ', ' module ', ' subsystem ', ' hardpoint '))
    if filename == 'expanded_mecha_and_components_all_genres.csv':
        return ('vehicle-component.mecha' if is_component else 'vehicle.mecha'), 'inferred-classification'
    return ('vehicle-component.spacecraft' if is_component else 'vehicle.spacecraft'), 'inferred-classification'


summary = {
    'format': 'multiversal-csv-domain-batch-summary',
    'workstream': contract['workstream'],
    'datasets': [],
    'totalRows': 0,
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0,
}

seen = set()
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
            for required in (spec['identityColumn'], spec['nameColumn']):
                if required not in fields:
                    raise SystemExit(f'{filename} missing required column {required}')
            for row_number, row in enumerate(reader, start=2):
                count += 1
                identity = (row.get(spec['identityColumn']) or '').strip()
                name = (row.get(spec['nameColumn']) or '').strip()
                route, evidence = classify(filename, row)
                routes[route] = routes.get(route, 0) + 1
                staging_id = f'mvstg:{slug(Path(filename).stem)}:{row_number}:{slug(identity or name)}'
                if staging_id in seen:
                    raise SystemExit(f'duplicate staging id {staging_id}')
                seen.add(staging_id)
                record = {
                    'stagingId': staging_id,
                    'dataset': filename,
                    'rowNumber': row_number,
                    'domain': 'vehicles',
                    'recordRouting': route,
                    'routingEvidence': evidence,
                    'identity': {'sourceIdentity': identity or None, 'displayName': name or None, 'canonicalId': None},
                    'rawSource': row,
                    'unmappedColumns': fields,
                    'provenance': {'archive': 'Csv.zip', 'dataset': filename, 'rowNumber': row_number},
                    'unresolvedManifest': [
                        'source-document-page-verification',
                        'field-level-provenance',
                        'component-parent-reconciliation',
                        'identity-reconciliation',
                        'vehicle-domain-validation',
                        'owner-promotion-approval'
                    ],
                    'validationState': 'vehicle-domain-staged-unverified',
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
