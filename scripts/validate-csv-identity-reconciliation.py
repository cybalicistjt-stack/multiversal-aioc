#!/usr/bin/env python3
import json
import sys
from pathlib import Path

path = Path('governance/object-system/csv-intake/CSV_IDENTITY_RECONCILIATION_REGISTRY.json')
registry = json.loads(path.read_text(encoding='utf-8'))
failures = []

if registry.get('format') != 'multiversal-csv-identity-reconciliation-registry':
    failures.append('unsupported registry format')
if registry.get('workstream') != '8E-009L6':
    failures.append('wrong workstream')

expected_decisions = {'same-record','probable-same-record','variant','homonym','conflict','unresolved'}
decisions = registry.get('decisions', [])
seen = {item.get('decision') for item in decisions}
if seen != expected_decisions:
    failures.append(f'decision coverage mismatch: {sorted(seen)}')
for item in decisions:
    if not isinstance(item.get('minimumEvidence'), list):
        failures.append(f"{item.get('decision')} missing evidence contract")
    if not item.get('effect'):
        failures.append(f"{item.get('decision')} missing effect")
    if not isinstance(item.get('automatic'), bool):
        failures.append(f"{item.get('decision')} missing automatic flag")

required_groups = {
    'weapons-ranged-ammunition',
    'general-items-and-magitech',
    'eva-hosts-and-modules',
    'living-implements-and-storage',
    'symbiotes-implants-modules',
}
groups = registry.get('overlapGroups', [])
group_ids = {item.get('groupId') for item in groups}
if group_ids != required_groups:
    failures.append('overlap group coverage mismatch')
for group in groups:
    if not group.get('datasets') or not group.get('identityColumns'):
        failures.append(f"{group.get('groupId')} incomplete")
    if not group.get('routingConstraint') or not group.get('defaultDisposition'):
        failures.append(f"{group.get('groupId')} missing routing contract")

stable = registry.get('stableIdentityKey', {})
if not stable.get('format', '').startswith('mvstg:'):
    failures.append('staging identity key format missing')
if len(stable.get('rules', [])) < 5:
    failures.append('staging identity rules incomplete')

review = registry.get('reviewCluster', {})
for required in ['clusterId','members','signals','conflicts','recommendedDisposition','verificationNeeded','status']:
    if required not in review.get('requiredFields', []):
        failures.append(f'review cluster missing {required}')
for prohibited in ['silent-merge','silent-field-precedence','discard-conflicting-claim','canonical-promotion']:
    if prohibited not in review.get('prohibitedActions', []):
        failures.append(f'missing prohibited action {prohibited}')

if len(registry.get('materialConflictFields', [])) < 10:
    failures.append('material conflict fields incomplete')
if registry.get('fieldPrecedence', {}).get('rule') != 'No dataset has universal precedence.':
    failures.append('field precedence boundary missing')
if 'does not certify source fidelity' not in registry.get('promotionBoundary', ''):
    failures.append('promotion boundary missing')

if failures:
    print('\n'.join(failures), file=sys.stderr)
    raise SystemExit(1)
print(f"CSV identity reconciliation validated: {len(groups)} overlap groups, {len(decisions)} dispositions.")
