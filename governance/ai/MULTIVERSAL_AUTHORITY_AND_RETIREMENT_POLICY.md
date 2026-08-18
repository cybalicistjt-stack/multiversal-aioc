# Multiversal Authority and Retirement Policy

**Document ID:** MV-AI-AUTHORITY-001  
**Version:** 1.0.0  
**Status:** ACTIVE CANDIDATE — CRS COMPLETION PENDING  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

## Purpose

Preserve project history without allowing superseded history to remain executable authority.

The governing rule is:

> Nothing may participate in current development merely because it still exists. Current authority must be explicitly registered, current, and consistent with live repository evidence.

## Lifecycle classes

Every governing or executable surface is assigned exactly one lifecycle class:

- `CURRENT` — authoritative now and allowed to govern or auto-execute.
- `CURRENT_COMPATIBLE` — supported current infrastructure that may be invoked by a `CURRENT` surface but cannot independently override canonical state.
- `HISTORICAL_INERT` — preserved for provenance; must not auto-trigger, block current work, or be interpreted as current status.
- `RETIRE_REMOVE` — obsolete material scheduled for removal or relocation after preservation requirements are satisfied.

Absence from the canonical authority registry means **not current**.

## Canonical state rules

1. `CURRENT_WORK_POINTER.json` is the only changing conversational work selector.
2. The bootstrap is a stable recovery protocol. It must not contain hard-coded claims about the current milestone, current PR, current branch, or next work item.
3. Current status belongs in the pointer, its named checkpoint, the roadmap index, and live GitHub evidence.
4. Bootstrap/current-state amendment files are transitional history. Their status facts must be folded into canonical files and then classified `HISTORICAL_INERT`; an amendment must never become a parallel current-state authority.
5. The full roadmap remains milestone/dependency authority, but runtime recovery must read only the section/index named by current state.
6. A pointer may not name a closed/superseded PR as active.
7. A work item may have at most one authoritative active integration PR. Older PRs remain preserved but closed or explicitly dormant.

## Workflow lifecycle rules

1. Every workflow under `.github/workflows/` must be registered as `CURRENT`, `CURRENT_COMPATIBLE`, or `HISTORICAL_INERT`.
2. Completed tranche/stage evidence workflows are historical unless explicitly designated reusable infrastructure.
3. A `HISTORICAL_INERT` workflow must not have automatic `push`, `pull_request`, `schedule`, or repository-event triggers. Historical validation may remain available only through a deliberately scoped manual/audit mechanism or preserved outside the active workflow directory.
4. Current application/package validation must use the completed Validation Core shared mechanics for checkout identity, runner preflight, diagnostics, deterministic evidence, and cross-platform comparison unless the workflow registry records a narrow technical exception.
5. A bespoke current workflow may own domain-specific runtime mechanics, but it must not independently reinvent shared validation identity/evidence semantics.
6. Current workflows must bind PR validation to the actual PR head SHA, not a synthetic merge SHA, when exact candidate identity is part of the gate.
7. Completed-program regression workflows may run only when intentionally registered as current regression coverage; completion status alone does not grant permanent automatic execution.

## Validator lifecycle rules

1. A validator is authoritative only for lifecycle states declared in its registry entry.
2. Historical lifecycle assertions such as `PREPARED`, `READY_TO_EXECUTE`, pre-activation state, or old completion gates must not be used as current prerequisites after the governed object has advanced.
3. Active validators must distinguish historical evidence validation from current-state validation.
4. Fixed baseline SHAs are permitted only when validating sealed historical evidence; current feature gates must derive their current baseline from canonical state or explicitly registered contracts.
5. When a validator becomes lifecycle-specific history, callers must retire it from current automatic paths instead of weakening its historical assertions.

## PR and branch lifecycle rules

- Superseded PRs are closed with a preservation/supersession note.
- Preserved branches are not current merely because they remain unmerged.
- Special-environment work may remain dormant, but the registry must state its activation condition and whether any automatic trigger exists.
- Closed PRs and historical branches must never be selected by bootstrap recovery as active work.

## Machine-enforcement requirements

The Canonicalization & Retirement Sweep must install checks that reject at least:

- bootstrap hard-coded current-work facts;
- pointer references to known closed/superseded PRs;
- unregistered active workflows;
- historical workflows with automatic triggers;
- current workflows using obsolete generic GitHub-hosted final-gate language;
- active references to retired runner labels or retired validation policy;
- multiple authoritative active PRs for one work item;
- active governance references to superseded bootstrap amendments;
- known lifecycle-state assertions used outside their registered historical scope.

## Stop-the-line rule

A repository-health defect that can alter work selection, validation outcome, or completion authority blocks unrelated feature completion until repaired or explicitly quarantined. Do not patch stale infrastructure opportunistically inside the feature and then leave the common defect intact.

## Completion standard

Repository historical material may remain extensive. The sweep is complete only when historical material is inert, current authority is singular and machine-checkable, current workflows are registered, stale executable paths are retired, and the final repository-health audit reports no known conflicting authority.