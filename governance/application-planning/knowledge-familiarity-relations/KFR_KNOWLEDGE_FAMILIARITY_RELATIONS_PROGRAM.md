# KFR — Knowledge & Familiarity Relations

**Program ID:** KFR  
**Status:** OWNER-APPROVED — COMPLETED THROUGH KFR-05; KFR-06 IN_PROGRESS  
**Activation:** after completed_verified WCI-05  
**Successor:** ODL-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

KFR-01 through KFR-05 are `completed_verified`.

KFR-05 — Operator Qualification & Vehicle/Machine/Equipment Integration — completed on exact validated application head `fdd8ab14bb6d078a3881018e6deccf4f83639e36`, current-family run `33484525780`, and application merge `25b37e11e6473c215c75b569a0dc91f0b7161eb7`. Its implementation authority is retired. Final proof used the governed self-hosted Windows and Linux lanes plus deterministic comparison; the deterministic receipt SHA-256 is `a72fd80e301024ae29b36e03583c42d4a326355a6a267e7e61146629df089943`.

KFR-06 — Profession, Research, Mentorship & Learning Integration — is bounded `in_progress` from exact application main `25b37e11e6473c215c75b569a0dc91f0b7161eb7` on `integration/kfr-06-profession-research-mentorship-learning-integration` after the owner `Continue` governed start.

## Purpose

KFR supplies governed familiarity relations that canonical Character, Skills/Progression, Professions, Research, Vehicle/platform, Equipment/Asset, Organization/relationship, World/WCI and permission systems may consume without replacing their state or authority.

## Tranches

1. **KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary** — completed_verified.
2. **KFR-02 — Hierarchical Familiarity Graph** — completed_verified.
3. **KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records** — completed_verified.
4. **KFR-04 — Transfer, Adjacency, Confidence & Unknown-State Rules** — completed_verified.
5. **KFR-05 — Operator Qualification & Vehicle/Machine/Equipment Integration** — completed_verified.
6. **KFR-06 — Profession, Research, Mentorship & Learning Integration** — in_progress.
7. **KFR-07 — Authoring, Inspection, Search & Provenance UX** — planned.
8. **KFR-08 — Cross-Domain Golden Proof** — planned.

## KFR-05 completion boundary

KFR-05 projects operator qualification only from explicit visible canonical-owner qualification evidence. `qualified`, `unqualified`, `unknown`, and `incompatible` remain explicit categorical states. Missing and explicit-unknown qualification evidence remain `unknown`; incompatible remains incompatible; conflicting qualified/unqualified evidence remains unresolved `unknown` for canonical owner resolution.

KFR-03 familiarity and KFR-04 advisory transfer/confidence remain explanatory context only and cannot grant or upgrade qualification. Existing visible active `VehicleStationGrant` authority is projected separately from qualification; station authority does not prove qualification and KFR-05 creates or mutates no station grant.

## KFR-06 governed-start boundary

KFR-06 implements a visibility-safe, read-only integration projection over explicit canonical-owner evidence for four separately labeled kinds: `profession`, `research`, `mentorship`, and `learning`. Owner evidence states are categorical `confirmed`, `not-confirmed`, `explicit-unknown`, or `incompatible`. Missing or explicit-unknown evidence remains unknown, incompatible remains incompatible, and conflicting confirmed/not-confirmed evidence remains unresolved for canonical-owner resolution.

DPL-02 profession/activity/mastery/credential definitions remain read-only. KFR familiarity, transfer or qualification cannot award profession membership, mastery, credentials or service readiness.

DPL-03 research evidence/result/discovery truth remains canonical. Contradiction is preserved rather than silently resolved. KFR-06 cannot create a discovery, reveal hidden knowledge, publish research or replace the DPL-03 evidence chain.

DPL-09 apprenticeship/mentorship/teaching/workforce definitions remain read-only. KFR-06 cannot enroll a learner, assign a mentor, mutate Social-Relations, execute an APW/D26 training Project or advance campaign time.

Progression-Abilities remains sole advancement authority. KFR-06 cannot award skill points, mastery, credentials, XP, levels, knowledge points or any other learning advancement.

KFR-03 records, KFR-04 advisory transfer/confidence and KFR-05 qualification may be carried only as separately labeled advisory context. They never upgrade canonical owner evidence.

Hidden/private owner evidence, profession/research/mentorship/learning references and KFR context are filtered before counts, projection, search, explanation, deterministic receipts and AI context. Hidden cardinality is not exposed.

KFR-06 introduces no durable persistence or duplicate profession/research/learning ledger; migration `0022` remains unreserved. Final validation requires exactly one KFR-06 Validation Core profile with zero historical predecessor fanout, genuine RED before production, and exact-head self-hosted Linux/Windows plus deterministic comparison.

KFR-07+, ODL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
