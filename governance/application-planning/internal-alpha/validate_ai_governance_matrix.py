from pathlib import Path
R=Path(__file__).parent
files=['IA-D08-002_AI_PERMISSION_PROVENANCE_COST_FALLBACK_MATRIX.md','IA-D08-002_AI_GOVERNANCE_FIXTURE_MATRIX.md','IA-D08-002_AI_GOVERNANCE_TRACEABILITY.md','IA-D08-002_AI_GOVERNANCE_READINESS.md','IA-D08-002_COMPLETION_RECORD.md']
e=[f'missing {f}' for f in files if not (R/f).exists()]
s=(R/files[0]).read_text() if not e else ''
for p in ['Hard limits exist','no silent overage','request-status lookup before retry','P9-06-008-attempt-002']:
    if p not in s:e.append(f'spec missing {p}')
if e:
 print('IA-D08-002 AI GOVERNANCE VALIDATION: FAIL');[print('- '+x) for x in e];raise SystemExit(1)
print('IA-D08-002 AI GOVERNANCE VALIDATION: PASS')
