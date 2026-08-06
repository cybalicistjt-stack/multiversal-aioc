from pathlib import Path
R=Path(__file__).parent
files=['IA-D07-003_CREATOR_CAMPAIGN_LOCAL_CONTENT_SPEC.md','IA-D07-003_CREATOR_CONTENT_FIXTURE_MATRIX.md','IA-D07-003_CREATOR_CONTENT_TRACEABILITY.md','IA-D07-003_CREATOR_CONTENT_READINESS.md','IA-D07-003_COMPLETION_RECORD.md']
e=[f'missing {f}' for f in files if not (R/f).exists()]
s=(R/files[0]).read_text() if not e else ''
for p in ['Campaign installation never grants canonical status','Arbitrary code','filtered before search','P9-06-008-attempt-002']:
    if p not in s:e.append(f'spec missing {p}')
if e:
 print('IA-D07-003 CREATOR CONTENT VALIDATION: FAIL');[print('- '+x) for x in e];raise SystemExit(1)
print('IA-D07-003 CREATOR CONTENT VALIDATION: PASS')