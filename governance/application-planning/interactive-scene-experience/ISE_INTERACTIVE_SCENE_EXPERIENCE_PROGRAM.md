# ISE — Interactive Scene Experience

**Program ID:** ISE  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL  
**Activation:** after AAI-10  
**Successor:** WCI-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-23

## Purpose

ISE turns Multiversal's existing governed Scene semantics plus completed MAI visual interoperability and AAI audio interoperability into the native, polished tabletop experience. The target is Foundry-level spatial capability with substantially lower preparation friction: users should be able to import or assemble legitimate map/audio assets, make them playable quickly, and interact with them through Multiversal's actual Character, Creature, Item, Encounter, Hazard, Vehicle, World/Reality, Action/Event and permission authorities rather than through a parallel VTT rules ledger.

ISE consumes the existing A5 Scene foundation, including versioned map references, square-grid calibration, cell/cell-area/named-zone/gridless semantic locations, dungeon primitives and Campaign-local placements. It expands the interaction/presentation layer; it does not replace Scene, World, Combat, Character, Item/Asset, permission, MAI or AAI ownership.

## Experience goals

- **Make Playable, not configure forever.** A normal map image should move through automatic grid/geometry assistance with fast manual correction; a structured import such as UVTT should reuse supported grid/wall/door/light metadata instead of requiring retracing.
- **Semantic map, not picture board.** Rooms, cells, regions, doors, hazards, encounters, objectives, items, portals and other placements remain meaningful governed objects.
- **Assets remain replaceable.** Map/audio intent is separate from the selected provider asset so legitimate user-owned or provider-controlled assets can be substituted without rebuilding the encounter.
- **Tactical when useful, cinematic when not.** Roleplay/theater-of-the-mind and mapless Scenes remain first-class; the native canvas appears when it adds value rather than becoming mandatory chrome.
- **GM power without scripting as the default.** Common triggers/interactions are authored as governed semantic operations. Macros/plugins may exist later, but a pressure plate, door, portal, hazard or audio transition should not require the GM to write code.
- **Player-safe by construction.** Hidden layers, placements, notes, unrevealed regions, sensor information and audio cue metadata remain permission-filtered before projection.

## Tranches

1. **ISE-01 — Native Canvas, Camera, Registration & Interaction Surface**  
   Deliver the accelerated native Scene canvas with mouse/touch/pen pan and zoom, fit/focus/bookmarks, selection, drag/drop, keyboard-accessible equivalents, undo/redo and GM/player view modes. Extend image registration beyond basic cell-size/origin calibration with rotation and bounded affine/perspective correction where needed, plus assisted grid detection and manual control points. Camera state remains presentation-only and cannot redefine canonical Scene meaning.

2. **ISE-02 — Tokens, Measurement, Tactical Movement & Area Templates**  
   Project Character, Creature/NPC and Vehicle references as governed tokens with footprints, selection/control ownership, drag/click movement proposals, ruler/path previews, snapping/free movement, facing/elevation where a profile requires it, mounts/attachments and touch-friendly controls. Add circles, cones, lines, walls, bursts, spheres and irregular area templates that preview governed targets/effects without bypassing Action/Event or movement authority.

3. **ISE-03 — Fog, Vision, Sensors, Walls, Doors & Exploration Memory**  
   Implement static and dynamic fog, individual/shared explored-area memory, walls/windows/doors, collision, light/vision boundaries and explicit GM reveal controls. Generalize perception beyond ordinary sight through profile-driven sensor channels such as authored thermal, radar/lidar, sonar, supernatural/spirit or other setting-local senses without inventing universal sensor rules.

4. **ISE-04 — Semantic Regions, Interactables & Governed Triggers**  
   Make cells, cell areas, rooms, named zones and gridless regions first-class interaction surfaces. Bind entry/exit/presence/interact/state-change triggers to existing Encounter, Hazard, Item, Objective, Door, Transition, Portal and other owner-domain operations. A map object may project a real governed object but never becomes a duplicate ownership ledger.

5. **ISE-05 — Levels, Elevation, Reality Layers & Map-State Families**  
   Support floors, roofs, vertical transitions, elevation-aware presentation and linked multi-level spaces. Add state-family registration for aligned map variants such as day/night, intact/ruined, dry/flooded, dormant/active or weather variants so semantic geometry/placements can persist across art changes. Add governed Reality/Timeline/Plane/phase overlays where MIB-11/MSS owners permit them, allowing spatially aligned but perceptually/state-distinct layers without silently merging realities.

6. **ISE-06 — Environment, Effects, Scene State & Audiovisual Orchestration**  
   Compose MAI layers and AAI cues with authored Scene/World/Event/Combat/Weather/Travel/Vehicle/Magic state: weather, smoke/fire/water or other supported visual effects, transitions, map-state changes, region-aware audio intent and optional scene-event cues. Audio/visual state supports Manual, Suggest and authorized Automatic modes; GM override, silence and no-effects operation remain first-class.

7. **ISE-07 — GM Cockpit, Instant Prep, Scene Recipes & Preview-as-Player**  
   Provide the low-friction preparation experience: drag/drop or import → recognize → calibrate/confirm → Make Playable. Include smart geometry/room suggestions, encounter/item/hazard/objective placement, palette/search, player-view preview, Scene Audio Deck, prepared cue buttons, intensity/mood controls and entitlement-aware provider resolution. Define shareable **Scene Recipes** that contain semantic preparation, mappings, provider references and fallback intent without redistributing third-party commercial media.

8. **ISE-08 — Multiplayer, Accessibility, Performance & Golden Native-Tabletop Proof**  
   Prove remote token/Scene synchronization, reconnect/rejoin, stale/conflict handling, GM adjudication, hidden information, mobile/tablet operation, keyboard/nonvisual equivalents, large maps, animated assets, audio-disabled operation and deterministic authoritative results. Golden proof covers asset import through prepared Scene, live encounter, interactive object/region, audiovisual transition and post-Scene state while preserving all owning-domain boundaries.

## Planned interoperability posture

- MAI owns map/tileset/image/geometry import, semantic asset resolution and provider/source provenance.
- AAI owns local/provider audio, capability negotiation, playback, semantic audio intent and entitlement/license constraints.
- ISE consumes MAI + AAI to create the native playable Scene experience.
- VTI later projects the same governed Scene/MAI/AAI state into external VTTs where their APIs and licenses permit it; external VTTs do not replace ISE or Multiversal rules authority.
- Structured imports should consume supported metadata rather than flattening everything to pixels. Unsupported metadata remains explicit.
- Commercial third-party assets are referenced/controlled under legitimate entitlement and license; ISE/Scene Recipes must not become a redistribution path.

## Invariants

- Existing Scene, World/Reality, Action/Event, Combat, Character, Creature, Item/Asset, Vehicle and permission authorities remain canonical.
- Pixel coordinates, token images, visual effects and audio never become canonical game truth by themselves.
- View/camera state is distinct from map registration/calibration and semantic location.
- Hidden/GM-only state is filtered before rendering, search, counts, automation, diagnostics, export or AI context.
- Automated Scene triggers cannot bypass owner-domain validation, consent, permissions, GM adjudication or expected-version/idempotency rules.
- Missing visual/audio assets never block play; placeholders, substitutions, silence and theater-of-the-mind remain legitimate states.
- Generated geometry/classification is assistance until confirmed where certainty is insufficient.
- Accessibility equivalents are required for consequential information/actions; the visual canvas is not the sole representation of authoritative Scene state.
