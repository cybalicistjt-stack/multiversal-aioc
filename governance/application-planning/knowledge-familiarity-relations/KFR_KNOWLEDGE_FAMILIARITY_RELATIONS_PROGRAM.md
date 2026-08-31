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

KFR-04 — Transfer, Adjacency, Confidence & Unknown-State Rules — is `in_progress` from exact application baseline `d6ffb4ec06bfb6da57cede5fd055a86e4e0076a8` on `integration/kfr-04-transfer-adjacency-confidence-unknown-state-rules`. Application PR #370 remains pre-production at exact head `1153616b86deede9f12043d2c2de9b378c3e562f`: acceptance and the RED profile exist, while KFR-04 production contract/UI surfaces have not been added. The original self-hosted RED selector remained queued, after which the owner authorized a KFR-04-only GitHub-hosted exception. Standard private hosted Ubuntu VM pools (`ubuntu-24.04` and `ubuntu-latest`) failed before step 1; an owner-signaled post-billing/access recheck of `ubuntu-latest` also failed before any step; and the materially different `ubuntu-slim` hosted container pool then failed before step 1 in run `33430984959` / job `99615993679`. The two-cycle no-progress limit is therefore exhausted in diagnostic mode. Product implementation remains paused until concrete private-repository Actions entitlement/budget/payment/access or allocation-service evidence changes, or the owner authorizes a genuinely different execution environment.

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
- Exactly one current KFR-04 Validation Core profile may run, with zero historical predecessor fanout and deterministic Linux/Windows/comparator proof.
- **KFR-04 runner override (owner-authorized 2026-08-31):** because the self-hosted Linux selector for RED run `33421330006` remained queued without executing, GitHub-hosted Linux, GitHub-hosted Windows and a GitHub-hosted comparator are accepted as final KFR-04 proof. This is a bounded KFR-04-only exception and does not change the project-wide default self-hosted final-gate policy for later tranches.
- **Current runner blocker:** private `Multiversal-app` GitHub-hosted jobs fail before workflow execution across standard Ubuntu VM labels and the distinct `ubuntu-slim` hosted-container pool. The owner-signaled recheck after the requested billing/access intervention also failed before any step. No additional runner-label retry is authorized. A subsequent attempt requires concrete changed account/repository Actions entitlement/budget/payment/access evidence, explicit GitHub allocation-service recovery evidence, or an owner-authorized genuinely different execution environment.
- KFR-05+, ODL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
