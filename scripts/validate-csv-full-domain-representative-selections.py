#!/usr/bin/env python3
import json, sys
from pathlib import Path

path = Path('governance/object-system/csv-intake/CSV_FULL_DOMAIN_REPRESENTATIVE_SELECTIONS.json')
data = json.loads(path.read_text(encoding='utf-8'))
errors = []
selections = data.get('selections', [])
if data.get('format') != 'multiversal-csv-full-domain-representative-selections': errors.append('invalid format')
if len(selections) != 13: errors.append(f'expected 13 selections, got {len(selections)}')
if len({s.get('dataset') for s in selections}) != 13: errors.append('datasets must be unique')
for s in selections:
    for key in ('dataset','rowNumber','sourceIdentity','domain','reason'):
        if not s.get(key): errors.append(f"{s.get('dataset','?')}: missing {key}")
    if not isinstance(s.get('rowNumber'), int) or s['rowNumber'] < 2: errors.append(f"{s.get('dataset','?')}: invalid rowNumber")
rules = data.get('rules', {})
for key in ('stagingOnly','rawRowRequired','mappingContractRequired','identityReconciliationRequired','sourceVerificationRequiredBeforePromotion'):
    if rules.get(key) is not True: errors.append(f'rule {key} must be true')
for key in ('canonicalIdsAllowed','promotionAllowed'):
    if rules.get(key) is not False: errors.append(f'rule {key} must be false')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print('CSV full-domain representative selections valid: 13 datasets')
