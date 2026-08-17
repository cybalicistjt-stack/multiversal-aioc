# Item Corpus Taxonomy Coverage Audit

**Work item:** `ITEM-CORPUS-AUDIT-001`  
**Status:** CONSTRUCTION EVIDENCE COMPLETE — VALIDATION / GOVERNED CONTINUITY PENDING  
**Owner:** John Brandon Turner  
**Audit branch:** `governance/item-corpus-taxonomy-coverage-audit`

## 1. Question answered

Did the later **Multiversal Item Taxonomy & Catalog System v0.12.0** get applied across the actual governed Item CSV corpus?

**Canonical-evidence answer: no corpus-wide governed adoption is verified.**

What *is* verified:

- the nine direct Item-domain CSV datasets contain exactly **5,389 governed rows**;
- the v0.12.0 preparation package designed a substantially richer Item/catalog system;
- that preparation performed a read-only whole-corpus preview and created migration/enrichment plans;
- STAGE-A-A8 later implemented bounded runtime/catalog seams needed to avoid future redesign;
- A8 explicitly did **not** reconstruct the checksum-bound 241-value Content Context registry;
- no canonical application artifact was located that records IA-I4 projection of all 5,389 rows, IA-I7/IA-I8 governed row-level adoption, or IA-I11 processing of the 5,443 enrichment work items.

Therefore **0 / 5,389 rows may currently be claimed as fully governed v0.12.0-adopted from repository evidence**. This is a verified-adoption evidence count, not a claim that no exploratory/off-repository work ever occurred.

## 2. Authority

Implementation status is determined from current GitHub repository evidence. The retained source archive is used only to verify the exact source corpus.

Key authorities:

- `governance/application-planning/parallel-preimplementation/PPIA-03_SOURCE_AND_DESIGN_INVENTORY.md`
- `governance/application-planning/stage-a-a8/supplemental-authority/source-extracts/item/IA_ITEM_INTEGRATION_HANDOFF.md`
- `governance/application-planning/stage-a-a8/supplemental-authority/source-extracts/item/IA_ITEM_MIGRATION_SEQUENCE.csv`
- `governance/application-planning/stage-a-a8/supplemental-authority/source-extracts/item/INTRINSIC_AFFINITY_COMPATIBILITY_SYSTEM.md`
- `governance/application-planning/stage-a-a8/supplemental-authority/STAGE_A_A8_SUPPLEMENTAL_AUTHORITY_RECONCILIATION.md`
- `Multiversal-app/database/migrations/0006_a8_asset_foundations.json`
- `Multiversal-app/packages/contracts/src/entity-catalog/*`
- `Multiversal-app/receipts/STAGE-A-A8-CLOSURE.json`

Exact preparation archive identity:

`Multiversal_IA_Item_Taxonomy_Preparation_v0.12.0.zip`  
SHA-256: `d12feab1375930e1ef5c121d485aee8622f2abfc34c05f23babb26a293ee47ca`

Exact retained portable source snapshot used for this source audit:

`MV_Master_01_Core.zip`  
SHA-256: `c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec`

## 3. Exact Item corpus

| Governed dataset | Retained source file | Rows |
|---|---|---:|
| `expanded_melee_weapons_all_genres.csv` | `Melee_Weapons.csv` | 327 |
| `expanded_ranged_weapons_catalog.csv` | `Ranged_Weapons.csv` | 230 |
| `weapons_and_ammo.csv` | `Weapons_Ammo.csv` | 36 |
| `expanded_items_all_genres.csv` | `Items.csv` | 761 |
| `expanded_magitech_items_all_genres.csv` | `Magitech_Items.csv` | 532 |
| `expanded_eva_suits_and_modules_all_genres.csv` | `EVA_Suits.csv` | 430 |
| `expanded_computers_all_genres.csv` | `Computers.csv` | 1,000 |
| `expanded_living_spellbooks_and_magic_charge_holders_all_genres.csv` | `Living_Spellbooks.csv` | 1,501 |
| `expanded_symbiotes_and_cybernetics_all_genres.csv` | `Symbiotes_Cybernetics.csv` | 572 |
| **Total** |  | **5,389** |

The two mixed-domain adjunct datasets identified by PPIA-03 remain outside this direct-row total and must not be counted wholesale as personal Items.

## 4. Source-corpus facts established by exact-byte read-only audit

Across all 5,389 direct rows:

- explicit source ID field populated: **2,501**
- category-like field populated: **5,353**
- subcategory-like field populated: **4,796**
- technology/tier-like field populated: **5,353**
- rarity populated: **4,796**
- origin/source-like field populated: **5,361**
- `All Genres` source signal: **63**
- specific Genre source signal: **5,060**
- no Genre value: **266**

Identity warning surface:

- normalized names: **5,325 unique**
- names occurring more than once: **55**
- rows participating in repeated names: **119**
- extra rows beyond one-per-normalized-name: **64**

These are **review signals, not duplicate identities**. Same-name rows may be valid variants, source overlaps, reference-only records, conflicting source contexts, or distinct products. Automatic name merging remains prohibited.

The largest cross-dataset same-name review surfaces are:

- ranged weapons ↔ weapons/ammo: 34 names
- general Items ↔ ranged weapons: 15
- general Items ↔ weapons/ammo: 8
- general Items ↔ melee weapons: 7

The known Taser conflict, source-unspecified energy capacities, and ammo-reference-only weapon-name guardrails remain controlling examples of why name or field-shape similarity cannot become automatic canonical promotion.

## 5. What v0.12.0 actually prepared

The later Item preparation package is explicitly marked **COMPLETE FOR SHELVING / NOT PRODUCTION-INTEGRATED**.

It prepared:

- **10** independent universal Item taxonomy axes / **171** controlled values;
- **9** shared setting/content facets / **241** controlled values;
- intrinsic vs affinity vs contextual compatibility semantics;
- product identity from generic concepts through family/line/model/variant/configuration;
- shared Creator / brand / culture / origin relations;
- source/current crosswalks and provenance recovery;
- **35** coverage domains;
- **28** composable coverage profiles;
- **980** qualitative profile expectation rows;
- **1,050** current-linked source-provenance occurrences;
- **55** recovered Armor/Materials source concepts;
- **54** missing concepts requiring future current-rule builds;
- a **5,443-work-item** enrichment/re-mechanization queue.

The package's own migration sequence reserved the actual whole-corpus work for later implementation:

- IA-I4: shadow-project **all 5,389 current records**;
- IA-I7: governed taxonomy/facet adoption;
- IA-I8: governed product/creator/origin adoption;
- IA-I9: compatibility activation;
- IA-I10: coverage-profile read surfaces;
- IA-I11: process all **5,443** enrichment work items;
- IA-I12: integrate governed definitions with A8 runtime references.

## 6. What A8 implemented versus what it did not

STAGE-A-A8 is genuinely `completed_verified`, but its purpose was the bounded Inventory/Equipment/Crafting/Vehicle runtime slice and the future-proof seams approved by A8-R0.

A8 implemented contracts for, among other things:

- Product Identity;
- Creator / Origin;
- Content Context references;
- Compatibility evaluation;
- product lineage;
- market-context metadata;
- source-state / re-mechanization references;
- reusable Definition versus live Asset Instance separation.

A8 migration `0006_a8_asset_foundations.json` creates five logical/provider-neutral runtime/reference tables. It does **not** seed the complete Item taxonomy/catalog corpus. The migration explicitly states that the checksum-bound **241-value Content Context registry is not embedded or reconstructed**.

The Content Context contract likewise declares:

`registryAuthority: "checksum-bound-item-v0.12.0"` and `registryValuesEmbedded: false`.

That is deliberate future-proofing, not row-level adoption.

## 7. Prepared migration phase assessment

| Phase | Audit assessment |
|---|---|
| IA-I0 | **Partial / reconciled authority.** A8-R0 authorized/adopted bounded seams, not the complete end-to-end Item migration. |
| IA-I1 | **Not verified.** No immutable 5,389-row pre-migration snapshot receipt located in current app evidence. |
| IA-I2 | **Partial bounded seams only.** A8 has catalog/provenance reference structures, not the complete prepared metadata persistence. |
| IA-I3 | **Not implemented as prepared.** Full controlled registries/profile seeds are not embedded. |
| IA-I4 | **Not verified.** No all-5,389 shadow projection artifact located. |
| IA-I5 | **Not verified.** No declared 1,050/55/54 evidence-and-build queue import located. |
| IA-I6 | **Partial contract validation only.** A8 validates seams, not a 5,389-record projection/behavior-diff corpus. |
| IA-I7 | **Not verified.** No governed row-level taxonomy/facet adoption ledger located. |
| IA-I8 | **Contracts exist; corpus adoption not verified.** |
| IA-I9 | **Generic evaluator exists; corpus activation not verified.** The preparation explicitly records no final per-row compatibility determination. |
| IA-I10 | **Not verified.** No prepared 28-profile/980-expectation application artifact located. |
| IA-I11 | **Not verified.** No evidence all 5,443 enrichment/re-mechanization work items were processed. |
| IA-I12 | **Bounded A8 runtime seam only.** Full prepared definition-link sequence prerequisite IA-I11 is not verified. |

## 8. Coverage verdict

There are three different percentages and they must not be confused:

1. **Source-corpus accounting:** **5,389 / 5,389 = 100%**.
2. **Read-only preparation Genre preview:** **5,389 / 5,389 = 100%**.
3. **Verified complete v0.12.0 governed taxonomy adoption:** **0 / 5,389 claimable from canonical evidence**.

That third number is the gap this work item exists to close.

## 9. Row-accounting evidence

A private working ledger was generated from the exact retained CSV bytes:

`ITEM_CORPUS_ROW_ACCOUNTING_LEDGER_v0.1.0.csv`

- rows: **5,389**
- SHA-256: `5db3c2f3cfd1ff4f0b46aae1853588d7acf0b2dbbbd921a4d7c1bf58dc80cfc0`
- public repository publication: **NO**

The ledger stores source dataset/row identity, source-row fingerprint, field-presence signals, Genre-source-signal class, duplicate-name review flags, and explicit `not_verified_projected` / `not_verified_adopted` states. It intentionally does not publish source item names/content to the public AIOC repository.

## 10. Required next operation

Do **not** start by editing the original CSVs.

The next content operation is an IA-I4-style **shadow projection**:

1. recover the exact v0.12.0 controlled registries and crosswalks;
2. bind every one of the 5,389 source rows to an immutable source-row fingerprint and stable derived working identity;
3. populate only deterministic mappings supported by the exact prepared registry/crosswalk;
4. preserve unknown/unmapped values explicitly;
5. route supporting records and cross-domain records rather than forcing every row into one Item Definition shape;
6. queue repeated-name/variant/conflict cases for review rather than merging them;
7. produce a 100%-accounted projection result;
8. validate source hashes, row counts, identity preservation, no-mechanics mutation and no unsupported taxonomy invention;
9. only then begin governed IA-I7/IA-I8 adoption batches.

## 11. Current blocker to full row-level projection

The exact `Multiversal_IA_Item_Taxonomy_Preparation_v0.12.0.zip` archive bytes are checksum-bound in canonical governance but are **not present in the currently retained project-source files available to this audit**. Repository extracts preserve the integration contract, migration sequence, compatibility contract and A8 boundaries, but not the complete 171-value taxonomy registry and all row crosswalk artifacts.

Therefore this audit can establish the integration gap with high confidence, and it can account for all 5,389 source rows, but it must **not reconstruct the missing controlled vocabulary/crosswalks from memory or inference**.

The correct continuation is to recover the exact v0.12.0 package from the prior owner artifact set or another checksum-verifiable copy, verify its SHA-256, and then execute the shadow projection.
