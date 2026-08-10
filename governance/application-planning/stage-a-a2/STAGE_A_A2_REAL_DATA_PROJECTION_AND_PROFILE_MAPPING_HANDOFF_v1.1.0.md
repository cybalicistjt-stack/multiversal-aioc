# STAGE-A-A2 Real-Data Projection and Profile Mapping Handoff v1.1.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Status:** pre-implementation mapping complete for the active source surface; A2 implementation not started by this handoff  
**AIOC branch:** `governance/stage-a-a2-detailed-design`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Owner/final authority:** John Brandon Turner

## Owner-visible package

`STAGE_A_A2_REAL_DATA_PROJECTION_AND_PROFILE_MAPPING_v1.1.0.zip`

SHA-256:

`b78c42e5d69ff55a63ff94cc1dbe27901b0d6ed4bb82f63eaa7a3ecdc18a5d22`

This package is an implementation addendum to `STAGE_A_A2_PREIMPLEMENTATION_EXECUTION_PACKAGE_v1.0.0`. It removes the largest remaining source-adapter/profile ambiguity using the current Batch 8E portable release and retained canonical project sources without fabricating the unavailable 8D-002 catalog.

## Verified coverage

- Batch 8E portable release objects: **11,861**;
- current objects with implementation-ready explicit/profile-supported binding: **11,776 (99.2834%)**;
- current objects deliberately retained on Generic fallback pending explicit profile promotion: **85**;
- current `Domain + Object_Type` pairs: **30**;
- Master Content Definition family prefixes: **10**;
- profile registry rows: **46**;
- release catalog inventory rows: **241**;
- projection-bearing CSVs: **148**;
- unique projection source schemas: **85**;
- source-field routing rows: **1,897**;
- open mapping/coverage gaps: **5**;
- canonical 245-kind completeness claim: **NOT ALLOWED**.

## Critical implementation binding rule

A2 must not use unqualified `Object_Type`, display names, aliases, file names, or parsed stable-ID prefixes to determine presentation profile.

Use a domain-qualified mapping key. For `Master Content::Definition`, join the governed object ID to `CANONICAL_DEFINITION_IDENTITIES_v1.1.0.csv` and use the recorded `Definition_Family_Prefix`. The `DEF-*` textual prefix is data, not a UI/presentation parsing convention.

This rule prevents real current-source collisions such as:

- `Ability/Spell::Enhancement` versus older unqualified Item-like Enhancement mapping;
- `Ability/Spell::Augmentation` versus Master Content augmentation content;
- `Ability/Spell::Upgrade` versus Master Content `Definition::UPG`.

## Master Content binding state

Current governed Definition family metadata is dispositioned as follows:

- `ITM`, `WPN`, `MAG`, `EVA`, `AUG`, `UPG`, `MAT` → Item profile where explicitly supported by the approved A2 seed;
- `BASE` → Facility profile through the explicit A2 seed;
- `FAC` → Facility profile through the direct approved screen profile/source shape;
- `CMP` → Generic pending explicit catalog/profile authority.

The Bases/Facilities source remains polymorphic. The file itself must never be globally treated as Facility.

## Ability/Spell binding state

Most current Ability/Spell types have explicit implementation-ready Ability or Pack bindings. The following source-supported mechanics remain non-promoted proposed bindings and must resolve through Generic until authoritative profile promotion:

- Specialization Option;
- Upgrade;
- Advancement Rank;
- Proficiency Level;
- Enhancement;
- Augmentation;
- Unique Facility.

Do not infer an Ability profile merely from a `DEF-ABL-*` style identifier.

## Source-only diagnostic bindings

Real source-only/noncanonical shapes may use specialized visual profiles for parser/UI acceptance while retaining **NO authoritative Picker receipt**:

- Computer → Item;
- Living Spellbook → Item;
- Vehicle → Vehicle;
- Mecha → Vehicle;
- Spacecraft → Vehicle;
- Hazard/Trap → Hazard;
- legacy Weapons/Ammo → Item.

Source-local IDs must not be promoted to governed Definition IDs by A2.

## Exhaustive source-field routing

Every field in every projection-bearing source schema on the active Batch 8E release surface has one explicit routing row in `A2_SOURCE_FIELD_TO_PROJECTION_MAP_v1.1.0.csv`. Routing targets include summary display/aliases/signature/description, detail fields, relationship projection, provenance projection, validation metadata, and identity/join-only behavior.

The no-loss rule is mandatory: a safely available structured field that is not yet semantically mapped must remain available as `unmappedFields`/`unknown_structured` or provenance/validation material; it must not silently disappear.

Child feature/property/choice/section rows do not become independent top-level Definitions unless a governed identity registry explicitly establishes that identity.

## Identity, relationship and provenance boundaries

- display names and aliases never merge identities;
- duplicate names remain distinct stable-ID objects;
- unresolved raw relationship targets remain unresolved and are not given fabricated clickable IDs;
- source-backed correction overlays may alter effective fields only where their correction ledger authorizes it, while original values remain provenance evidence;
- authored expansions remain visibly authored;
- inferred completion remains distinguishable from direct extraction;
- authorization/entitlement/redaction occurs before result counts, suggestions, relationships, provenance fragments or Picker projection;
- a presentation-profile binding never grants Picker authority by itself.

## 8D-002 / 245-kind authority boundary

The current Development Bible states that 8D-002 is authoritative for canonical object kinds and 8D-003 supplies contracts for all 245 catalog objects. The retained DB-004 source registry proves that `Multiversal_8D-002_Master_Game_Object_Catalog_v0.1.0` existed as an approved/validated Phase 8 package with 19 files and 883,450 uncompressed bytes.

The exact 8D-002 package/catalog rows are not available on the active retained source surface inspected for this tranche and were not recovered from the current canonical repositories. Historical COS material is supporting classification evidence only and is not substituted for the missing canonical catalog.

Therefore this package deliberately does **not** fabricate or claim an exhaustive 245-kind registry. Unknown/unrecovered kinds continue through `P-A2-GENERIC` until the exact catalog is recovered or a separately governed mapping is approved.

## Gap ledger

1. `A2-MAP-GAP-001` — exact canonical 8D-002 catalog unavailable; blocks 245-kind completeness claim.
2. `A2-MAP-GAP-002` — Master Content `CMP` profile ambiguity; use Generic.
3. `A2-MAP-GAP-003` — Enhancement/Augmentation domain-label collision; domain-qualified lookup required.
4. `A2-MAP-GAP-004` — several Ability/Spell subtypes lack explicit profile authority; use Generic until promoted.
5. `A2-MAP-GAP-005` — genuine `Owner Corrected` real-data acceptance record remains unavailable; do not synthesize.

## Codex integration

Before A2-01 implementation, Sunday Codex execution must consume this package in addition to the v1.0.0 pre-implementation execution bundle.

Day-one assertions added by this package:

1. every current Batch 8E release object resolves either to an implementation-allowed explicit binding or `P-A2-GENERIC`;
2. no presentation code parses stable-ID prefixes;
3. `Ability/Spell::Augmentation` cannot fall through the Master Content augmentation binding;
4. `Ability/Spell::Upgrade` cannot fall through `Definition::UPG`;
5. `Master Content::Definition::CMP` stays Generic pending promotion;
6. every projection-bearing source field has a mapping row and no source field is silently dropped;
7. source-only Vehicle/Mecha/Spacecraft/Hazard records may render but cannot finalize authoritative Picker receipts.

## Validation evidence

- package validator: **PASS**;
- `release_objects=11861`;
- `binding_ready=11776`;
- `generic_fallback=85`;
- `catalogs=241`;
- `projection_csvs=148`;
- `schemas=85`;
- `field_rows=1897`;
- internal SHA256 receipt verification: **PASS**;
- outer ZIP CRC/integrity: **PASS**;
- final ZIP SHA-256: `b78c42e5d69ff55a63ff94cc1dbe27901b0d6ed4bb82f63eaa7a3ecdc18a5d22`.

## Preservation boundary

This handoff does **not** change `CURRENT_WORK_POINTER.json`, does not activate A2 application implementation, does not alter the Design Standards primary attempt, does not promote any source-only record, and does not authorize internal-alpha release, production release or deployment.

## Exact next pre-Sunday A2 operation

Build deterministic **real search/filter/ranking golden acceptance cases** against the v0.8 object corpus plus this v1.1 domain-qualified profile/source map: stable-ID exact match, duplicate-name separation, alias collisions, source/pack/type facets, authorization-safe counts and suggestions, deterministic ranking, unresolved/source-only behavior, and deep-link lookup. Produce machine-readable query fixtures and expected ordered results suitable for direct transfer into the A2-02/A2-03 implementation slices.
