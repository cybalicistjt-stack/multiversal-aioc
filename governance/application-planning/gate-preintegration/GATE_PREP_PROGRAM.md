# GATE-PREP — Isolated preintegration engineering

Owner approved four packages on 2026-11-02. This reuses the GATE on-demand slot, not a fourth persistent implementation lane. Stage A GATE-01–08 is already completed and remains so in its separate backlog.

## Program packages and executable tests

- PREP-01: real disposable PostgreSQL 16 race/uniqueness test that reuses the preexisting SA-BILL05 synthetic schema and source command. 100 competing attempts with at most 24 simultaneous DB workers; does not certify 100 simultaneous clients or real PCV account/Session service.
- PREP-02: fake-provider billing reconciler and Node unit tests. Tested snapshot booleans do not verify actual Stripe signatures, merchant events or purchases.
- PREP-03: Node builtin Ed25519 signing and AES-256-GCM encryption experiment and restricted lineage decision tests. Not Windows DPAPI/Android Keystore or deployed DRM.
- PREP-04: state-only subscription UX, consent and management-routing checks, and support reconciliation/incident tabletops. No product user interface or charges.

## Execute

Node tests: node --test tests/gate_prep/*.test.mjs
Real disposable PostgreSQL: SA_BILL05_TEST_DATABASE_URL=postgresql://test@localhost:5432/test python tests/gate_prep/test_pg_allowance_race.py. WARNING: this inherits a destructive synthetic fixture initializer. Never point at Render or production.
Isolated CI workflow: .github/workflows/validate-gate-prep.yml uses a synthetic PostgreSQL service. Exact-head OPS5 source validation and publication queue still required.

## Explicit stop lines

No production application changes, A3/A5/PCV Session or installed Windows/Android implementation, merchant/Stripe credentials, money, published SKU, payment provider activation, deployment, store enrollment or new legal terms.
Passing isolated tests cannot certify GATE-09 backend, GATE-10 real provider, GATE-11 installed clients or GATE-12 independent security. The historical $4.99 figure is not an adopted retail price.
GATE09 owner selection remains separate; PCV03F identity and service boundary is not yet verified. GATE Stage A remains completed in its own canon.
**Completed isolated proof:** PR1961 head 9701f8aa3ffd5ce7fad0d3c71ebbda379eb7e26f, Node/real disposable PostgreSQL test run41521141211 success (11 Node tests and PG16 100 competing/24 workers), OPS5 run41521141144 success, merge 0e534b0a, publication queue428. Full 100 simultaneous DB sessions, A3 production identity, installed native devices and real Stripe remain NOT_RUN. Stage A GATE01–08 remains completed; GATE09 planned, not authorized.
