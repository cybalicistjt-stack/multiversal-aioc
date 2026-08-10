# Stage A — A5 Campaign and Scene Workspace — Preimplementation Handoff v0.1.0

**Status:** PREIMPLEMENTATION ONLY — NOT ACTIVATED  
**Owner/final authority:** John Brandon Turner  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Application main verified at preparation:** `dced7f92163050690c807c1fda937146bb8dce85`  
**Canonical source feature:** `MV-IA-F005 — Campaign, Scene, and Session Builder`  
**Source design status:** implementation-ready / complete-design-implementation-ready  
**Prepared artifact:** `STAGE_A_A5_CAMPAIGN_SCENE_WORKSPACE_PREIMPLEMENTATION_v0.1.0.zip`  
**Artifact SHA-256:** `1ec83b7564e2da8f43b15d554522661099bde17f094ffacb6bc2b796e32c7a98`

## Frozen source-backed dimensions

- 24 shared-foundation contracts;
- 9 aggregate types;
- 10 field/projection classes;
- 24 validation classes;
- 31 operation types;
- 31 durable Event types;
- 13 recovery states;
- 42 explicit denied cases;
- 13 required source fixtures;
- 55 bounded fixture/denial rows;
- 20 blocking `CSS-AC-001` through `CSS-AC-020` acceptance criteria with canonical source topics and traceability;
- 8 source implementation slices `CSS-IMP-01` through `CSS-IMP-08`;
- 17 required provider-neutral ports;
- 13 required evidence classes;
- 7 zero-service requirements;
- 0 blocking design findings.

## Non-negotiable architecture

1. A Session launches only from an immutable validated launch snapshot.
2. Mutable Scene drafts do not become live Session authority after launch.
3. Campaign-local placements reference but never mutate reusable source Definitions.
4. `placementId`, source Definition ID, `snapshotId`, `sceneId`, and `sessionId` remain distinct identities.
5. Authorization and entitlement projection occurs before hidden Campaign, Scene, note, placement, count, media, preview, export, diagnostic, or AI output.
6. Realtime delivery is advisory; durable Events and current server projections control recovery.
7. Campaign membership, role, Character control, ownership, observer access, Assistant-GM delegation, entitlement, and support access remain separate decisions.
8. Offline authoritative Campaign/Scene/invitation/membership/pack/snapshot/Session mutation is forbidden.
9. A2 Universal Object Experience, A3 identity/workspace context, and A4 Character workspace remain required predecessor implementations.

## Authority boundary

This handoff does **not**:

- activate A5;
- create an A5 application branch;
- change the application current-work pointer;
- supersede A2, A3, or A4 sequencing;
- implement Campaign, Scene, Session, invitations, or persistence;
- authorize A6 action/approval, A7 combat, A8 inventory, or A9 investigation/social scope;
- authorize production providers, credentials, spending, real-user data, canonical promotion, internal-alpha release, production deployment, or public release.

The parallel Design Standards work pointer remains independent and must not be rewritten by this preparation branch.

## Exact next preparation step

Build the A5 repository-compatibility and implementation-contract package against the actual application repository, mapping the eight canonical F005 implementation slices onto existing Campaign authorization, A3/A4 planned dependencies, persistence/migration, pack/entitlement, A2 Picker, Session Event/realtime/reconnect, media, UI, test, and CI foundations. Keep A5 unactivated.