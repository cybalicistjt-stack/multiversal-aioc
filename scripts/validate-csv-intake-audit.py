#!/usr/bin/env python3
import csv
import hashlib
import io
import json
import sys
import zipfile
from collections import Counter
from pathlib import Path

ARCHIVE = Path('Csv.zip')
SNAPSHOT = Path('governance/object-system/csv-intake/CSV_INTAKE_AUDIT_SNAPSHOT.json')

failures = []
if not ARCHIVE.is_file():
    failures.append('Csv.zip missing')
if not SNAPSHOT.is_file():
    failures.append('CSV audit snapshot missing')
if failures:
    print('\n'.join(failures), file=sys.stderr)
    raise SystemExit(1)

snapshot = json.loads(SNAPSHOT.read_text(encoding='utf-8'))
archive_hash = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
if archive_hash != snapshot['archiveSha256']:
    failures.append(f'archive hash mismatch: {archive_hash}')

actual = []
exact_duplicates = 0
uncompressed_bytes = 0
with zipfile.ZipFile(ARCHIVE) as bundle:
    csv_entries = sorted(i for i in bundle.infolist() if i.filename.lower().endswith('.csv'))
    for entry in csv_entries:
        raw = bundle.read(entry.filename)
        uncompressed_bytes += len(raw)
        text = raw.decode('utf-8-sig', errors='strict')
        rows = list(csv.reader(io.StringIO(text)))
        if not rows:
            failures.append(f'{entry.filename}: empty CSV')
            continue
        width = len(rows[0])
        body = rows[1:]
        widths = Counter(len(row) for row in body)
        exact_duplicates += len(body) - len({tuple(row) for row in body})
        actual.append({
            'name': Path(entry.filename).name,
            'rows': len(body),
            'columns': width,
            'ragged': any(row_width != width for row_width in widths),
        })

expected = sorted(snapshot['files'], key=lambda item: item['name'])
actual = sorted(actual, key=lambda item: item['name'])
if actual != expected:
    failures.append('CSV file structure differs from governed snapshot')
if len(actual) != snapshot['totals']['csvFiles']:
    failures.append('CSV file total mismatch')
if sum(item['rows'] for item in actual) != snapshot['totals']['rows']:
    failures.append('row total mismatch')
if uncompressed_bytes != snapshot['totals']['uncompressedBytes']:
    failures.append('uncompressed byte total mismatch')
if exact_duplicates != snapshot['totals']['exactDuplicateRows']:
    failures.append('exact duplicate total mismatch')
if 'does not certify semantic accuracy' not in snapshot.get('promotionBoundary', ''):
    failures.append('promotion boundary missing')

if failures:
    print('\n'.join(failures), file=sys.stderr)
    raise SystemExit(1)

print(f"CSV intake audit validated: {len(actual)} files, {sum(item['rows'] for item in actual):,} rows.")
