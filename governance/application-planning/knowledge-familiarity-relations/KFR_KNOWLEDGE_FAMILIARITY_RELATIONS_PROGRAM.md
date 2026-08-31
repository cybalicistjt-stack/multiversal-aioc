# KFR — Knowledge & Familiarity Relations

**Program ID:** KFR  
**Status:** OWNER-APPROVED — COMPLETED THROUGH KFR-02; KFR-03 SELECTED_NOT_STARTED  
**Activation:** after completed_verified WCI-05  
**Successor:** ODL-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary — remains `completed_verified`.

KFR-02 — Hierarchical Familiarity Graph — is `completed_verified` on exact validated head `e4630e179d75df5a1b9b975b0c7925ecaa402099`, current-family run `33413222385`, and application merge `c324ae8b82faf8815a35013e3a245a0c4ba6b29b`. Its implementation authority is retired.

KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records — is `selected_not_started` from exact application main `c324ae8b82faf8815a35013e3a245a0c4ba6b29b`. It has no implementation branch or implementation authority. A future owner Continue and green governed-start merge are required before application mutation.

## Purpose

KFR supplies governed familiarity relations that canonical Character, Skills/Progression, Professions, Research, Vehicle/platform, Equipment/Asset, Organization/relationship, World/WCI and permission systems may consume without replacing their state or authority.

## Tranches

1. **KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary** — completed_verified.
2. **KFR-02 — Hierarchical Familiarity Graph** — completed_verified.
3. **KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records** — selected_not_started.
4. **KFR-04 — Transfer, Adjacency, Confidence & Unknown-State Rules** — planned.
5. **KFR-05 — Operator Qualification & Vehicle/Machine/Equipment Integration** — planned.
6. **KFR-06 — Profession, Research, Mentorship & Learning Integration** — planned.
7. **KFR-07 — Authoring, Inspection, Search & Provenance UX** — planned.
8. **KFR-08 — Cross-Domain Golden Proof** — planned.

## KFR-02 completion boundary

KFR-02 delivered visibility-safe `parent`, `child` and `adjacent` familiarity topology over stable KFR-01/canonical owner references. Domain-specific graph shapes and cycles are allowed as topology; deterministic projection terminates safely. Explicit unknown remains unknown. Hidden/private nodes and incident edges are filtered before projection and aggregates. Graph position does not imply familiarity, permission, proficiency, certification, transfer percentage, qualification or automatic competence. Canonical owner taxonomies remain authoritative. No durable KFR-02 persistence or migration `0022` was introduced.

KFR-02 passed exactly one current KFR-02 Validation Core profile on self-hosted Linux and Windows plus deterministic comparison with zero historical predecessor fanout and no repair cycle.

## KFR-03 selection boundary

- KFR-03 may define explicit Character knowledge, experience evidence and familiarity records only after its own governed start.
- Canonical Character identity/state, Progression/Skill authority, domain-owner state and Permission/visibility remain authoritative.
- Explicit unknown and absent record are distinct; neither graph topology nor adjacency may invent knowledge or familiarity.
- Familiarity records must remain distinct from proficiency, certification, permission, ownership and action authority.
- Provenance, owner references, versioning, visibility and any durable persistence requirement must be resolved before implementation.
- Migration `0022` is not reserved at selection. Whether persistence/migration is necessary is a governed-start decision.
- Transfer/confidence propagation remains KFR-04 scope; operator qualification remains KFR-05 scope.
- Hidden/private records must be filtered before projection, counts, search, explanation, deterministic receipts or AI context.
- KFR-04+, ODL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
