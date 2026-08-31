# KFR — Knowledge & Familiarity Relations

**Program ID:** KFR  
**Status:** OWNER-APPROVED — COMPLETED THROUGH KFR-01; KFR-02 SELECTED_NOT_STARTED  
**Activation:** after completed_verified WCI-05  
**Successor:** ODL-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary — is `completed_verified` on application merge `d24c9b16a4decf60c178a06d6422bfc267e730e2`.

KFR-02 — Hierarchical Familiarity Graph — is `selected_not_started` from that exact application main. It has no implementation branch or implementation authority. A future owner Continue and green governed-start merge are required before application mutation.

## Purpose

KFR supplies governed familiarity relations that canonical Character, Skills/Progression, Professions, Research, Vehicle/platform, Equipment/Asset, Organization/relationship, World/WCI and permission systems may consume without replacing their state or authority.

## Tranches

1. **KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary** — completed_verified.
2. **KFR-02 — Hierarchical Familiarity Graph** — selected_not_started. Define reusable parent/child/adjacent familiarity relationships across domains without forcing one universal rigid tree or implying familiarity/competence from topology alone.
3. **KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records** — planned.
4. **KFR-04 — Transfer, Adjacency, Confidence & Unknown-State Rules** — planned.
5. **KFR-05 — Operator Qualification & Vehicle/Machine/Equipment Integration** — planned.
6. **KFR-06 — Profession, Research, Mentorship & Learning Integration** — planned.
7. **KFR-07 — Authoring, Inspection, Search & Provenance UX** — planned.
8. **KFR-08 — Cross-Domain Golden Proof** — planned.

## KFR-01 completion boundary

KFR-01 delivered a visibility-safe, deterministic source/authority crosswalk and vocabulary for `family`, `class`, `type`, `brand-manufacturer`, `model`, `unit`, `specialization`, `adjacency` and `explicit-unknown`. Canonical owner taxonomies remain authoritative; explicit unknown remains unknown; familiarity does not imply permission, ownership, proficiency, certification or action authority. No familiarity record, hierarchy, transfer/confidence rule, automatic competence, durable persistence or migration `0022` was introduced.

KFR-01 passed exactly one current KFR-01 Validation Core profile on self-hosted Linux and Windows plus deterministic comparison with zero historical predecessor fanout.

## KFR-02 selection boundary

- KFR-02 may define graph relationships over stable KFR-01 vocabulary and canonical owner references only after its own governed start.
- Parent/child/adjacent edges do not themselves assert Character familiarity or competence.
- Canonical domain taxonomies must not be replaced or mutated by the KFR graph.
- Domain-specific graph shapes are allowed; one rigid universal tree is not required.
- Explicit unknown remains unknown.
- Transfer percentage, confidence degradation and incompatibility rules remain KFR-04 scope.
- Hidden/private nodes and edges must be filtered before projection, counts, search, explanation and AI context.
- Persistence/migration needs remain unresolved until governed start; migration `0022` is not reserved at selection.
- KFR-03+, ODL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
