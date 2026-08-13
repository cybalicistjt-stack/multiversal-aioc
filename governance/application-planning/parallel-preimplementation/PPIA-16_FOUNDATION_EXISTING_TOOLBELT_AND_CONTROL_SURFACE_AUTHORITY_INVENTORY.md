# PPIA-16 Foundation — Existing Developer Toolbelt and Control-Surface Authority Inventory

**Work item:** PPIA-16 — Developer Console / AI-Team Control Surface  
**Bounded substep:** Foundation / Existing Developer Toolbelt and Control-Surface Authority Inventory  
**Status:** Foundation candidate  
**Application source anchor:** `cybalicistjt-stack/Multiversal-app` at `354e24007d2c453d090a2a6cdb31d3e3333c84c1`  
**Toolbelt anchor:** `mv-dev` v0.10.0 / DT-001 through DT-010

## Purpose

This Foundation freezes the source and authority model for the future Developer Console before detailed screen interaction contracts are authored.

The console is a developer-facing cockpit over existing governed tools and repository evidence. It is **not** a new authority source, application runtime, deployment surface, production control plane, or replacement for the governing work orders and repository evidence.

## Controlling boundaries

PPIA-16 remains a design/preimplementation tranche. It does not:

- mutate application runtime state;
- activate STAGE-A-A2;
- create release or deployment authority;
- grant tester access;
- use production credentials or paid services;
- promote canonical content without governing source authority;
- weaken deterministic assertions or stop conditions;
- turn tool PASS results, evidence receipts, generated task capsules, or traceability proof state into work-item completion.

Only `completed_verified` is complete under the repository continuity/completion policies.

## Existing Developer Toolbelt inventory

The completed application-repository toolbelt is ten separately governed tools. The future console must preserve that separation.

| Tool | Existing responsibility | Console authority treatment |
|---|---|---|
| DT-001 | repository-aware `mv-dev doctor` health/readiness checks | read-only observation; preserve PASS/WARN/BLOCK |
| DT-002 | A2 preflight/compatibility mapper | read-only observation; cannot activate A2 or replace exact changed-path authority |
| DT-003 | bounded Codex task-capsule builder | generated development aid; PREPARED/READY_TO_EXECUTE/BLOCKED is capsule scope only |
| DT-004 | fixture validation/normalization/role projection | development/test gateway; preserve canonical/synthetic/campaign-local/source-only classes |
| DT-005 | deterministic scenario/E2E runner and replay | deterministic evidence; built-in fixture adapter is read-only and cannot fake owning-domain mutation |
| DT-006 | permission/hidden-information leak scanner | blocking findings for supplied scan scope; not production security certification |
| DT-007 | exact-candidate UI evidence harvester | candidate-bound evidence receipts; synthetic CI PNGs remain tool tests only |
| DT-008 | design-system compliance linter/ratchet | source findings; legacy debt remains WARN while newly introduced violations BLOCK |
| DT-009 | stable-ID traceability compiler/proof graph | occurrences are not proof; PROVEN requires explicit integrity-valid proof links and is not work-item completion |
| DT-010 | recovery/performance harness | deterministic recovery/budget evidence; reference probes are not product proof and budgets require explicit authority |

The immutable documentation paths and blob SHAs inspected for each tool are recorded in `PPIA-16_FOUNDATION_TOOLBELT_AND_AUTHORITY_INVENTORY_v0.1.0.json`.

## Application-work authority remains separate

`Multiversal-app/.ai/current-work-order.md` names **STAGE-A-A2 — Universal Object Experience** as `AUTHORIZED CURRENT NEXT`.

The ready work order states **READY FOR ACTIVATION — IMPLEMENTATION NOT YET STARTED**, names branch `stage-a/a2-universal-object-experience`, preserves its explicit stop conditions, and grants no release/deployment authority.

PPIA-16 may display that application authority and use DT-002/DT-003 to prepare for it. PPIA-16 itself cannot activate A2. Likewise, the AIOC primary conversational pointer does not supersede the application repository's authorized current work order.

## AIOC control and evidence surfaces

The Foundation recognizes these as distinct control surfaces:

1. `CURRENT_WORK_POINTER.json` — selects the conversational primary attempt and preserves parallel/deferred tracks.
2. The named active checkpoint — recovery authority for exact branch, active substep, next action, blockers and completion gate.
3. `CURRENT_IMPLEMENTATION_STATUS.json` — compact derived projection that must remain consistent with pointer/checkpoint.
4. `PPIA_PROGRAM_BACKLOG.json` — current PPIA tranche/order/status/completion-gate authority.
5. `ROADMAP_INDEX.json` — work-item-to-governing-roadmap/dependency navigation map, not an activity log.
6. Bootstrap + checkpoint-efficiency + completion-integrity policies — recovery, checkpoint cadence and evidence-before-claim rules.
7. `INTERACTION_OPERATIONAL_SCORECARD.json` — historical deterministic control-health evidence for its recorded pilot, not live work-state.
8. `tools/continuity_state.py` — mechanical pointer/checkpoint/status/evidence consistency validator.
9. `governance/ci-failures/INDEX.md` on `ci/failure-records` — historical failure diagnostics; not an automatic current blocker.
10. GitHub commit/PR/workflow evidence — exact candidate identity, hosted validation, mergeability, merge and signature evidence.

## Authority precedence

The console must visibly distinguish five layers:

1. canonical repository authority;
2. active-attempt repository state and exact candidate evidence;
3. derived repository projections;
4. tool observations/evidence;
5. generated development aids.

A lower layer may summarize, index, transform or evidence a higher layer. It may not silently replace it.

For unfinished work, a newer internally consistent active-attempt branch checkpoint/substantive branch state may control recovery over an older `main` projection under the bootstrap's branch-versus-main rule. That does not turn the branch into `completed_verified`.

## Status model

Raw tool semantics remain visible instead of being flattened into one generic green/red state:

- `PASS`, `WARN`, `FAIL`, `BLOCK`;
- `PREPARED`, `READY_TO_EXECUTE`, `BLOCKED` for task capsules;
- `UNDECLARED`, `DECLARED`, `PROVEN` for traceability;
- repository lifecycle states including `started`, `in_progress`, `validation_failed`, typed blocked states, `ready_for_review`, and `completed_verified`.

The console may normalize these for filtering, but it must retain the producing tool's raw state and meaning.

## Evidence receipt model

Candidate-bound evidence must display at least:

- producing tool/workflow;
- repository and exact candidate/source ref;
- execution scope;
- raw result;
- run/timestamp identity;
- source roots/inputs;
- producer-defined digest when available;
- whether authoritative mutation occurred;
- authority limitations.

A screenshot, trace, workflow pass, scenario receipt or recovery result from an older candidate stays historical evidence for that candidate. It is visibly stale for a later candidate rather than silently reused.

## Findings model

Every finding retains:

- source;
- raw severity/state;
- summary and scope;
- exact source locator;
- candidate/input identity;
- blocking effect;
- resolution/next action.

Historical CI failures are diagnostic history. They become current blockers only when the active attempt or a current required gate binds to them.

## Initial information architecture

Foundation defines ten semantic screens:

1. **P16-SCR-001 — Developer Cockpit Overview**
2. **P16-SCR-002 — Current Work & Scope Authority**
3. **P16-SCR-003 — Repository Health & Preflight**
4. **P16-SCR-004 — Fixtures & Scenario Laboratory**
5. **P16-SCR-005 — Privacy & Design Quality**
6. **P16-SCR-006 — UI Evidence Workspace**
7. **P16-SCR-007 — Traceability & Proof Explorer**
8. **P16-SCR-008 — CI, Evidence Receipts & Findings**
9. **P16-SCR-009 — Recovery & Performance Harness**
10. **P16-SCR-010 — Interruption Recovery & AI-Team Handoff**

The IA includes persistent repository/ref/candidate/work-item context and an always-visible nonactivation/authority strip.

Detailed screen state, action enablement/confirmation, component interaction, keyboard/mobile, loading/empty/error/recovery variants and deterministic reference cases are intentionally deferred to the next PPIA-16 bounded substep.

## Initial workflow coverage

Foundation defines twelve end-to-end operator workflows:

- resume interrupted governed work;
- assess repository readiness and scope;
- prepare a bounded AI/Codex task;
- inspect/project governed fixtures;
- run deterministic scenario/replay;
- scan permission leakage;
- capture/harvest exact-candidate UI evidence;
- audit/ratchet design compliance;
- explore traceability/proof;
- run recovery/performance evidence;
- review exact-head CI/evidence gate;
- triage a blocking finding and recover the exact next action.

Every one of the sixteen owner-approved PPIA-16 cockpit concerns is mapped to at least one screen and workflow, and every DT-001 through DT-010 tool is mapped to a screen/workflow.

## Known source staleness

`PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md` correctly contains the PPIA-16 tranche definition, but its later historical **Current tranche** paragraph still names PPIA-03.

That paragraph is stale. `PPIA_PROGRAM_BACKLOG.json`, the PPIA-16 checkpoint, current-work pointer and verified PPIA-15→PPIA-16 transition evidence control current state.

Foundation records this as a provenance/health condition rather than using stale prose as current authority. Routine roadmap/program prose is not rewritten merely as checkpoint bookkeeping.

## Foundation exit boundary

Foundation is ready for its dedicated validation gate when:

- the ten DT source entries and immutable app anchor are present;
- all ten tool contracts retain their authority/non-authority boundaries;
- the AIOC control-source inventory is complete;
- authority precedence, raw status semantics, evidence receipts, findings and interruption-recovery models are explicit;
- all sixteen PPIA-16 requirements map to the initial IA;
- ten semantic screens and twelve operator workflows are present;
- all DT-001 through DT-010 tools have screen/workflow coverage;
- the stale-program-prose condition is recorded without overriding current repository state;
- no runtime/A2/release/deployment/tester/paid/credential/canonical-promotion authority is introduced.

Passing Foundation validation advances PPIA-16 to the detailed **Screen States / Action Contracts / Reference Cases** design substep. It does not complete PPIA-16.
