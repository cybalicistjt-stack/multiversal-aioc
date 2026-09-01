# KFR — Knowledge & Familiarity Relations

**Program ID:** KFR  
**Status:** OWNER-APPROVED — COMPLETED THROUGH KFR-07; KFR-08 IN_PROGRESS  
**Activation:** after completed_verified WCI-05  
**Successor:** ODL-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

KFR-01 through KFR-07 are `completed_verified`.

KFR-07 — Authoring, Inspection, Search & Provenance UX — completed on exact validated application head `ba200bda8de5b7298c205d852213a621b5ef0b77`, current-family run `33495773941`, and application merge `9e4754a52026723c77af5830b92a453a867b4025`. Its implementation authority is retired. Final proof used the governed self-hosted Windows and Linux lanes plus deterministic comparison; the deterministic receipt SHA-256 is `77351208992d931f1380745ec50c3a49c618a710478aefc6dcfddf7c5f64c9b5`.

KFR-08 — Cross-Domain Golden Proof — is `in_progress` on `integration/kfr-08-cross-domain-golden-proof` from exact application main `9e4754a52026723c77af5830b92a453a867b4025`.

## Purpose

KFR supplies governed familiarity relations that canonical Character, Skills/Progression, Professions, Research, Vehicle/platform, Equipment/Asset, Organization/relationship, World/WCI and permission systems may consume without replacing their state or authority.

## Tranches

1. **KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary** — completed_verified.
2. **KFR-02 — Hierarchical Familiarity Graph** — completed_verified.
3. **KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records** — completed_verified.
4. **KFR-04 — Transfer, Adjacency, Confidence & Unknown-State Rules** — completed_verified.
5. **KFR-05 — Operator Qualification & Vehicle/Machine/Equipment Integration** — completed_verified.
6. **KFR-06 — Profession, Research, Mentorship & Learning Integration** — completed_verified.
7. **KFR-07 — Authoring, Inspection, Search & Provenance UX** — completed_verified.
8. **KFR-08 — Cross-Domain Golden Proof** — in_progress.

## KFR-07 completion boundary

KFR-07 delivers a visibility-safe read-only UX projection across separately labeled KFR-01 through KFR-06 inputs. Hidden/private KFR and owner-domain inputs are filtered before topology, cardinality, search, autocomplete, counts, previews, inspection, exports, diagnostics, notifications, receipts or optional-AI context. Hidden cardinality is never exposed.

Search, count, preview/inspection and AI-context derived outputs require explicit visibility-projection authorization. Inspection remains read-only. Provenance UX displays only explicit existing provenance references attached to visible inputs; missing provenance remains absent/unknown and is never fabricated or inferred. Authoring remains intent/proposal UX only and existing AuthoringAuthority dimensions remain independent.

## KFR-08 governed-start boundary

KFR-08 is a composition/proof tranche only. It may add a thin cross-domain proof composer and accessible nonvisual proof panel that call completed KFR-01 through KFR-07 projection/receipt functions; it may not redefine their semantics.

The bounded golden fixture crosses Character familiarity, MIB-14 vehicle/machine references, DPL profession, DPL-03 research, mentorship/learning owner evidence, advisory transfer/qualification context and KFR-07 search/inspection/provenance UX. Deliberately hidden counterpart inputs must be filtered by the completed owner projections before any KFR-08 aggregate, count, provenance chain, receipt or AI context. Hidden cardinality remains undisclosed.

The proof must preserve explicit unknown/conflict semantics: explicit-unknown familiarity cannot become competence through adjacency; conflicting KFR-05 qualified/unqualified canonical evidence remains unknown pending the qualification owner; conflicting KFR-06 research evidence remains unknown pending the research owner; explicit-unknown mentorship remains unknown. KFR-07 authoring uses a deliberately non-matching authority dimension so no authority inheritance or write occurs.

Provenance may be aggregated only from explicit provenance references already emitted by completed KFR projections. Missing provenance remains missing and KFR-08 may not fabricate provenance. Stable visible summaries and completed deterministic receipts form one stable KFR-08 receipt independent of fixture input ordering.

Canonical KFR/source-domain owners, AuthoringAuthority and Permission/visibility remain authoritative. KFR-08 grants no permission/action authority, ownership/custody, proficiency/certification, profession advancement, research truth resolution, mentorship enrollment, authoring mutation or canonical write. No durable KFR-08 persistence is authorized and migration `0022` remains unreserved.

Exactly one current KFR-08 Validation Core profile is authorized. Genuine RED must precede the thin proof composer/panel; final proof requires exact-head self-hosted Linux and Windows plus deterministic comparison with zero historical predecessor profile fanout.

ODL-01+, provider activation, tester distribution, release and deployment remain unauthorized until KFR-08 is completed_verified and successor selection is recorded.
