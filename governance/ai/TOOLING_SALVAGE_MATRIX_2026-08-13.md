# Multiversal Tooling Salvage Matrix

**Date:** 2026-08-13  
**Purpose:** classify substantial unmerged tooling against current canonical capabilities so useful work is preserved without merging stale stacked branches wholesale.

## Current canonical baseline

### Multiversal-app `main`

The current `tools/mv_dev` toolbelt already provides:

- repository/environment doctor;
- design-system linting;
- stable-ID traceability compile/query;
- STAGE-A-A2 repository preflight;
- bounded A2 task capsules;
- governed fixture verification/normalization/projection;
- deterministic scenario verify/run/replay;
- differential privacy/permission scanning;
- UI evidence plan verification, capture orchestration, and harvest.

The app also retains `tools/repo_policy.py`, WP-011 tools, P9 verification/rehearsal tools, and physical-runner tooling.

### multiversal-aioc `main`

Current AIOC tooling includes at least:

- continuity state validation/projection;
- correction-to-regression tooling;
- governed write bridge;
- interaction audit/control tooling;
- CAPP transition/scope/reference/QA tools;
- large governance/content validation surface.

Therefore older maintenance branches must be evaluated by **capability**, not by file count.

## Application PR #64 — Development Console + Repository Brain

Historical branch: `wo/WO-MAINT-DEVCONSOLE-001`  
Disposition: **HIGH-VALUE SELECTIVE SALVAGE — DO NOT MERGE WHOLE BRANCH**

### Capability overlap with current main

| Historical capability | Current overlap | Disposition |
|---|---|---|
| repository readiness/preflight | `mv-dev doctor`, `mv-dev preflight a2` | **mostly superseded**; preserve generic lessons only |
| repository mapping/context selection | `mv-dev traceability`, task capsules | **partial overlap** |
| prompt/scope linting | design lint + governance policies | **partial overlap** |
| evidence packaging | task capsules, scenario/UI evidence tools | **partial overlap** |
| review packs/session continuation | bootstrap + continuity state + task capsules | **partial overlap; evaluate UX advantage** |
| failure memory/triage | no direct app-main equivalent identified | **salvage candidate** |
| co-change hints/test-impact ranking | no direct `mv-dev` equivalent identified | **salvage candidate** |
| local documentation search with line ranges | no direct `mv-dev` equivalent identified | **salvage candidate** |
| task sizing/planning heuristics | no direct `mv-dev` equivalent identified | **salvage candidate if deterministic** |
| deterministic scaffolding | no direct `mv-dev` equivalent identified | **salvage candidate with strict scope** |
| browser-local Development Console/Repository Brain UI | no direct `mv-dev` browser surface identified | **salvage candidate; optional UI layer** |

### Required integration approach

Do not carry forward the old branch's `.ai/current-work-order.md`, AGENTS, issue templates, or `repo_policy.py` wholesale. Extract unique capabilities into current `mv-dev`/governance patterns with new tests against current main.

## Application PR #66 — Multiversal Local Operator

Historical branch: `wo/WO-MAINT-LOCAL-OPERATOR-001`  
Disposition: **HIGH-VALUE ISOLATED SALVAGE — SECURITY/EXECUTION REVIEW REQUIRED**

### Unique capability candidates

- typed local action registry and machine-readable schemas;
- authorized-root and active-work-order path enforcement;
- explicit executable/subcommand allowlists;
- sanitized environment handling;
- one-time human approval for significant local actions;
- external journal, backups, rollback, and emergency stop;
- bounded file/Git/command/process/application/browser/clipboard/screenshot operations;
- Repository Brain and development-preparation actions;
- bounded batch execution to reduce agent round trips;
- authenticated loopback dashboard/API/MCP adapter;
- external state by default rather than polluting the Git worktree.

### Overlap

The governed AIOC write bridge handles a narrow class of repository-side governance writes, but it is not a general local operator. `mv-dev` is mostly inspection/validation/tooling, not a typed local execution adapter.

### Decision

The Local Operator is **not superseded**. It is potentially useful for Sunday/Codex and long development runs, but its execution surface is broader than the current toolbelt. Salvage it as a separately bounded local-development capability after code/security review; do not merge the old stacked branch directly.

## Application PR #68 — Credit-Offload Workbench

Historical branch: `wo/WO-MAINT-CREDIT-OFFLOAD-001`  
Disposition: **HIGH-VALUE SELECTIVE SALVAGE — PERFORMANCE/CREDIT OPTIMIZATION LAYER**

### Strong salvage candidates

- content-addressed incremental verification cache;
- stable-context/task-delta packet compiler;
- local symbol/dependency graph;
- dependency-free local documentation/code retrieval;
- failure diagnosis memory and safe retry recipes;
- avoided-token/avoided-cost reporting;
- hardware/runtime profiling;
- governed recipe/catalog model for repeatable tasks.

### Conditional candidates

- deterministic transform engine with preview/approval/backup/rollback — useful, but integrate only if it can reuse current scope and validation controls;
- local model adapters/routing — retain as optional proposal-only material; do not make a provider/model dependency or add downloads/installations to core development flow;
- localhost dashboards — combine with any surviving Console/Operator UI rather than multiplying local web surfaces.

### Current overlap

`mv-dev` already reduces repeated work via task capsules, traceability, deterministic fixtures/scenarios, and focused evidence tools. The credit-offload package still appears to add **verification caching, retrieval/indexing, symbol graph, failure memory, and explicit credit accounting** that are not present in the current `mv-dev` command set.

## AIOC PR #1 — Original operational architecture

Historical branch: `governance/session-bootstrap-v1`  
Disposition: **LARGE DIVERGENT CAPABILITY RESERVOIR — SALVAGE ONLY**

The branch is hundreds of commits behind current main and contains a broad alternative operational implementation: project-state engine, recovery/repository sync, repository intelligence, developer workbench, content studio, dashboards/orchestration, testing/simulation, and release-hardening services/workflows.

Current AIOC main does not expose the old `implementation/developer-workbench` tree at the same path, so the branch cannot be dismissed as purely duplicated. Conversely, current main has much newer continuity, correction, CAPP, object/content, IA, PPIA, and bootstrap governance that the old branch never knew about.

### Salvage candidates to compare later

- repository-intelligence projections;
- project-state engine concepts that can be generated from current pointer/checkpoints rather than compete with them;
- recovery/repository-sync diagnostics;
- developer change-plan/review/certification helpers;
- content authoring/release certification utilities;
- digital-twin/regression/test-harness projection utilities;
- executive dashboard/orchestration views;
- release-readiness/final-certification helpers.

Do not resurrect its old current-state files, roadmap, bootstrap, or branch-as-canonical assumptions.

## Consolidation recommendation

Build **one current development-operations toolkit** rather than reviving four historical tool systems.

### Core layer — keep current

- `mv-dev` inspection, traceability, fixtures, scenarios, privacy, UI evidence, A2 preflight/task capsules;
- application repository policy/validators;
- AIOC bootstrap/continuity/correction/governed-write controls.

### Salvage layer 1 — low-risk/high-return

1. checkout divergence classification in `mv-dev doctor`;
2. incremental verification cache;
3. local documentation/code search with line ranges;
4. symbol/dependency graph and test-impact hints;
5. failure memory/triage;
6. stable-context/task-delta packets;
7. avoided-credit reporting.

### Salvage layer 2 — useful but broader

1. consolidated local dashboard for doctor/tasks/evidence/search/triage;
2. deterministic scaffolding/transforms under current scope controls;
3. bounded Local Operator actions, journal, backup, rollback, emergency stop.

### Salvage layer 3 — optional later

1. local-model routing/adapters;
2. broader AIOC dashboards/orchestration projections;
3. content/release simulation utilities not needed for immediate Stage A work.

## Immediate implication

The old PR stack should remain open or preserved until the unique low-risk capabilities above are recovered or explicitly rejected. Do not merge #64/#66/#68 as-is and do not delete their branches during the solidity audit.
