# STAGE-A-A10 Repository Compatibility + Implementation Contracts — Handoff v0.2.0

Status: **PREIMPLEMENTATION COMPATIBILITY COMPLETE — NOT ACTIVATED**

Owner and final authority: **John Brandon Turner**

Prepared against Multiversal-app main:

`dced7f92163050690c807c1fda937146bb8dce85`

## Artifact

`STAGE_A_A10_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`

SHA-256:

`e8ce3f27a506ff9d34f6b67b4d5b0b9d665724fcf31ad59f88da7f1e12b28279`

Nested source-backed package:

`STAGE_A_A10_WORLD_CONTENT_AUTHORING_PREIMPLEMENTATION_v0.1.0.zip`

SHA-256:

`8a06165bec35a47aa8d24b4bbab1450c11d19e5112f8cf1221ffebc22d27ac6f`

Validator:

`STAGE-A-A10 REPOSITORY COMPATIBILITY + CONTRACTS v0.2.0: PASS`

Validated counts:
- repository/predecessor anchors: 32
- blocking gaps/risks: 26
- owning-domain/cross-domain decisions: 11
- planned provider-neutral contracts: 32
- exact future path actions: 70
- source-slice coverage: all 32 WSM/AM/CC/AI authoring slices
- reuse/composition decisions: 20
- validation/CI lanes: 28
- implementation invariants: 37

## Compatibility verdict

**COMPATIBLE WITH SPLIT D06/D07/D18/D28/D29/D05 AUTHORING CONTRACTS AND ADDITIVE STORAGE.**

A10 must preserve these canonical ownership boundaries:

- D06 `pack-registry` — pack manifest/version/install/enable/disable/pinning lifecycle;
- D07 `entity-catalog` — reusable definitions, versions, variants, dependency identity;
- D18 `world-location-map` — World/location/semantic geography/map structural state;
- D28 `adventure-travel` — Adventure definitions, Module graphs, Campaign run-local progression;
- D29 `authoring-provenance` — drafts, proposals, reviews, publication provenance, creator/local authoring workflow;
- D05 `visibility-projection` — audience-safe authoring/content projections;
- D13 `media-attachments` — media/attachment payload ownership referenced from D18.

The canonical bounded-domain rule remains controlling: each domain writes only its owned canonical persistence. Cross-domain authoring uses public contracts, stable references, expected versions, Events, reservations/sagas where required, and compensation. A10 must not create a monolithic shared authoring/content table.

## Existing storage foundation

`database/migrations/0001_initial_logical_schema.json` remains immutable.

It already provides:
- `content_packs` with stable ID, version, visibility and manifest;
- `canonical_objects` with pack ID, stable ID, object type, version, visibility, payload and provenance.

A10 should reuse these structures where they satisfy D06/D07 semantics rather than replace them.

They are not sufficient by themselves for the complete A10 source model. Drafts, immutable review proposals, review decisions, Campaign overlays, Adventure run-local state, source-migration decisions, import mappings and similar records remain distinct semantics. The exact additive physical decomposition is intentionally deferred until A2-A9 migrations exist and every record has one canonical owner.

## Authoring authority

The completed IA-D07 authority matrix remains controlling. Ownership, authorship, edit, review, publish, install, enable, reveal, runtime advance, export, import, deprecate, delete and canonical-promotion authority are independent.

Creator approval, private publication, Campaign installation, import, GM reveal/use or source ownership does not imply canonical promotion.

Canonical promotion remains an explicit owner-only gate requiring John Brandon Turner and is not authorized by A10 preparation.

Stage A also retains the explicit rule that Jordon/Zakk contributions remain proposals or drafts until owner-approved canonical promotion.

## A9/A10 boundary

A9 owns Campaign-runtime relationship/faction/social/investigation state.

A10 owns reusable World/Setting/Adventure/creator content authoring and governed source publication/install artifacts.

Runtime state may become an A10 draft only through an explicit provenance-preserving clone/propose workflow. It never silently becomes reusable or canonical content.

## Hidden-information rule

Private drafts, rejected proposals, hidden entries, hidden dependencies, future Adventure branches/scenes, GM-only mechanics, Campaign-local secrets and unpublished releases must be removed before:

- search/autocomplete;
- counts/totals and review-queue ranking;
- dependency or branch graphs;
- semantic map outlines;
- previews;
- exports and diagnostics;
- notifications;
- optional-AI context.

D05 is the reusable projection boundary. UI-only hiding is insufficient.

## Creator-content sandbox

Before Campaign installation, bounded creator content validates:

- schemas;
- stable IDs;
- references and dependency closure;
- processor allowlists;
- resource bounds;
- permissions;
- hidden-information behavior;
- deterministic fixtures.

Arbitrary code, executable scripts, network calls, secrets and unrestricted processors remain prohibited.

Installed creator/local content must use the same runtime permission, proposal, result, Asset, map, vehicle, World and Adventure contracts as canonical content.

## Source identifier notes

A source conflict is preserved rather than silently corrected:

- `INTERNAL_ALPHA_DEPENDENCY_MAP.md` uses F018 for Downtime/Crafting/Projects;
- IA-D07-003 source text labels Creator/Campaign-local Content as bounded F018.

Use **IA-D07-003** work-item identity for creator/Campaign-local content until canonical reconciliation exists.

Also, IA-D07-005 slice IDs `AI-S01` through `AI-S08` mean **Authoring Integration**, not Stage A11 artificial-intelligence authority.

## Dependency and implementation hold

A10 remains sequentially behind A2-A9.

This handoff does not:
- activate A10;
- create an A10 application branch;
- advance the application current-work pointer;
- authorize canonical promotion;
- authorize autonomous publication;
- authorize real-user content intake or a public marketplace;
- authorize a paid service or production credential;
- authorize internal-alpha release, deployment or public release;
- authorize a new graph/map/editor/state-management/provider runtime dependency.

A2 remains the authorized current Stage A implementation work item.

## Exact next preparation step

Prepare **Stage A11 — Contextual AI Interfaces** from the completed IA-D08 optional-AI design series, preserving A2 retrieval, A3 permissions, A6 proposal/review, A9/A10 hidden-information/provenance boundaries, explicit cost/fallback behavior and the rule that AI may draft or suggest but never publish, reveal hidden information, make authoritative decisions, or bypass human approval.
