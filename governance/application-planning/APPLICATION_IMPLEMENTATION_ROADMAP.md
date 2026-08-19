# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 4.8.0  
**Status:** ACTIVE — COMBINED WORKSPACE IMPLEMENTATION  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-19

## Authority and operating rule

Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence. Historical detail remains in Git history and completed checkpoints rather than being recopied into every roadmap revision.

Implementation transitions use one bounded state synchronization after a verified application merge, one AIOC repository-health gate, and one final selector verification. Ordinary implementation operations do not trigger repeated roadmap/pointer rewrites.

## Completed verified foundations

Phase 9 through P9-06-023, DT-001–DT-010, Stage A A0–A12, Internal Alpha tester/GATX T01–T08, PPIA-01–16, CAPP-01–12, CCTI-01–11 plus CCTI-12 T01–T03, VCH-01–06, CRS-01–06 and POST-GATX-SUCCESSOR are **COMPLETED_VERIFIED**.

The APW/APM/CSW design series is **COMPLETED_VERIFIED** through APW-08, APM-06 and CSW-10.

## Combined implementation progress

| Slice | State | Application evidence | Migration |
|---|---|---|---|
| APW-I01 | completed_verified | PR #205 / `2814de3c…` / merge `e1f074bb…` | none |
| CSW-I01 | completed_verified | PR #206 / `2836c170…` / merge `bebf833d…` | `0009_csw_creative_fragment_foundation.json` |
| APM-I01 | completed_verified | PR #207 / `cdf80bd3…` / merge `3941a066…` | `0010_apm_automated_run_foundation.json` |
| APW-I02 | completed_verified | PR #208 / `d5463609…` / merge `c5c4e896…` | none |
| APW-I03 | completed_verified | PR #209 / `9b6da923…` / merge `06c0d4ff…` | none |
| APW-I04 | completed_verified | PR #210 / `67029683…` / merge `a907fec7…` | `0011_apw_campaign_activity_foundation.json` |
| CSW-I02 | completed_verified | PR #211 / `8a067465…` / merge `72eb9a6b…` | `0012_csw_creator_library_memory.json` |
| APM-I02 | **selected_not_started** | `APM-I02-attempt-001` | inspect live head first |

### CSW-I02 completion evidence

Application PR #211 completed from exact validated head `8a0674650e003381083a8adc39c20721c73239d6` with repository-health run `32264579233` PASS and product run `32264579547` PASS after the unchanged Linux retry. Self-hosted Windows, self-hosted Linux and deterministic comparison all passed before squash merge `72eb9a6b23a3f90c58a2db0d5535f3e07cfe97a5`.

CSW-I02 delivered D29 Creator Project/library organization/Story Bible/Project Memory/saved-view metadata; six distinct Story Bible evidence classes; authorization-before-aggregation through D05; evidence-backed backlinks; saved-view reauthorization; revoked/hidden Campaign nonleakage; and a no-AI Creative Library + Story Bible + Project Memory surface. Migration `0012_csw_creator_library_memory.json` contains D29 creator-support metadata only; governed payloads remain with their owning domains.

Validation provenance is preserved in `CSW-I02-attempt-001`: the first profile lacked the standard `migrated_from` field, the second reached a test-only TypeScript cast error, and the final head passed all CSW-I02 tests/typecheck. Linux then encountered only the existing A2 p95 fluctuation (`296.612474ms` vs `250ms`); an unchanged rerun passed. No product assertion, performance threshold or scope was weakened.

## Current work — APM-I02

**APM-I02 — Cozy Solo core loop** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APM-I02-attempt-001`  
State: `selected_not_started`

Initial scope is **Cozy Solo in Personal context**. Cozy describes low-pressure pacing/presentation and bounded automation; it is setting-independent and does not create a separate rules engine or guarantee success.

Core loop:

**Orient → choose a focus → set/confirm bounds → progress routine work → stop at meaningful decisions → reflect/summarize → continue/change focus/pause/return to ordinary play.**

Required boundaries:
- explicit APM-I01 controller/run/delegation authority;
- eligible activities discovered from current Personal/APW/owning-domain profiles rather than invented by Cozy;
- every step revalidates owning-domain operation class and current authorization;
- automatic work is limited to `automatic_permitted` or `automatic_with_bounds` operations inside explicit budgets;
- proposal-required work remains proposal-driven;
- irreversible advancement, materially new direction, new costs outside budget, ownership/custody transfer, destructive deletion, Campaign binding, human consent, publication, ambiguity with material consequence, GM-only adjudication, real-money spending and widened automation bounds remain human-required hard stops;
- Cozy cannot convert GM/adjudication-required work into “AI decides as GM”;
- wall-clock time is not gameplay-progress authority;
- real-money/paid-credit automation budget is always zero;
- no-AI/manual ordinary Personal/Campaign workflows remain complete fallbacks;
- pause/revoke/stale/recovery boundaries must stop new automation and recover through stable operation/status/Event evidence without duplicate effects.

First operation: re-fetch App main and migration head **once**, inspect APM-I01 delegation/run plus Personal/APW-I04 activity seams, determine whether Cozy preference/run metadata genuinely requires another additive migration, then implement the smallest useful no-AI loop.

Canonical App baseline after CSW-I02: `72eb9a6b23a3f90c58a2db0d5535f3e07cfe97a5`. Migration head: `0012_csw_creator_library_memory.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through CSW-I02 is completed_verified. APM-I02 is selected_not_started. Later slices remain inactive.

## Migration and ownership policy

- migrations `0001` through `0012` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- no monolithic APW/CSW/APM state store is authorized;
- owning domains remain authoritative for gameplay state and Events;
- D29 creative support remains metadata/provenance/reference oriented;
- D05 authorization precedes derived aggregation;
- APM delegation never replaces fresh owning-domain authorization.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **APW-I05 remains**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **in progress**.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06.
6. Whole-system hybrid proof — APW-I07.

Tester distribution remains separately owner-gated.

## Preserved/deferred work

- **CCTI-12-T04:** owner-deferred until September 2026; preserve App PR #191 and its branches. On/after 2026-09-01 establish the owner-approved validation route before reevaluation.
- **WP-011:** dormant until the required special Mac environment is available.
- **DS-008:** blocked non-owner exact-byte transfer/validation; never reconstruct checksum-bound bytes from excerpts/OCR/memory.

## Permanent validation rules

Only evidence-backed `completed_verified` is complete. A failed required gate leaves work unfinished. Normal App/package acceptance is self-hosted Windows + self-hosted Linux + deterministic comparison where outputs should agree, plus exact-head repository health. AIOC repository health validates governance state; it does not substitute for product validation.

## Product-wide approved concerns

- **TODO-UX-VOICE:** knowledgeable, creative companion; warm, welcoming, encouraging, clear, confident and restrained; never obsequious.
- **TODO-FSF:** parental controls govern Multiversal-controlled capability/exposure; guardian authority remains distinct from GM/Campaign authority and does not imply access to private creative work.

## Nonauthorization

Current selection authorizes only APM-I02. It does not authorize APM-I03+, Connected Cozy/multiplayer automation, AI-as-GM authority, unbounded background play, automatic irreversible advancement or consent, real-money automated spending, APW-I05+, CSW-I03+, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
