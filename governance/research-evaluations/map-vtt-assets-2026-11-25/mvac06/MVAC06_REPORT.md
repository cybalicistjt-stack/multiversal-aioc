# MVAC-06 — Embedded asset manifests and immutable placement pins

25 November 2026. Standalone embedded-manifest adapter completed and locally verified. Installed asset management, transactional ingestion, authenticated rights enforcement and real-browser/full-workflow acceptance are separate later work.

## One complete HTML remains the runtime

`Multiversal_MVAC06_Embedded_Asset_Manifests.html` retains the entire MVAC-05 prototype: native rendering, seven example maps, selection/locking/isolation, author history/checkpoints and the rights review. The new **Asset packs** panel indexes the 48 PNG artworks already embedded in that HTML. No image bytes were added, moved to a companion folder, made downloadable on demand or replaced with remote URLs.

The optional source archive and metadata export are inspection/reproduction artifacts. The HTML does not need them to open. Its six previous script bodies are byte-identical to MVAC-05; the native renderer script receives an ID so the adapter can locate its existing embedded data. The new metadata/UI adds 95,382 bytes and no new image payload.

## Real catalog, explicit adapter scope

The manifest was generated from the existing MME-02E2 source catalog. All 48 original PNGs were decoded at build time with Pillow. Their declared and actual dimensions matched; byte lengths, complete SHA-256 digests, alpha-channel presence/observed extrema and embedded ICC presence were recorded. The adapter also verifies every original byte range against its digest and PNG dimensions.

These are adapter records over an existing local catalog, not a new canonical asset registry or storage system. Existing ARI/native owners retain registration and document authority. Legacy catalog IDs are preserved in each adapter asset record. Usage rights remain separate references: the current metadata records unknown license evidence rather than inferring permission from a verified digest or from being inside the HTML.

## Manifest contract

`MANIFEST.json` uses `multiversal.embedded-asset-pack.v1`, schema `1.0.0`, with an exact pack identity/version and an explicit mandatory feature list. V1 supports this existing PNG family and native artwork coordinates. It deliberately rejects unsupported profiles instead of guessing conversions.

| Record | Pinned or preserved fields |
| --- | --- |
| Pack | Stable adapter pack ID, exact `major.minor.patch` version, supported schema, mandatory features, exact dependency versions and optional metadata. No implicit version ranges or automatic upgrade. |
| Logical asset | Stable adapter asset ID, original catalog ID, label, tags/theme, source-owner reference, list/default representation and separate ARI rights reference. |
| Representation | Stable representation ID, asset owner, blob reference, MIME, dimensions, anchor, orientation, alpha observations, color profile, source blob and recipe ID/version/operation. |
| Immutable blob | SHA-256 identity, encoded byte length and embedded-script locator. Identical bytes may be referenced by distinct logical asset/representation records without merging their rights. |
| Instance pin | Native document ID/revision/floor reference, distinct instance ID, exact pack version, asset/representation/blob/recipe pins, immutable representation snapshot and per-instance transform. |

The observed draw operation centers images at `(-width/2,-height/2)`, so the current family uses anchor `(0.5,0.5)`. Orientation is asset-local x-right/y-down; it is not world north. Original `sizeHint` becomes a native-artwork width hint. Physical units per pixel stay explicitly unknown. The adapter rejects an implicit feet/meters calibration rather than inventing world distance.

The recipe is `preserve-original`, version `1`; no codec conversion, crop, recoloring or new rendition bytes are introduced. Alpha extrema and ICC presence are build observations of existing source images. Runtime verification checks byte identity and PNG header dimensions; it does not claim a new color/alpha quality certification.

Unknown optional metadata survives JSON round-trip. Unknown mandatory features, unsupported schemas/MIME/color profiles, duplicate identities, cross-owner representation references, invalid dimensions/anchors/scales, missing blobs, inconsistent recipe/source references, excessive counts and remote locators reject with named findings. This is bounded manifest validation, not a replacement for MVAC-07's untrusted-file ingestion transaction.

## Embedded byte resolution

Blob locators refer to a UTF-16 character range inside the existing `mvac-native-renderer` script. They do not contain a network address. These ranges are a build-local transport index; asset IDs and blob digests are the stable identities. A later build can regenerate offsets while preserving the same logical assets and bytes.

On explicit **Verify bytes & preview**, the adapter reads only the selected range, requires an embedded PNG data URI, decodes it under the declared size/range bounds, verifies complete SHA-256 and byte length, and checks PNG/IHDR dimensions. A wrong range, corrupt digest, unexpected media or dimension mismatch fails visibly. No external fetch or file lookup is attempted.

If SHA-256 is unavailable in a browser, this optional verification reports `verification-unavailable`; the existing map editor remains independent. It does not turn the HTML into a linked-file application or request a replacement download. A verified result can preview the already embedded image on a checkerboard background. A stale asynchronous result cannot replace a newly selected asset's preview.

## Version and dependency behavior

The baseline pack is `1.0.0`. A synthetic compatibility example offers `1.1.0` with a changed default anchor/recipe for the first asset while retaining the old representation. The original instance pin still resolves `1.0.0` and its original representation. If only `1.1.0` is available, resolution reports `missing-pinned-pack`; it does not substitute the new default.

Changing presentation metadata under the same pinned representation causes `incompatible-pinned-content`. The pin checks its full representation snapshot, blob and recipe version; a matching byte digest alone cannot silently change an anchor or render recipe. Per-instance position/width/rotation are returned from the explicit pin, not recomputed from the newest catalog defaults.

Exact dependency closure is checked before pin resolution. Missing versions, invalid schemas, cycles and duplicate immutable pack identities reject. The adapter never downloads a dependency or mutates an installed-pack state. Dependency/activation, trust/signatures, rollback and interrupted installs remain MVAC-11 and associated owner work.

The shared-byte scenario adds a clearly synthetic logical alias with its own representation and rights reference but the same blob. No bytes or grants are copied/merged. It demonstrates byte reuse independently from logical ownership.

## Native documents and the pin example

The seven frozen native maps have no explicit persistent bindings to these new manifest records. `INSTANCE_PIN.json` is therefore labelled as a synthetic placement reference anchored to the Tidewatch map/floor; it is not a claimed migration of an existing chest, tree or door. No native geometry, actor identity, wall opening, fog or gameplay state is changed.

Native author Save remains in the existing `multiversal-cartography-tester-v2` document format. This adapter prepares an extension boundary for later reviewed bindings; it does not replace native documents or silently attach an extra asset system. Resolution returns cloned metadata and explicit flags: no automatic upgrade, owner mutation, rights grant or byte-verification claim before verification actually runs.

## Review and export

The Asset packs panel searches real asset names, legacy IDs and theme tags; displays pins, scale, anchor, orientation, recipe and alpha/color metadata; runs eight compatibility examples; and verifies/previews the original embedded PNG. It also exports a metadata-only manifest for inspection. That exported JSON is not required to run the HTML and contains no copied source PNG payload.

The Asset rights panel from MVAC-05 is retained unchanged. Metadata validation and SHA-256 verification do not grant private use, campaign delivery, map export, modification or raw redistribution. The actual optional sheet license evidence remains unresolved; this cycle does not clear or convert those sheets.

## Evidence and limits

94 adapter/integrity checks pass, including complete hashing and dimension checks for all 48 embedded PNGs, exact version retention, shared bytes with separate rights records, schema/feature rejection, dependency failures, source immutability and defensive result copies. The exported manifest and synthetic pin match the data embedded in the delivered HTML.

71 manifest-review checks pass against the actual delivered script in a controlled DOM. They cover all eight scenarios, all 48 metadata records, real verified preview, stale preview cancellation, search/empty results, metadata export, source-document preservation and six unchanged prior script bodies.

The existing rights-review and editor suites are also run against this HTML: 66 MVAC-05 review checks, 33 MVAC-04 selection/history checks and 48 MVAC-03 native-editor checks pass. **312 local checks pass in total.** The old/new script fingerprint baselines and seven native fixture hashes are preserved in the evidence.

These are real local adapter/byte and controlled-runtime results. Actual browser layout, text undo/Escape/focus, touch usability, authenticated clients, signed manifest trust, storage/installation, receiving apps and installed runtime acceptance are not certified. MVAC-03/04 retain their existing browser/full-workflow gaps; all 40 broader workflow/device tasks remain NOT_RUN.

## Status and next step

MVAC-06 is complete for the bounded standalone embedded-manifest adapter and reference pin validation; installed-product `implementation_complete` remains false. Existing documents, original image bytes, selectors and persistent lanes remain unchanged.

Next is MVAC-07: bounded, transactional ingestion—validate bytes and media, control decode/archive limits, stage changes, preserve originals and cancel/reject without exposing half-ready content. The single-file HTML requirement remains: user-selected import files are optional data, not required companion assets or external services.
