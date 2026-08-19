# APW-02 Review Receipt

**Work item:** APW-02 — Asynchronous Action, Proposal and GM Inbox Contract  
**Attempt:** APW-02-attempt-001  
**Design branch:** `governance/apw-02-async-proposal-inbox`  
**Review state:** substantive design complete; repository/PR validation pending

## Reviewed source contracts

- APW-01 universal-user/contextual authority.
- A6 Action proposal, decision, operation-status and reconnect contracts.
- MV-IA-F006 First Playable Action and GM Approval Loop.
- MV-IA-F021 Autosave, Reconnect, Recovery and Bounded Offline Use.
- Existing permissions/hidden-information and APM-01 AI/automation authority boundaries.

## Findings

1. Asynchronous play can reuse A6 proposal/decision/Event architecture; no separate async rules engine is required.
2. One stable `proposalId` is the durable intent thread and may produce at most one final authoritative outcome.
3. Proposal revisions keep the proposal ID, increment proposal version, use new state-changing operation identity, preserve prior versions and cannot overwrite a final decision.
4. Semantic stale refresh requires explicit proposer revision/acceptance; presentation-only refresh does not.
5. Withdrawal maps to attributable revocation/cancellation before final decision and must resolve races using status lookup rather than rollback invention.
6. Expiry is server-governed; client clocks and notification age are not authority.
7. Clarification is nonfinal coordination. A GM may ask; the proposer explains, revises or withdraws. Clarification cannot silently rewrite Player intent.
8. GM inbox rows, ordering, assignment and review leases are permission-filtered coordination projections and cannot grant decision authority.
9. Final decision always reauthorizes current delegation, versions, permissions, entitlements, legality and prior final status.
10. Concurrent reviewers are safe because final uniqueness is enforced by domain persistence, not by UI locks.
11. Notifications are minimal attention signals with deep-link reauthorization; duplicate/missing delivery cannot change proposal truth.
12. Offline support remains bounded to safe local drafting; durable submit/revise/withdraw/decision requires authoritative connectivity unless a later separately proven command path changes that.
13. Reconnect uses status lookup, event-gap recovery and permission/cache invalidation before retrying state-changing work.
14. Optional AI/automation remains advisory and cannot decide, rewrite intent, expand delegation or commit.

## Gate review

- Draft/proposal/decision/Event distinctions explicit: **PASS**
- Stable revision and provenance model defined: **PASS**
- Withdrawal/revocation/expiry/race behavior defined: **PASS**
- Clarification preserves Player intent: **PASS**
- Inbox/lease/order are coordination only: **PASS**
- Decision-time reauthorization defined: **PASS**
- Stale-state classes and recovery defined: **PASS**
- Notification nonauthority/nonleakage defined: **PASS**
- Reconnect/status/idempotency at-most-one behavior defined: **PASS**
- AI/automation nonauthority preserved: **PASS**
- Application implementation/migration authorized: **NO**
- Alternate async mechanics authorized: **NO**
- CCTI-12-T04 resumed: **NO**

Repository-health/PR merge evidence remains to be attached before `completed_verified` is claimed.
