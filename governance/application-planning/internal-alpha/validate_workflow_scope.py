#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
WF = ROOT / '.github' / 'workflows'
BACKLOG = 'governance/application-planning/internal-alpha/INTERNAL_ALPHA_DESIGN_BACKLOG.md'
BROAD = "governance/application-planning/internal-alpha/**"
ALLOW_BROAD = {'internal-alpha-design-validation.yml', 'internal-alpha-content-fixtures-validation.yml', 'workflow-scope-validation.yml'}
errors=[]
for path in sorted(WF.glob('*.yml')):
    text=path.read_text(encoding='utf-8')
    if 'pull_request:' not in text:
        continue
    if BACKLOG in text:
        errors.append(f'{path.name}: live backlog must not trigger historical feature validation')
    if BROAD in text and path.name not in ALLOW_BROAD:
        errors.append(f'{path.name}: broad internal-alpha glob is not allowed')
    if 'internal-alpha' in text and 'concurrency:' not in text and path.name not in ALLOW_BROAD:
        errors.append(f'{path.name}: missing concurrency cancellation')
if errors:
    print('WORKFLOW SCOPE VALIDATION: FAIL')
    for error in errors: print('- '+error)
    sys.exit(1)
print('WORKFLOW SCOPE VALIDATION: PASS')
