# KFR — Knowledge & Familiarity Relations

**Program ID:** KFR  
**Status:** OWNER-APPROVED — COMPLETED THROUGH KFR-07; KFR-08 SELECTED_NOT_STARTED  
**Activation:** after completed_verified WCI-05  
**Successor:** ODL-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

KFR-01 through KFR-07 are `completed_verified`.

KFR-07 — Authoring, Inspection, Search & Provenance UX — completed on exact validated application head `ba200bda8de5b7298c205d852213a621b5ef0b77`, current-family run `33495773941`, and application merge `9e4754a52026723c77af5830b92a453a867b4025`. Its implementation authority is retired. Final proof used the governed self-hosted Windows and Linux lanes plus deterministic comparison; the deterministic receipt SHA-256 is `77351208992d931f1380745ec50c3a49c618a710478aefc6dcfddf7c5f64c9b5`. Genuine RED preceded production and the first production head passed without a feature repair commit.

KFR-08 — Cross-Domain Golden Proof — is `selected_not_started` only from exact application main `9e4754a52026723c77af5830b92a453a867b4025`. It has no implementation branch or implementation authority.

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
8. **KFR-08 — Cross-Domain Golden Proof** — selected_not_started.

## KFR-07 completion boundary

KFR-07 delivers a visibility-safe read-only UX projection across separately labeled KFR-01 through KFR-06 inputs. Hidden/private KFR and owner-domain inputs are filtered before topology, cardinality, search, autocomplete, counts, previews, inspection, exports, diagnostics, notifications, receipts or optional-AI context. Hidden cardinality is never exposed.

Search, count, preview/inspection and AI-context derived outputs require explicit visibility-projection authorization. Inspection remains read-only. Provenance UX displays only explicit existing provenance references attached to visible inputs; missing provenance remains absent/unknown and is never fabricated or inferred. Visible results, inspection collections, provenance references and deterministic receipts use stable ordering independent of input order.

Authoring remains intent/proposal UX only. Existing AuthoringAuthority dimensions remain independent; an allowed decision for one dimension does not imply another. KFR-07 composes authoring intent only after the relevant explicit allowed decision and does not execute AuthoringDraftPort or AuthoringProposalReviewPort writes, publish, reveal, or canonical-promote content.

Canonical KFR/source-domain owners, AuthoringAuthority/AuthoringDraft/AuthoringProposalReview, and Permission/visibility systems remain authoritative. KFR-07 introduced no canonical write, permission escalation, hidden-data reveal, provenance fabrication, publication or promotion authority, no durable persistence, and no migration `0022`.

## KFR-08 selection boundary

KFR-08 will resolve one cross-domain golden proof over completed KFR semantics only after a future owner `Continue` establishes its governed-start contract. Selection is proof/integration only and authorizes no new KFR algorithm, canonical write, permission escalation, provenance fabrication, hidden-data reveal, durable persistence or migration `0022`.

ODL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
