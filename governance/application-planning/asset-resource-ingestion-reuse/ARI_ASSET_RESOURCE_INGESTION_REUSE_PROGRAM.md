# ARI — Asset Resource Ingestion & Reuse

**Program ID:** ARI  
**Program name:** Asset Resource Ingestion & Reuse  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; NOT STARTED  
**Activation:** after SGC-08  
**Successor:** MIB-16  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-07

## Purpose

ARI makes user-owned, first-party/native, generated, imported and provider-referenced creative resources reusable across Multiversal instead of trapping them inside the feature where they first entered. The governing product rule is:

> Import once, generate once, retain one governed identity/lineage, and reuse everywhere the asset's capabilities, permissions and rights allow.

ARI is the common resource-library and ingestion layer beneath existing owning systems. It does not replace MAI map/visual semantics, AAI audio semantics, PAPT production-art authority, Character/CAPP appearance truth, Scene truth, inventory/Asset ownership, publishing authority or rights/provenance owners.

## Required behavior

- User-supplied collections like ZIP/RAR/7z resource packs may be ingested in bulk through safe staging rather than one-file-at-a-time upload.
- Native Multiversal assets and PAPT/CAPP-generated derivatives register through the same resource interface as user-owned assets.
- Provider-referenced resources may appear in the same catalog when legitimate reference/control semantics exist, but reference/control never implies byte ownership, extraction or redistribution rights.
- Maps, tilesets, sprites, portraits, tokens, props, icons, audio, animations, documents and future 3D derivatives may share catalog/search/provenance infrastructure while retaining type-specific owning-domain semantics.
- ARI indexes large libraries and retrieves lazily; “massive use” does not mean loading the whole library into memory.
- Rights are capability-specific. Possession of bytes does not automatically grant transform, export, redistribution or commercial-use authority.
- Unknown, unsupported, malformed, denied, missing or revoked states stay explicit and fail closed where required.

## Tranche sizing rule

Every ARI implementation tranche is designed for a **24-minute-or-less bounded execution target under a healthy governed environment**, including its focused construction/validation package. If the actual acceptance surface cannot credibly fit that bound, it must be split before governed start rather than expanding the tranche. Final repository/runner latency remains an external condition and does not justify weakening acceptance.

## Tranches

### ARI-01 — Universal Resource Handle & Capability Contract
Define provider-neutral resource identity, media kind, owning-domain reference, source class, availability and permitted-use capabilities. Completion proves consumers can reference one resource without creating a second canonical asset ledger.

### ARI-02 — Content-Addressed Byte Identity & Deduplication
Define digests, original-byte identity, duplicate detection, byte-present versus reference-only state and storage-neutral content addressing.

### ARI-03 — Derivative & Lineage Graph
Define original → thumbnail/preview/transcode/crop/render/export relationships, version lineage, stale derivative detection and replacement/supersession without mutating source truth.

### ARI-04 — Safe ZIP Staging & Extraction
Implement bounded ZIP intake with path-traversal, archive-bomb/size, nested-depth, malformed-entry and cancellation protections; extraction is staging, not automatic canon/import acceptance.

### ARI-05 — RAR/7z Archive Adapter Contract
Add governed RAR/7z extraction adapters with explicit runtime-capability detection and unsupported diagnostics rather than silently pretending extraction succeeded.

### ARI-06 — Recursive Discovery & Media Classification
Discover staged files recursively and classify actual media/container type independently of filename extension; preserve unknowns and raw source metadata.

### ARI-07 — Sidecar / Manifest Parser Adapter Framework
Provide deterministic parser adapters for XML/JSON/text sidecars and pack manifests with raw unsupported metadata preservation.

### ARI-08 — Syrinscape Soundset XML Adapter
Parse user-supplied Syrinscape-style soundset metadata and associate semantic names/grouping with local audio files without provider scraping, account extraction or rights promotion.

### ARI-09 — Map, Tileset & Variant-Family Recognition
Recognize related floors, grid/no-grid, print/VTT, tile, prop and other filename/manifest variants as one governed family with child variants where evidence supports that grouping.

### ARI-10 — Batch Import Transaction & Recovery
Implement stage → inspect → user accept/reject → commit semantics with cancellation, resumable cursors, partial-failure isolation and idempotent retry.

### ARI-11 — Rights, License & Use-Capability Matrix
Record evidence for private use, transform, campaign use, export, redistribution, commercial use and unknown/denied/revoked states. Downstream systems must filter actions through these capabilities.

### ARI-12 — Visual Derivative Worker
Create bounded thumbnails, previews, transparent/cropped display derivatives and dimension/color metadata while retaining original bytes and provenance.

### ARI-13 — Audio Metadata & Playback Derivative Worker
Extract duration/codec/channel metadata and safe waveform/playback proxies where permitted, without replacing originals or implying export/redistribution rights.

### ARI-14 — Semantic Tags, Collections & Family Grouping
Add deterministic evidence-backed tags, user tags, collections and variant groups. Optional AI suggestions remain proposals and may not alter source/rights/canon truth.

### ARI-15 — Large-Library Query, Pagination & Lazy Retrieval
Define indexed search/filter/sort/pagination and bounded lazy loading. Prove representative 1k/10k/50k synthetic catalog tiers without requiring whole-library memory residency.

### ARI-16 — MAI Bridge
Resolve ARI visual resources into MAI map/package/placeable/tileset workflows while MAI remains owner of map visual semantics, coordinates, layers and import translation.

### ARI-17 — AAI Bridge
Resolve local and provider-referenced audio through ARI catalog/search semantics while AAI remains owner of audio source/asset/cue/soundscape/playback/provider capability semantics.

### ARI-18 — PAPT, CAPP & Native Asset Registration Bridge
Register first-party/native assets and generated CAPP/PAPT outputs automatically into ARI with source entity, renderer/tool, version, rights and derivative lineage.

### ARI-19 — Universal Asset Picker / Resource Query API
Provide one permission- and capability-aware selection/query contract consumable by Scene, Character, Creator, VTT, SAA and later P3D surfaces.

### ARI-20 — Resource Pack Intake UX
Provide archive/folder drop/select, discovery summary, family preview, duplicate/unsupported warnings, provenance/rights review and bulk acceptance with accessible non-drag alternatives.

### ARI-21 — Missing Source, Relink & Derivative-Rebuild Recovery
Handle moved/deleted local sources, unavailable provider references, stale derivatives and explicit relink/rebuild operations without silent substitution.

### ARI-22 — Golden Bulk-Ingestion, Cross-System & Scale Proof
Prove imported + native + generated + reference-only resources through one catalog, including a resource-pack fixture shaped like the owner-provided example: multi-soundset local OGG/XML content plus a multi-floor map collection with print/grid/no-grid variants. Prove cross-system reuse, rights filtering, lazy retrieval, deterministic receipts and recovery behavior.

## Cross-system ownership

- **MAI** owns visual/map package and placeable semantics; ARI owns reusable resource identity/bytes/reference/lineage/catalog concerns.
- **AAI** owns audio provider/source/cue/soundscape/playback semantics; ARI owns reusable local/reference catalog concerns.
- **PAPT/CAPP** own renderer/appearance and production-generation semantics; generated output is registered through ARI instead of creating a separate distribution library.
- **SAA** consumes ARI references and creates provenance-linked composition derivatives; it does not duplicate source files by default.
- **P3D** later consumes renderer-neutral appearance/resource semantics and registers generated meshes back through ARI.
- **D29/publishing/provenance owners** retain canonical/publication authority. ARI existence never promotes canon or commercial clearance.

## Non-activation boundary

Planning ARI does not authorize application implementation, migration, production storage selection, content upload to a hosted service, provider credentials/network access, scraping/ripping/reverse engineering, external redistribution, commercial publication, tester distribution or release/deployment. Selection requires a later governed start after SGC-08.

## Completion standard

ARI completes only when ARI-01..22 are `completed_verified`, downstream systems can reuse the same governed resource identity without one-off shadow libraries, large-library behavior is bounded, third-party rights remain independently enforceable, and the golden bulk-ingestion proof demonstrates practical mass reuse rather than a schema-only design.