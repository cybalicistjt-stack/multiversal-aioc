# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01 COMPLETED_VERIFIED; MAI-02 SELECTED_NOT_STARTED  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-01 — Ecosystem, Format, License & Authority Survey  
**Current item:** MAI-02 — Canonical Map Asset, Placeable & Package Schema  
**Implementation branch:** none  
**Implementation authority:** none until future owner Continue governed-starts MAI-02  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

**MAI-01** is `completed_verified` on application PR **#312**. Its exact validated head `a743129605e60c19a384c6ab8dc0f8dec1a7f4ee` passed application Repository Health plus governed self-hosted Linux/Windows Validation Core and deterministic cross-platform comparison, then merged as `82dc4c8838876e66361b942f0243a63f3b1f20d8`.

Strict MAI order selects **MAI-02** only. MAI-02 has no implementation branch and no implementation authority until a future owner **Continue** freshly verifies canonical AIOC/application heads, re-reads the MAI-01 survey evidence and this program/backlog, resolves the exact schema/authority evidence set, and governed-starts MAI-02.

## MAI-01 completed survey contract

MAI-01 established a source/ecosystem/authority foundation without implementing MAI-02 schema/importer mechanics.

Verified survey evidence:

- retained `Now this.zip` SHA-256 `2a5eae712f483d1fb33ff9fb0087e96c4eb8b71b287cc707c196a4c17a2f78f4`;
- RSR-01 retained-media boundary of 12 unique embedded media objects, 11 substantive;
- 14 provider-neutral visual/map source classes;
- 10 explicit license-evidence classes;
- 4 current authoritative ecosystem/license references used as examples/evidence only: Tiled, LDtk, Foundry Scene JSON and Creative Commons license conditions;
- 6 authority-crosswalk concerns;
- 5 explicit incomplete-pack outcomes;
- canonical vendor/editor: none;
- license permission inference: forbidden;
- silent unsupported-metadata discard: forbidden;
- silent missing-asset invention: forbidden;
- artwork/maps/coordinates becoming World/combat truth: forbidden.

Exact completion evidence:

- application PR: `312`;
- validated head: `a743129605e60c19a384c6ab8dc0f8dec1a7f4ee`;
- Repository Health run/job: `32913613755 / 98012520566`;
- Validation Core run: `32913614016`;
- Linux job: `98012522361` — PASS;
- Windows job: `98012522432` — PASS;
- deterministic comparison job: `98013063310` — PASS;
- comparison artifact: `9587487213`;
- deterministic receipt: `215044e4d1e2746d6aa01e7ba3977a56e63f3330aac9a838f5095ff112de90cc`;
- application merge: `82dc4c8838876e66361b942f0243a63f3b1f20d8`;
- repair cycles: `0`.

## Critical incomplete-pack rule

No tileset or asset pack is expected to contain every semantic object Multiversal can represent. Semantic scene requirements remain separate from selected art. Resolution may use an exact compatible asset, a compatible permitted asset from another installed pack, GM/user choice, an explicitly approved placeholder, or a visibly unresolved state. Missing or incompatible art is never silently invented or treated as semantic truth.

## Persistent authority rules

- No creator/vendor/editor is the canonical Multiversal map model.
- Artwork, map coordinates and camera/view state are projection/presentation resources, not World or combat identity truth.
- MIB-11/D18 retains World/location identity authority.
- Existing Scene/tabletop and Combat/Exploration owners retain runtime truth.
- Hidden/GM-only layers remain permission-scoped.
- License/source/provenance metadata is preserved.
- Permission is evidence-driven and conservative; silence is not permission.
- Manual GM/user asset assignment remains first-class.
- Partial structured imports must surface unsupported/lost semantics rather than silently discarding them.

## MAI-02 selection contract

MAI-02 may eventually define the vendor-neutral canonical MapAsset, Tile, TerrainSet, ObjectAsset, Module, Battlemap, Layer, Placeable and package/source model, including stable identity, dimensions, transforms, anchors, grid metadata, elevation, variants, animation, dependencies and source/license provenance.

At selection time only, MAI-02 must preserve these requirements:

- consume MAI-01 without making Tiled, LDtk, Foundry, UVTT-class or any other ecosystem canonical;
- preserve source/checksum/license/evidence/import lineage and unresolved permissions;
- keep semantic requirements distinct from chosen visual assets;
- provide a future explicit path for unsupported source metadata rather than silent loss;
- treat geometry/coordinates as map-asset metadata, not World/combat identity truth;
- do not implement MAI-03 coordinate/projection mechanics, MAI-04 autotile grammar, MAI-05 geometry ownership, MAI-06 adapters or later resolver/workbench/runtime work.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `selected_not_started`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `planned`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `planned`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `planned`
6. **MAI-06 — Universal Import Adapter Framework** — `planned`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `planned`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `planned`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Downstream relationship

AAI follows MAI so provider-neutral asset/provenance patterns can be reused for audio without merging visual and audio ownership. ISE later consumes completed MAI + AAI for native tabletop/canvas experience.

## Invariants

- MAI-01 has no further implementation authority.
- MAI-02 is selection-only until a future owner Continue governed-starts it.
- MAI-03+ have no implementation authority.
- Missing art never blocks theater-of-the-mind/non-map play.
- No pack is assumed complete.
- Semantic requirement and chosen visual asset remain separable.
- No real-money commerce, tester distribution, release/deployment or provider/payment activation is authorized.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.
