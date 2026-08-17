# CCTI Platform v0.11.0 Candidate Projection / Review Baseline

**Date:** 2026-08-17  
**Status:** additive candidate projection complete; canonical adoption disabled

## Exact authority

The candidate projection uses the checksum-verified `Multiversal_IA_Platform_Catalog_Preparation_v0.11.0.zip` (SHA-256 `621b498b6d0fa1b99c86a96eac7446f682c715cb576cf0803d233ec2ffe0bdb6`) and the previously verified Content V2 identity/provenance joins. No taxonomy values are invented outside the exact prepared registries.

## Corpus accounting

All **5,628/5,628** Vehicles/Mecha/Spacecraft-domain rows are projected:

- Spacecraft: **2,311** rows;
- Mecha: **2,117** rows;
- Vehicles: **1,200** rows.

The established routing is preserved exactly:

- **2,984** platform/model/named-asset/archetype rows;
- **2,644** non-model component/module/rules/support/service/consumable rows.

Platform/model routing by source:
- Spacecraft: **1,101** platform/model/named/archetype + **1,210** non-model;
- Mecha: **930** platform/model/named + **1,187** non-model;
- Vehicles: **953** platform models + **247** non-model.

## Prepared crosswalk disposition

- `PROPOSED_CROSSWALK_ONLY`: **2,677** rows;
- `REVIEW_REQUIRED`: **2,951** rows.

Every row has an exact controlled `record_scope_id`. Every Content V2 join remains `PRIMARY_ACTIVE`, and all 5,628 source `(file,id,name)` positions match the current source CSVs.

Universal/domain/acquisition/access/creator-seed ID validation produced **0 foreign IDs**.

## Important unresolved/deferred surfaces

The package intentionally does not pretend the preparation was more complete than it was. The following remain explicit:

- Genre: deferred to the shared Content Taxonomy for all 5,628 rows.
- Technology: deferred to the shared Content Taxonomy/rules boundary for all 5,628 rows.
- Physical form: controlled registry gap for all 5,628 rows.
- Production lifecycle: no reliable current source field for all 5,628 rows.
- Contextual market availability: context-dependent/unresolved for all 5,628 rows.
- Product identity signals remain preparation signals rather than resolved lineage identity decisions.
- Creator crosswalk contains proposed seeds plus explicit unresolved/placeholder/parent-unit/split cases.

These remain review/adoption work; they are not filled by guessing.

## Validation

PASS:
- 5,628/5,628 row accounting;
- 2,984/2,644 platform-vs-nonmodel routing;
- 5,628 unique source file + record ID pairs;
- exact ID/name alignment against current Spacecraft/Mecha/Vehicles CSVs;
- 5,628 Content V2 `PRIMARY_ACTIVE` identity joins;
- exact v0.11.0 universal taxonomy registry membership;
- domain-native class/scale registry membership;
- acquisition/access registry membership;
- proposed creator-seed membership;
- source/master mutation false;
- candidate enablement false;
- mechanics/runtime/game-ready state unchanged.

Private candidate projection SHA-256: `9f100be1e7fb08a35d73a62df634b0a34d7db9cdfdf795d0e5b980500adb8e9e`  
Private review queue SHA-256: `906ccb3b28e94521adcd8cf6df4237f170194c5e0968ddbf0b56094e4fd17c1a`  
Private baseline SHA-256: `dce143369be5207d684799ab574c3f4ea17fe800b4bc77d653def9183eb285df`  
Private routing summary SHA-256: `aeffbfd072cd7e998727b39f588ebc61221fccf7db47e4368129a836f3b53ac7`

Private artifact: `CCTI_Platform_v011_Candidate_Projection_20260817.zip`  
SHA-256: `24b7eb1a780008826abae382f73654a7cd600e1c5a6bc047a1a194117568fd08`

## Next bounded work

The next Platform tranche should review/adopt the exact `record_scope` + model/non-model routing as the foundation, then resolve creator/product-lineage and physical-form gaps without flattening domain-native class/scale/role mechanics. Shared Genre/Technology context remains deferred to the exact 241-value shared context system.
