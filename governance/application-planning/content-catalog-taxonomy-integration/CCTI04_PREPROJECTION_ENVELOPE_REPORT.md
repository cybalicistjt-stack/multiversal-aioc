# CCTI-04 — Deterministic Preprojection Envelope

**Mode:** read-only; zero taxonomy values assigned

A one-row-per-target private working envelope was generated for all **11,017** CCTI records. It binds existing corpus identity/provenance/normalization evidence to an analytical route without changing any source or canonical content.

## Routing result

- `ITEM_SHADOW_PROJECTION`: **5,353**
- `LEGACY_REFERENCE`: **36**
- `PLATFORM_MODEL`: **2,984**
- `PLATFORM_COMPONENT_OR_MODULE`: **2,603**
- `PLATFORM_RULE_FRAMEWORK`: **33**
- `SUPPORT_EQUIPMENT_OR_SUPPLY`: **6**
- `SERVICE_OR_FACILITY`: **2**

Total: **11,017**.

The platform non-model routes sum to **2,644**, exactly matching CCTI-01 platform routing evidence.

## Prepared-taxonomy target

- Item v0.12.0 direct shadow target: **5,353** current non-reference rows.
- Platform v0.11.0 direct model target: **2,984** rows.
- Cross-domain component route: **2,603** rows.
- Rules-domain route: **33** rows.
- Cross-domain support route: **6** rows.
- Cross-domain service/facility route: **2** rows.
- Legacy/reference-only: **36** rows.

The 36 reference rows remain part of the 5,389 Item-corpus accounting but are not treated as 36 new Item Definitions.

## Envelope fields

Each private working row records only existing/derived audit state needed before taxonomy assignment, including source-record key, catalog/local/current Definition identity, current `Record_Type`, provenance class, identity status, analytical routing class, intended prepared-taxonomy target, normalization evidence count, identity-decision count, existing resolved-relationship touch count, and projection state.

Every row is currently marked `PREPROJECTION_ONLY_NO_TAXONOMY_VALUES_ASSIGNED`.

## Integrity receipts

- private preprojection envelope SHA-256: `59921372bb7fffe0a6491a2dc8a01d3a022fff0c8d633cbd15dbe6a70ad1d6ee`
- aggregate envelope metrics SHA-256: `d5a5bf61d7cdb50c1920dbdd259d1a02cc3884990169a239fe06792d08dcc6ee`
- source/master rows modified: **0**
- taxonomy values assigned: **0**

The full private working ledger is deliberately not copied into the public governance repository during this read-only tranche.

## Blocking prerequisite for CCTI-05/CCTI-06 value assignment

The envelope can route records now, but exact controlled taxonomy values must wait for recovery and checksum verification of the complete Item v0.12.0 and Platform v0.11.0 preparation archives. Partial extracts are insufficient for deterministic registry-complete assignment.
