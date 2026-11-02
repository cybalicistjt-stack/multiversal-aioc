# SA-BILL-07 — Cross-Authority Revocation and Derived-Content Provenance

**Status:** executable **synthetic A3/GM/source-rights PostgreSQL research**; not application implementation, security certification, or owner approval of unresolved commercial policy. Date: 2026-11-01 (America/Chicago).

## Authority and source limits

This tranche continues SA-BILL-01 through SA-BILL-06, including SA-BILL-05's verified PostgreSQL uniqueness/rollback fixtures and SA-BILL-06's synthetic-provider notification reconciliation. The actual application `packages/contracts/src/authorization/campaign-authorization-policy.ts` recognizes owner, GM, Player, observer roles, and the A3 `packages/contracts/src/a3/context-authority.ts` models stable subject, selected contextual role, permissions version and cache partition. Neither contract alone proves subscription-funded allowance issuance or provenance-safe transfer. **A3 owner records and real A5 Session data are not used in these new tests.**

The approved owner allowance still means **one Campaign allowance per Player-user**, issued by a current eligible subscribed GM. One root can grant one custom Setting and trusted dependencies or one eligible Species, item set or Ability tree; it grants no ownership, unrelated root or cross-Campaign Character/object transfers.

**Unresolved owner decisions remain unresolved:** period/grace issuance, replacement/retargeting, GM succession, terminal revoke versus suspend, offline protected read lease, price, SKU and refunds. The SQL deliberately fails closed on `grace_entitled` without converting that research assumption into final product policy.

## Real database fixture (NOT the deployed app)

- `SA_BILL_07_DISPOSABLE_SCOPE_SCHEMA.sql` creates seven table types for synthetic A3 role revisions, synthetic paid issuer state, content-owner registered releases and closure, Campaign one-slot allowance, resources and nested dependency edges.
- `tests/control_plane/test_sa_bill07_revocation_provenance.py` is **24 PostgreSQL 16 tests** against that schema, using actual SQL queries and local transactions.
- The SQL `protected_use_authorized` policy is a deliberately visible, **test-only SQL function**. A real backend must authenticate subject/session separately and prevent direct table bypass with least-privilege roles, appropriate RLS/security-definer review, protected asset delivery, endpoint-level checks, event filtering, and trusted source revisions.
- The `safe_protected_projection` function represents only a testable filtered database projection. It is **not** a real search/AI/WSS/index/export implementation. The tests show that calls to *that projection* deny after revocation, not that production search, AI or websockets do.

## Negative gates

| Scenario family | Expected test oracle |
|---|---|
| Current GM and Player with a valid sponsored Setting -> Item -> Tree | In-Campaign protected Character projection allowed |
| GM removed/demoted, Player removed, GM provider subscription revoked or source revision changed | No new protected projections; historical Campaign slot retained |
| Grant suspended, expired source verification, stale grant epoch or rights/canon version changed | Deny premium reads and uses |
| Unrelated premium branch smuggled into nested resource graph | Deny whole derived Character, not just top-level item |
| A dependency belongs to another Campaign or forms a graph cycle | Deny rather than ignore descendant or recurse forever |
| Player B requests Player A's Character, or Player A requests in Campaign Y | Deny; separate paid/free entitlement does not erase provenance |
| Export, transfer, publication, external download | Deny; allowed Campaign reads do not imply portable rights |
| Search/count, AI and realtime projection through the *same fixture policy* | Zero protected rows after revocation; raw endpoint integration remains untested |
| Premium rights lapse and a separate Player-authored biography remains | Protect restricted payload; retain explicitly owned raw note without granting protected dependency |
| 40 new Postgres connections after GM revocation commit | All new policy decisions deny (does not establish zero in-flight leakage) |

### Source-owner boundaries and race limitations

1. The fixture stores role and subscription flags in its own tables. It **cannot** establish that a canonical external A3 provider or a payment provider issued those facts; the service-side source adapter and freshness/fencing events are missing.
2. The fixture stores closure rows derived from an assumed registered source graph. A production engine must prove exact release versions, dependencies, rights and migrations from the relevant content owner, not take user-supplied edges.
3. The `issuer_entitlement.checked_at` one-hour freshness rule is a **fixture heuristic**, not an approved real offline lease or acceptable production staleness.
4. A fresh query after a committed revoke is denied; an already-started SQL snapshot or a fully disconnected device may still have previously received bytes. Requires measured in-flight request fencing, WSS/cache invalidation, short bounded leases, and object-store access-token controls.
5. Actual product SQL may be PostgreSQL, but these tests use a **separate synthetic schema**. No migrations against the deployed product database or services were made.
6. User-authored data recovery is limited to the isolated raw note column; do not infer that every authored export is legally permitted or safe from licensed dependency taint.

## Concrete application integration gates (NOT completed)

- **Real A3 and A5:** verify current stable subject, subscribed GM's scoped authority, Player membership and versioned role revocation, including denial of cross-device stale sessions.
- **Real provider:** use legitimate vendor API/status, purchase binding and verified entitlement period; no fake `source_verified` or signature string from clients.
- **Real registered content:** issue a single root with trusted rights-aware recursive closure and sticky provenance across Character inventory, species, skills, abilities, derived stats, graphics, exports and imports; forbid inherited grant laundering.
- **Actual endpoints:** independent hostile REST, direct asset URLs, WSS events, index/ranking/counts, vector retrieval, AI context, files, backups and diagnostics; test serialized bytes, not buttons.
- **Installed Windows and Android:** separate installation IDs on a single A3 account, copied encrypted caches, offline stale grant leases, logout, clock rollback, reconnect and revocation.
- **Durability/security:** DB-level least-privilege/RLS tests and 100-cross-process concurrent source revocation/issuance transactions, with retries under changing external owner revisions.
- **Product policy and launch:** all unresolved owner decisions, retail billing disclosures/storefront compliance and explicit activation authority.

**Published proof can only be claimed after the exact-head PostgreSQL + Operations V5 workflows pass and the FIFO protected-main merge is confirmed.** SA-BILL-01's 60 end-to-end hostile scenarios remain NOT EXECUTED; the 24 new tests are synthetic SQL fixtures and do not mark those real-boundary scenarios complete. `operations/CURRENT.json`, PCV-03F, MTLC-14, AXI-01 and live commerce remain untouched.
