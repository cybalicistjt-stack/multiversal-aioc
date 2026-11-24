# GM-MME-02D3 / E0-A — Multi-zoom Baseline and Source-space Procedural Field Preview

**Owner approval:** 2026-11-24 "I approve, update this in ops5 and continue", referring to the four-source procedural-art study and proposed shared-field architecture. This is **bounded owner-review standalone HTML**, not product implementation authority. OPS5 `gm-workspace / GM-00`; main `operations/CURRENT.json` and domain source owners unchanged. Draft review [PR #2049](https://github.com/cybalicistjt-stack/multiversal-aioc/pull/2049). New architecture registered at `GM_MME02E0_APPROVED_PROCEDURAL_ART_FOUNDATION.md`.

## Actual UHT-08 deliverable

- Full cumulative standalone tester: `Multiversal_Consolidated_Playtest_UHT08_MME02D3.html`, **40,689,985 bytes**, SHA-256 **`3de206e78c459a1873d1e1b208269334d7a02ed7ff99351ac8b44ed2c1f4ebaa`**.
- Embedded GM: `Multiversal_GM_MME02D3_Procedural_Field_Preview.html`, **23,957,528 bytes**, SHA-256 `46f6b49617dfbc38a5f5c61b1aa5964c0ef07897f153f9cddcb9be6a2a774921`.
- Native Map Maker: `Multiversal_MME02D3_Native_Map_Maker.html`, **5,951,544 bytes**, SHA-256 `c8d03b0fdc1cc52ce5f3bef55ed3d480be085f89092370645775fcad7fb79f09`.
- Owner-download ZIP: `Multiversal_MME_02D3_Procedural_Field_Review_Package.zip`, **47,269,273 bytes**, SHA-256 `7bf24016543f592b874ad3fc9a03b0259ba2dc1f2bb41280dcc338ef4817a437`; 43 entries, ZIP CRC verified, exact UHT-08 bytes verified in archive. Binaries are in the owner conversation, **not checked in** as product commits.
- Exact source input is owner UHT-07 SHA `2fe97ba6f1ed29897be04d05a556c24b2be75e7445bc16d654439319a138c044`. Build script removes 3 bounded native renderer hooks + 2 additive style/script blocks and reproduces original Map Maker *byte-for-byte*. Character, Downtime, Recovery and corpus compressed source payloads unchanged.

## Functional implementation

A `MMHT_MME02E0` deterministic visual-field engine with seeded coherent value noise, five-octave fBm, bounded domain warp, and procedural elevation/moisture/detail sampling used **only for illustration**. It clips cached raster material color and topographic tonal variation to source-authored floor, room, cave, tunnel and tactical-paper geometry, sampling world/map coordinates so the design survives zoom. Rasters capped at 280×280, cache max 96 entries, invalid seeds and settings refused. Local art preference controls: Original/Seeded fields; variation Subtle/Balanced/Defined; domain warp None/Soft/Organic; integer seed. The appearance preference is not map metadata.

The existing source geometry (including floor ID/revision/map ID and five-foot calibrated squares), art styles, GM game authoring dock, VTTG06–10 encounter/vision/trigger/loot/floor controls, 66 curated example catalog and other consolidated workbenches are retained. No canonical biome or elevation facts, gameplay movement, source-authorized light, fog, player rights, asset custody, inventory or rules events are changed.

## Exact tested scoped browser checks

| Chromium suite | Passed / total |
| --- | ---: |
| Five native maps: deterministic math, new material rendering, exact Original pixel recovery, source-data invariants and rejection checks | 41/41 |
| Entire UHT-08 launch, nested map workbench, five VTT panels, game-builder dock, 66 catalog | 19/19 |
| 390px mobile controls/access/no overflow | 10/10 |
| Calibrated five-foot grid and zoom/source preservation | 9/9 |
| 45 currently mounted maps open (34 interior, 7 regional, 2 tactical, 2 urban) | 5/5 |
| 3-map three-scale zoom/material/cache/ID tests | 16/16 |
| **Scoped checks** | **100/100** |

New JavaScript `node --check` passed and final ZIP integrity passed. This includes a deterministic field cache performance sample but **does not establish full-frame timing or low-end-device FPS**. 66 catalog entry presence is not 66-example workflow coverage; 45 mounted documents were smoke-opened.

## Comparable-to-existing-tools target

**Not achieved.** The preview adds a shared technical layer but produces incremental visible variation, not a quality match for finished Inkarnate/Dungeondraft/Dungeon Alchemist maps. Missing professionally illustrated/controlled asset packs, compelling geometry/composition, architectural variation, foliage richness, art direction and final export polish cannot be solved with noise alone.

**Next:** MME-02E0-B source-derived actual biome/elevation/moisture masks and material/edge-boundary blending (only on maps with source data), otherwise clean no-source fallback. Then E1 materials, E2 original/licensed high-fidelity assets, E3 clustering, E4 architecture, F shadows/lighting, G/H art style/export. Continued GM VTT authoring MME-07/08 remains a separate source-aware project goal.

**Unverified:** all 66 edited workflows, real server D05 authorization and Player export, installed Unity, Windows/Android two-device, physical low-end performance, screen readers, full inherited VTT regression and independent artist review. No protected-main changes or product authorization are implied.
