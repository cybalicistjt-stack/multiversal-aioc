# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-03; SCL-04 IN PROGRESS  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-03 remain `completed_verified`. SCL-04 — Command Phases & Deterministic Order Resolution — is `in_progress` from exact application main `a4913b3cb162c0c05e4efaf7a98b856f7d57c92a` on `integration/scl-04-command-phases-deterministic-order-resolution` under a sealed bounded implementation authority.

## Frozen predecessor contracts

SCL-01 retains source/scale/owner-domain routing and identity-preserving visibility-first projection. SCL-02 retains reusable unit/formation profile projections and explicit canonical leaf identity. SCL-03 retains read-only command relationships, ODL-04-backed delegation, order intent/lifecycle and descriptive communication projections. SCL-03 order types are `directive`, `task`, `constraint`, `coordination`; lifecycle is `proposed`, `issued`, `acknowledged`, `received`, `superseded`, `cancelled`.

## SCL-04 governed contract

Phase vocabulary is exactly `intake`, `eligibility`, `precedence`, `resolution`, `handoff`, `closed`. Outcome vocabulary is exactly `ready`, `partial`, `blocked`, `invalid`, `conflict`.

Eligibility is conservative. Only visible SCL-03 orders with resolved evidence, lifecycle `received`, resolved command/delegation scope and non-interrupted communication may become handoff candidates. `proposed`, `issued`, and `acknowledged` remain blocked pending receipt. `superseded` and `cancelled` are inactive-invalid.

SCL-04 defines no implicit order-type priority table. Precedence comes only from explicit visible dependency, supersession and conflict references. Missing dependency references block. Dependency cycles and unresolved explicit conflicts remain `conflict`; they never auto-select a winner. Independent eligible orders use stable order-id ordering only for deterministic receipt/handoff ordering, never as command authority.

SCL-04 resolves command-order coordination only. A result can be `ready`, `partial`, `blocked`, `invalid`, or `conflict`, and may emit zero or more explicit canonical owner-domain handoff requests. Handoff domains are exactly `action`, `combat`, and `event`. Downstream owner domains decide and commit canonical results. SCL-04 never executes an Action, applies Combat effects, creates an Event outcome, advances campaign time, or mutates canonical owner state; its receipt cannot be replayed as world-state truth or double-apply downstream effects.

`partial` requires at least one visible resolved owner-domain handoff and at least one other visible handoff that remains unknown, conflict, incompatible, or blocked. Hidden evidence never affects visible status or cardinality.

Permission/visibility filtering occurs before order inclusion, dependency/precedence/conflict evaluation, outcomes, handoff counts, summary/search/provenance, deterministic receipts or AI context. Missing, unknown, conflict or incompatible visible evidence remains conservative and is never guessed or auto-reconciled.

Stable order ids, explicit dependency/supersession/conflict ids and owner-domain handoff ids define deterministic receipt ordering. Presentation prose is excluded from canonical receipt truth.

SCL-05/SCL-06 retain morale/logistics mechanics; SCL-07 retains terrain/objective strategic-position mechanics; SCL-08 fleet/platform integration; SCL-09 casualty/damage reconciliation; SCL-10 strategic consequences. AI remains advisory only where separately governed. No durable SCL-04 ledger is created and migration `0022` remains unreserved.

## Validation

SCL-04 must establish genuine acceptance-first RED before production contract/panel mutation. Final validation must run exactly one changed current-family SCL-04 profile on exact-head self-hosted Linux and Windows with deterministic comparison and zero historical predecessor fanout.

## Tranches

1. SCL-01 — completed_verified.
2. SCL-02 — completed_verified.
3. SCL-03 — completed_verified.
4. SCL-04 — in_progress.
5. SCL-05 — planned.
6. SCL-06 — planned.
7. SCL-07 — planned.
8. SCL-08 — planned.
9. SCL-09 — planned.
10. SCL-10 — planned.
11. SCL-11 — planned.

## Invariants

- Ordinary Action/Combat/Event and canonical owner-domain truth remain authoritative.
- SCL-01 through SCL-03 remain frozen with retired implementation authority.
- SCL-04 may classify and coordinate order handoffs but may not execute or double-apply canonical downstream results.
- No AI autonomous command/adjudication, owner mutation, hidden-data reveal, duplicate ledger, persistence or migration `0022` is authorized.
