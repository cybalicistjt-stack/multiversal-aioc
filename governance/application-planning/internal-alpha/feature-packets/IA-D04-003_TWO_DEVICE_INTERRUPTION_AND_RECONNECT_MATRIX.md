# IA-D04-003 — Two-Device Interruption and Reconnect Matrix

**Program:** MV-IA-001  
**Version:** 0.1.0  
**Status:** implementation-ready design  
**Owner and final authority:** John Brandon Turner  
**Companion matrix:** `IA-D04-003_TWO_DEVICE_RECONNECT_MATRIX.json`

## 1. Purpose

This contract defines deterministic behavior when the Player and GM use separate devices and either device disconnects, retries, changes authorization, or receives delayed or duplicated delivery during the first playable proposal-and-approval loop.

## 2. Scope and boundary

It covers Player and GM devices, delegated Assistant-GM devices, observer projections, local drafts, proposal submission, pending review, advisory review claims, final decisions, consumer commits, Event delivery, reconnect, revocation, and recovery. It does not authorize application implementation, production services, credentials, release, or canonical promotion.

## 3. Governing authority

MV-IA-F021 controls recovery and bounded offline behavior. MV-IA-F006 controls the live Action loop. IA-D04-002 controls the reusable proposal-and-approval component. IA-D02-006 and IA-D03-005 control identity, authorization, stable IDs, projections, persistence, and Campaign/Session binding.

## 4. Core authority rule

> Device-local state, caches, review claims, notifications, and realtime messages are advisory. Accepted durable Events and current server projections control.

Silence is not approval. A sent command is not an accepted command. A displayed result is not authoritative until its durable status and current projection agree.

## 5. Device and session identity

Every reconnect and status lookup binds `subjectId`, `authSessionId`, `deviceId`, selected workspace and Campaign context, role, Character or actor control, permission and entitlement versions, protocol version, and correlation identity. Device identity assists recovery and diagnostics but never grants authority.

## 6. Stable operation identities

Proposal submit, decision, consumer commit, status lookup, and Event acknowledgement use stable IDs. Retrying with the same ID returns the prior result or current status. Reusing an ID with a conflicting payload fails safely.

## 7. State vector

Each device preserves only a safe state vector: selected context, proposal and decision IDs, operation IDs, expected versions, last acknowledged Event sequence, last projection version, permission and entitlement hints, consumer-profile version, pack lock, and correlation ID. Hidden business data is not copied merely to aid reconnect.

## 8. Two-device convergence

Authorized devices converge through status lookup, ordered durable Events, and current role-safe projections. They do not merge authoritative state peer-to-peer. Realtime delivery may accelerate display but cannot settle conflicts.

## 9. Player interruption before submit

Before authoritative submit, only local draft recovery is permitted. A local autosave on Device A does not create a proposal visible on Device B. Cross-device draft transfer requires an authorized, explicit synchronization mechanism and remains nonauthoritative until submission.

## 10. Ambiguous Player submit

When the submit response is lost, both Player devices query with the original `operationId`. Exactly one durable proposal, definitive rejection, or still-processing status is returned. Device B must not create a replacement operation merely because Device A lacks a response.

## 11. Pending proposal handoff

A Player may change devices while a proposal is pending. The new device receives only the role-safe proposal status and current projection. It does not resubmit, reserve costs, or reveal GM-only warnings.

## 12. GM review claims

Opening a review may create an advisory lease. A disconnect does not approve or deny. On expiry or explicit release, another authorized GM device may claim review. A claim never survives role or delegation revocation.

## 13. Ambiguous final decision

Approve, deny, and modify-and-approve commands use stable decision and operation IDs. Lost responses are recovered by decision and command status lookup. Exactly one final decision and at most one consumer commit may succeed.

## 14. Concurrent GM devices

When two authorized GM devices race, the authoritative service serializes against current proposal and aggregate versions. One final decision wins. The losing device receives current final status; silent overwrite is prohibited.

## 15. Stale versions and explicit conflict

Changes to Session, actor, target, proposal, permissions, entitlements, packs, or schemas can make a review stale. The proposal and evidence are preserved, no consumer mutation is committed, and the user receives an explicit recovery path.

## 16. Ordered Event-gap recovery

Each device sends its last acknowledged sequence. Duplicate Events are ignored by Event identity. A gap triggers bounded replay or a current snapshot plus sequence anchor. A client never invents missing Events or treats a later realtime message as proof that earlier Effects committed.

## 17. Projection and hidden-information safety

Player, GM, Assistant-GM, and observer devices receive server-filtered projections before serialization. Queue counts, notifications, history, reconnect payloads, exports, diagnostics, and optional-AI context follow the same filtering. Protected existence is not disclosed.

## 18. Revocation and cache invalidation

Role, delegation, control, permission, entitlement, or selected-context revocation invalidates review claims, subscriptions, protected caches, pending route access, status lookup outside current authority, and optional-AI projections on every device.

## 19. Offline and divergent drafts

Offline use may read unexpired authorized projections and edit local drafts. It cannot submit, decide, approve, deny, modify, or commit. Divergent drafts from two devices produce an explicit conflict record and allowed dispositions; silent last-write-wins is prohibited.

## 20. Accessibility and responsive parity

Desktop, tablet, and mobile devices expose the same status, conflict, recovery, and decision meaning. Screen-reader and keyboard users can inspect current device, authoritative status, stale findings, modification differences, and recovery choices. Noncolor text distinguishes local, pending, committed, stale, revoked, and recovery-required states.

## 21. Deterministic scenario matrix

The companion matrix defines 24 fixtures spanning Player and GM interruption boundaries, duplicate delivery, lost responses, stale versions, claim expiry, revocation, Event gaps, observer projection, offline conflicts, and service restart. Every scenario ends in a single explicit authoritative status.

## 22. Implementation slices

Eight dependency-ordered slices cover identity envelopes; local and submit recovery; pending and review handoff; decision and commit recovery; Event and projection convergence; revocation; offline conflict; and accessible deterministic adapters.

## 23. Blocking acceptance criteria

- **TDR-AC-001:** Two devices recover the same proposal by stable identity without duplicate submit.
- **TDR-AC-002:** Local drafts remain nonauthoritative and device-scoped until an explicit authorized synchronization.
- **TDR-AC-003:** Lost submit responses use status lookup before retry.
- **TDR-AC-004:** Lost decision responses use status lookup before retry.
- **TDR-AC-005:** At most one final decision succeeds.
- **TDR-AC-006:** At most one consumer commit succeeds.
- **TDR-AC-007:** Review claims are advisory, expiring, and revocation-aware.
- **TDR-AC-008:** Stale proposal or aggregate versions block commit and preserve evidence.
- **TDR-AC-009:** Duplicate Events and responses do not duplicate business effects.
- **TDR-AC-010:** Event gaps recover through ordered durable history or current snapshot plus sequence anchor.
- **TDR-AC-011:** Player projections exclude GM-only evidence.
- **TDR-AC-012:** Observer projections exclude proposal and queue existence.
- **TDR-AC-013:** Revocation clears protected access and caches on every device.
- **TDR-AC-014:** Permission and entitlement changes are revalidated before recovery.
- **TDR-AC-015:** Offline authoritative submit and decision are prohibited.
- **TDR-AC-016:** Divergent drafts require explicit conflict disposition.
- **TDR-AC-017:** Server time controls expiry.
- **TDR-AC-018:** Responsive and assistive presentations preserve recovery meaning.
- **TDR-AC-019:** Zero-paid-service and zero-AI core adapters remain possible.
- **TDR-AC-020:** The exact next handoff is IA-D04-004.

## 24. Handoff

IA-D04-004 must define the authoritative result and history presentation that consumes these recovery states, Event sequences, decision receipts, hidden-information projections, and accessible status semantics.
