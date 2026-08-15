# STAGE-A-A7 — Current Repository Revalidation v0.3.0

**Stage:** STAGE-A-A7 — Full Combat Interface  
**Status:** PASS — READY_FOR_BOUNDED_A7_ACTIVATION  
**Owner/final authority:** John Brandon Turner  
**Application product predecessor:** `cybalicistjt-stack/Multiversal-app@79425943f25cce347abcfd2c0abb721005d7a772`  
**Application current main at revalidation:** `cybalicistjt-stack/Multiversal-app@6272a19d09145f4a3e76af74f00f8733a13301f9`  
**A6 predecessor:** `COMPLETED_VERIFIED`, PR #141, verified squash merge `79425943f25cce347abcfd2c0abb721005d7a772`  
**A6 closure receipt:** `Multiversal-app/receipts/STAGE-A-A6-CLOSURE.json`  
**Recovered A7 branch:** `governance/stage-a-a7-preimplementation`  
**Recovered branch tip:** `2a0ba54381168f34551d0a2775e6ede3030c8585`  
**Recovered preimplementation package:** `STAGE_A_A7_FULL_COMBAT_INTERFACE_PREIMPLEMENTATION_v0.1.0.zip`  
**Recovered preimplementation SHA-256:** `752020c7e5f7fd328fac9ee075865fc69dbd4c425440c31697a94dc12860307a`  
**Recovered compatibility package:** `STAGE_A_A7_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`  
**Recovered compatibility SHA-256:** `8bfcddd2d97c73c7dd298404dd03492313a47fc67a86ddf72286c8818cb7b6b2`  
**Recovered 46-path plan SHA-256:** `e38bcd8bd50c1fe394a89b04b12118daf7fe4d86c06f98a3550738eb20faf6af`  
**Current changed-path authority:** `A7_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv`  
**Current scope SHA-256:** `e0643fce17d27d05d49a0c34389b189865a726957a6f12e9e167d59d72686517`  
**Current scope rows:** 95  
**Current dispositions:** 47 CREATE / 45 REUSE / 2 WRAP / 1 MODIFY_BOUNDED  
**Release/deployment/provider/vendor/paid-service authority:** NONE

## Revalidation verdict

`PASS — READY_FOR_BOUNDED_A7_ACTIVATION`.

The recovered A7 architecture remains compatible with the verified post-A6 application repository. All five Stage A predecessors A2–A6 that were historical blockers are now implemented and verified. The remaining historical gaps are bounded A7 combat work, not missing external prerequisites. No provider, vendor, paid service, production credential, deployment, tester-access, release, irreversible Character-loss decision, or canonical-promotion decision is required to begin provider-neutral A7 construction.

The historical preparation is not merged wholesale. It remains provenance and design input. This v0.3.0 current-repository record, its exact path authority, and live repository evidence control activation.

## Exact recovered evidence

The retained project-source archives were recovered byte-for-byte from `Pre-A2.zip`. Their SHA-256 values match the repository-recorded handoffs:

- v0.1.0 preimplementation: `752020c7e5f7fd328fac9ee075865fc69dbd4c425440c31697a94dc12860307a`;
- v0.2.0 compatibility/contracts: `8bfcddd2d97c73c7dd298404dd03492313a47fc67a86ddf72286c8818cb7b6b2`;
- historical 46-action repository path plan: `e38bcd8bd50c1fe394a89b04b12118daf7fe4d86c06f98a3550738eb20faf6af`.

The source-frozen A7/F007 dimensions remain:

- 10 encounter states;
- 8 participant types;
- 9 timing types;
- 13 Effect processors;
- 24 deterministic fixtures (`CBT-FX-001` through `CBT-FX-024`);
- 8 implementation slices (`CBT-S01` through `CBT-S08`);
- 28 blocking acceptance IDs (`CBT-AC-001` through `CBT-AC-028`);
- 20 provider-neutral A7 contracts;
- 18 historical compatibility gaps/risks;
- 16 reuse/composition decisions;
- 20 historical blocking validation/CI lanes.

The source publishes the 28 acceptance IDs but not their individual criterion wording in the recovered machine-readable matrix. This revalidation preserves those IDs and does not fabricate missing criterion wording.

## Current repository facts

- A2 Universal Object Experience is `COMPLETED_VERIFIED`; current governed Picker and Inspector surfaces are reusable Action/source selection and rule-inspection authority.
- A3 Identity/Dashboard/Workspace is `COMPLETED_VERIFIED`; current stable-subject, fresh workspace-entry, selected-context and scoped delegation/support contracts are present.
- A4 Character Workspace is `COMPLETED_VERIFIED`; current Character lifecycle/control/current-version/Resource/Condition persistence and role-safe projection contracts are present.
- A5 Campaign and Scene Workspace is `COMPLETED_VERIFIED`; current immutable launch snapshot, Session shell, authorization projection, Event projection and operation-status seams are present.
- A6 First Playable Action and Approval Loop is `COMPLETED_VERIFIED`; proposal, validation, GM decision, modify-and-approve evidence, status/reconnect, role projection, GM-actor self-review, durable Action Events and ten-write atomic commit are real implementation seams.
- `A6ToA7ActionResultHandoff` explicitly sets `resultAuthoritative: true` and `combatBreadthAuthority: false`; A7 receives only a committed Action result plus durable cursors and retains initiative, movement, reactions, interrupts, area templates, encounter end, rewards and defeat breadth.
- the A6 atomic result path remains authoritative: only an all-or-none ten-write transaction with durable `ActionResultCommitted` creates an accepted Action result. A7 coordinates combat state around that authority rather than replacing it.
- the migration chain is now `0001_initial_logical_schema.json` → `0002_character_workspace.json` → `0003_a5_campaign_scene.json` → `0004_a6_action_approval.json`; therefore the smallest additive A7 migration is `0005_a7_combat_runtime.json`.
- `packages/contracts/src/combat-initiative/README.md` is still only a WP-006 placeholder and explicitly contains no contract implementation, schema, fixture data, test logic or feature code. It is context, not an existing A7 runtime.
- the generic authoritative Session command handler still emits the full command payload in a public `command.accepted:*` Event. Combat payloads can contain protected targets, modifiers, eligibility evidence and GM-only state, so A7 must wrap this lower-level authorization/idempotency/revision pattern rather than directly publish its generic Event.
- the generic hidden-information response filter still returns `hiddenEventCount` after authorization. F007 protected-cardinality/inference-safety therefore remains a blocking A7 projection rule: unauthorized combat projections, previews, queues, notifications, exports, diagnostics and optional-AI context must not expose protected existence/count/rank.
- no A7 application branch exists at revalidation time. No A7 runtime, A7 migration, A7 UI, A7 tests or A7 focused CI exists on application `main`; those are intended A7 construction, not missing prerequisites.

## Historical gap disposition

| Historical gap | Current disposition | Current rule |
|---|---|---|
| A7-GAP-001 no combat persistence family | RETAIN AS A7 WORK | Add the smallest provider-neutral `0005_a7_combat_runtime.json` plus encounter/participant persistence contracts; preserve 0001–0004. |
| A7-GAP-002 no combat runtime ports/state machine | RETAIN AS A7 WORK | Add the 20 source-defined A7 contracts across CBT-S01..S08; do not repurpose the WP-006 placeholder as implementation. |
| A7-GAP-003 A2 not implemented | RESOLVED | Reuse current A2 Picker/Inspector and governed Action/source identity; no parallel Action catalog. |
| A7-GAP-004 A3 not implemented | RESOLVED | Reuse current stable subject, fresh workspace entry, selected context and scoped delegation/support authority. |
| A7-GAP-005 A4 not implemented | RESOLVED | Reuse Character lifecycle/control/current-version/Resource/Condition authority and role-safe projection. |
| A7-GAP-006 A5 not implemented | RESOLVED | Bind encounter bootstrap and recovery to current immutable launch snapshot and launched Session shell. |
| A7-GAP-007 A6 not implemented | RESOLVED + BOUNDARY STRENGTHENED | Reuse actual A6 proposal/decision/status/recovery/atomic-result contracts and `A6ToA7ActionResultHandoff`; never create a second approval engine. |
| A7-GAP-008 F012 encounter readiness is not runtime seam | RETAIN AS DESIGN INPUT / A7 WORK | Consume encounter/balance design and fixture inputs, but A7 owns executable Session-scoped combat runtime authority. |
| A7-GAP-009 generic P9 accepted command exposes public payload | RETAIN — CRITICAL PRIVACY BOUNDARY | Wrap the generic command-authority pattern; emit combat-specific role-safe durable Events and never expose raw hidden combat payload through the public accepted Event. |
| A7-GAP-010 generic hidden filter exposes `hiddenEventCount` | RETAIN — CRITICAL INFERENCE BOUNDARY | Wrap the filter; authorization precedes projection and protected combat counts/rank/topology/eligibility are omitted unless explicitly authorized. |
| A7-GAP-011 no controller assignment runtime | RETAIN AS A7 WORK | Add fresh controller assignment and delegation-aware participant control; no client/presentation control is authoritative. |
| A7-GAP-012 no profile-defined order/timing | RETAIN AS A7 WORK | Add deterministic profile-defined rounds/turns/phases/simultaneous groups/reaction/environment windows. |
| A7-GAP-013 no semantic positioning/target service | RETAIN AS A7 WORK | Add target eligibility plus semantic zone/range/elevation/cover/occupancy authority; pixels and dragging remain presentation. |
| A7-GAP-014 no reaction/interrupt claim engine | RETAIN AS A7 WORK | Claims remain advisory until accepted; exactly one accepted resolution path controls each reaction slot. |
| A7-GAP-015 no 13-Effect registry/cross-domain coordinator | RETAIN AS A7 WORK | Add the source-defined 13 Effect processors and Condition/Resource adapters around A6 atomic Action authority. |
| A7-GAP-016 no defeat/withdrawal/completion receipt | RETAIN AS A7 WORK | Preserve distinct profile-defined outcome states and explicit attributable encounter completion; no automatic rewards/canonical mutation. |
| A7-GAP-017 no combat-specific responsive/accessibility UI | RETAIN AS A7 WORK | Add Player/GM combat views, semantic order/position controls and keyboard/touch/screen-reader/high-zoom parity. |
| A7-GAP-018 reconnect lacks combat windows/claims/controllers/status | RETAIN + COMPOSE CURRENT RECOVERY | Compose P9/A5/A6 checkpoint, Event-gap and status recovery with A7 order/reaction/controller/current-projection authority. |

No blocking gap remains outside intended A7 implementation scope.

## Current path-plan reconciliation

The historical 46 actions remain traceable but are not copied literally. The current scope contains 95 unique rows because current repository reality requires:

1. replacing historical `database/migrations/<next>_a7_combat_runtime.json` with exact `database/migrations/0005_a7_combat_runtime.json`;
2. preserving all 20 planned provider-neutral A7 contracts as explicit current CREATE paths;
3. replacing broad historical `packages/contracts/src/a6/**` with explicit current A6 proposal, validation, decision, modification, atomic commit, status, reconnect, Event, projection, GM-actor and A6→A7 result-handoff seams;
4. replacing broad historical `packages/contracts/src/a4/**` with exact Character control/repository/projection/calculation/validation/persistence paths;
5. replacing broad historical `apps/client-ui/src/a2/**` with the current Picker and Inspector seams;
6. explicitly consuming A3 stable subject/workspace/delegation/context; A5 immutable launch snapshot/Session shell/authorization/Event/status; and provider-neutral entitlement/persistence/realtime/checkpoint/audit/export foundations;
7. treating `packages/contracts/src/combat-initiative/README.md` as REUSE context only because it remains an explicit no-implementation placeholder;
8. wrapping both the generic authoritative command handler and generic hidden-information filter: the former can publicly expose raw command payload; the latter exposes `hiddenEventCount`;
9. colocating A7 Vitest contract/targeting/atomicity/reaction/privacy/recovery/accessibility/integration tests under `apps/client-ui/src/a7/**` instead of creating a disconnected root `tests/a7/**` island;
10. keeping one bounded `apps/client-ui/src/App.tsx` integration only after the A7 package exists and fresh launched-Session/encounter authorization is satisfied;
11. preserving package/final evidence and closure receipt as later completion-only writes, not construction authority.

Disposition counts are 47 CREATE, 45 REUSE, 2 WRAP and 1 MODIFY_BOUNDED. There is no DELETE, REWRITE or REPLACE action.

## Activation invariants

1. combat is an authoritative Session-scoped state machine; UI/pixels/drag state never becomes authority by accident;
2. A6 remains the sole Action proposal/GM review/approve-deny-modify/decision receipt/atomic accepted-result authority; A7 creates no second proposal engine;
3. A7 accepts only authoritative committed A6 results through the A6→A7 handoff and current durable Session cursors;
4. one accepted Action produces one authoritative result group or none; A7 combat coordination may not create partial authoritative mutation around a failed A6 result;
5. fresh authorization precedes participant/controller lookup, target eligibility, order/reaction queue membership, counts/rank, hidden topology, projection, notification, export, diagnostics and optional AI context;
6. generic Session command authorization/idempotency/revision behavior may be reused internally, but raw hidden combat payload may not escape through its public generic Event;
7. generic `hiddenEventCount` is never surfaced by default through A7 Player/observer/queue/preview/notification/export/analytics/AI projections;
8. current A2 Action/source identity and inspection are reused;
9. current A3 subject/workspace/delegation context is reused and freshly revalidated for protected combat operations;
10. current A4 Character lifecycle/control/current version/Resources/Conditions remain authoritative participant-state inputs;
11. current A5 immutable launch snapshot and Session shell bind the encounter; mutable authoring drafts do not drive live combat truth;
12. reaction/interrupt claims are advisory until accepted, and each reaction slot has exactly one accepted resolution path;
13. target and position authority is semantic: zones/range/elevation/cover/occupancy, not incidental pixels/color/animation;
14. the 13 source-defined Effect processor categories remain profile-governed and execute through bounded adapters;
15. defeated/incapacitated/dying/dead/destroyed/surrendered/fled/removed/unavailable remain distinct profile-defined states; zero Resource is never universal death;
16. encounter completion is explicit and attributable and does not itself grant loot, Assets, XP, advancement, faction standing or canonical changes;
17. realtime remains advisory; durable Events, current server projections, checkpoints and stable status control recovery;
18. offline authoritative combat mutation is prohibited; only previously authorized reads/local presentation state may survive offline;
19. AI has no Action-selection, controller, hidden-state, reaction acceptance, decision, commit or canonical-outcome authority;
20. A7 stops at a complete runnable encounter and does not absorb A8 inventory/equipment/crafting/shared Asset lifecycle or broad vehicle operations;
21. no new UI framework/runtime dependency or production service/provider choice is authorized by A7 activation;
22. build meaningful bounded slices before broad CI; use focused checks during construction and predecessor/browser evidence at package/final boundaries.

## Validation plan at activation

The historical 20 validation lanes remain conceptually valid but are updated to current repository structure:

- focused A7 verifier lanes for encounter contracts, controller/timing, targeting/semantic position, A6 Action integration, atomic combat coordination, reactions/hazards/outcomes, privacy/projection and recovery;
- current persistence, Campaign authorization, entitlement, Session command, realtime, hidden-information, reconnect and structured-audit regression seams;
- current A6 full verifier and A6 Action authority/atomicity/privacy/recovery regressions;
- client TypeScript, focused `apps/client-ui/src/a7/**` Vitest, accessibility and portable build;
- exact-head A1–A6 and DT-008 predecessor regressions at the bounded package/final gate rather than after every small mutation;
- real-browser package evidence for keyboard/touch/accessibility, manual/offline denial, role-safe Player/GM projections, semantic movement/targeting, A6 Action→combat result, reactions and responsive/high-zoom behavior.

## Activation decision

A7 may be activated on a fresh application branch from current `Multiversal-app@6272a19d09145f4a3e76af74f00f8733a13301f9` only after this revalidation package passes its focused repository validator and merges to AIOC `main`.

The application work order must copy exact current scope SHA `e0643fce17d27d05d49a0c34389b189865a726957a6f12e9e167d59d72686517`, retain verified A6 product predecessor `79425943f25cce347abcfd2c0abb721005d7a772`, and preserve `releaseAuthorized=false`, `deploymentAuthorized=false`, `providerVendorPaidServiceAuthorized=false`.

A8–A12 remain sequential future stages. The separate WP-011 Apple track and unfinished Design Standards exact-byte ingestion track remain untouched.
