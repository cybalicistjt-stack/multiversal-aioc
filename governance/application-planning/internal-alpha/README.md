# MV-IA-001 — Internal Alpha Feature Design Program

**Document ID:** MV-IA-001  
**Version:** 0.11.0  
**Status:** ACTIVE — DESIGN PROGRAM  
**Owner and final authority:** John Brandon Turner

## Purpose

MV-IA-001 converts the approved Project Bible, Stage A program, Phase 9 architecture, and historical feature roadmap into implementation-ready internal-alpha design contracts. It does not bypass P9-06 or authorize release.

## Completed foundations

IA-D01 and IA-D02 are complete. Shared contracts cover governed objects, identity, authority, projections, persistence, recovery, diagnostics, accessibility, provider neutrality, and zero-service operation.

## Completed preparation packets

- IA-D03-001 — Character Creation and Advancement.
- IA-D03-002 — Campaign, Scene, and Session Builder.
- IA-D03-003 — Encounter Builder and Balance Lab.

## IA-D03-002 — Campaign, Scene, and Session Builder

Complete at design level with Campaign rules and packs, invitations and membership, roles and Character control, Scene drafts and stable-ID placements, Campaign-local overrides, notes, accessible map alternatives, Player-safe previews, launch validation, immutable launch snapshots, Session lifecycle, Event recovery, exports, diagnostics, accessibility, and twenty blocking acceptance criteria.

## IA-D03-003 — Encounter Builder and Balance Lab

Complete at design level with governed Encounter composition, stable-ID provenance, dependency and compatibility validation, twelve independent pressure dimensions, explicit uncertainty and omitted-variable tracking, source-grounded warnings, deterministic bounded simulation, scenario comparison, permission-safe projections, Scene attachment, recovery, accessibility, and twenty blocking acceptance criteria. The design prohibits guaranteed-balance, fairness, safety, victory, survival, optimality, and actual-play prediction claims.

## IA-D03-004 — Internal Alpha Content and Deterministic Fixtures

Complete at design level with:

- 36 exact inherited source-backed golden fixtures;
- 119 explicitly synthetic noncanonical fixtures;
- five exact-version fixture packs;
- identity, Campaign, Character, content, Scene, Action, permission, Asset, relationship, investigation, Encounter, failure, pack lifecycle, and accessibility coverage;
- stable IDs, versions, grouped expected contracts, migration, cleanup, and checksum derivation;
- twenty blocking acceptance criteria and zero blocking findings;
- explicit source-selection and complete-game coverage limits;
- deterministic validation and dedicated CI.

The corpus is bounded test data, not the complete game and not a canonical content release. Unselected source material is preserved.

## Primary artifacts

- `INTERNAL_ALPHA_CONTENT_AND_FIXTURES.md`
- `IA-D03-004_INTERNAL_ALPHA_CONTENT_AND_FIXTURE_SPEC.md`
- `INTERNAL_ALPHA_FIXTURE_CATALOG.json`
- `INTERNAL_ALPHA_FIXTURE_COVERAGE_MATRIX.json`
- `IA-D03-004_IMPLEMENTATION_TRACEABILITY.json`
- `IA-D03-004_REVIEW_RECEIPT.md`
- `IA-D03-004_READINESS_RECORD.md`
- `IA-D03-004_COMPLETION_RECORD.json`
- `validate_internal_alpha_content_fixtures.py`

## Execution boundary

Design work may proceed while implementation dependencies remain incomplete. No document here authorizes canonical promotion, paid services, production credentials, real-user data, internal-alpha release, production deployment, or public release.

## Current next design action

**IA-D03-005 — Character/Campaign integration review.**
