from pathlib import Path
R=Path(__file__).parent
files=['IA-D08-003_ADVANCED_MAP_VEHICLE_DEFERRAL_PACKAGE.md','IA-D08-003_DEFERRAL_FIXTURE_MATRIX.md','IA-D08-003_DEFERRAL_TRACEABILITY.md','IA-D08-003_DEFERRAL_READINESS.md','IA-D08-003_COMPLETION_RECORD.md']
e=[f'missing {f}' for f in files if not (R/f).exists()]
s=(R/files[0]).read_text() if not e else ''
for p in ['No silent approximation','opaque, versioned extension data','capability negotiation','P9-06-008-attempt-002']:
    if p not in s:e.append(f'package missing {p}')
if e:
 print('IA-D08-003 ADVANCED DEFERRAL VALIDATION: FAIL');[print('- '+x) for x in e];raise SystemExit(1)
print('IA-D08-003 ADVANCED DEFERRAL VALIDATION: PASS')
