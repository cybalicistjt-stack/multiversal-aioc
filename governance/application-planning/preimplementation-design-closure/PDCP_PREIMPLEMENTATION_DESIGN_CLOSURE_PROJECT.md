# PDCP — Preimplementation Design Closure Project

**Status:** OWNER-APPROVED — ACTIVE DESIGN PROJECT  
**Project ID:** `PDCP`  
**Approved:** 2026-09-16  
**Owner and final authority:** John Brandon Turner  
**Implementation authority:** none  
**OPS3 lane:** `content-design` when this project is the user's explicit session intent  
**Operational selector:** none; `operations/CURRENT.json` remains the only live selector

## Purpose

PDCP moves research, architecture decisions, mechanics design, state modeling, operation semantics, UX behavior, edge-case resolution and acceptance-design work **out of future product-development tranches** wherever those obligations can be completed before software implementation begins.

The objective is not to reduce capability. The objective is to reduce future roadmap execution units by arriving at governed start with implementation-ready contracts, so retained tranches contain only work that materially requires product code, schema/migration, UI construction, runtime integration, automated proof, packaging or other repository-bound implementation.

PDCP is a design/planning project, not a product family. It does not appear as an implementation node in `ROADMAP_DEPENDENCY_GRAPH.json`, does not receive an implementation branch, does not mutate canonical game/application state, and cannot grant implementation authority.

## Scope

PDCP covers the newer planned specialist/runtime wave that remains future/unstarted as of the baseline snapshot:

| Family | Baseline tranches | Design track |
|---|---:|---|
| MCS — Multiversal Cartography Studio | 21 | Specialist Creator Track |
| MCCS — Multiversal Character & Creature Studio | 21 | Specialist Creator Track |
| MNCS — Multiversal NPC & Creature Studio | 24 | Specialist Creator Track |
| MSAS — Multiversal Sound & Audio Studio | 21 | Post-MAS Runtime/Creator Track |
| MRCS — Multiversal Rules & Content Studio | 21 | Post-MAS Runtime/Creator Track |
| GPR — Gameplay Pattern Runtime & Loop Minis | 16 | Post-MAS Runtime/Creator Track |
| MERA — Multiversal Engineering, Refit & Assembly | 24 | Post-MAS Runtime/Creator Track |
| MBES — Multiversal Built Environment & Settlement | 24 | Post-MAS Runtime/Creator Track |
| MSLR — Multiversal Spatial Law Runtime | 18 | Post-MAS Runtime/Creator Track |
| MSWI — Multiversal Systemic Worldplay Integration | 18 | Post-MAS Runtime/Creator Track |

**Baseline in-scope total:** 208 planned tranches.

### Explicit exclusion

`MAS` is excluded. MAS was already in active product execution when PDCP was approved and is close to completion. PDCP must not reopen, redesign, renumber, merge, delay or otherwise interfere with MAS work.

Completed programs and already-completed tranches elsewhere are also out of scope unless a future in-scope family merely consumes their stable owner contracts.

## Design tracks

### Track A — Specialist Creator Systems

`MCS → MCCS → MNCS`

The track closes design obligations for cartography, character/creature presentation and NPC/creature generation/construction while preserving their existing owner boundaries and DAG relationships.

### Track B — Post-MAS Runtime/Creator Spine

`MSAS → MRCS → GPR → MERA → MBES → MSLR → MSWI`

MAS is a dependency/handoff context where required but is not itself a PDCP workstream.

### Cross-family capability stream

Benchmark-derived improvements are resolved into the correct existing owners rather than automatically becoming a new roadmap family. Initial capability packets are:

1. social-interaction grammar, cultural norms, indirect influence and autonomous choice;
2. systemic investigation, evidence traces, witness/record provenance and hypothesis views;
3. autonomous actors, threats, agendas, bounded resources and offscreen action;
4. semantic affordances, composable effects and material/environment response;
5. persistent history, legacy, succession, institutional memory and delayed consequences;
6. multi-resolution simulation, aggregation/refinement and autonomous world evolution;
7. creator/GM execution UX, preview/commit, intervention, debugging and live control;
8. simulation/formal validation, route coverage, constraint solving, solvability and exploit diagnostics.

Each packet must be assigned to existing owners/families wherever possible. A new implementation family requires a later explicit owner decision; PDCP may not create one by inference.

## Design Closure Package

Before a baseline tranche may be merged, absorbed or removed as a standalone implementation unit, PDCP must close the tranche's non-code obligations in a durable Design Closure Package (DCP). A DCP contains, as applicable:

1. benchmark/capability conclusions and clean-room boundaries;
2. existing-owner and authority crosswalk;
3. canonical versus proposed/projection/live-state distinctions;
4. data/state contract and identity/provenance rules;
5. operations, transitions, validation and conflict semantics;
6. resolution-depth/abstraction rules and cross-scale behavior;
7. GM/player/creator UX behavior including preview, commit and undo/recovery where relevant;
8. permission, visibility, knowledge and hidden-information behavior;
9. replay, Event attribution, recovery, versioning and migration expectations;
10. failure cases, edge cases, accessibility requirements and unsupported/unknown behavior;
11. concrete test vectors and golden scenarios with expected outcomes;
12. an implementation mapping showing exactly what repository-bound work remains and where it will execute.

Discussion alone is not closure. A DCP must be durable, internally consistent and specific enough that a future implementation tranche does not need to rediscover product semantics.

## Roadmap reduction dispositions

Every baseline tranche receives exactly one final PDCP disposition during its family reduction review:

- `RETAIN_IMPLEMENTATION` — distinct implementation work remains and warrants its own tranche.
- `MERGE_IMPLEMENTATION` — remaining implementation obligations are merged into a named surviving tranche without losing acceptance scope.
- `ABSORB_EXISTING_OWNER` — the capability is already owned/implemented elsewhere; the future family only needs a named integration/proof obligation in a surviving tranche.
- `DESIGN_CLOSED_NO_STANDALONE` — PDCP fully closes the standalone design/research work; any residual wiring/test obligations are mapped elsewhere.
- `REMOVE_DUPLICATE` — the baseline tranche duplicates another governed capability and is removed with explicit evidence and replacement coverage.
- `RETAIN_OWNER_DECISION` — a material owner decision remains, so the tranche cannot be reduced yet.

There is no predetermined reduction percentage or target count. A lower count is valid only when scope and proof are preserved.

## Reduction invariants

1. No currently selected, governed-started or in-progress product work is eligible for PDCP reduction.
2. MAS is excluded in full.
3. PDCP never grants implementation authority.
4. `operations/CURRENT.json` is never changed merely to perform PDCP design work.
5. `ROADMAP_DEPENDENCY_GRAPH.json` remains cross-program activation authority.
6. A tranche ID referenced by a DAG start/golden gate may be removed or renumbered only in the same atomic planning change that updates that gate to an equivalent surviving proof.
7. Golden proof, migration, recovery, accessibility, permission/privacy, provenance and deterministic validation obligations may not be silently deleted to reduce count.
8. Existing owner boundaries remain authoritative; PDCP prefers integration over duplicate ledgers/runtimes.
9. Research/design closure is not software completion. Future implementation status remains `planned` until OPS3 grants product authority and implementation is verified.
10. Reduction changes must be reviewable from a before/after coverage map.

## OPS3 coordination

PDCP uses existing OPS3 semantics rather than modifying them:

- `content-design` is the normal on-demand lane for PDCP design sessions.
- Explicit owner requests to integrate PDCP results into the roadmap authorize bounded planning updates, not product implementation.
- Product-development CURRENT state remains preserved while PDCP work occurs.
- When a family reduction is ready, its planning change must reconcile the family backlog, any affected DAG milestone references, program/amendment prose and control-plane tests atomically.
- A future `Continue` in a product-development conversation follows `operations/CURRENT.json`, not this project.
- This file is not a current-work selector and must never be used to override OPS3.

## Family reduction review

A family is ready for roadmap reduction only when:

- every baseline tranche has a final disposition;
- every merged/absorbed/removed tranche has a durable DCP or explicit existing-owner evidence;
- every surviving tranche has a bounded implementation-only scope;
- the family golden proof still covers the complete accepted capability set;
- cross-family dependencies and DAG gate references remain valid;
- the before/after count and scope mapping are machine-readable;
- no current OPS3 product work is disturbed.

At that point the family backlog may be amended to its reduced strict order. The reduction itself remains planning work; future implementation still requires ordinary OPS3 governed start.

## Project completion

PDCP completes when all ten in-scope families have approved reduction receipts and the effective future roadmap has been reconciled to those receipts, with no capability loss and no unauthorized product start.

The baseline count of 208 is historical provenance. The final reduced count is intentionally unknown until the design work proves what can safely collapse.
