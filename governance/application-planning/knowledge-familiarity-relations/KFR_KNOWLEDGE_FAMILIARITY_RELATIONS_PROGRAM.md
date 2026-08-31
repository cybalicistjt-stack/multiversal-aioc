# KFR — Knowledge & Familiarity Relations

**Program ID:** KFR  
**Status:** OWNER-APPROVED — COMPLETED THROUGH KFR-03; KFR-04 IN_PROGRESS  
**Activation:** after completed_verified WCI-05  
**Successor:** ODL-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary — remains `completed_verified`.

KFR-02 — Hierarchical Familiarity Graph — remains `completed_verified`.

KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records — remains `completed_verified` on exact validated head `80d5dc21260de2d03d41712b29c0b3eca18e0ec0`, current-family run `33419444476`, and application merge `d6ffb4ec06bfb6da57cede5fd055a86e4e0076a8`. Its implementation authority is retired.

KFR-04 — Transfer, Adjacency, Confidence & Unknown-State Rules — is `in_progress` from exact application baseline `d6ffb4ec06bfb6da57cede5fd055a86e4e0076a8` on `integration/kfr-04-transfer-adjacency-confidence-unknown-state-rules`, effective only after its exact governed-start AIOC candidate passes Repository Health and merges.

## Purpose

KFR supplies governed familiarity relations that canonical Character, Skills/Progression, Professions, Research, Vehicle/platform, Equipment/Asset, Organization/relationship, World/WCI and permission systems may consume without replacing their state or authority.

## Tranches

1. **KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary** — completed_verified.
2. **KFR-02 — Hierarchical Familiarity Graph** — completed_verified.
3. **KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records** — completed_verified.
4. **KFR-04 — Transfer, Adjacency, Confidence & Unknown-State Rules** — in_progress.
5. **KFR-05 — Operator Qualification & Vehicle/Machine/Equipment Integration** — planned.
6. **KFR-06 — Profession, Research, Mentorship & Learning Integration** — planned.
7. **KFR-07 — Authoring, Inspection, Search & Provenance UX** — planned.
8. **KFR-08 — Cross-Domain Golden Proof** — planned.

## KFR-03 completion boundary

KFR-03 delivered visibility-safe explicit `knowledge`, `experience`, `familiarity`, and `explicit-unknown` record projection over stable Character, KFR subject and canonical owner/version/provenance references. Explicit unknown remains distinct from no record. KFR-02 topology cannot create records. Hidden/private records are filtered before aggregates/search/explanation/receipts/AI context. Evidence does not imply proficiency, certification, permission, ownership or action authority. Canonical Character, Progression/Skill, owner-domain and Permission/visibility systems remain authoritative.

KFR-03 introduced no durable KFR persistence, duplicate Character knowledge ledger or migration `0022`.

## KFR-04 governed-start contract

- KFR-04 may project **advisory transfer eligibility** only from an explicit visible KFR-04 rule plus a visible explicit KFR-03 source record and a visible referenced KFR-02 graph relation.
- Adjacency alone is never transfer eligibility and never creates familiarity, proficiency, competence or qualification.
- Eligibility states are `eligible`, `ineligible`, and `unknown`. `eligible` is advisory only; it writes no target knowledge/familiarity record and grants no action authority.
- Confidence states are explicit categorical `high`, `medium`, `low`, `unknown`, and `incompatible`. Confidence is not a computed proficiency percentage. `incompatible` cannot resolve to eligible.
- Explicit-unknown source records remain explicit unknown. Missing source records remain absent. Neither state may be silently rewritten or converted into familiarity.
- Hidden/private rules, source records and relation inputs are filtered before projection, counts, search, explanation, deterministic receipts or AI context; hidden cardinality is not exposed.
- Canonical Character, Progression/Skill, domain-owner and Permission/visibility authority remains unchanged.
- Operator qualification remains KFR-05 scope.
- No durable KFR-04 persistence or duplicate transfer ledger is introduced. Migration `0022` remains unreserved.
- Exactly one current KFR-04 Validation Core profile may run, with zero historical predecessor fanout and final self-hosted Linux/Windows/comparator proof.
- KFR-05+, ODL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
