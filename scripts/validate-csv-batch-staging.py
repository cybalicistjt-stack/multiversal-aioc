#!/usr/bin/env python3
import json
import sys
from pathlib import Path

contract = json.loads(Path('governance/object-system/csv-intake/CSV_BATCH_STAGING_CONTRACT.json').read_text())
out_dir = Path('artifacts/csv-staging-batch')
summary = json.loads((out_dir / 'SUMMARY.json').read_text())
failures = []

if contract.get('format') != 'multiversal-csv-batch-staging-contract': failures.append('unsupported contract format')
if contract.get('workstream') != '8E-009L10-correction': failures.append('wrong contract workstream')
if len(contract.get('datasets', [])) != 20: failures.append('expected twenty batch datasets')
if contract.get('expectedTotalRows') != 19199: failures.append('expected full source row total')
if summary.get('totalRows') != contract.get('expectedTotalRows'): failures.append('summary total mismatch')
if summary.get('canonicalIdsAssigned') != 0: failures.append('canonical IDs assigned')
if summary.get('promotionReadyRows') != 0: failures.append('promotion-ready rows produced')
if summary.get('status') != 'full-source-staging-complete': failures.append('full-source batch status incomplete')

summary_by_file = {d['file']: d for d in summary.get('datasets', [])}
seen_ids = set()
record_count = 0
for spec in contract.get('datasets', []):
    entry = summary_by_file.get(spec['file'])
    if not entry or entry.get('rows') != spec['rows']:
        failures.append(f'{spec["file"]} summary mismatch')
        continue
    if entry.get('mappingState') != spec['mappingState']:
        failures.append(f'{spec["file"]} mapping state mismatch')
    if not entry.get('identityColumnUsed'):
        failures.append(f'{spec["file"]} identity fallback missing')
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
        if row.get('mappingState') != spec['mappingState']: failures.append(f'{sid} mapping state mismatch')
        if row.get('rawSource') is None: failures.append(f'{sid} missing raw source')
        if not row.get('unresolvedManifest'): failures.append(f'{sid} missing unresolved manifest')
        expected_state = 'staged-inference-quarantine' if row.get('inferenceWarning') else 'staged-unverified'
        if row.get('validationState') != expected_state: failures.append(f'{sid} validation state mismatch')

if record_count != contract.get('expectedTotalRows'): failures.append('validated record count mismatch')
if not contract.get('identityRules', {}).get('rowNumberAlwaysIncludedInStagingId'): failures.append('collision-safe staging ID rule missing')
if not contract.get('outputRules', {}).get('preserveRawRow'): failures.append('raw-row preservation disabled')
if not contract.get('outputRules', {}).get('preserveDomainRoutingBoundary'): failures.append('domain routing boundary disabled')
if contract.get('outputRules', {}).get('assignCanonicalIds') is not False: failures.append('canonical ID rule unsafe')
if 'noncanonical staging data only' not in contract.get('promotionBoundary', ''): failures.append('promotion boundary missing')

if failures:
    print('\n'.join(failures[:100]), file=sys.stderr)
    raise SystemExit(1)
print(f'CSV full-source staging validated: {record_count} rows across 20 datasets; 0 canonical IDs.')
