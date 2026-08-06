# Interaction and Governance Incident
## P9-06-008 Stale Roadmap Misclassification

**Incident ID:** MV-INC-P9-06-008-STALE-ROADMAP-MISCLASSIFICATION  
**Detected:** 2026-08-06  
**Severity:** P0 — could create a false backlog completion  
**Status:** correction in progress

## Summary

A stale derived section in `governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md` described P9-06-008 as backup, restore, and provider-exit export ports. The authoritative Phase 9 backlog instead defines P9-06-008 as the initial 17-table logical schema migration.

The stale description caused a useful recovery-contract package to be implemented and merged in application PR #78 under the wrong backlog identifier.

## Authoritative source

`governance/phase9/P9-06_IMPLEMENTATION_BACKLOG_AND_ACCEPTANCE_GATES.json`

Relevant authoritative sequence:

- P9-06-008 — Create initial 17-table logical schema migration.
- P9-06-009 — Add deterministic seed and reset fixtures.
- P9-06-010 — Add expand-migrate-contract migration checks.
- P9-06-011 — Add backup restore and export rehearsal scripts.

## Impact

- The merged code remains useful, provider-neutral, deterministic recovery-contract groundwork.
- P9-06-008 was **not** completed.
- P9-06-011 was **not** completed because rehearsal scripts and prerequisite data-foundation work remain absent.
- The existing P9-06-008 attempt must be superseded rather than completed.

## Correction

1. Reclassify the PR #78 package as P9-06-011A preparatory recovery-contract foundation.
2. Rename its validator and CI workflow and correct fixture/schema identity.
3. Correct the derived application roadmap to match the authoritative backlog.
4. Supersede `P9-06-008-attempt-001` with explicit disposition evidence.
5. Create a real application branch and `P9-06-008-attempt-002` for the authoritative 17-table logical schema migration.
6. Do not advance to P9-06-009 until attempt 002 is `completed_verified`.

## Prevention

Before starting any P9-06 backlog item, the agent must read the exact item from `P9-06_IMPLEMENTATION_BACKLOG_AND_ACCEPTANCE_GATES.json` and compare it with the roadmap index and current checkpoint. When derived prose conflicts with the canonical backlog JSON, the canonical backlog controls and the stale derivative must be corrected before implementation.

## Preserved boundaries

No provider, credential, paid service, production data, deployment, release, or irreversible commitment was introduced. IA-D03-003 remains an explicit planned parallel track.
