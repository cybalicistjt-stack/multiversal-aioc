# CCTI Read-Only Corpus Baseline — 2026-08-17

**Work item:** CCTI-READONLY-01  
**Mode:** read-only evidence reconstruction  
**Source mutation:** none authorized

## Content Consolidation evidence

The active owner-supplied `Content Consolidation.zip` was inspected without modifying it.

- session SHA-256: `cf82636489b6a5616766e0631646591bf2e558c90ef8d4529ff04aaa153969b8`
- nested consolidation packages: 15
- Content V2 completeness/provenance corpus: 20 catalogs / 19,199 records
- record provenance profiles: 19,199
- gameplay cells classified: 970,063
- blank unclassified gameplay cells: 0

The CCTI target is the 12-catalog / 11,017-record subset covering Items plus Vehicles, Mecha, and Spacecraft.

## Target accounting

| Catalog | Rows | Canonical Definition IDs in record-provenance profile | Notes |
|---|---:|---:|---|
| Items.csv | 761 | 761 | Item corpus |
| EVA_Suits.csv | 430 | 430 | Item corpus |
| Ranged_Weapons.csv | 230 | 230 | Item corpus |
| Computers.csv | 1,000 | 1,000 | Item corpus including device/component/system types |
| Magitech_Items.csv | 532 | 532 | Item corpus |
| Symbiotes_Cybernetics.csv | 572 | 572 | Item corpus |
| Weapons_Ammo.csv | 36 | 30 | Legacy/reference-only; 30 canonical targets, 6 retained without current Definition target |
| Melee_Weapons.csv | 327 | 327 | Item corpus |
| Living_Spellbooks.csv | 1,501 | 1,501 | Spellbooks, charge holders, source modules/upgrades/rules |
| Vehicles.csv | 1,200 | 1,200 | Platform + module/support rows |
| Mecha.csv | 2,117 | 2,117 | Platform + component/rules rows |
| Spacecraft.csv | 2,311 | 2,311 | Platform + component/class-framework rows |
| **Total** | **11,017** | **11,011 current Definition targets + 6 reference-only holds** | 100% rows represented in provenance profile |

## Provenance-class distribution by target catalog

- Items.csv: 411 `MIXED_SOURCE_AND_COMPLETION`; 350 `AUTHORED_EXPANSION`.
- EVA_Suits.csv: 50 mixed; 380 authored expansion.
- Ranged_Weapons.csv: 17 mixed; 19 `SOURCE_DERIVED`; 194 authored expansion.
- Computers.csv: 100 source-derived; 900 authored expansion.
- Magitech_Items.csv: 232 mixed; 300 authored expansion.
- Symbiotes_Cybernetics.csv: 67 mixed; 505 authored expansion.
- Weapons_Ammo.csv: 36 `REFERENCE_ONLY`.
- Melee_Weapons.csv: 53 source-derived; 4 mixed; 270 authored expansion.
- Living_Spellbooks.csv: 55 mixed; 6 source-derived; 1,440 authored expansion.
- Vehicles.csv: 80 source-derived; 1,120 authored expansion.
- Mecha.csv: 137 source-derived; 1,980 authored expansion.
- Spacecraft.csv: 439 source-derived; 12 mixed; 1,860 authored expansion.

These classes are record-level provenance profiles; they do not imply that every field in a mixed/source-derived record has the same provenance.

## Platform/model routing result

The Platform v0.11.0 handoff reports 5,628 current catalog records and 2,984 current platform/model records analyzed. Existing Content V2 `Record_Type` evidence explains the exact split:

### Vehicles.csv
- 953 `Vehicle` platform/model rows.
- 239 `Vehicle Module` rows.
- 3 Support Equipment.
- 3 Consumable Supply.
- 1 Service Facility.
- 1 Service Package.

### Mecha.csv
- 900 Original Mecha.
- 30 Named Mecha.
- 1,080 Original Mecha Component.
- 87 Source Mecha Component.
- 20 Rules Framework.

Platform/model subtotal: 930.

### Spacecraft.csv
- 960 Original Spacecraft.
- 81 Named Spacecraft.
- 60 Class Archetype Spacecraft.
- 900 Original Ship Component.
- 186 Ship Component.
- 111 Class Module.
- 13 Ship Class Framework.

Platform/model subtotal: 1,101.

### Combined
- valid platform/model rows: **2,984**
- non-model platform-catalog rows requiring component/module/rules/support routing: **2,644**

This routing distinction is mandatory for later projection. A row's presence in Vehicles.csv, Mecha.csv, or Spacecraft.csv does not itself make that row a platform model.

## Existing consolidation sidecars to preserve

The fifteen-package consolidation body includes, among other governed evidence:

- stable source-record and canonical Definition identity registries;
- cross-catalog identity review and decisions;
- legacy Weapons/Ammo supersession mapping;
- cross-package resolved and unresolved relationships;
- typed normalization vocabularies, rules, aliases, normalized values, coverage, and review queues;
- field completeness-state ledgers and provenance profiles;
- deferred-candidate recovery queues and receipts;
- later world/environment/branch/empire reconciliation evidence.

CCTI must consume these sidecars instead of restarting identity/normalization/provenance work from raw CSV names.

## Exact taxonomy authority status

Canonical A8-R0 records the Item v0.12.0 and Platform v0.11.0 archive SHA-256 identities and repository text extracts. The complete exact archive bytes were not found in the active `/mnt/data` source surface during this baseline inspection.

Therefore:

- CCTI-01 reconstruction can proceed;
- platform/model versus component routing is evidenced and can proceed;
- deterministic crosswalk envelopes can proceed;
- final row-level assignment to the complete 171-value Item registry and complete Platform registry must wait for exact-byte recovery/checksum verification rather than being reconstructed from memory or partial extracts.

## No-change receipt

This baseline records read-only findings only. It does not modify any source/master CSV, identity decision, taxonomy assignment, supersession disposition, or application runtime data.
