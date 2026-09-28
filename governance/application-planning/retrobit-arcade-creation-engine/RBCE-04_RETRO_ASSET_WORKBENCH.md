# RBCE-04 — Retro Asset Workbench

**Program:** Retrobit Arcade & Creation Engine (RBCE)  
**Work item:** RBCE-04  
**Status:** OWNER-DIRECTED DESIGN BASELINE  
**Owner and final authority:** John Brandon Turner  
**Operational authority:** none; this design does not select live product implementation and cannot override OPS3  
**Consumes:** RBCE-01 project assets/bindings, RBCE-02 projection constraints, RBCE-03 Studio, MAI-01..08 asset/provenance/import/resolver/workbench contracts  
**Presentation:** `retrobit-classic-arcade` by default; shared accessibility/status semantics remain authoritative

## 1. Purpose

RBCE-04 defines the **Retro Asset Workbench**, the Retrobit-specific pixel-art and 2D asset preparation surface used to create original assets and prepare permitted imported assets for Retrobit projects.

The workbench fills the gap between generic MAI asset interoperability and the creator experience needed for sprite/tile-driven games.

A creator must be able to:

1. create a new original pixel asset locally;
2. intake an already supplied/catalogued asset through MAI evidence;
3. crop/trim and perform bounded pixel-safe transforms when permission allows;
4. slice sprite sheets or tile sheets deterministically;
5. edit original pixel art with a bounded pixel editor;
6. define frames, animation groups, anchors and draw offsets;
7. build tilesets and visual terrain groupings without inventing gameplay truth;
8. preview palette/size constraints for Retrobit Standard, 8-bit-inspired, 16-bit-inspired and custom profiles;
9. preserve source, checksum, lineage, permission and unsupported metadata;
10. hand off validated assets/metadata to MAI and RBCE-03 without publishing a `.pack` or mutating canonical gameplay state.

RBCE-04 is not a general-purpose Photoshop replacement and is not an asset marketplace/downloader.

## 2. Authority boundary

### 2.1 MAI remains canonical asset/provenance authority

RBCE-04 consumes MAI rather than replacing it.

Binding rules:

- MAI-01 license/authority evidence remains binding.
- MAI-02 canonical asset/package/source/provenance records remain the asset data authority.
- MAI-03 projection/scale data remains presentation geometry.
- MAI-04 terrain connectivity remains visual connectivity only.
- MAI-05 geometry/occlusion/interaction hints remain descriptive.
- MAI-06 import adapters own provider-specific structured translation.
- MAI-07 owns eligibility, semantic requirement resolution, cross-pack substitution and explicit unresolved outcomes.
- MAI-08 owns reversible evidence-aware intake/workbench draft semantics.

RBCE-04 specializes those contracts for Retrobit pixel/sprite/tile preparation.

### 2.2 RBCE-04 owns only Retrobit authoring intent and permitted derived presentation assets

RBCE-04 may own:

- workbench document state;
- pixel-editor state for user-authored originals or transform-permitted derivatives;
- deterministic slice definitions;
- frame/animation presentation metadata;
- anchors and draw offsets;
- palette definitions/remaps;
- bounded nearest-neighbor scaling/cropping/trimming;
- tile extraction and visual grouping;
- atlas/sheet layout intent;
- Retrobit constraint-analysis results;
- reversible authoring history;
- deterministic derived-asset lineage receipts.

It may not independently create:

- World/Scene/Combat/Exploration truth;
- collision/cover/line-of-sight adjudication;
- GPR operations or gameplay rules;
- permissions or licenses;
- campaign/character state;
- publishing rights;
- provider entitlements;
- final `.pack` publication.

### 2.3 RBCE-02 remains projection/runtime authority

RBCE-04 may preview:

- sprite anchors;
- draw offsets;
- tile dimensions;
- animation frames;
- authored hitbox/hurtbox overlay references;
- projection and pixel-grid fit.

It does not decide collision outcomes. Hitbox/hurtbox editing is limited to presentation/geometry descriptors and governed references consumed by RBCE-02/GPR.

## 3. Workbench modes

RBCE-04 v1 defines six creator modes.

### `asset:intake`

Evidence-aware intake over supplied/catalogued sources.

Shows:

- source identity;
- checksum;
- license evidence;
- ingest/use/transform/substitute/redistribute permission states;
- MAI-06 adapter/import status where applicable;
- preserved unsupported metadata;
- MAI-07 eligibility/resolution state.

No network acquisition, scraping, purchase or provider authentication occurs.

### `asset:pixel-edit`

Bounded pixel editor for:

- user-authored original assets; or
- derivatives whose source evidence explicitly permits transform.

Required tools:

- pencil;
- eraser;
- fill;
- line;
- rectangle;
- selection/move;
- copy/paste within the workbench document;
- color replace;
- palette-index selection;
- zoom and pixel grid;
- optional symmetry preview.

The editor uses deterministic integer-pixel operations. Free-form filters, generative transforms and arbitrary plug-ins are not required in v1.

### `asset:sprite`

Sprite/sheet/atlas preparation:

- grid slicing;
- explicit rectangle slicing;
- frame naming;
- frame reorder;
- anchor/origin;
- draw offset;
- facing/mirroring metadata;
- sheet/atlas preview;
- transparent trim/crop;
- nearest-neighbor scale where permitted.

### `asset:animation`

Animation authoring:

- named animation groups;
- ordered frame references;
- per-frame duration;
- loop / once / ping-pong presentation modes;
- preview speed;
- onion-skin for editable originals;
- state-label mapping for later RBCE-02 binding.

Animation presentation does not create gameplay timing authority.

### `asset:tiles`

Tile preparation:

- fixed-grid extraction;
- explicit tile selection;
- tileset organization;
- tile labels/tags;
- visual terrain grouping;
- autotile/connectivity preview where MAI-04 data already exists;
- tile animation frame grouping;
- collision/interaction overlay preview as descriptive references only.

The workbench must not infer walkability, damage, doors, cover, or triggers from art.

### `asset:palette`

Palette and retro-constraint preparation:

- create/edit palette for original assets;
- inspect unique colors;
- map colors to a target palette;
- preview palette reduction;
- preview 8-bit-inspired / 16-bit-inspired / custom constraint fit;
- show warnings for dimensions, color count, frame complexity and other asset-local limits supplied by RBCE-02 profiles.

No palette reduction is committed without an explicit creator action and transform permission.

## 4. Source classes and workbench roles

RBCE-04 does not introduce new canonical MAI asset kinds. It presents Retrobit-oriented **workbench roles** over MAI records.

Initial roles:

- `retro-role:pixel-canvas`
- `retro-role:sprite-sheet`
- `retro-role:sprite-atlas`
- `retro-role:animated-sprite`
- `retro-role:tile-sheet`
- `retro-role:tileset`
- `retro-role:background-layer`
- `retro-role:foreground-layer`
- `retro-role:ui-sprite`
- `retro-role:effect-sprite`
- `retro-role:object-sprite`

Each role must retain its MAI asset/source/package references.

## 5. Original asset creation

Creators may create a blank local pixel document.

A new original asset requires:

- stable asset draft ID;
- declared user-authored-original origin;
- canvas width/height;
- transparent/opaque background policy;
- optional initial palette;
- creation timestamp/editor metadata excluded from deterministic semantic fingerprints unless required by the governing owner;
- provenance statement marking it as creator-authored rather than imported.

Creating an original does not grant the workbench authority to declare downstream redistribution policy beyond the creator's explicit rights declaration.

## 6. Imported asset intake

Imported/supplied assets enter through MAI evidence.

RBCE-04 must display and preserve:

- source reference;
- SHA-256;
- license evidence class/reference;
- independent permission states;
- import adapter/version;
- import diagnostics;
- unsupported metadata envelope;
- package/source lineage.

RBCE-04 never infers permission from filename, source URL, provider identity or visible availability.

## 7. Permission gates

Every persisted transform/derived artifact uses explicit permission gates.

### No transform required

Operations that only create workbench metadata may proceed when the source may be used for authoring, provided they do not alter the source bytes.

Examples:

- naming frames;
- creating non-destructive slice rectangles;
- previewing anchors;
- adding local labels.

### Transform required

Operations producing altered image bytes or a durable derived image require `transform: granted`.

Examples:

- crop that emits new bytes;
- trim-transparent export;
- palette remap;
- resize;
- pixel painting on imported art;
- compositing;
- atlas repacking;
- destructive color replacement.

If transform is denied or unknown:

- the source remains visible;
- non-destructive preview may be allowed;
- the persistent derivative action is blocked;
- the diagnostic remains visible;
- the workbench does not silently copy/flatten a modified result.

### Use / redistribution remain separate

`transform: granted` does not imply:

- `useInExperience: granted`;
- `redistribute: granted`;
- `substitute: granted`.

The handoff/readiness UI must keep these states separate.

## 8. Non-destructive document model

Imported originals are immutable evidence.

A workbench document stores:

- source asset reference;
- optional parent derivative reference;
- ordered transform intents;
- frame/slice metadata;
- layer/frame working state for original/transform-permitted assets;
- palette references;
- animation definitions;
- deterministic normalized metadata;
- diagnostics.

Undo/redo changes the authoring document, not the immutable source evidence.

## 9. Pixel editor document

The v1 pixel editor is intentionally bounded.

Required editable primitives:

- raster canvas;
- integer pixel coordinates;
- indexed or RGBA color values;
- frame stack;
- simple visual layers per frame;
- visibility/lock for working layers;
- deterministic flatten preview;
- selection region;
- palette reference.

The workbench does not require:

- arbitrary shader graphs;
- vector illustration;
- Photoshop plug-in compatibility;
- unrestricted scripting;
- destructive edit of the preserved source file.

## 10. Sprite slicing

Supported slicing modes:

- `slice:grid`
- `slice:explicit-rects`

Grid slicing declares:

- origin;
- frame width/height;
- row/column count or bounded extent;
- spacing;
- margin;
- deterministic reading order.

Explicit slicing stores stable frame IDs and rectangles.

Automatic opaque-bound detection may be offered as a proposal, but creator acceptance writes explicit rectangles. Runtime behavior never depends on re-running image-analysis heuristics.

## 11. Frames and anchors

Every frame may define:

- frame ID;
- source rectangle;
- anchor/origin;
- draw offset;
- optional facing hint;
- optional descriptive geometry reference;
- optional palette variant reference.

Anchor/offset metadata is presentation data and must normalize independently of editor zoom.

## 12. Animation groups

An animation group defines:

- animation ID;
- ordered frame IDs;
- per-frame or default duration;
- loop mode;
- optional semantic state label;
- optional facing variant label.

Allowed loop modes:

- `loop`
- `once`
- `ping-pong`
- `hold-last`

Frame duration is presentation timing unless a governed GPR/RBCE-02 contract exposes a semantic event boundary.

## 13. Tile extraction and visual terrain metadata

Tiles are extracted using explicit dimensions/rectangles and receive stable tile IDs.

The workbench may author:

- tile tags;
- visual terrain group;
- variant group;
- animation group;
- edge/connectivity metadata compatible with MAI-04;
- decorative/foreground/background role.

It may not infer or author gameplay consequences such as walkability, damage, cover, doors or trigger effects merely from tile appearance.

## 14. Palette model

A palette contains:

- palette ID;
- ordered swatches;
- optional transparent index;
- labels;
- source/derivation evidence;
- optional RBCE-02 constraint-profile association.

Palette remapping must be deterministic and explicit.

For constrained profiles, the workbench may show:

- current unique-color count;
- target/limit;
- colors outside the selected palette;
- preview mapping;
- blocking/advisory status supplied by profile policy.

No automatic profile conversion silently modifies source or gameplay.

## 15. Retro constraint analysis

RBCE-04 consumes RBCE-02 constraint profiles.

Asset-local checks may include:

- width/height;
- frame dimensions;
- color count;
- palette compatibility;
- frame count;
- animation complexity;
- tile dimensions;
- atlas dimensions;
- alpha/transparency policy.

Scene-level constraints such as total simultaneously visible sprites remain RBCE-02/Studio validation and are not falsely certified by the asset workbench.

## 16. Atlas/sheet generation

The workbench may generate a deterministic derived atlas/sheet when transform and downstream use permissions allow.

Layout policy must be explicit and deterministic, for example:

- stable input frame ordering;
- fixed padding;
- fixed maximum dimensions;
- deterministic row packing for v1.

The generated image and metadata carry:

- parent asset references;
- operation list;
- checksum;
- transform permission evidence;
- normalized frame mapping;
- derivation receipt.

RBCE-04 does not require optimal bin packing in v1.

## 17. Handoff to MAI and Studio

Accepted workbench output is a **handoff**, not publication.

Handoff may include:

- MAI-compatible derived asset record proposal;
- preserved source/provenance references;
- sprite frame/atlas metadata;
- tileset metadata;
- animation presentation metadata;
- palette metadata;
- RBCE-02 presentation binding hints;
- constraint-analysis result;
- diagnostics.

RBCE-03 consumes accepted asset references in its palette/Inspector.

Final `.pack` assembly/distribution remains RBCE-07.

## 18. Validation states

RBCE-04 validation uses four severities:

- `blocking`
- `needs-attention`
- `advisory`
- `information`

Representative failure codes:

- `source-evidence-missing`
- `source-checksum-missing`
- `license-evidence-unresolved`
- `use-permission-denied`
- `use-permission-unknown`
- `transform-permission-denied`
- `transform-permission-unknown`
- `redistribution-permission-denied`
- `redistribution-permission-unknown`
- `import-adapter-unresolved`
- `unsupported-metadata-discard-forbidden`
- `invalid-slice-grid`
- `overlapping-explicit-frame`
- `frame-reference-unresolved`
- `animation-frame-unresolved`
- `invalid-anchor`
- `invalid-palette`
- `constraint-profile-exceeded`
- `derived-lineage-missing`
- `nondeterministic-derivative-layout`
- `handoff-incomplete`

Diagnostics sort deterministically by code, semantic path and stable reference.

## 19. Accessibility

Required workbench accessibility:

- keyboard operation for all essential tools;
- numeric coordinate/rectangle editing as an alternative to drag;
- zoom independent of source pixels;
- screen-reader labels for tools, frames, layers and palette swatches;
- non-color-only validation;
- high-contrast UI;
- reduced-motion previews;
- animation pause;
- frame/tile lists as non-canvas alternatives;
- accessible palette values using text/RGB/hex representation;
- focus preservation between canvas, timeline and Inspector.

The workbench canvas may be visual, but required metadata authoring must remain possible without precision pointer use.

## 20. Offline/local-first behavior

Normal RBCE-04 authoring is local-first and provider-off.

The workbench does not require:

- cloud storage;
- external AI;
- provider login;
- marketplace access;
- network asset search.

Optional AI may propose slicing, tags, palette mappings or accessibility descriptions, but deterministic validation and manual editing remain complete without AI.

## 21. Four-Engine asset proof

RBCE-04 is design-complete when its contract can prepare the original/right-cleared Four-Engine Test Chamber asset set without external specialist software.

The proof must cover:

1. create one original player pixel sprite locally;
2. intake one permitted sprite sheet with explicit provenance;
3. slice that sheet into stable frames;
4. author at least two animation groups;
5. set and preview an anchor/draw offset;
6. intake/extract a terrain tile sheet into stable tile IDs;
7. assign visual terrain tags without creating collision/gameplay truth;
8. create or remap a small palette and preview an inspired constraint profile;
9. block a derivative transform when transform permission is unknown/denied;
10. preserve a visibly unresolved/missing optional asset and allow an approved placeholder only through MAI evidence;
11. generate one deterministic atlas/sheet derivative with lineage;
12. hand accepted asset references to RBCE-03 without canonical owner mutation;
13. recover workbench draft state after interruption;
14. perform the workflow provider-off with AI disabled.

## 22. Machine contract identifiers

RBCE-04 machine-readable design artifacts use:

- schema ID: `RBCE04.ASSET_WORKBENCH.v1`
- semantic schema version: `1.0.0`
- default UI skin: `retrobit-classic-arcade`
- output boundary: `mai-handoff`
- publication authority: none

## 23. Explicit non-goals

RBCE-04 does not:

- become the canonical MAI schema;
- download/scrape/purchase assets;
- authenticate to asset providers;
- infer licenses or permissions;
- implement a marketplace;
- emulate NES/SNES graphics hardware;
- implement unrestricted image filters/plugins/scripts;
- create gameplay collision from pixels;
- create World/Scene/Combat truth;
- publish final `.pack` files;
- replace RBCE-03 Studio;
- define RBCE-05 Gameplay Parts.

## 24. Activation boundary

This is a durable content/design contract only.

Product implementation begins only when OPS3 explicitly selects and authorizes RBCE-04 or equivalent governed implementation work. PCV-03F and other live selectors are unaffected.
