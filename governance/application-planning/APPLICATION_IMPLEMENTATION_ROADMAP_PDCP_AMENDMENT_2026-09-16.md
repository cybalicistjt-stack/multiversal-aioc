# Application Implementation Roadmap — PDCP Amendment — 2026-09-16

**Status:** OWNER-APPROVED PLANNING AMENDMENT  
**Project:** PDCP — Preimplementation Design Closure Project  
**Implementation authority:** none

## Purpose

Register a preimplementation design-closure process for the newer future specialist/runtime families so their eventual OPS3 product-development backlogs can be reduced to implementation-only tranches without losing accepted capability or proof obligations.

This amendment does **not** reduce any family yet. It establishes the evidence and reconciliation protocol under which future reductions may occur.

## OPS3 preservation

- `operations/CURRENT.json` remains the only live work selector.
- The active MAS product-development work is not changed by this amendment.
- MAS is explicitly excluded from PDCP.
- PDCP does not become a `ROADMAP_DEPENDENCY_GRAPH.json` implementation node.
- No PDCP artifact grants product implementation authority.
- A future family reduction changes planning only; future product implementation still requires OPS3 governed start.

## In-scope baseline

PDCP snapshots 208 planned tranches across:

- MCS — 21
- MCCS — 21
- MNCS — 24
- MSAS — 21
- MRCS — 21
- GPR — 16
- MERA — 24
- MBES — 24
- MSLR — 18
- MSWI — 18

The snapshot and source blob SHAs are recorded in:

`governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json`

## Governing PDCP artifacts

- Project charter: `governance/application-planning/preimplementation-design-closure/PDCP_PREIMPLEMENTATION_DESIGN_CLOSURE_PROJECT.md`
- Design-closure/reduction contract: `governance/application-planning/preimplementation-design-closure/PDCP_DESIGN_CLOSURE_CONTRACT.md`
- Baseline/reduction ledger: `governance/application-planning/preimplementation-design-closure/PDCP_REDUCTION_LEDGER.json`
- Benchmark-derived capability register: `governance/application-planning/preimplementation-design-closure/PDCP_BENCHMARK_CAPABILITY_REGISTER.md`

## Reduction rule

A future baseline tranche may be removed as a standalone roadmap execution unit only when:

1. its research/design obligations are durably closed to the PDCP contract;
2. every remaining repository-bound implementation and validation obligation is mapped to a named surviving implementation tranche or existing owner;
3. capability and golden-proof coverage are demonstrably preserved;
4. any referenced DAG start/golden milestone is updated atomically if the tranche ID changes;
5. no selected/in-progress OPS3 work is affected;
6. the before/after family mapping is recorded in a family reduction receipt.

The accepted dispositions are `RETAIN_IMPLEMENTATION`, `MERGE_IMPLEMENTATION`, `ABSORB_EXISTING_OWNER`, `DESIGN_CLOSED_NO_STANDALONE`, `REMOVE_DUPLICATE`, and `RETAIN_OWNER_DECISION`.

## Effective roadmap count

The effective count remains unchanged at project setup. The 208-tranche PDCP baseline is not replaced by a guessed reduced count.

As each family completes PDCP reduction review, its actual reduced strict order will be written to the family backlog and the PDCP ledger will record the approved before/after count. The user-facing roadmap guide may then be regenerated from the reconciled family backlogs and DAG.

## Cross-program activation

`governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json` remains the sole cross-program activation/dependency authority. PDCP may simplify the number and identity of future family tranches, but it may not weaken predecessor capabilities or skip start/golden gates by implication.

If a PDCP reduction removes or renumbers an ID referenced by the DAG, the same planning change must point the DAG to an equivalent surviving implementation/golden proof and update the applicable regression tests.

## Non-goals

This amendment does not:

- reopen MAS;
- modify CURRENT;
- start MCS/MCCS/MNCS/MSAS/MRCS/GPR/MERA/MBES/MSLR/MSWI implementation;
- declare any baseline tranche completed;
- replace existing owner-domain contracts;
- set an arbitrary tranche-reduction quota;
- allow design documents to substitute for required product code or validation.
