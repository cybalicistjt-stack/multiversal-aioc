# PPIA-06 — Character Appearance Creator Source and Design Inventory

**Work item:** PPIA-06 — Character Appearance Creator  
**Foundation scope:** renderer-independent appearance semantics plus the first governed renderer profile, `pixel-art-v1`.

## Authority order

PPIA-06 does not reopen or reinterpret Species/Form biology. It consumes the verified PPIA-05 contract: reusable Species/Form Definitions are distinct from Character selection/current body/form state; unknown or source-unspecified anatomy and compatibility remain unknown; hidden biological information is permission-filtered before projection; and accessible nonvisual morphology/selection/transformation are required.

PPIA-03 remains authoritative for Item/Asset Definition versus Asset-instance state, ownership/custody/possession/control/access, equipment state, runtime Resource state, lineage, and permission-safe projections. An appearance preview may display authorized equipment but cannot grant, consume, transfer, equip, unequip, or otherwise mutate it.

MV-IA-F004 keeps Player-authored descriptive identity separate from governed mechanical selections, uses stable IDs/versioned references, and explicitly excludes full 3D appearance sculpting from its internal-alpha slice while deferring richer visual appearance to later work. Its responsive/accessibility contract includes desktop, tablet, mobile, keyboard, touch, screen-reader, high-zoom, reduced-motion, and noncolor-status behavior.

The approved project design source `SCREEN_DESIGN_BIBLE.md`, section SD-105 — Character Appearance, requires Body, Face, Hair, Colors, Clothing preview, Equipment preview, Accessibility preview, Randomize, Save preset, and Import/export appearance. Shared character-screen requirements include keyboard navigation and responsive layouts. The approved `UI_DESIGN_BIBLE.md` requires desktop/tablet/phone usability; operation without reliance on color, motion, or pointer input; keyboard operation; screen-reader semantics; touch targets and non-drag alternatives; noncolor status; high-zoom/text scaling; mobile primary-task preservation; and reduced-motion behavior.

The PPIA-11→PPIA-06 transition records the owner-selected visual direction: high-detail modular pixel art is the first fully specified renderer. That direction is a renderer profile, not Species taxonomy and not a permanent limitation of Character appearance data.

## Evidence boundary

Six evidence classes are retained: `source_truth`, `inherited_contract`, `project_source_design_contract`, `player_authored_appearance`, `renderer_metadata`, and `unresolved_gap`.

Renderer metadata never becomes Species/Form truth. Player-authored appearance never becomes biological truth. Missing renderer support never becomes missing Character validity.

## Verified inherited source surface

The foundation inherits, rather than re-audits, the completed PPIA-05 evidence boundary: 29 direct Species/Form/Biology PDFs / 654 pages; 6 supporting environment/Adaptation PDFs / 233 pages; a governed 2,203-row mixed Species/Elementalist/Innate Ability surface; and a supporting 1,018-row prestige/environment/special Ability surface including 296 Environment-Based Ability Collection rows. These counts are provenance anchors, not a license to infer new anatomy.

PPIA-03 contributes its verified 5,389-row Item CSV surface only through the completed Item/Asset contracts. PPIA-06 does not reinterpret Item rows as appearance truth.

## Renderer-independent semantic model

The appearance state is defined across eighteen renderer-independent, independently inspectable layers, beginning with identity/version and authoritative morphology/current-Form projections and ending with renderer coverage/fallback and accessibility/nonvisual summary. The core state has no mandatory sprite filename, pixel coordinate, texture, mesh, bone, or renderer-specific asset field.

Compatibility remains four separate compatibility dimensions and must not be collapsed: biological validity; appearance-choice compatibility; renderer compatibility; and equipment visual compatibility.

Renderer support is `supported`, `partial`, `unsupported`, or `unknown`. `partial`, `unsupported`, and `unknown` are presentation states, not Character invalidity.

## `pixel-art-v1` architecture

`pixel-art-v1` uses stable asset IDs, semantic render bands, semantic anchors, explicit occlusion masks, controlled palette zones/ramps, topology support matrices, stable pose IDs, and version-pinned asset-pack locks.

The universal minimum semantic anchors are `root`, `visual_center`, `portrait_focus`, and `occupancy_bounds`. Topology profiles may require additional anchors. A missing required anchor produces partial/unsupported renderer coverage; it never authorizes anatomical approximation.

Semantic render bands are not a fixed humanoid skeleton and are not Species taxonomy. Topology-specific overrides are allowed. Nonhumanoid topology is first-class.

Palette zones and ramps have semantic names and noncolor labels. Color alone never communicates eligibility, visibility, support, selection, warning, or state.

A semantic render plan is deterministic for the same authorized appearance-state version, authoritative Form snapshot, renderer/version, asset-pack lock, pose, view, and permission-projection version.

## Presets and randomization

Presets may carry portable Player-authored appearance choices and renderer preferences. They do not carry or override source-owned morphology, hidden biological state, or equipment ownership.

Randomization is deterministic from seed + lock set + eligible-choice-set version + appearance-state version. It can only select among currently authorized Player-authored choices. Locked fields remain fixed. Source-owned morphology, current Form, hidden state, and equipment ownership are never randomized.

## Permission and hidden-information boundary

Permission filtering occurs before hidden morphology or equipment is used for asset selection, derivative summaries, silhouette/layer behavior, counts, renderer diagnostics, exports, or AI context. Hidden state may not leak through a different asset count, missing-asset warning, palette zone, anchor, occlusion behavior, or fallback message.

## Form changes

A transformation or current-Form change is owned by PPIA-05/the Character workflow. PPIA-06 reprojects the new authorized current Form and may retain only portable Player-authored choices that remain compatible. It never silently carries incompatible anatomy or invents replacement features.

## Portrait/token and future-renderer handoff

Portrait and token outputs are versioned presentation handoffs derived from the same semantic appearance state and permission projection. They do not become Character truth.

A future 3D renderer must be able to consume the same renderer-independent semantic state through its own adapter. No `pixel-art-v1` sprite/pixel metadata is mandatory in the Character appearance aggregate.

## Foundation QA corpus

Twenty-four explicitly noncanonical synthetic QA fixtures cover supported humanoid-like rendering, nonhumanoid topology, valid Characters with unsupported renderers, unknown anatomy, current-Form changes, preset portability, hidden markers, equipment projection/nonleak, accessibility, deterministic randomization, asset-pack replay/version mismatch, missing anchors/masks, portrait/token outputs, and the future 3D boundary.

## Non-activation boundary

This foundation does not activate application runtime, STAGE-A-A2, release, deployment, tester access, paid services, production credentials, or canonical promotion of unsupported source content.
