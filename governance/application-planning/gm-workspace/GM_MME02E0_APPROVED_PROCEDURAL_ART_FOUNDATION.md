# GM-MME-02E0 — Approved Shared Procedural-Art Foundation

**Owner approved:** 2026-11-24. Owner supplied four references and approved the source-grounded proposal for a shared procedural-art/field foundation: Game Genius Lab procedural biome generation; Catlike Coding Unity Basics; Scratchapixel procedural texturing; Inigo Quílez graphics articles. This is **owner-approved scope**, not an assertion that every article in the Quílez directory was accessible.
**OPS5 scope:** `gm-workspace / GM-00` on-demand standalone HTML increments only, `implementation_authority: false`. `operations/CURRENT.json` on protected main remains sole selector. Draft registration [PR #2049](https://github.com/cybalicistjt-stack/multiversal-aioc/pull/2049).
**Current baseline:** Owner-supplied UHT-07 `Multiversal_Consolidated_Playtest_UHT07_MME02D2.html`. Reuse original MMHT map source: source map document/geometry IDs/revisions and 5ft grid/Fog/Combat/Scene/Inventory source owners remain unchanged.

## Accepted architectural decision

Instead of continuing indiscriminate per-map screen filters, extend the native Map Maker with one deterministic procedural field/material system. The **source owns geometry, levels, biomes and authored water**. A bounded, purely illustrated field samples authored coordinates to produce surface character and rich variation. Do not move coastlines, add canonical terrain/loot or shift existing map anchors, and do not hide Player-sensitive data with CSS only.

Proposed compositing sequence:
1. Input: authored map/floor/material/source version, seeded design parameters.
2. Multi-scale noise fields (value/simplex-compatible), fractional Brownian motion, bounded domain warping; elevation/moisture/climate masks only where actual source data exists; source geometry controls clipping.
3. Derived distance/edge masks, material coordinate transforms, biome-aware appearance rules; verify aliasing across zoom.
4. Art atlas and later editable scatter: original/properly licensed objects with author and provenance, not random dotted noise.
5. Consistent visual lighting/depth and style profile separate from true rules light/LOS.
6. Artwork drawn under/alongside native map art and before VTT tokens/FOG/5-ft anchors; editable source data stays untouched.

**Reference-specific limitations:** Game Genius Lab's tutorial is a high-level recipe, not a ready integration contract; Catlike Coding's Basics tutorials use older Unity revisions so API/performance claims must be reverified for Unity 6.3 LTS; Scratchapixel illustrates texture-coordinate and filtering principles, not finished Multiversal assets; the Quílez directory was partially access-blocked when assessed, so no falsely attributed specific implementation claim.

## Revised delivery order

- **MME-02D3:** measured multi-scale renderer/visual audit with the original four/six map categories and check at realistic zoom; retain all prior features, produce a reusable quality benchmark and forward compatible field integration contract.
- **MME-02E0-A (new):** prototype deterministic source-space multi-octave noise/fBm, bounded domain warp, material masks and seed/density/intensity UI. Render art on original editable maps only, reversible, map-id and VTT invariants, opt-in. Include pixel/zoom measurement and robust cache/no-data limits.
- **MME-02E0-B (optional):** source-aware biome climate/elevation inputs (not synthetic claim where source lacks data), domain-aware material edge bands, coast/river/cave topology and performance refinements.
- **MME-02E1–E4:** richer materials, original/licensed illustrated assets, intentional object clustering, architecture/roof/wall/room composition.
- **MME-02F1/F2:** structural and environmental shadows and atmosphere independent from rules lighting.
- **MME-02G/H:** genre art direction, cartographic labeling, anti-aliasing, high-quality export, quality and performance acceptance.
- **MME-07/08 remains:** GM encounters/NPCs/hazards/loot/events/triggers edited directly on original artwork using their actual source owner records and explicit review.

## Quality acceptance

Do not claim parity with Inkarnate, Dungeondraft or Dungeon Alchemist based on pixel-change counts. Compare actual saved map screenshots at 100%, 200% and export size against sourced reference categories. Assess material richness, object/art detail, spatial hierarchy, art direction, clutter density, editability, and naturalistic transitions. Performance, source/restoration, GM-only/projections and VTT-regression receipts are required each cycle. Some maps have sparse authored environmental detail: a field shader alone cannot achieve parity. No copyrighted competitor image assets copied.

**Status:** approved roadmap, implementation for standalone review as explicitly requested by owner; no production authority or main-branch merge.
