# STAGE-A-A6 Preimplementation Handoff v0.1.0

**Stage:** STAGE-A-A6 — First Playable Action and Approval Loop  
**Status:** PREIMPLEMENTATION ONLY — NOT ACTIVATED  
**Owner/final authority:** John Brandon Turner  
**Prepared:** 2026-08-10  
**Application repository preparation base:** `dced7f92163050690c807c1fda937146bb8dce85`  

## Canonical source basis

- `STAGE_A_UI_IMPLEMENTATION_PROGRAM.md` — A6 vertical slice and exit condition.
- `MV-IA-F006_FIRST_PLAYABLE_ACTION_AND_GM_APPROVAL_LOOP.md` — implementation-ready F006 design.
- `MV-IA-F006_ACTION_APPROVAL_MATRIX.json` — machine-readable state/field/validation/operation/event/denial/fixture/slice authority.
- `MV-IA-F006_IMPLEMENTATION_TRACEABILITY.json` — acceptance/control/test traceability.
- `MV-IA-F006_COMPLETION_RECORD.json` — design-complete record; implementation still dependency-gated.

## Prepared package

Local artifact: `STAGE_A_A6_FIRST_PLAYABLE_ACTION_PREIMPLEMENTATION_v0.1.0.zip`  
SHA-256: `35676b0fa492fa3d613896645f12f3e9016dd6f7c02bd480c09c68305e93b13b`

Validator result: **PASS**.

Frozen source-backed dimensions:

- 24 required shared contracts;
- 28 preparation contracts;
- 18 canonical Action-loop states;
- 28 Action proposal required fields;
- 20 decision-receipt required fields;
- 28 validation classes;
- 28 operation types;
- 28 durable Event types;
- 40 denied cases;
- 14 deterministic synthetic fixtures;
- 54 bounded fixture/denial rows;
- 10 dependency-ordered F006 implementation slices;
- 20 blocking `FPA-AC-001` through `FPA-AC-020` acceptance criteria with exact source wording;
- 10 atomic accepted-result write classes;
- zero blocking design findings.

## Controlling authority rules

1. The complete slice remains `Campaign → Character → Scene → Action proposal → GM inspection/modification/decision → authoritative Result → synchronized persistent state`.
2. Player Action history and My Proposals remain secondary surfaces.
3. Player available Actions and quick-rule inspection are permission-, entitlement-, actor-, Session-, launch-snapshot-, pack-, schema-, and visibility-filtered before projection.
4. Final GM decision types are exactly `approve`, `deny`, and `modify-and-approve`.
5. Modification preserves the original proposal, records changed fields/final values/reasons/decider authority, revalidates current authority and compatibility, and requires final confirmation.
6. GM-controlled NPC/enemy Actions use the same inspection, decision receipt, atomic commit, and history model before authoritative Effects.
7. Only an accepted durable decision plus atomic `ActionResultCommitted` makes costs, Effects, Resources, Conditions, target-state changes, Session sequence/version, history, notifications, and durable Events authoritative.
8. Realtime messages and notifications remain advisory delivery; durable Events and current server projections control recovery.
9. Stable operation identity and status lookup prevent duplicate submit/decision/commit and handle ambiguous failures before retry.
10. Revocation invalidates protected routes, subscriptions, caches, receipts, queue entries, status lookup, and optional-AI projections.
11. Offline use may retain authorized reads/local drafts only. Offline submit, decide, modify, approve, deny, resource spend, Effect/Condition application, target mutation, Session command, restore/migration/export finalization remain prohibited.
12. AI has no actor-control, decision, modification, approval, denial, commit, support, or authority-widening role.

## Stage dependency boundary

A6 remains sequentially dependent on completed A2, A3, A4, and A5 implementations. This preparation must not be used to bypass their contracts:

- A2 supplies governed Action/object inspection and stable source references.
- A3 supplies subject identity, selected context, role/delegation and workspace authority.
- A4 supplies Character lifecycle/control and Character projection semantics.
- A5 supplies Campaign, Scene, immutable launch snapshot, active Session shell, durable Event/realtime/recovery foundations.

A7 remains responsible for full combat breadth such as initiative/order, movement, reactions, interrupts, area templates, encounter end, rewards, and defeat handling.

## Authority holds

- A2 remains the current application work item.
- A3, A4, A5, and A6 are preparation-only and unactivated.
- No A6 application branch exists.
- No production credential, paid service, real-user-data collection, internal-alpha release, deployment, production, or public release authority is granted.
- No current-work pointer is changed by this handoff.
- The parallel Design Standards publication-ingestion pointer is untouched.

## Exact next preparation action

Build the A6 repository-compatibility and implementation-contract package against the then-current application repository, mapping F006-S01 through F006-S10 onto the existing A5 Session shell, P9 authoritative Session command/Event/reconnect contracts, A4 Character-control state, A3 role/delegation context, A2 object/rule inspection, persistence, projection, UI, tests, and CI without activating A6.
