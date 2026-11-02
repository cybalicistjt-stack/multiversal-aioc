# Reproduce GATE-PREP testbed

These are nonproduction tests with synthetic subjects, snapshots, packages, and scopes.

Node: node --test tests/gate_prep/*.test.mjs

PostgreSQL: set SA_BILL05_TEST_DATABASE_URL to an EXPLICIT LOOPBACK TEST database, install psycopg 3, then run python tests/gate_prep/test_pg_allowance_race.py. THIS TRUNCATES THE EXISTING SA-BILL FIXTURE TABLES. Never connect to Render or production.

PG race = 100 competing requests with 24 max concurrent workers, not 100 simultaneous sessions. Fake-provider verified field is a fixture assumption. Real Node crypto is not an OS key guarantee; the UI model does not charge or launch.

See governance/application-planning/gate-preintegration/GATE_PREP_PROGRAM.md for strict boundaries.
