import csv
import json
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_VEHICLE_PARENT_RECONCILIATION_CONTRACT.json').read_text())
out_path = ROOT / contract['output']
out_path.parent.mkdir(parents=True, exist_ok=True)

PARENT_HEADERS = {
    'Parent_ID', 'Parent_Id', 'ParentID', 'Parent', 'Parent_Vehicle_ID',
    'Vehicle_ID', 'Mecha_ID', 'Spacecraft_ID', 'Host_ID', 'Platform_ID'
}
COMPONENT_TERMS = ('component', 'module', 'system', 'weapon', 'engine', 'armor', 'shield', 'hardpoint', 'subsystem')

report = {
    'format': 'multiversal-csv-vehicle-parent-reconciliation-report',
    'version': '0.1.0',
    'workstream': contract['workstream'],
    'datasets': [],
    'totals': {
        'rows': 0,
        'vehicles': 0,
        'components': 0,
        'deterministicParentLinks': 0,
        'unresolvedComponents': 0
    },
    'resolution': 'pending-source-verification',
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0
}

with zipfile.ZipFile(ROOT / contract['archive']) as zf:
    members = {Path(name).name: name for name in zf.namelist() if not name.endswith('/')}
    for filename in contract['datasets']:
        member = members.get(filename)
        if not member:
            raise SystemExit(f'missing {filename}')
        with zf.open(member) as raw:
            reader = csv.DictReader(line.decode('utf-8-sig') for line in raw)
            headers = reader.fieldnames or []
            explicit_parent_headers = sorted(set(headers) & PARENT_HEADERS)
            counts = Counter()
            unresolved = []
            for row_number, row in enumerate(reader, start=2):
                counts['rows'] += 1
                record_type = (row.get('Record_Type') or '').strip().lower()
                text = ' '.join(str(v or '') for v in row.values()).lower()
                is_component = any(term in record_type for term in COMPONENT_TERMS)
                if not record_type:
                    is_component = any(f' {term} ' in f' {text} ' for term in COMPONENT_TERMS)
                if is_component:
                    counts['components'] += 1
                    parent_values = {
                        header: (row.get(header) or '').strip()
                        for header in explicit_parent_headers
                        if (row.get(header) or '').strip()
                    }
                    if parent_values:
                        counts['deterministicParentLinks'] += 1
                    else:
                        unresolved.append({
                            'rowNumber': row_number,
                            'catalogId': (row.get('Catalog_ID') or '').strip() or None,
                            'itemName': (row.get('Item_Name') or '').strip() or None,
                            'recordType': (row.get('Record_Type') or '').strip() or None,
                            'sourceDocument': (row.get('Source_PDF') or '').strip() or None,
                            'reason': 'no-explicit-parent-reference-in-csv'
                        })
                else:
                    counts['vehicles'] += 1

        dataset_report = {
            'file': filename,
            'headers': headers,
            'explicitParentHeaders': explicit_parent_headers,
            'rows': counts['rows'],
            'vehicles': counts['vehicles'],
            'components': counts['components'],
            'deterministicParentLinks': counts['deterministicParentLinks'],
            'unresolvedComponents': len(unresolved),
            'unresolvedQueue': unresolved,
            'requiredNextEvidence': [
                'source-document-page-verification',
                'explicit-parent-or-platform-evidence',
                'component-compatibility-validation'
            ]
        }
        report['datasets'].append(dataset_report)
        for key in ('rows', 'vehicles', 'components', 'deterministicParentLinks'):
            report['totals'][key] += counts[key]
        report['totals']['unresolvedComponents'] += len(unresolved)

if report['totals']['deterministicParentLinks']:
    report['resolution'] = 'partially-resolved-explicit-links-only'
elif report['totals']['components'] == report['totals']['unresolvedComponents']:
    report['resolution'] = 'csv-insufficient-all-components-require-source-verification'

out_path.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
print(json.dumps(report['totals'], sort_keys=True))
