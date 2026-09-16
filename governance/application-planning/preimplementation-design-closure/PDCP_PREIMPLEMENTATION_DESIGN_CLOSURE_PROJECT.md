# PDCP — Preimplementation Design Closure Project

**Status:** OWNER-APPROVED — ACTIVE FAMILY REDUCTION PROJECT  
**Project ID:** `PDCP`  
**Approved:** 2026-09-16  
**Owner and final authority:** John Brandon Turner  
**Implementation authority:** none  
**OPS3 lane:** `content-design` when this project is the user's explicit session intent  
**Operational selector:** none; `operations/CURRENT.json` remains the only live selector

## Purpose

PDCP moves research, architecture decisions, mechanics design, state modeling, operation semantics, UX behavior, edge-case resolution and acceptance-design work **out of future product-development tranches** wherever those obligations can be completed before software implementation begins.

The objective is not to reduce capability. The objective is to reduce future roadmap execution units by arriving at governed start with implementation-ready contracts, so retained tranches contain only work that materially requires product code, schema/migration, UI construction, runtime integration, automated proof, packaging or other repository-bound implementation.

PDCP is a design/planning project, not a product family. It does not appear as an implementation node in `ROADMAP_DEPENDENCY_GRAPH.json`, does not receive product implementation authority, does not mutate canonical game/application state, and cannot grant implementation authority.

## Current phase

The eight benchmark-derived capability packets are `design_closed`. PDCP is in the **family-by-family reduction and roadmap-reconciliation phase**.

Durable control surfaces:

- `PDCP_DESIGN_CLOSURE_CONTRACT.md` — closure/reduction standard;
- `PDCP_REDUCTION_LEDGER.json` — historical baseline and approved/effective family counts;
- `PDCP_CROSS_FAMILY_OVERLAP_REGISTER.md` — mandatory intra-family/inter-family overlap and folding register;
- family-specific DCPs and `PDCP_<PROGRAM>_REDUCTION_RECEIPT.json` files.

Every family reduction must prove both intra-family overlap resolution and cross-family/shared-owner absorption before the reduced count is accepted.

## Scope

PDCP covers ten future specialist/runtime families:

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

The baseline count is immutable historical provenance. Effective counts change only through complete family reduction receipts.

### Explicit exclusion

`MAS` is excluded. PDCP must not reopen, redesign, renumber, merge, delay or otherwise interfere with MAS work.

Completed programs and already-completed tranches elsewhere are out of scope unless a future in-scope family merely consumes their stable owner contracts.

## Design tracks

### Track A — Specialist Creator Systems

`MCS → MCCS → MNCS`

### Track B — Post-MAS Runtime/Creator Spine

`MSAS → MRCS → GPR → MERA → MBES → MSLR → MSWI`

MAS is a dependency/handoff context where required but is not a PDCP workstream.

## Closed cross-family capability packets

The eight closed packets are:

1. social-interaction grammar, cultural norms, indirect influence and autonomous choice;
2. systemic investigation, evidence traces, witness/record provenance and hypothesis views;
3. autonomous actors, threats, agendas, bounded resources and offscreen action;
4. semantic affordances, composable effects and material/environment response;
5. persistent history, legacy, succession, institutional memory and delayed consequences;
6. multi-resolution simulation, aggregation/refinement and autonomous world evolution;
7. creator/GM execution UX, preview/commit, intervention, debugging and live control;
8. simulation/formal validation, route coverage, constraint solving, solvability and exploit diagnostics.

No ninth benchmark packet is implied. New benchmark insights discovered during family reduction are first mapped to existing owners and only reopen a packet/family design boundary if they expose a genuine unresolved capability.

## Design Closure Package standard

Before a baseline tranche may be merged, absorbed or removed as a standalone implementation unit, PDCP must close the tranche's non-code obligations in a durable DCP. A DCP contains, as applicable:

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

Discussion alone is not closure.

## Roadmap reduction dispositions

Every baseline tranche receives exactly one final disposition:

- `RETAIN_IMPLEMENTATION`;
- `MERGE_IMPLEMENTATION`;
- `ABSORB_EXISTING_OWNER`;
- `DESIGN_CLOSED_NO_STANDALONE`;
- `REMOVE_DUPLICATE`;
- `RETAIN_OWNER_DECISION`.

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
9. Every family must perform both an intra-family overlap audit and a cross-family/shared-owner overlap audit before its receipt can mutate count.
10. Generic engines/workflows should have one practical owner; specialist families implement only domain-specific schemas/adapters/UX/proof.
11. Prefer stable sparse IDs over gratuitous renumbering when start/golden milestone references can remain valid.
12. Research/design closure is not software completion. Future implementation status remains `planned` until OPS3 grants product authority and implementation is verified.
13. Reduction changes must be reviewable from a before/after coverage map.

## OPS3 coordination

- `content-design` is the normal on-demand lane for PDCP design sessions.
- Explicit owner requests to integrate PDCP results into the roadmap authorize bounded planning updates, not product implementation.
- Product-development CURRENT state remains preserved while PDCP work occurs.
- Family reduction changes reconcile the backlog, any affected DAG milestone references, program prose/new reduction amendment and control-plane tests atomically.
- Historical roadmap amendments remain provenance; create new reduction amendments rather than rewriting historical facts where appropriate.
- A future `Continue` in a product-development conversation follows `operations/CURRENT.json`, not this project.
- This file is not a current-work selector and must never override OPS3.

## Family reduction review

A family is ready for roadmap reduction only when:

- every baseline tranche has a final disposition;
- every merged/absorbed/removed tranche has durable DCP or explicit existing-owner evidence;
- every surviving tranche has bounded implementation-only scope;
- intra-family overlap is resolved;
- cross-family generic infrastructure is assigned to one practical owner and local work is reduced to adapters/semantics/proof;
- the family golden proof covers the complete accepted capability set;
- cross-family dependencies and DAG gate references remain valid;
- before/after count and scope mapping are machine-readable;
- no current OPS3 product work is disturbed.

## Reduction progress

Three family reductions are now resolved in planning sources.

### MSLR

- historical baseline: 18;
- surviving tranches: 9;
- removed standalone future tranches: 9;
- stable gates: `MSLR-01` / `MSLR-18`;
- DCP: `PDCP_MSLR_FAMILY_DESIGN_CLOSURE.md`;
- receipt: `PDCP_MSLR_REDUCTION_RECEIPT.json`.

### MSWI

- historical baseline: 18;
- surviving tranches: 7;
- removed standalone future tranches: 11;
- stable gates: `MSWI-01` / `MSWI-18`;
- DCP: `PDCP_MSWI_FAMILY_DESIGN_CLOSURE.md`;
- receipt: `PDCP_MSWI_REDUCTION_RECEIPT.json`.

### MBES

- historical baseline: 24;
- surviving tranches: 9;
- removed standalone future tranches: 15;
- stable gates: `MBES-01` / `MBES-24`;
- cross-owner absorbed historical tranches: `MBES-11`, `MBES-17`, `MBES-22`;
- DCP: `PDCP_MBES_FAMILY_DESIGN_CLOSURE.md`;
- receipt: `PDCP_MBES_REDUCTION_RECEIPT.json`.

**Historical PDCP baseline:** 208.  
**Current effective future count after three family receipts:** 173.  
**Standalone future tranches removed so far:** 35.

The next selected PDCP family review is **MERA**, followed by the overlap-aware reverse-consumer order in `PDCP_CROSS_FAMILY_OVERLAP_REGISTER.md`.

## Project completion

PDCP completes when all ten in-scope families have approved reduction receipts and the effective future roadmap is reconciled to those receipts, with no capability loss and no unauthorized product start.

The final reduced count remains evidence-driven rather than preselected.
