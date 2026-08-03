# AIOC-0-012 Implementation Gate Test Matrix

## Architecture and continuity

- GATE-001: bootstrap file exists on the working branch.
- GATE-002: canonical current-state file identifies one active milestone.
- GATE-003: App and AIOC repository purposes are not conflated.
- GATE-004: packages AIOC-0-001 through AIOC-0-011 are represented.
- GATE-005: outgoing work orders form a continuous implementation path.
- GATE-006: `Continue` resolves to a concrete next work item.
- GATE-007: recovery mode detects an unverifiable repository state.
- GATE-008: completion cannot be claimed without repository evidence.

## Data and contracts

- GATE-009: every persistent object requires a stable ID.
- GATE-010: every persistent object records schema version.
- GATE-011: migrations create a backup before mutation.
- GATE-012: migrations expose rollback or restore behavior.
- GATE-013: commands and events have correlation identifiers.
- GATE-014: projections can be regenerated from governed records.
- GATE-015: evidence references remain immutable once attached.
- GATE-016: duplicate IDs block promotion.

## Security and governance

- GATE-017: protected actions default to deny.
- GATE-018: permission checks occur before proposal execution.
- GATE-019: approvals identify actor, scope, decision, and time.
- GATE-020: altered runtime results preserve original and final values.
- GATE-021: secret values never appear in repository files.
- GATE-022: secret values never appear in browser local storage.
- GATE-023: release actions require release authority.
- GATE-024: emergency access is time-bounded and audited.

## Assistant and orchestration

- GATE-025: answers are distinguished from action proposals.
- GATE-026: proposed writes identify repository, branch, and paths.
- GATE-027: uncertainty is surfaced rather than hidden.
- GATE-028: destructive actions require explicit approval.
- GATE-029: agent assignments include owner, status, and evidence.
- GATE-030: failed work does not advance the canonical milestone.
- GATE-031: cross-repository actions cannot silently change target.
- GATE-032: context restoration prefers repository evidence.

## Runtime and recovery

- GATE-033: interrupted writes do not corrupt the active state.
- GATE-034: backup export can be restored into a clean installation.
- GATE-035: offline edits are queued with provenance.
- GATE-036: synchronization conflicts require explicit resolution.
- GATE-037: replay reconstructs approved runtime transitions.
- GATE-038: audit records survive restore operations.
- GATE-039: smoke tests block merge when core contracts fail.
- GATE-040: current passing smoke baseline is preserved.

## Gate outcome

All forty gate requirements are represented by completed architecture controls or mandatory implementation conditions.

**Result: PASS WITH CONTROLLED IMPLEMENTATION CONDITIONS**
