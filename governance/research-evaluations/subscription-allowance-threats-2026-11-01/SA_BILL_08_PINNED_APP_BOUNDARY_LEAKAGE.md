# SA-BILL-08 — Pinned Application Authorization Boundary and Protected-Content Leakage Study

**Classification:** source-backed research, not production mitigation or proof of live exploit. **Scope:** actual Multiversal-app lower-level TypeScript contracts + synthetic owner gateway with isolated adversarial fixtures. Date: 2026-11-01–02.

## Exact application-source pins

Verbatim source from `cybalicistjt-stack/Multiversal-app` main after AXI-19 app publication:

| Source path | Pinned Git blob | Role |
|---|---|---|
| `packages/contracts/src/authorization/campaign-authorization-policy.ts` | `b7b038b63774b7e4e8c1deb72c9ed09d35bc48b6` | Core Campaign role authorization |
| `packages/contracts/src/session/hidden-information-response-filter.ts` | `d948d92c06560fb9a560fcf4325ba4a258216e2a` | Generic and A9-safe hidden event projections |
| `packages/contracts/src/session/authoritative-session-command-handler.ts` | `8b0ec123e99ccbbfc00fdc0c4e1e38aa42c71656` | Generic session commands, idempotent receipt replay, A9-safe result projection |

Pinned verbatim copies are in `tests/fixtures/sa-bill08/app-src/`. Before tests run, their Git-style blob SHA-1 values are verified. Node's TypeScript strip loader requires extension-bearing relative imports, so the test creates throwaway copies and **rewrites only the relative import specifier**; it never changes the pinned original. This validates these historical source versions, **not** all future app heads or live server deployment.

## Observed actual-source authorization concerns

1. **SA08-AS01 — hidden cardinality at lower-level projection**: `filterSessionEventsForViewer` includes `hiddenEventCount: events.length - visibleEvents.length` for an otherwise authorized viewer. This is a **metadata side channel if that generic result is published to an unentitled Player**. The same source explicitly wraps this for A9 via `filterSessionEventsForA9`, which removes the count. Thus it is a **call-site contract hazard**, not proof A9 leaks.
2. **SA08-AS02 — public command-event payload**: `handleAuthoritativeSessionCommand` constructs a `visibility.kind: 'public'` event retaining the entire `command.payload`. If a caller puts protected data in that payload and exposes the lower-level event unfiltered, it can disclose content. The existing `projectAcceptedSessionCommandForA9` strips those bytes for A9 projection. The test characterizes both results without claiming a production leak.
3. **SA08-AS03 — replay before fresh authorization**: In `handleAuthoritativeSessionCommand`, a processed command with a supplied `existingReceipt` returns `accepted:true,replayed:true` **before** the `authorizeCampaignRequest` branch. The test demonstrates this with an actor lacking Campaign membership. A real authoritative endpoint must bind the original command, actor and receipt, recheck current authorization before returning replayed results and never trust a caller-supplied receipt. No deployed exploit is asserted.
4. **SA08-AS04 — role does not equal purchase rights**: the app `campaign-authorization-policy.ts` handles roles and Campaign actions; it does not validate subscribed GM or registered rights on sponsored content. This is a legitimate layered architecture, but every protected caller must **combine** canonical A3 membership, provider-entitled GM, one-slot allowance, registered source closure, and action-specific rights. A returned role alone must not be treated as premium content entitlement.

## Synthetic surface integration and test semantics

`tests/control_plane/sa_bill08_boundary_gateway.mjs` is a deliberately isolated model of **REST-like direct read, search/results/count, AI context, WSS-like event polling, transfer/export refusal, authored raw-note recovery and command-replay gating**.

These are **not actual deployed REST handlers, search indexes, WSS, AI retrieval, application data stores or endpoint security tests**. They consume fake canonical subject tokens and mutable fake owner records, invoke SA-BILL-04's reference entitlement decision, and follow a mock dependency graph. The only actual application code executed by the same test file is the pinned source subset above.

`tests/control_plane/test_sa_bill08_app_boundary.mjs` adds **21 executable cases** including 700 seeded hostile variations. Expected proof:
- Valid Campaign access to a sponsored Character is allowed; unrelated root and other Player/other Campaign are not.
- GM role loss, Player removal, refund and grant-epoch change deny fresh direct/search/count/AI/WSS reads.
- Nested unauthorized Species/item/tree, mixed-Campaign object, cycles and source version changes invalidate derived Character projections; unauthorized object IDs do not change safe error shape.
- Transfer, restricted Character export and protected asset download are denied in the mock gateway even when the user has a separate account; originals are not automatically globally owned.
- Separate independently user-authored note recovery remains possible when premium projections lapse, subject to source ownership validation.
- No front-end `gmSubscriptionActive` boolean grants authority.
- Replay is denied by the synthetic outer gateway **before** calling the vulnerable source-level idempotency branch when current Campaign permission is missing.
- The generic app event projection's hidden count and generic accepted session command's public payload are characterized, alongside the A9-safe wrappers.

## Known proof gaps / mandatory future gates

- **Live A3 and A5:** actual authenticated service-owner subject, Campaign membership and role revision, trusted bound receipts, session-store replay, protected content rights, grants and revocation events.
- **Actual endpoints:** direct HTTPS/REST/command, Rules/Lore search/count/vector index, AI retrieval/context, realtime WSS, object store/CDN signed download, export/import/backup, diagnostics and error shape. Every byte including metadata/citation references must be tested.
- **Security enforcement at database boundary:** least-privileged real service accounts, RLS and SQL role denial, not only trusted SQL functions and mocked surface adapters.
- **Race/security:** requests started before revoke, stale caches and session ownership, disconnected offline Android/Windows; durable epoch fencing and bounded read leases.
- **Rights:** actual registered premium root dependency closure and Character/source provenance. A mock dependency array is not a production owner graph.
- **Provider authenticity:** synthetic billing records do not prove Google Play or any actual payment processor.
- **Owner product decisions:** subscription price, trial/grace issuance, GM succession, replacement and offline lease remain unapproved.

## Publication rules

This study does not change `operations/CURRENT.json`, GPR PCV-03F, MTLC-14, AXI-01, Multiversal-app source, payment processing, prices or live grants. The **60 original real-boundary SA-BILL-01 adversarial cases remain unexecuted** even if this research simulation passes. Any local red-green evidence must be linked to exact immutable commits and CI logs. Publish only after exact-head Operations V5 plus OPS5 FIFO protected-main gate.
