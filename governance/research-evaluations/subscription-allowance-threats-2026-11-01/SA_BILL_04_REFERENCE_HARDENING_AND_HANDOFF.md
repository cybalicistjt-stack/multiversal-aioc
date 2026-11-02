# SA-BILL-04 — Hardened Entitlement Reference and Adversarial Authorization Gate

**Status:** research-only executable design. **Date:** 2026-11-01. **No commercial, entitlement, billing provider or app implementation authority added.** Source: SA-BILL-01, 02, 03 study; current AIOC `operations/CURRENT.json` remains the only selector.

## 1. New executable reference

- `tests/control_plane/sa_bill04_reference.mjs` models fail-closed timestamp parsing, subscription-term/grace decisions, source-versioned dependency closure, current GM/Player/Campaign authorization, grant epoch and rights checks.
- `tests/control_plane/test_sa_bill04_reference.mjs` runs 15 cases including **1,200 reproducible denial variations**. The suite is included in **exact-head Operations V5**; neither a passing source test nor a caller-provided `origin:'verified-billing-ledger'` field cryptographically proves a payment or a server authorization decision.
- Previous source characterization: `tests/control_plane/test_sa_bill03_app_evaluator.mjs`, pinned actual app evaluator Git blob `11e9a377a2231dc4c8305df36a299aca37b36de9`. Its tests pass by observing currently **incorrect/incomplete** behavior; they are NOT a passing product-security acceptance suite.
- App production source is **unchanged**. A separate owner-authorized application tranche must port and independently verify any fix; the study file cannot be wired directly to production.

## 2. Security behavior and design choices

| Obligation | Reference decision | Production proof still required |
|---|---|---|
| Expiry times with `Z` or explicit offsets | Compare validated *instants*; reject invalid, naive, calendrically impossible or bad-offset times | Actual app evaluator port, server-controlled clock and monotonic subscription source revisions |
| Cancellation requested, paid interval unexpired | Continue already-provider-verified paid access until `entitledUntil`; do not charge additional renewals locally | Provider sandbox status, refund and cancellation flow; actual app behavior |
| Grace after paid interval | Only when provider confirms a separately bounded grace expiry; existing protected reads may continue; **no new GM grants** in proposed conservative policy | Owner final grace-grant rule; actual provider period and revocation |
| Account hold, expired, refunded, malformed source | Deny new premium and protected use | Payment provider and ledger reconciliation; direct API negative tests |
| GM-sponsored allowance | One owner-registered root with trusted recursive dependencies; no unrelated root bundling | Live A3 GM/Player membership and authoritative one-slot database unique index/transaction |
| Restricted content | Reject other Campaign/subject, source version/rights changes, expired issuer, revoked epoch; deny export, copy, publication, dependent Character transfer | Real asset/object/Character import-export, search, AI, backup, direct endpoints |
| Offline premium | No mutation; protected read requires a separately verified cryptographic lease, not implemented here | Native Windows/Android keystore isolation, clock rollback, disconnected revoke TTL |
| Pure eligibility | Returns `ELIGIBLE_FOR_ATOMIC_OWNER_TRANSACTION_ONLY`; never mints or reserves grant | Real PostgreSQL SERIALIZABLE, unique slot, idempotency and audit rollback |

**Policy holds (NOT adopted):** trial allowance issuance, new issuance in provider grace, a post-lapse allowance's suspension versus irrevocable cancel, replacement/retargeting, succession to another GM, safe export details for user-authored content, max dependency size (the 256 cap is illustrative), verified offline lease duration, price, currency, SKU, taxes, refund timing, optional paid AI. The proof does **not** authorize charges.

## 3. Important defects uncovered while strengthening the reference

A first reference implementation erroneously required `now < paid_term_end` for *all* states. That would deny a verified grace period even when the provider explicitly extends entitlement past the original paid end. This was detected in local testing, repaired by treating grace as an independently verified bounded interval `[paid_end, grace_end)`, and rerun. A provider's actual semantics must still determine the allowed grace window. Keeping this negative case protects the future application implementation from recreating that error.

**Purchase ownership warning:** `(provider,event_id)` deduplication alone cannot prevent reassigning one original purchase to different subjects with separate events. SA-BILL-03 added a distinct `(provider,purchase_origin_id)` purchase-binding PK and a foreign key to event records. That DDL is a reference, **not applied on PostgreSQL**.

**Source-authentication warning:** A pure policy function with an `origin` string or `verified_by_provider=true` bool is forgeable when called with client input. The real adapter must be behind the authoritative trusted backend; demand cryptographic provider source verification, canonical purchase subject binding and A3 identity/session binding. Any direct API accepting these flags as proof is a security failure.

**Distributed revocation:** an isolated PostgreSQL transaction does not atomically fence provider or external A3 state that has not yet propagated. Need owner-published revision events, bounded freshness for entitlement-source reads, fail-closed on unknown revisions, and strict epoch checking on every protected mutation and projection. Do not claim instant erasure of disconnected decryptable content.

## 4. Validation and release ladder

1. **Source:** preserve SA-BILL-03 red-characterization fixtures and add fixed-behavior app tests (they must fail on old evaluator and pass on repair) plus privilege escalation/race regressions; avoid modifying current app source without selected authority.
2. **SQL:** apply *reviewed* DDL to a disposable PostgreSQL instance under a future approved test scope. Confirm `UNIQUE(campaign,player,slot_kind)`, purchase binding, 100 simultaneous multi-process operations, rollback when audit insertion fails, stale GM revocation, repeat request IDs, digest mismatch and SERIALIZABLE retries. SQLite results remain SQLite-only evidence.
3. **External authority:** sign/verify sandbox provider notifications then fetch the current provider purchase state; A3 real GM/Player sessions and A5 Campaign scope; measure revocation latency and invalidate derived decisions.
4. **Cross-surface:** actual direct REST, pack downloader, graph/search/counts/facets, WSS, Character transfer, import/export, AI context, offline caches and device keystore. Detect restricted bytes as well as rendered UI.
5. **Approval:** owner product decisions and privacy/storefront compliance, followed by separate activation authority. No study gate can activate live payments.

## 5. Reportable evidence

**Executed proof** (only when exact-head workflow job is green): 15 reference tests, normalized offset/invalid time handling, cancellation/grace reference behavior, source lineage and scope negative cases, 1,200 seeded adversarial variations.

**Not proven:** deployed subscription service, real payment signatures or purchase ownership, real PostgreSQL, multi-process transaction race, fully-disconnected remote erase, installed Android/Windows encryption, 60 end-to-end hostile scenarios, safe active production billing.

**Operations guard:** no change to `operations/CURRENT.json`, GPR PCV-03F, MTLC-14, AXI-01, current Core26 canon or published prices; publication uses OPS5 exact-head PR and shared FIFO queue.