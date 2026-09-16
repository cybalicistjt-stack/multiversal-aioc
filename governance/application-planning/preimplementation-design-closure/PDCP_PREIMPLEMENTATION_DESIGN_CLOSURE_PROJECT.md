# PDCP — Preimplementation Design Closure Project

**Status:** OWNER-APPROVED — ACTIVE FAMILY REDUCTION PROJECT  
**Project ID:** `PDCP`  
**Approved:** 2026-09-16  
**Owner and final authority:** John Brandon Turner  
**Implementation authority:** none  
**OPS3 lane:** `content-design` when explicitly requested  
**Operational selector:** none; `operations/CURRENT.json` remains the live selector

## Purpose

PDCP closes research/design obligations before implementation and reduces future execution units only when capability coverage, owner boundaries and proof obligations remain explicit. It is a planning project, not a product family, and cannot grant product authority.

## Scope

Ten future families are in scope; MAS is excluded:

- MCS 21;
- MCCS 21;
- MNCS 24;
- MSAS 21;
- MRCS 21;
- GPR 16;
- MERA 24;
- MBES 24;
- MSLR 18;
- MSWI 18.

Historical baseline: **208** tranches. This baseline remains immutable provenance.

All eight benchmark-derived design packets are `design_closed`. No ninth packet is implied.

## Reduction rules

Every family receives a complete before/after receipt. Both intra-family overlap and cross-family/shared-owner overlap must be audited. Generic infrastructure has one practical owner; specialist families retain domain adapters, semantics, UX and proof. DAG milestone IDs are preserved where practical. Golden proof, migration/recovery, accessibility, permissions/privacy, provenance and deterministic validation cannot disappear. PDCP does not modify `operations/CURRENT.json` merely to do design work.

Allowed dispositions: `RETAIN_IMPLEMENTATION`, `MERGE_IMPLEMENTATION`, `ABSORB_EXISTING_OWNER`, `DESIGN_CLOSED_NO_STANDALONE`, `REMOVE_DUPLICATE`, `RETAIN_OWNER_DECISION`.

## Resolved family reductions

- **MSLR:** 18 → 9; removed 9; stable `MSLR-01/MSLR-18`.
- **MSWI:** 18 → 7; removed 11; stable `MSWI-01/MSWI-18`.
- **MBES:** 24 → 9; removed 15; stable `MBES-01/MBES-24`.
- **MERA:** 24 → 10; removed 14; stable `MERA-01/MERA-24`.
- **GPR:** 16 → 10; removed 6; stable `GPR-01/GPR-05/GPR-16`.
- **MRCS:** 21 → 13; removed 8; stable `MRCS-05/MRCS-13/MRCS-14/MRCS-21`.
- **MSAS:** 21 → 11; removed 10; stable `MSAS-01/MSAS-21`; generic generation absorbed to PCA-09/PCA-08 and generic lifecycle/provenance remains ARI/PCA-owned.

**Current effective future count:** 135.  
**Standalone future tranches removed:** 73.  
**Resolved family receipts:** 7 / 10.

The next selected PDCP family review is **MNCS**, followed by MCCS and MCS under `PDCP_CROSS_FAMILY_OVERLAP_REGISTER.md`.

## Current durable control surfaces

- `PDCP_DESIGN_CLOSURE_CONTRACT.md`;
- `PDCP_REDUCTION_LEDGER.json`;
- `PDCP_CROSS_FAMILY_OVERLAP_REGISTER.md`;
- eight packet DCPs/closure records;
- family DCPs and `PDCP_<PROGRAM>_REDUCTION_RECEIPT.json` receipts.

## OPS3 coordination

PDCP uses the on-demand content-design lane when explicitly requested. Product-development work remains governed solely by `operations/CURRENT.json` and `ROADMAP_DEPENDENCY_GRAPH.json`. Historical roadmap amendments remain provenance; reduced family backlogs and receipts are the effective planning contracts.

## Completion

PDCP completes when all ten in-scope families have reconciled receipts and the effective future roadmap reflects those receipts without capability loss or unauthorized product start. The final count is evidence-driven, not preselected.
