from pathlib import Path
R=Path(__file__).parent
files=['IA-D08-001_OPTIONAL_AI_ASSISTANT_SPEC.md','IA-D08-001_OPTIONAL_AI_FIXTURE_MATRIX.md','IA-D08-001_OPTIONAL_AI_TRACEABILITY.md','IA-D08-001_OPTIONAL_AI_READINESS.md','IA-D08-001_COMPLETION_RECORD.md']
e=[f'missing {f}' for f in files if not (R/f).exists()]
s=(R/files[0]).read_text() if not e else ''
for p in ['AI output is advisory','Redaction occurs before retrieval','AI failure never blocks core non-AI workflows','P9-06-008-attempt-002']:
    if p not in s:e.append(f'spec missing {p}')
if e:
 print('IA-D08-001 OPTIONAL AI VALIDATION: FAIL');[print('- '+x) for x in e];raise SystemExit(1)
print('IA-D08-001 OPTIONAL AI VALIDATION: PASS')
