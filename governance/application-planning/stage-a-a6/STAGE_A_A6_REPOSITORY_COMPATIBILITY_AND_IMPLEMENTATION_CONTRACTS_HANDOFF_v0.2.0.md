# STAGE-A-A6 Repository Compatibility + Implementation Contracts Handoff v0.2.0

**Stage:** STAGE-A-A6 — First Playable Action and Approval Loop  
**Status:** PREIMPLEMENTATION ONLY — NOT ACTIVATED  
**Owner/final authority:** John Brandon Turner  
**Prepared:** 2026-08-10  
**Application repository compatibility base:** `dced7f92163050690c807c1fda937146bb8dce85`  

## Prepared package

Local artifact: `STAGE_A_A6_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`  
SHA-256: `ca80319e0282821f19b7fa4f43e439107bc845f0ececfa2937c8bc5418152d00`

Validator result: **PASS**.

Frozen compatibility dimensions:

- 20 current repository/predecessor anchors;
- 16 blocking gaps/risks;
- 18 planned provider-neutral A6 contracts;
- 42 exact future repository path actions across `F006-S01` through `F006-S10`;
- 15 reuse/composition decisions;
- 18 blocking validation/CI lanes;
- zero new runtime dependencies required;
- zero production-provider requirements.

## Repository compatibility result

**COMPATIBLE WITH ADDITIVE A6 ACTION/APPROVAL CONTRACTS.**

P9 already supplies the generic foundations A6 should reuse:

- provider-neutral Session command/Event/checkpoint/realtime primitives;
- current Campaign authorization;
- command idempotency and exact Session revision checking;
- ordered duplicate-safe realtime Event delivery and gap detection;
- hidden-information projection after authorization;
- trusted checkpoint/reconnect restoration;
- provider-neutral persistence, transactions, migration, backup/restore/export and structured audit patterns.

A6 adds Action-specific proposal, validation, queue/decision, atomic-result, projection, status, reconnect, history/export and GM-actor contracts. It does not replace the P9 foundations.

## Critical compatibility finding — protected cardinality

The current generic hidden-information filter returns a `hiddenEventCount` to an authorized Campaign viewer. F006 separately requires protected proposal, queue and Event existence/count information to remain inference-safe.

Therefore A6 may wrap the generic filter internally but must not surface generic hidden-event cardinality as a Player, observer, queue, notification or analytics value by default. A6 queue counts/ranking and proposal/Event summaries must be computed only after A6-specific authorization and projection.

This is a compatibility requirement, not a change to the already-completed P9 contract.

## Shared proposal/approval component

The completed IA-D04-002 `MV-IA-SS06-PROPOSAL-APPROVAL` contract is a direct A6 design dependency. A6 must reuse its shared component semantics rather than create a second approval framework:

- seven governed consumer profiles;
- twelve component surfaces;
- immutable original accepted proposal;
- advisory review claims;
- approve, deny and modify-and-approve;
- explicit changed paths/original values/final values/reasons;
- explicit final confirmation;
- decision receipt and atomic commit adapters;
- status lookup, reconnect, event-gap and revocation behavior;
- server-side role-safe projection;
- silence is not approval.

F006 remains the consumer-specific authority for its richer 28-field proposal, 28 validation classes, actor/Character/Session/snapshot bindings, Action evidence, and atomic Action result transaction.

## Generic Session-command boundary

`handleAuthoritativeSessionCommand` is necessary but not sufficient for F006. It enforces Campaign authorization, operation identity and exact Session revision, but it does not know:

- actor or Character control/lifecycle;
- immutable launch-snapshot compatibility;
- Action Definition/version/source-pack compatibility;
- hidden/eligible target state;
- Resources, costs and requirements;
- roll evidence and modifier ordering;
- Effect schema;
- Assistant-GM decision delegation;
- proposal staleness or final decision rules.

A6 therefore performs its full authoritative validation before durable proposal creation and again immediately before final decision/atomic commit.

## Atomic result boundary

The A6 accepted-result transaction is all-or-none across the source-defined write classes:

1. final decision receipt;
2. final costs;
3. final Effects;
4. Resource changes;
5. Condition changes;
6. target-state changes;
7. Session sequence/version;
8. Action history;
9. required notifications;
10. durable Events.

Only successful completion plus `ActionResultCommitted` makes those changes authoritative. A failed dependency/write cannot expose a partial accepted result.

## Predecessor boundaries

A6 must consume, not recreate:

- A2 for governed Action/source lookup and rule inspection;
- A3 for stable subject, workspace, role/delegation and selected context;
- A4 for Character lifecycle/control/current Resources/Conditions/version;
- A5 for Campaign/Scene bindings, immutable launch snapshot and active Session shell.

If any implemented predecessor materially differs from these prepared contracts, repository compatibility must be refreshed before A6 activation.

## Authority holds

- A2 remains the current application work item.
- A3, A4, A5 and A6 remain preparation-only and unactivated.
- No A6 application branch exists.
- No new runtime dependency, provider SDK, production provider, paid service, production credential, real-user-data collection, internal-alpha release, deployment, production or public-release authority is granted.
- No current-work pointer is changed by this handoff.
- The parallel Design Standards publication-ingestion pointer remains untouched.

## Exact next preparation action

Prepare **Stage A7 — Full Combat Interface** from the completed combat design sources, preserving A6 as the underlying action/approval authority and adding only the combat-specific initiative/order, participant, movement, resource/condition, NPC/enemy, reaction/interrupt, encounter-history and encounter-lifecycle contracts defined by the canonical design.
