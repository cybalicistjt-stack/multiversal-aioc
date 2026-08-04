#!/usr/bin/env python3
import json
import sys
from pathlib import Path

path = Path('governance/object-system/item-examples/CSV_PILOT_CONVERSION_OBJECTS.json')
data = json.loads(path.read_text())
failures = []

if data.get('format') != 'multiversal-csv-pilot-conversion-objects':
    failures.append('unsupported pilot format')
if data.get('workstream') != '8E-009L8':
    failures.append('wrong workstream')
objects = data.get('objects', [])
if len(objects) != 7:
    failures.append('expected exactly seven pilot objects')

expected_ids = {
    'mvstg:expanded-melee-weapons-all-genres:2',
    'mvstg:expanded-ranged-weapons-catalog:2',
    'mvstg:expanded-items-all-genres:2',
    'mvstg:expanded-eva-suits-and-modules-all-genres:2',
    'mvstg:expanded-computers-all-genres:CMP-0001',
    'mvstg:expanded-living-spellbooks-and-magic-charge-holders-all-genres:LS-S-001',
    'mvstg:expanded-symbiotes-and-cybernetics-all-genres:2'
}
seen = set()
for obj in objects:
    sid = obj.get('stagingId')
    if sid in seen:
        failures.append(f'duplicate stagingId {sid}')
    seen.add(sid)
    for key in ('templateId', 'identity', 'provenance', 'unresolvedFields', 'validationState'):
        if key not in obj:
            failures.append(f'{sid} missing {key}')
    if obj.get('identity', {}).get('canonicalId') is not None:
        failures.append(f'{sid} assigned canonical ID')
    if not obj.get('unresolvedFields'):
        failures.append(f'{sid} must preserve unresolved fields')
    if obj.get('validationState') not in {
        'staged-with-unresolved-fields', 'staged-inference-quarantine', 'staged-faceted-object'
    }:
        failures.append(f'{sid} has unsupported validation state')
    if obj.get('provenance', {}).get('inferenceWarning') and obj.get('validationState') != 'staged-inference-quarantine':
        failures.append(f'{sid} inference warning not quarantined')

if seen != expected_ids:
    failures.append('pilot staging IDs do not match governed selections')
rules = data.get('rules', {})
for key in ('preserveSourceClaims', 'noSilentDefaults', 'noCanonicalIds', 'unverifiedInferencesRemainUnresolved', 'promotionRequiresOwnerApproval'):
    if rules.get(key) is not True:
        failures.append(f'missing safety rule {key}')
if 'noncanonical' not in data.get('promotionBoundary', ''):
    failures.append('promotion boundary missing noncanonical status')

if failures:
    print('\n'.join(failures), file=sys.stderr)
    raise SystemExit(1)
print('CSV pilot conversion validated: 7 governed staging objects.')
