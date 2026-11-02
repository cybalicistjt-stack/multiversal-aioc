# SA-BILL-05 — Isolated PostgreSQL Transactional Boundary Study

**Scope:** research and executable database fixture; not a product migration or commercial entitlement activation. **Date:** 2026-11-01. Continues SA-BILL-01 through SA-BILL-04 without modifying product code or active OPS5 lane selectors.

## 1. What is actually exercised

The workflow `.github/workflows/validate-sa-bill05-postgres.yml` provisions a disposable PostgreSQL 16 service within GitHub Actions on a synthetic local-only dataset and executes `tests/control_plane/test_sa_bill05_postgres.py` using psycopg 3. This is **not SQLite** and not a mocked in-memory mutex. It uses SA-BILL-03's proposed DDL, PostgreSQL `SERIALIZABLE` transactions, row-lock reads, a durable `PRIMARY KEY(campaign_id,player_subject_id,slot_kind)`, command receipts, an immutable event log and a distinct canonical purchase-to-account binding key.

If the workflow cannot provision the Docker service or driver, report **infrastructure/proof unavailable** rather than changing product authority, inventing a result or claiming a passing PostgreSQL test.

### Ten hostile fixture cases (code is the independent oracle)

| Case | Boundary and expected observation |
|---|---|
| PG-01 | 40 separate PostgreSQL connections issue different grants for the same Campaign/Player. Exactly one issued row, one receipt, one event; 39 slot conflicts, with bounded retries on SQLSTATE `40001`/deadlocks |
| PG-02 | Same command ID and identical digest returns an idempotent status; same ID with changed payload fails without extra state |
| PG-03 | Event insertion violating CHECK fails the entire transaction; no partial allowance, receipt or event |
| PG-04 | Deactivated recipient membership blocks issuance |
| PG-05 | Same Player across two Campaigns and two Players in one Campaign get separate independent slots, not one global slot |
| PG-06 | A provider purchase origin cannot bind to two canonical payer subjects even if event IDs differ |
| PG-07 | Duplicate provider event IDs cannot append duplicate financial ledger effects |
| PG-08 | A direct duplicate slot `INSERT` (bypassing the service's `ON CONFLICT`) raises PostgreSQL uniqueness violation |
| PG-09 | Inactive registered root / rights revision blocks issuance |
| PG-10 | GM subscription expires (monotonically advanced provider revision); newly issued allowance is denied |

**Note:** the test case IDs above describe intended coverage; the source test methods run in lexicographic order. A green workflow is the evidence that the specific named cases executed.

## 2. Exact read/transaction assumptions

1. All command inputs are synthetic. A3 actor/session and provider purchase verification are **seeded fixture facts**, not evidence of a deployed trust boundary. SQL reads membership, bill source, and registered release rows inside one transaction; the client does not supply trust booleans.
2. Subscription status is checked from the test database at command time. No out-of-db provider or A3 source participates atomically. The `provider_checked_at` freshness heuristic is demonstrative (one hour), **not** a selected production lease duration or sufficient external owner revocation fence.
3. Issuance does not modify a user's subscription or bill a method of payment. A valid request writes one allowance slot, one command receipt and one event in the same durable transaction.
4. There is no selected allowance replacement or owner succession rule. The durable slot is never deleted to make a new grant; revocation or retargeting policy remains owner-held.
5. Role and rights inputs are illustrative local projections. An installed live A3/GM or content source must provide versioned current state and independent authorization before this structure could become application code.
6. SQLSTATE conflict retries are bounded. An ambiguous network commit requires status lookup by stable command ID before retry; this fixture does not claim to simulate a remote network partition.

## 3. Why this is materially stronger but still insufficient

Earlier SA-BILL-02 used SQLite transaction tests and SA-BILL-04 used a pure decision model. This tranche runs the proposed relational schema on PostgreSQL with concurrent distinct connections, real unique constraints, commit/rollback enforcement, foreign keys and source-state reads. It establishes **transactional fixture behavior**, not full application security.

Remaining P0 blockers: genuine A3 stable subject and verified GM/Player role revision; payment provider-signed receipt/purchase status and cross-account ownership; remote revocation fencing; materialized trusted dependency-graph digest and rights/lineage in every Character/Setting/Species/item; direct server APIs and WSS/search/AI/export negative tests; physical Android/Windows offline encrypted-content and clock manipulation; full 60-case independent adversarial acceptance.

## 4. Research-to-implementation handoff

The selected GPR/PCV-03F service-first path and owner source contracts remain the controlling system architecture. A future owner-selected, product-authorized tranche should:
- Introduce a canonical allowance owner service/port with `(Campaign, PlayerSubject, slotKind)` unique transactional row and a stable idempotency ledger. Keep producer-specific original purchase identity and account binding separate from provider event deduplication.
- Derive premium issuance authority from current server-verified GM subscription **and** A3 Campaign GM role/Player membership, registered immutable root version/dependency closure, user-safe policy decisions and source rights.
- Compute action-specific entitlement/rights and provenance checks at every actual protected endpoint and derivative export; deny unauthorized transfer even where a separate personal paid subscription exists.
- Use a provably current provider/role epoch and deny protected mutations on unavailable external owner truth. Do not assume that two service databases can share one PostgreSQL transaction.
- Build a realistic negative-control test that removes uniqueness, skips current GM role revision, or bypasses a dependency taint and proves the corresponding real-boundary test fails.
- Require explicit owner policy on trial/grace issuance, retarget/reissue, GM succession, refund adjudication, offline lease expiration and final SKU/pricing before production billing code.

**Operational invariant:** Research cannot self-select product implementation, grant billing or pricing authority, alter `operations/CURRENT.json`, or modify GPR PCV-03F, MTLC-14, AXI-01, content canon or release state. Source/fixture tests cannot be presented as live store or installed-device proof.
