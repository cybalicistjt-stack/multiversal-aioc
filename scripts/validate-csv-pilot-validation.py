#!/usr/bin/env python3
import json
import sys
from pathlib import Path

base = Path('governance/object-system/item-examples')
report = json.loads((base / 'CSV_PILOT_VALIDATION_REPORT.json').read_text())
pilot = json.loads((base / 'CSV_PILOT_CONVERSION_OBJECTS.json').read_text())
core = json.loads(Path('governance/object-system/item-templates/ITEM_TEMPLATE_REGISTRY.json').read_text())
ext = json.loads(Path('governance/object-system/item-templates/ITEM_TEMPLATE_EXTENSION_REGISTRY.json').read_text())
failures = []

if report.get('format') != 'multiversal-csv-pilot-validation-report': failures.append('unsupported report format')
if report.get('workstream') != '8E-009L9': failures.append('wrong workstream')
results = report.get('results', [])
objects = pilot.get('objects', [])
if len(results) != 7 or len(objects) != 7: failures.append('pilot/report must each contain seven records')

object_by_id = {o['stagingId']: o for o in objects}
if len(object_by_id) != 7: failures.append('pilot staging IDs are not unique')
template_ids = {t['templateId'] for t in core.get('templates', [])} | {t['templateId'] for t in ext.get('templates', [])}

for result in results:
    sid = result.get('stagingId')
    obj = object_by_id.get(sid)
    if not obj:
        failures.append(f'report references unknown staging object {sid}')
        continue
    if result.get('templateId') != obj.get('templateId'):
        failures.append(f'{sid} template mismatch')
    if result.get('templateId') not in template_ids:
        failures.append(f'{sid} references unknown template')
    if result.get('structural') != 'pass' or result.get('identity') != 'pass':
        failures.append(f'{sid} failed structural or identity validation')
    if result.get('promotion') != 'blocked':
        failures.append(f'{sid} must remain promotion-blocked')
    if not result.get('blockers'):
        failures.append(f'{sid} missing blockers')
    if obj.get('identity', {}).get('canonicalId') is not None:
        failures.append(f'{sid} has canonical ID')
    if not obj.get('unresolvedFields'):
        failures.append(f'{sid} lost unresolved fields')
    if obj.get('provenance', {}).get('inferenceWarning') and result.get('templateValidation') != 'quarantined':
        failures.append(f'{sid} inference not quarantined')

summary = report.get('summary', {})
expected = {
    'objectCount': 7, 'structuralPass': 7, 'identityPass': 7,
    'provenancePresent': 7, 'canonicalIdsAssigned': 0,
    'objectsWithUnresolvedFields': 7, 'inferenceQuarantined': 3,
    'facetedObjects': 1, 'promotionReady': 0
}
for key, value in expected.items():
    if summary.get(key) != value: failures.append(f'summary mismatch for {key}')
readiness = report.get('batchReadiness', {})
if readiness.get('mappingEngineReadyForBoundedExpansion') is not True: failures.append('bounded expansion readiness missing')
if readiness.get('canonicalPromotionReady') is not False: failures.append('canonical promotion must remain false')
if 'controlled staging expansion' not in report.get('promotionBoundary', ''): failures.append('promotion boundary missing staging limit')

if failures:
    print('\n'.join(failures), file=sys.stderr)
    raise SystemExit(1)
print('CSV pilot validation report verified: 7 staging objects, 0 promotion-ready.')
