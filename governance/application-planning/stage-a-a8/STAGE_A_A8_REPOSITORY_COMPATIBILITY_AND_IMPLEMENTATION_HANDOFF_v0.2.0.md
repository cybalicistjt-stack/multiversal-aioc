# STAGE-A-A8 Inventory, Equipment, Crafting, and Vehicles — Repository Compatibility + Implementation Handoff v0.2.0

**Status:** REPOSITORY COMPATIBILITY COMPLETE — A8 NOT ACTIVATED  
**Application baseline:** `cybalicistjt-stack/Multiversal-app` main `dced7f92163050690c807c1fda937146bb8dce85`  
**Current application sequence:** A2 remains current; A3–A8 are not activated  
**Owner/final authority:** John Brandon Turner

## Prepared package

`STAGE_A_A8_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`

SHA-256: `985319ccbf6f41655a94fbc0e4a1cb1af65c23547cf3a8d0df0ab6433d149bdf`

Nested preimplementation package:

`STAGE_A_A8_INVENTORY_CRAFTING_VEHICLES_PREIMPLEMENTATION_v0.1.0.zip`

Nested SHA-256: `692bae390c47dffc3d6104739fc9a7cb4087a3226b115612bea0ac02cc0a4af6`

Validator result:

`STAGE-A-A8 REPOSITORY COMPATIBILITY + CONTRACTS v0.2.0: PASS`

Validated dimensions:

- 27 current repository/predecessor anchors;
- 22 blocking compatibility gaps/risks;
- 8 owning-domain/cross-domain boundary decisions;
- 24 planned provider-neutral contracts;
- 55 exact future repository path actions across all 16 `AST-S01`–`AST-S08` and `VEH-S01`–`VEH-S08` source slices;
- 19 explicit foundation reuse/composition decisions;
- 25 blocking validation/CI lanes.

## Compatibility verdict

`COMPATIBLE_WITH_SPLIT_D17_D27_A8_CONTRACTS_AND_ADDITIVE_PERSISTENCE`

The application repository already contains the correct architectural foundation but no A8 runtime implementation.

Existing foundations include:

- canonical D17 `inventory-equipment` boundary;
- canonical D27 `shared-assets` boundary for vehicles/mecha/ships;
- D04 `authority-control` boundary;
- D26 `downtime-projects` boundary;
- provider-neutral expected-version persistence and transactions;
- immutable migration registry baseline;
- Campaign authorization and entitlement contracts;
- Session command/Event/realtime/reconnect foundations;
- backup/restore/export and privacy-bounded observability;
- A1 client/UI foundation.

The D17 and D27 public contract/schema/fixture/golden-test roots are currently placeholders and contain no A8 runtime model.

## Critical repository rule — no monolithic A8 Asset source of truth

The canonical application-domain catalog separates:

- **D17 — Inventory & Equipment**;
- **D27 — Shared Assets, Vehicles, Mecha & Ships**.

Their repository boundary files prohibit direct imports of another domain's persistence and direct cross-domain storage tables.

Therefore A8 implementation must preserve one authoritative owning domain for every record and communicate across boundaries using public contracts, stable references, reservations, immutable Events and compensating operations.

Do not create one generic `packages/contracts/src/a8/**` persistence/source-of-truth layer that bypasses the canonical domain roots.

Before the first A8 migration, reconcile each F008 record class against the then-current canonical data-ownership catalog and implemented A2–A7 state. This package deliberately does not freeze a permanent physical table decomposition prematurely.

## Exact repository contract direction

Future A8 implementation is mapped primarily into:

- `packages/contracts/src/inventory-equipment/**`;
- `schemas/domains/inventory-equipment/**`;
- `fixtures/domains/inventory-equipment/**`;
- `tests/golden/domains/inventory-equipment/**`;
- `packages/contracts/src/shared-assets/**`;
- `schemas/domains/shared-assets/**`;
- `fixtures/domains/shared-assets/**`;
- `tests/golden/domains/shared-assets/**`;
- bounded `apps/client-ui/src/a8/**` composition surfaces;
- additive `database/migrations/<next>_a8_*.json` only after predecessor migrations are known.

`database/migrations/0001_initial_logical_schema.json` remains immutable.

## Frozen cross-domain boundaries

### Character and equipment

A4 remains authoritative for Character lifecycle/control and Character-owned current Resource/Condition state. A8 equipment and Asset records reference Character state through public contracts rather than duplicating Character truth.

### Action and combat

A6 remains authoritative for proposal/decision/accepted Action result. A7 remains authoritative for combat timing, targeting, semantic positioning and encounter coordination.

A8 owning domains validate and commit their own quantity/reservation/ammunition/charge/durability/Vehicle-resource writes through explicit adapters in the same ordered accepted result group.

Denied or failed-before-commit Actions consume nothing.

### Crafting and salvage

A8 owns Asset inputs, reservations, transformations, outputs, byproducts and lineage.

D26 / F018 owns long-running Project timing and research.

Asset inputs may not be consumed and outputs may not be created until the owning work order and Asset-side validation commit atomically.

### Vehicles

Basic F014 Vehicle/Mecha/Starship operation remains inside D27 shared-assets:

- profile and stable Asset identity;
- crew/stations and controller grants;
- semantic movement/navigation;
- systems, power, fuel, heat and ammunition;
- A6/A7-governed Vehicle Actions;
- damage/failure/repair;
- boarding, docking, capture, cargo/passengers and carried craft;
- recovery, hidden information, provenance and accessible operation.

Advanced construction, fleet logistics and autonomous AI command remain deferred.

## Security and inference rules

Hidden Asset existence, identity, quantity, owner, custodian, location, contents, value, restrictions, reservations, cargo, occupants, systems and routes must be removed **before** count, total, weight, capacity, value, search, notification, export, diagnostic or optional-AI aggregation.

The generic Session hidden-information filter is only a baseline and cannot serve as the final A8 aggregate-projection policy.

## Explicit nonauthorization

This package does **not**:

- activate A8;
- create an A8 application implementation branch;
- modify the application repository;
- supersede A2 as current work;
- implement A3–A7;
- resolve every F008 record's permanent physical storage before predecessor implementation;
- authorize irreversible Asset destruction;
- authorize advanced vehicle construction, fleet logistics or autonomous AI command;
- authorize canonical content promotion;
- authorize real-user data collection, production credentials, paid services, internal-alpha release, deployment, production or public release.

## Exact next preparation step

Prepare **Stage A9 — Investigation and Social Workspaces** from the completed Investigation/Clue Board, Social Interaction, Relationships/Reputation/Factions design series, preserving hidden-information and durable-consequence boundaries and keeping A9 unactivated.