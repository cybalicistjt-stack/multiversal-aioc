import csv
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_ITEM_DOMAIN_BATCH_1_CONTRACT.json').read_text())
archive = ROOT / 'Csv.zip'
out_dir = ROOT / contract['outputDirectory']
out_dir.mkdir(parents=True, exist_ok=True)


def slug(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-') or 'unnamed'


def classify(dataset: str, row: dict) -> tuple[str, str]:
    text = ' '.join(str(v or '') for v in row.values()).lower()
    if dataset == 'weapons_and_ammo.csv':
        ammo_terms = ('ammo', 'ammunition', 'round', 'shell', 'rocket', 'grenade', 'cartridge', 'magazine')
        target = 'item.ammunition' if any(term in text for term in ammo_terms) else 'item.weapon.firearm'
        return target, 'inferred-classification'
    magitech_type = (row.get('Magitech Type') or '').lower()
    if any(term in magitech_type for term in ('weapon', 'firearm', 'blade', 'gun')):
        target = 'item.weapon.firearm'
    elif any(term in magitech_type for term in ('implement', 'focus', 'wand', 'staff')):
        target = 'item.magic.implement'
    else:
        target = 'item.device.computer'
    return target, 'inferred-classification'

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
                target, evidence = classify(filename, row)
                routes[target] = routes.get(target, 0) + 1
                record = {
                    'stagingId': f'mvstg:{slug(Path(filename).stem)}:{row_number}:{slug(identity)}',
                    'dataset': filename,
                    'rowNumber': row_number,
                    'domain': 'items',
                    'templateRouting': target,
                    'routingEvidence': evidence,
                    'identity': {'sourceIdentity': identity or None, 'canonicalId': None},
                    'rawSource': row,
                    'unmappedColumns': fields,
                    'provenance': {'archive': 'Csv.zip', 'dataset': filename, 'rowNumber': row_number},
                    'unresolvedManifest': [
                        'source-document-page-verification',
                        'field-level-provenance',
                        'identity-reconciliation',
                        'template-validation',
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
