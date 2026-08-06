# IA-D07-003 — Bounded MV-IA-F018 Creator and Campaign-local Content

**Owner:** John Brandon Turner  
**Status:** COMPLETE DESIGN / IMPLEMENTATION-READY  
**Boundary:** Internal-alpha design only; implementation remains dependency-gated by P9-06.

## Purpose

Define safe creation, proposal, review, approval, versioning, installation, use, export, and retirement of creator-authored and Campaign-local content without silently promoting it to canonical source content.

## Content classes

`CreatorDraft`, `CreatorRelease`, `CampaignLocalObject`, `ContentProposal`, `ReviewDecision`, `InstallBinding`, and `LocalOverride` use stable IDs and exact provenance. Supported bounded types are Abilities, Actions, Effects, Conditions, Items, Creatures/NPCs, Species, Vehicles, Rules Profiles, World entries, maps, and adventure fragments.

## Authority and lifecycle

Draft, submit, review, approve, reject, revise, publish to private creator library, install to Campaign, enable, disable, export, import, and delete are separate permissions. Campaign installation never grants canonical status. Canonical promotion is an owner gate outside this work item.

## Validation and sandboxing

Schemas, stable IDs, references, dependency closure, processor allowlists, resource bounds, permissions, hidden-information behavior, and deterministic fixtures are validated before installation. Arbitrary code, network calls, secrets, executable scripts, and unrestricted processors are prohibited.

## Campaign-local overlays

Campaign-local objects and overrides are scoped to one Campaign, versioned, attributable, reversible, and distinguishable in every projection. Overrides pin their base source version and express explicit differences; source updates never overwrite them silently.

## Proposal and review

Creators submit immutable proposal revisions. Review records rationale, requested changes, risk classification, provenance, and acceptance scope. Approval produces a bounded installable release, not a mutation of the draft or canonical source.

## Runtime integrity

Installed content participates through the same server-authoritative proposal, result, permission, Asset, map, vehicle, world, and adventure contracts as canonical content. Invalid or disabled definitions cannot initiate new operations; prior history remains interpretable through snapshots and tombstones.

## Hidden information and exports

Private drafts, rejected proposals, hidden local objects, GM-only mechanics, dependency details, and unpublished releases are filtered before search, counts, previews, exports, diagnostics, notifications, and optional-AI context. Exports are role-filtered and provenance-complete.

## Accessibility and recovery

List, table, detail, diff, dependency outline, review queue, keyboard, touch, screen-reader, responsive, high-contrast, reduced-motion, and nonvisual parity are required. Mutations use idempotency keys and expected versions; recovery uses status lookup, snapshot-plus-tail repair, and compensating events.

## Implementation slices

CC-S01 identity/lifecycle; CC-S02 schemas/sandbox; CC-S03 proposals/reviews; CC-S04 Campaign installation/overlays; CC-S05 runtime adapters; CC-S06 hidden projections/accessibility; CC-S07 import/export/recovery; CC-S08 fixtures/handoff.

## Decision

IA-D07-003 is implementation-ready. Next: **IA-D07-004 — world/adventure content authority matrix**. `P9-06-008-attempt-002` remains unfinished and unmodified.