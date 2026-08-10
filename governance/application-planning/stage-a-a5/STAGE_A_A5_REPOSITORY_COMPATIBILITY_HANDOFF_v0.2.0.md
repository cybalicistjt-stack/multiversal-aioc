# STAGE-A-A5 Repository Compatibility Handoff v0.2.0

**Stage:** STAGE-A-A5 — Campaign and Scene Workspace  
**Status:** PREIMPLEMENTATION ONLY — NOT ACTIVATED  
**Application repository inspected:** `cybalicistjt-stack/Multiversal-app`  
**Verified app main:** `dced7f92163050690c807c1fda937146bb8dce85`  
**Prepared package:** `STAGE_A_A5_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`  
**Package SHA-256:** `fd5afc623feed86ea1af88cd915c881fe64b315f50032c2f2a28c92a936cf36e`

## Validation result

`STAGE-A-A5 REPOSITORY COMPATIBILITY + CONTRACTS v0.2.0: PASS`

- current repository/foundation anchors: 24
- blocking gaps/risks: 14
- planned A5 provider-neutral contracts: 17
- exact future path actions: 40
- reuse/composition decisions: 14
- validation/CI lanes: 17
- nested source-backed A5 preimplementation package: v0.1.0

## Compatibility decision

The current application repository is compatible with additive A5 Campaign/Scene/Session contracts and persistence.

Existing foundations to preserve and compose include provider-neutral persistence/migrations, Campaign authorization, entitlements, authoritative Session command handling, ordered realtime delivery, hidden-information projection, checkpoint/reconnect restoration, backup/restore/export, media/session domain boundaries, and the A1 client shell.

The missing A5 domain layer includes Scene/placement/note persistence, invitation/delegation lifecycle, F005 repository ports, role-safe Campaign/Scene projections, exact pack-lock service boundary, immutable launch snapshots, and exactly-once launch orchestration.

## Frozen implementation rules

1. A5 may not activate until A2, A3, and A4 are `completed_verified` and current repository authority advances.
2. A5 must reuse A2 governed object Picker/selection receipts, A3 identity/workspace context, and A4 Character lifecycle/control. It must not recreate those systems.
3. Existing `database/migrations/0001_initial_logical_schema.json` is immutable. A5 persistence must be the smallest additive provider-neutral migration against the then-current schema.
4. Campaign-local placements reference but never mutate governed source Definitions. Source Definition IDs and placement IDs remain separate.
5. Authorization/entitlement evaluation occurs before projections, counts, previews, media access, search results, diagnostics, exports, and optional AI context.
6. A Session launches only from an immutable validated launch snapshot. Later Scene draft edits do not mutate the active Session.
7. Session launch is exactly-once and ambiguous outcomes are resolved by operation-status lookup, not blind retry.
8. Realtime is advisory. Durable Events, projections, and checkpoints control recovery.
9. Assistant-GM authority is explicitly delegated/scoped/expiring. Owner/Admin operational authority is not blanket private-play access.
10. Offline authoritative Campaign/Scene/invitation/membership/control/pack/snapshot/Session/migration/export-finalization mutation remains forbidden.
11. Media scope is bounded reference metadata plus required nonvisual alternative; no advanced map platform is introduced in A5.
12. A5 stops at the launched Session shell. A6 owns action proposal/GM approval/result authority.

## Authority boundary

- A2 remains the current application work item.
- A3, A4, and A5 are preparation-only.
- No A5 application branch is authorized or created by this handoff.
- No production provider, credential, paid service, real-user-data collection, internal-alpha release, deployment, public release, or canonical promotion is authorized.
- Parallel Design Standards work is untouched.
