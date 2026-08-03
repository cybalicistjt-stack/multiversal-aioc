# Multiversal Content Recovery and Ingestion Roadmap

**Document ID:** MV-CONTENT-RECOVERY-001  
**Version:** 1.0.0  
**Status:** ACTIVE — OWNER APPROVED  
**Owner and final authority:** John Brandon Turner  
**Repository:** `cybalicistjt-stack/multiversal-aioc`  
**Approved:** 2026-08-03

## Mission

Recover the years of existing Multiversal content losslessly, make it searchable and usable in the Content Library, and normalize it into COS only where deterministic evidence supports the mapping.

> Recover the content first. Use the COS to organize it second.

This workstream is not a new Development Brain release. Releases A–G remain complete. It is an application of the governed AIOC and Development Brain to the existing Multiversal content corpus.

## Verified starting evidence

The live Content Library currently exposes 487 records from the `Multiversal Phase 1–8 canonical object bundle`. That count is a partial extraction, not the complete Multiversal corpus.

A source census over the available archive set found:

- 47,849 structured-file occurrences;
- 11,912 unique structured files after exact SHA-256 deduplication;
- 5,123 unique files likely to contain game content;
- 291,724 exact-file-deduplicated source rows or JSON entries classified as likely content.

A neutral recovery-ledger pass extracted:

- 359,291 source records;
- 294,571 unique exact payloads;
- 64,720 exact duplicate payload rows;
- 99,761 rows with source-provided IDs;
- 259,530 rows assigned stable recovery identities;
- 185,243 conservative identity groups;
- 33,609 identities with multiple distinct payload variants.

These totals are recovery records, not a final count of unique game objects. They include primary assets, relationships, indexes, mappings, embedded mechanics, reports, and support records.

## Non-negotiable recovery rules

1. Original source payloads remain preserved and retrievable.
2. Content is not discarded because it does not fit the current COS schema.
3. Deterministic evidence outranks AI semantic inference.
4. Evidence order is: stable ID, explicit type, pack metadata, source file/workbook, sheet/table, field names, directory, cross-references, record shape, then AI-assisted review.
5. Exact duplicates may be collapsed operationally but remain traceable to all occurrences.
6. Variants and conflicts are preserved; they are never silently merged or overwritten.
7. Uncertain records enter as partially mapped, structured raw, or unresolved assets rather than being lost.
8. The existing 487-record database remains restorable throughout recovery.
9. Representative samples must be reviewed before a domain is promoted from staging.
10. Do not create deeper semantic subsystems unless a specific observed failure proves one is necessary.
11. Success is measured against the source corpus and reconciliation evidence, not against the current live count.
12. John Brandon Turner retains final approval authority for promotion, conflict resolution, and production migration.

## Phase 0 — Preserve and freeze

**Purpose:** Protect source archives, the current 487-record database, and generated recovery evidence.

Work:

1. Record checksums for all source archives and packages.
2. Snapshot the current live database and deployment fingerprint.
3. Preserve the census, recovery ledger, payload archive, collision ledger, and error reports.
4. Establish read-only source inputs and separate generated outputs.
5. Prevent normalization from overwriting original payloads.

Exit criteria:

- Every source and recovery artifact has a stable checksum.
- The current library can be restored exactly.
- Original payloads cannot be overwritten by later mapping.

Estimated bounded batches: 1.

## Phase 1 — Deterministic Classification Contract

**Purpose:** Define reproducible classification without beginning with semantic guesses.

Primary record classes:

- primary game-asset candidate;
- relationship or edge;
- reference or index;
- supporting structured record;
- balance or test record;
- source note;
- manifest or governance record;
- technical artifact.

Mapping outcomes:

- `native-cos`;
- `cos-mapped`;
- `partially-mapped`;
- `structured-raw`;
- `unresolved`;
- `support-record`;
- `technical-excluded`.

Confidence levels:

- `exact`;
- `strong`;
- `partial`;
- `unresolved`.

Work:

1. Define machine-readable rules using explicit IDs, types, pack metadata, source paths, sheets, fields, and record shapes.
2. Define precedence and conflict behavior.
3. Build a mixed-domain representative fixture.
4. Record expected classifications.
5. Measure errors and revise only rules with observable failures.

Exit criteria:

- The fixture classifies reproducibly.
- Most classifications do not require AI inference.
- Uncertain records remain preserved rather than forced.

Estimated bounded batches: 1–2.

## Phase 2 — Primary assets versus support records

**Purpose:** Prevent inventories, reports, mappings, and relationship rows from being presented as game objects.

Work:

1. Apply the classification contract to the recovery ledger.
2. Separate primary assets from edges, support records, indexes, reports, governance, and technical artifacts.
3. Group exact duplicate payloads while retaining all provenance.
4. Attach support records and references to likely primary identities.
5. Review representative samples from every classification.

Exit criteria:

- Primary candidates are separated from support and technical records.
- Duplicate counts reconcile.
- Sample review finds an acceptable and documented error rate.

Estimated bounded batches: 1–2.

## Phase 3 — Identity, version, and variant groups

**Purpose:** Determine which records describe the same asset without destroying alternate forms or revisions.

Identity evidence order:

1. exact stable ID;
2. legacy ID;
3. pack ID plus local ID;
4. explicit cross-reference;
5. deterministic normalized name plus domain and source context;
6. owner or manual review when required.

Work:

1. Establish identity groups and recovery IDs.
2. Distinguish exact duplicates, revisions, variants, alternate forms, and true conflicts.
3. Preserve all payloads and source locations.
4. Build supported version chains.
5. Produce identity-confidence and conflict reports.

Exit criteria:

- Every primary candidate has an identity or recovery ID.
- No record is lost through deduplication.
- Variants and conflicts remain explicitly visible.

Estimated bounded batches: 2.

## Phase 4 — Domain recovery passes

Domains proceed separately so errors remain bounded and reviewable:

1. abilities, actions, effects, traits, and conditions;
2. species, subspecies, forms, cultures, and adaptations;
3. items, weapons, armor, materials, and crafting assets;
4. creatures, companions, mounts, and summons;
5. NPCs, factions, relationships, and social roles;
6. vehicles and components;
7. environments, hazards, traps, and terrain;
8. worlds, regions, locations, and settings;
9. adventures, scenes, encounters, clues, and rewards;
10. core rules, resources, progression, and rules profiles.

Each domain pass must:

1. identify authoritative sources;
2. extract matching ledger records;
3. apply deterministic classification;
4. reconcile duplicates;
5. group identities and variants;
6. map fields only where reliable;
7. preserve unmapped fields and complete original payloads;
8. attach support records and relationships;
9. generate an import-ready package;
10. review representative examples;
11. load into staging;
12. validate search, filtering, selection, and detail display.

Per-domain deliverables:

- source inventory;
- identity ledger;
- direct-COS objects;
- partial mappings;
- structured-raw assets;
- support records;
- variant and conflict report;
- staging import package;
- validation report.

Exit criteria:

- Source totals reconcile.
- Representative records retain their original detail.
- No fields are silently dropped.
- Assets open correctly in staging.

Estimated bounded batches: 14–20 total.

## Phase 5 — Lossless library import format

**Purpose:** Allow useful recovered content into the library before perfect COS normalization.

Every imported record must preserve:

- identity and recovery identity;
- source classification and domain;
- display name and source type;
- COS type when supported;
- mapping state and confidence;
- mapped fields;
- unmapped fields;
- complete original payload or immutable payload reference;
- source provenance;
- versions, variants, and conflicts;
- relationships;
- validation state.

Work:

1. Define the neutral import record.
2. Build generator and validator.
3. Index mapped and unmapped fields for search.
4. Prove examples for every mapping state.
5. Ensure future COS upgrades do not require source re-extraction.

Exit criteria:

- Partial and raw structured records can be used without data loss.
- Original content remains retrievable.
- Search covers preserved source fields.

Estimated bounded batches: 2.

## Phase 6 — Staging Content Library integration

**Purpose:** Prove usability and performance before production migration.

Work:

1. Maintain a staging database separate from the current live database.
2. Load domain packages incrementally.
3. Show source coverage and mapping state clearly.
4. Add filters for domain, source, mapping state, confidence, and conflict status.
5. Show mapped and original source views.
6. Preserve direct access to variants.
7. Test desktop and mobile interactions.
8. Test large-corpus search and rendering performance.
9. Test export, backup, restoration, and rollback.

Exit criteria:

- Thousands of recovered assets can be searched and opened.
- Original payloads remain accessible.
- Mobile and desktop interactions work.
- Performance and restore tests pass.

Estimated bounded batches: 2–3.

## Phase 7 — Coverage and quality validation

**Purpose:** Establish evidence that recovery succeeded rather than relying on green schemas alone.

Required metrics:

- source files scanned;
- records extracted;
- duplicate payloads;
- primary candidates;
- unique identities;
- variants and conflicts;
- native or mapped COS objects;
- partial mappings;
- structured-raw assets;
- support records;
- unresolved and unreadable records;
- records visible in staging.

Work:

1. Reconcile every domain against source totals.
2. Compare sampled recovered records to original payloads.
3. Verify IDs, names, descriptions, mechanics, relationships, and provenance.
4. Test known owner-selected objects.
5. Test unusual and edge-case formats.
6. Detect truncation or silent field loss.
7. Document unresolved gaps honestly.

Exit criteria:

- Totals reconcile into explained categories.
- No unexplained large-scale losses remain.
- Representative assets match their sources.
- Owner approves recovery quality.

Estimated bounded batches: 2.

## Phase 8 — Production migration

**Purpose:** Replace the misleading 487-only presentation with the approved recovered library safely.

Work:

1. Retain the 487 records as a named source collection.
2. Add approved recovered collections.
3. Migrate staging to production.
4. Display totals by source and mapping state.
5. Remove any implication that 487 records represent the complete corpus.
6. Run production smoke and interaction tests.
7. Verify rollback.
8. Record the deployed corpus fingerprint.

Exit criteria:

- Approved recovered assets are available in production.
- The original 487 remain intact and correctly labeled.
- Counts match the approved coverage report.
- Rollback is tested.

Estimated bounded batches: 1–2.

## Phase 9 — Gradual COS normalization

**Purpose:** Improve structure over time without withholding recovered content.

Work proceeds by owner-approved priority. Partial and raw records remain usable while clearer mappings, relationships, validation, and conflict resolutions are added. Original payloads are never discarded after normalization.

This phase is ongoing and must not become a prerequisite for using recovered content.

## Milestones

### Milestone A — Recovery foundation

Phases 0–3. Every source record is preserved, classified, and assigned an identity or recovery ID.

Estimated batches: 5–7.

### Milestone B — Domain recovery

Phase 4. Every major domain has an import-ready package.

Estimated batches: 14–20.

### Milestone C — Usable staging library

Phases 5–6. The recovered corpus is searchable and inspectable in staging.

Estimated batches: 4–5.

### Milestone D — Certification and production

Phases 7–8. Recovery is reconciled, owner-reviewed, and safely deployed.

Estimated batches: 3–4.

### Milestone E — Ongoing normalization

Phase 9. COS quality improves without blocking access to content.

## Overall estimate

- 26–36 bounded batches through production certification;
- four major milestones before production;
- early usable staging results after the first domain packages and neutral import format;
- no manual recreation of the original game content.

## Current exact next executable work item

**Phase 0 — Preserve and Freeze, followed immediately by Phase 1 — Deterministic Classification Contract.**

The first implementation batch must:

1. preserve and checksum the available census and recovery-ledger evidence;
2. snapshot the current 487-record database and deployment fingerprint;
3. define the machine-readable classification vocabulary, precedence, mapping states, and confidence levels;
4. create a mixed-domain representative fixture with expected outcomes;
5. validate deterministic classification behavior;
6. update current state and handoff with evidence.

Do not classify the entire 359,291-row ledger until the mixed-domain fixture passes review.
