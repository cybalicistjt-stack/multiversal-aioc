# APW-07 Review Receipt

**Work item:** APW-07 — Persistence, Recovery, Security and Hybrid Acceptance Architecture  
**Attempt:** APW-07-attempt-001  
**Review scope:** APW persistence/recovery/security/hybrid design only  
**Completion claim:** pending exact-head repository-health and merge

## Reviewed authority and dependencies

- APW-02 through APW-06 are `completed_verified`.
- CSW-10 is `completed_verified` in PR #449 and supplies creator persistence/handoff boundaries without activating CSW implementation.
- MV-IA-F021 remains the existing recovery foundation for local draft versus authoritative state, stable operation IDs, expected versions, command-status lookup, Event cursors, conflict records, bounded offline snapshots and permission/entitlement/schema/lifecycle revalidation.
- Existing Campaign, Action/proposal, Event, resource, authoring, visibility and notification owning domains remain authoritative.

## Decisions reviewed

1. **One state/history model.** Live, asynchronous and hybrid cadence use the same Campaign identity and authoritative owning-domain/Event history.
2. **No offline authoritative mutation.** Bounded read-only snapshots and approved local drafts remain the Internal Alpha boundary.
3. **Stable idempotency identity.** One user intent uses one stable operation ID across retry/reconnect/duplicate transport.
4. **At-most-once accepted effect.** Replayed transport requests return prior status/result rather than applying business effects twice.
5. **Expected-version concurrency.** Mutations that depend on mutable state must fail stale/conflict rather than silently overwrite.
6. **Ambiguous failure uses status lookup.** A timeout becomes `status unknown`; a new operation ID is not automatically generated.
7. **Event/history order comes from the owning service.** Client clocks, notification times and device arrival order are not authoritative ordering.
8. **Notification delivery is not business authority.** Underlying operations/results remain durable and discoverable even if delivery fails.
9. **Reauthorization before delayed mutation.** Permission, delegation, control, entitlement and object lifecycle are re-evaluated before decision/commit and on protected reconnect/restore.
10. **Current visibility precedes aggregation.** Counts, search, history, notifications, diagnostics, exports, conflicts and optional-assistance context are computed only after authorization filtering.
11. **Cross-device caches are non-authoritative.** Divergent drafts are preserved and reconciled explicitly; no last-write-wins governed state.
12. **Long delay does not advance Campaign state.** Expiry/progress exists only where an owning workflow explicitly defines it.
13. **Recovery preserves evidence.** Prefer status-unknown/stale/conflict/recovery-required over guessed success/failure or destructive reset.
14. **Zero-paid-service core remains testable.** Recovery/status/Event-gap/local-draft behavior and deterministic fixtures require no paid sync, notification or AI service.

## Hybrid proof reviewed

The live → async → live proof preserves:

- one Campaign ID;
- one authoritative Event/history sequence;
- stable proposal/operation identity;
- current-version and current-authority checks at delayed GM decision;
- one authoritative result or a stale/review-required outcome;
- result discovery independent of notification delivery;
- cross-device status/Event-gap recovery;
- current visibility/entitlement filtering on Player return;
- live resumption without a forked state engine.

## Security/nonleakage review

Protected data must be removed before:

- queue or badge counts;
- search/autocomplete;
- history/recent lists;
- notification payload generation;
- conflict comparison;
- offline snapshot issuance;
- diagnostics/export;
- optional-assistance context.

Spoiler Shield remains a presentation preference only and cannot change authorization.

## Nonauthorization confirmed

This package does **not** authorize:

- application implementation;
- migration execution;
- broad offline authoritative play;
- peer-to-peer/multi-master authoritative sync;
- automatic last-write-wins governed state;
- paid synchronization/notification/AI dependencies;
- release/deployment;
- CCTI-12-T04 work before September 2026.

## Declared validation gate

The bounded APW-07 governance branch must pass AIOC `Validate Repository Health` on its exact PR head before merge. Only after that success and merge may `APW-07-attempt-001` be recorded `completed_verified` and APM-06 be selected.
