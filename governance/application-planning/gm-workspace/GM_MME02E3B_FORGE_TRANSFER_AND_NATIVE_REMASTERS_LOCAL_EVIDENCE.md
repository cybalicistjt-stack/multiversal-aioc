# GM-MME-02E3-B — Map Forge v1.0.2 transfer audit and native ship/cavern remasters

**Owner direction:** 2026-11-24, "Continue (also this was a previous work project we did, is there anything in here worth transferring over to the current map maker?)", with uploaded `Multiversal_Map_Forge_App_v1.0.2.zip`. **Scope:** independently reviewable, source-faithful local HTML and audit in `gm-workspace / GM-00`. **Implementation authority remains false**; protected `operations/CURRENT.json`, app code, MMHT/PCV/MTLC source owners and gameplay permissions are unchanged. Review in draft [PR #2049](https://github.com/cybalicistjt-stack/multiversal-aioc/pull/2049).

## Evidence and exact artifact identity

- Map Forge user source ZIP SHA-256: `9d4c818258dfcc6948ad636f43181c59a45d61b5cc6abb3111d9b101008097d2`. Reviewed its README, separate source modules and test suite. Original `npm test`: **19/19 passed**, separately from this increment.
- **UHT-14** `Multiversal_Consolidated_Playtest_UHT14_MME02E3B.html`, **51,612,244 bytes**, SHA-256 **`f0937a1cb68bbf1bb91451b0224f68792bdedf3ce71d35b4536074e1ee0693ed`**.
- Native `Multiversal_MME02E3B_Native_Map_Maker.html`, **14,590,079 bytes**, SHA-256 `ae188b0635f2d8c48a40f8746e7c7eedada2f37f0e6eaf4272ae61469cf74f8c`; nested GM `Multiversal_GM_MME02E3B.html`, **35,475,576 bytes**, SHA-256 `b242d84e16f5376ee01a8b98e5fb7b3caf802ecbed1a60fa21be1ec6c2c1be09`.
- Owner-review ZIP `Multiversal_MME_02E3B_Map_Forge_Transfer_And_Remasters_Review_Package.zip`, **69,106,953 bytes**, SHA-256 **`116e6ad347cb806ef321894628cd80166386f680b11a879576c5d43601826ae1`**; **46 entries**, ZIP CRC/per-member SHA-256 checks passed, exact tested UHT-14 member matches the separately verified artifact. Pack contains original Forge archive/source, compare screenshots, native editable map JSON exports, source/test scripts, handoff and transfer audit; large files supplied via owner conversation, not committed to governance repo.
- Exact original UHT-13 native map source recovers byte-for-byte after removing four additive UI/source blocks and reversing one E2 registry extension; UHT Character, Downtime, Recovery and corpus payloads unchanged.

## Transfer decisions grounded in previous Map Forge source

**Transfer implemented in this local increment:**
- Original pure `source/js/extractor-core.js` functions and `source/js/file-loader.js` mobile-compatible image upload strategies, without replacing MMHT map file/editor identity.
- Art import panel with **Auto** connected components, **Grid** 4×3 or other rows×cols, and numeric **Manual** region; preview/crop and optional background cleanup. Alpha-aware branch prevents RGB-background classification from deleting content on transparency-rich sprite sheets; old opaque-image behavior retained.
- Source-aware asset registry bridge `MMHT_MME02E2.registerExternal` / `exportExternal`, separate local art-pack JSON, bounded upload/region counts. New sprites usable in existing E2 artwork placement and map copy workflow.

**Transfer not implemented:** old grid-only Map Forge editor or native `.mapforge.json` directly into Map Maker, asset bytes inside native MMHT document, complete merge of old undo/editor model, real Android physical Photos picker certification, draggable manual crop UI. Those require adapters/source-owner review. A real 4×3 existing architecture sheet produced **12/12** tiles through Grid, while Auto yielded **22 components** (oversegmentation); the preview and Grid fallback are essential, not optional decorations.

## Actual E3-B map structure

- **Kestrel Courier Main Deck:** a new native editable copy with **28 features (15 original)**; new compartments/passages and room assignments for cockpit, crew, galley, clinic, cargo and airlock. Engineering deck, structural hull and both cross-floor shaft IDs remain. Original reference unchanged; 11 small visual decorative references, no gameplay authority.
- **Brinegate Split Caverns, gallery level −1:** a new native copy with **19 features (12 original)**; redesigned Broken Gallery, added chambers, caverns and connecting tunnels. Hoist, ladder, hidden overpass and external exit references retained; internal map connection IDs bound to the new copy, external destination unchanged. Automatically open the edited floor; original and other levels unchanged. Nine small decor references.
- Both maps are **editable native geometry with real Map Maker JSON exports**, not generated promo mockups. Artwork is separate from playable physics and requires source bundle for display. Source alignment and 5-ft VTT remains inherited.

## Executed exact-output browser tests

| Scope | Pass |
| --- | ---: |
| Native Map Maker: editable ship/cave documents, feature-level source guards, cross-floor connections, extracted sprites and real art-pack transfer | **52/52** |
| Complete UHT-14 launcher → nested GM → native Map Maker + five VTTG06–10 dock panels | **15/15** |
| 390px mobile/control and stratified mounted-document sample (12 documents; 5 interior, 3 regional, 2 tactical, 2 urban), 22 categories/66 example catalog presence | **14/14** |
| **Scoped new browser tests** | **81/81** |
| Original separate Map Forge npm tests | **19/19** |

The attempted **full 45-mounted-document sweep timed out**; it is *not* counted as passed. Also unverified: 66 complete example editing flows, installed Unity and Android/Windows multi-device, real Android image picker, server D05 player disclosures, actual A5/A6/A7/D17 event/custody, screen-reader coverage, low-end frame rate, full inherited VTTG regression, and independent commercial-art acceptance. Visual remasters are structurally different but **do not yet meet comparative commercial graphical quality**.

**Next bounded cycle:** `MME-02E3-C` settlement/urban native structural remasters and richer purpose-specific architecture, with an additional `.mapforge.json` → art-only import adapter and art image package/provenance investigation if feasible without duplicate MMHT authority. Maintain original map examples and all source IDs when generating new native editable copies.
