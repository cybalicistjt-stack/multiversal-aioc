# Multiversal Pixel Asset Production Toolkit Program

**Program ID:** PAPT  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED PARALLEL STUDIO TOOLING; NOT STARTED  
**Owner/final authority:** John Brandon Turner  
**Approved:** 2026-08-22  
**Primary repository:** `cybalicistjt-stack/multiversal-aioc`

## Purpose

PAPT turns Multiversal's completed Character Appearance Production Preparation (CAPP) pixel-art architecture into a broader governed studio asset-production toolchain. The program exists to make large-volume pixel-based production art feasible without creating a second visual system, weakening canonical source authority, hiding AI-assisted/generated provenance, or forcing manual art production to scale linearly with Multiversal content volume.

PAPT is additive. It does not replace CAPP, PPIA-06, Species/Form authority, Asset/equipment authority, creature/item/world source registries, the Multiversal application visual-language authority, or NCG corporate IP/provenance controls.

## Visual doctrine

1. **Pixel art is the current production-content art language.** Characters, creatures, items, equipment, props, environmental assets, map/tile assets, portraits/tokens and related game-facing imagery should use governed pixel-art production standards unless a later owner-approved art direction supersedes this rule.
2. **The existing Multiversal UI/design language remains the cross-surface brand authority.** Pixel content sits inside the same design-token, hierarchy, spacing, state, accessibility and interaction language used by the Multiversal application. PAPT does not make every corporate/media surface look like a low-resolution retro UI.
3. **Typography may use higher-definition treatment.** Brand/editorial typography may be more refined than the pixel asset language as long as it remains compatible with Multiversal hierarchy, accessibility and brand-system decisions.
4. **Generation is disclosed and provenance-bound.** Generated or AI-assisted production assets may be used, but the method, source data, model/tool where applicable, human edits, version and rights/canon state must be retained. No false handcrafted/no-AI claim is permitted.
5. **Canonical data drives generation.** PAPT should compile from governed semantic inputs and source registries rather than relying on unconstrained natural-language prompting as the production source of truth.
6. **Human art remains first-class.** Human-created source assets, palettes, templates, premium illustrations or corrections can enter the same pipeline and may become higher-authority or anchor assets through explicit review.
7. **Missing renderer coverage never invalidates canonical content.** The asset system renders what it can, diagnoses unsupported coverage and falls back explicitly; it may not invent mechanics, anatomy, ownership, canon or hidden information.

## Upstream authorities

PAPT inherits, without reopening them:

- `CAPP-03` Pixel-Art Asset Production Standard — `completed_verified`.
- `CAPP-04` Asset Manifest and Coverage Analyzer Contract — `completed_verified`.
- `CAPP-05` Deterministic Appearance Compiler / Reference Engine — `completed_verified`.
- `CAPP-06` Wardrobe and Equipment-Fit Compatibility Catalog — `completed_verified`.
- `CAPP-08` Portrait, Token and Export Production Contract — `completed_verified`.
- `CAPP-09` Appearance Versioning and Migration Engine Contract — `completed_verified`.
- `CAPP-10` Accessibility Description Grammar — `completed_verified`.
- `CAPP-11` generated QA/coverage corpus and `CAPP-12` integrated handoff — `completed_verified`.
- PPIA-06 Character Appearance Creator architecture.
- PPIA-05 Species/Form/current-body/persistent/live biology authority.
- PPIA-03 actual Asset ownership/equipment/install-state authority.
- Current Multiversal visual-language/design-token/accessibility authority in the application Development Bible and later owner-approved design standards.
- Domain-specific canonical registries for creatures, items, ingredients, environments, maps, worlds, equipment and other content families as those domains provide source inputs.
- NCG rights/provenance and public-claim controls for commercial/media use.

## Non-activation boundary

Planning or repository-side reference tooling in PAPT does not itself authorize application runtime integration, public release, marketing publication, external asset generation spending, production credentials, customer data use, merchandising, licensing, canon promotion, or replacement of existing validated application assets.

## Work program

### PAPT-01 — Multiversal Pixel Style Authority

Extract one implementation-grade pixel production authority from completed CAPP pixel contracts plus current Multiversal visual-language rules. Define canvas classes, density families, semantic bands, outline/shading behavior, palette-role constraints, transparency, safe areas, view conventions, anti-aliasing policy, scaling/export behavior, UI/content boundaries and typography separation.

**Parallelism:** first foundation item; no downstream asset forge should lock a separate style before this closes.

### PAPT-02 — Palette, Shading & Outline Compiler

Build deterministic palette ramps, role-based color mapping, palette validation/remapping, outline rules, value/contrast checks, accessibility-aware color constraints and controlled variant generation. Support biome/faction/material/status themes without letting color alone communicate required state.

**Depends on:** PAPT-01.  
**Parallel after close:** PAPT-03 may overlap late validation; asset-family forges may prototype against stable fixtures only.

### PAPT-03 — Shared Asset Metadata, Rights & Provenance Schema

Define stable asset IDs, family/type, source entity IDs, canonical semantic inputs, tool/model/method, human edits, source references, rights state, provenance class, generation seed/settings where reproducibility is possible, version lineage, replacement/supersession, canonical/concept/promotional state, commercial-use review and derived-output relationships.

Integrate with CAPP manifest/versioning contracts and NCG corporate provenance controls.

**Depends on:** PAPT-01.  
**May run in parallel with:** PAPT-02.

### PAPT-04 — Character Asset Forge

Extend the Character Appearance Customizer/CAPP semantic model into a production-facing character component forge/assembler for governed pixel assets: body/surface/face/hair/features/markings/appendages/wardrobe/equipment projection and permitted presentation layers. It must consume CAPP eligibility/constraint/fit rules and produce manifest/provenance-valid components and derivatives.

**Depends on:** PAPT-01..03 and completed CAPP.  
**Can run in parallel with:** PAPT-05..09 after shared foundations close.

### PAPT-05 — Creature Pixel Forge

Generate/assemble pixel creature assets from governed creature/species morphology, topology, surface, coloration, appendage, biome, lifecycle/form and presentation data. Support explicit unsupported/unknown source fields rather than filling source gaps as canon.

**Depends on:** PAPT-01..03 plus usable canonical creature/species source registries.  
**Parallel:** PAPT-04, 06, 07, 08, 09.

### PAPT-06 — Item, Equipment, Ingredient & Material Forge

Create governed pixel production assets for weapons, armor, tools, vehicles/components where appropriate, crops, ingredients, alchemical/cooking materials, loot/salvage components, artifacts and ordinary items from canonical item/material semantics.

**Depends on:** PAPT-01..03 plus owning domain registries.  
**Parallel:** PAPT-04, 05, 07, 08, 09.

### PAPT-07 — Pixel Icon Forge

Create standardized icons for actions, resources, conditions, tags, statuses, item categories, abilities and system references. Define silhouette/readability standards, multi-size export, disabled/unknown/pending/error variants and accessibility-safe redundant cues.

**Depends on:** PAPT-01..03 and UI semantic/state authority.  
**Parallel:** PAPT-04..06, 08, 09.

### PAPT-08 — Environment, Prop & Cozy Asset Forge

Produce governed scenery/prop asset families for interiors, furniture, facilities, crops/plants, crafting/cozy spaces, buildings, settlement/environment objects and interactables. Preserve domain ownership: an image cannot create a place, facility, item or mechanic that does not exist in source authority.

**Depends on:** PAPT-01..03 plus relevant world/facility/cozy registries.  
**Parallel:** PAPT-04..07, 09.

### PAPT-09 — Tile, Map & Marker Asset Forge

Define/generate terrain tiles, walls/floors/roads, biome sets, overlays, map markers, tactical/world-map symbols and seamless/edge compatibility rules. Integrate pixel style with the application's map/UI language without forcing typography or interface chrome into pixel resolution.

**Depends on:** PAPT-01..03 plus map/world authority.  
**Parallel:** PAPT-04..08.

### PAPT-10 — Sprite & Animation Assembler

Build deterministic sprite-sheet/animation assembly from approved layered assets and topology-specific anchor data. Cover idle/walk/basic presentation loops and extensible animation metadata without inventing action mechanics.

**Depends on:** PAPT-04 and/or PAPT-05 plus PAPT-02/03; may consume PAPT-06/08 for held/worn/context assets.

### PAPT-11 — Equipment-Fit, Layer, Anchor & Occlusion QA Tool

Generalize CAPP equipment-fit/layering diagnostics into a studio QA surface across generated characters/creatures/equipment. Detect clipping, invalid anchors, missing masks, occlusion conflicts, unsupported topology, unsafe crops and layer-order defects.

**Depends on:** PAPT-04, PAPT-06 and CAPP-06; can begin once representative fixtures exist.

### PAPT-12 — Portrait, Token & Derivative Export Factory

Automate deterministic portraits, tactical tokens, thumbnails, transparent cutouts, social/reference derivatives and approved output sizes from canonical asset assemblies with versioned derivative identity and stale-output invalidation.

**Depends on:** PAPT-04/05, PAPT-03 and CAPP-08.  
**Parallel:** PAPT-10/11/13 once source assemblies exist.

### PAPT-13 — Batch QA, Contact Sheet & Style-Lint System

Create repository-side batch validation and visual review packages: contact sheets, asset-family completeness, palette/style lint, dimensions/transparency, duplicate/similarity warnings, missing views, topology/fit coverage, provenance completeness and export validity.

**Depends on:** PAPT-01..03; incrementally consumes every asset-family forge.  
**Parallel:** may evolve continuously alongside PAPT-04..12.

### PAPT-14 — Production Queue, Regeneration & Dependency Graph

Define a studio production queue where canonical entity/version changes identify stale derivatives, affected asset families and required regeneration/review. Support batch jobs, bounded retries, deterministic seeds/settings where available and explicit manual-review states.

**Depends on:** PAPT-03 and PAPT-13 plus at least one operating forge.

### PAPT-15 — Human Review, Correction & Canon/Commercial Promotion Workflow

Define how generated, assembled, manually edited and fully human-created art move through concept → production candidate → reviewed → canonical product asset → promotional/commercial-cleared states. Preserve reviewer identity, corrections, rights/provenance evidence and rejection reasons. No generation output becomes canonical or commercially cleared merely by existing.

**Depends on:** PAPT-03 and PAPT-13; consumes NCG rights/claim controls.  
**Parallel:** may begin before all forges finish.

### PAPT-16 — Integrated Studio Pixel Asset Factory

Integrate character, creature, item, icon, environment/map, animation, QA, derivative export, regeneration and human-review systems into one versioned studio handoff. Demonstrate golden cross-family production runs with exact source/provenance traceability and no silent source-authority mutation.

**Depends on:** PAPT-04..15 as applicable; final integration gate.

## Dependency-optimized execution order

Foundation spine:

`PAPT-01 → (PAPT-02 || PAPT-03) → shared-foundation gate`

Asset-family fan-out after the shared-foundation gate:

`PAPT-04 || PAPT-05 || PAPT-06 || PAPT-07 || PAPT-08 || PAPT-09`

Downstream tools:

- `PAPT-10` after representative character/creature assets exist.
- `PAPT-11` after character + equipment fixtures exist.
- `PAPT-12` after character/creature assemblies and provenance exist.
- `PAPT-13` starts incrementally as soon as shared foundations close and expands with each forge.
- `PAPT-14` follows provenance + QA + at least one working forge.
- `PAPT-15` follows provenance + QA and may mature in parallel with later forges.
- `PAPT-16` closes only after the selected production families and downstream controls are integrated.

## Corporate/media relationship

PAPT is a Multiversal engineering/studio-tooling program governed in AIOC. NCG's corporate roadmap may schedule and commercialize outputs, but it may not redefine PAPT technical truth. NCG uses PAPT output only after the relevant rights/provenance, claim, release and franchise/canon gates pass.

## Completion standard

Planning approval is not completion. Each PAPT work item reaches `completed_verified` only with bounded repository artifacts, stable IDs, explicit upstream authority/provenance, deterministic validation appropriate to the work item, repository health/CI where applicable, completion evidence and no unauthorized runtime/public/commercial activation.

## Recovery and selection rule

PAPT is an owner-approved parallel preparation/tooling track. It does not change the selected application critical-path item, currently RSR-06 under Application Implementation Roadmap v6.27.0. Selecting or executing a PAPT tranche requires an explicit governed start; planning PAPT does not mark RSR, MSS or any other family complete, paused or superseded.