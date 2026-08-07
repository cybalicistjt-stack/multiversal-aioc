#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
WF = ROOT / '.github' / 'workflows'
TARGETS = {
    'relationship-tracker-validation.yml',
    'two-device-reconnect-validation.yml',
    'full-combat-interface-validation.yml',
    'inventory-ownership-shared-assets-validation.yml',
    'bounded-maps-zones-positioning-validation.yml',
    'vehicle-operations-validation.yml',
    'investigation-clue-board-validation.yml',
    'graph-list-accessibility-validation.yml',
    'campaign-scene-session-design-validation.yml',
    'character-campaign-integration-validation.yml',
    'encounter-builder-balance-lab-design-validation.yml',
    'first-playable-action-approval-validation.yml',
    'internal-alpha-content-fixtures-validation.yml',
    'noncombat-integration-validation.yml',
    'proposal-approval-shared-component-validation.yml',
    'validate-ia-d06-005-combat-asset-integrity.yml',
    'validate-ia-d06-006-combat-assets-integration.yml',
    'validate-ia-d07-001-world-setting-management.yml',
    'internal-alpha-design-validation.yml',
}
BACKLOG = 'governance/application-planning/internal-alpha/INTERNAL_ALPHA_DESIGN_BACKLOG.md'
BROAD = 'governance/application-planning/internal-alpha/**'
errors=[]
for name in sorted(TARGETS):
    path=WF/name
    if not path.exists():
        errors.append(f'{name}: missing')
        continue
    text=path.read_text(encoding='utf-8')
    if BACKLOG in text: errors.append(f'{name}: live backlog trigger remains')
    if BROAD in text: errors.append(f'{name}: broad internal-alpha glob remains')
    if 'concurrency:' not in text or 'cancel-in-progress: true' not in text:
        errors.append(f'{name}: concurrency cancellation missing')
    if 'timeout-minutes:' not in text:
        errors.append(f'{name}: timeout missing')
if errors:
    print('WORKFLOW SCOPE VALIDATION: FAIL')
    for error in errors: print('- '+error)
    sys.exit(1)
print(f'WORKFLOW SCOPE VALIDATION: PASS ({len(TARGETS)} workflows)')
