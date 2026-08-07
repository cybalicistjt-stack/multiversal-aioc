# IA-D08-004 — Broad Offline Deferral Readiness

**Owner:** John Brandon Turner  
**Status:** READY FOR TARGETED VALIDATION

## Readiness conclusion

The broad-offline boundary is sufficiently specified for internal-alpha implementation planning because it distinguishes recoverable local work from authoritative mutation, explicitly defers broad offline authority, and defines reconnect, conflict, visibility, provenance, accessibility, and migration behavior.

## Retained capability readiness

The retained internal-alpha contract is bounded to:

- authorized read-only cache with explicit stale/offline state;
- recoverable local drafts;
- local presentation state;
- only explicitly replay-safe queued intent envelopes;
- command status lookup;
- authoritative Event-gap recovery;
- reconnect reauthorization and revalidation;
- explicit conflict routing;
- permission-safe cache invalidation;
- opaque versioned extension preservation.

These seams are compatible with existing IA-D04 reconnect and approval contracts and do not require broad offline infrastructure.

## Deferred capability readiness

Broad offline hosting, offline canonical GM authority, peer-to-peer authority transfer, CRDT/OT canonical collaboration, unrestricted offline mutation, offline publication/ownership/entitlement changes, and silent automatic merge remain explicitly deferred.

No retained internal-alpha capability depends on these deferred systems.

## Blocking acceptance criteria

1. No local client can fabricate authoritative Session Events.
2. No ambiguous command is retried before status/Event reconciliation.
3. Replay-safe intents carry stable idempotency and expected-version context.
4. No silent last-write-wins is permitted for divergent canonical/draft state.
5. Approval, ownership, publication, shared-Resource spending, entitlement mutation, and destructive canonical changes remain online-governed.
6. Role/permission changes remove newly unauthorized cached content from display, semantics, search, counts, exports, and optional-AI context.
7. Hidden map/graph topology cannot remain inferable from cached layout after revocation.
8. Local timestamps are provenance only and never canonical order.
9. Unknown extension processors never execute.
10. Unsupported future data is preserved or rejected explicitly, never silently discarded or approximated.
11. Offline state is accessible without color/motion-only signaling.
12. User-authored drafts remain recoverable where policy permits even when canonical commit is rejected.
13. Event-gap recovery uses authoritative checkpoint/sequence state.
14. Multi-device divergence enters explicit conflict/review unless the owning type has a deterministic merge contract.
15. No broad-offline feature is represented as required for the internal-alpha first playable path.
16. P9-06-008-attempt-002 remains separate, unfinished, and unmodified.

## Non-blocking future work

The following remain intentionally future-facing and do not block internal alpha:

- production-grade encrypted offline data stores;
- long-duration offline campaign hosting;
- CRDT/OT infrastructure;
- peer authority election;
- offline pack publication;
- offline canonical world migration;
- offline subscription/entitlement mutation;
- unattended bulk replay policy;
- advanced offline conflict visualization;
- large-scale device synchronization.

## Implementation risks

### Risk — Cached privileged data after role change
Mitigation: authorization-scoped cache identity, reconnect reauthentication, projection invalidation, semantic/search purge.

### Risk — Duplicate Effects after ambiguous disconnect
Mitigation: idempotency identity, status lookup, authoritative Event sequence reconciliation before retry.

### Risk — User assumes queued means committed
Mitigation: explicit queued/unsynchronized/stale/conflicted vocabulary and accessible state semantics.

### Risk — Draft loss after server rejection
Mitigation: separate local draft persistence from canonical commit result; preserve recoverable user-authored content when policy permits.

### Risk — Future extension data silently affects current resolution
Mitigation: opaque versioned retention plus processor allowlist/capability negotiation; unsupported processors do not execute.

## Handoff readiness

IA-D08-005 may begin after IA-D08-004 passes its targeted validator and final relevant hosted gate. It should perform the optional/experimental isolation review using IA-D08-001 through IA-D08-004 as its governing input set.
