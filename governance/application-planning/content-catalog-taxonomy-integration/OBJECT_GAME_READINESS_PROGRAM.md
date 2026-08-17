# Multiversal Object Game-Readiness Program

**Program ID:** OGR  
**Owner:** John Brandon Turner  
**Status:** OWNER-APPROVED DIRECTION / TRANCHE 1 ACTIVE  
**Started:** 2026-08-17  
**Dependency:** CCTI modern catalog/taxonomy integration

## Purpose

Move the governed Item, Vehicle, Mecha, Spacecraft and supporting-object corpus from catalog-complete content to genuinely game-ready content without flattening unlike record types into a single object model.

OGR is downstream of CCTI. Taxonomy/catalog integration establishes what each record is, its identity/provenance, context, product/creator/lineage and relationships. OGR then proves whether that record has the descriptive content, mechanics, runtime behavior, validation and playtest evidence needed for its actual game role.

A taxonomy-complete record is not automatically game-ready. A record is game-ready only after every dimension required by its route-specific readiness profile has passed.

## Corpus boundary

Current CCTI corpus: **11,017 source rows**.

- 5,389 Item-corpus rows, including 36 legacy/reference-only Weapons/Ammo rows.
- 5,628 Vehicle/Mecha/Spacecraft-domain rows.
- 2,984 of those Platform-domain rows are models, named assets or archetypes.
- 2,644 are components, modules, rules/support, equipment/supplies or services and must be certified under those roles rather than as standalone platform models.

The current corpus contains 11,011 rows with current Definition targets plus six deliberate reference-only holds. Identity multiplicity/aliases/supersession mean source-row count is not itself a count of distinct playable object identities.

## Core readiness dimensions

1. **Identity & provenance** — stable identity, source ancestry, aliases/supersession and no unresolved identity conflict.
2. **Taxonomy & classification** — correct current taxonomy/domain routing, controlled values and explicit unresolved state.
3. **Descriptive metadata** — enough name/description/use/context metadata for GM/player comprehension; unknowns remain explicit.
4. **Context & compatibility** — intrinsic requirements, affinity/context and compatibility are valid where applicable; compatibility stays distinct from legality, rarity, availability and price.
5. **Relationships & lineage** — required parentage, ammunition/power/component/host/product/creator/lineage relationships are canonical or explicitly unresolved.
6. **Mechanics** — current-rule effects, resources, limits, durability/repair/consumption and domain mechanics are complete enough for the record role.
7. **Runtime behavior** — applicable operations are bound to existing A8/F014/etc. authority without duplicating Definition and Instance state.
8. **Validation** — schema, references, provenance, permissions, save/load/offline/pack and domain regressions pass where applicable.
9. **Playtest** — focused or cohort playtest evidence exists for novel/high-risk behavior; routine records may inherit validated cohort evidence when the profile permits it.

## Route-specific certification

OGR does not require the same checklist from every row.

- `ITEM_DEFINITION`: reusable Item Definition; A8 owns live instances, ownership, quantity, equipped state, damage, repair and consumption.
- `PLATFORM_MODEL`: reusable Vehicle/Mecha/Spacecraft design; individual asset history remains separate.
- `PLATFORM_NAMED_ASSET_DEFINITION`: named/specific catalog definition whose runtime instantiation must still respect model-vs-instance boundaries.
- `PLATFORM_ARCHETYPE`: class/archetype exemplar; runtime instantiation may be non-applicable unless separately governed.
- `PLATFORM_COMPONENT` / `PLATFORM_MODULE`: requires host/compatibility/install mechanics but is not itself a full platform.
- `RULES_SUPPORT`: rules/framework content; no fake runtime object is required.
- `SUPPORT_EQUIPMENT` / `SUPPORT_CONSUMABLE`: cross-domain equipment/supply certification.
- `SERVICE_FACILITY` / `SERVICE_PACKAGE`: service/economy/support certification; not an owned platform by default.
- `LEGACY_REFERENCE`: provenance/supersession evidence only; never promoted merely to satisfy a readiness percentage.

The machine-readable route/dimension requirements live in `OBJECT_GAME_READINESS_PROFILE_MATRIX.csv`.

## Program sequence

### OGR-01 — Readiness schema and baseline

Create the state registry, dimension registry, route profiles, deterministic ledger schema and one-row-per-corpus baseline. Do not label any current row game-ready merely because mechanics or taxonomy exists.

### OGR-02 — Complete taxonomy/catalog parity

Finish CCTI Item IAX-01 through IAX-10 assignments, Platform unresolved crosswalk review, shared context, creator/product/lineage and cross-domain relationships. Every source row receives an explicit disposition: mapped, reference-only, routed, unresolved or owner-decision required.

### OGR-03 — Descriptive-content completeness

Audit the information required to understand/use each route: descriptions, aliases, intended use, creator/origin disposition, model/variant context, source provenance and appropriate search/browse metadata. Unknown remains unknown rather than invented.

### OGR-04 — Mechanics audit

Audit current mechanics by domain and record role. Preserve current mechanics by default. Identify incomplete, inconsistent, stale, unsupported or current-rule-invalid mechanics without rewriting healthy records.

### OGR-05 — Governed re-mechanization and missing-content build

Use current domain rules and peer evidence only for records that fail OGR-04 or represent prepared missing concepts. Legacy/source numeric mechanics remain non-authoritative provenance. The Item preparation's 54 missing Armor/Materials concepts and the Platform preparation's bounded re-mechanization queue enter here.

### OGR-06 — Cross-object functional graph

Resolve ammunition, power/fuel, host/interface, component/module, EVA, repair/material, upgrade, factory configuration, cargo/support, creator/manufacturer and product-lineage relationships through stable IDs. Definition compatibility never asserts current runtime installation/ownership.

### OGR-07 — Runtime contract certification

For applicable records, prove acquire/equip/install/uninstall/use/consume/reload/recharge/repair/modify/craft/salvage/transfer/damage/destroy/restore/crew/operate/dock/launch behavior through existing runtime authorities. Keep Definition and Instance state separate.

### OGR-08 — GM/player usability

Expose validated taxonomy/search/filter/inspector/compatibility/product/creator/lineage/crafting/repair and authoring surfaces through existing UI authorities. This stage does not invent a competing object system.

### OGR-09 — Automated validation and playtest cohorts

Run deterministic corpus checks and representative cohort tests. Concentrate direct human testing on novel mechanics, outliers, high-impact objects and unresolved edge cases instead of manually testing 11,017 rows one by one.

### OGR-10 — Game-ready certification

Issue route-specific machine-readable certification only when all required dimensions pass. Valid terminal dispositions include `GAME_READY`, `GAME_READY_COMPONENT`, `GAME_READY_SUPPORT`, `REFERENCE_ONLY`, and `REVIEW_REQUIRED`; unresolved records are not hidden to improve percentages.

## Current evidence and starting point

- Item v0.12.0 says all **5,389/5,389** current Item records have minimum domain-defining mechanics/effect fields. This is a mechanics-presence baseline, not a full OGR mechanics certification.
- Item v0.12.0 retains a **5,443-item enrichment/re-mechanization queue**, including **54** recovered Armor/Materials concepts absent from current catalogs that require future current-rule construction.
- Platform v0.11.0 inventories **5,628** current catalog records and analyzes **2,984** platform/model rows. Its bounded re-mechanization queue contains **326** items: 244 future candidates, 81 current-ancestry reconciliations and one identity hold.
- Platform v0.11.0 assesses 221 current catalog fields for individual-asset state and finds zero that should be reinterpreted as instantiated asset state.

These facts make OGR a targeted completion/audit problem rather than an 11,017-object rewrite.

## Tranche 1 boundary

OGR-01 is authorized now alongside CCTI write-sidecar work. The initial ledger is a measurement/control artifact only. It does not authorize source/master CSV rewrites, automatic mechanics changes, runtime asset creation, release/deployment, or public publication.

Before OGR-05 mechanics mutation begins, present the concrete failing mechanics cohorts and proposed current-rule repair policy to the owner. Before OGR-07 runtime mutations or OGR-08 app-facing enablement, preserve the existing Stage A owner gates.
