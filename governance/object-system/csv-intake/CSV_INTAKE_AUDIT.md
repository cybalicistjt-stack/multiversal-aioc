# Governed CSV Intake and Data-Quality Audit

**Workstream:** 8E-009L1  
**Source archive:** `Csv.zip`  
**Archive SHA-256:** `2f621e71cbcf614317189c38ffe7d670ce13dd9e7ed20bdf35438377f4af061b`

## Verified archive totals

- CSV files: **20**
- Data rows: **19,199**
- Uncompressed CSV bytes: **50,376,355**
- Exact duplicate rows: **0**

These are structured intake records, not automatically canonical objects. No mass conversion or promotion is authorized by this audit.

## Dataset summary

| File | Rows | Columns | Structural issue |
|---|---:|---:|---|
| `magic_arcane_and_faction_ability_trees_catalog.csv` | 118 | 58 | none detected |
| `profession_and_crafting_ability_trees_catalog.csv` | 221 | 58 | ragged row widths |
| `prestige_environment_and_special_ability_trees_catalog.csv` | 1,018 | 58 | ragged row widths |
| `species_elementalist_and_innate_abilities_catalog.csv` | 2,203 | 58 | ragged row widths |
| `ability_trees_and_abilities_catalog.csv` | 1,256 | 58 | ragged row widths |
| `expanded_living_spellbooks_and_magic_charge_holders_all_genres.csv` | 1,501 | 60 | none detected |
| `completed_magic_spells_catalog.csv` | 385 | 53 | none detected |
| `expanded_hazards_and_traps_all_genres.csv` | 1,901 | 87 | ragged row widths |
| `expanded_mecha_and_components_all_genres.csv` | 2,117 | 88 | ragged row widths |
| `expanded_spacecraft_and_components_all_genres.csv` | 2,311 | 72 | none detected |
| `expanded_land_sea_air_vehicles_all_genres.csv` | 1,200 | 61 | none detected |
| `expanded_computers_all_genres.csv` | 1,000 | 47 | none detected |
| `expanded_bases_facilities_materials_and_homesteads_all_genres.csv` | 1,080 | 40 | none detected |
| `expanded_symbiotes_and_cybernetics_all_genres.csv` | 572 | 36 | none detected |
| `expanded_eva_suits_and_modules_all_genres.csv` | 430 | 29 | none detected |
| `expanded_magitech_items_all_genres.csv` | 532 | 23 | none detected |
| `expanded_items_all_genres.csv` | 761 | 16 | none detected |
| `expanded_melee_weapons_all_genres.csv` | 327 | 15 | none detected |
| `expanded_ranged_weapons_catalog.csv` | 230 | 15 | none detected |
| `weapons_and_ammo.csv` | 36 | 10 | none detected |

## Initial disposition

All 20 datasets are provisionally **usable after governed normalization**. This does not certify their semantic accuracy, source fidelity, completeness, or canonical identity.

The five ability/hazard/mecha datasets with ragged rows require explicit recovery rules before mapping. Rows wider than the declared header must not be silently truncated. The audit detected no exact duplicate full rows, but repeated names and source names remain expected collision signals and must be resolved by the cross-file identity index rather than automatically merged.

## Required intake rules

1. Preserve `Csv.zip` unchanged as the immutable intake source.
2. Record archive and per-file hashes.
3. Treat CSV values as structured claims requiring provenance and mapping classification.
4. Distinguish direct values, deterministic normalization, inferred classification, unresolved values, and unsupported fields.
5. Do not silently truncate ragged rows, merge duplicate names, fill missing values, normalize contradictory mechanics, or promote records.
6. Use PDFs and rendered pages for ambiguous, mechanically incomplete, conflicting, or visually encoded fields.
7. Keep facilities, services, effects, actions, modifications, software, materials, creatures, and artificial beings routed to their proper object families.

## Next executable action

Build the governed **CSV Source Registry and Template-Coverage Matrix**. It must route each dataset to canonical domains, measure field coverage against current registries, identify required template additions, and define the first deterministic column-to-canonical mapping contracts for a bounded item pilot.
