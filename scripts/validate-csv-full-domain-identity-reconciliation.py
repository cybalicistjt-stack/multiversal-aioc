#!/usr/bin/env python3
import json
from pathlib import Path

path = Path('governance/object-system/csv-intake/CSV_FULL_DOMAIN_IDENTITY_RECONCILIATION.json')
data = json.loads(path.read_text())
failures = []
if data.get('format') != 'multiversal-csv-full-domain-identity-reconciliation': failures.append('format')
if data.get('workstream') != '8E-009L14': failures.append('workstream')
scope = data.get('scope', {})
if scope.get('datasetCount') != 20: failures.append('dataset count')
if scope.get('rowCount') != 19199: failures.append('row count')
expected_domains = {'items','mixed','hazards','vehicles','spells','abilities'}
if set(scope.get('domains', [])) != expected_domains: failures.append('domains')
groups = data.get('identityGroups', [])
files = [f for g in groups for f in g.get('datasets', [])]
if len(files) != 20 or len(set(files)) != 20: failures.append('dataset coverage')
if len(groups) != 7: failures.append('identity group count')
rules = data.get('rules', {})
for key in ['sourceIdsRemainNamespaced','normalizedNamesAreComparisonSignalsOnly','crossDomainMergesProhibited','variantsRemainSeparate','conflictingClaimsArePreserved','ownerApprovalRequiredForPromotion']:
    if rules.get(key) is not True: failures.append(key)
if rules.get('canonicalIdsAssigned') is not False: failures.append('canonical IDs')
if set(data.get('decisionStates', [])) != {'exact-source-id','probable-same-record','variant','homonym','conflict','unresolved'}: failures.append('decision states')
if 'does not merge records' not in data.get('promotionBoundary',''): failures.append('promotion boundary')
if failures:
    raise SystemExit('CSV full-domain identity reconciliation invalid: ' + ', '.join(failures))
print('CSV full-domain identity reconciliation validated: 20 datasets, 19,199 rows, 7 identity groups.')
