#!/usr/bin/env python3
import csv, io, json, zipfile
from pathlib import Path

archive = Path('Csv.zip')
configs = {
  'expanded_melee_weapons_all_genres.csv': ['Weapon','Category','Damage','Reach or Range','Weight','Cost','Origin'],
  'expanded_ranged_weapons_catalog.csv': ['Weapon','Category','Damage','Range','Standard Capacity','Ammo or Power'],
  'expanded_items_all_genres.csv': ['Item','Source Name','Category','Subcategory','Effect','Uses or Capacity','Activation','Origin'],
  'expanded_eva_suits_and_modules_all_genres.csv': ['Item','Source Name','Item Type','Subtype','Primary Effect','Compatibility','Intended Environment','Origin'],
  'expanded_computers_all_genres.csv': ['Item_ID','Item_Name','Processing_Power_PP','Memory_Rating_MC','Security_Rating_SR','Source_PDF','Source_Section'],
  'expanded_living_spellbooks_and_magic_charge_holders_all_genres.csv': ['Catalog_ID','Item_Name','Record_Type','Item_Family','Primary_Effect','Uses_or_Charges','Sentience_Level','Source_PDF','Source_Section'],
  'expanded_symbiotes_and_cybernetics_all_genres.csv': ['Item','Source Name','Upgrade Class','Family','Subtype','Primary Effect','Host Requirement','Origin','Source PDF'],
}
output = {}
with zipfile.ZipFile(archive) as bundle:
    entries = {Path(i.filename).name: i for i in bundle.infolist() if i.filename.lower().endswith('.csv')}
    for filename, fields in configs.items():
        text = bundle.read(entries[filename]).decode('utf-8-sig')
        rows = list(csv.DictReader(io.StringIO(text)))
        ranked = sorted(enumerate(rows, start=2), key=lambda pair: (-sum(bool((pair[1].get(f) or '').strip()) for f in fields), pair[0]))
        candidates = []
        for row_number, row in ranked[:3]:
            candidates.append({'rowNumber': row_number, 'filled': sum(bool((row.get(f) or '').strip()) for f in fields), 'values': {f: row.get(f,'') for f in fields}})
        output[filename] = candidates
print('CSV_REPRESENTATIVE_CANDIDATES=' + json.dumps(output, ensure_ascii=False, separators=(',',':')))
