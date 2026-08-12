# PPIA-08 — Campaign / Scene / Session Authoring Experience Specification v1.0.0

**Work item:** PPIA-08 — Campaign / Scene / Session Authoring Depth  
**Specification state:** IMPLEMENTATION-READY COMPLETION CANDIDATE  
**Runtime activation authorized:** No  
**STAGE-A-A2 activation authorized:** No

## 1. Purpose

This specification locks the verified PPIA-08 design into an implementation-ready Campaign / Scene / Session authoring contract. It does not redesign the earlier milestones. It integrates the verified foundation, Inspector/action/reference corpus and end-to-end workflow package into one final implementation target.

The completion target is the canonical PPIA-08 gate: an implementation-ready Campaign/Scene/Session authoring packet with hierarchy, templates, content placement, hidden state, branching, preparation/live/post-session workflows, reference Campaign material, GM map-image upload with grid scale/alignment calibration, cell-addressable assignment of items/hazards/encounters/other governed Scene content, and a basic dungeon-map construction kit.

PPIA-08 defines authoring semantics and integration boundaries. It does not activate the application runtime and it does not claim final Encounter or system balance calibration.

## 2. Authority and provenance boundary

The retained authority set contains **9 canonical repository sources** and **3 retained supporting design-source groups**.

Canonical sources are MV-IA-F005, F020, F021 and F012 plus the completed PPIA-12, PPIA-02, PPIA-03, PPIA-04 and PPIA-05 experience contracts. The retained supporting design sources are `SCREEN_DESIGN_BIBLE.md`, `UI_DESIGN_BIBLE.md` and `FEATURE_BIBLE.md`.

The owner-directed map extension dated 2026-08-11 is blocking. It requires GM map-image upload, square-grid scale/cell-size calibration, grid pan/origin-offset alignment, versioned calibration lock/recalibration, cell/area-addressable Scene content assignments, stable Item/Hazard/Encounter and other governed placements, and a basic dungeon-map construction kit.

The retained sources establish map/media references, map and Scene authoring intent, grid/gridless presentation, layers, triggers, hidden information, launch snapshots, recovery and accessibility. They **do not** define the exact uploaded-image square-grid calibration transform, the cell-addressing schema, or the dungeon primitive schema. Those elements are therefore governed PPIA-08 implementation-ready design, not recovered source canon.

## 3. Governed semantic model

PPIA-08 preserves **16 semantic identity/state layers**:

1. Campaign definition and policy.
2. Membership, role and character control.
3. Scene definition and hierarchy.
4. Scene template and branching.
5. Reusable source reference.
6. Campaign-local placement and override.
7. Map/media asset reference.
8. Grid calibration and coordinate transform.
9. Cell/area/zone addressing.
10. Map-content placement and layering.
11. Dungeon geometry and construction.
12. Hidden/reveal and knowledge state.
13. Encounter/objective/trigger/event links.
14. Preparation, launch snapshot and Session binding.
15. Live-Session amendment and post-session history.
16. Permission, provenance, recovery and accessibility.

The required presentation surface remains **12 profiles**: Campaign Overview; Campaign Policy & Membership; Scene Outline & Branching; Scene Builder; Map Asset & Grid Calibration; Grid Cell/Area/Zone Inspector; Placement Layer Browser; Dungeon Construction Kit; Hidden/Reveal Preview; Launch Readiness & Snapshot; Live Session Control & Amendment; and History/Recovery/Accessible Linear View.

## 4. Aggregate and ownership model

Campaign, Scene and Session are distinct governed aggregates and lifecycles.

Reusable Definitions remain owned by their source domains. PPIA-08 stores Campaign-local composition, local allowed overrides, placements, visibility/knowledge state, map calibration, dungeon geometry, launch packaging, governed live amendments and post-session history. It never takes ownership of reusable Definitions merely because they are placed in a Scene.

Stable references use `ownerDomain`, `objectId` and `objectVersion`. A large Vehicle or other multi-cell object is represented by one owning object and one placement over a semantic area; the source object is not duplicated per occupied cell.

Ownership handoffs remain exactly **10**:

- `P8-HO-001` MV-IA-F005 Campaign/Scene/Session Builder.
- `P8-HO-002` PPIA-12 World/Setting Authoring.
- `P8-HO-003` PPIA-02 Creature/NPC Experience.
- `P8-HO-004` PPIA-03 Items/Inventory Experience.
- `P8-HO-005` PPIA-04 Vehicle Experience.
- `P8-HO-006` PPIA-05 Species/Forms Biology.
- `P8-HO-007` MV-IA-F012 / PPIA-11 Encounter & Balance.
- `P8-HO-008` MV-IA-F020 Permissions.
- `P8-HO-009` MV-IA-F021 Recovery.
- `P8-HO-010` Battle Map / Scene Builder design standards.

## 5. Inspector and action contract

The final implementation target preserves **16 Inspector projection groups** (`P8-PG-001..016`) and **26 governed actions** (`P8-ACT-001..026`).

Of the 26 actions, **22 are authoritative mutations** and four are read/validation operations. Every authoritative mutation uses the global protocol:

1. authorize the current subject, role and delegation before protected reference resolution;
2. revalidate aggregate, source-reference, map, calibration and placement versions;
3. require `expected_version`;
4. require a stable `operation_id`;
5. after an ambiguous response, query operation status and current version before retry;
6. return the prior compatible result for duplicate operation-ID retry while rejecting conflicting reuse;
7. emit attributable durable evidence only after an accepted atomic mutation.

Blind last-write-wins is prohibited. Broad offline authoritative Campaign/map/Session mutation is prohibited; safe local drafts may be retained only where the owning contract permits them.

## 6. Map asset and calibration contract

Uploaded map image bytes and grid calibration are separate versioned objects. Calibration never destructively rewrites the image.

The required initial coordinate modes are **square** and **gridless**. PPIA-08 does not invent a universal distance-per-square.

A square-grid calibration contains at least:

- `calibrationId`;
- calibration `version`;
- `mapMediaReferenceId`;
- `cellSizePx`;
- `originOffsetXPx`;
- `originOffsetYPx`;
- `locked`;
- `expected_version` for mutation.

`cellSizePx` is the square side length in source-image pixel space. `originOffsetXPx` and `originOffsetYPx` translate the grid origin relative to the image origin. This grid translation is authoring/calibration state and is explicitly different from camera pan/zoom view state.

Recalibration creates a new calibration version. Prior versions remain attributable and recoverable. Post-launch recalibration never silently moves content in an active Session.

## 7. Semantic location addressing

Square-cell identity uses stable integer `column,row` under a specific calibration ID and version. Areas may span multiple cells. Named zones are permitted. Gridless Scenes use named or described semantic locations.

The required location reference kinds are:

- `cell`;
- `cell-area`;
- `named-zone`;
- `gridless-location`.

A visual pixel position alone is never the sole authoritative location meaning.

## 8. Placement and layer authoring

Campaign-local placement records preserve a stable owning-object reference and a semantic location reference. Required placement kinds include Item, Hazard, Encounter, Creature/NPC, Vehicle, Objective, Trigger, Note, environment feature, door feature, transition marker and other governed Scene content.

Placement editing may change permitted local location, layer, z-order, local state, label and visibility metadata. It may not silently rewrite the referenced reusable Definition.

Multiple placements may reference the same source Definition where the owning domain permits that composition. Multi-cell occupancy does not create duplicate owning objects.

## 9. Hidden information and reveal

Authorization and filtering occur before protected reference resolution, aggregation or serialization.

Unauthorized users must not learn hidden Scene/map existence through counts, labels, search/autocomplete, layer serialization, errors, exports, diagnostics, notifications or AI context.

Reveal is a governed knowledge-state mutation, not merely a client-side visual toggle. A Player projection changes only after the reveal mutation is accepted and authorized.

## 10. Dungeon-map construction kit

PPIA-08 locks **seven dungeon primitive families**:

1. room/floor region;
2. corridor/path region;
3. wall segment;
4. door/opening;
5. terrain/feature region;
6. stairs/portal/transition marker;
7. reusable tile/stamp.

Permitted authoring operations include create, select, move, resize where the primitive permits, duplicate, remove, undo, redo and grid snapping where the Scene coordinate mode permits it.

Dungeon output is Scene-owned authoring geometry with both renderable and semantic/nonvisual projections.

Dungeon geometry does **not** invent or imply collision, line of sight, cover, movement legality, damage, lighting, fog simulation, procedural-generation rules, Encounter power or balance.

## 11. Encounter, objective, trigger and Event links

PPIA-08 may place and link Encounter references, objectives, hazards, spawn/location metadata, triggers and durable Event hooks.

Encounter Definition, simulation, tactical resolution and final balance remain owned by MV-IA-F012 / **PPIA-11**. PPIA-08 does not derive Encounter legality, threat or balance from map artwork or dungeon geometry.

## 12. Launch readiness and immutable Session snapshots

Launch readiness resolves an exact candidate version set and returns permission-safe blocking findings.

A launch snapshot pins the exact Campaign/Scene composition and the required map asset, calibration, placement and visibility-policy versions plus Session-binding inputs. The snapshot is immutable.

Later map replacement, recalibration, placement change or visibility change does not silently rewrite the active Session. Adoption into live play requires either a new launch snapshot for a future/new Session or a governed live-session amendment.

## 13. Live amendments and post-session history

Live changes use explicit amendment proposal and decision paths. Accepted amendments preserve exact changed references, before/after versions, decision evidence and durable Event evidence. The original launch snapshot remains attributable.

Post-session outcomes are Campaign-local history. They do not rewrite reusable Setting, Creature/NPC, Item, Vehicle or Species/Form Definitions.

## 14. Recovery and concurrency

Every authoritative write is optimistic-concurrency and idempotency aware through `expected_version` and `operation_id`.

A stale expected version fails safely with current-version and recovery information. An ambiguous response requires operation-status/current-version lookup before retry. Repeating a compatible operation ID returns the existing result/status rather than duplicating placements, snapshots, amendments or other authoritative state.

Reconnect and recovery must reauthorize access before protected Scene/map/history data is returned.

## 15. Accessibility and nonvisual equivalence

The visual map is never the only authoritative representation.

Every required visual map/grid/layer/drag/geometry operation has an equivalent ordered semantic path supporting keyboard operation, touch alternatives, high zoom/reflow, screen-reader summaries and nonvisual authoring. Required meaning never depends solely on drag, hover, color, animation or pixel position.

Square cells, areas, named zones, gridless locations, placements, hidden/reveal state, dungeon geometry, launch snapshots, amendment history and recovery status are all representable textually and semantically.

Gridless Scenes are first-class rather than a degraded accessibility fallback.

## 16. Integrated workflow contract

The implementation target preserves **17 end-to-end authoring workflows**, of which **15 perform authoritative mutation**:

1. Campaign setup, policy, membership and bounded delegation.
2. Scene hierarchy, templates and explicit branching.
3. Reusable source-reference preparation and permitted Campaign-local overrides.
4. Map-image asset upload, replacement and attribution.
5. Square-grid calibration, preview, lock and recalibration.
6. Cell, multi-cell-area, named-zone and semantic location authoring.
7. Scene content placement, movement, layering and multi-cell occupancy.
8. Hidden content, knowledge state and governed reveal.
9. Basic dungeon construction and semantic geometry editing.
10. Encounter, objective, trigger and Event-link authoring.
11. Launch readiness, immutable snapshot and Session binding.
12. Governed live-Session amendment proposal and decision.
13. Post-session outcome, history and reusable-definition isolation.
14. Reconnect, stale-write conflict and ambiguous-operation recovery.
15. Semantic nonvisual map, Scene and history authoring.
16. Gridless Scene authoring and placement.
17. Post-launch map replacement or recalibration isolation and adoption.

Traceability remains zero-gap across all 16 projection groups, 12 presentation profiles, 26 actions, 26 reference cases and 10 handoffs.

## 17. Reference corpus

The final contract preserves all **26 contiguous reference cases `PPIA08-RC-001..026`**. They cover Campaign policy and delegation; Scene hierarchy/templates/branching; reusable references and local overrides; upload/replacement; square-grid calibration; camera/calibration separation; cell/zone and multi-cell locations; Item/Hazard/Encounter/Creature/Vehicle placement; gridless authoring; all seven dungeon primitive families; hidden non-leak and reveal; launch snapshots; post-launch recalibration isolation; live amendment; post-session history; stale-version conflict; duplicate retry; and accessible nonvisual authoring with revoked access.

## 18. Final acceptance policy

PPIA-08 completion is blocked unless the final acceptance matrix verifies **48 requirements across 16 categories** and traces the entire verified design surface:

- 9 canonical repository sources and 3 retained supporting design-source groups;
- 16 semantic layers;
- 12 presentation profiles;
- 16 projection groups;
- 26 actions / 22 authoritative mutations;
- 26 reference cases;
- 17 workflows / 15 authoritative-mutation workflows;
- 10 domain handoffs;
- square + gridless coordinate modes;
- `cellSizePx` plus X/Y origin-offset square-grid calibration;
- 7 dungeon primitive families;
- immutable launch snapshots;
- permission-before-aggregation;
- expected-version/idempotent recovery;
- semantic nonvisual authoring.

## 19. Completion and balance boundary

This specification is sufficient to implement the Campaign / Scene / Session authoring experience and to construct deterministic test fixtures for the verified authoring behaviors.

It does **not** claim that every Encounter or map arrangement is numerically balanced, tactically legal or physically simulated. **PPIA-11 retains final Encounter/balance calibration authority.**

It also does not authorize application-runtime mutation, STAGE-A-A2 activation, release, deployment, tester access, paid services, production credentials or unsupported source/canon promotion.

PPIA-08 may become `completed_verified` only after this final completion package passes its exact-head completion gate and every applicable repository regression, merges to canonical main, and the post-merge checkpoint/backlog evidence records the validated exact head, pull request and merge.