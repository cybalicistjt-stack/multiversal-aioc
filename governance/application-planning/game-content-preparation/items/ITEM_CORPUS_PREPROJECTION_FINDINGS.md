# Item Corpus Preprojection Findings

**Work item:** `ITEM-CORPUS-AUDIT-001`  
**Purpose:** Preserve useful work completed before the exact v0.12.0 controlled registries are recovered. Nothing in this document assigns v0.12.0 taxonomy values.

## 1. Identity anchors are stronger than first assumed

The exact 5,389-row source corpus contains **2,501 explicit source IDs and all 2,501 are unique**.

That leaves **2,888 rows without an explicit source ID**. Of those:

- **2,771** have a normalized display name that occurs only once in the direct Item corpus;
- **117** participate in a repeated normalized-name group.

This materially improves the future IA-I4 projection strategy:

- preserve all existing explicit source IDs as source identity anchors;
- use source-file + row fingerprint as the immutable source coordinate for every row;
- never convert unique names into canonical IDs merely because they are unique;
- prioritize the 117 no-ID repeated-name rows for identity review.

## 2. Repeated-name identity queue

The direct corpus has:

- **55** repeated normalized-name groups;
- **119** participating rows;
- **64** extra rows beyond one row per normalized name.

A private review queue has been constructed with exact source coordinates and current-definition candidates:

`ITEM_CORPUS_IDENTITY_COLLISION_REVIEW_QUEUE_v0.1.0.csv`

- rows: **119**
- groups: **55**
- SHA-256: `522ebd2b23d3adcddf4f865a2af30df9e1de91e0b273d1e486d39c9686599f65`

It is intentionally not published because it contains detailed proprietary source-row content.

Current-definition occurrence evidence gives:

- **46** groups with one exact occurrence-anchor Definition candidate;
- **2** additional Chainsaw Bayonet mode groups with one explicit mode-reference Definition candidate requiring review;
- **7** groups with no exact current Definition evidence from this method.

No group is auto-merged.

## 3. Whole-corpus current-definition candidate crosswalk

A read-only exact-name crosswalk was also generated for all **5,389 rows** against the 8E-008G Item Definition occurrence evidence.

Private ledger:

`ITEM_CORPUS_CURRENT_DEFINITION_CANDIDATE_CROSSWALK_v0.1.0.csv`

SHA-256: `45d091c42a5493157de641246f3e2ab258a790df4b517ca3638e937835963332`

Results:

- **466** source rows have exactly one exact-normalized-anchor current Definition candidate;
- **13** have multiple exact current Definition candidates and therefore require explicit identity/consolidation review;
- **4,910** have no exact-anchor Definition evidence by this conservative method;
- **479 / 5,389** rows have at least one exact occurrence candidate.

This is **not** a taxonomy result and is **not** proof that the other 4,910 rows lack current content. It only states what can be linked through the deliberately conservative exact occurrence-anchor method.

The 13 multiple-candidate rows expose a concrete historical consolidation surface, including parallel `consumable` versus `medicine_toxin` IDs for several elixirs/potions plus parallel `consumable` versus `general_supply` IDs for rations and acid. Those identities must be reconciled by governed identity evidence, not by choosing one from the name alone.

## 4. Weapons & Ammo provenance repair

`Weapons_Ammo.csv` contains **36 rows**. Its original source-note coverage was only **8 / 36**.

The 8E-008G source-reference occurrence map was used to recover direct Item Definition provenance for **all 28 originally blank-source-note rows**, without touching the original CSV.

Derived crosswalk committed as:

`WEAPONS_AMMO_SOURCE_AND_IDENTITY_CROSSWALK_v0.1.0.csv`

Current-result accounting:

- 36 source rows;
- 28 source-note gaps recovered through 8E-008G evidence;
- 33 rows carry a current Definition or explicit mode-reference candidate;
- 31 unique current Definition IDs across those 33 rows;
- 3 rows remain source-reference-only with no current Item Definition, matching the pre-existing PPIA-03 guardrail: Energy Sniper Rifle, Plasma Carbine, Cryo Blaster;
- no v0.12.0 taxonomy assignment has been made.

## 5. Source-transformation review queue

The current source catalogs already contain explicit text showing that many rows include transformation or completion work rather than only verbatim source facts.

Across the 5,389 rows, **2,297 rows** contain one or more of the audited textual review signals. Signal counts overlap:

- `expanded design`: **1,114**
- `completed` fields/content: **1,071**
- `best judgment`: **828**
- `inferred`: **342**
- `ammo-only`: **6**
- malformed-source completion: **1**

Private review queue:

`ITEM_CORPUS_PROVENANCE_TRANSFORMATION_REVIEW_QUEUE_v0.1.0.csv`

- rows: **2,297**
- SHA-256: `15772c7609aa59ac9192254e2907c41286aa01f3426dda4abc6a8b86ffc67e11`

These are **review signals, not defects**. They matter because the future provenance model must not silently re-label an inferred or expanded current value as if it were direct legacy-source fact. Current mechanics remain protected unless a separate governed revision changes them.

## 6. Source-native classification surface

The current CSV fields are far broader and messier than a single categorical column. Before v0.12.0 normalization, the direct corpus contains:

- **375** unique category-like raw values;
- **999** unique subcategory-like raw values;
- **241** unique technology/tier-like raw values;
- **8** unique rarity raw values;
- **179** unique Genre raw values.

Private source-value inventory:

`ITEM_CORPUS_SOURCE_VALUE_REVIEW_INVENTORY_v0.1.0.csv`

- rows: **1,802 unique raw dimension values**
- SHA-256: `da12d5fad3e92afc7ea32ababd526a45ca3cbd3e3a0cc8778ffc198202c74f3f`

These 1,802 raw values are **not** the 171-value Item taxonomy or 241-value Content Context registry. They are the source vocabulary that the exact prepared crosswalk must normalize or preserve as unresolved/source-native metadata.

## 7. Mixed record shapes require routing, not forced Item promotion

Several Item-adjacent catalogs intentionally contain records that are not all the same object kind.

Examples from exact source rows:

### EVA catalog

- 360 EVA Module
- 26 Suit Interface
- 25 EVA Suit Chassis
- 10 EVA Accessory or Consumable
- 9 Customization Package

### Computer catalog

Large categories include Complete Computer, Software / Protocol, Core Component, Network Component, Control System, Expansion Module and other system/component records.

### Living Spellbook / Charge Holder catalog

- 720 Original Living Spellbook
- 720 Original Charge Holder
- 40 Source Charge Holder
- 10 Source Ability Module
- 5 Source Personality Archetype
- 4 Source Upgrade
- 1 Source Base Chassis
- 1 Source Progression Rule

### Symbiote / Cybernetics catalog

- 284 Cybernetic Implant or System
- 248 Symbiote
- 15 Symbiotech Integration
- 10 Maintenance/Bonding/Surgical Item
- 8 Cybernetic Weapon/Projector
- additional fusion, limb/replacement and external-frame records

Therefore IA-I4 must support at least:

- ordinary Item Definition projection;
- component/module projection;
- software/protocol/supporting-record routing;
- Ability/personality/progression cross-domain routing;
- source-only/reference-only records;
- unresolved identity state.

It must not force every CSV row into one universal Item Definition shape simply to obtain a 100% taxonomy number.

## 8. What is now ready before registry recovery

The following prerequisites are now materially prepared:

1. exact nine-dataset / 5,389-row source baseline;
2. immutable row-fingerprint strategy;
3. 2,501 unique explicit source identity anchors;
4. 55-group repeated-name identity review queue;
5. 5,389-row conservative current-definition candidate crosswalk;
6. 36-row Weapons & Ammo provenance/identity crosswalk;
7. provenance/transformation review queue for 2,297 rows;
8. 1,802-value source-native classification vocabulary inventory;
9. mixed-record routing requirements;
10. deterministic audit and row-accounting tooling.

The remaining hard dependency for **actual v0.12.0 taxonomy projection** is the checksum-matching preparation package containing the exact controlled registries and prepared crosswalks. Reconstructing those from these source values would defeat the purpose of the original governed preparation work.
