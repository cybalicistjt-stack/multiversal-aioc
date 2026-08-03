# AIOC-I-001A — Project State Engine and Canonical Work Ledger

## Status

Implementation complete; validation pending CI execution.

## Purpose

This module supplies the first executable component of the AIOC Operational Core. It replaces conversational assumptions with versioned, machine-readable project state and an append-only evidence ledger.

## Files

- `project-state.schema.json` — canonical JSON Schema.
- `canonical-project-state.seed.json` — initial governed Multiversal state.
- `project-state-engine.mjs` — validation, transitions, decisions, handoffs, reconciliation, hashing, and persistence hooks.
- `project-state-engine.test.mjs` — executable Node acceptance tests.

## Enforced invariants

1. The Multiversal App and AIOC repositories are separate canonical records.
2. Exactly one work item is active.
3. The active pointers reference existing records.
4. Work-item dependencies must exist and must be complete before activation.
5. Completed work must carry evidence.
6. Completed milestones cannot contain unfinished work.
7. Duplicate stable identifiers are rejected.
8. Every accepted mutation appends an actor, reason, before hash, after hash, timestamp, and evidence.
9. Failed validation rolls back the mutation.
10. Decisions and session handoffs are first-class project records.

## Running tests

```bash
node implementation/operational-core/project-state/project-state-engine.test.mjs
```

Expected result:

```text
RESULT 13/13 passed
```

## Integration boundary

AIOC-I-001A deliberately does not call GitHub or other connectors directly. Repository synchronization belongs to AIOC-I-001B. The engine accepts a `persist(state)` adapter so browser storage, filesystem storage, GitHub-backed state, or a future database can be attached without changing the governance model.

## Completion evidence

The work item may be marked complete after:

- the test command returns `13/13 passed`;
- schema validation succeeds;
- the smoke suite remains green;
- the canonical state is advanced to AIOC-I-001B with the commit and test evidence recorded.
