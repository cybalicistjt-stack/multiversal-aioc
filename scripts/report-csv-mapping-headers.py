#!/usr/bin/env python3
import csv
import io
import json
import zipfile
from pathlib import Path

archive = Path('Csv.zip')
targets = [
    'expanded_items_all_genres.csv',
    'expanded_eva_suits_and_modules_all_genres.csv',
    'expanded_living_spellbooks_and_magic_charge_holders_all_genres.csv',
    'expanded_symbiotes_and_cybernetics_all_genres.csv',
]
with zipfile.ZipFile(archive) as bundle:
    names = {Path(info.filename).name: info.filename for info in bundle.infolist()}
    report = {}
    for target in targets:
        raw = bundle.read(names[target])
        text = raw.decode('utf-8-sig')
        reader = csv.reader(io.StringIO(text))
        report[target] = next(reader)
print('CSV_MAPPING_HEADERS=' + json.dumps(report, ensure_ascii=False, separators=(',', ':')))
