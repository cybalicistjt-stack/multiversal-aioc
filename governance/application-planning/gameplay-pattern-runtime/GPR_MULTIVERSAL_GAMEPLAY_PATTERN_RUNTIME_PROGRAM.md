# GPR — Gameplay Pattern Runtime & Loop Minis

**Program ID:** GPR  
**Program name:** Gameplay Pattern Runtime & Loop Minis  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED FUTURE INTERSTITIAL; NOT STARTED  
**Activation:** after MRCS-21  
**Successor:** MERA-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-11  
**Implementation authority:** none

## Purpose

GPR turns the completed MAL microgame foundation plus the later 175-game clean-room gameplay study into one reusable Multiversal gameplay-pattern runtime. It is the layer that lets accepted rules, characters, maps, assets, encounters and campaign state become playable loops without creating one bespoke engine per minigame, game genre or feature family.

The governing flow is:

`accepted owner-domain state + MRCS definitions + semantic pattern contract + rights-cleared presentation bindings → deterministic gameplay instance → typed events/outcome → owner-domain handoff`

GPR is not a replacement for Character, World, Scene, Combat, Inventory, Economy, Project, Action/Event, map, audio, adventure or content-definition owners.

## Why this is separate from MAL

MAL-01..10 are already `completed_verified` and remain frozen. MAL established original microgame primitives, small state machines, GM composition recipes, owner handoffs, accessibility/performance behavior and a starter/golden microgame library.

The later research baseline is materially broader: 175 mined games, 168 reusable gameplay patterns, 461 primitives, 29 normalized mechanics modules, 169 catalog operations, 85 primitive-bound operations exercised in conformance, 129 presentation roles, seven delivery modes, versioned replay/snapshot behavior and 672 adaptation cases.

GPR therefore **extends the product capability without reopening MAL**. MAL remains the small-loop substrate and prior proof. GPR productizes broad reusable gameplay execution and authoring.

## Roadmap placement

Owner-approved placement:

`… → MSAS-01..21 → MRCS-01..21 → GPR-01..16 → MERA-01..24 → MBES-01..24 → SMB-08 …`

This is the best dependency point because:

- MRCS must exist first so reusable Actions, Effects, Conditions, Resources, Abilities, items, creatures, vehicles, environments, encounters and scoped rules can be authored through governed definitions.
- MCS/MCCS/MNCS/MAS/MSAS are already upstream, so maps, appearance/actors, NPC/creature continuity, adventure structure and audio can bind into loops through their owners.
- MERA and MBES come afterward so engineering, construction and settlement gameplay can consume the shared gameplay runtime rather than creating their own parallel execution engines.
- SMB-08/09 then produce first-party content and campaign material on top of one proven gameplay substrate.

This insertion changes no current execution authority. ARI-16 remains the live selected work item until canonical execution advances normally.

## Research baseline

Planning provenance is frozen in `GPR_RESEARCH_BASELINE_v3.6.json`.

Key verified reference results:

- 175 / 175 games gameplay-mined;
- 168 reusable gameplay patterns;
- 461 gameplay primitives;
- 29 mechanics API modules;
- 169 registered mechanics operations, with 85 primitive-bound operations exercised by canonical patterns;
- 129 semantic gameplay asset roles across 9 original Multiversal asset families;
- 168 / 168 success-path pattern conformance;
- 672 / 672 failure/partial/cozy/GM adaptation cases;
- deterministic replay and snapshot round-trip evidence;
- snapshot migration 1.0 → 1.1;
- zero generic-fallback hits in the primitive-bound operation set;
- seven delivery modes proven on the reference vertical slices.

The reference package identity is preserved by SHA-256 in the baseline manifest. The package is research/conformance provenance, not automatically a shipping artifact.

## Core doctrines

1. **Composition instead of game forks.** A playable loop is data/configuration over reusable operations, state, events and semantic presentation roles.
2. **Owner-domain truth remains external.** Gameplay consumes governed projections and returns typed outcomes; it does not create parallel identity or canonical ledgers.
3. **MAL remains frozen.** GPR consumes completed MAL contracts but does not rewrite its completion evidence or originality boundary.
4. **Definition is not execution.** MRCS-authored content becomes playable only when a GPR instance binds accepted definitions and owner-domain state.
5. **Reference is not production content.** ROM-derived and third-party commercial expression stays reference/evidence only.
6. **Semantic assets are swappable.** Mechanics bind roles/states/anchors rather than filenames or one skin.
7. **Direct/cozy/GM/TTRPG share one model.** Adaptation is governed configuration and outcome policy, not separate engines.
8. **Replay and persistence are versioned.** Deterministic modules must reproduce state/event results from the same command stream and seed.
9. **Multiplayer authority is explicit.** Shared/co-op state declares ownership/authority and synchronization gates.
10. **User-authored loops are bounded.** Authoring validates safe caps for actors, projectiles, timers, recursion/procedural spawn and persistent objects.

## Seven delivery modes

Every reusable gameplay pattern must be able to declare support for:

1. direct play;
2. cozy/low-pressure play;
3. GM-led play;
4. world-map / TTRPG bridge;
5. embedded minigame inside a session/adventure;
6. user-authored reusable loop mini;
7. Multiversal roster injection.

A pattern may expose different parameters in each mode, but mode support must not create a second mechanics truth.

## Sixteen bounded tranches

### GPR-01 — Gameplay Runtime Authority, Research Baseline & MAL/MRCS Convergence

Register the authority map, v3.6 research baseline, MAL/MRCS relationship, clean-room boundary, semantic namespaces and completion evidence required before application implementation begins.

### GPR-02 — Semantic Gameplay Registry, Pattern/Primitive Contract Import & Namespace Lint

Import the normalized module/operation/primitive/pattern/asset-role contracts into governed application schemas with stable IDs, namespace validation and explicit unsupported states.

### GPR-03 — Entity, Input, Physics, Collision & Deterministic State Kernel

Implement the deterministic entity/state kernel, semantic input abstraction, collision/trigger model, fixed-step state transition rules and safe authoring caps.

### GPR-04 — Movement, Combat, Projectile, Ability, Resource & Interaction Core

Implement broad action execution for traversal, combat, projectiles, abilities, resources, pickups/interactions and the common state transitions used across the corpus.

### GPR-05 — Inventory, Economy, Progression, Objective & World-Route Runtime

Implement inventory/equipment interaction, economy/rewards, progression/unlocks, objectives/missions and room/zone/world routing over owner-domain contracts.

### GPR-06 — Puzzle, Sports, Vehicle, Party, Strategy, Social & Stealth Specialist Modules

Implement specialist reusable modules for puzzles, sports possession/match rules, vehicles/mounts, parties/companions, tactical/strategy state, social/investigation and stealth/detection.

### GPR-07 — AI/Encounter, Score/Timing, Loadout & Skill-Resolution Runtime

Implement AI/encounter pacing, score/timing/rhythm resolution and loadout/build configuration with deterministic bounded behavior and inspectable events.

### GPR-08 — Loop-Mini Contract, Pattern Composer & Data-Driven Authoring Schema

Productize the loop-mini schema and pattern composer so authors select objectives, maps, actors/roles, operations, resources, rules, rewards, limits and difficulty parameters without writing bespoke runtime code.

### GPR-09 — Seven Delivery Modes: Direct, Cozy, GM, World/TTRPG, Embedded, User Mini & Roster Injection

Implement the seven delivery adapters while preserving one state/outcome model: direct, cozy, GM-led, world/TTRPG, embedded, user-authored and roster-injected.

### GPR-10 — Original Asset-Role Binding, Rights Filtering & Presentation Contract

Bind mechanics to original/rights-cleared semantic asset roles, enforce rights/use capability before selection/export and preserve presentation-state/accessibility contracts without source-game dependencies.

### GPR-11 — Camera, UI, Audio, Feedback, Accessibility & Device Projection

Implement camera, HUD/menu/map/dialogue/reticle projections, semantic sound/music cues, accessibility alternatives and supported input/device presentation over authoritative gameplay state.

### GPR-12 — Multiplayer/Co-op Authority, Replay, Determinism & Event Trace

Implement multiplayer/co-op player-slot authority, synchronization gates, shared/competitive state, deterministic replay/trace receipts and explainable event logs.

### GPR-13 — Persistence, Snapshot Migration, Recovery & Version Compatibility

Implement versioned snapshots, restore, migration, replay compatibility, corruption/unsupported-version failure behavior and recovery boundaries.

### GPR-14 — Creator/GM Loop Studio UX, World Binding & Character/Roster Injection

Deliver creator/GM-facing loop authoring and test surfaces, character/roster injection, world/map/adventure binding, presets and governed GM override workflows.

### GPR-15 — Full 168-Pattern / 85-Operation / 672-Variant Conformance & Regression Gate

Run the full corpus-derived conformance gate: all 168 canonical patterns, all 85 primitive-bound operations, success paths, failure/partial/cozy/GM variants, replay/snapshot checks, rights checks and regression preservation.

### GPR-16 — Golden Cross-System Gameplay Runtime Proof & MERA/MBES/SMB Handoff

Run the golden cross-system application proof with original Multiversal content and hand the completed gameplay runtime to MERA, MBES, SMB-08/09 and later product UX/content families without ownership bleed.

## Golden proof

GPR-16 must demonstrate, using original or otherwise rights-cleared Multiversal content:

- at least one traversal/action loop, puzzle loop, sports/skill loop, tactical/strategy loop, vehicle loop, social/investigation loop and stealth loop;
- the same semantic pattern executed in direct and cozy modes without a rules fork;
- one GM-led resolution and one world/TTRPG bridge resolution with typed success/partial/failure consequences;
- an embedded minigame inside an Adventure/session context;
- a user-authored loop mini created through the governed authoring surface;
- roster injection of an existing Multiversal Character without replacing Character identity or canonical equipment/ability ownership;
- map/world binding through stable references;
- original actor/world/object/UI/effect/audio bindings with reference-only/commercial asset rejection;
- multiplayer/co-op authority and synchronization behavior where the selected proof pattern supports it;
- snapshot/restore, deterministic replay, version migration and unsupported-version failure;
- explainable event/outcome traces suitable for GM tools, support and later product diagnostics;
- full 168-pattern / 85-operation / 672-variant conformance evidence;
- successful operation with paid/cloud providers disabled.

## Rights and clean-room boundary

The 175-game research corpus is capability evidence. GPR may preserve factual mechanical observations, normalized semantic taxonomies, test vectors and provenance records, but must not ship or depend on protected source-game art, music, maps, screenshots, sprite sheets, level layouts, distinctive authored text or proprietary code.

Production presentation comes from original Multiversal assets, user-created/right-cleared assets, or other materials with appropriate rights. Rights/use capability is checked at binding/export boundaries rather than assumed from technical readability.

## Family execution rule

Each GPR tranche targets **24 active minutes or less under a healthy governed environment**, preserving normal closeout reserve. Oversized work is split before governed start. No GPR runtime preflight, branch or implementation authority exists now.

## Completion standard

GPR completes only when all 16 tranches are `completed_verified`, the application runtime has no game-specific core fork requirement for the 168 canonical patterns, the seven delivery modes are productized through one state/event/outcome model, production assets remain rights-safe and swappable, and the golden proof hands a reusable gameplay substrate to MERA/MBES and first-party content production.
