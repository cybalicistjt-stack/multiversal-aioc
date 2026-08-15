# STAGE-A-A5 — Current Repository Revalidation v0.3.0

**Stage:** STAGE-A-A5 — Campaign and Scene Workspace  
**Status:** PASS — READY_FOR_BOUNDED_A5_ACTIVATION  
**Owner/final authority:** John Brandon Turner  
**Application repository baseline:** `cybalicistjt-stack/Multiversal-app@90f84cfd4b9f00be3eee560530560a6c3cc28ab6`  
**A4 predecessor:** `COMPLETED_VERIFIED`, PR #138, squash merge `38f47a8aa7a5a921fb72a7365dfa6c3f0ea94c31`  
**Recovered A5 branch:** `governance/stage-a-a5-preimplementation`  
**Recovered branch tip:** `ca93ea4588d1380da596f19d0a89f76ffdf28767`  
**Recovered compatibility package:** `STAGE_A_A5_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`  
**Recovered package SHA-256:** `fd5afc623feed86ea1af88cd915c881fe64b315f50032c2f2a28c92a936cf36e`  
**Recovered 40-path plan SHA-256:** `72f6c3ee18a028734ba2112e4a921f28768368fd03059a63d8993d74f4a8561c`  
**Current changed-path authority:** `A5_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv`  
**Current scope SHA-256:** `89082bb72bb8097e5f3066c0b88b158e94b3e5b2676bfb7865ff2580e494fd03`  
**Current scope rows:** 57  
**Release/deployment/provider/vendor/paid-service authority:** NONE

## Revalidation verdict

`PASS — READY_FOR_BOUNDED_A5_ACTIVATION`.

The recovered A5 architecture remains compatible with the current post-A4 application repository. No owner-only provider, vendor, paid-service, production-credential, deployment, release, tester-access, or irreversible decision is required to begin bounded provider-neutral implementation.

The historical preparation is not merged wholesale. It remains provenance and design input. This v0.3.0 record and the current application repository control A5 activation.

## Evidence recovered exactly

The retained project-source package was recovered byte-for-byte. Its SHA-256 equals the repository-recorded `fd5afc623feed86ea1af88cd915c881fe64b315f50032c2f2a28c92a936cf36e`. The historical exact path plan contains 40 actions and hashes to `72f6c3ee18a028734ba2112e4a921f28768368fd03059a63d8993d74f4a8561c`.

The historical package defined 17 provider-neutral contracts, 14 reuse/composition decisions and 14 blocking gaps/risks. Its architecture remains the starting point, subject to the current classifications below.

## Current repository facts

- A2 Universal Object Experience is implemented; `apps/client-ui/src/a2/picker/**` is present and controls governed object selection.
- A3 identity/workspace implementation is present, including invitation, delegation/support, selected-context, workspace-entry and inference-safe notification-summary contracts.
- A4 Character Workspace is `COMPLETED_VERIFIED`; `CharacterControlPort` and bounded `character-scene-reference.ts` are present.
- provider-neutral Session foundations remain present: authoritative command handling, ordered realtime delivery, hidden-information filtering and checkpoint/reconnect restoration.
- the logical migration chain is now `0001_initial_logical_schema.json` → `0002_character_workspace.json`; therefore A5's smallest additive migration is `0003_a5_campaign_scene.json`.
- PPIA-08 is `COMPLETED_VERIFIED` and is the later Campaign/Scene/Session authoring overlay, including semantic square/gridless map authoring, versioned calibration, governed placements, dungeon primitive families, permission-before-aggregation, immutable launch snapshot and idempotent recovery requirements.

## Historical gap disposition

| Historical gap | Current disposition | Current rule |
|---|---|---|
| A5-GAP-001 Scene/placement/note/snapshot persistence absent | RETAIN AS A5 WORK | Install the smallest additive provider-neutral `0003` migration; never rewrite 0001/0002. |
| A5-GAP-002 F005 repository ports absent | RETAIN AS A5 WORK | Add A5 feature ports over generic persistence/current Session foundations. |
| A5-GAP-003 A2 not implemented | RESOLVED | Reuse current A2 Picker/selection receipts; no A5 selector fork. |
| A5-GAP-004 A3 not implemented | RESOLVED | Reuse current A3 subject, invitation, delegation, context and entry contracts. |
| A5-GAP-005 A4 not implemented | RESOLVED | Reuse current Character control and Character→Scene reference contracts. |
| A5-GAP-006 Assistant-GM delegation gap | UPDATE/REVALIDATE | A3 now owns generic scoped/expiring delegation. A5 adds Campaign-specific authority binding without inventing blanket role power. |
| A5-GAP-007 invitation lifecycle absent | UPDATE/REVALIDATE | A3 invitation identity/lifecycle is now real. A5 composes it into Campaign membership/role/delegation semantics rather than rebuilding generic invitations. |
| A5-GAP-008 exact pack lock absent | RETAIN AS A5 WORK | Add exact provider-neutral pack/version/dependency lock and pin it into launch snapshot. |
| A5-GAP-009 A5 role-safe projection absent | RETAIN AS A5 WORK | Compose A3 authorization/context + Campaign policy + A4 Character control + entitlement before aggregation/projection. |
| A5-GAP-010 media reference absent | UPDATE WITH PPIA-08 | Keep bounded reference metadata plus semantic nonvisual map representation; no advanced map/runtime platform. |
| A5-GAP-011 immutable launch orchestration absent | RETAIN + STRENGTHEN | Implement immutable exact-version snapshot, operation-id launch and status lookup using existing Session command/recovery patterns. |
| A5-GAP-012 notification service absent | UPDATE/REVALIDATE | Reuse A3 inference-safe notification summaries; A5 adds only bounded invitation/launch/revocation projection. |
| A5-GAP-013 backup/export predates A5 | RETAIN AS A5 WORK | Extend only after A5 records exist; filter authorization before export. |
| A5-GAP-014 A1 shell lacks A5 experience | RETAIN AS A5 WORK | Feature-local `apps/client-ui/src/a5/**` plus one bounded `App.tsx` integration after package construction. |

No blocking gap remains outside the intended A5 implementation scope.

## PPIA-08 overlay adopted at activation

A5 implementation must preserve these completed PPIA-08 requirements where they intersect Stage A runtime:

- map image reference/versioning with square-grid calibration using `cellSizePx`, `originOffsetXPx`, and `originOffsetYPx`;
- square and gridless initial coordinate modes;
- semantic locations represented independently from visual pixels, including cells, multi-cell areas, named zones and gridless locations;
- Campaign-local placement stores stable owning-domain reference (`ownerDomain`, `objectId`, `objectVersion`) plus placement identity/state and never becomes source Definition ownership;
- seven dungeon authoring primitive families remain geometry, not collision/LOS/movement/damage/balance authority;
- permission filtering occurs before protected reference lookup, aggregation, counts, search, errors, export, diagnostics, notification and optional AI context;
- launch pins exact Campaign, Scene, map asset, calibration, placements, visibility policy and Session-binding inputs;
- later draft/map/calibration changes never silently mutate the active Session;
- authoritative writes require expected version and stable operation identity; ambiguous responses use status/current-version lookup before retry;
- visual maps always have semantic nonvisual, keyboard, touch and high-zoom/reflow equivalents.

Owning-domain truth remains outside A5: PPIA-02 Creature/NPC, PPIA-03 Item/Inventory, PPIA-04 Vehicle, PPIA-05 Species/Form, PPIA-11 Encounter/final balance, PPIA-12 reusable Setting. A5 stores references and Campaign-local placement state only.

## Current path-plan reconciliation

The historical 40 actions remain traceable but are not copied literally. The current scope contains 57 rows because current repository reality requires:

1. replacing historical `<next>_a5_campaign_scene.json` with exact `0003_a5_campaign_scene.json`;
2. turning A2/A3/A4 `REUSE_FUTURE` assumptions into concrete present-day reuse paths;
3. composing A3 invitation, delegation, selected-context, workspace-entry and notification contracts rather than duplicating them;
4. composing A4 `character-scene-reference.ts` in addition to Character control;
5. making Campaign/Scene/membership/launch transfer schemas explicit;
6. adding the historically planned-but-not-enumerated `notification-port.ts`, `runtime-utilities.ts`, and `scene-session-handoff.ts` contracts;
7. colocating A5 Vitest privacy/recovery, accessibility and integrated tests under the client source tree rather than creating a disconnected `tests/a5/**` island;
8. adding a bounded persistence fixture family for the new `0003` migration.

Disposition counts are 42 CREATE, 14 REUSE and 1 MODIFY_BOUNDED. There is no DELETE or destructive migration action.

## Activation invariants

1. immutable launch snapshot is separate from mutable Campaign/Scene drafts and from Session identity;
2. `placementId`, owning source Definition ID/version, `sceneId`, `snapshotId`, `sessionId`, map asset version and calibration version remain distinct;
3. authorization precedes lookup/aggregation/projection/export/diagnostic/notification/AI context;
4. A2 Picker is the governed selection seam;
5. A3 controls stable subject/workspace entry/invitation/delegation context;
6. A4 controls Character lifecycle/control and Character→Scene reference boundary;
7. realtime remains advisory; durable Events/projections/checkpoints govern recovery;
8. exactly-once authoritative operations use stable operation identity and status lookup before retry;
9. offline authoritative Campaign/Scene/invitation/membership/pack/snapshot/Session/final-export mutation is forbidden;
10. A5 stops at the launched Session shell; A6 owns action proposal/GM approval/result authority;
11. no new UI framework/runtime dependency or production service/provider selection is authorized;
12. build meaningful slices before broad CI; use focused checks while constructing and broad predecessor/browser validation only at the package/closure boundary.

## Activation decision

A5 may now be activated on a fresh application branch from `Multiversal-app@90f84cfd4b9f00be3eee560530560a6c3cc28ab6` after this revalidation package passes its focused repository validator and merges to AIOC `main`.

The application work order must copy the exact current scope SHA and preserve `releaseAuthorized=false`, `deploymentAuthorized=false`.
