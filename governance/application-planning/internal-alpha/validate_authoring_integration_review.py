from pathlib import Path
R=Path(__file__).parent
files=['IA-D07-005_AUTHORING_INTEGRATION_REVIEW.md','IA-D07-005_INTEGRATED_JOURNEY_FIXTURES.md','IA-D07-005_TRACEABILITY_READINESS.md','IA-D07-005_COMPLETION_RECORD.md']
e=[f'missing {f}' for f in files if not (R/f).exists()]
s=(R/files[0]).read_text() if not e else ''
for p in ['IA-D07 is complete','eight journeys','Eleven adapters','P9-06-008-attempt-002']:
    if p not in s:e.append(f'review missing {p}')
if e:
 print('IA-D07-005 AUTHORING INTEGRATION VALIDATION: FAIL');[print('- '+x) for x in e];raise SystemExit(1)
print('IA-D07-005 AUTHORING INTEGRATION VALIDATION: PASS')