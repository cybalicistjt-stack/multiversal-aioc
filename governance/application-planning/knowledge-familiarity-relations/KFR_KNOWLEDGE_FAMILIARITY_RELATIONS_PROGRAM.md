# KFR — Knowledge & Familiarity Relations

**Program ID:** KFR  
**Status:** OWNER-APPROVED — COMPLETED THROUGH KFR-01; KFR-02 IN_PROGRESS  
**Activation:** after completed_verified WCI-05  
**Successor:** ODL-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary — is `completed_verified` on application merge `d24c9b16a4decf60c178a06d6422bfc267e730e2`.

KFR-02 — Hierarchical Familiarity Graph — is `in_progress` from that exact application main on registered branch `integration/kfr-02-hierarchical-familiarity-graph`. Product mutation becomes effective only after the exact governed-start AIOC candidate passes Repository Health and merges.

## Purpose

KFR supplies governed familiarity relations that canonical Character, Skills/Progression, Professions, Research, Vehicle/platform, Equipment/Asset, Organization/relationship, World/WCI and permission systems may consume without replacing their state or authority.

## Tranches

1. **KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary** — completed_verified.
2. **KFR-02 — Hierarchical Familiarity Graph** — in_progress. Define reusable parent/child/adjacent familiarity topology across domains without forcing one universal rigid tree or implying familiarity/competence from topology alone.
3. **KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records** — planned.
4. **KFR-04 — Transfer, Adjacency, Confidence & Unknown-State Rules** — planned.
5. **KFR-05 — Operator Qualification & Vehicle/Machine/Equipment Integration** — planned.
6. **KFR-06 — Profession, Research, Mentorship & Learning Integration** — planned.
7. **KFR-07 — Authoring, Inspection, Search & Provenance UX** — planned.
8. **KFR-08 — Cross-Domain Golden Proof** — planned.

## KFR-01 completion boundary

KFR-01 delivered a visibility-safe, deterministic source/authority crosswalk and vocabulary for `family`, `class`, `type`, `brand-manufacturer`, `model`, `unit`, `specialization`, `adjacency` and `explicit-unknown`. Canonical owner taxonomies remain authoritative; explicit unknown remains unknown; familiarity does not imply permission, ownership, proficiency, certification or action authority. No familiarity record, hierarchy, transfer/confidence rule, automatic competence, durable persistence or migration `0022` was introduced.

## KFR-02 governed-start boundary

- Graph nodes are stable KFR-01 familiarity subject references plus canonical owner references/versions; owner taxonomies remain canonical.
- Allowed edge kinds are `parent`, `child` and `adjacent`.
- Domain-specific graph shapes are valid. KFR-02 does not force all domains into one universal rigid tree.
- Cycles may exist as topology; deterministic projection must terminate safely and cannot interpret cycles as inherited authority or competence.
- Parent/child/adjacent topology does not itself assert Character familiarity, permission, ownership, proficiency, certification, action authority, qualification or automatic competence.
- Explicit unknown remains unknown. Missing familiarity cannot be invented from graph position.
- Transfer percentages, confidence degradation, incompatibility weighting and competence inheritance remain KFR-04/KFR-05 scope and are unauthorized here.
- Unauthorized nodes and incident edges must be filtered before projection, counts, search, explanation, deterministic receipts and AI context; hidden cardinality must not leak.
- Graph topology, node labels, edge kinds, explicit-unknown state and authority explanations require accessible nonvisual equivalents; visual layout is not semantic truth.
- KFR-02 introduces no durable persistence. The graph is a deterministic code/governance projection over stable canonical references; migration `0022` remains unreserved.
- Final validation uses exactly one KFR-02 Validation Core profile with zero predecessor fanout, genuine RED before production, self-hosted Linux/Windows and deterministic comparison on one exact head.
- KFR-03+, ODL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
