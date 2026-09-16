# PDCP — Preimplementation Design Closure Project

**Status:** OWNER-APPROVED — ACTIVE FAMILY REDUCTION PROJECT  
**Project ID:** `PDCP`  
**Approved:** 2026-09-16  
**Owner and final authority:** John Brandon Turner  
**Implementation authority:** none  
**OPS3 lane:** `content-design` when this project is the user's explicit session intent  
**Operational selector:** none; `operations/CURRENT.json` remains the only live selector

## Purpose

PDCP moves research, architecture decisions, mechanics design, state modeling, operation semantics, UX behavior, edge-case resolution and acceptance-design work out of future product-development tranches wherever those obligations can be completed before software implementation begins.

The objective is not to reduce capability. It is to arrive at governed start with implementation-ready contracts so retained tranches contain only work that materially requires product code, schema/migration, UI construction, runtime integration, automated proof, packaging or other repository-bound implementation.

PDCP is a design/planning project, not a product family. It cannot grant implementation authority or override `operations/CURRENT.json`.

## Current phase

All eight benchmark-derived capability packets are `design_closed`. PDCP is in the family-by-family reduction and roadmap-reconciliation phase.

Durable control surfaces:

- `PDCP_DESIGN_CLOSURE_CONTRACT.md`;
- `PDCP_REDUCTION_LEDGER.json`;
- `PDCP_CROSS_FAMILY_OVERLAP_REGISTER.md`;
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

**Historical baseline:** 208 planned tranches. The baseline is immutable provenance; effective counts change only through complete receipts.

`MAS` is excluded in full.

## Design tracks

- Specialist Creator: `MCS → MCCS → MNCS`
- Post-MAS Runtime/Creator: `MSAS → MRCS → GPR → MERA → MBES → MSLR → MSWI`

## Closed capability packets

The eight closed packets cover: social interaction/norms; systemic investigation/evidence; autonomous actors/threats; semantic affordances/effects; persistent history/legacy; multi-resolution simulation/world evolution; creator/GM execution UX; and simulation/formal validation.

No ninth benchmark packet is implied.

## Reduction dispositions

Every baseline tranche receives exactly one final disposition:

- `RETAIN_IMPLEMENTATION`;
- `MERGE_IMPLEMENTATION`;
- `ABSORB_EXISTING_OWNER`;
- `DESIGN_CLOSED_NO_STANDALONE`;
- `REMOVE_DUPLICATE`;
- `RETAIN_OWNER_DECISION`.

There is no predetermined target percentage or final count.

## Reduction invariants

1. No currently selected, governed-started or in-progress product work is eligible for PDCP reduction.
2. MAS is excluded.
3. PDCP never grants implementation authority or mutates `CURRENT.json` merely for design work.
4. `ROADMAP_DEPENDENCY_GRAPH.json` remains cross-program activation authority.
5. Referenced DAG milestone IDs may be removed/renumbered only with an atomic equivalent-gate update.
6. Golden proof, migration, recovery, accessibility, privacy/permissions, provenance and deterministic validation may not disappear.
7. Existing owner boundaries remain authoritative.
8. Every family performs both intra-family and cross-family/shared-owner overlap audits.
9. Generic engines/workflows have one practical owner; specialist families retain domain adapters/semantics/UX/proof.
10. Stable sparse IDs are preferred when they avoid gratuitous DAG churn.
11. Design closure is not software completion.
12. Every change remains reviewable through a complete before/after receipt.

## Reduction progress

Five family reductions are now resolved.

- **MSLR:** 18 → 9; removed 9; stable gates `MSLR-01` / `MSLR-18`.
- **MSWI:** 18 → 7; removed 11; stable gates `MSWI-01` / `MSWI-18`.
- **MBES:** 24 → 9; removed 15; stable gates `MBES-01` / `MBES-24`.
- **MERA:** 24 → 10; removed 14; stable gates `MERA-01` / `MERA-24`.
- **GPR:** 16 → 10; removed 6; stable milestones `GPR-01`, `GPR-05`, `GPR-16`; `GPR-15` conformance proof absorbed into `GPR-16`.

**Historical PDCP baseline:** 208.  
**Current effective future count after five receipts:** 153.  
**Standalone future tranches removed so far:** 55.

The next selected family review is **MRCS**, followed by MSAS, MNCS, MCCS and MCS under the overlap-aware reverse-consumer order in `PDCP_CROSS_FAMILY_OVERLAP_REGISTER.md`.

## OPS3 coordination

PDCP sessions normally use the on-demand `content-design` lane. Product-development work continues to follow `operations/CURRENT.json`. Family reductions may reconcile planning sources and affected milestone references but do not start product implementation.

## Project completion

PDCP completes when all ten in-scope families have approved receipts and the effective future roadmap is reconciled to them without capability loss or unauthorized product start.
