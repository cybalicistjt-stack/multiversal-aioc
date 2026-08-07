# IA-D08-004 — Broad Offline Deferral Package

**Owner:** John Brandon Turner  
**Status:** READY FOR VALIDATION — DESIGN BOUNDARY  
**Boundary:** Internal-alpha design only; implementation remains dependency-gated by P9-06.

## Purpose

Define exactly which offline capabilities are intentionally deferred beyond internal alpha, while preserving the limited offline-safe behaviors already required by canonical Multiversal contracts. This package prevents a disconnected client from becoming an alternate authority, prevents silent last-write-wins after reconnect, and preserves unsupported offline intent and data in a recoverable form.

## Governing rule

**Offline does not create authority.**

A disconnected client may preserve user-authored drafts, cached authorized projections, queued low-risk intents, and recoverable local context where a canonical contract explicitly permits them. It may not invent authoritative session Events, spend authoritative Resources, resolve contested state, approve proposals, publish content, transfer ownership, reveal hidden information, or silently reconcile divergent versions.

## Retained internal-alpha offline-safe capabilities

The internal-alpha retained contract supports, where the governing feature permits it:

1. **Read-only authorized cache:** previously authorized projections may remain viewable when policy and cache lifetime permit, clearly marked stale/offline.
2. **Recoverable drafts:** unsent notes, authored text, form edits, search/filter state, layout state, and other explicitly draft-scoped data may be persisted locally.
3. **Queued idempotent intent:** a bounded command may be queued only when its contract defines an idempotency key, expected version, status lookup, safe replay semantics, and server-side reauthorization.
4. **Reconnect status lookup:** ambiguous commands are resolved by authoritative status/event lookup before retry.
5. **Event-gap recovery:** clients resume from authoritative sequence/checkpoint state and request missing Events rather than reconstructing truth locally.
6. **Draft export/recovery:** user-authored local material may be preserved/exported when policy permits, even if it cannot be committed automatically.
7. **Permission-safe cached reference:** reference content may remain available only within the last authorized projection and must not widen access.
8. **Explicit stale-state UX:** offline, queued, unsynchronized, rejected, conflicted, and revalidated states are visibly distinct from canonical success.

## Broad offline capabilities deferred beyond internal alpha

The following are intentionally deferred unless a later work item explicitly promotes them:

- full offline campaign hosting;
- offline GM authority over canonical Session state;
- offline authoritative combat resolution;
- peer-to-peer authority transfer during server loss;
- multi-user offline collaborative editing with automatic merge;
- CRDT/OT-backed canonical world editing;
- unrestricted offline inventory/ownership transfer;
- offline entitlement mutation;
- offline publication or pack promotion;
- offline canonical character advancement;
- offline cross-device command arbitration;
- automatic three-way merge of opaque creator content;
- offline AI actions that later auto-commit;
- background local simulation treated as authoritative history;
- local creation of server Event sequence numbers;
- local approval/denial treated as committed GM authority;
- offline hidden-information expansion based on cached privileged data;
- unrestricted queued destructive actions;
- unattended bulk replay of stale commands after long disconnects;
- silent rebase or last-write-wins conflict resolution;
- local schema migration that silently rewrites canonical synced records;
- offline financial/subscription/sponsored-month mutation;
- autonomous offline vehicle/faction/NPC control that later backfills history.

## Command classes while offline

### Class O0 — local-only presentation state

Examples: current tab, map camera, expanded sections, local sort/filter.

May update freely. Never canonical.

### Class O1 — recoverable user draft

Examples: notes, unsent message, creator draft, unpublished description edits.

May persist locally with stable draft identity and provenance. Reconnect requires authorization and version validation before canonical commit.

### Class O2 — bounded replay-safe intent

Allowed only when the owning command contract explicitly declares replay safety, idempotency, expected-version handling, and status lookup. The client queues intent, not result.

### Class O3 — online-required governed command

Examples: approve/deny/modify proposal, spend shared Resource, transfer ownership, publish, reveal, destructive mutation, canonical advancement.

Must not be represented as completed offline. The UI may retain a draft/proposed intent for later revalidation.

### Class O4 — prohibited offline authority

Any operation that would fabricate authoritative Event history, permissions, entitlements, ownership, hidden information, or canonical sequence. It is rejected locally and not queued as a canonical command.

## Reconnect algorithm

1. Reauthenticate and refresh effective role/permissions.
2. Resolve current canonical checkpoint/version/sequence.
3. Compare cached projection revision to current authority.
4. Perform status lookup for every ambiguous previously submitted command.
5. Fetch missing authoritative Events/projections before replay decisions.
6. Revalidate each queued O2 intent independently against current version, permissions, targets, Resources, and dependencies.
7. Promote accepted intents only through the normal canonical command path.
8. Route divergent drafts or stale commands to explicit conflict/review state.
9. Remove newly unauthorized cached detail from active projection and semantic/search surfaces.
10. Preserve rejected user-authored drafts where policy permits; never mislabel them canonical.

## Conflict rule

**No silent last-write-wins.**

When local and canonical versions diverge materially, the system must either use a deterministic merge contract explicitly owned by that data type or present a review/conflict workflow. Timestamp recency alone is not authority.

## Hidden-information rule

Offline cache never expands what a user can see. After reconnect or role change, authorization is re-evaluated before display, search, autocomplete, export, AI context, graph layout, map fit, counts, or command availability. Previously cached privileged data must not remain visible after revocation.

## Provenance and audit

Every replayed or recovered intent must retain, as applicable:

- stable client operation ID;
- draft/intent ID;
- actor identity;
- originating device/session;
- local creation time;
- reconnect submission time;
- expected canonical version;
- authoritative acceptance/rejection receipt;
- owning-domain Event IDs;
- conflict/revalidation result;
- migration or compatibility receipt for opaque deferred data.

Local timestamps do not establish canonical order.

## Accessibility

Offline and reconnect states must be available through text labels, screen-reader semantics, keyboard, touch, controller where supported, and nonvisual alternatives. Color, animation, iconography, or network-indicator shape cannot be the sole carrier of stale/queued/conflicted status.

## Data preservation for future offline expansion

Unsupported future offline metadata may be retained as opaque, versioned extension data when safe. The current client must not execute unknown processors or silently discard payloads. Future support must use capability negotiation, versioned migrations, explicit receipts, and compatibility reporting.

## Implementation slices

- **OFF-S01 — Offline capability registry:** command/data classification O0–O4 and owning-domain policy.
- **OFF-S02 — Draft persistence:** stable draft IDs, provenance, encryption/storage policy seam, cleanup, export/recovery.
- **OFF-S03 — Queued-intent envelope:** idempotency, expected version, replay policy, dependency references.
- **OFF-S04 — Reconnect reconciliation:** authentication, status lookup, Event-gap recovery, reauthorization, conflict routing.
- **OFF-S05 — Cache/visibility invalidation:** stale projections, role revocation, search/autocomplete/AI-context filtering.
- **OFF-S06 — Deferred-data preservation:** opaque extension namespaces, compatibility reports, migration receipts.
- **OFF-S07 — Accessibility and observability:** state semantics, failure diagnostics, privacy-safe telemetry.
- **OFF-S08 — Fixtures and handoff:** deterministic matrix, validator, traceability, IA-D08-005 integration boundary.

## Internal-alpha acceptance boundary

Internal alpha is allowed to require an active authoritative service for governed multiplayer/canonical mutation. Limited offline-safe behavior exists to protect user work and recover from interruption, not to provide a second authority plane.

No feature may claim “offline support” merely because it caches screens. The exact offline class and limitations must be exposed by its contract.

## Decision

IA-D08-004 defines an implementation-ready broad-offline deferral boundary. The next design item is **IA-D08-005 — optional and experimental isolation review**. `P9-06-008-attempt-002` remains unfinished, paused, and unmodified.
