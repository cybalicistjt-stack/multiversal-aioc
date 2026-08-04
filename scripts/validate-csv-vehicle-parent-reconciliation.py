import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(ROOT / 'scripts/reconcile-csv-vehicle-parent-links.py')], check=True)
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_VEHICLE_PARENT_RECONCILIATION_CONTRACT.json').read_text())
report = json.loads((ROOT / contract['output']).read_text())

assert len(report['datasets']) == 2
assert report['totals']['rows'] == 4428
assert report['totals']['vehicles'] + report['totals']['components'] == 4428
assert report['totals']['unresolvedComponents'] + report['totals']['deterministicParentLinks'] == report['totals']['components']
assert report['canonicalIdsAssigned'] == 0
assert report['promotionReadyRows'] == 0
assert all('unresolvedQueue' in dataset for dataset in report['datasets'])
assert all(dataset['rows'] > 0 for dataset in report['datasets'])
assert report['resolution'] in {
    'csv-insufficient-all-components-require-source-verification',
    'partially-resolved-explicit-links-only'
}
print(json.dumps({'status': 'passed', 'totals': report['totals'], 'resolution': report['resolution']}, sort_keys=True))
