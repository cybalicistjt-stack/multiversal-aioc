# MVAC-07 — Bounded transactional asset intake

25 November 2026. Completed for the bounded standalone inspection adapter and local evidence scope. Installed-product implementation and real-browser acceptance remain open.

Open `Multiversal_MVAC07_Transactional_Asset_Intake.html`, choose **Asset intake**, and try the embedded sample or select optional files. Stage validates the entire batch privately. **Keep validated batch for local inspection** publishes the complete batch together. Cancel, decode failure and stale activation leave the previous active collection intact. Show validated preview displays a worker-produced PNG.

The HTML is self-contained. All eight MVAC-06 script bodies, existing source documents, 48 embedded PNG assets and earlier controls are preserved. The new worker code and tiny sample are embedded too. No asset server, companion script, archive, or installation is required. Imported files are optional session data and never become requirements for opening the existing maps.

## Actual behavior and boundaries

- PNG, 8-bit baseline/sequential/progressive JPEG, static lossy/lossless WebP, and a positive geometry-only SVG subset are supported. Image bytes, signature/headers, dimensions, single-frame policy and declared MIME are checked before native decoding. Decoder success and matching dimensions are also required. Container validation is not a complete media-format conformance certificate.
- PNG checks chunk boundaries, CRC, critical chunks, palette/transparency constraints, IDAT contiguity and exact EOF. APNG and animation WebP reject. GIF, RAR, 7z and other unsupported files reject explicitly.
- SVG supports svg/g, rect, circle, ellipse, line, polyline and polygon with bounded coordinates, vertices, nesting, solid paint and selected stroke attributes. Paths, CSS, text, scripts, events, entities, references, images, URLs, filters and animation reject. A reconstructed geometry tree is drawn directly; the raw SVG never enters an image/DOM decoder.
- Raster decoding receives a metadata-free copy. PNG keeps structural/palette/transparency/image-data chunks; JPEG drops APP/COM metadata; WebP keeps canvas/alpha/image chunks and clears metadata flags. Exact originals remain byte-identical. Previews are for inspection: orientation, ICC color fidelity and metadata preservation in derivatives are not claimed. The measured rendition pipeline belongs to MVAC-09.
- ZIP supports stored/deflate entries and checked data descriptors. Central/local headers, CRC, exact expansion length, normalized names and entry ranges are checked. Traversal, duplicate case/NFC paths, absolute/drive/backslash/reserved names, links/devices, encryption, ZIP64, nested archives and unsupported active files reject. No archive entries are extracted to the filesystem. Expansion streams stop when declared bounded output is exceeded.
- TXT/JSON sidecars are bounded UTF-8 evidence, retained as original bytes. They are not executed, merged into application objects or interpreted as permission grants. Unknown rights remain unknown.
- Original selected archives, extracted image sources and sidecars are retained privately in memory with source hash and archive lineage. Equal bytes can share a blob while keeping distinct logical asset IDs. Defensive-copy getters protect stored originals.
- The existing pinned ARI-10 helper supplies private stage/inspect/decision/commit receipts. Its partial internal commit stays private; the adapter publishes only when every candidate is complete and the activation revision still matches. This is one atomic local inspection collection, not a new canonical registry or entitlement authority.
- Imported assets are not bound to native maps, exported, saved with project documents or persisted between sessions. Reloading loses the optional collection. Durable/crash-safe activation, storage and portable saves belong to MVAC-11/12/13; artwork placement belongs to MVAC-10. The original HTML maps remain usable independently.

## Limits

| Resource | Bound |
| --- | --- |
| Selected files / ZIP entries / images | 32 / 64 / 32 per batch |
| Image source / ZIP / encoded batch | 8 / 16 / 24 MiB |
| Expanded batch / expansion ratio | 24 MiB / 200:1 |
| Dimensions / pixels per image | 4096 per axis / 4,194,304 |
| Pixels per batch | 8,388,608 |
| Active collection | 64 images; 64 MiB unique original bytes |
| Safe SVG / evidence sidecar | 256 / 128 KiB |
| Preview | At most 512 per axis; 2 MiB PNG |
| Worker timeout / transaction timeout | 5 / 30 seconds |
| Concurrent stages / retained transaction records | 2 / 32 |

Decoders run sequentially in terminable workers. Browser execution uses an embedded Blob worker with OffscreenCanvas/createImageBitmap; originals are never rendered directly. Unsupported runtime capabilities produce a rejected batch. The Node test adapter uses actual worker threads and a native codec. A worker is a cancellation/resource-lifetime boundary, not a claim of an OS security sandbox or a hard native-memory cap. This cycle does not certify codecs against every malformed stream or establish lower-powered-device performance budgets.

## Verification

316 local checks passed; zero failed.

| Evidence | Passed | Scope |
| --- | --- | --- |
| VERIFICATION.json | 78 | Real PNG/JPEG/WebP and safe-vector decode in isolated Node workers; real ZIP decompression; negative headers/paths/expansion; original retention; ARI private partial commit/retry/idempotence; stale activation; cancellation, worker death and timeout |
| UI_VERIFICATION.json | 20 | Delivered HTML in controlled DOM harness using actual Node decoder workers via a Worker shim; source-stream and worker cancellation; close cleanup; atomic activation; inherited-script identity |
| MVAC03_REGRESSION.json | 48 | Existing native renderer/editor flows in controlled DOM/native canvas |
| MVAC04_REGRESSION.json | 33 | Selection/history/checkpoint regressions |
| MVAC05_REVIEW_REGRESSION.json | 66 | Rights-review regressions |
| MVAC06_REVIEW_REGRESSION.json | 71 | Manifest-review regressions |

Browser Worker/OffscreenCanvas/createImageBitmap behavior, file-picker/drop interaction, browser layout, physical devices and installed builds are NOT_RUN. MVAC-03 remains blocked_external and MVAC-04 implemented_validation_partial. All 40 broader full workflow/device acceptance tasks remain NOT_RUN. These are test-environment/acceptance gaps; the HTML has no missing runtime dependency.

## Reproduction and provenance

`node verify.mjs` tests the core against the pinned owner-contract copies and generated fixtures. `node check-intake-ui.cjs` executes the delivered HTML through the controlled harness. The suite expects Node 24, `@napi-rs/canvas` and the same neighboring deliverables used by the harness. Those are developer-test dependencies only, not HTML runtime requirements. The optional evidence archive preserves test code, workers, validator, fixtures, hashes, owner contracts and reports; it is not needed to run the HTML.

Owner contracts are pinned to Multiversal-app commit `db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f`, with exact blob and SHA-256 digests in SOURCE_PINS.json. Existing ARI/PCA ownership and the rights model are retained. No user sheets have been newly embedded or granted rights. Fixtures are generated specifically for this validation; no external art is needed.

Format references used to check the bounded readers: [W3C PNG Third Edition](https://www.w3.org/TR/png-3/), [Google WebP RIFF specification](https://developers.google.com/speed/webp/docs/riff_container), [PKWARE ZIP APPNOTE 6.3.10](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT). Their specifications are referenced, not redistributed.

## Next step

MVAC-08: prepare a small coherent illustrated asset family for settlement/interior/vegetation, with reviewed alpha/crops, scale/anchors, palette, source lineage and shadow policy. Compare before/after scenes at fixed geometry and several zoom levels. Keep creator visual review separate from automated measurements and retain the self-contained HTML.
