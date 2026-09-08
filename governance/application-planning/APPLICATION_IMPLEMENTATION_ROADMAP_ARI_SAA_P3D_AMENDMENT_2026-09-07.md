# Application Implementation Roadmap — ARI / SAA / P3D Planning Amendment — 2026-09-07

**Status:** OWNER-APPROVED PLANNING AMENDMENT  
**Owner and final authority:** John Brandon Turner  
**Runtime effect:** none; VTI-10 remains the currently selected/in-progress product work under `CURRENT_WORK_POINTER.json`.  
**Implementation authority created by this amendment:** none.

## Owner decision preserved

Multiversal must make massive practical use of assets a user legitimately possesses or that Multiversal provides/generates, rather than confining those resources to the subsystem where they first entered. The same governed resource library must support imported packs, native assets, generated pixel assets, maps/tilesets, audio and future derivative families.

Two programs are added to the future critical path:

- **ARI — Asset Resource Ingestion & Reuse** after SGC-08 and before MIB-16.
- **SAA — Sequential Art Authoring** after SMB-09 and before SMB-10.

One future project is recorded without critical-path activation:

- **P3D — Physical 3D & Miniature Pipeline**, owner-approved but explicitly deferred, with no implementation authority and no automatic activation.

## Corrected effective forward order

The effective forward dependency order is amended to:

`VTI-10..12 → SGC-01..08 → ARI-01..22 → MIB-16 → MIB-17 → MIB-18 → SMB-01 → SMB-02 → SMB-03 → SMB-04 → SMB-05 → SMB-06 → SMB-07 → SMB-08 → SMB-09 → SAA-01..20 → SMB-10 → SMB-11 → SMB-12 → SMB-13 → SMB-14 → SMB-15 → SMB-16 → BRP-01..11 → SMB-17 → SMB-18`

Completed predecessors remain completed; this amendment does not reopen MAI, AAI, CAPP/PPIA, ISE, SSA, WCI, KFR, ODL, SCL, MAL, ECI or ALP.

PAPT remains an owner-approved parallel studio/tooling track, not an automatic critical-path program. Its future generated outputs must publish through ARI once ARI's shared resource/provenance foundations exist.

P3D remains outside the automatic critical path even after its readiness prerequisites are satisfied. A later owner decision and governed start are mandatory.

## ARI insertion contract

### Why ARI is inserted after SGC

SGC is the source/product coverage closure gate and must first classify retained asset/import/creator requirements against their exact owning systems. SGC-06 and SGC-08 therefore include ARI/SAA/P3D disposition routes so the newly approved functions cannot disappear merely because their implementation programs occur later.

ARI then builds the common ingestion/reuse layer before MIB-16. This allows MIB-16 diagnostics/provenance/dependency/search surfaces to inspect the actual universal resource library, and MIB-18 can include ARI in backbone integration/readiness rather than requiring a post-MIB retrofit.

### ARI does not replace existing owners

- MAI remains visual/map semantic authority.
- AAI remains audio source/cue/soundscape/playback/provider authority.
- CAPP/PAPT remain renderer/appearance/production-art authorities.
- Scene/World/Character/Inventory/Asset owners remain canonical live-state authorities.
- D29/publishing/provenance and rights controls remain publication/canon/commercial authorities.

ARI owns reusable resource identity/bytes-or-reference state, derivative lineage, bulk ingestion, catalog/search/lazy retrieval, rights-use capability projection, relink/recovery and cross-system resource selection.

## SAA insertion contract

SAA is inserted after SMB-09 so it has mature first-party Campaign/content material and after ARI has already been integrated through the resumed MIB/early-SMB path. SAA runs before SMB-10 so the later “Full Player / GM / Creator Product UX” tranche integrates an actual working comic-authoring subsystem rather than burying a new editor engine inside one already-large UX tranche.

SAA-18 produces a comic-project packaging/dependency contract. SMB-11 remains the owner of controlled creator interchange/sharing and consumes that contract instead of SAA creating public-sharing or marketplace authority.

SAA must be able to consume:

- user-owned/imported resources allowed by ARI rights capabilities;
- native Multiversal assets;
- CAPP/PAPT-generated Character/creature/item/environment/tile/sprite derivatives;
- MAI maps/tilesets and Scene-derived backgrounds;
- props/equipment/icons/effects;
- optional AAI cues for digital-comic presentation.

Static comic export and digital audio-enhanced presentation remain separate capabilities.

## PAPT integration amendment

PAPT-01 and PAPT-02 may continue to define pixel style/palette foundations independently when separately selected. PAPT-03 and later work must not create a competing resource/provenance library after ARI exists.

The intended relationship is:

- PAPT owns how governed pixel assets are generated/assembled/reviewed;
- ARI owns how generated outputs are registered, stored/referenced, indexed, discovered, reused and related as derivatives;
- SAA consumes those ARI-registered outputs without copying them into a private comic-only asset store.

PAPT's historical recovery text naming an old currently selected tranche is not runtime authority; current work remains controlled exclusively by the live pointer/index.

## P3D future-project contract

P3D is recorded now to protect renderer-neutral architecture. The canonical direction is:

`Character / creature / asset semantic truth → renderer-neutral appearance snapshot → renderer`

Pixel and 3D representations are sibling renderers. A detailed miniature should not primarily infer anatomy from a low-resolution pixel sprite when governed appearance/species/form/equipment semantics already exist.

P3D will eventually use composable atomic parts plus parametric morphing, topology-family eligibility, anchors/rigs/poses and print-safety validation. It plans both `physical-pixel-v1` and `physical-detailed-v1` outputs.

Readiness prerequisites normally include ARI-22, mature PAPT/CAPP renderer semantics and creator-package/provenance contracts where interchange is required. None of those prerequisites automatically activates P3D.

## Tranche-duration control

ARI, SAA and the future P3D tranche map are deliberately split into small acceptance-sized units. Each is designed around a **24-minute-or-less bounded execution target under a healthy governed environment**. If a tranche cannot credibly meet that target before governed start, its acceptance surface is split into smaller tranches rather than letting one owner `Continue` expand into an oversized package. Required final evidence is never weakened to hit the target.

## Durable discovery

Canonical planning artifacts added by this amendment:

- `asset-resource-ingestion-reuse/ARI_ASSET_RESOURCE_INGESTION_REUSE_PROGRAM.md`
- `asset-resource-ingestion-reuse/ARI_PROGRAM_BACKLOG.json`
- `sequential-art-authoring/SAA_SEQUENTIAL_ART_AUTHORING_PROGRAM.md`
- `sequential-art-authoring/SAA_PROGRAM_BACKLOG.json`
- `future-projects/P3D_PHYSICAL_3D_MINIATURE_PIPELINE.md`
- `future-projects/DEFERRED_FUTURE_PROJECTS_REGISTRY.json`

A control-plane regression test must keep these files, the corrected forward order, SGC successor route, PAPT/ARI boundary and SMB SAA insertion from being silently dropped by later roadmap edits.

## Authority and non-activation rules

- This planning amendment does not create product/application implementation authority.
- VTI-10 remains the live selected/in-progress item; this branch must not modify its pointer/checkpoint/acceptance authority.
- ARI cannot start before SGC-08 reaches `completed_verified` and a separate governed start selects ARI-01.
- SAA cannot start before its declared upstream completion conditions and a separate governed start selects SAA-01.
- P3D is deferred and has no automatic successor relationship.
- No provider credential, scraping/ripping/content extraction, paid service, external generation spend, printing/manufacturing purchase, tester distribution, release/deployment, public marketplace, canon promotion or commercial publication is authorized here.
- No later roadmap edit may silently drop ARI, SAA or the P3D deferred-future record; removal/reordering requires an explicit later owner decision and canonical amendment.