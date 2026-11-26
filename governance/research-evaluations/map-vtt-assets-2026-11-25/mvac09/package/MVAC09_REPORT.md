# MVAC-09 — Measured renditions and color/alpha pipeline

26 November 2026. Bounded standalone rendition adapter and named local codec/profile validation complete. Browser/device, managed-display/print and installed-product acceptance remain open.

Open **Multiversal_MVAC09_Image_Renditions.html → Image renditions**. Select one of the 11 embedded harbor sources, choose a size/format and generate/download a copy. Thumbnail is bounded to 128 pixels, Play to 256, and Source/print candidate to the source's existing pixels. No profile enlarges a source. The format selector offers PNG, lossy WebP quality 90 and JPEG quality 92. JPEG conversion of transparent art rejects unless the user explicitly chooses white or black flattening.

The original PNGs and all prior artwork remain embedded. Each conversion starts from the preserved source; it never recompresses the last preview. A versioned recipe records source SHA-256, source/output dimensions, format, quality, color/orientation/alpha policy and matte. The encoded output receives its own SHA-256 and is decoded again to check dimensions and requested format. Silent encoder MIME fallback, bad signatures or mismatched dimensions reject. Preview cancellation/selection changes suppress late results; closed/replaced previews revoke Blob URLs.

## Measurements, not assumed format wins

Actual encoded trials on all 11 sprites used the named local Pillow encoder/decoder. The report preserves per-asset bytes, hashes, encode time, five-decode median, alpha identity and black/white composite error.

| Encoding at original sprite dimensions | Bytes | Reduction from original PNG |
| --- | ---: | ---: |
| Preserved original PNG | 1,490,044 | — |
| Optimized PNG | 1,478,306 | 0.79% |
| Lossless WebP | 1,050,696 | 29.49% |
| Lossy WebP quality 85 | 336,704 | 77.40% |
| JPEG quality 90 on explicit white matte | 263,742 | 82.30% |

Optimized PNG and lossless WebP decode to exactly the same RGBA values in the local Pillow comparison. Lossy WebP retains the alpha channel but changes RGB. JPEG loses transparency and is excluded from automatic map use. JPEG's size saving does not justify applying an opaque box to translucent art. The browser-facing WebP option is quality 90 and must not be confused with the separate local lossless or quality-85 trials.

No full-resolution alternative set is embedded alongside the originals. The HTML grows by only 12,979 bytes, to 13,618,915 bytes, because optional outputs are generated when requested. The table describes potential rendition bytes, not an equivalent reduction in the complete HTML or a measured network/storage bill. Runtime compatibility is checked through actual encode/decode rather than assumed from an extension.

## Native map integration

**Toggle play previews on map** builds bounded 256-pixel canvases for the family and requests a native redraw. Turning it off clears those derived previews and returns rendering to the original sources. It changes neither native geometry nor saved document/scene revisions. Pending author edits must be applied or cancelled first. The temporary profile is not a new canonical asset version or saved placement pin.

The existing family draw call can choose a generated preview with a proportionally scaled content rectangle, anchor and pivot; unavailable previews fall back to the embedded source. No new renderer/catalog/document system is introduced. The author shell gains only a guarded refresh hook; family rendering gains only the preview-selection seam. Ten of the twelve MVAC-08 script bodies remain byte-identical, including the original renderer, rights/manifest review, intake and full family source data.

The native city comparison uses identical geometry/camera with source sprites before and play previews after. These views should look close: this cycle preserves scene quality while preparing smaller renditions. The local mean channel difference is approximately 0.155 on a 0–255 scale, with a maximum 54 at isolated edge/detail pixels. This is a measured comparison, not artistic approval or a perceptual-quality certificate. Single-run render timings are retained but support no speed claim. Original image/source caches are retained, so this prototype does not claim lower total memory use; lifecycle/eviction remains later storage work.

## Color, alpha, orientation and print limits

The embedded generated sprites are untagged RGBA PNG sources; their pixel values are treated as assumed sRGB. This is an explicit interpretation, not proof of their originating color space. Runtime canvases request sRGB and report the actual context color space when the engine exposes it; an unreported result remains unreported. This panel operates on the normalized embedded family, not arbitrary untrusted/profiled uploads.

The offline profile set preserves originals and creates 33 PNG derivatives: 128-pixel thumbnails, 256-pixel play copies and source-pixel print candidates. These use an embedded sRGB ICC profile. A print candidate receives 300-DPI metadata, but no additional image detail or print suitability is invented. The manifest reports physical inches at 300 DPI; a roughly 320-pixel object is only about one inch at that density.

Actual synthetic JPEG fixtures exercise EXIF orientation 6 through Pillow's transpose operation, then an ICC sRGB-to-sRGB transform. Axes swap once, orientation is removed, identity-conversion pixels match and original encoded bytes remain unchanged. This is named local color/orientation proof, not browser ICC parity or professional print calibration.

A translucent colored-edge fixture with blue alpha-zero surroundings verifies alpha-aware resizing without blue matte contamination. Black and white composites, opaque JPEG, transparent PNG/WebP, explicit JPEG mattes and repeated source-based conversions are covered. A symmetric synthetic tile checks opposite-edge continuity; the harbor objects remain explicitly non-tileable. No claim of making individual foliage/buildings seamless is made.

## Verification

306 fresh checks pass, zero fail:

| Suite | Checks |
| --- | ---: |
| Rendition core, actual native codecs and delivered controls | 33 |
| Local ICC/orientation/alpha/profile cases | 7 |
| Family regression | 28 |
| Native editor / selection-history regressions | 48 / 33 |
| Rights / manifest review regressions | 66 / 71 |
| Delivered intake regression with actual Node decoder workers | 20 |

The native-code test harness supplies real local image encoders/decoders and Blob URL loading; it is explicitly a controlled DOM, not a real browser. Earlier renderer/review/intake bodies and full source data are checked for exact preservation. Physical Windows/Android targets, browser encoder/ICC/layout behavior, GPU/display/print output and installed builds remain NOT_RUN. MVAC-03/04 gaps and all 40 broader workflow/device tasks remain open. No final creator acceptance is inferred.

## Next

MVAC-10 — usable asset discovery and editable placements: searchable/tagged/style/scale browsing with cheap previews, recent/favorite sets and per-instance edits over the existing native object system. Source fallback, explicit provenance and the single self-contained HTML remain requirements.
