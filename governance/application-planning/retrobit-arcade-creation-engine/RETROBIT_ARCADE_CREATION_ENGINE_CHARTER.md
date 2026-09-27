# Retrobit Arcade & Creation Engine — Durable Project Charter

**Program working ID:** RBCE  
**Program name:** Retrobit Arcade & Creation Engine  
**Status:** OWNER-APPROVED PLANNING BASELINE  
**Owner and final authority:** John Brandon Turner  
**Durability purpose:** preserve the approved Retrobit product intent independently of chat history  
**Operational authority:** none; this document does not select current work and cannot override `operations/CURRENT.json` or `operations/BOOTSTRAP.md`

## 1. Owner decision preserved by this charter

Retrobit is approved as a Multiversal product layer that turns the existing gameplay, content, map/asset, scene and presentation systems into a coherent 2D arcade/game-creation experience.

Retrobit is **not** a new parallel rules engine. It is the product and composition layer that exposes existing Multiversal capabilities as a usable game creator and arcade runtime.

The approved architecture is:

`Retrobit Arcade Studio`
→ uses **MRCS** for governed reusable definitions
→ uses **MAI** for sprites, tiles, maps, atlases and visual provenance
→ authors a versioned **Retrobit Game Project** built around **GPR Loop Mini** configuration
→ executes semantic gameplay through **GPR**
→ uses a dedicated **Retrobit 2D projection/runtime layer** for pixel/tile/sprite rendering and platform/top-down presentation behavior
→ reuses **ISE** scene, trigger, spatial, permission and preparation infrastructure where appropriate
→ reuses existing audio, provenance, rights, persistence, replay, multiplayer and accessibility systems
→ presents through the existing **Retrobit Classic Arcade** UI identity.

The long-term user-facing goal is a creator who can open Retrobit Arcade, choose or compose a game style, build rooms/levels with legitimate assets, assign reusable behaviors, playtest immediately, save/publish safely, and either play the result directly or embed it in a Multiversal campaign.

## 2. Provenance from the NES/SNES studies

The earlier NES/SNES studies are retained as design/research provenance for identifying reusable gameplay structures. They are not production dependencies and do not authorize copying protected game expression, ROM assets, maps, dialogue, audiovisual material or proprietary implementation.

The useful architectural conclusions from those studies survived into later Multiversal systems:

- device-independent movement and action intents;
- deterministic state transitions;
- collision and trigger semantics;
- reusable traversal/action patterns;
- connected-room and gated-exploration structures;
- platform/hazard/dependency behavior;
- dialogue and persistent event state;
- objectives, scoring, rewards and failure/partial variants;
- presentation separated from semantic mechanics.

Current GPR rights-safe rules remain controlling: production Retrobit content must be original, licensed, user-owned, public-domain or otherwise explicitly permitted.

## 3. Existing foundation that Retrobit must reuse

### 3.1 Gameplay Pattern Runtime (GPR)

GPR is the semantic gameplay backbone. It already provides deterministic gameplay-instance state, semantic input normalization, collision/trigger evaluation, owner-operation routing, specialist gameplay modules, encounter/score/timing behavior, loop-mini composition, delivery modes, rights-safe presentation binding, persistence/replay/continuity and terminal conformance proof.

Retrobit must consume GPR rather than fork it.

### 3.2 Multiversal Rules & Content Studio (MRCS)

MRCS is the governed reusable-definition authoring system for Actions, Effects, Conditions, Resources, abilities, items, creatures, environments, encounters, rewards, house rules and related content families.

Retrobit may provide simplified arcade-facing editors over accepted MRCS definitions, but it must not create a second definition authority.

### 3.3 Map Asset Interoperability (MAI)

MAI provides vendor-neutral asset/provenance handling for sprite sheets/atlases, tilesets, structured tilemaps, modular room assets, animation-capable sources and Tiled/LDtk-class structured imports.

Retrobit must preserve source/license/provenance metadata and must not silently flatten structured source semantics when supported metadata exists.

### 3.4 Interactive Scene Experience (ISE)

ISE provides native canvas, camera, placements, movement proposals, collision, regions, walls/doors, interactables, governed triggers, levels/elevation, environmental presentation, instant preparation and multiplayer/accessibility semantics.

Retrobit may reuse those contracts and components where they fit, but its dedicated 2D projection layer may optimize differently for tile/sprite games.

### 3.5 Retrobit Classic Arcade UI skin

The existing `retrobit-classic-arcade` skin supplies the presentation identity for the creator and arcade shell: stepped block geometry, CRT/cabinet framing, score-like numerals and the approved blue/red/yellow arcade relationship.

The skin is presentation only. It cannot define or alter gameplay mechanics.

## 4. Product scope

Retrobit should ultimately support at least:

- top-down exploration/action;
- connected-room adventure structures;
- side-scrolling/platform traversal;
- puzzle and hazard challenges;
- sports/skill and timing games;
- tactical/strategy play;
- vehicle/racing play;
- stealth/detection play;
- social/investigation/dialogue play;
- cozy/low-pressure loops;
- standalone arcade games;
- campaign-embedded minigames;
- GM-led variants;
- world-map/TTRPG bridges;
- existing-character/roster injection;
- user-authored loop minis.

These are delivery/composition profiles over shared GPR semantics, not isolated game engines.

## 5. Product principles

1. **Build games, not configuration puzzles.** The normal creator path must be visual, inspectable and fast.
2. **One semantic truth.** Retrobit presentation cannot create a competing rules/state ledger.
3. **Data-driven composition.** Games are versioned projects assembled from explicit scenes, assets, roles, patterns, operations and rules.
4. **Original/right-cleared by construction.** Research references never become production assets automatically.
5. **Playable without AI.** AI may assist creation, but deterministic authoring/play must work with AI disabled.
6. **Local-first where existing Multiversal contracts permit it.** A paid/cloud provider must not be mandatory for basic creation or play.
7. **Accessible consequential actions.** Visual arcade presentation cannot be the only way to understand or perform required game actions.
8. **Fast preview loop.** Edit → validate → playtest → inspect should be a first-class workflow.
9. **Campaign integration without ownership bleed.** Embedded games return typed, controlled outcomes to canonical owners.
10. **Presentation is replaceable.** Retrobit is the default arcade presentation, but semantic project content must not be inseparable from a particular visual skin.

## 6. Approved first productization sequence

### RBCE-01 — Retrobit Game Project Format
Define the durable, versioned project object tying together GPR configuration, scenes/levels, MAI assets, sprite roles, input mappings, variables/save state, audio references, rights/provenance, tests and publishing metadata.

### RBCE-02 — Retrobit 2D Projection Runtime
Add the dedicated pixel/tile/sprite projection layer: tile rendering, sprite batching, animation state, top-down/side-scroll cameras, parallax, hitboxes/hurtboxes, platform collision helpers, gravity/jump/ladder/slope/checkpoint/spawn presentation support and pixel-perfect scaling. This layer consumes GPR semantics and may not own canonical game truth.

### RBCE-03 — Retrobit Arcade Studio
Create the user-facing project/template picker, level/room editor, actor palette, property/behavior inspector, variable/event tools, objectives/rewards setup, preview/playtest, diagnostics and save/publish workflow.

### RBCE-04 — Retro Asset Workbench
Provide sprite-sheet slicing, animation naming, anchors, hitboxes, palette handling, tileset/autotile/metatile helpers, semantic asset-role assignment and reusable visual presets over MAI.

### RBCE-05 — Human-Readable Gameplay Parts Library
Project the GPR pattern/operation corpus into creator-facing names, categories, examples, parameters and compatibility guidance such as Top-Down Movement, Locked Door, Collect Key, Moving Platform, Checkpoint, Dialogue Choice and Timed Escape.

### RBCE-06 — Four-Engine Test Chamber Golden Game
Recreate the original architecture proof as fully original/right-cleared Multiversal content. One small editable game must prove:

1. top-down exploration and scene transitions;
2. connected rooms, collision and ability/item-gated traversal;
3. side/platform traversal with hazards and dependencies;
4. NPC branching dialogue and persistent event state.

The proof is successful only when the game can be created/edited in Retrobit Studio, validated, played, saved, reloaded and replayed without hand-coded game-specific mechanics.

### RBCE-07 — Product Entry Points & Packaging
Expose Create Retrobit Game, Play Arcade, Add as Campaign Minigame, Attach to Scene/Object, Use Existing Character/Roster, standalone roster flow and governed `.pack` export/share behavior.

## 7. Non-goals and stop lines

Retrobit does not:

- emulate NES/SNES hardware or run commercial ROMs as a product requirement;
- redistribute protected game assets;
- create a second Multiversal Character, Combat, World, Inventory, Action/Event or persistence authority;
- replace MRCS definition governance;
- replace MAI rights/provenance handling;
- make ISE obsolete;
- make a specific third-party editor or renderer canonical;
- require AI, paid cloud or a mandatory 3D engine for basic operation;
- silently invent missing semantic definitions or missing rights.

## 8. Durable recovery statement

A future conversation recovering this project should begin from this charter plus the active RBCE specification(s), then enter through OPS3 before any implementation. The intended next step after this charter is **RBCE-01 — Retrobit Game Project Format**.

This document preserves product intent only. `operations/CURRENT.json` remains the sole live work selector.
