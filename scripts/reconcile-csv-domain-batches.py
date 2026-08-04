import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / 'governance/object-system/csv-intake/CSV_CROSS_BATCH_RECONCILIATION_CONTRACT.json').read_text())

commands = [
    'scripts/convert-csv-batch-to-staging.py',
    'scripts/convert-csv-item-domain-batch-1.py',
    'scripts/convert-csv-mixed-hazard-domain-batch.py',
    'scripts/convert-csv-vehicle-domain-batch.py',
    'scripts/convert-csv-spell-domain-batch.py',
    'scripts/convert-csv-ability-domain-batch.py',
]
for command in commands:
    subprocess.run([sys.executable, str(ROOT / command)], check=True)

full_dir = ROOT / 'artifacts/csv-staging-batch'
jsonl_files = sorted(full_dir.glob('*.jsonl'))
rows = 0
staging_ids = set()
datasets = set()
quarantined = 0
for path in jsonl_files:
    with path.open(encoding='utf-8') as handle:
        for line in handle:
            record = json.loads(line)
            rows += 1
            sid = record.get('stagingId')
            if not sid or sid in staging_ids:
                raise SystemExit(f'duplicate or missing stagingId: {sid}')
            staging_ids.add(sid)
            datasets.add(record.get('dataset'))
            if not record.get('rawSource') or not record.get('unresolvedManifest'):
                raise SystemExit(f'missing preservation fields in {sid}')
            if record.get('identity', {}).get('canonicalId') is not None or record.get('promotionReady') is True:
                raise SystemExit(f'promotion boundary violated by {sid}')
            if record.get('routingEvidence') == 'inferred-classification' or record.get('validationState') == 'inference-quarantined':
                quarantined += 1

if rows != contract['expectedRows']:
    raise SystemExit(f'rows {rows} != {contract["expectedRows"]}')
if len(datasets) != contract['expectedDatasets']:
    raise SystemExit(f'datasets {len(datasets)} != {contract["expectedDatasets"]}')
if sum(x['rows'] for x in contract['domainBatches']) != rows:
    raise SystemExit('domain batch row arithmetic mismatch')
if sum(x['datasets'] for x in contract['domainBatches']) != len(datasets):
    raise SystemExit('domain batch dataset arithmetic mismatch')

report = {
    'format': 'multiversal-csv-cross-batch-reconciliation-report',
    'version': '0.1.0',
    'workstream': contract['workstream'],
    'status': 'validated-staging-reconciled',
    'datasetsValidated': len(datasets),
    'rowsValidated': rows,
    'uniqueStagingIds': len(staging_ids),
    'quarantinedRowsObserved': quarantined,
    'canonicalIdsAssigned': 0,
    'promotionReadyRows': 0,
    'relationshipQueues': contract['relationshipFamilies'],
    'assertions': contract['requiredAssertions'],
    'nextExecutableWork': 'Resolve bounded relationship and identity queues, beginning with vehicle-component parent links and ability tree-parent links.',
    'promotionBoundary': contract['promotionBoundary'],
}
out = ROOT / 'build/csv-cross-batch-reconciliation-l25'
out.mkdir(parents=True, exist_ok=True)
(out / 'REPORT.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
print(json.dumps(report, sort_keys=True))
