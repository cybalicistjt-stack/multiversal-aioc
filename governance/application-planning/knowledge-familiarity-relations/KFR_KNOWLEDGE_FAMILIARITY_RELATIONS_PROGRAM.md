# KFR — Knowledge & Familiarity Relations

**Program ID:** KFR  
**Status:** OWNER-APPROVED — COMPLETED THROUGH KFR-02; KFR-03 IN_PROGRESS  
**Activation:** after completed_verified WCI-05  
**Successor:** ODL-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary — remains `completed_verified`.

KFR-02 — Hierarchical Familiarity Graph — remains `completed_verified` on application merge `c324ae8b82faf8815a35013e3a245a0c4ba6b29b`. Its implementation authority is retired.

KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records — is bounded `in_progress` from exact application baseline `c324ae8b82faf8815a35013e3a245a0c4ba6b29b` on `integration/kfr-03-character-knowledge-experience-explicit-familiarity-records`, effective only after its exact governed-start AIOC candidate passes Repository Health and merges.

## Purpose

KFR supplies governed familiarity relations that canonical Character, Skills/Progression, Professions, Research, Vehicle/platform, Equipment/Asset, Organization/relationship, World/WCI and permission systems may consume without replacing their state or authority.

## Tranches

1. **KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary** — completed_verified.
2. **KFR-02 — Hierarchical Familiarity Graph** — completed_verified.
3. **KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records** — in_progress.
4. **KFR-04 — Transfer, Adjacency, Confidence & Unknown-State Rules** — planned.
5. **KFR-05 — Operator Qualification & Vehicle/Machine/Equipment Integration** — planned.
6. **KFR-06 — Profession, Research, Mentorship & Learning Integration** — planned.
7. **KFR-07 — Authoring, Inspection, Search & Provenance UX** — planned.
8. **KFR-08 — Cross-Domain Golden Proof** — planned.

## KFR-02 completion boundary

KFR-02 delivered visibility-safe `parent`, `child` and `adjacent` familiarity topology over stable KFR-01/canonical owner references. Domain-specific graph shapes and cycles are allowed as topology; deterministic projection terminates safely. Explicit unknown remains unknown. Hidden/private nodes and incident edges are filtered before projection and aggregates. Graph position does not imply familiarity, permission, proficiency, certification, transfer percentage, qualification or automatic competence. Canonical owner taxonomies remain authoritative. No durable KFR-02 persistence or migration `0022` was introduced.

## KFR-03 governed-start boundary

- KFR-03 may define explicit `knowledge`, `experience`, `familiarity` and `explicit-unknown` record inputs/projections over stable Character, KFR subject and canonical owner references.
- Each record requires stable record identity, Character reference, KFR subject reference, canonical owner reference/version, record version, provenance and visibility references.
- Explicit unknown is an explicit record state; absence of a record remains absence. Neither may be inferred from the other.
- KFR-02 topology, ancestry or adjacency cannot create a KFR-03 record or invent knowledge/familiarity.
- Knowledge, experience and familiarity evidence remain distinct from proficiency, certification, permission, ownership, progression state and action authority.
- Hidden/private records are filtered before projection, counts, search, explanation, deterministic receipts and AI context; hidden cardinality is not exposed.
- Canonical Character, Progression/Skill, domain-owner and Permission/visibility systems remain authoritative; KFR-03 performs no canonical owner mutation.
- **Persistence decision:** no durable KFR-03 persistence and no duplicate Character knowledge ledger. Migration `0022` remains unreserved.
- Transfer/confidence propagation remains KFR-04 scope; operator qualification remains KFR-05 scope.
- Accessible nonvisual record/state/provenance/authority equivalents and deterministic stable ordering are required.
- Exactly one current KFR-03 Validation Core profile may run; historical predecessor fanout remains zero.
- KFR-04+, ODL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
