#!/usr/bin/env python3
import json
from pathlib import Path

pilot_path = Path('governance/object-system/csv-intake/CSV_FULL_DOMAIN_PILOT_OBJECTS.json')
selection_path = Path('governance/object-system/csv-intake/CSV_FULL_DOMAIN_REPRESENTATIVE_SELECTIONS.json')
existing_path = Path('governance/object-system/item-examples/CSV_PILOT_CONVERSION_OBJECTS.json')

pilot = json.loads(pilot_path.read_text())
selections = json.loads(selection_path.read_text())
existing = json.loads(existing_path.read_text())

errors = []
objects = pilot.get('objects', [])
selected = selections.get('selections', [])
if len(objects) != 13:
    errors.append(f'expected 13 new pilot objects, found {len(objects)}')
if len(selected) != 13:
    errors.append(f'expected 13 selections, found {len(selected)}')
if len(existing.get('objects', [])) != 7:
    errors.append('existing pilot set must contain 7 objects')

selected_pairs = {(x['dataset'], x['rowNumber']) for x in selected}
object_pairs = {(x.get('provenance', {}).get('dataset'), x.get('provenance', {}).get('rowNumber')) for x in objects}
if selected_pairs != object_pairs:
    errors.append(f'selection/object provenance mismatch: missing={sorted(selected_pairs-object_pairs)} extra={sorted(object_pairs-selected_pairs)}')

ids = [x.get('stagingId') for x in objects]
if len(ids) != len(set(ids)) or any(not x or not x.startswith('mvstg:') for x in ids):
    errors.append('staging IDs must be unique and use mvstg namespace')

allowed_domains = {'items','mixed','hazards','vehicles','spells','abilities'}
for obj in objects:
    sid = obj.get('stagingId', '<missing>')
    if obj.get('domain') not in allowed_domains:
        errors.append(f'{sid}: invalid domain')
    if not obj.get('templateRouting'):
        errors.append(f'{sid}: missing template routing')
    if obj.get('identity', {}).get('canonicalId', 'missing') is not None:
        errors.append(f'{sid}: canonicalId must be null')
    if not obj.get('provenance', {}).get('dataset') or not obj.get('provenance', {}).get('rowNumber'):
        errors.append(f'{sid}: incomplete provenance')
    if not obj.get('unresolvedFields'):
        errors.append(f'{sid}: unresolved fields must be explicit')
    if obj.get('validationState') not in {'staged-with-unresolved-fields','staged-inference-quarantine'}:
        errors.append(f'{sid}: invalid validation state')

all_datasets = {x['provenance']['dataset'] for x in objects} | {x['provenance']['dataset'] for x in existing['objects']}
if len(all_datasets) != 20:
    errors.append(f'expected representative pilot coverage for 20 datasets, found {len(all_datasets)}')

if pilot.get('rules', {}).get('noCanonicalIds') is not True:
    errors.append('noCanonicalIds guard missing')
if pilot.get('rules', {}).get('promotionRequiresSourceVerificationAndOwnerApproval') is not True:
    errors.append('promotion approval guard missing')

if errors:
    raise SystemExit('CSV_FULL_DOMAIN_PILOT_VALIDATION_FAILED\n- ' + '\n- '.join(errors))
print('CSV_FULL_DOMAIN_PILOT_VALIDATION_PASS datasets=20 existing=7 new=13 total_objects=20 canonical_ids=0 promoted=0')
