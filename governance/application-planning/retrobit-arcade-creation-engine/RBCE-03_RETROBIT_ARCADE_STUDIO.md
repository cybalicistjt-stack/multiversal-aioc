# RBCE-03 — Retrobit Arcade Studio

**Program:** Retrobit Arcade & Creation Engine (RBCE)  
**Work item:** RBCE-03  
**Status:** OWNER-DIRECTED DESIGN BASELINE  
**Owner and final authority:** John Brandon Turner  
**Operational authority:** none; this design does not select live product implementation and cannot override OPS3  
**Consumes:** RBCE-01 Retrobit Game Project Format, RBCE-02 Retrobit 2D Projection Runtime  
**Presentation:** `retrobit-classic-arcade` skin by default, with shared accessibility-safe UI behavior

## 1. Purpose

RBCE-03 defines the creator-facing **Retrobit Arcade Studio**: the workspace used to create, edit, validate, playtest and prepare Retrobit Game Projects without hand-editing JSON or writing game-specific code.

The Studio exists to satisfy the charter rule **build games, not configuration puzzles**.

A creator should be able to:

1. create or open a Retrobit project;
2. choose a starting template or blank project;
3. build scenes/rooms/levels visually;
4. place actors, assets, regions, triggers and exits;
5. attach governed gameplay definitions and behaviors;
6. configure variables, outcomes, controls, audio and accessibility;
7. switch into a faithful playtest quickly;
8. inspect diagnostics without losing work;
9. save a valid RBCE-01 project;
10. reach an explicit publish-readiness result without the Studio inventing missing rights or gameplay authority.

RBCE-03 is an authoring surface over existing contracts. It is not a second rules engine, scene engine, asset authority, scripting platform or package format.

## 2. Authority boundary

### 2.1 Studio owns authoring interaction

RBCE-03 owns:

- project/workspace navigation;
- editor layout and selection state;
- visual authoring gestures;
- draft edits to RBCE-01 project data;
- editor-only view state such as pane sizes, zoom and current selection;
- validation presentation;
- playtest launch/stop/reset controls;
- comparison between draft source and playtest snapshot;
- undo/redo history for Studio-authored draft changes;
- autosave/recovery of draft authoring state;
- creator-facing diagnostics and source-location navigation.

### 2.2 Studio does not own semantic truth

The Studio may not independently define or mutate canonical truth belonging to:

- GPR gameplay patterns, operations or deterministic runtime;
- MRCS reusable definitions;
- MAI assets, rights or provenance;
- ISE/Scene/World semantic ownership;
- Character, NPC, Combat, Inventory, Economy or Campaign owner domains;
- AAI/MSAS audio definitions;
- RBCE-02 projection semantics;
- package/install/entitlement authority.

The Studio edits references and project-owned composition. Owner mutations occur only through the owning system.

### 2.3 Preview is not canon

Playtest and preview state are disposable projections unless a governed owner operation explicitly commits an allowed result.

Closing or resetting a playtest must not mutate:

- campaign state;
- character inventory;
- campaign objectives;
- published project versions;
- reusable MRCS definitions;
- MAI source assets.

## 3. Primary user model

RBCE-03 is designed first for a **creator/GM who understands the game they want to make but should not need to understand internal schema layout**.

The normal path is visual and guided.

Advanced users may inspect stable IDs, dependency references and normalized diagnostics, but there is no arbitrary script editor in v1.

AI assistance, where available, is optional and proposal-only. Provider-off authoring remains complete.

## 4. Studio information architecture

The Studio uses five persistent conceptual regions on desktop:

1. **Project Navigator** — project, scenes, tests and settings hierarchy.
2. **Tool/Palette Rail** — placeable assets, actors, geometry and governed gameplay parts/references.
3. **Main Canvas** — visual scene/room/level editor or selected nonspatial editor.
4. **Inspector** — properties and bindings for the current selection.
5. **Playtest & Diagnostics Tray** — validation, playtest state, logs, tests and blocking issues.

The application shell additionally provides shared authoring affordances where applicable:

- breadcrumbs;
- global search;
- command palette;
- rule inspector;
- provenance viewer;
- save/autosave state;
- undo/redo;
- validation status;
- playtest button;
- project mode switcher.

The Retrobit skin provides stepped arcade construction and identity. Protected validation, permission, accessibility and provenance states retain their shared semantic styling.

## 5. Responsive behavior

### Desktop

Desktop is the primary authoring target:

`Navigator | Palette | Canvas | Inspector`

with a collapsible bottom diagnostics/playtest tray.

### Tablet

- navigator and palette collapse into drawers;
- inspector becomes a drawer or secondary pane;
- canvas remains the primary workspace;
- playtest may occupy the full content area.

### Mobile

Mobile supports meaningful review and bounded editing, but does not pretend that every dense map-authoring gesture is equally efficient.

Required mobile capabilities include:

- open/project review;
- validation review;
- property edits that fit the form model;
- scene hierarchy edits;
- test/playtest controls where input layout permits;
- accessible alternatives for drag operations;
- save/recovery.

No required project field may become impossible to reach solely because the user is on a smaller screen.

## 6. Studio modes

RBCE-03 v1 defines four workspace modes.

### `studio:project`

Project-level configuration:

- identity, version and lineage visibility;
- compatibility/capability references;
- delivery modes;
- project-level accessibility;
- provenance summary;
- project tests;
- publish-readiness summary.

### `studio:build`

Primary visual authoring mode:

- scenes/rooms/levels;
- layers;
- placements;
- geometry;
- exits;
- triggers;
- actor/asset bindings;
- camera/projection choices;
- movement and constraint profile selection.

### `studio:logic`

Structured non-script logic/composition mode:

- GPR loop/pattern/operation references;
- MRCS rule/definition references;
- project variables;
- prerequisites;
- outcomes;
- input bindings;
- audio bindings;
- declarative test cases.

This mode uses forms, graphs, tables and dependency views rather than free-form executable code.

### `studio:playtest`

Runs an isolated playtest snapshot from the current structurally valid draft.

The author can:

- start;
- pause when supported;
- restart scene;
- restart run;
- stop;
- inspect state;
- compare draft versus runtime snapshot;
- execute project test cases;
- jump from a diagnostic to its source object.

## 7. Project creation flow

The project creation flow is:

`New Project`
→ choose `Blank`, `Template`, or `Import Existing Retrobit Project`
→ establish identity
→ choose default projection family
→ choose movement profile where applicable
→ choose retro constraint profile
→ choose delivery modes
→ create first scene
→ enter Studio.

Templates provide initial references/configuration only. Creating from a template creates new project identity and lineage.

RBCE-03 does not define the full creator-facing Gameplay Parts taxonomy; RBCE-05 owns that later projection. Until RBCE-05 exists, Studio consumes stable governed references and may use minimal descriptive labels already provided by owners.

## 8. Project Navigator

The Project Navigator exposes at least:

- Project
- Scenes
- Actors
- Variables
- Inputs
- Outcomes
- Audio
- Accessibility
- Tests
- Provenance
- Publishing Readiness

Scene nodes expose:

- layer stack;
- entry points;
- exits;
- placements;
- geometry/regions;
- trigger references;
- local variables.

Navigator operations:

- add;
- duplicate where identity rules permit;
- rename;
- reorder only where order is semantic;
- move;
- archive/remove from draft;
- reveal dependencies;
- reveal inbound references;
- jump to diagnostic.

Deleting a referenced object must fail or require an explicit reference-repair choice. The Studio must never silently orphan references.

## 9. Palette model

The Palette presents **things that may be placed or bound**, not arbitrary files.

Initial categories:

- Actors
- Visual Assets
- Tiles/Maps
- Geometry
- Regions/Triggers
- Entries/Exits
- Checkpoints/Spawns
- Audio Roles
- Gameplay References
- Templates/Presets

Palette items retain source identity and provenance.

The Studio may show thumbnails, labels and compatibility badges, but it must not flatten MAI assets into untraceable local copies.

RBCE-04 later owns specialized sprite/tile asset preparation. RBCE-03 only selects, places and configures already available/imported assets.

## 10. Canvas and scene editing

The Main Canvas must support:

- pan and zoom;
- fit/focus selection;
- grid visibility and snapping;
- pixel-grid preview;
- layer visibility/locking;
- selection/multiselection;
- drag/drop placement with keyboard equivalent;
- move/resize/rotate only where the bound geometry supports it;
- authored depth/layer ordering;
- region and collision geometry visualization;
- entry/exit links;
- trigger linkage visualization;
- camera bounds and viewport preview;
- spawn/checkpoint markers;
- projection-profile preview;
- constraint-profile preview.

The canvas edits authoring data. Camera zoom, pane size and editor selection are editor-only state and do not alter project fingerprints.

## 11. Inspector

The Inspector is contextual and must explain what is being edited.

For a selected object it may show:

- stable identity;
- label;
- owner/source;
- bound asset/definition references;
- transform/placement;
- layer role;
- projection properties;
- collision/geometry role;
- animation/presentation bindings;
- variable/rule bindings;
- prerequisite references;
- outcome references;
- accessibility metadata;
- provenance/rights state;
- validation issues;
- inbound/outbound references.

Advanced IDs may be visible, but ordinary users should work primarily with names, categories and controls.

Fields unavailable because of projection/profile/permission constraints are disabled with an explanation rather than silently omitted when the distinction matters.

## 12. Structured logic/composition tools

The Studio must provide bounded editors for the RBCE-01 composition areas that are awkward to author directly on a canvas.

### Variables

Table/form editor for:

- variable ID;
- type;
- scope;
- default;
- allowed enum values where applicable;
- write policy.

Campaign-projection variables remain owner proposals and cannot become direct campaign mutation.

### Inputs

Input editor maps device inputs to semantic commands.

The Studio must make it possible to test at least:

- primary input mapping;
- accessibility/alternate mapping.

### Outcomes

Outcome editor binds:

- outcome identity;
- owning domain;
- governed operation;
- parameter bindings;
- permitted delivery modes.

The Studio must show clearly that an outcome is a proposal/owner handoff, not an unconditional local mutation.

### Tests

Test authoring uses declarative commands and assertions from RBCE-01. No arbitrary test scripting is introduced.

## 13. Validation model

Validation is continuous but must not be noisy.

The Studio groups results into:

- **Blocking** — project cannot perform the requested action.
- **Needs attention** — valid draft but incomplete for a later lifecycle gate.
- **Advisory** — quality/usability issue.
- **Information** — resolved dependency/provenance context.

Validation stages map to existing owners:

1. RBCE-01 structural project validation.
2. RBCE semantic/reference validation.
3. GPR capability/runtime binding validation.
4. RBCE-02 projection/profile validation.
5. MAI asset/provenance/rights validation.
6. owner-domain definition/operation validation.
7. accessibility critical-path validation.
8. project test execution.
9. publishability validation.

The Studio never converts an unresolved required dependency into a local invented definition.

## 14. Lifecycle presentation

The Studio displays the RBCE-01 lifecycle distinctly:

- Draft
- Structurally Valid
- Playable
- Publishable
- Migration Required
- Blocked

**Playable** and **Publishable** remain separate.

A creator may playtest an original local project that is not yet publishable because redistribution rights are unresolved.

The UI must not display “ready to publish” merely because a playtest succeeds.

## 15. Playtest contract

Playtest is a first-class authoring loop:

`Edit → Validate → Snapshot → Play → Inspect → Stop/Reset → Edit`

Rules:

- playtest uses a stable snapshot/fingerprint of the draft;
- changing the draft while a playtest is active either queues the edit for next run or visibly invalidates/hot-reloads only presentation-safe fields according to implementation policy;
- semantic hot reload is not assumed;
- playtest runtime is deterministic under the same accepted inputs/state;
- playtest state is isolated from canonical campaign/save state unless a specific test harness owner explicitly supplies a sandbox;
- stopping restores the authoring workspace without losing draft changes;
- diagnostics can link runtime failures back to authoring objects.

## 16. Undo, autosave and recovery

The Studio requires:

- undo/redo for reversible draft-authoring operations;
- autosave of draft state;
- explicit saved-version checkpoints where supported;
- recovery after interruption;
- unsaved-change warning where a destructive context switch would lose data;
- no undo operation that silently rewrites external owner records.

Undo/redo history is editor history, not canonical gameplay event history.

## 17. Provenance and rights UX

Rights/provenance state is visible where it matters:

- asset Inspector;
- project readiness;
- dependency views;
- publishability diagnostics.

The Studio must distinguish at least:

- original/user-owned;
- licensed/permitted;
- public-domain or equivalent governed state;
- reference-only/research-only;
- unresolved;
- redistribution forbidden/limited where known.

Protected/reference-only material may remain visible as research provenance without becoming a production dependency.

## 18. Accessibility

The Studio follows the Multiversal UI/Screen bibles:

- keyboard-first authoring;
- screen-reader landmarks;
- touch alternatives for drag;
- non-color validation indicators;
- high-contrast compatibility;
- reduced-motion compatibility;
- scalable text/HUD;
- accessible labels for icon-only controls;
- focus preservation across inspector/canvas interactions.

Spatial editing requires a non-pointer alternative. At minimum, users must be able to:

- select an object from a hierarchy/list;
- move it by keyboard or numeric properties;
- edit geometry numerically/structurally where direct manipulation is inaccessible;
- inspect relationships and diagnostics without reading the visual canvas alone.

## 19. Retrobit visual identity

The default Studio presentation uses `retrobit-classic-arcade`.

The Studio inherits:

- stepped 90-degree construction;
- dark cabinet/pixel-panel surfaces;
- blue/red/yellow identity accents;
- score-like numerals where appropriate;
- blocky control housings;
- restrained CRT framing.

However:

- body text remains highly readable;
- sustained authoring text is not placed under moving scanlines;
- semantic status colors remain accessibility-safe;
- dense editors prioritize legibility over nostalgia;
- the skin never changes editor behavior or project semantics.

## 20. AI boundary

Optional AI may propose:

- project scaffolding;
- scene descriptions;
- asset search terms;
- variable/test suggestions;
- diagnostics explanations;
- template selection;
- accessibility reminders.

AI may not:

- silently commit edits;
- invent rights;
- claim unresolved dependencies are valid;
- mutate owner-domain canon;
- replace deterministic validation;
- make cloud access mandatory for normal authoring.

Every AI-authored change enters the same draft/validation path as a human-authored change.

## 21. Four-Engine Test Chamber Studio acceptance

RBCE-03 is design-complete only when its Studio contract can author/edit the RBCE-01 Four-Engine Test Chamber without hand-editing JSON or game-specific code.

The Studio proof must cover:

1. create/open the project;
2. edit the top-down plaza scene and exit;
3. edit the fixed-room gated scene and prerequisite reference;
4. edit the side-scroll foundry platform/hazard/checkpoint layout;
5. edit the dialogue scene’s governed dialogue reference and persistent variables;
6. swap between `retrobit-standard` and an inspired retro constraint profile without changing semantic gameplay;
7. remap an alternate/accessibility input profile;
8. run the four project tests;
9. locate and repair at least one deliberately broken reference through diagnostics;
10. demonstrate playable vs publishable distinction;
11. stop/reset playtest without campaign/canonical mutation;
12. recover the draft after an interrupted authoring session.

## 22. Machine contract identifiers

RBCE-03 machine-readable design artifacts use:

- schema ID: `RBCE03.STUDIO.v1`
- semantic schema version: `1.0.0`
- default skin: `retrobit-classic-arcade`

Required Studio mode IDs:

- `studio:project`
- `studio:build`
- `studio:logic`
- `studio:playtest`

Required desktop region IDs:

- `region:project-navigator`
- `region:palette`
- `region:main-canvas`
- `region:inspector`
- `region:playtest-diagnostics`

## 23. Explicit non-goals

RBCE-03 does not define:

- asset slicing/pixel-art preparation tools — RBCE-04;
- the final creator-facing Gameplay Parts taxonomy — RBCE-05;
- the final golden shipped game content — RBCE-06;
- distribution/store/installation entry points — RBCE-07;
- arbitrary scripting;
- ROM import/emulation;
- a new asset or rights authority;
- a new gameplay runtime;
- a new campaign state engine;
- a required cloud collaboration service;
- a marketplace.

## 24. Activation boundary

This is a durable content/design contract only.

Product implementation begins only when OPS3 explicitly selects and authorizes RBCE-03 or equivalent governed implementation work. PCV-03F and other live selectors are unaffected by this artifact.
