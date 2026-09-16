# Application Implementation Roadmap — MCS PDCP Reduction Amendment — 2026-09-16

## Status

Owner-approved planning amendment under PDCP. No implementation authority is granted. `operations/CURRENT.json` remains the only live product selector.

## Decision

MCS is reduced from the historical 21-tranche plan to 12 implementation/proof tranches after complete intra-family and cross-family/shared-owner overlap review.

Effective strict order:

`MCS-01 → MCS-03 → MCS-05 → MCS-07 → MCS-08 → MCS-10 → MCS-13 → MCS-14 → MCS-15 → MCS-18 → MCS-19 → MCS-21`

Historical baseline remains preserved in `PDCP_MCS_REDUCTION_RECEIPT.json`.

## Fold summary

- `MCS-01+02 → MCS-01` — workspace/document + large-map canvas/render lifecycle.
- `MCS-03+04 → MCS-03` — selection/transform/snapping + precision vector/path editing.
- `MCS-05+06 → MCS-05` — raster/mask/texture + symbols/stamps/scatter/components.
- `MCS-07+17 → MCS-07` — typography/labels/legends + styles/themes/templates/layout.
- `MCS-08+09 → MCS-08` — terrain/elevation + water/routes/borders/networks.
- `MCS-10+11+12 → MCS-10` — one map-specific procedural proposal workbench over PCA-owned generator substrate.
- `MCS-13` — settlement/city cartography retained.
- `MCS-14+16 → MCS-14` — dungeon/interior/multi-level + isometric/deck/section projection.
- `MCS-15` — tactical-scene authoring retained.
- `MCS-18` — semantic binding/world sync retained.
- `MCS-19+20 → MCS-19` — map interchange/atlas + map-specific review/version/publishing adapters.
- `MCS-21` — golden proof retained.

## Cross-family/shared-owner reconciliation

MCS does not implement generic procedural graphs, simulation/solvers, style-generation, provenance/version/review infrastructure, live scene runtime, canonical spatial law, built-environment truth or runtime combat/visibility consequences.

Those remain respectively with PCA-02/PCA-03, PCA-12/Packet-08, PCA-09/ARI, ARI/PCA/Packet-07, ISE/Scene/Tabletop, SSA/World/reduced MSLR, Settlement/reduced MBES, and Combat/Visibility/Exploration/reduced MSWI.

MCS retains only cartography-domain editing, map-specific generator packs, presentation/layout, geographic/urban/interior/tactical authoring, semantic-binding UX, map interchange/atlas adapters and proof.

## DAG impact

No `ROADMAP_DEPENDENCY_GRAPH.json` mutation is required. `MCS-21` survives with equivalent-or-stronger golden semantics and remains the MSLR start requirement plus relevant specialist golden proof. `MCS-01` remains the family start.

## PDCP cumulative effect

Historical in-scope baseline: **208** tranches.  
Effective count after MCS: **105** tranches.  
Standalone future tranches removed: **103**.  
Family receipts complete: **10 / 10**.

MCS is the final family reduction. After this amendment is published, PDCP proceeds only to final whole-project reconciliation and closeout.
