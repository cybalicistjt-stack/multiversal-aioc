# Work Order — AIOC-I-001A
## Project State Engine and Canonical Work Ledger

**Parent milestone:** AIOC-I-001 — Operational Core Implementation  
**Status:** Ready

## Objective

Implement the first working Operational Core slice that makes project continuity, milestone state, work-package state, decisions, blockers, evidence, and handoffs native AIOC records instead of manually maintained chat context.

## Required implementation

1. Define versioned schemas for project state, work packages, decisions, blockers, evidence references, and handoffs.
2. Add stable-ID generation and validation.
3. Add migration from the current local state into the new ledger without data loss.
4. Implement append-only state-transition and audit records.
5. Implement dependency-aware next-work resolution.
6. Implement the deterministic `Continue` operation as a proposed transition, not an untracked action.
7. Add projections for current milestone, last completed work, next executable work, blockers, and pending approvals.
8. Add backup, restore, interrupted-write, duplicate-ID, and migration tests.
9. Add a read-only GitHub state adapter interface, with writes explicitly deferred.
10. Update diagnostics and smoke tests to validate the new core contracts.

## Acceptance criteria

- A fresh installation can create and persist canonical project state.
- Existing local data migrates with backup and rollback support.
- Every ledger record has stable ID, schema version, timestamps, provenance, and audit linkage.
- `Continue` returns exactly one executable work item or a concrete blocker.
- Failed or unapproved work cannot advance the milestone.
- Restoring a backup reconstructs the same current-state projection.
- Smoke and contract tests pass.

## Expected repository areas

- `src/core/state/` or equivalent modular core path;
- `schemas/operational-core/`;
- `tests/operational-core/`;
- diagnostics and smoke-test updates;
- migration and recovery documentation.

## Completion evidence

- implementation commits;
- passing tests;
- migration report;
- updated canonical current state;
- outgoing AIOC-I-001B work order.
