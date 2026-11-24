# GM-MME-02E0-B — Source-aware regional rendering local acceptance

**Owner continuation:** 2026-11-24 · "Continue" following approved procedural-art foundation (MME-02E0). OPS5 lane/work item: `gm-workspace / GM-00`. Implementation authority remains `false`; this is standalone HTML owner playtest only. Protected `operations/CURRENT.json` unchanged; draft registration and review [PR #2049](https://github.com/cybalicistjt-stack/multiversal-aioc/pull/2049).

## Exact owner-review artifacts
- `Multiversal_Consolidated_Playtest_UHT09_MME02E0B.html`, **40,698,836 bytes**, SHA-256 `d5e790bb2d50486fa41720186b1408080cf342c1b5431a848ed1acafbb4596bc`.
- Nested GM standalone, `Multiversal_GM_MME02E0B_Regional_Source_Art.html`, **23,977,088 bytes**, SHA-256 `9adb1b3c2d67e6e70dfb7264244cd1b5eda13413072cc738b753085ab19807fd`.
- Native Map Maker, `Multiversal_MME02E0B_Native_Map_Maker.html`, **5,966,214 bytes**, SHA-256 `12fcee2899afae7e39a9ddf5440b62918491db7014873746eb21139ab982e10b`.
- Owner-review ZIP `Multiversal_MME_02E0B_Source_Aware_Regional_Review_Package.zip`, **47,329,292 bytes**, SHA-256 `91004d922d0d3d9a6f9891a62c963f7d70d36db25e1b47d7492ccb8c2da0b68d`; 49 entries, every CRC and SHA-256 in included manifest verified, exact tested consolidated HTML bytes match archive. Files distributed as conversation artifacts, not committed binaries.

## Exact source contract and implementation
- Rebuilt from owner UHT-08 SHA-256 `3de206e78c459a1873d1e1b208269334d7a02ed7ff99351ac8b44ed2c1f4ebaa`. The Map Maker source is reconstructed **byte-identically** by undoing four bounded rendering/cache hooks and removing two attached style/script blocks. Character, Downtime, Recovery, corpus compressed payloads byte-identical.
- Existing regional source features include `terrainClass` (e.g. `ARCH-FOREST`, `ARCH-WETLAND`, `ARCH-HIGHLAND`, legacy `forest`), optional environment references and authored `elevationMeters`. Actual regional relief channels include source-based land/water RGBA masks, distance-to-shore/sea, forest, marsh, mountains, snow and relief height. *No universal source climate/moisture dataset established.*
- `MMHT_MME02E0B` renders constrained visual terrain motifs and source river/shore/ridge finishing. It does not create or move any sources, elevation, biome, roads, watercourses, assets or gameplay Events; unknown terrain classes stay unchanged.
- Specific native relief display issue addressed: cached source relief may intentionally skip feature paint; added source-aware decoration at the existing GM-visible, layer-filtered regional relief branch, rather than creating a separate board or unfiltered layer. The relief masks' RGBA layout is validated before use. In the first trial, strong polygon outlines harmed organic relief appearance; they were explicitly removed from the relief branch before final acceptance.
- Original/source mode and Soft/Balanced/Defined styling. Controls placed in the existing collapsed advanced panel to keep canvas-first. Global Original switch disables E0B. Art remains underneath native VTTG06–10 overlays and does not alter calibrated 5-ft grid IDs or fog.

## Final-file scoped Chromium evidence
| Suite | Pass |
| --- | ---: |
| Six native map cases (four regional examples that change, regional no-source and nonregional no-change), fallback/reversibility, source and Event guards | 55/55 |
| Actual UHT-09 launcher > nested GM and Map Maker/VTT panels, canvas-first and global Original semantics | 21/21 |
| 390px mobile controls and no horizontal overflow | 11/11 |
| Three real maps / two zoom increments / stable five-foot references and source data | 16/16 |
| All 45 mounted documents open: 34 interior, 7 regional, 2 tactical, 2 urban | 5/5 |
| **Total scoped** | **108/108** |

Original-pixel restoration is exact in the six tested map cases. Visual changes are intentionally restrained, not a claim of commercial graphical parity. `node --check` passed; source reversal and ZIP integrity passed.

## Known limitations
The 66 curated **example catalog remains present**, but the 45 mounted documents do not represent 66 fully completed example workflows. Full inherited GM/VTT regressions, actual server D05 visibility rights, Player-safe exports, true A5/A6/A7/D17 owner gameplay effects, native file-origin reload, screen reader conformance, Unity deployment, physical Windows/Android LAN, low-powered frame-rate benchmarks and independent artistic acceptance are **not certified**.

**Next:** MME-02E1 material/edge atlas with coherent multi-scale art direction; then E2 original/licensed illustrated asset packs, E3 clustering, E4 architecture, F1/F2 shadow/environment lighting, G genres and H final export/performance/quality gates. Keep GM-in-map encounter/trap/loot/NPC authoring on the approved MME-07/08 trajectory.
