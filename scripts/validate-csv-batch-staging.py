#!/usr/bin/env python3
import json
import sys
from pathlib import Path

contract = json.loads(Path('governance/object-system/csv-intake/CSV_BATCH_STAGING_CONTRACT.json').read_text())
out_dir = Path('artifacts/csv-staging-batch')
summary = json.loads((out_dir / 'SUMMARY.json').read_text())
failures = []

if contract.get('format') != 'multiversal-csv-batch-staging-contract': failures.append('unsupported contract format')
if contract.get('workstream') != '8E-009L10': failures.append('wrong contract workstream')
if len(contract.get('datasets', [])) != 7: failures.append('expected seven batch datasets')
if summary.get('totalRows') != contract.get('expectedTotalRows'): failures.append('summary total mismatch')
if summary.get('canonicalIdsAssigned') != 0: failures.append('canonical IDs assigned')
if summary.get('promotionReadyRows') != 0: failures.append('promotion-ready rows produced')
if summary.get('status') != 'batch-staging-complete': failures.append('batch status incomplete')

summary_by_file = {d['file']: d for d in summary.get('datasets', [])}
seen_ids = set()
record_count = 0
for spec in contract.get('datasets', []):
    entry = summary_by_file.get(spec['file'])
    if not entry or entry.get('rows') != spec['rows']:
        failures.append(f'{spec["file"]} summary mismatch')
        continue
    path = Path(entry['output'])
    if not path.exists():
        failures.append(f'{spec["file"]} output missing')
        continue
    lines = path.read_text(encoding='utf-8').splitlines()
    if len(lines) != spec['rows']:
        failures.append(f'{spec["file"]} output row mismatch')
    for line in lines:
        record_count += 1
        row = json.loads(line)
        sid = row.get('stagingId')
        if not sid or sid in seen_ids: failures.append(f'duplicate or missing staging ID {sid}')
        seen_ids.add(sid)
        if row.get('canonicalId') is not None: failures.append(f'{sid} has canonical ID')
        if row.get('candidateTarget') != spec['target']: failures.append(f'{sid} target mismatch')
        if not row.get('rawSource'): failures.append(f'{sid} missing raw source')
        if not row.get('unresolvedManifest'): failures.append(f'{sid} missing unresolved manifest')
        expected_state = 'staged-inference-quarantine' if row.get('inferenceWarning') else 'staged-unverified'
        if row.get('validationState') != expected_state: failures.append(f'{sid} validation state mismatch')

if record_count != contract.get('expectedTotalRows'): failures.append('validated record count mismatch')
if not contract.get('outputRules', {}).get('preserveRawRow'): failures.append('raw-row preservation disabled')
if contract.get('outputRules', {}).get('assignCanonicalIds') is not False: failures.append('canonical ID rule unsafe')
if 'noncanonical staging data only' not in contract.get('promotionBoundary', ''): failures.append('promotion boundary missing')

if failures:
    print('\n'.join(failures[:100]), file=sys.stderr)
    raise SystemExit(1)
print(f'CSV batch staging validated: {record_count} rows across 7 datasets; 0 canonical IDs.')
