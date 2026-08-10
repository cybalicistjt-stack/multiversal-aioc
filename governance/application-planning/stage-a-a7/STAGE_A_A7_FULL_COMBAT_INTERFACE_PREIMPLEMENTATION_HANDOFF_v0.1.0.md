# STAGE-A-A7 Full Combat Interface — Preimplementation Handoff v0.1.0

**Status:** PREIMPLEMENTATION ONLY — NOT ACTIVATED  
**Owner/final authority:** John Brandon Turner  
**Prepared:** 2026-08-10  
**Application repository preparation anchor:** `dced7f92163050690c807c1fda937146bb8dce85`

## Source authority

This preparation is grounded in the merged canonical IA-D06-001 / MV-IA-F007 Full Combat Interface design from PR #167, exact source head `30989b5a0aad24f023054087795e4c4cedb7236b`.

Canonical source metrics preserved:

- 10 encounter states;
- 8 participant types;
- 9 timing types;
- 13 Effect processors;
- 24 deterministic fixtures (`CBT-FX-001` through `CBT-FX-024`);
- 8 implementation slices (`CBT-S01` through `CBT-S08`);
- 28 blocking acceptance IDs (`CBT-AC-001` through `CBT-AC-028`);
- 7 resolved findings;
- 0 blocking findings.

The source publishes the acceptance IDs but not their individual criterion wording in the fetched machine-readable matrix. This preparation preserves those IDs and does not fabricate missing wording.

## Prepared package

`STAGE_A_A7_FULL_COMBAT_INTERFACE_PREIMPLEMENTATION_v0.1.0.zip`

SHA-256: `752020c7e5f7fd328fac9ee075865fc69dbd4c425440c31697a94dc12860307a`

Package validator result:

`STAGE-A-A7 FULL COMBAT PREIMPLEMENTATION v0.1.0: PASS`

`states=10 participants=8 timing=9 effects=13 fixtures=24 criteria=28 slices=8 gates=16`

## Governing implementation boundary

A7 extends the first playable Action/GM approval loop into complete encounter execution. It does **not** create a second proposal/approval engine.

A6 remains the controlling Action authority for:

- Action proposal evidence;
- GM inspect / approve / deny / modify-and-approve;
- attributable final decision receipts;
- atomic accepted Action result commits;
- status lookup, recovery and authoritative result/history semantics.

A7 adds combat-specific orchestration around that authority:

- Session-scoped encounter lifecycle;
- typed combat participants and controller assignments;
- profile-defined rounds, turns, phases, reactions, interrupts, simultaneous groups, environmental pulses and encounter-end windows;
- deterministic target sets;
- semantic positioning and movement;
- Resource costs/reservations;
- typed Effect and Condition processors;
- reactions and interrupts;
- hazards and environmental pulses;
- defeat, withdrawal and profile-defined death/destruction boundaries;
- explicit encounter completion;
- Player and GM combat presentation;
- reconnect, Event-gap recovery, revocation and role-safe projections.

## Required predecessor sequence

A7 is dependency-gated behind:

1. A2 — Universal Object Experience;
2. A3 — Identity, Dashboard, and Workspace Selection;
3. A4 — Character Workspace;
4. A5 — Campaign and Scene Workspace;
5. A6 — First Playable Action and Approval Loop.

No A7 application branch may be created or activated until those predecessors are `completed_verified` and current repository authority advances to A7.

## Important semantic rules

- Combat is an authoritative Session-scoped state machine.
- Clients propose intent and render role-safe projections; presentation state is never combat authority.
- NPC/enemy Actions use the same governed proposal, review, result and history path as Player Actions.
- Position authority is semantic; pixels, token coordinates, dragging, color and animation are presentation aids unless an explicitly bound rules profile maps them to semantic state.
- One accepted Action creates one authoritative result group; every cost and Effect commits atomically or the result group fails without partial mutation.
- Reaction claims are advisory until accepted; exactly one accepted resolution path controls each reaction slot.
- Hidden targets, modifiers, eligibility, topology, counts, previews, notifications, exports, diagnostics and optional-AI context are filtered before projection.
- Defeated, incapacitated, dying, dead, destroyed, surrendered, fled, removed and unavailable remain distinct profile-defined states. Zero Health or another zero Resource does not universally imply death.
- Encounter completion is explicit and attributable. It does not itself grant loot, Assets, XP, advancement, faction standing or canonical changes.
- Realtime is advisory; durable ordered Events and current server projections control recovery.
- Offline authoritative combat mutation is prohibited.

## Scope boundary

A7 stops at a complete runnable encounter without development-only interfaces.

It does not absorb:

- A8 inventory ownership, equipment/crafting/shared Asset lifecycle and broad vehicle Asset operations;
- advanced precision-map authoring, fog-of-war authoring, dynamic lighting or precision-canvas-only authority;
- irreversible Character loss without the bound rules profile and existing authority;
- AI decision, Action-selection, hidden-state, Event-commit or canonical-outcome authority.

## Authority holds

This preparation does **not** authorize:

- A7 application implementation or activation;
- an A7 application branch;
- paid services;
- production credentials;
- real-user data collection;
- internal-alpha tester access or release;
- production deployment;
- public release;
- irreversible Character loss;
- canonical promotion.

## Current application sequence

`STAGE-A-A2` remains the authorized current next application item. A3 through A7 remain preparation-only.

## Exact next non-Codex preparation item

Build the **A7 repository-compatibility + implementation-contract package**, mapping `CBT-S01` through `CBT-S08` onto the current P9 Session/Event/realtime/reconnect/security foundations and the prepared A2-A6 implementation seams, including exact repository path targets, combat persistence gaps, timing/reaction contracts, semantic positioning boundaries, A6 reuse points, tests and CI.