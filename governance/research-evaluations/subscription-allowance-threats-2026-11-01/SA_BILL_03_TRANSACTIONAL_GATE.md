# SA-BILL-03 — Source parity, transactional issuance and provenance gate

**Classification:** security research extension to published SA-BILL-01 and portable SA-BILL-02. **Not** a selected product implementation, payment activation, live billing service or approved new subscription policy.

## 1. Reproducing the actual application evaluator

Pinned verbatim application file: `Multiversal-app/packages/contracts/src/identity-device/entitlement-evaluator.ts`; application `main` `db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f`, Git blob `11e9a377a2231dc4c8305df36a299aca37b36de9`. Mirror is `tests/fixtures/sa-bill-03/entitlement-evaluator.ts`, pinned by blob hash in `tests/control_plane/test_sa_bill03_app_evaluator.mjs`. **Do not** confuse this with a test of a live service or future app heads.

Exact implementation-specific observations (characterization tests explicitly assert the **undesired** existing behavior):

| Finding | Existing source behavior | Correct design / blocking gate |
|---|---|---|
| SA03-02 | Mixed timezone offset expiry remains eligible after its actual UTC expiration | Parse valid timezone-aware instants and compare epochs; reject malformed windows, evaluate with trusted server time |
| SA03-03 | `status:cancelled` loses access immediately even while paid interval is current | Separate `autoRenew` from provider-confirmed `entitledUntil`; preserve paid term subject to verified refund/revoke |
| SA03-04 | Sponsored month with Campaign X counts as subscriber when requesting no Campaign | Disambiguate global sponsored month from GM's Campaign allowance; no unintended premium bleed. Policy remains unresolved |
| SA03-05 | Campaign premium grant only has a subject, Campaign, grant ID and dates | Introduce issuer, root, dependency digest, slot and verified owner authority as distinct source records |
| SA03-07 | Nonsense expiry string can be treated as future because of lexical comparison | Reject invalid provider/ledger timestamps, no implicit infinite entitlement |
| SA03-08 | Repeated source grant IDs appear multiple times in returned active IDs | Service-side unique source keys, idempotent writes and precise decision provenance |
| SA03-09 | `nextChangeAt` selects lexicographically earliest timestamp, not earliest UTC instant | Normalize all transition instants and choose minimum UTC expiration/revision boundary |
| SA03-10 | Multiple Campaign grants can be evaluated in the same Campaign/subject | Real atomic single allowance slot; distinguish any existing *other* grant sources and sponsored months |

The tests also check legitimate free/subscribed baseline and cross-Campaign/subject denial already present in this evaluator. Passing characterization tests **document the defects rather than certify them fixed**.

## 2. Explicit counterexample

```
startsAt    = 2026-10-31T00:00:00Z
endsAt      = 2026-11-01T00:00:00+02:00  = 2026-10-31T22:00:00Z
evaluatedAt = 2026-10-31T23:00:00Z
```

Thus evaluatedAt is **one hour past expiry**, while JS lexical comparison `"2026-10-31T23:00:00Z" < "2026-11-01T00:00:00+02:00"` is true. This is a source-level behavior gap, not a demonstrated production attacker exploit.

## 3. Provider money ledger vs entitlement decision

The payment processor/store owns **payment truth**; the trusted billing adapter verifies purchase status, product, app/environment, purchaser binding, provider effective interval, refund, trial, grace/hold and revision. The application owner database persists only verified derived billing state, unique provider event/source IDs and stable A3 purchaser subject. Nonblocking asynchronous webhooks are signals: on event, fetch the provider's latest source of truth, ignore stale/misordered events and keep an auditable append-only state log.

A verified subscription may grant independently approved paid product capability, but it **does not** grant GM status, a registered content license, Character ownership, transfers, or additional Campaign slots. A nonrenewal event does **not** by itself imply premium access ends immediately. A refund/revocation may end entitlement earlier, only based on provider and plan policy.

**Unknown owner decisions:** trial GM grants, grace-period *new* issuance, owner change on existing GM-issued grants, refund appeals, allowance retargeting and maximum offline lease. Freeze those decision edges, retain historical author-owned data and avoid invented policy.

## 4. Transactional allowance owner — proposed PostgreSQL design

See `SA_BILL_03_POSTGRESQL_REFERENCE.sql`. This is **schema sketch for code review**, not a migration to apply to a production database. It uses a persistent unique tuple `(campaign_id,player_subject_id,slot_kind)`, immutable command/event ledger, provider-verified GM subscription row, current Campaign GM/Player membership and registered source release. All authority inputs are fetched *inside* a single `SERIALIZABLE` transaction with row-version expectations, not accepted as client booleans.

For issuance, require issuer and recipient active in the same Campaign, issuer current GM and provider-entitled subscriber, registered and allowed root/version, trusted dependency closure digest and source-rights permission. Acquire locks in canonical order, perform immutable idempotency lookup and payload digest comparison, insert or conflict at the one-slot unique key, then append event and increment epoch in the same DB transaction. Identical request ID + identical digest is idempotent; same ID + changed payload is rejected. Concurrent different request IDs cannot both create active grants, regardless of number of service replicas.

**Important limit:** `SERIALIZABLE` is not magic cross-service atomicity. If the payment provider or managed A3 service revokes permissions before its updated canonical revision has reached this database, the transaction may use temporarily stale source data. A correct implementation needs verified source freshness, bounded staleness, revision fencing and fail-closed handling of unavailable external owner truth. A post-commit revoke must increment the entitlement/role epoch and invalidate derived decisions. An external A3 source requires a real adapter, not a second shadow authority.

## 5. Every protected use re-evaluates *both* rights and scope

A Campaign allowance gives a **single registered root with trusted dependencies** only to the recipient in that Campaign, while the current issuer/recipient roles, subscription and source release remain valid. It never changes self-paid tier, moves ownership to recipient, confers transfer or installs an unrelated premium release. Derived Characters, ability choices, items, graphics, exports, offline caches and AI snippets carry the dependency lineage. A Character with restricted content cannot simply be exported/transferred to another Campaign. A safely redacted self-authored base may be recoverable if separate source-owner rights permit.

Permission protection occurs in canonical owner queries and all derived surfaces: UI, direct REST/command, indexed search, counts/facets, realtime/WSS, vector retrieval, exports/backup, AI prompts, notifications, diagnostics and temporary/signed asset URLs. Declaring a role or premium flag on the client is never owner authorization.

## 6. Adversarial gate and proof ladder

| Proof | Status of this study | Proof still needed |
|---|---|---|
| Exact app evaluator source behavioral characterization | Script committed against a pinned unmodified app blob; CI results should be read separately | Confirm current app main has not drifted, and retest after proposed source repair |
| SA-BILL-02 portable replay | Local archive has recorded 23/23 Python/SQLite fixture tests; archive isn't repository CI | Real managed backend, provider and device evidence |
| Proposed PostgreSQL owner DDL | Static contract, **not executed** | Real disposable Postgres schema, 100 simultaneous `SERIALIZABLE` transactions, GM downgrade race, aborted audit rollback |
| External provider billing state | Reference normalization only | Provider sandbox receipts, verified signatures, out-of-order RTDN/webhook, refunds, plan changes, store route validation |
| Source owner A3/A4/A5/Content | Existing contracts studied only | Live current session, GM permission/Player membership, content-release owner epoch and measured revocation propagation |
| Windows and Android offline | No additional real-device test | Keystore binding, clock rollback, copied cache, encrypted pack revoke + exports |
| Consumer payment approval | Explicitly absent | Owner's SKU/tier/price/consent decisions and separate production/store compliance gate |

**Do not** change `operations/CURRENT.json`, PCV-03F, MTLC-14, AXI-01, game canon or live billing to publish this research. Even after a source-level fix, no source-only test may be promoted to paid release readiness.
