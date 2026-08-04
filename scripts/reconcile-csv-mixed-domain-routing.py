import csv
import json
import re
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_MIXED_DOMAIN_ROUTING_RECONCILIATION_CONTRACT.json').read_text())
out_dir = ROOT / contract['outputDirectory']
out_dir.mkdir(parents=True, exist_ok=True)


def normalize(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', ' ', (value or '').lower()).strip()


CONTROLLED = {
    'base': 'base',
    'bases': 'base',
    'facility': 'facility',
    'facilities': 'facility',
    'homestead': 'homestead',
    'homesteads': 'homestead',
    'material': 'item.material.crafting-resource',
    'materials': 'item.material.crafting-resource',
    'crafting material': 'item.material.crafting-resource',
    'crafting materials': 'item.material.crafting-resource',
    'construction material': 'item.material.crafting-resource',
    'construction materials': 'item.material.crafting-resource'
}

filename = contract['dataset']
rows = []
with zipfile.ZipFile(ROOT / 'Csv.zip') as zf:
    members = {Path(name).name: name for name in zf.namelist() if not name.endswith('/')}
    member = members.get(filename)
    if not member:
        raise SystemExit(f'missing {filename}')
    with zf.open(member) as raw:
        reader = csv.DictReader(line.decode('utf-8-sig') for line in raw)
        fields = reader.fieldnames or []
        required = {'Item', contract['routingColumn']}
        missing = sorted(required - set(fields))
        if missing:
            raise SystemExit(f'{filename} missing required columns {missing}')
        for row_number, row in enumerate(reader, start=2):
            rows.append((row_number, row))

if len(rows) != contract['expectedRows']:
    raise SystemExit(f'row count {len(rows)} != {contract["expectedRows"]}')

summary = {
    'format': 'multiversal-csv-mixed-domain-routing-reconciliation-report',
    'workstream': contract['workstream'],
    'dataset': filename,
    'rows': len(rows),
    'resolvedRows': 0,
    'unresolvedRows': 0,
    'routes': Counter(),
    'sourceValueCensus': Counter(),
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0
}

resolved_path = out_dir / 'RESOLVED_ROUTING.jsonl'
unresolved_path = out_dir / 'UNRESOLVED_ROUTING.jsonl'
with resolved_path.open('w', encoding='utf-8') as resolved, unresolved_path.open('w', encoding='utf-8') as unresolved:
    for row_number, row in rows:
        raw_value = (row.get(contract['routingColumn']) or '').strip()
        normalized = normalize(raw_value)
        summary['sourceValueCensus'][normalized or '<blank>'] += 1
        route = CONTROLLED.get(normalized)
        state = 'resolved' if route else ('blank' if not normalized else 'unsupported-source-value')
        record = {
            'dataset': filename,
            'rowNumber': row_number,
            'sourceIdentity': (row.get('Item') or '').strip() or None,
            'recordTypeSource': raw_value or None,
            'recordTypeNormalized': normalized or None,
            'routingState': state,
            'resolvedRoute': route,
            'routingEvidence': 'exact-controlled-source-value' if route else None,
            'canonicalId': None,
            'promotionReady': False
        }
        if route:
            summary['resolvedRows'] += 1
            summary['routes'][route] += 1
            resolved.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n')
        else:
            summary['unresolvedRows'] += 1
            unresolved.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n')

summary['routes'] = dict(sorted(summary['routes'].items()))
summary['sourceValueCensus'] = dict(sorted(summary['sourceValueCensus'].items()))
(out_dir / 'SUMMARY.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
print(json.dumps(summary, sort_keys=True))
