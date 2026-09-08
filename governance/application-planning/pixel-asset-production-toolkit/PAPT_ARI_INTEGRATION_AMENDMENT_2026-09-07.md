# PAPT — ARI Integration Amendment — 2026-09-07

**Status:** OWNER-APPROVED PLANNING AMENDMENT  
**Implementation authority:** none  
**Controls:** future PAPT relationship to ARI/SAA/P3D without reopening completed CAPP/PPIA contracts.

## Shared-resource decision

PAPT remains the pixel production/generation/tooling authority. ARI becomes the reusable resource-library/ingestion/catalog/derivative authority. PAPT must not create a competing persistent asset library once ARI's corresponding contracts exist.

The intended boundary is:

- **PAPT:** style authority, palette/shading, pixel component generation/assembly, sprite/animation production, fit/occlusion QA, batch QA, regeneration, human correction/review and production candidate promotion.
- **ARI:** reusable resource identity, bytes/reference state, content digest/deduplication, derivative lineage, rights-use capability projection, large-library search/indexing, cross-system selection, relink/recovery and resource registration.
- **SAA:** consumes eligible PAPT outputs through ARI for comic/sequential-art composition.
- **P3D:** later consumes renderer-neutral CAPP/PPIA/PAPT semantic appearance/product knowledge and registers 3D outputs through ARI; it does not make pixel assets canonical Character truth.

## PAPT tranche dependency clarification

- **PAPT-01** and **PAPT-02** may be separately governed before ARI because they establish pixel style and palette/shading rules rather than a shared resource store.
- **PAPT-03** keeps ownership of production-art metadata needed to reproduce/review generated assets, but after ARI-03 it must extend/map into ARI resource/provenance/derivative identity rather than defining a second cross-product library.
- **PAPT-04..12** outputs register through ARI when the needed ARI registration interfaces exist.
- **PAPT-13** may validate ARI registration/provenance completeness as part of batch QA.
- **PAPT-14** regeneration/dependency work consumes ARI derivative lineage/reverse references where applicable rather than constructing an incompatible duplicate graph.
- **PAPT-15** human review/canon/commercial promotion remains PAPT/D29/rights authority; ARI resource existence never promotes an asset.
- **PAPT-16** golden integrated studio runs must prove ARI registration for produced outputs when ARI is complete.

## Character and future-renderer invariant

Completed CAPP/PPIA renderer-neutral Character appearance authority remains unchanged. Pixel art is one renderer/product language; future P3D physical renderers are sibling projections. PAPT cannot make sprite/pixel fields mandatory canonical Character state merely because PAPT generates production art.

## Non-activation boundary

This amendment changes planning/dependency ownership only. It does not select PAPT, ARI, SAA or P3D; activate external generation services; authorize spend; promote generated assets to canon/commercial clearance; or alter the current VTI work selector.