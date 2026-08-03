# AIOC Session Handoff

**Status:** CONTENT RECOVERY AND INGESTION ACTIVE — PHASE 0/1 NEXT  
**Owner and final authority:** John Brandon Turner  
**Repository:** `cybalicistjt-stack/multiversal-aioc`  
**Branch:** `main` after governance PR merge  
**Handoff date:** 2026-08-03

## Completed workstreams

- Operational AIOC certification — COMPLETE
- Development Brain Releases A–G — COMPLETE AND BEHAVIORALLY VALIDATED
- Content Library mobile COS selection repair — merged through PR #23
- Source census — COMPLETE
- Neutral recovery ledger — COMPLETE
- Content Recovery and Ingestion roadmap — OWNER APPROVED

## Current problem statement

The live Content Library exposes 487 records from the Phase 1–8 canonical bundle. Those records are a partial extraction and do not represent the years of existing Multiversal content.

The owner does not authorize recreating that content manually. The active objective is to recover and use the existing content corpus losslessly, whether records map directly into COS or must first enter as partially mapped or structured-raw assets.

## Verified evidence

Source census:

- 47,849 structured-file occurrences;
- 11,912 unique structured files;
- 5,123 unique content-likely structured files;
- 291,724 exact-file-deduplicated likely-content rows or JSON entries.

Neutral recovery ledger:

- 359,291 source records;
- 294,571 unique exact payloads;
- 64,720 exact duplicate payload rows;
- 99,761 source-provided IDs;
- 259,530 stable recovery identities;
- 185,243 conservative identity groups;
- 33,609 multi-payload identity groups.

These are recovery records, not a final unique game-object count.

## Governing doctrine

> Recover the content first. Use the COS to organize it second.

Do not:

- begin with broad AI semantic classification;
- discard records that fail COS mapping;
- silently merge or overwrite variants;
- treat indexes, mappings, reports, or relationship rows as primary game objects;
- classify the entire ledger before representative deterministic rules pass;
- create subsystems of subsystems to chase uncertain semantics.

Do:

- preserve complete original payloads and provenance;
- classify from stable IDs, explicit types, pack metadata, source files, sheets, fields, directories, and cross-references before semantic review;
- preserve partial, raw, unresolved, duplicate, variant, and support-record states;
- use staging and representative review before production promotion;
- keep the current 487-record database restorable.

## Canonical roadmap

Read:

- `governance/content-recovery/CONTENT_RECOVERY_ROADMAP.md`

Roadmap phases:

0. Preserve and freeze
1. Deterministic Classification Contract
2. Primary assets versus support records
3. Identity, version, and variant groups
4. Domain recovery passes
5. Lossless library import format
6. Staging Content Library integration
7. Coverage and quality validation
8. Production migration
9. Gradual COS normalization

## Exact next executable work item

Execute one bounded Phase 0/1 foundation batch:

1. Preserve the source-census and neutral-ledger evidence with checksums and provenance.
2. Snapshot the current 487-record Content Library database and deployed build fingerprint.
3. Define a machine-readable deterministic classification contract containing:
   - primary record classes;
   - mapping states;
   - confidence levels;
   - evidence precedence;
   - conflict and fallback behavior.
4. Build a mixed-domain representative fixture from abilities, species, items, creatures, NPCs, vehicles, environments, worlds/adventures, rules, relationship rows, reports, and technical artifacts.
5. Record expected classifications from objective source evidence.
6. Run and validate the fixture.
7. Report observed errors without widening scope.
8. Update the governed handoff only after validation.

**Hard gate:** Do not run full-ledger classification over 359,291 records until the representative fixture passes review.

## Authority boundary

John Brandon Turner retains final approval over classification policy, conflict resolution, domain promotion, staging acceptance, and production migration. AI and deterministic tooling may propose and validate but may not silently discard, merge, promote, or certify recovered content.

## Separate workstream

`WP-011 — Tauri iOS/iPadOS Spike` remains a separate Mac-dependent Multiversal App task and does not replace the content-recovery workstream unless the owner explicitly switches priorities.
