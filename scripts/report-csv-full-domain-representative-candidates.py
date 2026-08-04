#!/usr/bin/env python3
import csv, io, json, zipfile
from pathlib import Path

archive = Path('Csv.zip')
configs = {
  'weapons_and_ammo.csv': ['Weapon','Damage','Range','Weight','Cost','Special Rules','Standard Capacity','Source Notes'],
  'expanded_magitech_items_all_genres.csv': ['Item','Source Name','Magitech Type','Category','Subcategory','Primary Effect','Damage or Healing','Range or Area','Activation','Uses or Capacity','Failure or Drawback','Origin'],
  'expanded_bases_facilities_materials_and_homesteads_all_genres.csv': ['Item','Source Name','Record Type','Category','Subcategory','Primary Function','Mechanical Effect','Output or Capacity','Construction Materials','Cost','Origin','Source PDF'],
  'expanded_hazards_and_traps_all_genres.csv': ['Catalog_ID','Item_Name','Record_Type','Hazard_or_Trap','Category','Subtype','Description','Trigger','Detection_DC','Disarm_DC','Damage','Condition','Special_Rules','Source_PDF'],
  'expanded_land_sea_air_vehicles_all_genres.csv': ['Vehicle_ID','Item_Name','Record_Type','Vehicle_Class','Domain','Subtype','Description','Crew','Passengers','Cargo_Capacity','Durability_HP','Armor_or_Hardness','Cost','Source_PDF'],
  'expanded_mecha_and_components_all_genres.csv': ['Catalog_ID','Item_Name','Record_Type','Mecha_Class','Subclass_or_Component_Category','Description','HP','Armor_DR','Weapon_or_Primary_System','Damage_or_Output','Module_Slots','Cost'],
  'expanded_spacecraft_and_components_all_genres.csv': ['Catalog_ID','Item_Name','Record_Type','Ship_Class','Subclass_or_Component_Category','Description','Crew_Min','Hull_HP','Shield_HP','Primary_Weapon_or_Effect','Damage_or_Output','Module_Slots','Cost'],
  'completed_magic_spells_catalog.csv': ['Spell_ID','Spell_Name','Primary_School','Origin','Spell_Level','Mana_Cost','Spell_Role','Effect_Category','Casting_Time','Range','Duration','Damage','Healing','Condition_or_Buff','Source_PDF'],
  'ability_trees_and_abilities_catalog.csv': ['Record_ID','Record_Type','Ability_Name','Tree_ID','Ability_Tree','Tree_Category','Tier','Ability_XP_Cost','Ability_Type','Effect','Mechanics','Source_PDF'],
  'magic_arcane_and_faction_ability_trees_catalog.csv': ['Record_ID','Record_Type','Ability_Name','Tree_ID','Ability_Tree','Tree_Category','Tier','Ability_XP_Cost','Ability_Type','Effect','Mechanics','Source_PDF'],
  'profession_and_crafting_ability_trees_catalog.csv': ['Record_ID','Record_Type','Ability_Name','Tree_ID','Ability_Tree','Tree_Category','Tier','Ability_XP_Cost','Ability_Type','Effect','Mechanics','Source_PDF'],
  'prestige_environment_and_special_ability_trees_catalog.csv': ['Record_ID','Record_Type','Ability_Name','Tree_ID','Ability_Tree','Tree_Category','Tier','Ability_XP_Cost','Ability_Type','Effect','Mechanics','Source_PDF'],
  'species_elementalist_and_innate_abilities_catalog.csv': ['Record_ID','Record_Type','Ability_Name','Tree_ID','Ability_Tree','Tree_Category','Tier','Ability_XP_Cost','Ability_Type','Effect','Mechanics','Source_PDF'],
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
print('CSV_FULL_DOMAIN_REPRESENTATIVE_CANDIDATES=' + json.dumps(output, ensure_ascii=False, separators=(',',':')))
