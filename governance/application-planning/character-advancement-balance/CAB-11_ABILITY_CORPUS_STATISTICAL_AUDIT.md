# CAB-11 — Ability Corpus Statistical Audit

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-11  
**Corpus:** five retained Ability CSVs, 4,816 records total

## 1. Scope

Audit the bounded Ability corpus statistically before structural/high-risk review. This tranche does not rewrite or reprice individual records. Counts are screening evidence; source silence is not automatically an error.

## 2. Source-family census

| File | Records | Numeric Tier 1–5 records | Distinct nonblank Tree_IDs |
|---|---:|---:|---:|
| Abilities_Core.csv | 1,256 | 1,192 | 64 |
| Species_Innate_Abilities.csv | 2,203 | 1,872 | 108 |
| Magic_Faction_Abilities.csv | 118 | 74 | 10 |
| Prestige_Env_Abilities.csv | 1,018 | 569 | 80 |
| Profession_Crafting_Abilities.csv | 221 | 210 | 11 |
| **Total** | **4,816** | **3,917** | — |

The sum of file-local distinct Tree_ID counts is not a count of tiered progression groups; tree headers, collections, references, and non-tiered structures are included.

## 3. Record-type distribution

Largest record classes:

- Ability: 3,787;
- Perk: 366;
- Species Perk: 238;
- Ability Tree: 192;
- Ability Listing: 57;
- Situational Perk: 45;
- Collection / System: 42;
- Perk Collection: 22;
- smaller classes include specialization options, upgrades, proficiency levels, mastery perks, augmentations, enhancements, and references.

The corpus is therefore not a flat list of purchasable Abilities. Headers, systems, collections, listings, and upgrades must not receive invented purchase semantics merely to fill fields.

## 4. Tier distribution

Numeric Tier 1–5 rows:

- T1: 773;
- T2: 785;
- T3: 824;
- T4: 771;
- T5: 764;
- nonnumeric/nonstandard tier states: 899.

The 899 include 510 `Not specified in source`, 272 tree-level records, 60 Starter records, 26 explicitly not-tiered records, and smaller source-specific labels. CAB-11 does not force these into T1–T5.

## 5. Price coverage

Direct Ability XP:

- numeric direct XP values: 1,712 records;
- `Not specified in source`: 2,810;
- `Not applicable`: 294.

For numeric direct prices:

- minimum: 20 XP;
- 25th percentile: 387.5 XP;
- median: 700 XP;
- 75th percentile: 2,500 XP;
- 90th percentile: 5,000 XP;
- 95th percentile: 7,500 XP;
- 99th percentile: 20,000 XP;
- maximum: 50,000 XP.

Numeric direct-price medians by numeric tier are approximately T1 250, T2 700, T3 1,500, T4 3,000, T5 5,000 XP, but every tier has broad overlap and outliers. This supports CAB-05/CAB-06: tier correlates historically with price but does not determine price.

Numeric Tier Unlock XP appears in 1,338 records. Its median is 5,000 XP and maximum 30,000 XP, reflecting incompatible source ladders rather than one authoritative schedule.

## 6. Requirement and runtime-field coverage

After removing `Not specified`, `Not applicable`, `None`, and aggregate `Varies by...` placeholders where applicable, meaningful populated counts include:

- Tier prerequisites: 704;
- Ability prerequisites: 314;
- concrete Attribute requirements: 189;
- situational-perk requirements: 199;
- Action Economy: 418;
- Passive/Active: 476;
- Usage Frequency: 548;
- Resource Cost: 339;
- Duration: 830;
- Environment/Context: 657;
- Special Rules: 347;
- Scaling/Additional Bonus: 615;
- Roll Bonus/Penalty: 1,534;
- Condition: 549;
- Upgrade Effect: 402.

Sparse population is especially important for Action Economy, frequency, and Resources because CAB-07/08 balance cannot safely infer missing timing or stacking behavior.

## 7. Completion/provenance state

The corpus overwhelmingly preserves published source rather than silently authoring replacements:

- 4,464 rows: published source record, no new Ability added;
- 188: published structure indexed;
- 57: published source listing;
- 55: published tree indexed;
- smaller classes explicitly preserve partial trees, headings with missing definitions, upgrades, example-progressions, and source omissions.

This provenance discipline must survive repair.

## 8. Identity audit

### Record_ID is file-scoped, not globally unique

`Record_ID` alone is unsafe as a global canonical key. There are **1,256 duplicated ID values**, affecting **2,512 rows**, because the `ABLREC-xxxxx` namespace is reused across source files (notably Abilities_Core and Species_Innate).

CAB therefore requires a source-qualified identity during repair/migration, such as `(source_dataset, Record_ID)`, until a governed globally unique stable ID is explicitly assigned.

### Tree_ID

No cross-file Tree_ID collision was found in the bounded portable corpus.

### Exact same name/tree/tier

42 rows duplicate the same Ability_Name + Ability_Tree + Tier tuple. These require identity/provenance review, not automatic deduplication; some may be legitimate source repetitions, listings, upgrades, or reconciliation artifacts.

## 9. Statistical repair classes

CAB-11 adopts the following triage classes:

1. `identity_namespace_review` — source-qualified IDs required where local IDs collide;
2. `purchase_semantics_unresolved` — price/acquisition absent on a record that later proves purchasable;
3. `runtime_timing_unresolved` — consequential active/passive effects with missing action/frequency/duration/resource semantics;
4. `prerequisite_semantics_unresolved` — requirement text incomplete or non-machine-readable where progression depends on it;
5. `interaction_semantics_unresolved` — stacking/synergy group missing where combination materially matters;
6. `source_intentional_absence` — field absent because header/listing/grant/non-applicable source genuinely does not require it;
7. `provenance_only_gap` — source itself omits the mechanic and CAB must not fabricate it during audit.

## 10. Decision

Under the standing owner delegation, CAB-11 adopts source-qualified record identity and the seven-class statistical repair taxonomy. No individual record is automatically changed or repriced by this audit.

## 11. Successor

CAB-12 — Ability-Tree Structural Audit.