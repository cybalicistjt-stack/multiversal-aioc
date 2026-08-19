# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 4.3.0  
**Status:** ACTIVE — COMBINED WORKSPACE IMPLEMENTATION  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-19

## Authority and purpose

This is the concise current application roadmap. Historical revisions remain in Git history and receipts; they are not current-work selectors. Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence.

## Completed verified foundations

Phase 9 through P9-06-023, DT-001–DT-010, Stage A A0–A12, Internal Alpha tester/GATX T01–T08, PPIA-01–16, CAPP-01–12, CCTI-01–11 plus CCTI-12 T01–T03, VCH-01–06, CRS-01–06 and POST-GATX-SUCCESSOR are **COMPLETED_VERIFIED**.

The APW/APM/CSW design series is **COMPLETED_VERIFIED** through APW-08, APM-06 and CSW-10.

## Combined implementation progress

### APW-I01 — COMPLETED_VERIFIED

**APW-I01 — Contextual account/role projection and Personal-context authority extensions** is complete.

Evidence:
- Application PR #205;
- exact validated head `2814de3c08e62f8fc6b857f5f43800f3106615dd`;
- application repository-health run `32248201457`: PASS;
- product validation run `32248201728`: self-hosted Linux PASS, self-hosted Windows PASS, deterministic cross-platform comparison PASS;
- squash merge `e1f074bb44b89ade0ab27da205043e2681d2a1be`.

Delivered foundation:
- one stable subject across Personal, Campaign and Session contexts without permanent Player/GM account caste;
- contextual roles remain scoped descriptors rather than global account identity;
- authorized zero-Campaign Personal context;
- protected context partitioning and fresh authorization on authority transitions;
- Owner/Admin separation from Campaign authority;
- cadence independence and sanitized client context projection;
- unchanged Stage A selected-context receipt v0.1 and migrations `0001` through `0008`.

### CSW-I01 — COMPLETED_VERIFIED

**CSW-I01 — Creative identity lifecycle provenance foundation** is complete.

Evidence:
- Application PR #206;
- exact validated head `2836c17042bb11d52755d2589814e6b1e542867c`;
- application repository-health run `32250405319`: PASS;
- product validation run `32250405607`: self-hosted Linux PASS, self-hosted Windows PASS, deterministic cross-platform comparison PASS;
- squash merge `bebf833d59923fbfc78ba593219c727a635fc7b7`;
- resulting migration head `database/migrations/0009_csw_creative_fragment_foundation.json`.

Delivered foundation:
- stable D29 `CreativeFragment` identity and monotonic versioning;
- fixed `pre-authoritative` creator-support authority class;
- creator ownership/authorship plus Personal/Campaign context binding;
- deterministic lifecycle states: inbox, scratch, developing, ready, incorporated, superseded, archived and tombstoned;
- durable source/provenance and semantic relationship references;
- exact-version incorporation receipts that bridge to owning-domain operations without moving governed payload authority into CSW;
- reload/recovery, stale-version rejection, tombstone retention and idempotent operation bookkeeping;
- additive provider-neutral migration `0009` with all new records owned by D29 authoring-provenance;
- full client regression/typecheck evidence on both owner-controlled platforms.

Failed intermediate validation attempts remain preserved in the CSW-I01 checkpoint. The final Linux lane initially encountered one unrelated A2 performance timing fluctuation while all CSW-I01 cases and Windows passed; an unchanged retry passed the full suite. No A2 budget or validation scope was weakened.

## Current work — APM-I01

**APM-I01 — Automated-run authority and lifecycle foundation** is the selected next application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APM-I01-attempt-001`  
State: `selected_not_started`

APM-I01 implements the first automated-play application foundation from APM-01/APM-06 and the shared APW authority/recovery architecture:

- stable `automationControllerId` and bounded `automationRunId` identity;
- explicit versioned `AutomationDelegationGrant` scoped to one current Personal, Campaign or Session context;
- controller as a nonhuman service actor, never Player, GM, Campaign Owner, Owner/Admin or other human role;
- owning-domain operation classification: `automatic_permitted`, `automatic_with_bounds`, `proposal_required`, `human_required`, or `prohibited`;
- execution-time reauthorization so delegation is necessary but never sufficient authority;
- deterministic run lifecycle and pause/resume/stop/revoke/expiry barriers;
- operation IDs, expected versions, status lookup and Event-sequence evidence for safe retry/recovery;
- ordinary owning-domain Events remain authoritative game/workspace state rather than an automation ledger;
- feature-flag/no-AI/manual fallback so disabling automation leaves ordinary play available.

The first APM-I01 operation is to re-fetch current App main and migration head, inspect identity/context, permission/delegation, Action/Event, operation-status/idempotency, recovery and feature-flag seams, then create a bounded application branch from verified current main.

Current canonical application main is `bebf833d59923fbfc78ba593219c727a635fc7b7`; current observed migration head is `database/migrations/0009_csw_creative_fragment_foundation.json`. APM-I01 must independently re-fetch both before deciding whether another migration is required.

## Design handoff evidence

Final design handoff evidence remains:
- CSW-10: PR #449 / repo-health `32237196497` / merge `d27a6774470261450f41e1591580c7feba174cee`;
- APW-07: PR #451 / repo-health `32237975517` / merge `e9592399eaca07d0cdf28b79320fc6bf59bde5ef`;
- APM-06: PR #453 / repo-health `32244745957` / merge `9396ce2ec6094982d292eb4a630036c641094904`;
- APW-08: PR #455 / exact head `f6263185682ec04c948ef865d8f5f3b674b6e825` / repo-health `32245783537` / merge `608e3ddde4b634a1d545856cfd6cb3b2c273fbc7`.

The design series produced a 21-slice additive implementation program, migration/touch-point inventory, six incremental Internal Alpha milestones, 36 cross-program blocking acceptance cases, feature/fallback/no-AI requirements and explicit Stage A non-reopening rules.

## Combined implementation handles

### APW
APW-I01 through APW-I07.

### CSW
CSW-I01 through CSW-I08, with D29 `authoring-provenance` as the initial creative-support persistence owner and explicit receipt-bound governed incorporation.

### APM
APM-I01 through APM-I06, with bounded automation over ordinary owning-domain/Event authority and complete no-AI recovery paths.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

`APW-I01` and `CSW-I01` are completed_verified. `APM-I01` is selected_not_started. Every later item remains inactive until its own canonical selector transition.

## Migration and ownership policy

- migrations `0001` through `0009` are immutable predecessors once merged;
- each implementation tranche rechecks current migration head before mutation;
- no migration is required when a slice has no schema delta;
- no monolithic APW/CSW/APM state store is authorized;
- D29 `authoring-provenance` owns CSW creative-support durable records and provenance, while governed World/Adventure/Character/Campaign/A9/Asset payloads remain references to their owning domains;
- APM run/delegation bookkeeping must use an established owning seam selected from live architecture and must not become a parallel game-state ledger;
- ordinary accepted owning-domain Events remain authoritative state;
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

Current selection authorizes only the bounded APM-I01 application implementation tranche. It does not authorize APM-I02 or later slices, APW-I02, CSW-I02, Cozy/AutoGM scenario execution beyond the authority/lifecycle foundation, global GM/controller authority, unbounded background autonomy, T04 before September, tester distribution, public release/deployment, paid-provider activation, canonical publication or broad Stage A redesign.

## Mandatory execution behavior

“Continue” means execute the next verified unfinished operation. Preserve provenance, hidden-information boundaries, permissions, reversibility and owner gates.
