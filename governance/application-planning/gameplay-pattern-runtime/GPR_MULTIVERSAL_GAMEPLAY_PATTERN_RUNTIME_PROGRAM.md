# GPR — Gameplay Pattern Runtime & Loop Minis

**Program ID:** GPR  
**Program name:** Gameplay Pattern Runtime & Loop Minis  
**Version:** 0.2.0 — PDCP REDUCED  
**Status:** ACTIVE — GPR-09 SELECTED_NOT_STARTED  
**Activation:** concurrent start authorized after MRCS-05 + completed MAL + core owner contracts; later MRCS late-binds; GPR-16 waits for MRCS-21  
**Successor:** MERA-01  
**Owner and final authority:** John Brandon Turner  
**Implementation authority:** none until an owner GPR execution command starts the CURRENT-selected GPR-09 attempt

## Purpose

GPR turns the completed MAL microgame foundation plus the 175-game clean-room gameplay study into one reusable Multiversal gameplay-pattern runtime. It lets accepted rules, Characters, maps, Assets, encounters and campaign state become playable loops without one bespoke engine per minigame, genre or feature family.

The governing flow remains:

`accepted owner-domain state + accepted MRCS definitions + semantic pattern configuration + authorized presentation bindings → gameplay instance → typed Events/outcomes → owner-domain handoff`

GPR is an execution/composition layer, not a second Character, World, Scene, Combat, Inventory, Economy, Project, Action/Event, content-authoring, rights/provenance, map or audio owner.

## PDCP reduction

The historical 16-tranche roadmap is preserved in `PDCP_GPR_REDUCTION_RECEIPT.json`. After intra-family and cross-family overlap closure, future repository-bound work is reduced to ten sparse tranches:

`GPR-01 → GPR-03 → GPR-05 → GPR-06 → GPR-07 → GPR-08 → GPR-09 → GPR-10 → GPR-12 → GPR-16`

The reduction preserves `GPR-01` as the family start gate, `GPR-05` as the existing MERA rotation milestone and `GPR-16` as the family golden/downstream handoff gate. No DAG rewrite is required.

## Existing owner boundaries

- **MAL-01..10** remain completed_verified and frozen. GPR extends broad pattern coverage without reopening MAL completion evidence.
- **MRCS** remains reusable rule/content-definition authority. GPR imports and executes accepted definitions.
- **Action/Event and domain owners** remain canonical mutation truth for Characters, Combat, Inventory/Assets, Economy, Progression, World/Scene/Map, Vehicles/Mounts, Projects/Time and other governed domains.
- **ARI/PCA** retain generic resource identity, rights, derivative provenance, version/review/import-export infrastructure.
- **MCS/MCCS/MNCS/MSAS** retain map, presentation/actor, NPC/creature and audio authoring ownership.
- **Packet 07** owns common preview/commit/explanation/intervention/debug/recovery semantics.
- **PCA-12/Packet 08** own generic simulation/formal-analysis machinery.
- **Reduced MERA/MBES/MSLR/MSWI** consume GPR execution/composition but retain their own specialist state and semantics.

## Research baseline

`GPR_RESEARCH_BASELINE_v3.6.json` remains planning/conformance provenance. Its verified scope includes:

- 175 mined games;
- 168 reusable patterns;
- 461 gameplay primitives;
- 29 mechanics API modules;
- 169 registered mechanics operations, including 85 primitive-bound operations used by canonical patterns;
- 129 semantic presentation roles;
- seven delivery modes;
- 168/168 success-path conformance;
- 672/672 failure/partial/cozy/GM adaptation cases;
- replay/snapshot round-trip evidence and snapshot migration evidence.

The research package is not automatically shippable code or content.

## Core doctrines

1. Composition instead of game forks.
2. Owner-domain truth remains external.
3. MAL remains frozen.
4. Definition is not execution.
5. Reference material is not production content.
6. Mechanics bind semantic roles, not one presentation skin.
7. Direct/cozy/GM/TTRPG/embedded/user-mini/roster modes share one mechanics model.
8. Replay and persistence are versioned and explicit.
9. Multiplayer authority is explicit.
10. User-authored loops are bounded.
11. Unsupported/unknown state fails closed rather than receiving invented fallback semantics.
12. Blocking gameplay remains usable without paid/cloud providers or a mandatory 3D/twitch-only interface.

## Runtime identity/state model

GPR keeps separate:

- accepted reusable Pattern/operation/primitive definitions and versions;
- authored `PatternConfiguration` / loop-mini configuration;
- live `GameplayInstance` identity;
- stable owner-domain participant/Asset/World references;
- delivery-mode configuration/projection;
- authoritative GPR-local runtime state;
- semantic command/input stream;
- typed Event/outcome trace;
- versioned replay/snapshot receipt;
- presentation projection.

A definition is not a live instance. A preview is not a committed owner mutation. A snapshot is not reusable source truth. A presentation role is not an Asset identity.

## Ten bounded implementation/proof tranches

### GPR-01 — Gameplay Runtime Authority, Contract Registry & MAL/MRCS Convergence

Absorbs historical GPR-01 and GPR-02. Implement the GPR runtime authority shell, stable pattern/primitive/operation/asset-role registry projection, MAL/MRCS compatibility import, namespace/schema validation and explicit unsupported states. MRCS remains definition authority.

### GPR-03 — Deterministic Entity, Input, Collision & State Kernel

Implement gameplay-instance state, semantic input abstraction, collision/trigger handling, declared deterministic transition ordering, seed/configuration binding and safe runtime/authoring caps. Presentation frame order is never authoritative state order.

### GPR-05 — Owner-Domain Gameplay Operation, Objective & Route Runtime

Absorbs historical GPR-04 and GPR-05. Implement pattern-level execution adapters for traversal, combat/projectiles, abilities, Resources, interactions, Inventory/equipment, Economy/rewards, Progression/unlocks, objectives/missions and World/Scene routing. Canonical mutation remains with each owning domain.

`GPR-05` remains the existing MERA rotation milestone.

### GPR-06 — Specialist Puzzle, Sports, Vehicle, Party, Strategy, Social & Stealth Pattern Modules

Implement reusable specialist adapters and fixtures for puzzles, sports/match possession, Vehicle/Mount play, parties/companions, tactical/strategy state, social/investigation and stealth/detection. These modules use shared operations and owner contracts rather than bespoke game forks.

### GPR-07 — Encounter, Autonomy, Score/Timing, Loadout & Skill-Resolution Runtime

Implement bounded encounter/autonomous selection, score/timing/rhythm resolution, loadout/build execution and skill-resolution adapters. NPC psychology, AI authority, Character build truth, skill definitions and authored audio remain external owner concerns.

### GPR-08 — Loop-Mini Contract, Pattern Composer & Bounded Authoring Schema

Productize the data-driven loop-mini configuration schema and composer: objectives, maps, participants/roles, operations, Resources, rules, rewards, limits, difficulty/configuration and declared delivery support. Authoring enforces safe caps and emits noncanonical configuration until execution/owner commit.

### GPR-09 — Seven Delivery Modes, Creator/GM Control & World/Roster Binding

Absorbs historical GPR-09 and GPR-14. Implement direct, cozy/low-pressure, GM-led, world-map/TTRPG bridge, embedded minigame, user-authored loop-mini and roster-injection delivery adapters over one state/outcome model. Provide GPR-specific creator/GM test/control surfaces, World/Map/Adventure binding and Character roster injection using Packet-07 shared execution-inspection semantics.

### GPR-10 — Rights-Safe Semantic Presentation & Accessibility Projection

Absorbs historical GPR-10 and GPR-11. Bind authorized semantic actor/world/object/UI/effect/audio roles to runtime presentation, with rights/use validation before production selection/export. Implement camera/HUD/menu/dialogue/reticle, semantic cue, accessibility and device projections without making presentation authoritative mechanics truth.

### GPR-12 — Multiplayer, Replay, Persistence, Recovery & Version Continuity

Absorbs historical GPR-12 and GPR-13. Implement player/controller-slot authority, synchronization gates, deterministic replay/Event traces where declared, versioned snapshots, restore/migration, reconnect, unsupported-version/corruption behavior and recovery boundaries. Owner-domain idempotency/version rules remain authoritative for owner mutations.

### GPR-16 — Full Conformance, Golden Cross-System Runtime Proof & Downstream Handoff

Absorbs historical GPR-15 and GPR-16. Run the full 168-pattern/85-operation/672-variant conformance/regression battery plus the original-content cross-system golden proof. GPR does not close until both conformance and downstream handoff are verified.

## Seven delivery modes

Every reusable pattern declares which of these it supports:

1. direct play;
2. cozy/low-pressure play;
3. GM-led play;
4. world-map/TTRPG bridge;
5. embedded minigame;
6. user-authored reusable loop mini;
7. Multiversal roster injection.

Mode support may change governed timer/aggression/resource/retry/hint/control/presentation policies. It cannot fork owner-domain mechanics truth.

## Replay/persistence/multiplayer boundary

GPR-12 records gameplay-instance continuity, including runtime version, pattern/configuration version, owner-reference versions when semantically necessary, command stream, seed/randomness contract where applicable, ordered Events/outcomes and snapshot/migration metadata.

A deterministic replay must reproduce governed semantic state/Event outcomes from the same declared inputs and versions. Rendering frames need not be bit-identical unless a separate engine contract promises that. Network arrival order cannot silently become gameplay authority.

## Rights, visibility and privacy

Visibility/permission filtering occurs before participant/target lists, counts, route choices, diagnostics, replay/export, optional-AI context and presentation-role binding are constructed for an audience.

Reference ROMs, screenshots, maps, sprites, music, distinctive source layouts/text and other protected benchmark expression remain evidence only. Production bindings must be original, user-created or otherwise rights-cleared under ARI/PCA authority.

## Accessibility/provider independence

Semantic alternatives exist for blocking drag/twitch/visual-only operations where the governing pattern supports equivalent interaction. Camera/UI/audio/haptic presentation may vary without changing mechanics truth. GPR cannot require a paid/cloud provider or 3D renderer for blocking execution, authoring, replay, recovery or proof.

Optional AI is visibility-safe advisory only. It cannot grant permission, mutate owner state, canonize definitions or declare a conformance/golden proof passed.

## Golden proof

GPR-16 must prove at minimum:

- original/right-cleared traversal/action, puzzle, sports/skill, tactical/strategy, Vehicle, social/investigation and stealth loops;
- direct and cozy execution of the same semantic pattern without rules fork;
- governed GM-led and World/TTRPG success/partial/failure outcomes;
- an embedded Adventure/session minigame;
- a user-authored loop mini;
- Character roster injection without identity/ownership replacement;
- stable World/Map binding;
- rights-safe presentation binding and explicit rejection of reference-only/commercial content;
- multiplayer/co-op authority where the proof pattern supports it;
- deterministic replay where declared, snapshot/restore, migration and unsupported-version failure;
- explainable Event/outcome traces;
- the complete 168-pattern/85-operation/672-variant conformance battery;
- provider-off local operation and an equivalent nonvisual flow;
- successful reusable handoff to MERA, MBES, MSLR, MSWI and SMB without ownership bleed.

The detailed 48-vector acceptance set is governed by `PDCP_GPR_FAMILY_DESIGN_CLOSURE.md`.

## Family execution rule

Each surviving tranche targets no more than 24 active minutes and reserves at least eight minutes for closeout. Preload only the selected tranche and dependency closure. Split before governed start if that bound is not credible. A single owner `Continue` carries a governed-started tranche through implementation, required validation, verified closeout and successor marking unless an OPS3 owner-only boundary or genuine external blocker is reached.

No GPR runtime branch or implementation authority exists until a future OPS3 governed start selects a specific surviving work item.

## Completion standard

GPR completes only when the ten surviving tranches are `completed_verified`, `GPR-16` contains the full conformance and golden evidence, the seven delivery modes use one state/Event/outcome model, production presentation remains rights-safe/swappable, and downstream families can consume the runtime without creating parallel gameplay engines.


## GPR-01 completed runtime-registry result

GPR-01 completed_verified on 2026-09-20. The published application contract `GPR-01.1` establishes GPR as the executable registry/projection authority over accepted MRCS definitions and frozen MAL-01..10 primitives without creating another definition ledger or canonical owner runtime.

The registry covers semantic pattern, primitive, operation and asset-role references; validates explicit namespaces, semantic IDs/versions, source authority and foundation evidence; produces deterministic sorted runtime IDs/receipts; and preserves explicit `supported`, `unsupported` and `unknown` states. Binding resolution fails closed on missing, mismatched, unsupported or unknown references and never treats registry presence as proof of owner mutation or gameplay occurrence.

Causal RED: run `35529417335` at `e127881c5c8ac562f225e3615356b45e83d13ec0`. Exact-head cross-platform GREEN: run `35529549717` at `a91f50f515cdd3e397dd6ee566adcff397a1d7a3`. Published application: PR #649 through READY candidate `GPR-01-app-001` as `6fc0030d952355eecea63928fcbc4736feb110f3`.

The fresh roadmap DAG supplies no interstitial successor override, so GPR-03 is selected_not_started. Later MRCS domains remain late-bind dependencies and GPR-16 remains gated on MRCS-21 plus relevant specialist golden proofs.


## GPR-03 completed deterministic-kernel result

GPR-03 completed_verified on 2026-09-20. The published application contract `GPR-03.1` establishes the bounded gameplay-instance entity/input/collision/state kernel over the GPR-01 executable registry seam.

GameplayInstance identity remains distinct from reusable pattern/configuration identity. Raw device controls normalize to semantic commands before transitions; presentation-frame sequence is explicitly non-authoritative. Deterministic ordering is based on governed semantic command/collision identities, with explicit deterministic seed and configuration/version binding. Entity, spawn and transition caps fail closed.

Collision/trigger processing emits GPR-local outcomes only. Unsupported or unknown GPR-01 bindings remain blocked/unresolved with no generic fallback. The kernel cannot perform or prove canonical World, Combat, Action/Event or other owner-domain mutation.

Causal RED: run `35530223806` at `88dc7ccf4d1209b8697f18242a33537bfcc9dbf9`. Exact-head cross-platform GREEN: run `35530339162` at `ef5d69a5e38cf24d05f6517d67ccab58cf3ddab4`. Published application: PR #651 through READY candidate `GPR-03-app-001` as `b82eb6532d9d1b0815836a9ae3e852ac8fff2839`.

The fresh roadmap DAG supplies no interstitial successor override, so GPR-05 is selected_not_started. Later MRCS domains remain late-bind dependencies and GPR-16 remains gated on MRCS-21 plus relevant specialist golden proofs.


## GPR-05 completed owner-operation/objective/route runtime result

GPR-05 completed_verified on 2026-09-20. Published application contract `GPR-05.1` provides one common pattern-level adapter surface for traversal, combat/projectiles, ability/resource, interaction, Inventory/equipment, Economy/reward, Progression/unlock, objective/mission and World/Scene route requests over GPR-01 registry bindings and GPR-03 GameplayInstance state.

Requests bind stable operation runtime IDs, GameplayInstance identity and explicit canonical owner domains. Deterministic ordering uses governed order keys/request IDs; presentation order and network-arrival order are explicitly non-authoritative. Unsupported, unknown and owner-mismatched bindings fail closed.

GPR-local planning cannot prove owner mutation. A canonical owner mutation is considered committed only after an explicit matching owner receipt with owner evidence is returned. Objective and route composition remain sorted GPR-local orchestration projections and do not create canonical World/Scene/Quest truth.

Causal RED: run `35531204847` at `287753ecc78b2290c1919621347a504866a7e43e`. A test-helper-only TypeScript annotation defect was diagnosed after run `35531314861` without changing production behavior or assertions. Exact-head cross-platform GREEN: run `35531488677` at `ac379018668f0e85929320717d72063a14578105`. Published application: PR #654 through READY candidate `GPR-05-app-001` as `a22391fdb136354c5eef93b9dbfc85de4deec35b`.

The fresh roadmap DAG supplies no interstitial successor override, so GPR-06 is selected_not_started.


## GPR-06 completed specialist-module result

GPR-06 completed_verified on 2026-09-20. The published application contract `GPR-06.1` establishes one shared specialist-module interface for puzzle, sports, Vehicle/Mount, party/companion, tactical/strategy, social/investigation and stealth/detection play over the GPR-05 owner-operation runtime.

Each specialist family retains explicit semantic profiles and required owner capabilities rather than using a generic fallback guess. Unsupported or unresolved specialist bindings, missing owner capabilities and rejected shared GPR-05 operations fail closed. Specialist outcomes remain GPR-local until matching canonical owner receipts are supplied, and no bespoke specialist runtime fork or canonical owner mutation is created by GPR.

Causal RED: run `35532367213` at `09280a7e47e904b9f33e37cabd0c54de0b5528b6`. Exact-head cross-platform GREEN: run `35532445182` at `0c2de1f7cf1c9bc41b45da69e6e57b2c68f96486`. Published application: PR #655 through READY candidate `GPR-06-app-001` as `faf9d34c091ce096d910b10b61063ffd7a025ea9`.

The fresh roadmap DAG supplies no interstitial successor override, so GPR-07 is selected_not_started. GPR-07 remains bounded to encounter/autonomous selection, score/timing/rhythm resolution, loadout/build execution and skill-resolution adapters; NPC psychology, AI authority, Character build truth, skill definitions and authored audio remain external owner concerns.


## GPR-07 completed bounded-resolution result

GPR-07 completed_verified on 2026-09-20. The published application contract `GPR-07.1` establishes bounded encounter/autonomous selection, semantic score/timing/rhythm resolution, loadout/build projection and skill-resolution adapters over the existing GPR runtime.

Encounter/autonomous selection uses explicit bounded candidates and external owner references; GPR does not own NPC psychology or AI authority. Score/timing mechanics use declared semantic clocks and deterministic event ordering; authored audio and presentation frames remain non-authoritative projections. Loadout/build execution requires explicit Character, Inventory/Asset and Progression owner capabilities and cannot replace Character build truth. Skill resolution consumes accepted skill definitions plus GPR-05 owner operations; GPR does not author or canonize skills.

Causal RED: run `35535649049` at `0091a243b3da84a05d9eac00acfeb42e37ee1318`. Exact-head cross-platform GREEN: run `35535747817` at `2024f9f1bfcb5aa3c5f8f8512b9bde37ca91f0da`. Published application: PR #658 through READY candidate `GPR-07-app-001` as `c45873b7d73c0423c4ef3280cbf5b341536e425b`.

MRCS-21 is terminal completed_verified and the fresh roadmap DAG supplies no interstitial successor override, so GPR-08 is selected_not_started.


## GPR-08 completed loop-mini contract/composer result

GPR-08 completed_verified on 2026-09-20. The published application contract `GPR-08.1` provides one versioned, data-driven loop-mini configuration schema and deterministic bounded composer for objectives, map/world references, participants/roles, operations, Resources, rules, rewards, limits, difficulty/configuration and declared delivery support.

Stable GPR runtime bindings are validated through the existing registry. Unsupported or unresolved bindings and unsupported delivery declarations fail closed. Explicit authoring caps bound participants, objectives, operations, Resources, rules, rewards and map references. Semantically equivalent input ordering normalizes to the same configuration receipt.

Draft and preview outputs remain noncanonical configuration: they do not establish execution, owner commit or canonical owner mutation. Generic creator/debug studio authority remains external.

Causal RED: run `35536420697` at `1f52059c82f34445b8af10de000f2ba27388947c`. Exact-head cross-platform GREEN: run `35536509276` at `46b02fb679cff886c4750478fb54bd6efd3221b8`. Published application: PR #660 through READY candidate `GPR-08-app-001` as `1fac56244a41cd58e6cd70751d85b7d1c52c327b`.

The fresh roadmap DAG supplies no interstitial successor override, so GPR-09 is selected_not_started. GPR-09 absorbs historical GPR-09/GPR-14 and implements the seven delivery adapters plus GPR-specific Creator/GM controls, World/Map/Adventure binding and roster injection using Packet-07 shared execution-inspection semantics rather than a new generic studio framework.
