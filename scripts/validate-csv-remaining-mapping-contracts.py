#!/usr/bin/env python3
import json
import sys
from pathlib import Path

path = Path('governance/object-system/csv-intake/CSV_REMAINING_MAPPING_CONTRACT_REGISTRY.json')
data = json.loads(path.read_text())
failures = []

if data.get('format') != 'multiversal-csv-remaining-mapping-contract-registry': failures.append('unsupported format')
if data.get('workstream') != '8E-009L13': failures.append('wrong workstream')
contracts = data.get('contracts', [])
if len(contracts) != 13 or data.get('datasetCount') != 13: failures.append('expected 13 contracts')
if sum(c.get('rows', 0) for c in contracts) != 14378 or data.get('rowCount') != 14378: failures.append('row total mismatch')
if len({c.get('dataset') for c in contracts}) != 13: failures.append('duplicate dataset contract')
allowed = {'direct','deterministic-normalization','inferred-classification'}
for contract in contracts:
    if not contract.get('identityColumn'): failures.append(f"missing identity column: {contract.get('dataset')}")
    if not contract.get('target') or not contract.get('domain'): failures.append(f"missing routing: {contract.get('dataset')}")
    mappings = contract.get('mappings', [])
    if not mappings: failures.append(f"no mappings: {contract.get('dataset')}")
    sources = [m.get('source') for m in mappings]
    if contract.get('identityColumn') not in sources: failures.append(f"identity not mapped: {contract.get('dataset')}")
    for mapping in mappings:
        if not mapping.get('source') or not mapping.get('target') or not mapping.get('transform'): failures.append(f"incomplete mapping: {contract.get('dataset')}")
        if mapping.get('evidence') not in allowed: failures.append(f"bad evidence: {contract.get('dataset')}")
rules = data.get('rules', {})
for key in ('exactHeadersRequired','noSilentDefaults','preserveRawRow','preserveUnmappedColumns','crossDomainCoercionForbidden','canonicalIdsForbidden','sourceVerificationRequiredBeforePromotion'):
    if rules.get(key) is not True: failures.append(f'missing safety rule: {key}')
if 'do not' not in data.get('promotionBoundary','').lower(): failures.append('promotion boundary missing')

if failures:
    print('\n'.join(failures), file=sys.stderr)
    raise SystemExit(1)
print('Remaining CSV mapping contracts validated: 13 datasets, 14,378 rows.')
