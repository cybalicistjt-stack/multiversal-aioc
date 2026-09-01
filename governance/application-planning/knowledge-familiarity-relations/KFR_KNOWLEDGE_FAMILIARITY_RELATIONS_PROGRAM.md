# KFR — Knowledge & Familiarity Relations

**Program ID:** KFR  
**Status:** OWNER-APPROVED — COMPLETED THROUGH KFR-06; KFR-07 IN_PROGRESS  
**Activation:** after completed_verified WCI-05  
**Successor:** ODL-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

KFR-01 through KFR-06 are `completed_verified`.

KFR-06 — Profession, Research, Mentorship & Learning Integration — completed on exact validated application head `8a52c98924a59e48d92edcae552cc79e2e576a4f`, current-family run `33487548247`, and application merge `ac01ececdeab93e03c2155d28759b9b2a477f63e`. Its implementation authority is retired. Final proof used the governed self-hosted Windows and Linux lanes plus deterministic comparison; the deterministic receipt SHA-256 is `8b69620843dc98a1dabe23adfa8d6bbf6d0be1f202c8fa5b813684248ac73cd7`.

KFR-07 — Authoring, Inspection, Search & Provenance UX — is bounded `in_progress` from exact application main `ac01ececdeab93e03c2155d28759b9b2a477f63e` on `integration/kfr-07-authoring-inspection-search-provenance-ux` after the owner `Continue` governed start.

## Purpose

KFR supplies governed familiarity relations that canonical Character, Skills/Progression, Professions, Research, Vehicle/platform, Equipment/Asset, Organization/relationship, World/WCI and permission systems may consume without replacing their state or authority.

## Tranches

1. **KFR-01 — Source/Authority Crosswalk & Familiarity Vocabulary** — completed_verified.
2. **KFR-02 — Hierarchical Familiarity Graph** — completed_verified.
3. **KFR-03 — Character Knowledge, Experience & Explicit Familiarity Records** — completed_verified.
4. **KFR-04 — Transfer, Adjacency, Confidence & Unknown-State Rules** — completed_verified.
5. **KFR-05 — Operator Qualification & Vehicle/Machine/Equipment Integration** — completed_verified.
6. **KFR-06 — Profession, Research, Mentorship & Learning Integration** — completed_verified.
7. **KFR-07 — Authoring, Inspection, Search & Provenance UX** — in_progress.
8. **KFR-08 — Cross-Domain Golden Proof** — planned.

## KFR-06 completion boundary

KFR-06 delivers a visibility-safe read-only integration projection over explicit canonical-owner evidence for `profession`, `research`, `mentorship`, and `learning`. KFR-03 records, KFR-04 transfer/confidence and KFR-05 qualification remain separately labeled advisory context only and never advance owner state. Hidden/private evidence is filtered before counts, search, explanation, deterministic receipts and AI context. No durable KFR-06 persistence or migration `0022` was introduced.

## KFR-07 governed-start boundary

KFR-07 implements a visibility-safe, read-only UX projection across separately labeled KFR-01 through KFR-06 inputs. Hidden/private KFR and owner-domain inputs are filtered before topology, cardinality, search, autocomplete, counts, previews, inspection, exports, diagnostics, notifications, receipts or optional-AI context. Hidden cardinality is never exposed.

Search, count, preview/inspection and AI-context derived outputs require their corresponding explicit visibility-projection authorization. Denied output authorization returns no derived content rather than leaking a count, snippet, detail or provenance clue.

Inspection remains read-only. Provenance UX displays only explicit existing provenance references attached to visible inputs; missing provenance remains absent/unknown and is never fabricated or inferred. Visible results, inspection collections, provenance references and deterministic receipts use stable ordering independent of input order.

Authoring is intent/proposal UX only. Existing AuthoringAuthority dimensions remain independent and an allowed decision for one dimension does not imply another. KFR-07 may compose authoring intent only after the relevant explicit allowed decision. It does not itself execute AuthoringDraftPort or AuthoringProposalReviewPort writes, publish, reveal, or canonical-promote content.

Canonical KFR/source-domain owners, AuthoringAuthority/AuthoringDraft/AuthoringProposalReview, and Permission/visibility systems remain authoritative. KFR-07 grants no canonical write, permission escalation, hidden-data reveal, provenance fabrication, publication or promotion authority.

KFR-07 introduces no durable persistence, duplicate search index, duplicate provenance ledger or canonical write store; migration `0022` remains unreserved. Accessible nonvisual equivalents are required. Final validation requires exactly one KFR-07 Validation Core profile with zero historical predecessor fanout, genuine RED before production, and exact-head self-hosted Linux/Windows plus deterministic comparison.

KFR-08, ODL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
