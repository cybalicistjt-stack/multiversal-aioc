# IA-D08-004 — Broad Offline Deferral Traceability

**Owner:** John Brandon Turner  
**Status:** TRACEABILITY COMPLETE FOR DESIGN REVIEW

## Purpose

Trace the broad-offline deferral boundary to existing Multiversal authority, reconnect, proposal/approval, shared draft, permission, history, and future-extension contracts.

## Upstream authority

| Source | Contract reused |
|---|---|
| P9-02 Authoritative Session Architecture | Authoritative service owns canonical Session command/Event ordering and reconnect. |
| IA-D04-002 Proposal and Approval Shared Component | Approval authority, decision receipts, expected versions, review claims, permission-safe projection. |
| IA-D04-003 Two-Device Interruption and Reconnect Matrix | Ambiguous command status, duplicate delivery, lost responses, Event-gap recovery, revocation. |
| IA-D04-004 Authoritative Result and History Presentation | Canonical result history is server-authoritative and attributable. |
| IA-D05 / IA-D06 integration contracts | Cross-domain Effects remain atomic and owning-domain authoritative. |
| IA-D07 Creator/Campaign-local Content | Draft vs published/canonical state, immutable versions, reviewed migration, import/export boundaries. |
| IA-D08-001 Optional AI Assistant | AI output remains advisory/draft and cannot become authority during offline operation. |
| IA-D08-002 AI Governance Matrix | Provider/privacy/cost/provenance and deterministic non-AI fallback remain intact offline. |
| IA-D08-003 Advanced Map/Vehicle Deferral | Unsupported future data may be retained opaquely; unknown processors never execute silently. |
| MV-AI-EFFICIENCY-001 | Targeted construction validation and one relevant hosted final gate. |

## Requirement traceability

| Requirement | Package section | Fixtures |
|---|---|---|
| Offline cannot create canonical authority | Governing rule / O3-O4 | 005, 006, 023, 024 |
| Ambiguous submit must use status lookup | Reconnect algorithm | 002, 003, 004, 007 |
| Duplicate replay must be idempotent | O2 / reconnect | 004, 012 |
| Expected-version conflict prevents blind replay | Reconnect / conflict rule | 013, 015 |
| No silent last-write-wins | Conflict rule | 011, 013 |
| Role change invalidates privileged cache | Hidden-information rule | 009, 010, 017 |
| Event gaps recover from authoritative sequence | Reconnect algorithm | 020 |
| Local clocks are not authority | Provenance | 021 |
| Drafts survive without becoming canonical | O1 | 001, 011 |
| Presentation state may remain local | O0 | 022 |
| Unsupported future data preserved opaquely | Deferred-data preservation | 018, 019 |
| Unknown processors never execute | Deferred-data preservation | 019 |
| Ownership/publication require online governance | O3 | 023, 024 |
| Accessibility communicates stale/conflict state | Accessibility | all stateful fixtures |

## Downstream handoff to IA-D08-005

IA-D08-005 must verify that all optional and experimental capabilities are isolated so they cannot become hidden mandatory dependencies. It must consume this offline boundary together with:

- optional AI isolation;
- advanced map/vehicle deferral;
- creator/experimental extension boundaries;
- provider and cost fallback;
- capability negotiation;
- permission/provenance rules.

The IA-D08-005 isolation review must treat broad offline as **deferred optional capability**, not as a missing prerequisite for the internal-alpha first playable path.

## Application implementation boundary

P9-06 implementation may build only the retained offline-safe seams required by accepted upstream contracts until a later owner-approved work item promotes broader offline capability. No design text in IA-D08-004 authorizes peer authority, production offline databases, CRDT infrastructure, paid synchronization services, or deployment.
