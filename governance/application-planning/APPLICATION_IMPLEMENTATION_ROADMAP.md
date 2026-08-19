# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 4.1.0  
**Status:** ACTIVE — COMBINED WORKSPACE IMPLEMENTATION  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-19

## Authority and purpose

This is the concise current application roadmap. Historical revisions remain in Git history and receipts; they are not current-work selectors. Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence.

## Completed verified foundations

Phase 9 through P9-06-023, DT-001–DT-010, Stage A A0–A12, Internal Alpha tester/GATX T01–T08, PPIA-01–16, CAPP-01–12, CCTI-01–11 plus CCTI-12 T01–T03, VCH-01–06, CRS-01–06 and POST-GATX-SUCCESSOR are **COMPLETED_VERIFIED**.

Current application main at implementation activation is `bf61c64c89e7ea997842ea7442797fba619d0e28`; current migration head is `database/migrations/0008_a10_world_content_authoring.json`. These values must be re-fetched before the first implementation branch is created.

## APW / APM / CSW design series — COMPLETED_VERIFIED

The full owner-approved APW/APM/CSW design sequence is complete through:

- APW-01 through APW-08;
- APM-01 through APM-06;
- CSW-01 through CSW-10.

Final handoff evidence:
- CSW-10: PR #449 / repo-health `32237196497` / merge `d27a6774470261450f41e1591580c7feba174cee`;
- APW-07: PR #451 / repo-health `32237975517` / merge `e9592399eaca07d0cdf28b79320fc6bf59bde5ef`;
- APM-06: PR #453 / repo-health `32244745957` / merge `9396ce2ec6094982d292eb4a630036c641094904`;
- APW-08: PR #455 / exact head `f6263185682ec04c948ef865d8f5f3b674b6e825` / repo-health `32245783537` / merge `608e3ddde4b634a1d545856cfd6cb3b2c273fbc7`.

The design series produced a 21-slice additive implementation program, migration/touch-point inventory, six incremental Internal Alpha milestones, 36 cross-program blocking acceptance cases, feature/fallback/no-AI requirements and explicit Stage A non-reopening rules.

## Current work — APW-I01

**APW-I01 — Contextual account/role projection and Personal-context authority extensions** is the selected first application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APW-I01-attempt-001`  
State: `selected_not_started`

APW-I01 implements the highest-leverage shared foundation:

- one stable user subject rather than permanent Player/GM account castes;
- explicit Personal, Campaign and Session contexts;
- Campaign-scoped role/control/delegation projections;
- additive compatibility with current Stage A A3 contracts;
- safe context switching, cache partitioning and reauthorization;
- useful Personal context for a user with zero Campaign memberships;
- entitlement/resource independence from unrelated Campaign role changes;
- no UI/route/query parameter treated as authority.

The first implementation operation is to re-fetch App main and migration head, inspect the exact APW-I01 touchpoints and current validator/regression surface, then create a bounded application branch from the verified current main.

## Combined implementation handles

### APW
APW-I01 through APW-I07.

### CSW
CSW-I01 through CSW-I08, with D29 `authoring-provenance` as the initial creative-support persistence owner and explicit receipt-bound governed incorporation.

### APM
APM-I01 through APM-I06, with bounded automation over ordinary owning-domain/Event authority and complete no-AI recovery paths.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Each item becomes active only through its own canonical selector transition. Completing APW-I01 does not automatically activate later slices.

## Migration and ownership policy

- migrations `0001` through `0008` are immutable predecessors;
- `0009` is merely the current next slot while App main remains unchanged, not a permanent reservation;
- each implementation tranche rechecks current migration head before mutation;
- no migration is required when a slice has no schema delta;
- no monolithic APW/CSW/APM state store is authorized;
- APW orchestration, CSW creator support and APM run bookkeeping remain additive to established owning domains;
- authorization/visibility filtering precedes count/search/topology/notification/export/diagnostic/AI aggregation.

## Internal Alpha implementation milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06.
6. Whole-system hybrid proof — APW-I07.

Tester distribution remains separately owner-gated.

## Deferred work — CCTI-12-T04

CCTI-12-T04 remains unfinished and owner-deferred until September 2026 under `governance/ai/runtime/OWNER_DECISION_2026-08-18_DEFER_CCTI12_T04_TO_SEPTEMBER.md`.

Preserve App PR #191 and the clean reconstruction branch as provenance only. Neither gains merge authority by existence. On/after 2026-09-01, first establish the owner-approved GitHub-hosted validation route or explicit bounded policy exception before re-evaluating the tranche against then-current App main.

## Other preserved unfinished work

- **WP-011:** special Mac-environment work; may temporarily preempt the normal implementation order when the required borrowed Mac is available.
- **DS-008:** blocked non-owner exact-byte transfer/validation; checksum-bound content must never be reconstructed from excerpts/OCR/memory.

## Permanent completion and validation rules

- Only evidence-backed `completed_verified` is complete.
- Artifact existence or partial tests never establish completion.
- A failed required validation leaves the slice unfinished.
- Normal application/package final acceptance uses owner-controlled self-hosted Windows + Linux plus deterministic comparison where outputs should agree, unless a bounded owner-approved exception explicitly applies.
- Exact-head AIOC repository health is governance evidence, not a substitute for product/platform gates.
- One stable operation ID represents one authoritative intent across retries; accepted effects are at-most-once.
- Successor work does not reopen completed Stage A evidence unless fresh independent evidence proves a predecessor regression.

## Product-wide approved concerns

- **TODO-UX-VOICE:** knowledgeable, creative companion; warm, welcoming, encouraging, clear, confident and restrained; never obsequious.
- **TODO-FSF:** parental controls govern Multiversal-controlled capability/exposure; guardian authority remains distinct from GM/Campaign authority and does not imply access to private creative work.

## Nonauthorization

Current selection authorizes only the bounded APW-I01 application implementation tranche. It does not authorize APW-I02 or later slices, T04 before September, tester distribution, public release/deployment, paid-provider activation, canonical publication, or broad Stage A redesign.

## Mandatory execution behavior

“Continue” means execute the next verified unfinished operation. Preserve provenance, hidden-information boundaries, permissions, reversibility and owner gates.
