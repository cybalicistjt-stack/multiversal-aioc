# MV-IA-001 — Internal Alpha Feature Design Program

**Document ID:** MV-IA-001  
**Version:** 0.18.0  
**Status:** ACTIVE — DESIGN PROGRAM  
**Owner and final authority:** John Brandon Turner

## Purpose

MV-IA-001 converts the approved Project Bible, Stage A program, Phase 9 architecture, source game framework, and historical feature roadmap into implementation-ready internal-alpha design contracts. It does not bypass P9-06 or authorize release.

## Completed foundations

IA-D01 and IA-D02 are complete. Shared contracts cover governed objects, identity, authority, projections, persistence, recovery, diagnostics, accessibility, provider neutrality, and zero-service operation.

## Completed Character and Campaign preparation

IA-D03-001 through IA-D03-005 are complete, including Character, Campaign/Scene/Session, Encounter preparation, bounded deterministic fixtures, and the Character/Campaign integration review.

## Completed first playable loop

IA-D04-001 through IA-D04-005 are complete. The tranche defines Player and GM Action proposals, approve/deny/modify adjudication, atomic durable results, NPC/enemy parity, shared proposal/approval components, two-device recovery, authoritative role-safe result/history presentation, and a twelve-package implementation handoff.

## IA-D05-001 — Relationship Tracker

Completed at design level with:

- first-class directional relationship edges and explicit mutual pairing;
- fourteen registry-capable relationship dimensions;
- profile-defined scales, bands, and thresholds instead of a universal attitude score;
- append-only Event-backed history and exact source/version provenance;
- seven independently authorized reveal layers;
- server-filtered GM and Player graph/list projections;
- required mobile list/tree and accessible nonvisual parity;
- separate relationship, reputation/standing, public status, mood, intent, and stance aggregates;
- social Bonds with profile thresholds and human agreement gates;
- structured leverage, favors, promises, debts, oaths, and obligations;
- twenty-four deterministic fixtures, eight implementation slices, twenty-eight blocking criteria, five resolved findings, and zero blocking findings.

Primary artifacts:

- `feature-packets/MV-IA-F009_RELATIONSHIP_TRACKER.md`
- `feature-packets/MV-IA-F009_RELATIONSHIP_TRACKER_MATRIX.json`
- `feature-packets/MV-IA-F009_SOURCE_COVERAGE_AND_PROVENANCE.json`
- `feature-packets/MV-IA-F009_IMPLEMENTATION_TRACEABILITY.json`
- `feature-packets/MV-IA-F009_REVIEW_RECEIPT.md`
- `feature-packets/MV-IA-F009_READINESS_RECORD.md`
- `feature-packets/MV-IA-F009_COMPLETION_RECORD.json`
- `validate_relationship_tracker.py`

## Governing decisions

Relationships are directional unless explicitly paired. There is no universal attitude score. Missing source relationship data remains missing. Graph/list/cache/notification/realtime/AI views are nonauthoritative and role-filtered. Romantic, intimate, or emotionally controlling Bonds cannot be created automatically by a roll. Silence is not approval.

## Execution boundary

Design work may proceed while implementation dependencies remain incomplete. `P9-06-008-attempt-002` remains unfinished parallel application work. No document here authorizes canonical promotion, paid services, production credentials, real-user data, internal-alpha release, production deployment, or public release.

## Efficiency boundary

MV-AI-EFFICIENCY-002 governs: no intra-step validation, marker files, checkpoint maintenance, status projection, or administrative commits. Build the whole bounded step, then validate and update once at its boundary.

## Current next design action

**IA-D05-002 — MV-IA-F016 Factions, Reputation, and Organizations.**

## Historical route anchors

IA-D03 completed Character/Campaign preparation. IA-D04 completed the first playable loop. IA-D05 begins the relationship, faction, social-interaction, and investigation tranche.
