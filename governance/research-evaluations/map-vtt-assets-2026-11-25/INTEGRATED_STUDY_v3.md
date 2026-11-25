# Map Makers, VTTs and Assets — Integrated Evolution and Gap Study v3

25 November 2026 · Multiversal · UHT28 standalone baseline · Research and OPS5 planning

This report combines the two preceding map-maker/VTT studies with asset lifecycle research and a concrete gap plan. Read the Asset sections and MVAC plan first for the new findings; the retained Map, VTT and Joint sections follow with their original evidence. The final source register covers all 85 records. This edition adds 28 records: 25 public sources and three pinned NCG research records.

**Recommended direction:** retain native editable documents and existing gameplay/media owners; provide coherent editing and preparation; use referenced optional assets with measured renditions, durable originals, bounded caches and complete recovery; qualify authorized live play at real client boundaries.

The 24 MVAC steps below are recorded as planned, not selected or implemented. OPS5 CURRENT remains the only live selector. This research cycle authorizes no product rewrite, provider purchase, new subscription system or installed release. UHT28 and the supplied originals remain unchanged. The previous studies remain preserved as separate artifacts.

## Asset study — decisions that avoid repeated mistakes

**Keep a small core application, reference optional versioned asset packs, preserve original sources, and load only the renditions needed for the current task and audience.** Treat images, editable objects, media blobs, permissions and scene placements as related records with different responsibilities. This is an integration direction to validate against our existing ARI/media/document owners, not permission to replace them.

The strongest recurring failures are broader than file extensions: oversized decoded images, broken relative paths, backups without dependencies, updates changing old work, permission leaks through previews, too many live resources, and asset libraries that are technically large but difficult to use. We can adopt the known design responses early. Our own hardware, artwork and multiplayer boundaries still require tests; literature cannot eliminate those lessons in advance.

This edition combines the previous map-maker and VTT studies with a dedicated asset investigation: 85 source records in total, including 25 new public asset/format/runtime sources and three pinned NCG research records. It adds a fresh bounded audit of our 22 supplied sheets and a 24-step convergence plan. Historical map/VTT findings are retained below; the MVAC plan is the current recommendation in this report. Product implementation remains paused.

## Asset 1. Method and evidence

Coverage includes raster and vector art, terrain/materials, editable placements, architectural assemblies, 3D imports, animation/audio, source/master versus delivery format, packaging, resource identity, storage, caches, offline use, migrations, recovery, security, rights, quality, performance and operating cost. It does not claim a complete history of every commercial product or a universal best codec.

Evidence is divided into developer history, documented capability, primary format/runtime specifications, bounded local measurements, and proposed Multiversal behavior. A creator's workaround is useful evidence of a problem, not proof of its frequency. A format appearing in a manual is not installed-device compatibility. A module or SDK being public does not make the engine or artwork open source.

The asset research concentrates on Foundry, Owlbear, Roll20, Fantasy Grounds, Tiled, LDtk, Dungeondraft tooling, Wonderdraft, Dungeon Alchemist and TaleSpire, with runtime references from Unity, Khronos, Mozilla, W3C and OWASP. The earlier study retains additional map-maker histories. Product-family counts should not treat Unity or a graphics specification as additional VTT competitors.

**Existing project research:** NCG DAMC separates logical assets, immutable blobs, renditions, recipes, delivery and offline packs. Its current status records a synthetic reproduction harness but leaves independent-host and real application/device boundaries open. The older debt document's R1 wording predates that progress; CURRENT controls the current family status. This study uses the model as advisory and carries the open evidence forward. [A26](#a26) [A27](#a27) [A28](#a28)

## Asset 2. Evolution and the problems it exposed

| Documented point | Change or problem | Lesson we can apply before scaling |
| --- | --- | --- |
| ProFantasy's 2014 art journal, retained in the map study | A sample map precedes a coordinated symbol/effect family | Review one complete style scene before ordering thousands of assets [S02](#s02) |
| Tiled 1.1 and later format changes | External templates, chunked infinite maps, compression and compatibility-related field changes | Resource referencing and format evolution need explicit version handling [A25](#a25) |
| MapTool 1.9.3, July 2021 | Separate fixes for cache failure, UVTT lighting, ownership and export overwrite | Asset, import, permission and recovery errors require separate acceptance cases [A12](#a12) |
| Dungeondraft community pack tooling, README copyright 2021 | Tags, pack/unpack, conversion and map dependency inspection | Pack construction is tooling and metadata work; compression alone does not reduce decoded pixels [A11](#a11) |
| Roll20's retrieved English guide, January 2023 | WebP conversion can help but can also make a file larger | Choose by measured result and visual quality, not extension [A08](#a08) |
| Dungeon Alchemist, August 2023 | Custom 3D import and configured models shared through Workshop | Imported bytes require configuration and distribution, not only a file picker [A14](#a14) |
| Foundry v11-era packaging and v13-era filepicker rules | Reusable content modules and protected upload locations | Keep installed content separate from user additions and migration-safe paths [A02](#a02) [A03](#a03) |
| Owlbear 1→2 migration documentation | Conversion creates separate map/image and scene resources | Preserve old work while changing storage concepts; import selectively with limitations [A07](#a07) |
| Owlbear May/October 2026 journals, retained in VTT study | Conditional conversion, improved structural extraction and service-latency tradeoffs | An optimization should include fallback, correction and the full user wait [V15](#v15) [V19](#v19) |
| Present-day primary runtime guidance | Reference lifetimes, updates, quota failure and GPU texture formats | The delivery, durable-storage and runtime-memory problems need distinct solutions [A17](#a17) [A18](#a18) [A19](#a19) [A20](#a20) |

This is a sampled evolution, not a claim that every product progressed through the same stages. The older guide dates identify historical advice; they are not a complete current compatibility inventory.

## Asset 3. What we learned from the asset systems

### Foundry — packaging, paths and backup closure

Its media guide distinguishes opaque/translucent art, token orientation, scalable symbols and animated delivery, while acknowledging CPU-versus-bandwidth tradeoffs. Asset Management describes user-data locations, v13 filepicker upload restrictions and player upload permissions. The packaging guide recommends reusable modules and compendia, including staged paths, rather than treating a prebuilt world as the preferred distribution unit. [A01](#a01) [A02](#a02) [A03](#a03)

Its backup documentation is explicit that package backups/snapshots cover package directories and can omit assets elsewhere. A recoverable world is therefore not established by a world database alone. [A04](#a04)

**For us:** package identity, immutable referenced content, user overrides and the dependency closure must be visible. A backup screen should say whether artwork, audio, fonts and optional packs are included or still required. Preserve user content outside installed-pack replacement paths. Validate the receiving tool, not just JSON syntax.

### Owlbear — reusable images and manageable libraries

The asset interface separates a frequently used dock from an asset manager with search, tags, editing and import. A map image exists outside a scene and can be shared across scenes without repeatedly storing the large image. The migration guide converts `.owlbear` to `.ob2`, with selective import and compatibility notes. [A05](#a05) [A06](#a06) [A07](#a07)

**For us:** one source asset should support many placements and scenes. Keep instance transforms/overrides in the native document; do not duplicate the whole image for each tree or session. A common map-import path should remain short even when pack controls grow. Keep a recoverable copy when migrating older documents.

### Roll20 and Fantasy Grounds — target profiles matter

Roll20's conversion guide warns that results vary and distinguishes static WebP from animation support. Its historical encoder example should not become a general claim about today's Dungeondraft exporter. [A08](#a08)

Fantasy Grounds' creator guide distinguishes map, stamp, token, animation and skybox recommendations. It advises avoiding duplicate common images in player and GM modules. These are vendor guidelines, not measured limits for our app. [A09](#a09)

**For us:** create named recipient profiles with verified codec, size, scale, transparency and light behavior. Share only genuinely public/common images; GM-specific variants remain private. Do not label all web or Unity clients compatible because a desktop decoder opened the file.

### Tiled, LDtk and Dungeondraft — metadata makes art useful

Tiled describes external tilesets and image references, offsets and template instances; its changelog demonstrates schema evolution. LDtk publishes versioned JSON documentation and deprecation guidance. The Dungeondraft API exposes its existing tool/world/exporter boundaries, while EightBitz's original tooling documents pack and tag creation and explicitly distinguishes compressed disk bytes from decoded memory. [A10](#a10) [A13](#a13) [A24](#a24) [A11](#a11)

**For us:** a tree's image, usable size, anchor, collision/sight policy, categories, variants and placed instance are not interchangeable. Keep display names separate from IDs and transport paths. Changing a file path or rebuilding an atlas must not change the logical identity of every placed object. An asset importer should extend native documents through existing contracts.

### Dungeon Alchemist and TaleSpire — 3D adds preparation obligations

Dungeon Alchemist's Treasury update introduced configurable imported 3D models and Workshop sharing. TaleSpire's FAQ describes TaleWeaverLite for Unity-compatible mini models and mod.io distribution, while broader asset-import categories are phrased as future intentions. Those future statements are not counted as shipped coverage here. [A14](#a14) [A15](#a15)

**For us:** a future 3D branch needs scale/pivot, materials, geometry/texture budgets, dependency review and platform testing. Do not require 3D assets to finish the 2D map library. A reusable scene assembly and a raw 3D mesh have different compatibility and rights requirements.

### Wonderdraft — owning a map result does not imply raw-pack rights

The reviewed vendor pack license allows specified use in derived works but restricts redistributing the underlying items on their own. That illustrates the distinction; it does not determine rights to our supplied sheets or every third-party pack. [A16](#a16)

**For us:** store evidence for private authoring, table delivery, flattened output, editing, commercial output, attribution and raw redistribution separately. A JPEG sheet supplied for review does not by itself establish permission to ship individual sprites in a subscription app.

## Asset 4. Formats are different layers of the system

The following are candidate policies, not a claim that UHT28 currently imports all these formats. Preserve a verified original independently of its delivery variant. Supported import should be a deliberately bounded list, expanded after relevant tests.

| Layer / material | Candidate source or exchange | Candidate delivery | What must be preserved or tested |
| --- | --- | --- | --- |
| Finished opaque map or photographic texture | Original image; lossless master if available | Existing JPEG or measured WebP; AVIF only after target testing | Detail/labels, color, decode time and map calibration; avoid lossy generation chains |
| Isolated illustrated prop or top-down token | Transparent PNG or reviewed lossless source | PNG or measured alpha-capable WebP | Edge halos, semi-transparency, hidden color, rotation, anchor and actual footprint |
| Terrain/material set | Source tiles and material metadata | Small repeatable textures, several compatible variants | Seam/padding, world-space scale, blend boundaries and zoom stability |
| Symbols and labels | Trusted/sanitized SVG, text and licensed font references | Vector where supported; raster fallback | Secure processing, font availability, legibility and print behavior [A22](#a22) |
| Sprite sheets / texture atlases | Sheet plus explicit rectangles, padding and anchors | Bounded atlas or isolated sprites according to workload | No baked background, trim offset, mip bleed, private/public partition and rebuild mappings |
| Native map/scene document | Existing Multiversal JSON document and extensions | Native records plus referenced pack/rendition identities | Geometry, stable IDs, source revisions, units, floors and per-instance overrides |
| Installable art pack | Versioned manifest plus content/dependencies in a bounded archive | Optional installed content, not core HTML growth | Integrity, rights, compatibility, interrupted installation and last-good rollback |
| Portable project backup | Native records plus dependency closure and rights report | File/bundle prepared explicitly for backup | Restore on an empty device, missing assets and original document compatibility |
| VTT handoff | Recipient-supported raster plus UVTT where supported | Named receiving-tool profile | Origin, units, wall/door/light translation and private-data exclusion |
| Editable architectural assembly | Native grouped objects and relationship metadata | Referenced reusable definition with instance overrides | Doors/roof parts remain editable; structural changes do not silently alter mechanics |
| Animated map, effect or token | Original clip/frames and timing metadata | Verified WebM/MP4 profile and static poster/fallback | Container versus codec, alpha, frame cost, user pause/reduced-motion and no unwanted audio [A01](#a01) |
| Sound/music/ambience | Highest-quality permitted original plus loop/cue metadata | Existing audio owner chooses measured Ogg/Opus, AAC/MP3 or other target fallback | License, looping, decoding, volume and offline permissions; no new audio engine in Map Maker |
| 3D mesh/material/mini | Original project plus selected interchange such as glTF/GLB | Runtime-specific build only if selected | Geometry, textures, extensions, scale and dependency closure; GLB may still reference external files [A21](#a21) |
| GPU texture representation | Verified source plus build recipe | KTX2 or native runtime compression only where supported | Format/device support, levels, alpha/color accuracy and transcoding cost [A19](#a19) |

A `.zip` is a transport container, a `.json` is a record encoding, and `.png/.webp` are image encodings. None alone specifies permissions, editable relationships or the full restore set. Similarly, a familiar `.mp4` extension does not identify a single codec profile. Our pack format should be a small versioned contract over existing owners, not an attempt to replace every media standard.

A compact image is normally decoded before ordinary canvas use. GPU block-compressed textures solve a different runtime problem from JPEG/WebP transfer compression. KTX2 defines texture formats, levels and supercompression; using it needs a capable renderer path. It is a later measured option, not a drop-in `<img>` replacement. [A19](#a19)

## Asset 5. Fresh audit of our supplied sheets and app

The new bounded audit verifies all 22 sheet hashes against the prior receipt, decodes their dimensions, and performs one WebP quality-75/method-4 trial in memory. Originals and the app were not modified. Tools: Python 3.12.14, Pillow 13.0.0, libwebp 1.6.0, Linux x86_64. These are local codec measurements, not MacBook Air, Windows, Android or WebGL performance results.

| Quantity | Result | Interpretation |
| --- | --- | --- |
| Current delivered UHT28 HTML | 58,687,922 bytes; approximately 55.97 MiB | Bundled app/test payload, not the size of these sheets alone |
| Original 22 JPEGs | 4,998,320 bytes; approximately 4.77 MiB | Existing encoded source size |
| Estimated RGBA8 for all sheets | 108,968,192 bytes; approximately 103.92 MiB | Arithmetic pixel storage; excludes decoder, canvases, GPU copies and other overhead |
| Largest single RGBA8 sheet | 8,238,604 bytes; approximately 7.86 MiB | Supports bounded review; no need to decode the entire library to browse |
| Prior quality-85 WebP trial | 5,357,212 bytes; approximately 5.11 MiB | Larger than originals; retained counterexample to automatic conversion |
| New quality-75 WebP trial | 3,985,730 bytes; approximately 3.80 MiB | 20.26% smaller in total; all 22 smaller, with additional lossy compression |
| New PSNR versus decoded JPEG | 34.141–37.939 dB across sheets | Numeric error against an already-lossy source, not artistic acceptance or original quality |
| Base64 text for separate original payloads | 6,664,452 characters before prefixes | About one-third expansion before any outer compression; runtime strings/decodes can add other costs |
| Transparency in supplied originals | None of the 22 has an alpha channel | The sheets are review/reference material, not finished transparent placement sprites |

The correct conclusion is **conditional transcoding plus source preservation**, not “quality 75 is approved.” Before shipping it, inspect at normal and close zoom, test actual client decode and compare translucent art on light/dark backgrounds. Numeric quality settings are not interchangeable between formats or encoders. A JPEG converted to lossless storage cannot recover detail already removed by JPEG.

The existing reviewer limits active sheet decoding and records readiness/provenance. It does not provide installed packs, alpha-cut sprites, persistent placed objects or rights clearance. Each useful sprite still needs reviewed extraction, clean transparency, scale, anchor, orientation, tags and identity. Do not infer individual object count from the number of decorative items visible on a contact sheet.

The prior core-size audit scoped literal raster data URLs in the decoded map payload; it did not measure every role's escaped payload or live cache. Its numbers must not be presented as an exhaustive app-deduplication result. The current baseline hash remains `ab66ac31aeacec06b3a78db9e4689532774c0a7d21b6ecd957f1367ce43eb9d2`.

## Asset 6. Size, memory and rendering strategy

An 8192×8192 RGBA8 image alone needs 256 MiB for one full pixel buffer, whatever its compressed download size. A complete ordinary mip chain approaches another one-third for large power-of-two textures. Intermediate render targets, retained CPU pixels, undo snapshots, export surfaces, atlas copies and video frames can add more. These are arithmetic examples, not measured allocations in our app.

**Proposed policies:**

- Browse an indexed, virtualized catalog using small thumbnails; do not decode source masters for search results.
- Load a screen-appropriate rendition for play and a higher-resolution rendition for explicit close editing or export. Preserve the original footprint and native geometry.
- Use view/scene culling and layered caches only when invalidation is correct. A cached roof must refresh after an attached wall edit.
- Separate packed draw efficiency from residency. A huge atlas can reduce draw overhead while retaining many unused pixels. Partition by use and audience, cap texture dimensions and preserve padding/trim metadata.
- Reuse identical textures for repeated placements; keep position, scale, tint and variant choices as lightweight editable instance records.
- Release inactive canvases, images, event subscriptions and texture handles. Measure repeated scene switches for growth rather than relying on a single successful load.
- Give high-resolution export a bounded job with progress/cancel and a safe failure path. Tiling or banded rendering must overlap/filter correctly and respect renderer limits; it is not automatically seam-free.

Unity Addressables documents reference-counted resource use and notes that releasing one asset need not free its memory while the containing bundle remains in use. Its update workflow also distinguishes incremental content updates from full re-downloads and requires retained platform/release build state. These mechanisms should be compared with our actual installed runtime before adoption; the standalone HTML and installed app need separate adapters behind shared asset semantics. [A17](#a17) [A18](#a18)

## Asset 7. Storage, offline use, backup and updates

| Store | Purpose | Durability and removal policy we should implement |
| --- | --- | --- |
| Original sources | Preserve accepted source bytes and provenance | Durable; never treat as ordinary evictable cache |
| Logical registry | Identity, rights, names, tags, source lineage and availability | Durable; a content hash does not replace this record |
| Derivatives | Known recipe outputs for a target/purpose | Rebuildable if original, recipe and rights remain available; otherwise retention must be explicit |
| Pack installations | Verified manifest and required content | Atomic activation, pins, rollback and dependency checks |
| Browser/download cache | Accelerate access to permitted content | Evictable and replaceable; quota failure cannot corrupt durable state |
| Decoded/GPU cache | Keep active render resources | Bounded lifetime and measured high-water mark, independent of disk cache |
| Map/scene saves | Authored structure and instance references | Native document persists without copying each source image |
| Portable backup | Restore records and required permitted dependencies | Explicit included/missing inventory; validate on an empty profile |
| Snapshot/history | Recover prior project revisions | Pins protect referenced dependencies until retention/removal policy permits deletion |

Mozilla documents best-effort storage, persistent-storage requests and quota exceptions; permission is not guaranteed and private browsing behaves differently. Browser storage therefore needs explicit failure handling and backup. A request for persistence is useful but does not turn a local browser profile into a second durable copy. File-origin and embedded-frame behavior require direct tests in our distribution configuration. [A20](#a20)

**Pack lifecycle proposal:** install to staging, validate manifest and dependencies, verify full content hashes, then activate one new manifest pointer. Keep the last verified version until dependent maps can resolve the new version or the user explicitly accepts a migration. Cancel/retry must be safe. Differentiate uninstall, clear disposable cache, delete project and remove original source. Garbage collection should trace current documents, history, backups and offline pins; it must not delete referenced bytes because an item was removed from the current scene.

For updates, pin asset/pack versions in saved maps and record migrations rather than silently substituting a newer illustration. Avoid making one changed thumbnail trigger a giant pack download. Very small files can be grouped for transfer; very large bundles can amplify updates and memory residency. Choose grouping after real access/update measurements. Preserve exact installed-version recovery where rights permit.

A portable project should choose between linked references, a permitted dependency bundle, and a flattened output. It should preview what is included, unavailable or nonredistributable. Raw originals and GM-private material must not accidentally travel in an ordinary player map export. A `.mapforge.json` migration remains a reviewed adapter that creates a native copy; it must not replace the native document system.

## Asset 8. Safe ingest, privacy, rights and distribution

OWASP's upload guidance covers content/type validation, permissions, storage and decompressed limits. W3C SVG defines processing modes with different script and external-resource behavior. We should support a declared safe vector subset or rasterize a validated source rather than place arbitrary uploaded markup into the application DOM. Decoder safety remains necessary even when re-encoding. [A23](#a23) [A22](#a22)

For our asset packs, proposed checks include compressed bytes, entry count, normalized paths, path traversal, case collisions, duplicate names, uncompressed expansion, image dimensions/pixels, animation frame count/duration, nested archives and parser time/memory. Reject scripts and remote-reference fetches unless a separately designed trusted extension capability explicitly allows them. Integrity hashes detect byte changes; trust and authorization require separate decisions.

**Privacy extends beyond the visible canvas.** An unrevealed room's thumbnail, asset filename, pack tag, search count, cached texture or download URL can disclose information. Player projections should contain only authorized dependencies and metadata. Do not put private and public art into the same downloaded atlas. A GM-only overlay drawn over a publicly downloaded secret map is not evidence that the underlying map is confidential.

Keep blob deduplication separate from logical ownership. Identical bytes can have different licenses, audiences and campaign rights. Never deduplicate user-facing records merely because their hashes match; do not expose “already exists” responses across unauthorized accounts. A warm cache must re-enter the appropriate access decision when the logical asset is used in a new context.

Reuse existing identity/admission, ARI and GATE entitlement/offline controls. This study does not create an asset-specific subscription system. Authorized offline access needs explicit pin/expiry/reconciliation behavior; it cannot promise to revoke already exported or captured material. Removing a catalog entry, expiring a delivery URL, invalidating a cache and legally deleting retained copies are separate operations.

For supplied or commissioned art, capture creator, source file, source hash, acquisition/license evidence, permitted uses, attribution, modifications and derivative lineage. Preserve rights metadata even if an image's public derivative strips private EXIF or other unneeded metadata. Free download, purchase, inclusion in a repository and an app's code license are not interchangeable evidence of asset-distribution rights.

## Asset 9. Asset UX and quality are part of the pipeline

The library should answer practical questions: What is this? What scale/style is it? Is it installed? Can I use or export it here? Where is it used? What will an update change? What happens if it disappears? Surface the common answers at placement time; keep long provenance details in the inspector.

Recommended metadata includes semantic category, style/theme/genre, intended scale, orientation, pivot/anchor, visual bounds versus placement footprint, layering, roof/wall/door attachment roles, color/alpha space, shadow/light policy, animation/audio behavior, dependencies, variants and license evidence. A path in a folder is not enough. Some metadata belongs to a reusable definition and some to an individual placement.

Preview the actual candidate at a useful map scale, permit seeded variant selection, and make results editable. Regeneration must respect pinned authored placements and exclusion masks. A library can contain many files yet still lack the parts needed for a coherent district or room. Evaluate coverage by complete scene requirements and composition quality, with consistent before/after geometry and zoom.

Use small style packs spanning matching materials, trees, architecture, interiors, clutter and labels. Distinguish a decorative cast shadow from a sight blocker, roof occlusion or legal movement constraint. Specialized ship/mecha/base/cave/non-Euclidean scenes should consume the same asset identity model while retaining their own spatial requirements; gameplay simulation stays with its established owner.

## Asset 10. Costs, evidence gaps and acceptance

Do not choose a storage vendor from the JPEG total alone. A provider-neutral estimate should count unique originals, materialized derivatives, installed packs, catalog/previews, replicas, backups and retained revisions. Keep device caches outside server-storage totals. Estimate transfer by actual recipient count, cold-cache rate, scene changes and revoked/replaced content, and record processing jobs, object requests, backup/restore traffic and support burden.

A useful model is `stored bytes = retained unique originals + retained derivatives + metadata + backups + replicas`. The terms must be non-overlapping: define whether replicas already include originals before summing. A corresponding delivery model counts bytes actually sent to each authorized client after cache reuse. These are planning identities, not cost quotes. We have no measured user workload, provider bill or production CDN evidence in this cycle.

The new codec audit does not establish GPU residency, mobile decode, network interruption recovery, rights enforcement or aesthetic acceptance. DAMC's larger synthetic model does not close those gaps either. Before shipping, run the relevant boundary tests with real native saves, actual storage, authenticated clients and target devices. [A28](#a28)

**New asset acceptance scenarios:**

| ID | Scenario | Required observation |
| --- | --- | --- |
| A-T01 | Import a sheet and prepare isolated sprites | Original retained; alpha/edges/scale/anchor accepted; each sprite has stable identity |
| A-T02 | Import malformed, huge or hostile pack fixtures | Bounded rejection, no path escape, no active content and no partial ready state |
| A-T03 | Browse a large library and place repeated objects | Thumbnails/indexes suffice; placements share art while overrides remain independent |
| A-T04 | Update a pack used by old maps | Existing version resolves or an explicit migration/repair is offered; rollback works |
| A-T05 | Interrupt install and fill storage | Last-good pack/save survives; cancellation and quota failure are clear |
| A-T06 | Clear caches with documents/history/offline pins present | Rebuildable data removed; referenced durable content preserved |
| A-T07 | Restore on an empty profile/device | Dependency closure succeeds or reports missing/rights-restricted items precisely |
| A-T08 | Deliver public and GM-private variants to two clients | Wrong audience gets no private metadata, thumbnail, URL, atlas or cached content |
| A-T09 | Revoke access or change campaign rights | Existing entitlement policy applied at real delivery/cache boundary; residual offline/export limits stated |
| A-T10 | Compare codecs and transparent edges | Actual target quality/decode/memory results, not extension-based approval |
| A-T11 | Repeat scene/floor switches and a long session | Decode/GPU resources settle under measured budgets; no monotonic resource growth |
| A-T12 | Export high-resolution/portable/UVTT profiles | Correct recipient result, dependencies, scale and light policy; safe cancel/failure |

The plan below maps all earlier R01–R12 and C01–C12 recommendations into concrete steps, retains T01–T12 and J01–J16, and adds A-T01–A-T12. It covers the map rendering/composition roadmap and the workflow, asset and VTT foundations revealed by the combined research. It does not claim that every MME feature is still absent: local implementations and open acceptance gaps remain separate.

## Gap plan — 24 ordered steps

All steps are planned and not selected for execution. Dependencies define readiness, not a second OPS5 selector. Product-scoped steps keep existing identity, session, ARI, GATE, PCV and domain authority. Steps whose prerequisites are ready can be prepared independently; numeric order is the recommended default, not a forced serialization of independent work.

| Step | Deliverable | Depends on | Completion evidence | Existing owner / scope |
| --- | --- | --- | --- | --- |
| **MVAC-01 — Freeze representative fixtures and measurable gap baseline** | One versioned regional, settlement, interior, cave, tactical, ship and non-Euclidean fixture set; exact native/render/role baselines and device matrix. | Baseline | Fixture IDs/hashes, expected secrets and dependency failures recorded; current UHT28 kept intact; real-browser and physical-device evidence gaps explicit. | MMHT/UHT; GM-00; existing validation owners; standalone planning |
| **MVAC-02 — Define shared spatial and media integration contracts** | Map/scene/asset/blob/representation/instance/rights separation, units/origins, revisions, update and failure contracts; map extensions rather than replacement docs. | MVAC-01 | Trace one door, tree, NPC token and GM handout through create/save/prep/play/export/recovery without duplicate owners; missing/stale/incompatible states specified. | Native Map Maker; ARI/PCA; A5/A6/A7/D17; account/session owners; shared design |
| **MVAC-03 — Build one Author / Prepare / Play interaction shell** | Canvas-first context shell, stable tool options and selected-object inspector, visible role and scene revision; minimal player controls. | MVAC-01, MVAC-02 | J01/J03/J10 observed in an executable prototype; no hidden mode changes, role switch described as local preview until authenticated. | MME-01/UHT-09; UI and scene presentation owners; standalone prototype |
| **MVAC-04 — Unify selection, tools, shortcuts, undo and checkpoints** | Predictable tool lifecycle, overlap selection/lock/isolate, focus-scoped shortcuts, compound edit undo and named author checkpoints. | MVAC-03 | J03/J10/J11; text undo/Escape never edits map beneath dialog; cancel preserves source; author undo cannot roll back accepted gameplay events. | Native editor command/history; campaign event owner; standalone prototype |
| **MVAC-05 — Establish asset provenance and rights capabilities** | Per-asset creator/source/license evidence and separate private use, session delivery, flattened-map output, raw redistribution, modification and attribution capabilities. | MVAC-02 | Unknown license remains unknown; synthetic fixtures prove rights decisions; no asset hash, purchase or exported map permission treated as pack-redistribution permission. | Existing ARI/OCS/PCA; GATE/MCB for entitlement and commercial decisions; shared design |
| **MVAC-06 — Specify versioned asset and pack manifests** | Stable logical asset IDs, immutable rendition digests, pack/version dependencies, recipe version, scale, anchor, orientation, alpha, tags and source license refs. | MVAC-02, MVAC-05 | Two logical records can share bytes without merging rights; one version update cannot silently alter existing placement; unknown mandatory features reject clearly. | Existing ARI and native document extensibility; standalone adapter |
| **MVAC-07 — Implement bounded, transactional ingestion** | Content validation, byte/dimension/frame/decoded-pixel limits, archive path/expansion limits, safe vector subset, staging, cancel and atomic registration. | MVAC-05, MVAC-06 | Reject traversal, duplicate-path, oversized-decode, malformed media and unsupported active content; interrupted import exposes no half-ready pack; originals preserved. | Existing media intake/ARI/PCA; standalone adapter |
| **MVAC-08 — Prepare one coherent illustrated asset family** | Small settlement/interior/vegetation sample with reviewed crop/alpha, scale/anchor, pivot, palette, shadow policy, tile edges and source lineage. | MVAC-05, MVAC-06, MVAC-07 | Before/after same-geometry scenes at multiple zooms; no white-box JPEG placement; edge halos and door/roof orientation checked; creator review distinct from automated metrics. | MME-02E2 / approved art-production owner; standalone artwork |
| **MVAC-09 — Build measured renditions and color/alpha pipeline** | Preserved source plus browser/play/thumbnail/print variants with explicit color, alpha, recipe and target profile; JPEG/WebP/PNG trials before AVIF/KTX2 adoption. | MVAC-07, MVAC-08 | Actual sample quality and target decode tested; no upsizing by default; opaque and translucent cases; black/white backgrounds, seam and repeated-edit checks; larger conversions retain source fallback. | Existing renderer/media transform owner; standalone adapter |
| **MVAC-10 — Build usable asset discovery and editable placements** | Virtualized search/tag/style/scale library with cheap previews, recent/favorite sets, multi-placement and per-instance overrides/assemblies. | MVAC-03, MVAC-06, MVAC-08, MVAC-09 | Find and place within dense sample library without decoding all originals; edit one instance without changing others; missing pack and provenance visible. | MME-03; ARI query/pagination and native placed-object owner; standalone prototype |
| **MVAC-11 — Implement optional packs and crash-safe activation** | Small built-in set, local optional packs, dependency resolver, verified staging, atomic activation, rollback, pin/uninstall and last-good manifest. | MVAC-06, MVAC-07, MVAC-09 | Interrupt download/write/verification/activation; every restart gives prior or new complete pack; required pinned content survives cache trim; offline availability is explicit. | Existing installer/offline/ARI owners; standalone adapter |
| **MVAC-12 — Separate durable storage, caches and garbage collection** | Original/derivative storage and indexes; measured quotas; decoded/GPU lifetimes; safe eviction; retained references/checkpoints/offline pins; tombstones and repair. | MVAC-06, MVAC-11 | Low disk/quota denial leaves last valid document; eviction can rebuild disposable data; no deletion of referenced originals; clear-cache differs from delete-project; cross-tenant logical rights preserved. | Existing local store/media storage; ARI; shared design and adapter |
| **MVAC-13 — Prove portable save, backup, restore and legacy migration** | Linked-save versus portable-bundle choices, dependency-closure report, license-aware inclusion, safe restore and copy-based reviewed legacy import. | MVAC-04, MVAC-06, MVAC-11, MVAC-12 | Restore on an empty profile without source folders; missing/nonredistributable dependencies explicit; repeated restore safe; legacy file unchanged and native IDs preserved where appropriate. | Native document/recovery owners; legacy .mapforge adapter; standalone adapter |
| **MVAC-14 — Finish editable roads, rooms, roofs, walls and doors** | Relationship-aware joins and architectural assemblies, linked door openings, roof/wall art and boundary editing; general road joins beyond consecutive rendering runs. | MVAC-02, MVAC-04, MVAC-08 | Crossing/branching/nonconsecutive roads merge visually without closing bridges; room edits preserve or explicitly invalidate attached doors/blockers; geometry and gameplay remain distinct. | Native Map Maker structural/spatial owner; standalone map |
| **MVAC-15 — Finish editable procedural composition and selective regeneration** | Seeded biome/district-aware placement, exclusions, assemblies and regenerate-selected controls for regional, city, cave, interior and specialty fixtures. | MVAC-06, MVAC-10, MVAC-14 | Pinned edits survive regeneration; same seed+recipe deterministic; all placed results editable; clearance and district composition improve without adding gameplay simulation. | MME-02E0/E3; procedural and specialty spatial owners; standalone map |
| **MVAC-16 — Unify materials, depth, shadows, labels and style packs** | Coherent natural/manufactured materials, zoom-stable details, shared art direction, structural shadows/atmosphere and readable genre labels. | MVAC-08, MVAC-09, MVAC-14, MVAC-15 | Same regional/settlement/interior/tactical geometry compared before/after at fixed zooms; removable grid and source geometry preserved; decorative lighting changes no sight authority. | Existing renderer/presentation owners; standalone renderer |
| **MVAC-17 — Qualify map exports and receiving-tool imports** | Player/GM raster, gridless/transparent-grid, print/high-resolution and UVTT profiles with units/origin/floor/door/light policy and warnings. | MVAC-09, MVAC-13, MVAC-14, MVAC-16 | J15 in named actual receiving versions; distances and portals match; private data excluded; no duplicate baked/dynamic lighting; bounded/cancellable export fails safely on large maps. | MME-06 exporter; recipient VTT adapter owners; standalone interoperability |
| **MVAC-18 — Bind authenticated users, ownership and private projections** | Role and document/action policy enforced before delivery; current scene revision and per-character projection; private asset metadata excluded. | MVAC-02, MVAC-06 | Actual GM plus two authenticated clients; hidden actor/trigger/thumbnail/search/count/URL payload not delivered; forged role/view flags grant nothing. | Existing PCV-03F identity/admission/session owners; A5; GATE where applicable; product integration gated |
| **MVAC-19 — Connect authoritative actions and scene state** | Movement/door/trigger/loot requests with action IDs, revisions, owner validation, rejection explanations and accepted event projection. | MVAC-14, MVAC-18 | J05/J09/J11; duplicate or reordered requests produce one accepted effect; no second combat/inventory ledger in renderer; prepared scenes cannot execute live actions. | Existing A5/A6/A7/D17 owners; PCV-04/06 sequence; product integration gated |
| **MVAC-20 — Qualify reconnect, floors, transitions and session recovery** | Resync protocol, expected/pending/accepted state, floor/portal transitions, asset-ready handshake and last accepted checkpoint. | MVAC-13, MVAC-18, MVAC-19 | J07/J08/J09/J12/J16 with transport/process failures; no phantom connection, duplicate travel, leaked destination or unexplained state loss. | Existing session/scene/travel/MTLC owners; product integration gated |
| **MVAC-21 — Qualify authorized media delivery and offline access** | Audience-scoped asset/dependency manifests, secure fetch/cache keys, warm-scene preload, cancellation, entitlement/offline policy and original export controls. | MVAC-05, MVAC-11, MVAC-12, MVAC-18 | Two-client wrong-user/expired/revoked/private-preview tests at actual storage/network boundary; shared bytes do not share rights; existing authorized offline behavior retained; no claim of clawing back exported files. | Existing ARI/identity/GATE allowance/offline owners; provider only if selected; product integration gated |
| **MVAC-22 — Establish performance, storage and cost acceptance budgets** | Cold/warm workload matrix for editor and live clients; bytes/CPU/decode/GPU/cache/export limits; measured provider-neutral storage/egress/ops model. | MVAC-10, MVAC-12, MVAC-16, MVAC-17 | Actual lower-powered Windows/Android targets plus specified browser; decoded high-water and scene-switch release traced; no desktop-Node benchmark substituted; observations determine budgets. | MME-02D3/MME-06; renderer/media/performance owners; cross-boundary validation |
| **MVAC-23 — Integrate accepted behavior into installed app contracts** | Per-feature source crosswalk and platform adapters; reuse project runtime asset manager; evaluate Unity Addressables only against actual installed stack. | MVAC-13, MVAC-17, MVAC-20, MVAC-21, MVAC-22 | Installed builds save/load native docs and resolve approved dependencies; no duplicate catalog/renderer/domain owner; content update/rollback parity on supported platforms. | Existing PCV-04..10/MTLC/ARI/media/runtime owners; product integration gated |
| **MVAC-24 — Run full workflow acceptance and resolve remaining gaps** | Observed author/GM/player journey, complete multi-scene session, failure/recovery suite, creator visual review and final evidence matrix. | MVAC-04, MVAC-15, MVAC-17, MVAC-20, MVAC-21, MVAC-22, MVAC-23 | All retained T01..12/J01..16 plus asset negatives pass at their real boundary or remain explicitly open; next-step status reconciled; owner review separate from automated success. | Existing GM/UHT/PCV-10/MTLC acceptance owners; independent/user validation |

## Integrated gap coverage and execution boundary

| Gap family | Existing evidence / limitation | Planned steps |
| --- | --- | --- |
| Canvas-first workflow and predictable editing | Local dock and editor code exist; observed browser/novice acceptance remains open | MVAC-01–04 |
| Rich assets without uncontrolled application growth | 22-sheet reviewer and bounded codec audits; no finished sprite/install library | MVAC-05–13 |
| Natural composition and architectural coherence | Existing MME structures/materials/composition; general relationship editing and complete artistic acceptance open | MVAC-08–10, 14–16 |
| Procedural and specialty maps | Existing source-owned spatial examples; consistent generation/editability and accepted workflows open | MVAC-14–16, 20 |
| Export, grid/zoom, print and interoperability | Local adapters/receipts; actual receiving-tool and physical-device acceptance open | MVAC-09, 16–17, 22 |
| Trustworthy live VTT | Local rehearsal/proposals; real auth, audience delivery and session continuity not established by UHT28 | MVAC-18–21 |
| Installed convergence and final acceptance | Existing product owners and prerequisites remain controlling | MVAC-22–24 |

The machine-readable backlog maps every retained R01–R12 and C01–C12 recommendation to at least one step. It preserves the 12 map tasks, 16 joint scenarios and adds 12 asset scenarios. This records requirements and dependencies, not 24 completed features. Independent ready tasks can proceed without inventing a rigid waterfall.

**Next bounded execution candidate:** MVAC-01, the representative fixture and acceptance baseline, followed by MVAC-02's shared contracts and the MVAC-03/04 interaction prototype. The research audit already provides exact source hashes; do not repeat it as busywork. The next cycle should add executable/observed workflow evidence and settle the concrete media/spatial contract. Product integration uses separately selected existing owners and prerequisites.

## Retained map-maker and VTT studies

The sections below preserve the earlier historical investigation, UHT28 evaluation and source identifiers. Their recommendations are inputs to MVAC, not competing OPS5 selectors. They remain documentary/source evidence and do not become runtime acceptance because they are included in a larger report.

## Map 1. Findings that should change our direction

For map authoring, our next design priority should be **a coherent editing workflow**. We have already invested in native map documents, structural artwork, materials, composition, lighting and export. The highest-value next question is whether someone can predictably build, revise, recover and deliver a useful map using those capabilities.

Across the sources, I found repeated responses to accumulated complexity: context-sensitive controls, stronger object and layer models, reusable definitions, safer regeneration, and clearer recovery. These responses appeared at different times in different products. This is a set of branching traditions, not a universal sequence in which every newer tool is better.

Three findings matter especially for Multiversal:

- **UI consolidation often follows feature accumulation.** Tiled unified overlapping terrain tools; LDtk replaced a confusing compact mode; Inkarnate reworked layers and contextual controls. The common lesson is to manage the user's mental model as features grow. [S07](#s07) [S13](#s13) [S20](#s20)
- **Authoring intent and rendered appearance benefit from separate representations.** Tiled's blueprint-driven Automapping and LDtk's IntGrid-driven auto-layers are concrete examples. We can apply this principle to native roads, rooms, boundaries and decorative artwork while retaining our document system. [S08](#s08) [S12](#s12)
- **A beautiful result must remain editable and recoverable.** Watabou documents the limits of mesh-based editing; Inkarnate distinguishes autosave from named snapshots; ProFantasy documents an art-development process that begins with a sample map. These are more useful lessons than copying a toolbar's appearance. [S27](#s27) [S22](#s22) [S02](#s02)

These are research conclusions, not proof that our proposed changes will improve task times. The evaluation below identifies what we can preserve, what needs a prototype, and what needs observation.

## Map 2. Method, evidence and limits

The study uses 36 source records across 12 product families: Campaign Cartographer, Tiled, LDtk, Dungeon Scrawl, Inkarnate, Azgaar's Fantasy Map Generator, Watabou's generators, Dungeondraft, Wonderdraft, Dungeon Alchemist, TrenchBroom and MapTool. Watabou's related generators count as one family; the Interactive Atlas is considered alongside Campaign Cartographer.

The source set favors developer journals, dated release notes, official manuals and original repositories. Two Tiled source files were spot-checked for tool lifecycle and command-history design. License identities were checked for selected repositories. This is not a full source-code audit, a legal compatibility opinion, or a hands-on test of every competing editor.

Evidence labels used here:

| Label | Meaning | What it does not establish |
| --- | --- | --- |
| Developer account | The maker describes a problem, change or tradeoff | That the change improved every user's experience |
| Documentation | A workflow or capability is described in official material | Its speed, polish or reliability on our hardware |
| Source spot-check | A particular implementation mechanism was inspected | Whole-program architecture or production fitness |
| Local inspection | Code or packaged evidence exists in UHT28 | Installed app parity or a successful novice workflow |
| Inference / proposal | My interpretation or recommended design | A shipped feature or accepted product decision |

Publication dates, version labels and live documentation are kept separate. A 2026 retrospective does not make the Interactive Atlas a 2026 invention. Historical LDtk documentation and newer release notes differ; this is useful evidence of evolution, not permission to combine every page into an imaginary single version. Prices and market-share rankings are outside scope.

The originally linked Dungeon Scrawl V2 rationale article could not be retrieved. The accessible developer announcement supports a rebuild and temporary feature-parity gap; it does not justify invented details about the internal rewrite. Several legacy ProFantasy help URLs failed, so the historical PDF and developer journals carry the corresponding claims. The current Wonderdraft page supports its asset-pack approach but provides weak evidence for historical UI changes. These gaps remain explicit.

## Map 3. A dated evolution map

The following chronology samples documented changes. It is not a claim about the first-ever invention of each feature.

| Period / date | Documented example | Feature or interface shift | Relevance to us |
| --- | --- | --- | --- |
| 1993, recalled in 2013 | Campaign Cartographer adapted FastCAD for roleplaying maps [S01](#s01) | General spatial precision becomes a domain-specific toolset | Use a robust spatial core with map-oriented actions |
| 2014 | ProFantasy's style-development journal [S02](#s02) | A sample map precedes a coherent family of art, tools and effects | Validate a complete scene before mass asset production |
| 2015 tutorial artifact | CC3+ effects dialogs and unit choices [S03](#s03) | Layered appearance with explicit map/view scale semantics | Make scale, shadow and export units visible |
| 2017-03-30 | Azgaar's initial journal [S23](#s23) | Interactive plausible geography balanced against speed | Generation quality has interaction and latency constraints |
| 2017-05-24 | Tiled 1.0 [S05](#s05) | External tilesets and hierarchical layers | Shared resources and organization require editor support |
| 2017-06-01 | Watabou's early devlog [S26](#s26) | Contextual ward labels, touch hints; iframe obstructs permalinks | Embedding can break otherwise sound interaction assumptions |
| 2018-01-03 | Tiled 1.1 [S06](#s06) | Sparse expanding maps, reusable templates, contextual toolbar | Workspace growth and discoverability evolve together |
| 2020-07-05 to 15 | Dungeon Scrawl 1.3 and 1.4 [S15](#s15) [S16](#s16) | Geometry robustness, image manipulation, local undo and panel space | Small interaction details are core editor functionality |
| 2021-03-23 | Tiled 1.5 [S07](#s07) | Consolidated terrain painting and clearer selection policies | Retire competing mental models as capabilities converge |
| 2022-10-15 | Dungeon Scrawl V2 [S17](#s17) | Complete rebuild; some existing features temporarily incomplete | A rewrite has migration and parity costs |
| 2022 / 2024 documentation | LDtk auto-layers and interface [S12](#s12) [S11](#s11) | Semantic input, generated visuals, definitions and instances | Reusable visual rules should not erase authored intent |
| 2024-11-26 | Watabou Village 1.6.4 [S28](#s28) | Request a crossroads through a generator tag | High-level intent can be simpler than many low-level knobs |
| 2025-12-08 | Inkarnate 2.0 [S20](#s20) | Layer-system migration, scene reuse and recovery features | Compatibility is part of UI evolution |
| 2026-02-17 | Dungeon Scrawl update [S18](#s18) | Shared texture access and separate wall light-blocking controls | Reduce artificial tool divisions; separate appearance from rules |
| 2026-07-14 | Tiled Automapping tutorial [S08](#s08) | Editable blueprints drive finished dungeon boundaries | Automate the repetitive consequences of an edit |
| 2026-09 to 11 | Scrawl export and Azgaar changelog [S19](#s19) [S25](#s25) | Better handoff, editor search, handle scaling and data-based loading | Delivery, navigation and longevity remain active engineering work |

A parallel historical thread is linked cartography. ProFantasy's participant retrospective describes an atlas with more than 800 interconnected editable maps and a separate viewer, spanning world-to-building navigation. Multi-scale linking and audience-appropriate viewing are longstanding concerns. Its exact original launch date is not established by this study. [S04](#s04)

## Map 4. The problems developers actually described

### Map 4.1 Precision and cartographic expression — Campaign Cartographer

**Documented:** ProFantasy began by adapting a CAD system. Its later art journal starts with a small map, then develops matching tools, symbols, effects and multiple resolution catalogs. The historical tutorial exposes effect parameters with different spatial units. [S01](#s01) [S02](#s02) [S03](#s03)

**Interpretation:** Detailed art succeeds as a system of compatible parts. A large folder of unrelated sprites is not the same deliverable. Precise tools also need vocabulary that makes sense to mapmakers.

**For Multiversal:** Pick one settlement and one interior style target. Review roof language, tree scale, line weight, labels and shadows together. Keep advanced geometry tools available, but expose actions such as Connect road, Attach door and Edit room boundary in the ordinary workflow.

### Map 4.2 Repeated objects and expanding projects — Tiled

**Documented:** Tiled 1.0 addressed external tileset editing and group layers. Version 1.1 added file-referenced object templates with instance overrides, a context-sensitive toolbar and sparse infinite maps. Version 1.5 combined previously overlapping Wang/Terrain tools and provided selection preferences for overlapping objects. [S05](#s05) [S06](#s06) [S07](#s07)

**Interpretation:** Growing projects need both resource organization and interaction consistency. Referencing shared resources only works well when the editor makes definitions, instances and overrides understandable.

**For Multiversal:** Preserve native placement records; add pack identity and explicit per-instance overrides. Prefer one tool's contextual options over several competing finish panels. Offer visible selection scope, lock and isolate controls rather than making users fight overlapping decorations.

### Map 4.3 Tedious boundaries — Tiled Automapping and LDtk

**Documented:** Tiled's 2026 tutorial shows the remaining burden of manually correcting wall tiles after a floor-layout edit, then derives finished walls/floors from a blueprint. LDtk similarly supports rule-driven visual layers sourced from semantic integer grids. [S08](#s08) [S12](#s12)

**Interpretation:** The valuable automation is often the predictable consequence of an authored change. Fully random generation is only one part of procedural assistance.

**For Multiversal:** Treat room extent, road path and structural relationships as source intent. Derive joins and presentation without changing the source unless the user requests an edit. Our road fix is a useful rendering correction, but it does not create road-network connectivity or a general topology solver. Make that distinction visible in engineering and validation.

### Map 4.4 Too much interface, unclear contexts — LDtk

**Documented:** LDtk's older interface documentation explains a layer-dependent palette and the distinction between global definitions and placed instances. Its 1.4.0 notes replace a described-as-confusing compact mode with Zen mode, add denser palettes, and record a macOS shortcut change. [S11](#s11) [S13](#s13)

**Interpretation:** A compact UI is not automatically a clear UI. Reveal behavior, context and familiar platform commands matter as much as pixel savings.

**For Multiversal:** Keep a stable place for the active tool's options and selected object's properties. Provide a temporary canvas-only view, a visible return control, a shortcut reference, and trackpad-friendly navigation. Do not make a hover-only sidebar essential for keyboard or touch users.

### Map 4.5 Polygon fragility and fine interaction costs — Dungeon Scrawl

**Documented:** The 1.3 devlog explicitly offered a fast solver that could produce polygon problems and a slower, more robust alternative, with undo/retry instructions. The following image-focused update added pre-placement rotation/scaling, temporary snap override, image grouping, point-level undo and a collapsible panel. [S15](#s15) [S16](#s16)

**Interpretation:** Geometry correctness and editing ergonomics must be developed together. Asking the user to recover from a geometry failure is a documented historical workaround, not a design goal we should copy.

**For Multiversal:** Validate joins, concave boundaries, near-touching paths and self-crossings. Keep malformed edits non-destructive and explain the failure. One undo should reverse one meaningful gesture; while drawing, removing the last point should be predictable and distinct from undoing a completed object.

### Map 4.6 Rewrites, parity and operational handoff — Dungeon Scrawl

**Documented:** The October 2022 announcement calls V2 a rebuild with improved controls/performance and acknowledges unfinished isometric, hex-grid and PDF features. Later releases describe a unified texture catalog, global grid hiding and UVTT export of interactive map metadata. Wall visibility and light blocking are explicitly different settings. [S17](#s17) [S18](#s18) [S19](#s19)

**Interpretation:** The need for architectural consolidation does not itself justify a full rewrite. Feature parity and saved work are real migration costs. A successful editor must also complete the handoff to play.

**For Multiversal:** Consolidate through adapters and an explicit interaction contract first. Retain native documents and the legacy import adapter. Present output fidelity and rules metadata clearly. Our decorated interior UVTT route has source-level alignment checks; receiving-VTT import is still an open acceptance task.

### Map 4.7 Mature layer systems and safe change — Inkarnate

**Documented:** Inkarnate 2.0 introduced custom layers, scene stamps, autosave and an updated brush workflow, with per-scene opt-in for existing maps. Its current overview describes stable workspace zones and context-dependent tool settings. Current recovery documentation differentiates snapshots from latest-state recovery and says loading a snapshot creates a clone. [S20](#s20) [S21](#s21) [S22](#s22)

**Interpretation:** Discoverability and reversible migration are part of the feature, not documentation extras. The fact that a control exists does not tell a user what state is safe.

**For Multiversal:** Separate Save status, Undo history, Restore snapshot and Export copy. Keep migrations reversible. Present art layers, structural identity, visibility and audience permission as distinguishable properties. A global command search can complement stable visible controls, not replace them.

### Map 4.8 Plausibility, preservation and longevity — Azgaar

**Documented:** Azgaar's 2017 journal prioritizes plausible interactive maps and fast dragging/generation while deferring expensive automatic labeling. Current heightmap docs distinguish destructive regeneration from preserving edits, including limits on coast changes. The 2026 changelog records search, fixed-size edit handles, editor-reference cleanup and loading maps from data rather than depending on stored SVG. [S23](#s23) [S24](#s24) [S25](#s25)

**Interpretation:** Generation becomes more useful as users can preserve investments and understand consequences. Performance work also includes memory retained after a panel is closed.

**For Multiversal:** Show what selective regeneration will preserve, replace and invalidate. Pin manually edited buildings, labels and junctions. Keep semantic map data authoritative and treat render caches as disposable. Test repeated editing sessions, not only a fresh render.

### Map 4.9 Editable generation has boundaries — Watabou

**Documented:** An early devlog notes that iframe embedding blocked the intended permalink behavior. The Warp-tool journal explains that roads and rivers follow an underlying mesh: moving it edits the layout, but cannot add arbitrary roads or islands and excessive distortion can glitch. A later crossroads tag lets users request a high-level layout condition. [S26](#s26) [S27](#s27) [S28](#s28)

**Interpretation:** A coherent model enables useful editing but also defines its limits. Controls should describe those limits instead of implying that every visible mark is an unconstrained vector object.

**For Multiversal:** Provide both intent-level composition requests and direct native editing. Before adopting a generated district, show its assumptions and regeneration scope. Test embedding, downloads and focus behavior inside the actual consolidated wrapper; a standalone editor is not the same execution context.

### Map 4.10 Domain-shaped tools and asset ecosystems — Dungeondraft and Wonderdraft

**Documented:** Dungeondraft's PathTool API exposes an active unfinished path, preview/confirmation actions, width, over/under sorting, library state and an explicit light-blocking setting. Its support page discusses export and graphics problems. Wonderdraft's current site offers separate themed asset packs and symbol color variants. [S29](#s29) [S30](#s30) [S31](#s31)

**Interpretation:** A path is more than a painted stroke. Its lifecycle, spatial order and behavioral attributes need controls. Asset delivery is also part of the product system.

**For Multiversal:** A road/bridge inspector should expose width, material, elevation/plane, crossing behavior and preview before commit. Optional packs need previews, dependency identity, unavailable-asset behavior and controlled memory use. No benchmark or historical UI leadership is inferred from these product pages.

### Map 4.11 Room intent and visible results — Dungeon Alchemist

**Documented:** The official FAQ describes choosing a theme, drawing rooms, automatic furnishing/doors/windows/lighting, and editing the result before export. It describes in-house procedural generation rather than a generative-image pipeline. [S32](#s32)

**Interpretation:** Room function is a strong authoring input because it reduces several manual placement decisions at once. A generated result still needs inspectable objects and ordinary editing.

**For Multiversal:** Consider a small recipe such as Workshop or Archive with a preview, editable placements and pinned exclusions. Establish clear access paths before adding clutter. Do not turn the Map Maker into the gameplay or settlement simulation owner.

### Map 4.12 Spatial validation and play state — TrenchBroom and MapTool

**Documented:** TrenchBroom documents 2D/3D viewport choices, linked groups, editing tools, automatic backups and an issue browser. MapTool documents topology-driven visibility, lights and fog within a VTT; its proposed JavaFX refresh is a future statement on that page, not proof of a finished UI. [S33](#s33) [S34](#s34)

**Interpretation:** Spatial editors benefit from feedback about invalid content, not only attractive rendering. A VTT adds operational responsibilities beyond authoring.

**For Multiversal:** Build actionable validation messages and keep Author, Review and Present contexts explicit. Multi-deck and non-Euclidean work may benefit from linked views later, but importing a full 3D editor's controls now would add complexity without a demonstrated user need.

## Map 5. How the interfaces evolved

The recurring pattern is a change in **what the interface organizes**, not simply a change from light to dark colors.

| Interface tradition | Main organizing idea | What it makes easier | Recurring problem | Direction worth testing |
| --- | --- | --- | --- | --- |
| CAD-derived cartography | Precise entities, commands and appearance controls | Exact spatial construction and style systems | Domain terminology and many dialogs can require learning | Map-oriented actions over a precise native core [S01–S03](#s01) |
| Tile/level editors | Layers, reusable resources and object definitions | Structured reuse and engine handoff | Picking overlaps and repeated low-level decisions | Context tools, templates and semantic-to-visual rules [S05–S12](#s05) |
| Fast dungeon sketching | A few direct shapes and stamps | Immediate useful output | Boundary robustness and fine manipulation | Gesture-local feedback, predictable snapping and recovery [S15–S16](#s15) |
| Illustrated browser cartography | Art catalogs, brushes and compositing | Rich artwork without drawing each symbol | Asset/layer scale and discoverability | Shared catalog, contextual settings and reversible layer migration [S20–S22](#s20) |
| Editable generators | Seeds, parameters and constrained edits | A coherent first draft | Preserving authored changes and explaining limits | Intent controls plus previewed selective regeneration [S23–S28](#s23) |
| VTT-aware authoring | Art plus walls, portals and audience state | Delivery to play | Appearance and rules become easy to confuse | Explicit metadata overlays and audience-specific validation [S19](#s19) [S34](#s34) |

A practical inference for us is a stable workspace: navigation and document state at the top; tool families at the side; current tool options beside the canvas; selection properties in one inspector; library access with search; a clear presentation context. This is a proposed arrangement for testing, not a specification to copy from any one product.

Progressive disclosure must preserve orientation. Hide advanced options while retaining the current tool name, active plane, snap state, selected object, save state and an obvious route back. Shortcuts should have visible equivalents, respect focused text fields, and be discoverable on demand. A small laptop needs efficient use of width; touch users also need reliable target sizes and non-hover alternatives.

## Map 6. Evaluation against our current Map Maker

### Baseline and fairness

The audited artifact is **Multiversal_Consolidated_Playtest_UHT28_MME06_UVTT_Optional_Assets.html**, 58,687,922 bytes, SHA-256 **ab66ac31aeacec06b3a78db9e4689532774c0a7d21b6ecd957f1367ce43eb9d2**. The decoded map HTML and native core were inspected. This baseline is not a claim about current protected-main source, the Unity app, or installed player/GM builds.

Existing receipts are prior evidence, not new tests run for this study. The UHT28 bundle reports 82 focused checks and four-scene pixel preservation; those do not measure task completion, novice confusion, visual quality against competitors, or physical-device acceptance.

A static inventory found 549 button tags, 223 select tags, 31 dialog tags and 18 literal body-append call sites in the decoded map payload. Many are specialty controls, conditional UI or tester scaffolding; generated UI is additional. These counts establish an inventory problem to investigate. They do not mean 549 buttons are visible, or prove poor usability.

### Comparative findings

| Area | What ours demonstrably contains | Assessment and comparison | Evidence / next proof |
| --- | --- | --- | --- |
| Canvas-first workspace | MME-01 quickbar, fixed GM dock, map tools/layers and inspector toggles | **Preserve.** The foundation exists; consistency of later additions needs review | map HTML gm-mme01-style/script; compare S11, S21; observe first-open canvas |
| Tool discoverability | Several native tools plus separate material/composition/style/export modules | **Partial.** Capabilities are distributed across entry points; that is a source-backed organization concern, not a measured failure rate | module IDs and append sites; test find-and-use tasks |
| Tool and modal lifecycle | Native selection/drawing states and keyboard guards; newer dialogs have their own handlers | **Risk to test.** One central key handler enumerates many dialogs; additions can drift | core document.onkeydown near line 29947; verify shortcuts in every modal |
| Selection and overlap | Native selection, layer locks and object/vertex modes | **Present; workflow unmeasured.** Need consistent overlap picking, isolate and mixed-selection feedback | core paint/edit controls; compare S07; dense-scene task |
| Undo and recovery | commit/changeHistory, 50-entry past limit, local save status | **Present, incomplete recovery equivalence.** No evidence here of a unified named-snapshot workflow covering every art setting | core near lines 25000–25056; compare S10, S22; reload/restore tests |
| Road continuity | Two-pass same-plane road runs; editable features retained | **Useful scoped correction.** It is not a general network/topology model; interleaved runs remain a limitation | core roadSurfacePlane/paintRoadSurfaceRun; UHT27 handoff |
| Room and wall relationships | Native room/wall/opening structure and filtered UVTT boundaries | **Promising basis.** Extend predictable relationships, not independent redraw patches | native tabletopExport and nativeArtworkVTT; compare S08, S12, S29 |
| Materials and illustrated style | Layered finish, seeded detail, structural artwork, art direction and lighting modules | **Broad implementation; artistic parity unproven.** Review one coherent style family at several scales | map scripts mme02e4/mme02f/mme02g; compare S02 |
| Procedural editing | Generators, controlled composition and some pinned generated housing behavior | **Partial.** A clear preservation/replace contract across all generation paths is not established | core commit pins changed housing; compare S24, S27 |
| Asset libraries | Existing illustrated marks plus a local optional sheet reviewer | **Partial.** Supplied pack is review-only; alpha sprites, persistent installation and missing-pack placement are follow-up | assets28-ui.js; supplied audit and optional pack manifest |
| Save/load document authority | Native versioned documents, validation, legacy import adapter and independent export projections | **Preserve.** Rendering can change while native source remains authoritative | H prepare/render and core validation; compare S04, S25 |
| Export workflow | PNG, lossless PDF, raster-containing SVG, image-only UVTT and interior walls/portals option | **Present with boundaries.** SVG is not editable vector output; lighting is baked; current fog blocks static art export | formats28-core/UI and H options; receiving application acceptance open |
| Rules and audience | Explicit player review, private-field filtering, separate gameplay owners | **Preserve and clarify.** Visibility, GM access, decorative shadows and occlusion are distinct | H prepare, native UVTT bridge; compare S18, S34 |
| Performance | Component timings, bounded preparation and an export benchmark | **Development evidence only.** No verified app-wide/device speedup | UHT25/28 handoffs; repeated-session and real-device tasks needed |
| Multi-scale links | Several specialty maps and link-related tools | **Potential strength; consistency unmeasured.** Test return navigation and cross-scale context | native map/link controls; compare S04, S33 |

### The most consequential local risks

**A. We can accumulate correct features inside an inconsistent editor.** MME-01 already moved VTT stacks into a dock. Newer modules then add their own UI, callbacks and settings. That does not justify discarding the dock. It calls for a shared command registry, tool lifecycle and inspector contract so each feature integrates into the same places.

**B. Our road fix illustrates the difference between a visible repair and a general editing model.** Same-plane consecutive road surfaces now paint clean intersections, and authored geometry remains separate. A user may still expect roads on the same plane to connect across insertion order, layers or edits. Test and define that expectation before promising network editing. Bridge crossings, junction creation and surface appearance should be separate explicit concepts.

**C. Some important state may live outside the obvious history path.** Native commit records draft/editing state, validates the result and saves locally. Rendering preferences and add-on controls have separate code paths. This inspection does not prove which preferences persist or undo incorrectly; it identifies a boundary to audit with state-diff and reload tests. We should not describe all reversible actions as covered merely because Ctrl/Cmd+Z exists.

**D. Art preparation and asset delivery are separate problems.** The supplied 22 JPEGs are 4.77 MiB compressed and approximately 104 MiB as a combined RGBA allocation estimate. Their backgrounds are baked pixels. The optional review pack avoids new image payload in the core, but it is not ready placement artwork or a production pack manager. Clean sprites and consistent style matter alongside caching and references.

**E. Our export fidelity labels need to remain visible.** The implementation now distinguishes native map data, static artwork and interactive wall/portal metadata. Users should see those distinctions before download. A receiving VTT can still interpret units, origin, portals or baked light differently; producing valid JSON does not complete that workflow.

## Map 7. A proposed unified interaction model

This is a design proposal derived from the study, not an implementation change.

**Author:** Create or select a region, settlement, interior or tactical map. Choose a style and a starting workflow: blank, example, import or controlled generation. Put structural actions ahead of optional decorative controls. Keep the artwork visible immediately.

**Edit:** The active tool owns transient drawing state, preview, snap override, confirm/cancel and a documented undo policy. The same inspector handles selected native objects and their visual settings. Advanced tools register in the existing shell instead of creating another independent panel. Asset definitions and placed instances are visibly different.

**Review:** Provide overlays for source geometry, derived joins, asset bounds/anchors, audience projection and export metadata. Show unresolved dependencies and validation issues with select-and-fix actions. Keep these inspection overlays out of player artwork unless deliberately requested.

**Present / Export:** Preview the intended audience and output type. State whether grids are removable, whether art is rasterized, which floor is exported, whether lighting is baked and which interactive metadata is included. Gameplay state belongs to its existing owner; an export or decorative toggle must not silently change it.

The shared implementation surface worth prototyping is small: one command registry, one tool-state lifecycle, one selection/inspector adapter, one history transaction interface, and explicit resource/document dependencies. This can be layered over the native Map Maker rather than replacing its save format. Prototype two contrasting tools first—Road and Room—before migrating the entire feature set.

## Map 8. Prioritized recommendations

Priority is my assessment of user impact and dependency order. Effort bands are rough planning categories, not delivery estimates or approvals.

| ID | Priority | Recommendation | Why / source basis | Concrete acceptance | Effort |
| --- | --- | --- | --- | --- | --- |
| R01 | P0 | Establish a repeatable current-workflow baseline | No task-level usability proof for UHT28; compare S16, S21 | Record the task suite below on a small laptop; log completion, errors, help and recovery | Small |
| R02 | P0 | Integrate add-on tools into one shell and contextual inspector | Consolidation pattern in S07, S11, S21; local modules are distributed | Road, room, art and export controls have predictable locations and discoverable labels | Medium |
| R03 | P0 | Define tool/modal keyboard and undo transactions | S09–S10 source patterns; local enumerated dialog guard | Escape, Enter, undo and text input behave consistently; one gesture restores exactly | Medium |
| R04 | P0 | Add explicit recovery snapshots and migration rehearsal | S20, S22; existing local save is a different mechanism | Restore a named state after reload without overwriting the original; old maps remain recoverable | Medium |
| R05 | P1 | Prototype structural Road and Room editing together | S08, S12, S27, S29 | Join/split/edit operations preserve doors, widths, planes and selected exclusions; no hidden geometry loss | Medium–large |
| R06 | P1 | Build one coherent alpha-ready art family through a reference scene | S02; supplied sheets need preparation | Consistent scale, anchors, edge quality and light direction; editable placements at normal zoom | Medium |
| R07 | P1 | Implement reference-based optional assets with preview and offline policy | S05–S06, S31; local review is not installation | Repeated objects share bytes; missing pack is explicit; reinstall restores art; pinned campaign works offline | Medium–large |
| R08 | P1 | Expose selective-regeneration consequences | S24, S27, S32 | Preview preserved/replaced objects; pinned edits survive; cancel leaves source unchanged | Medium–large |
| R09 | P1 | Validate export in receiving tools and print viewers | S19, S30 and current UVTT boundary | Image/grid/wall/portal alignment and audience checks pass a real import | Small–medium |
| R10 | P1 | Establish multi-zoom and repeated-session budgets | S25, S33; local component evidence is incomplete | Report interaction latency, retained memory, export peak and recovery on target hardware | Medium |
| R11 | P2 | Add reusable assemblies, named presets and searchable commands | S06, S20, S25 | Copy a room/district assembly with explicit instance overrides and dependencies | Medium |
| R12 | P2 | Unify linked-map navigation and validation issues | S04, S33 | Enter a detail map, preserve location/context, return; invalid link can be selected and repaired | Medium |

R01–R04 can establish the editing contract before a broad visual overhaul. R05–R09 then connect structure, art and delivery. Ordering can change after observation; no research recommendation automatically authorizes app publication or a native-document replacement.

## Map 9. Concrete evaluation protocol

Use the same source geometries in Multiversal and any comparator where the format/workflow permits. Compare tasks within the appropriate category: a world generator is not a substitute for a precision interior editor, and a tile editor is not judged as a turnkey illustrated mapmaker. Separate a novice's first encounter from an experienced repeat run.

| Task | Procedure | Record / success evidence |
| --- | --- | --- |
| T01 First useful view | Open an existing settlement at 1366×768; do not customize the UI first | Time to visible artwork; canvas area; whether any required action is off-screen |
| T02 Road correction | Build a T junction and crossroads, vary widths, reorder roads, add an elevated crossing | Internal seams, geometry changes, explicit plane behavior, undo/reopen result |
| T03 Room revision | Join rooms, attach a door, resize a host, then split or remove part of a wall | Opening attachment, stale geometry, pointer feedback and meaningful undo steps |
| T04 Dense selection | Pick a small object below foliage, isolate its layer, nudge/rotate it | Mis-selections, selection scope clarity and reversibility |
| T05 Asset reuse | Place twenty copies, save, remove/reinstall the pack, reopen offline with/without pinning | Document growth, dependency identity, missing-state clarity and restored placement |
| T06 Controlled generation | Regenerate one district/room while preserving three manual edits | What changes versus what was promised; preview/cancel fidelity |
| T07 Recovery | Create a named snapshot, make edits, close/reopen, restore to a clone | Exact state restoration, original preservation and intelligible save status |
| T08 Modal safety | Edit text and numeric fields; invoke each dialog; test Escape, Enter and undo | Text changes stay local; canvas actions do not leak through dialogs |
| T09 Multi-zoom | Repeat object selection, pan and zoom at 25%, 50%, 100% and 200% | Handle size/readability, pointer anchoring and task errors |
| T10 Audience/export | Include explicitly private geometry; export player art and interior metadata; import into a receiving VTT | Private content absent, correct image size/grid origin, walls/portals aligned, light not doubled |
| T11 Long session | Alternate documents, open/close editors and packs, edit, export and recover | Retained memory trend, input responsiveness and reload safety |
| T12 Context navigation | Enter a linked building/deck and return to settlement | Return location, breadcrumb/context, floor/plane identity and unchanged data |

Record time-to-first-useful-map, successful completion without help, wrong-mode actions, selection errors, undo correctness, data loss, help requests and receiving-tool mismatches. If instrumentation is added, report median/p95 interaction and export times, decoded and retained memory where measurable, hardware/browser/build and map/asset counts. Do not substitute Node component timings for these observations.

Proposed gates to calibrate: all core tasks must be reachable without hidden knowledge; no unreported destructive changes; no shortcut leakage from a modal; correct undo/recovery and audience filtering are non-negotiable. A provisional p95 visible-response target of 100 ms can guide feedback testing, but is a design target here, not a measured competitor standard or an accepted promise. Device-specific memory/time budgets should follow actual measurements.

A desk review can identify risks; it cannot determine how many participants will struggle or whether an attractive new layout fixes them. Keep an observation log with task, symptom, competing explanation, result and confidence. A poor result can come from interaction design, geometry, rendering, test setup, browser embedding or misunderstood task wording. Diagnose that boundary before prescribing a redesign.

## Map 10. Open-source material worth studying

| Resource | Mechanism worth examining | Reuse boundary / evidence status |
| --- | --- | --- |
| Tiled AbstractTool and MapDocument [S09](#s09) [S10](#s10) | Activated tool event ownership, contextual toolbar hooks, command stack and compound undo macros | Two current files spot-checked; their headers say GPL-2.0-or-later. Other Tiled components have their own license files |
| LDtk [S12](#s12) [S14](#s14) | Semantic source and generated visual layers; definition/instance vocabulary | Repository declares MIT; art and dependencies still require their own provenance |
| Watabou TownGeneratorOS [S35](#s35) | Historical mesh/district generation and relationship structure | GPL-3.0 metadata; README explicitly says later water/options UI is missing. Do not treat it as current app source |
| Azgaar [S24](#s24) [S25](#s25) | Regeneration consequences, data-driven loading, fixed-screen handles and editor cleanup | Read docs/release history; no blanket code-reuse or performance certification |
| TrenchBroom [S33](#s33) [S36](#s36) | Spatial tools, linked groups, issues browser and reversible editing | GPL-3.0 metadata; manual reviewed, full implementation not audited |
| Dungeondraft API [S29](#s29) | Domain tool lifecycle and preview/confirm contracts | Public API documentation is not the application's open-source implementation |

This study copies no competitor implementation into Multiversal. Study mechanisms first; evaluate any actual code, dependency and asset license at the point of a specific reuse proposal. Publicly readable does not by itself mean permissively reusable.

## Map 11. What to preserve, change and defer

**Preserve:** the native document system and validators; user-editable objects; stable source geometry under rendering improvements; player projection and explicit review; the canvas-first dock; existing specialty spatial owners; and the separation between artwork and gameplay simulation.

**Change next in a prototype:** the consistency of tool integration, selection properties, modal focus, undo/recovery and structural editing. Prove those with the short task suite before scaling the migration. Build a small approved style sample alongside that work.

**Defer until justified:** a full engine rewrite; copying a competitor's entire layer model; a 3D editor UI for all maps; a large uncurated asset dump; rebuilding settlement/gameplay simulation inside the map renderer; and numerical claims that our tester matches mature editors without direct evidence.

These retained map-only recommendations feed the integrated priorities in Joint 4 below. The combined edition adds VTT acceptance boundaries and end-to-end tasks. No new UHT product build or third-party runtime benchmark is claimed.


## VTT 1. Evolution has several branches

A VTT can prioritize rules automation, a lightweight shared table, cinematic presentation, or constructed 3D space. These are different choices about prep effort and live attention, not successive maturity levels. Multiversal should support its own campaign and rules workflows without inheriting every competitor's interface.

| Date / period | Documented change | Problem or tradeoff | Lesson for our combined workflow |
| --- | --- | --- | --- |
| 2004; later CoreRPG development | Fantasy Grounds grows from D20 support into layered rulesets [V04](#v04) | Repeating campaign functionality across systems | Shared campaign services with rules-specific adapters |
| 2010 interview, republished 2019 | MapTool creator recalls connected token movement, then a powerful but fragmented interface [V01](#v01) | Capability accumulation outruns cohesion | Test both synchronized basics and the integrated user experience |
| 2021 | Fantasy Grounds Classic retires in favor of Unity [V04](#v04) | Engine change must preserve campaign investment | Treat compatibility and migration as product work |
| 1.0 → 2.0 migration guide; date unverified | Owlbear introduces persistent rooms, cloud assets and multi-map scenes [V11](#v11) | Browser-storage loss and richer workspace complexity | Durable state plus an easy path for the common case |
| Late 2023 → January 2025 | Jumpgate project reaches default-new-game release [V06](#v06) | Aging renderer and transition costs | Stage migrations; preserve user data and task continuity |
| February 2025 | Dungeon Scrawl connects to Roll20 pages [V20](#v20) | Repeated export/upload interrupts improvisation | Improve handoff without assuming one monolithic document |
| 2025 v13 retrospective | Foundry consolidates UI and movement infrastructure [V08](#v08) | Inconsistent interfaces and complex movement interactions | Stable interaction contracts matter beneath visible controls |
| January 2026 | Roll20 reports atlas/instancing optimization [V07](#v07) | Many editable scene objects increase draw overhead | Measure representative crowded scenes, not one empty canvas |
| May → October 2026 | Owlbear fog automation progresses from beta to release [V15](#v15) [V19](#v19) | Manual tracing, structural errors and service latency | Keep automatic results editable; include service waiting in latency |
| August 2026 preview | Roll20 alignment redesign uses guided interactive prototypes [V21](#v21) | Hidden tool, offsets, drift and existing-object alignment | A static mockup cannot validate spatial interaction |
| November 2026 stable notes | Foundry fixes selection, focus and ownership/level edge cases [V10](#v10) | Small state interactions remain consequential | Regression suites must cover action sequences and context changes |

These dates identify documented milestones, not first inventions. A later release is not proof that every earlier problem is solved for every device.

## VTT 2. Problems and responses in developer evidence

### MapTool — the shared table comes before the elaborate table

**Documented:** In the retrospective, Trevor Croft describes an initial background, grid and draggable images whose movement appeared on connected clients. He also criticizes the later interface despite its powerful features. Those are historical developer observations, not a present-day ranking. [V01](#v01)

**Source spot-check:** ServerPolicy has separate fields for strict token management, movement locking, impersonation, individual views and individual fog, with DTO conversion. This establishes explicit policy representation, not proof of enforcement at every network operation. The repository and file identify AGPL licensing. [V02](#v02) [V03](#v03)

**For Multiversal:** Preserve the local overlay as a rehearsal tool. Validate authenticated player delivery and action handling in the owning multiplayer layer before describing it as live play. Model who may move a token separately from who may see a region or inspect an actor. Do not copy open-source implementation without a specific license review.

### Fantasy Grounds — automation and preparation need structure

**Documented:** Its historical account describes a reusable CoreRPG base beneath system rulesets and compatibility across the move to Unity. The current image manual organizes play, base/layers, painting, effects, line of sight, lighting, masks and grids into modes and submodes. [V04](#v04) [V05](#v05)

**Interpretation:** This is an instructive division of responsibilities, with a mode-learning cost that still needs usability testing. It does not establish that a large mode hierarchy is best for our audience.

**For Multiversal:** Keep artwork editing out of routine player controls. Give the GM an explicit preparation context and a clear live context. Reuse campaign, combat, inventory and rules owners through references. An authored door can have a visual frame, a sight boundary and an interaction binding without becoming three competing gameplay records.

### Roll20 — migration and rendering are workflow issues

**Documented:** Jumpgate became the default for new games in January 2025. The later engineering diary explains a side-by-side engine migration using existing game data and reducing draw overhead through instancing and texture atlases, with ordering and texture-size constraints. Its reported gains depend on workload and hardware; we did not reproduce them. [V06](#v06) [V07](#v07)

**For Multiversal:** Measure the actual dense scene, loading delay, memory and lower-powered client before prescribing an engine. Retain native documents and use compatible adapters. A renderer replacement is justified by a measured bottleneck and migration plan, not another product's headline.

### Roll20 — alignment and connected authoring reveal the handoff problem

**Documented:** The alignment designer describes a hard-to-discover command, baked-grid borders and drift, then previews a guided process and contextual hotbar. Working prototypes exercised input methods and already-placed scene objects. This is design-process evidence, not verified shipment. [V21](#v21)

The Scrawl connection documents live map updates in a Roll20 page, but also a save/session boundary when the authoring tab closes. It explicitly distinguishes decorative Scrawl lighting from Roll20 Dynamic Lighting. [V20](#v20)

**For Multiversal:** Make scale, origin and revision visible during handoff. Update or reject dependent overlays explicitly when geometry changes. A convenient connected preview still needs durable saves, stale-link handling and independent audience filtering. Treat visual light and vision authority as different data contracts.

### Foundry — coherent UI and movement need shared infrastructure

**Documented:** The 2025 account describes a multi-version UI effort culminating in ApplicationV2 and a movement framework with paths and rule hooks. It also explains deferring a disruptive Pixi migration to protect the ecosystem. These are historical decisions, not a statement of today's renderer internals. [V08](#v08)

The permissions guide distinguishes role capabilities from permissions on individual documents; its accounts are world-scoped. We should study the distinction without copying that account model into Multiversal's verified-email design. [V09](#v09)

The verified v14 stable notes include focus, locked-selection and level-related fixes, reminding us that integrated behavior remains active work even in a mature system. [V10](#v10)

**For Multiversal:** Establish one active-tool lifecycle, scoped shortcuts, selection rules and command interface. Route movement intent through its owner; show requested, pending, accepted, rejected and superseded states. A ruler drag is not sufficient evidence of a valid action. Freeze package/document contracts before increasing extension surface.

### Owlbear Rodeo — simplicity is an actively maintained property

**Documented:** The migration guide attributes serious losses to browser-only storage, moves toward persistent rooms and cloud storage, expands maps into scenes, and retains a create-from-map path. It describes a lean extensible base with meaningful image types. [V11](#v11)

The SDK exposes contextual UI and explicit tool modes. Scene readiness and unsubscribable events are documented; temporary local feedback items have a separate API from scene items. These are API contracts, not a full open engine implementation. [V12](#v12) [V13](#v13) [V14](#v14)

**For Multiversal:** Offer a direct Open map → Prepare scene path, then reveal advanced tools when needed. Do not rely on browser storage as the only durable copy. Keep hover guides, measuring previews and personal camera state separate from committed scene content. Make unavailable dependencies and extensions understandable at load time.

### Owlbear Rodeo — automate preparation but preserve correction

**Documented:** The May 2.4 journal combines automatic fog with repair tools and optional import conversion that retains the original if conversion saves nothing. The October release explains a room-graph approach and a shift from GPU execution to CPU execution after GPU availability caused waiting. Release access is described for named subscriber tiers. [V15](#v15) [V19](#v19)

**Interpretation:** Relationship-aware structure and service availability can matter more than the nominal speed of an isolated operation.

**For Multiversal:** Native walls should be the preferred source for native documents; imported images can use assisted tracing later, with editable correction. Evaluate total preparation time and failure behavior. Keep the original asset when a proposed conversion is worse: our sheet trial already demonstrated that a WebP preset can increase bytes.

### Alchemy — live attention need not always center on the grid

**Documented:** Its shortcut guide exposes story, tactical, camera and Zen views, an in-game search command, tactical tools, and a topmost-modal escape action. This source establishes interaction choices, not their complete history or comparative success. [V16](#v16)

**For Multiversal:** A setting-independent campaign may need narrative presentation without constant tactical tools. Keep scene context while changing presentation. Scope shortcuts to the active view and focused field; do not copy global bindings without testing browser and text-entry behavior.

### TaleSpire — assembled space and visibility are stateful

**Documented:** The slab guide selects existing build pieces, frames a thumbnail and publishes the assembly. Dev Log 516 describes vision-limit failures after chains of actions and cleanup that still required playtesting at the time of that post. [V17](#v17) [V18](#v18)

**For Multiversal:** Learn from reusable assemblies without making every map 3D. Test floor switches, preview switches, hidden areas and undo in sequence. A visually correct first frame cannot establish visibility correctness after several transitions.

## Joint 1. One workflow, explicit responsibilities

The following division is a proposed integration contract, not a replacement for existing architecture. The owning project services remain authoritative.

| Responsibility | Data it owns or consumes | What the user should understand | Boundary to validate |
| --- | --- | --- | --- |
| Map document | Editable native features, stable IDs, dimensions, floors, revisions, source geometry | Which map and version is being edited | Scene references remain resolvable or become explicitly stale |
| Artwork renderer | Materials, roofs, decorative shadows, labels, illustration references | How the scene looks and which style is applied | Presentation changes do not silently alter collision, vision or rules |
| Prepared scene | Chosen map revision, placed actor references, configured blockers, starts and private GM information | What is ready, unresolved or only a rehearsal | Preparation cannot accidentally publish secrets or execute gameplay |
| Live session owner | Authorized scene revision, accepted placements, audience policy, authoritative event ordering | Connected, syncing, ready, pending or rejected | Requests are authenticated, authorized and idempotently committed |
| Rules and domain owners | Legal actions, HP, effects, loot, custody, travel and campaign state | Why an action was accepted and what changed | The map presents intent; the correct owner validates effects |
| Personal view | Camera, selected tool, local feedback, permitted sight presentation | Whose perspective is being viewed | Local preferences do not change another user's private state |
| Recovery and delivery | Versioned saves, checkpoints, dependency manifests, supported export transforms | What will be restored or shared | No hidden data, silent scale change or overwritten unrelated work |

Scene publication is an action with a visible audience and revision. It is not an implicit side effect of saving artwork. Similarly, a GM's local player preview is a diagnostic view, not a player session. A privacy-safe payload must be created before delivery; removing DOM elements after private data reaches a client does not establish confidentiality.

For maps already active in play, propose an updated revision, show changes affecting doors, starts or blockers, and let the session owner apply it at a clear transition. This avoids a roof edit unexpectedly moving a token or changing a player's sight mid-action. The exact conflict strategy belongs to the multiplayer design and needs an executable test.

## Joint 2. Combined evaluation against UHT28

This audit concerns the delivered HTML and its extracted map/core scripts. It does not assess repository main, the installed Unity app, or an existing networking build. Status words below deliberately separate source presence from practical acceptance.

| Area | What exists in the inspected baseline | Status and practical gap | Implication |
| --- | --- | --- | --- |
| Canvas-first authoring | MME-01 relocates the original VTT panels into a dock and returns the map stage to an earlier position | Implemented local UI; novice/browser task outcome unmeasured | Preserve this foundation and test full journeys |
| Native map structure | Versioned map/level/grid references and native authored features | Implemented foundation; roads fix covers consecutive same-plane runs, not general topology | Improve structural editing independently of VTT authority |
| Sight rehearsal | VTTG-06 stores actors, blockers, per-user fog and per-character exploration in local GM state | Local synthetic preview; source explicitly says real player packets require D05 | Do not call this multiplayer vision |
| Combat mapping | VTTG-07 validates read-only encounter snapshots and map/revision association | Local reference/proposal integration; no combat owner writes in this overlay | Preserve single gameplay ownership and test the actual owner path |
| Triggers | VTTG-08 has GM review and an empty trigger player projection | Local withholding is useful, but production server filtering explicitly absent | Test real player payloads and reject unauthorized requests |
| Loot and custody | VTTG-09 records source-linked GM requests; authority flags remain false | Review scaffold, not inventory transfer or player grants | Avoid a second inventory system in the map UI |
| Floors and links | VTTG-10 keeps source-scoped links and destination previews; player packet is empty | Local spatial preparation; no gameplay travel or access grant | Validate accepted transition, loading and reconnect as a separate owner operation |
| Identity and live connection | Local role/view controls and browser persistence are present | Authenticated remote participation is not established by this artifact | Evaluate account/session work in its own build; do not infer absence across the whole project |
| Recovery | Native history plus local GM JSON import/export paths | Bounded source mechanisms; no whole-session crash/reconnect acceptance here | Validate named checkpoints and a durable backup workflow |
| Export | UHT28 UVTT adapter plus focused prior receipts | Component-level evidence; receiving-VTT import, browser and real audience acceptance open | Use fixed recipient versions and scale/light/door fixtures |
| Optional artwork | 22 original sheets, one decoded reviewer image at a time; no installed editable pack workflow | Reviewer exists; pack distribution, licensing and per-placement editability remain work | Separate core app, optional pack and per-scene dependency budgets |
| Interaction consistency | Multiple specialty tools, dialogs and global/native handlers remain | Static evidence motivates testing; it does not measure visible clutter | One lifecycle and focus policy, then observed task comparison |

Source anchors for this local review: map-28.html lines 36252–36290 (overlay storage and sight), 36422–36455 (read-only combat binding), 36638 (trigger projection), 36760 (loot projection), 36802–36825 and 36853 (transitions), 36884–36935 (dock and explicit GM-local preview). Line numbers refer to the extracted audit copy. The package hash and exact module identities are in the evidence archive.

**The strongest existing direction is native editable structure plus explicit owner boundaries. The largest unproven VTT step is the passage from private rehearsal into authorized shared play.** That finding does not mean all previous work failed; it identifies which acceptance claim the current evidence can support.

## Joint 3. Artwork size becomes a session-delivery problem

The earlier trial measured 4,998,320 bytes for the 22 JPEG sheets and approximately 104 MiB of decoded RGBA pixels. The trial WebP output was larger than those originals. These are different quantities from UHT28's roughly 56 MiB standalone HTML, which also contains bundled application/test material. They must not be added together and called one asset budget.

Proposed approach: keep a small coherent built-in set; install optional packs by manifest and stable content identity; save references and instance overrides in native maps; create previews separately from placement renditions; load only the active scene's dependencies and evict unused decoded textures. Offer an explicit portable export that gathers permitted dependencies when needed. A missing pack should produce a clear placeholder and resolution path, not corrupt geometry or silently substitute artwork.

For live play, distribute only permitted dependencies, track progress and allow a low-cost preview while required assets load. Public map art must not accidentally include a GM-only annotation atlas or thumbnail. Measure download bytes, installed bytes, decoded memory, retained/GPU memory where measurable, and preparation/cache time independently. Optional packs reduce core delivery size; they do not eliminate client memory costs or licensing obligations.

Roll20's atlas discussion motivates draw-call measurements; Owlbear's conversion behavior motivates conditional transcoding. Neither proves that atlasing or WebP is automatically best for our supplied sheets. [V07](#v07) [V15](#v15)

## Joint 4. Priorities for the next design cycles

These priorities incorporate the map-only findings. They are research recommendations, not a renumbered shipped roadmap. The installed MVP boundary remains unchanged. VTT-dependent work applies when the VTT workstream is scheduled and must use existing account, session and domain owners.

| ID | Priority | Concrete deliverable | Required evidence / dependency |
| --- | --- | --- | --- |
| C01 | Immediate | Freeze one integrated task baseline and state/owner matrix | UHT28 artifact identity, fixture IDs and failure observations |
| C02 | Immediate | Prototype a consistent Author / Prepare / Play shell with role-specific controls | J01–J03 and J10; retain native document and original owners |
| C03 | Immediate | Define active tool, selection, focus, shortcut and local command contracts | J03, J10, J11; improve predictable editing before mass migration |
| C04 | VTT prerequisite | Define accepted session state, authorization and audience projections | J04–J06; implemented in owning services, not CSS or local role switches |
| C05 | VTT prerequisite | Define request identity, revision checks, rejection and reconnect behavior | J05, J07–J09; one authoritative owner per effect |
| C06 | Immediate / shared | Define durable author checkpoints and separate live recovery semantics | J08, J11; editor undo must not rewrite committed campaign history |
| C07 | Shared spatial | Improve structural roads, rooms, doors and dependency invalidation | J02, J06, J12; visual joins remain distinct from rules movement |
| C08 | Shared visual | Review one coherent settlement/interior asset family and optional-pack path | J13–J14; approved sample scene before bulk asset production |
| C09 | Handoff | Validate native-to-scene and external export/import transforms | J02, J12, J15; correct units, origin, wall/door and lighting semantics |
| C10 | Shared performance | Profile representative preparation and play on target lower-powered hardware | J14–J16; report hardware, build, scene counts and cold/warm load |
| C11 | Later extension | Add stable search, assemblies and constrained extension contracts | J03, J13; versioning, dependencies and failure isolation first |
| C12 | Acceptance | Run observed comparative workflows and actual multi-client sessions | All J tasks; documentary comparison cannot close these gates |

The v2 interaction-prototype recommendation feeds MVAC-01 through MVAC-04 in this edition; the VTT contracts feed MVAC-18 through MVAC-21. These retained priorities are superseded by the integrated MVAC plan above for sequencing, not by a new network stack in the map renderer.

## Joint 5. End-to-end validation scenarios

This is a proposed protocol, not a list of tests run in this study. Reuse one settlement, its linked two-room interior, a cave, a tactical area, and a specialty ship/deck fixture. Include two players with different owned characters and a GM. Real-client cases require separate authenticated clients; developer instrumentation must record only authorized test data.

| ID | Task | Success condition | Evidence to record |
| --- | --- | --- | --- |
| J01 | Open the existing settlement as author, GM and player | Immediate useful map; permitted tools and current context are clear | First-useful-view time, help, wrong-mode actions, visible content |
| J02 | Repair crossing roads, enter an interior, publish a prepared revision | Geometry stays editable; joins and dependent overlay changes are predictable | Before/after native diff, reference resolution, author observation |
| J03 | Select a door among overlapping art and search for its action | Inspector identifies correct object, layer and source; no guesswork | Selection errors, completion time, keyboard/pointer paths |
| J04 | Join as each player and inspect delivered data | Neither receives hidden triggers, GM labels, other private sheets or restricted dependencies | Actual client payload/state inspection with known secret fixtures |
| J05 | Attempt owned, unowned and replayed token/action changes | Authorized action commits once; unauthorized or duplicate request has no extra effect | Request ID, subject, owner receipt, revision and state delta |
| J06 | Open/close a door and change light/fog/sight | Art, blockers, exploration and per-character visibility remain coherent and private | Both clients' state and rendered result; no secret labels/count leaks |
| J07 | Disconnect a player mid-request and reconnect | Clear connection state; accepted state restored without phantom success or duplicate action | Connection timeline, server revision, client reconciliation |
| J08 | Restart after a scene checkpoint and unsaved local edits | Restored scope and data loss, if any, are explicit; no cross-campaign overwrite | Save/checkpoint provenance and recovered state comparison |
| J09 | Edit map revision while an action or floor transition is pending | Stale references are rejected or explicitly reconciled by the owner | Controlled interleaving, rejection explanation, final accepted state |
| J10 | Type in a dialog, undo text, press Escape and change tools | Only intended focused context responds; no underlying map or live action fires | Event trace and native/live before-after state |
| J11 | Undo a map edit, cancel preparation and correct an accepted game action | Each uses the appropriate history/owner path; no silent campaign rollback | Separate author history and gameplay event/compensation evidence |
| J12 | Traverse a linked floor, ship hatch or portal | Correct authorized destination, scale, owned actor and visibility load; retry safe | Scene IDs/revisions, transition receipt, both clients' views |
| J13 | Open a scene with missing, outdated or unavailable pack/extension | Understandable status and placeholder; original placements preserved | Dependency manifest, blocked action, successful later resolution |
| J14 | Load art-heavy fixtures on the lower-powered target | Remains usable under a measured agreed budget; loading/cancel paths work | Cold/warm bytes, decode/memory, frame/interaction distributions |
| J15 | Import exported UVTT in named receiving versions | Calibration, doors, blockers and light policy match intended output; private content excluded | Recipient screenshots, measured distances, structured import result |
| J16 | Run a long session across maps and presentation modes | Stable responsiveness and connection; understandable recovery after induced failure | Session duration, retained resources, errors, outcome and device specs |

Record task completion, help requests, incorrect actions, recovery effort and explanations, as well as time. Compare novice and experienced users on the same fixture, counterbalance order when comparing builds, and preserve failures rather than excluding them from averages. A measured slower path that prevents an accidental private reveal may be preferable; the tradeoff must be visible.

Proposed hard gates are no unauthorized state changes, no private information delivered to the wrong audience, no silent data destruction and no duplicate accepted gameplay effects. Interaction and performance thresholds should be calibrated on actual target hardware, not borrowed from vendor marketing. A source-level test suite can support these gates but cannot replace real-client and observed-workflow evidence.

## Joint 6. Open-source and research follow-through

| Material | What was actually examined | Useful next investigation | Reuse boundary |
| --- | --- | --- | --- |
| MapTool [V02](#v02) [V03](#v03) | Repository metadata and one ServerPolicy file, blob 37ab58feecbde99f0fa029143ceeaf9aa1475956 | Trace request-to-enforcement and visibility projection paths in a separate code audit | AGPL-3.0; no code copied into our app |
| Owlbear [V12](#v12) [V13](#v13) [V14](#v14) | Public extension architecture and scene/local APIs | Examine SDK source, lifecycle teardown and extension isolation if adopting an integration | Public SDK docs do not make the full service open source |
| Foundry [V08](#v08) [V09](#v09) | Developer rationale and role/document permission model | Compare a real preparation and player task in a fixed version | Public documentation is not a permissive engine license |
| Tiled / LDtk / TrenchBroom | Retained map-study source/manual review | Reuse the earlier lifecycle, definitions and undo research | Preserve per-component licensing and asset provenance |
| Roll20 / Alchemy / TaleSpire | Journals, manuals and documented workflows | Direct task observations and state-sequence trials | No implementation copying or claim of tested equivalence |

The study does not establish a preferred commercial VTT, pricing comparison, market share, accessibility certification or legal clearance for third-party assets. It also does not prove a multiplayer security model through one policy file. Those are separate questions with different evidence requirements.

**Retained v2 result:** the map/VTT documentary findings and task set remain evidence for the integrated MVAC plan in this edition. Product changes, releases and real-player acceptance remain unclaimed.


## Source register — all three studies

Read 25 November 2026. S01–S36 are retained map-maker sources; V01–V21 are retained VTT/integration sources; A01–A28 are new asset sources. Repeated URLs retain one original identifier where possible. The NCG records are pinned internal research, not additional public competitors. Source snapshots, version labels, dates and limitations must travel with any implementation proposal.

### S01 — Campaign Cartographer: Phoenix Bound

Simon Rogers / ProFantasy. 2013-02-21. Type: developer retrospective. [Read source](https://rpgmaps.profantasy.com/phoenix-bound/).

CAD origin and cartography-specific adaptation.

Limit: Documentary/source evidence; no independent usability outcome established.

### S02 — Campaign Cartographer: CC3+ – The Evolution of a Map Style

Simon Rogers / ProFantasy. 2014-01-14. Type: developer art-pipeline journal. [Read source](https://rpgmaps.profantasy.com/cc3-the-evolution-of-a-map/).

Sample-map approval precedes symbols, tools, effects and resolution catalogs.

Limit: Documentary/source evidence; no independent usability outcome established.

### S03 — Campaign Cartographer: Campaign Cartographer 3+ Tutorial

ProFantasy-hosted tutorial. 2015 path; exact publication day unverified. Type: tutorial with historical UI figures. [Read source](https://rpgmaps.profantasy.com/wp-content/uploads/2015/02/Campaign-Cartographer-3plus-Tutorial.pdf).

Sheet effects, explicit effect units and map styling dialogs.

Limit: Documentary/source evidence; no independent usability outcome established.

### S04 — Campaign Cartographer / FRIA: The Forgotten Realms Interactive Atlas

Ralf Schemmann / ProFantasy. 2026-06-09 retrospective. Type: participant retrospective. [Read source](https://rpgmaps.profantasy.com/the-forgotten-realms-interactive-atlas/).

Linked map scales, viewer/author separation and durable editability; not a 2026 launch.

Limit: Documentary/source evidence; no independent usability outcome established.

### S05 — Tiled: Tiled 1.0 released

Thorbjørn Lindeijer. 2017-05-24. Type: developer release analysis. [Read source](https://www.mapeditor.org/2017/05/24/tiled-1-0-0-released.html).

External tilesets, layer hierarchy and distinct editor contexts.

Limit: Documentary/source evidence; no independent usability outcome established.

### S06 — Tiled: Tiled 1.1 released

Thorbjørn Lindeijer. 2018-01-03. Type: developer release analysis. [Read source](https://www.mapeditor.org/2018/01/03/tiled-1-1-0-released.html).

Sparse infinite maps, connected terrain/roads, templates and contextual toolbar.

Limit: Documentary/source evidence; no independent usability outcome established.

### S07 — Tiled: Tiled 1.5 Released

Thorbjørn Lindeijer. 2021-03-23. Type: developer release analysis. [Read source](https://www.mapeditor.org/2021/03/23/tiled-1-5-0-released.html).

Unifies overlapping terrain tools; selection policy and format compatibility.

Limit: Documentary/source evidence; no independent usability outcome established.

### S08 — Tiled: Focus on Level Design with Automapping

Thorbjørn Lindeijer. 2026-07-14. Type: developer technical tutorial. [Read source](https://www.mapeditor.org/2026/07/14/focus-on-level-design-with-automapping.html).

Blueprint input produces walls/floors via rules; hidden power needs teachable setup.

Limit: Documentary/source evidence; no independent usability outcome established.

### S09 — Tiled: src/tiled/abstracttool.h

Tiled contributors. current file read 2026-11-25. Type: source spot-check. [Read source](https://github.com/mapeditor/tiled/blob/master/src/tiled/abstracttool.h).

Tool activation, event handling, tool toolbar hook and tool undo-stack hook. Blob b8d71a0bbf9604927dd108956a3f9de7d9e2f167.

Limit: Documentary/source evidence; no independent usability outcome established.

### S10 — Tiled: src/tiled/mapdocument.cpp

Tiled contributors. current file read 2026-11-25. Type: source spot-check. [Read source](https://github.com/mapeditor/tiled/blob/master/src/tiled/mapdocument.cpp).

Undo commands and grouped macros; blob fdebacd4582d8bbb09b4e11199653595ff6c37cb.

Limit: Documentary/source evidence; no independent usability outcome established.

### S11 — LDtk: Interface overview

Deepnight Games. 2024-01-04 update. Type: official UI documentation. [Read source](https://ldtk.io/docs/general/editor-components/).

Definitions vs instances, context palettes and compact sidebar; this older page is not the latest release history.

Limit: Documentary/source evidence; no independent usability outcome established.

### S12 — LDtk: Auto layers

Deepnight Games. 2022-04-04 update. Type: official technical documentation. [Read source](https://ldtk.io/docs/general/auto-layers/).

Separate semantic IntGrid input from generated visual layers.

Limit: Documentary/source evidence; no independent usability outcome established.

### S13 — LDtk: Releases, especially 1.4.0 Zen mode

Deepnight Games. version 1.4.0; exact year not pinned here. Type: developer release history. [Read source](https://github.com/deepnight/ldtk/releases).

Confusing Compact mode replaced; sidebar reveal, palette density and shortcut change on macOS.

Limit: Documentary/source evidence; no independent usability outcome established.

### S14 — LDtk: Repository and LICENSE

Deepnight Games. accessed 2026-11-25. Type: source/license identity. [Read source](https://github.com/deepnight/ldtk).

Repository declares MIT; LICENSE blob 1d96a63457c528790b87b804ee101010a11a5517.

Limit: Documentary/source evidence; no independent usability outcome established.

### S15 — Dungeon Scrawl: Dungeon Scrawl 1.3.0 Update

ProbableTrain / Keir. 2020-07-05. Type: developer devlog. [Read source](https://probabletrain.itch.io/dungeon-scrawl/devlog/159803/dungeon-scrawl-130-update).

Documented fast/fragile versus slower/more robust Boolean solver tradeoff.

Limit: Documentary/source evidence; no independent usability outcome established.

### S16 — Dungeon Scrawl: Dungeon Scrawl 1.4.0 Update

ProbableTrain / Keir. 2020-07-15. Type: developer devlog. [Read source](https://probabletrain.itch.io/dungeon-scrawl/devlog/162228/dungeon-scrawl-140-update).

Placement transforms, snapping override, grouping, local point undo and collapsible UI.

Limit: Documentary/source evidence; no independent usability outcome established.

### S17 — Dungeon Scrawl: Dungeon Scrawl V2 is now available!

ProbableTrain / Keir. 2022-10-15. Type: developer rebuild announcement. [Read source](https://probabletrain.itch.io/dungeon-scrawl/devlog/439864/dungeon-scrawl-v2-is-now-available).

Rebuild claimed better controls/performance; feature parity temporarily incomplete.

Limit: Documentary/source evidence; no independent usability outcome established.

### S18 — Dungeon Scrawl: February 26 Update: Subscriber Requests

Dungeon Scrawl. 2026-02-17. Type: official change report. [Read source](https://blog.dungeonscrawl.com/february-2026-update).

Unified texture lists, separate wall light-blocking, global grid hide and export fix.

Limit: Documentary/source evidence; no independent usability outcome established.

### S19 — Dungeon Scrawl: Automatic Dynamic Lighting with UVTT Export

Dungeon Scrawl. 2026-09-09. Type: official workflow release. [Read source](https://blog.dungeonscrawl.com/uvtt-export).

Export packages image, walls, doors and lighting for receiving VTTs; vendor claims are not our import proof.

Limit: Documentary/source evidence; no independent usability outcome established.

### S20 — Inkarnate: Inkarnate 2.0

Inkarnate. 2025-12-08. Type: official release changelog. [Read source](https://feedback.inkarnate.com/changelog/inkarnate-20-star).

Layer overhaul, scene reuse, context controls, autosave and opt-in migration; launch marked beta features.

Limit: Documentary/source evidence; no independent usability outcome established.

### S21 — Inkarnate: Editor Overview

Philipp Brockerhoff / Inkarnate. live documentation; accessed 2026-11-25. Type: official UI documentation. [Read source](https://help.inkarnate.com/articles/6452044-editor-overview).

Persistent workspace zones and context-sensitive tool settings/shortcuts.

Limit: Documentary/source evidence; no independent usability outcome established.

### S22 — Inkarnate: Autosave & Snapshots

Philipp Brockerhoff / Inkarnate. live documentation; accessed 2026-11-25. Type: official recovery documentation. [Read source](https://help.inkarnate.com/articles/8751126-autosave-and-snapshots).

Current restore behavior creates a clone; differentiates latest recovery and named restore points.

Limit: Documentary/source evidence; no independent usability outcome established.

### S23 — Azgaar: Introduction

Azgaar. 2017-03-30; updated 2017-04-27. Type: developer journal. [Read source](https://azgaar.wordpress.com/2017/03/30/first-post/).

Original priorities included interactive plausible maps and fast generation/dragging; early label automation deliberately deferred.

Limit: Documentary/source evidence; no independent usability outcome established.

### S24 — Azgaar: Heightmap customization

Fantasy Map Generator maintainers. current documentation; accessed 2026-11-25. Type: official project documentation. [Read source](https://github.com/Azgaar/Fantasy-Map-Generator/blob/master/docs/wiki/Heightmap-customization.md).

Keep/Risk/Erase consequences and current drainage/locked-river preservation.

Limit: Documentary/source evidence; no independent usability outcome established.

### S25 — Azgaar: Changelog

Fantasy Map Generator maintainers. dated entries through 2026-11-12; accessed 2026-11-25. Type: official release history. [Read source](https://github.com/Azgaar/Fantasy-Map-Generator/wiki/Changelog).

Search, fixed-screen edit handles, listener cleanup, current data-driven load and backups.

Limit: Documentary/source evidence; no independent usability outcome established.

### S26 — Watabou: 0.2.2: Temples, wards overview

watabou. 2017-06-01. Type: developer devlog. [Read source](https://itch.io/devlog/2062/022-temples-wards-overview.amp).

Label helper and touchscreen tooltips; iframe blocked initial permalink approach.

Limit: Documentary/source evidence; no independent usability outcome established.

### S27 — Watabou: 0.5.2: Warp tool

watabou. historical 0.5.2; exact calendar date not established. Type: developer devlog. [Read source](https://watabou.itch.io/medieval-fantasy-city-generator/devlog/22794/052-warp-tool).

Mesh editing preserves relationships but cannot create arbitrary new topology; excessive warp may glitch.

Limit: Documentary/source evidence; no independent usability outcome established.

### S28 — Watabou: 1.6.4: crossroads and numbered houses

watabou. 2024-11-26. Type: developer devlog. [Read source](https://watabou.itch.io/village-generator/devlog/840277/164-crossroads-and-numbered-houses).

Request an intersection through a tag; developer acknowledges a numbering limitation.

Limit: Documentary/source evidence; no independent usability outcome established.

### S29 — Dungeondraft: PathTool API

Megasploot. live API; accessed 2026-11-25. Type: official developer API. [Read source](https://megasploot.github.io/DungeondraftModdingAPI/reference/PathTool/).

Active path, preview/confirmation, over/under sorting, width, library state and explicit light blocking.

Limit: Documentary/source evidence; no independent usability outcome established.

### S30 — Dungeondraft: Official product FAQ

Megasploot. live page; accessed 2026-11-25. Type: official support/product information. [Read source](https://dungeondraft.net/).

Custom art ecosystem and export/storage/graphics troubleshooting. This is not an internal performance study.

Limit: Documentary/source evidence; no independent usability outcome established.

### S31 — Wonderdraft: Official site and themed asset packs

Megasploot. live page; accessed 2026-11-25. Type: official product information. [Read source](https://wonderdraft.net/).

Separate art packs and symbol color variants; limited historical UX evidence on current page.

Limit: Documentary/source evidence; no independent usability outcome established.

### S32 — Dungeon Alchemist: FAQ

Briganti. live page; accessed 2026-11-25. Type: official workflow description. [Read source](https://www.dungeonalchemist.com/faqs).

Theme-first room population, editable generated result and VTT handoff; not a measured speed comparison.

Limit: Documentary/source evidence; no independent usability outcome established.

### S33 — TrenchBroom: 2026.2 Reference Manual

TrenchBroom maintainers. 2026.2 manual; accessed 2026-11-25. Type: official technical/UI manual. [Read source](https://trenchbroom.github.io/manual/latest/).

Direct spatial editing, selectable viewport layouts, linked groups, issues browser and backup support.

Limit: Documentary/source evidence; no independent usability outcome established.

### S34 — MapTool: MapTool product and feature overview

RPTools. live page; accessed 2026-11-25. Type: official VTT overview. [Read source](https://www.rptools.net/toolbox/maptool/).

Art, vision and topology coexist; a proposed 2.0 UI refresh is roadmap, not evidence of shipped completion.

Limit: Documentary/source evidence; no independent usability outcome established.

### S35 — Watabou: TownGeneratorOS README

watabou. repository accessed 2026-11-25. Type: historical open-source snapshot. [Read source](https://github.com/watabou/TownGeneratorOS).

README explicitly lacks later water/options UI; GPL-3.0 repository metadata. Not current product parity.

Limit: Documentary/source evidence; no independent usability outcome established.

### S36 — TrenchBroom: Repository LICENSE.txt

TrenchBroom contributors. accessed 2026-11-25. Type: source/license identity. [Read source](https://github.com/TrenchBroom/TrenchBroom).

GPL-3.0 metadata; license blob 94a9ed024d3859793618152ea559a168bbcbb5e2.

Limit: Documentary/source evidence; no independent usability outcome established.

### V01 — MapTool: Blast from the Past: Interview with Trevor Croft

Trevor Croft / RPTools. Original interview 2010; republished 2019-03-22. Type: developer retrospective. [Read source](https://www.rptools.net/2019/03/blast-from-the-past-interview-with-trevor-croft/).

Early shared token table and later interface complexity; historical opinions are not current comparative facts.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V02 — MapTool: MapTool repository

RPTools contributors. Live repository read 2026-11-25. Type: original repository / license metadata. [Read source](https://github.com/RPTools/maptool).

Open implementation under AGPL-3.0; not permissive code reuse.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V03 — MapTool: ServerPolicy.java

RPTools contributors. Default branch snapshot read 2026-11-25. Type: source spot-check. [Read source](https://github.com/RPTools/maptool/blob/develop/src/main/java/net/rptools/maptool/server/ServerPolicy.java).

Separate movement, impersonation, individual view and fog policy; blob 37ab58feecbde99f0fa029143ceeaf9aa1475956.

Limit: One policy representation inspected, not request-path enforcement or a security audit.

### V04 — Fantasy Grounds: Press Kit — Fantasy Grounds Classic

Derek Batting / SmiteWorks. Updated 2024-06-17; historical account 2004–2021. Type: official retrospective / archival press kit. [Read source](https://fantasygroundsunity.atlassian.net/wiki/spaces/FGCP/pages/1861877768/Press+Kit+-+Fantasy+Grounds+Classic).

Ruleset layering, Classic retirement and Unity content compatibility. Exact original release day differs from a search-result store listing; use year 2004.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V05 — Fantasy Grounds: Using the Image Control

Derek Batting / SmiteWorks. Live manual; October 2026 examples. Type: official workflow manual. [Read source](https://fantasygroundsunity.atlassian.net/wiki/spaces/FGCP/pages/4349886468).

Play, layers, paint, effects, LOS, lighting and mask modes; documented, not measured usability.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V06 — Roll20: The Future of Tabletop Gaming: Jumpgate Officially Launches

Roll20 / Jayme Boucher. 2025-01-06. Type: release announcement. [Read source](https://blog.roll20.net/posts/the-future-of-tabletop-gaming-jumpgate-officially-launches/).

Default for new games after beta; late-2023 project announcement. Vendor satisfaction claims not treated as independent evidence.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V07 — Roll20: Behind the Scenes: How we 10x’d VTT Performance

Jeff Lamb / Roll20. 2026-01-20. Type: developer performance diary. [Read source](https://blog.roll20.net/posts/10x-vtt-performance-update/).

Parallel engine on existing game data; batching, atlases and ordering limits. Headline gain is workload/hardware dependent.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V08 — Foundry VTT: Year in Review: Five-Year Anniversary Edition

Andrew Clayton and Foundry development team. 2025 anniversary account; exact day not established. Type: developer retrospective. [Read source](https://foundryvtt.com/article/year-in-review-2025/).

ApplicationV2, movement framework and deliberate deferral of disruptive renderer work. Historical account, not latest engine inventory.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V09 — Foundry VTT: Users and Permissions

Foundry VTT. Updated 2025-10-20; v13.350. Type: official permissions documentation. [Read source](https://foundryvtt.com/article/users/).

Role-level and document-level controls; world-scoped users. Version label retained; not an authentication model recommendation for Multiversal.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V10 — Foundry VTT: Release 14.370

Foundry VTT. 2026-11-02. Type: stable release notes. [Read source](https://foundryvtt.com/releases/14.370).

A confirmed shipped v14 baseline, with focus, selection, ownership and level-related fixes; not a complete latest-version survey.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V11 — Owlbear Rodeo: Migrating from Owlbear Rodeo 1.0 to 2.0

Owlbear Rodeo. Live migration guide; original publication date unverified. Type: developer migration rationale. [Read source](https://docs.owlbear.rodeo/docs/migration/migrate-from-1-to-2/).

Storage loss, scene abstraction and retention of simple import path; richer image types and optional extensions.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V12 — Owlbear Rodeo: Extensions: Getting Started

Owlbear Rodeo. Live documentation read 2026-11-25. Type: official SDK architecture documentation. [Read source](https://docs.owlbear.rodeo/extensions/getting-started/).

Manifests, embedded extension UI, contextual items and scene-ready tool lifecycle; not the full engine source.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V13 — Owlbear Rodeo: Scene API

Owlbear Rodeo. Live documentation read 2026-11-25. Type: official API documentation. [Read source](https://docs.owlbear.rodeo/extensions/apis/scene/).

Readiness events, subscription cleanup and partial metadata updates.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V14 — Owlbear Rodeo: Local Scene API

Owlbear Rodeo. Live documentation read 2026-11-25. Type: official API documentation. [Read source](https://docs.owlbear.rodeo/extensions/apis/scene/local/).

Temporary items visible only to current user, separate from shared scene items.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V15 — Owlbear Rodeo: Automatic Fog Detection — 2.4

Mitch McCaffrey. 2026-05-23. Type: developer release journal. [Read source](https://blog.owlbear.rodeo/owlbear-rodeo-2-4-release-notes/).

Editable automatic-fog cleanup and conditional storage conversion; historical beta state superseded by V19.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V16 — Alchemy: Keyboard Shortcuts

Alchemy. 2026-06-06. Type: official UI documentation. [Read source](https://help.alchemyrpg.com/en/articles/10508541-keyboard-shortcuts).

Story, tactical, camera and Zen modes; OmniSearch and topmost-modal handling. Current interaction evidence, weak historical evolution evidence.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V17 — TaleSpire: Publishing Slabs

Bouncyrock. Live guide read 2026-11-25; publication date unverified. Type: official assembly workflow guide. [Read source](https://talespire.com/publishing-slabs).

Selected build assemblies, thumbnail framing and publication workflow; 3D case, not a proposed mandatory dimension for our app.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V18 — TaleSpire: TaleSpire Dev Log 516

Baggers / Bouncyrock. Relative date only in retrieved page; read 2026-11-25. Type: developer journal. [Read source](https://bouncyrock.com/news/articles/talespire-dev-log-516).

Sequences of actions broke vision-limit views; cleanup awaited playtesting/shipping in that post. Do not mark fixed based on intention.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V19 — Owlbear Rodeo: Forecast Released

Mitch McCaffrey. 2026-10-23. Type: developer release journal. [Read source](https://blog.owlbear.rodeo/forecast-released/).

Room-graph improvement and GPU-queue-to-CPU service tradeoff; release to named subscriber tiers, not universal access.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V20 — Roll20: Build Epic VTT Maps in Minutes! Dungeon Scrawl Connects With Roll20

Roll20 / Jayme Boucher. 2025-02-19. Type: integration announcement and workflow. [Read source](https://blog.roll20.net/posts/build-epic-vtt-maps-in-minutes-dungeon-scrawl-connects-with-roll20/).

Connected authoring reduces handoff; explicitly documented save/session and decorative-versus-dynamic-light boundaries.

Limit: Documentary evidence; no independent user trial or runtime verification.

### V21 — Roll20: Enhancing VTT Map Alignment: A Sneak Peek

Fran / Roll20 Senior Product Designer. 2026-08-11. Type: designer diary / pre-release preview. [Read source](https://blog.roll20.net/posts/align-to-grid-designer-diary/).

Guided alignment, contextual hotbar, interactive prototypes and existing-object handling. Preview, not proof of current shipped availability.

Limit: Documentary evidence; no independent user trial or runtime verification.

### A01 — Foundry VTT: Media Optimization Guide

Foundry VTT. Live source read 2026-11-25. Type: official media guide. [Read source](https://foundryvtt.com/article/media/).

Image, alpha, orientation and animation recommendations; bandwidth/decode tradeoffs.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A02 — Foundry VTT: Asset Management

Foundry VTT. Live source read 2026-11-25. Type: official storage guide. [Read source](https://foundryvtt.com/article/asset-management/).

Data folders, upload permissions and protected locations beginning with v13.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A03 — Foundry VTT: Content Packaging Guide

Foundry VTT. Live source read 2026-11-25. Type: official packaging guide. [Read source](https://foundryvtt.com/article/packaging-guide/).

Reusable modules and compendia; v11 Module Maker; path staging and validation. Old example version values are not current compatibility advice.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A04 — Foundry VTT: Backups and Snapshots

Foundry VTT. Live source read 2026-11-25. Type: official backup guide. [Read source](https://foundryvtt.com/article/backups/).

Package-directory backup scope can omit external media; storage amplification and restore boundaries.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A05 — Owlbear Rodeo: Assets

Owlbear Rodeo. Live source read 2026-11-25. Type: official asset UX guide. [Read source](https://docs.owlbear.rodeo/docs/managing-assets/).

Dock, search, tags and import/edit workflow.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A06 — Owlbear Rodeo: Scenes

Owlbear Rodeo. Live source read 2026-11-25. Type: official resource model guide. [Read source](https://docs.owlbear.rodeo/docs/scenes/).

One map image can be referenced by multiple scenes, avoiding repeated large image storage.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A07 — Owlbear Rodeo: Transferring 1.0 data to 2.0

Owlbear Rodeo. Live source read 2026-11-25. Type: official migration guide. [Read source](https://docs.owlbear.rodeo/docs/migration/transfer-from-1-to-2/).

Conversion from .owlbear to .ob2, selective import and compatibility boundary. Guide retains pre-launch wording.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A08 — Roll20: Converting to WebP

Roll20. 2023-01-12 shown by retrieved English page; translations have later dates. Type: official codec guide. [Read source](https://help.roll20.net/hc/en-us/articles/11616928242967-Converting-to-WebP).

Conversion is not guaranteed to shrink; static/animated support differs; inspect the result. Historical test uses Dungeondraft 1.0.4.7.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A09 — Fantasy Grounds: Developer Guide — Product Guideline and Procedures

Fantasy Grounds. Live source read 2026-11-25. Type: official creator guidelines. [Read source](https://fantasygroundsunity.atlassian.net/wiki/spaces/FGCP/pages/3693707267/Developer+Guide+-+Product+Guideline+and+Procedures).

Media-specific limits, player/GM module reuse and optimized asset recommendations; guidelines are not our measured limits.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A10 — Tiled: TMX Map Format

Tiled. Live source read 2026-11-25. Type: official format reference. [Read source](https://doc.mapeditor.org/en/stable/reference/tmx-map-format/).

External TSX references, image paths, offsets and template instances; relative-resource and unknown-field compatibility concerns.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A11 — Dungeondraft community tooling: EightBitz Dungeondraft Tools

Dungeondraft community tooling. Live repository read 2026-11-25; README copyright 2021. Type: original tool-author README. [Read source](https://github.com/EightBitz/Dungeondraft-Tools).

Pack/tag tooling and explicit disk-compression versus decoded-memory distinction. README CC-BY-NC notice, not permissive app reuse.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A12 — MapTool: MapTool 1.9.3 Released

MapTool. 2021-07-13. Type: official release notes. [Read source](https://www.rptools.net/2021/07/maptool-1-9-3-released/).

Historical cache loading, UVTT light import, ownership and overwrite defects were separately fixed.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A13 — LDtk: JSON Documentation

LDtk. Retrieved JSON 1.5.3 documentation. Type: official format entry and schema links. [Read source](https://ldtk.io/json/).

Versioned JSON format and deprecation documentation; no claim of a universally stable schema.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A14 — Dungeon Alchemist: The Treasury Update is Live

Dungeon Alchemist. 2023-08-31. Type: developer release journal. [Read source](https://www.dungeonalchemist.com/post/the-treasury-update-is-live).

3D custom-asset import/configuration and Steam Workshop sharing.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A15 — TaleSpire: FAQ: Modding / TaleWeaverLite

TaleSpire. Live source read 2026-11-25. Type: official capability FAQ. [Read source](https://talespire.com/faq).

Unity-compatible mini import and mod.io distribution; broader asset import listed as future, not shipped proof.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A16 — Wonderdraft: PACK_LICENSE.txt

Wonderdraft. Repository snapshot read 2026-11-25. Type: vendor license source. [Read source](https://github.com/Megasploot/Wonderdraft/blob/master/PACK_LICENSE.txt).

Separates derived-work distribution from standalone asset redistribution; blob d6aa6646efae78b9805d24502be8352428495fe7.

Limit: Specific license example, not a legal clearance for our supplied sheets.

### A17 — Unity Addressables: Managing Addressable Asset Memory

Unity Addressables. Addressables 2.7.6 docs, not verified package in our app. Type: official runtime guide. [Read source](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/memory-assets.html).

Reference-counted loads/releases and bundle lifetime; released assets need not immediately free memory.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A18 — Unity Addressables: Introduction to Update Builds

Unity Addressables. Addressables 2.7.6 docs, not verified package in our app. Type: official content update guide. [Read source](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/content-update-builds-overview.html).

Update catalogs, changed bundles and platform/release content state; avoid indiscriminate full redownload.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A19 — Khronos KTX: KTX File Format Specification

Khronos KTX. Specification revision 2.0.4, 2025-02-20. Type: primary graphics specification. [Read source](https://registry.khronos.org/KTX/specs/2.0/ktxspec.v2.html).

Texture level indices, GPU formats and supercompression; runtime texture representation differs from ordinary image delivery.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A20 — Mozilla MDN: Storage Quotas and Eviction Criteria

Mozilla MDN. Page modified 2026-01-05. Type: browser API documentation. [Read source](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria).

Best-effort versus persistent data, quota failures and browser-specific eviction. No universal storage promise.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A21 — Khronos glTF: glTF 2.0 Specification

Khronos glTF. Retrieved specification 2.0.1, 2021-10-11. Type: primary 3D specification. [Read source](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html).

GLB container versus external resources; a GLB can still reference external media.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A22 — W3C SVG: SVG 2 Conformance Criteria

W3C SVG. Live source read 2026-11-25. Type: primary vector specification. [Read source](https://www.w3.org/TR/SVG/conform.html).

SVG processing contexts differ; secure static mode disables scripts, external references and animation.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A23 — OWASP: File Upload Cheat Sheet

OWASP. Live source read 2026-11-25. Type: official security guidance. [Read source](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html).

Validate content, permissions and expanded resource limits; archive and decoder threat handling.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A24 — Dungeondraft: Modding API: Globals

Dungeondraft. Live source read 2026-11-25. Type: official API documentation. [Read source](https://megasploot.github.io/DungeondraftModdingAPI/Globals/).

Existing world, tool, exporter and asset category integration; public API is not an open engine implementation.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A25 — Tiled: TMX Changelog

Tiled. Live source read 2026-11-25. Type: official format change history. [Read source](https://doc.mapeditor.org/en/stable/reference/tmx-changelog/).

Chunked infinite maps, templates, compression and later field-renaming compatibility changes.

Limit: Documentary evidence; no installed or comparative device acceptance.

### A26 — NCG DAMC: CURRENT — Digital Asset, Media & Content Pipeline Engineering

NCG DAMC. Pinned NCG source 8f5baac…; read 2026-11-25. Type: pinned project research status. [Read source](https://github.com/cybalicistjt-stack/NCG/blob/8f5baac1b5e7d273b23fde52c7122c9138b2b15d/docs/damc/CURRENT.json).

First-pass research and synthetic tests; independent-host and real app proofs remain open.

Limit: Read-only advisory; active follow-on, not product acceptance.

### A27 — NCG DAMC: DAMC29 Practitioner Handbook

NCG DAMC. 2026-10-08 on pinned source. Type: pinned project research synthesis. [Read source](https://github.com/cybalicistjt-stack/NCG/blob/8f5baac1b5e7d273b23fde52c7122c9138b2b15d/docs/damc/handbook/DAMC29_PRACTITIONER_HANDBOOK.md).

Logical asset, immutable blob, representation, recipe, derivative, delivery projection and offline pack distinctions.

Limit: Design synthesis; no product adoption or independent real-boundary acceptance.

### A28 — NCG DAMC: DAMC30 First-Pass Audit and Research Debt

NCG DAMC. 2026-10-08 on pinned source. Type: pinned project research limitations. [Read source](https://github.com/cybalicistjt-stack/NCG/blob/8f5baac1b5e7d273b23fde52c7122c9138b2b15d/docs/damc/handbook/DAMC30_FIRST_PASS_AUDIT_AND_RESEARCH_DEBT.md).

Explicit NOT_RUN real-byte, device, cache/privacy, install/restore and economics tests; R1 status superseded by family CURRENT.

Limit: Historical debt inventory is subordinate to current family status.

## Reproducibility and delivery receipt

The companion evidence package includes the 85-record source ledger, 24-step JSON/CSV backlog, retained recommendation/task tables, local sheet audit and codec methodology, report builder, validation receipt and the OPS5 log receipt when publication is complete. The original images and 58.7 MB app are not duplicated into the study. No third-party implementation or full source articles are redistributed.

The new local experiment used the existing 22 JPEG sheets, checked their prior SHA256 identities, encoded WebP quality75/method4 in memory and compared decoded pixels with the decoded source JPEG. It did not change files, approve the artwork, benchmark a client, exercise a live cache or validate security. Timings are retained with their environment and operation boundaries in asset_audit.json. The prior focused UHT28 receipts remain bounded earlier engineering evidence.

The UHT28 SHA256 is ab66ac31aeacec06b3a78db9e4689532774c0a7d21b6ecd957f1367ce43eb9d2. Report/source anchors, script syntax, filter/reset behavior, dependency acyclicity, recommendation coverage, source references, plan status and baseline preservation are checked locally. No installed-device, competitor runtime, recipient import, participant study or live multiplayer acceptance is claimed in this cycle.
