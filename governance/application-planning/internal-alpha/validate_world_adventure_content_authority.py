from pathlib import Path
R=Path(__file__).parent
files=['IA-D07-004_WORLD_ADVENTURE_CONTENT_AUTHORITY_MATRIX.md','IA-D07-004_AUTHORITY_FIXTURE_MATRIX.md','IA-D07-004_AUTHORITY_TRACEABILITY_READINESS.md','IA-D07-004_COMPLETION_RECORD.md']
e=[f'missing {f}' for f in files if not (R/f).exists()]
s=(R/files[0]).read_text() if not e else ''
for p in ['Published source versions are immutable','Campaign runs and overlays never mutate source definitions','filtered before aggregation','John Brandon Turner']:
    if p not in s:e.append(f'matrix missing {p}')
if e:
 print('IA-D07-004 AUTHORITY VALIDATION: FAIL');[print('- '+x) for x in e];raise SystemExit(1)
print('IA-D07-004 AUTHORITY VALIDATION: PASS')