from pathlib import Path

R = Path(__file__).parent
FILES = [
    'IA-D08-004_BROAD_OFFLINE_DEFERRAL_PACKAGE.md',
    'IA-D08-004_OFFLINE_DEFERRAL_FIXTURE_MATRIX.md',
    'IA-D08-004_OFFLINE_DEFERRAL_TRACEABILITY.md',
    'IA-D08-004_OFFLINE_DEFERRAL_READINESS.md',
    'IA-D08-004_COMPLETION_RECORD.md',
]

errors = [f'missing {name}' for name in FILES if not (R / name).exists()]

texts = {}
for name in FILES:
    path = R / name
    if path.exists():
        texts[name] = path.read_text(encoding='utf-8')

package = texts.get(FILES[0], '')
fixtures = texts.get(FILES[1], '')
trace = texts.get(FILES[2], '')
readiness = texts.get(FILES[3], '')
completion = texts.get(FILES[4], '')

required_package_phrases = [
    'Offline does not create authority',
    'No silent last-write-wins',
    'opaque, versioned extension data',
    'Event-gap recovery',
    'P9-06-008-attempt-002',
    'IA-D08-005',
]
for phrase in required_package_phrases:
    if phrase not in package:
        errors.append(f'package missing required phrase: {phrase}')

for fixture_id in range(1, 25):
    token = f'OFF-FX-{fixture_id:03d}'
    if token not in fixtures:
        errors.append(f'fixture matrix missing {token}')

for phrase in ['IA-D04-003', 'IA-D08-003', 'IA-D08-005', 'authorization']:
    if phrase not in trace:
        errors.append(f'traceability missing {phrase}')

for phrase in ['Blocking acceptance criteria', 'Unknown extension processors never execute', 'No broad-offline feature']:
    if phrase not in readiness:
        errors.append(f'readiness missing {phrase}')

for phrase in ['Twenty-four deterministic fixtures', 'Eight bounded implementation slices', 'merge evidence']:
    if phrase not in completion:
        errors.append(f'completion record missing {phrase}')

if errors:
    print('IA-D08-004 BROAD OFFLINE DEFERRAL VALIDATION: FAIL')
    for error in errors:
        print('- ' + error)
    raise SystemExit(1)

print('IA-D08-004 BROAD OFFLINE DEFERRAL VALIDATION: PASS')
