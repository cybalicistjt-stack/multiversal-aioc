# PPIA-01 — Exact CSV Content Quality Baseline

**Evidence run:** GitHub Actions `31491548248` — Validate PPIA-01 Content Quality  
**Evidence artifact:** `ppia-01-csv-content-quality-baseline`  
**Artifact digest:** `sha256:f378ed52ff2ae879a5cb7d84335496be9265e0da6efdb2328ea85bdea6ca3f8c`  
**Repository CSV archive SHA-256:** `2f621e71cbcf614317189c38ffe7d670ce13dd9e7ed20bdf35438377f4af061b`  
**Final registry workstream:** `8E-009L63`

## Exact baseline

- datasets: **20**
- governed/promoted registry rows: **19,199**
- high-priority explicit source-gap rows: **84**
- explicit `Not specified in source` cell occurrences: **142,173**
- rows containing governed inference/estimate language: **10,594**
- actual blank cells: **76**

The final 19,199-row reconciliation reproduced successfully before this audit. The scanner then produced the same baseline twice byte-for-byte, and tracked checkout mutation validation passed.

## High-priority source gaps

| Reason | Rows |
|---|---:|
| Published listing/source record provides no effect text | 57 |
| Published definition/heading/system is explicitly missing | 15 |
| Source explicitly omits a quantitative amount/value | 12 |
| **Total** | **84** |

By dataset:

| Dataset | High-priority rows |
|---|---:|
| `species_elementalist_and_innate_abilities_catalog.csv` | 66 |
| `magic_arcane_and_faction_ability_trees_catalog.csv` | 11 |
| `prestige_environment_and_special_ability_trees_catalog.csv` | 4 |
| `expanded_symbiotes_and_cybernetics_all_genres.csv` | 2 |
| `profession_and_crafting_ability_trees_catalog.csv` | 1 |

The exact 84-row queue is preserved in `PPIA-01_HIGH_PRIORITY_SOURCE_GAPS.csv`.

## Interpretation boundaries

### 142,173 `Not specified in source` cells

This is **not** 142,173 defects. The ability catalogs deliberately fill unstated fields with explicit source-absence markers. Many fields may be non-applicable to a particular ability. PPIA-01 must judge requirement/applicability before treating one as a repair target.

### 10,594 rows with estimates/inferences

These are also **not automatically defects**. The active owner recommendation delegation explicitly permits bounded evidence-based recommendations where the source is incomplete, provided raw source values, rationale, provenance, reversibility, and alternatives are preserved.

They form a later review queue after explicit source gaps are handled.

### 76 blank cells

All 76 structural blanks occur in `weapons_and_ammo.csv`. They require field-level review because ammunition/support rows may legitimately omit weapon-only fields.

## Per-dataset metrics

| Dataset | Rows | Source-unspecified cells | Inference/estimate rows | Missing definition | No effect text | Amount omitted | Duplicate-name groups |
|---|---:|---:|---:|---:|---:|---:|---:|
| magic/faction abilities | 118 | 3,107 | 1 | 10 | 0 | 1 | 0 |
| profession/crafting abilities | 221 | 6,015 | 0 | 1 | 0 | 0 | 4 |
| prestige/environment/special abilities | 1,018 | 29,816 | 0 | 4 | 0 | 0 | 22 |
| species/elementalist/innate abilities | 2,203 | 68,291 | 0 | 0 | 57 | 9 | 60 |
| core abilities | 1,256 | 34,944 | 0 | 0 | 0 | 0 | 44 |
| living spellbooks / charge holders | 1,501 | 0 | 1,486 | 0 | 0 | 0 | 0 |
| magic spells | 385 | 0 | 385 | 0 | 0 | 0 | 0 |
| hazards/traps | 1,901 | 0 | 900 | 0 | 0 | 0 | 0 |
| mecha/components | 2,117 | 0 | 2,087 | 0 | 0 | 0 | 0 |
| spacecraft/components | 2,311 | 0 | 2,106 | 0 | 0 | 0 | 0 |
| land/sea/air vehicles | 1,200 | 0 | 1,200 | 0 | 0 | 0 | 0 |
| computers | 1,000 | 0 | 959 | 0 | 0 | 0 | 0 |
| bases/facilities/materials/homesteads | 1,080 | 0 | 378 | 0 | 0 | 0 | 0 |
| symbiotes/cybernetics | 572 | 0 | 310 | 0 | 0 | 2 | 0 |
| EVA suits/modules | 430 | 0 | 56 | 0 | 0 | 0 | 0 |
| magitech items | 532 | 0 | 532 | 0 | 0 | 0 | 0 |
| general items | 761 | 0 | 182 | 0 | 0 | 0 | 0 |
| melee weapons | 327 | 0 | 5 | 0 | 0 | 0 | 0 |
| ranged weapons | 230 | 0 | 7 | 0 | 0 | 0 | 0 |
| weapons/ammo | 36 | 0 | 0 | 0 | 0 | 0 | 1 |

## First repair sequence

1. Reconcile the 57 source-listed abilities with no effect text against other rows and exact retained source evidence.
2. Resolve the 15 explicit missing-definition records where a fuller definition exists elsewhere; otherwise move them to the unresolved-source register.
3. Resolve the 12 explicit amount/value omissions from exact source or governed reversible recommendation where the delegation applies.
4. Review actual structural blanks in `weapons_and_ammo.csv` for applicability.
5. Only then begin the much larger inference/estimate review queue, prioritized by downstream PPIA and Stage A impact.

No content repair or source absence has been declared resolved by this baseline alone.