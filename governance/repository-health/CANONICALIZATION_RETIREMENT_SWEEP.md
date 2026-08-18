# Canonicalization & Retirement Sweep (CRS)

**Program ID:** CRS  
**Status:** OWNER-APPROVED / EXECUTION ACTIVE  
**Date:** 2026-08-18

## Objective

Stop feature progression long enough to remove stale executable authority from both canonical repositories.

Preserve history, but leave nothing historical in a position to silently select work, impose an obsolete gate, auto-trigger expensive validation, or contradict current repository state.

## Tranches

### CRS-01 — Authority Canonicalization

- make the bootstrap status-agnostic;
- make the work pointer select CRS as the primary operation;
- create the authority lifecycle policy and registry;
- remove parallel bootstrap-amendment authority;
- record all paused production tracks explicitly.

### CRS-02 — PR / Branch Retirement

- classify every open PR in both canonical repositories;
- close superseded and completed-era PRs with preservation notes;
- retain only deliberately active/dormant PRs;
- ensure one authoritative integration path per unfinished work item;
- ensure recovery records never point to a closed superseded PR.

### CRS-03 — Workflow Retirement & VCH Adoption

- inventory every workflow in `Multiversal-app` and `multiversal-aioc`;
- classify each workflow lifecycle;
- make completed-stage/tranche workflows inert;
- remove automatic triggers from historical workflows or move them outside the active workflow directory;
- register reusable current infrastructure;
- migrate current application/package gates to Validation Core mechanics or record a narrow exception.

### CRS-04 — Validator & Lifecycle-Assumption Sweep

- inventory validators and their declared lifecycle assumptions;
- find fixed historical state assertions used as current prerequisites;
- separate sealed historical-evidence validators from current-state validators;
- remove retired validators from automatic current paths;
- search for obsolete hosted-runner gates, old runner labels, old active states, old branch names, and stale fixed baselines.

### CRS-05 — Work-Order / Runtime-State Cleanup

- audit `.agent/active-work-orders`, `.ai/current-work-order*`, ready-work orders, runtime pointers, roadmap indexes, amendments, dispatches, and checkpoints;
- ensure completed work is not stored under an operationally active namespace without explicit inert metadata;
- establish one canonical active-work projection per repository;
- preserve historical work orders outside current selection semantics.

### CRS-06 — Machine Enforcement & Final Health Audit

- add deterministic authority/workflow/staleness validators;
- add a repository-health CI gate scoped to governance/infrastructure changes;
- produce `CANONICAL_STATE_AUDIT.json` with zero known conflicting authority;
- verify current bootstrap → pointer → checkpoint → live PR/branch evidence chain;
- verify all historical workflows are inert;
- verify every current workflow is registered and VCH-compatible or explicitly excepted;
- resume production only after the sweep is `completed_verified`.

## Preserved production work during stop-the-line

- Post-GATX successor refresh: preserve current App branch/PR evidence, but no completion/merge while CRS is active.
- CCTI-12-T04: preserve construction and quarantine evidence; no completion/merge while CRS is active.
- WP-011: preserve Mac-dependent work and its special activation gate; do not consume Mac/hosted authorization during CRS.
- DS-008: preserve blocked work unchanged.
- APW / CSW / APM: remain owner-approved planned work, not active implementation.

## Completion gate

CRS is complete only when all six tranches are verified and the final health audit demonstrates:

1. one current bootstrap protocol with no hard-coded current milestone/work item;
2. one current work selector and internally consistent checkpoint;
3. zero active references to superseded/closed PRs;
4. every open PR classified and intentionally retained;
5. every active workflow registered;
6. historical workflows unable to auto-trigger;
7. no current gate relies on obsolete generic GitHub-hosted completion policy;
8. current package/application workflows use Validation Core shared mechanics or a documented technical exception;
9. lifecycle-specific historical validators cannot block later current states;
10. operational work-order namespaces do not silently contain completed-era authority;
11. machine staleness checks pass;
12. `CANONICAL_STATE_AUDIT.json` records zero known conflicting authority.

Feature work resumes only after this gate.