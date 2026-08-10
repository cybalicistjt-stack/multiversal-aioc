# STAGE-A-A7 Repository Compatibility + Implementation Contracts Handoff v0.2.0

**Stage:** STAGE-A-A7 — Full Combat Interface  
**Status:** PREIMPLEMENTATION ONLY — NOT ACTIVATED  
**Owner:** John Brandon Turner  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Verified app main:** `dced7f92163050690c807c1fda937146bb8dce85`  
**AIOC branch:** `governance/stage-a-a7-preimplementation`

## Prepared artifacts

- `STAGE_A_A7_FULL_COMBAT_INTERFACE_PREIMPLEMENTATION_v0.1.0.zip`
  - SHA-256: `752020c7e5f7fd328fac9ee075865fc69dbd4c425440c31697a94dc12860307a`
- `STAGE_A_A7_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`
  - SHA-256: `8bfcddd2d97c73c7dd298404dd03492313a47fc67a86ddf72286c8818cb7b6b2`

Local deterministic validation:

`STAGE-A-A7 REPOSITORY COMPATIBILITY + CONTRACTS v0.2.0: PASS`

Validated dimensions:

- 22 repository/predecessor anchors;
- 18 blocking compatibility gaps/risks;
- 20 provider-neutral A7 implementation contracts;
- 46 exact future repository path actions covering `CBT-S01` through `CBT-S08`;
- 16 explicit reuse/composition decisions;
- 20 blocking validation/CI lanes;
- nested v0.1.0 preimplementation archive CRC verified.

## Compatibility verdict

`COMPATIBLE_WITH_ADDITIVE_A7_COMBAT_CONTRACTS`

The current app already supplies the generic foundations A7 should extend rather than replace:

- Campaign authorization;
- provider-neutral persistence and transactions;
- authoritative Session command idempotency/revision checks;
- ordered realtime Event delivery and gap detection;
- hidden-information filtering;
- trusted checkpoint/reconnect restoration;
- structured privacy-bounded audit/telemetry;
- portability/recovery foundations;
- A1 React/Vite/TypeScript/Vitest/axe client foundation.

No current combat runtime, combat persistence family, combat timing engine, or reaction engine exists on app main.

## Critical repository-specific adaptations

### Generic accepted command payload

The P9 authoritative Session command handler emits a generic accepted Event with public visibility and includes the command payload. A7 combat payloads can contain hidden targets, modifiers, eligibility evidence, GM-only information and other protected combat state.

A7 must therefore wrap the P9 command-authority pattern and emit combat-specific role-safe Events. Raw hidden combat command payload may not be exposed through the generic public Event path.

### Generic hidden count

The P9 hidden-information filter authorizes before projection, but its generic projection contains `hiddenEventCount`.

F007 forbids inference of hidden targets, modifiers, topology, eligibility and protected counts. A7 may use the generic filter internally, but protected combat views, target previews, queues, notifications, exports, diagnostics and AI context must not expose hidden cardinality unless explicitly authorized by the A7 projection policy.

## Predecessor boundary

A7 remains dependency-gated and must not duplicate predecessor systems:

- A2 owns governed Action/source lookup and rule inspection;
- A3 owns subject/workspace/role/delegation context;
- A4 owns Character lifecycle/control/Resources/Conditions/version;
- A5 owns immutable launch snapshot and active Session shell;
- A6 owns Action proposal, GM review, approve/deny/modify-and-approve, decision receipt, idempotent status recovery and atomic Action acceptance.

A7 adds encounter lifecycle, participants/controllers, timing/order, targeting, semantic positioning, Resource-cost coordination, Effect/Condition adapters, reactions/interrupts, hazards/environment, defeat/withdrawal, encounter completion, combat projections and combat recovery around those foundations.

## Persistence boundary

`database/migrations/0001_initial_logical_schema.json` remains immutable.

When A7 becomes current, inspect the then-current schema after A2-A6 implementation and add the smallest provider-neutral migration required by the frozen combat record contracts. The preparation package does not prematurely freeze a physical table layout.

## Combat authority boundary

- combat is a Session-scoped authoritative state machine;
- realtime remains advisory;
- one accepted Action produces one atomic result group or none;
- reaction claims are advisory until accepted;
- each reaction slot has exactly one accepted resolution path;
- semantic zones/range/elevation/cover/occupancy control positioning, not incidental pixel/drag state;
- zero Resource value never universally means death;
- encounter completion does not itself grant Assets, XP, advancement, faction standing or canonical changes;
- AI has no Action-selection, hidden-information, decision or commit authority.

## Current-state boundary

This handoff does **not**:

- activate A7;
- create an A7 application branch;
- modify `Multiversal-app`;
- change the current Stage A pointer;
- supersede STAGE-A-A2;
- mark A3, A4, A5 or A6 implemented;
- modify the parallel Design Standards track;
- authorize irreversible Character loss, real-user data, paid providers, production credentials, Internal Alpha release, deployment, public release or canonical promotion.

## Exact next preparation item

Prepare **STAGE-A-A8 — Inventory, Equipment, Crafting, and Vehicles** from the completed IA-D06 Asset/Vehicle design series, preserving A7/A6 authority and keeping A8 unactivated.