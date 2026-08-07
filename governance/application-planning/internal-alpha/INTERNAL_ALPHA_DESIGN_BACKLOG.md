# Internal Alpha Feature Design Backlog

**Program:** MV-IA-001  
**Version:** 0.36.0  
**Status:** ACTIVE DESIGN BACKLOG  
**Owner:** John Brandon Turner

## Backlog rule

This backlog governs design packets, fixture specifications, and integration reviews. Implementation remains dependency-gated by P9-06. A design item is complete only when artifacts exist, limitations and boundaries are explicit, deterministic validation passes, and repository merge evidence is recorded.

## IA-D01 — Program foundation — COMPLETE
## IA-D02 — Shared foundations — COMPLETE
## IA-D03 — Character and Campaign preparation — COMPLETE
## IA-D04 — First playable loop — COMPLETE
## IA-D05 — Relationship, social, and investigation systems — COMPLETE
## IA-D06 — Combat and Assets — COMPLETE
## IA-D07 — World, adventure, and Project depth — COMPLETE

## IA-D08 — Optional AI and experimental systems — COMPLETE

1. **IA-D08-001 — MV-IA-F023 Optional AI Assistant boundaries and interaction contract — complete.**
2. **IA-D08-002 — AI permission, provenance, cost, and fallback matrix — complete.**
3. **IA-D08-003 — advanced map and vehicle deferral package — complete.**
4. **IA-D08-004 — broad offline deferral package — complete.**
5. **IA-D08-005 — optional and experimental isolation review — complete; merged in PR #186.**

## IA-D09 — Internal-alpha release-design package

Traceability, bounded fixture catalog, permission/accessibility/recovery matrices, explicit budgets, tester onboarding, dependency-ordered implementation queue, owner-decision register, release boundaries, and final design completion review.

**IA-D09 — Internal-alpha release-design package — package constructed; targeted validation and merge verification pending.**

## Completion records

### IA-D07

World, adventure, creator, Campaign-local content, authority, and authoring integration design are complete. `P9-06-008-attempt-002` remains unfinished and unmodified.

### IA-D08

The optional/experimental series is complete through IA-D08-005. The final isolation review requires all-optionals-off core operation, manual and semantic fallbacks, provider-neutral canonical identity, feature-gate safety, failure containment, opaque unsupported-extension preservation, identical permission filtering, accessibility independence, typed diagnostics, and fresh owning-domain validation before optional output can affect a governed proposal. IA-D08-005 merged in PR #186 at merge SHA `2d8eed23ac15a56e4274ebda11fac30741334599`.

### IA-D09

The release-design package consolidates IA-D01 through IA-D08 into an engineering handoff with series-level bidirectional traceability, twenty-four bounded deterministic release fixtures, permission/accessibility/recovery blocking gates, explicit performance/cost/test-data budgets, tester-entry requirements, a twelve-slice dependency-ordered implementation queue, owner-only release/data/credential/spend gates, and a final design-completion review. It explicitly does not authorize tester access, implementation release, deployment, public release, production credentials, real-user data collection, paid-provider commitment, or autonomous AI canonical authority.

## Current next design item

**IA-D09 — targeted validation, governed PR, and merge verification. Do not invent IA-D10.**

## Parallel paused tracks

- `P9-06-008-attempt-002` remains unfinished and paused in the application-implementation track.
- The Design Standards Completion subproject is paused/resumable as recorded in `APPLICATION_IMPLEMENTATION_ROADMAP.md` v2.1.0; its chat-generated DS-006/DS-007 working packages are not repository-canonical until later governed ingestion.

## Validation-efficiency rule

`governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md` controls. Each IA item uses its targeted deterministic validator during construction and one final relevant hosted gate. Unrelated historical IA or Development Brain workflows must not be treated as required validation for every new packet. Recurring unrelated fan-out is a workflow-scoping defect.

## Historical validation anchors

These archival statements preserve earlier validated routes and versions. They are not the current next item.

IA-D03-004 — alpha content and fixture specification — complete.  
IA-D03-005 — Character/Campaign integration review — complete.  
IA-D04-001 through IA-D04-005 — first playable loop series — complete.  
IA-D05-001 through IA-D05-006 — relationship/social/investigation series — complete.  
IA-D06-001 through IA-D06-006 — combat/assets series — complete.  
IA-D07-001 through IA-D07-005 — world/adventure/authoring series — complete.  
IA-D08-001 through IA-D08-005 — optional AI/experimental isolation series — complete.
