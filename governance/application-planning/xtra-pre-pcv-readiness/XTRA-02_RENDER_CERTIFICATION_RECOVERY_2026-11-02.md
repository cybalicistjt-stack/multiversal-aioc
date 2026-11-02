# XTRA-02 — Render PostgreSQL Certification Continuity and Recovery

**Evidence timestamp:** 2026-11-02  
**Result:** EXTERNALLY BLOCKED for actual backup and isolated restore. Read-only inventory and procedure are complete; no backup, PITR, recovery time, data retention or security certification is claimed.  
**Execution authority:** XTRA-02, read-only nonpaid investigation; do not change provider cost, IP networking, credentials, live data or production environments without appropriate authorization.

## Live source observations

- Render resource: `multiversal-pcv03f-certification` (`dpg-db4dbknlot8c738kn0k0-a`); plan `free`, PostgreSQL `17`, region `ohio`, role `primary`, status `available`, no HA, replicas or connection pool. Created `2026-10-09T11:53:54Z` and **expires `2026-11-08T11:53:54Z`**. Verified through the connected Render list and get operations on 2026-11-02. Dashboard: https://dashboard.render.com/d/dpg-db4dbknlot8c738kn0k0-a.
- External IP allowlist is empty. The connected Render read-only SQL action returned an explicit refusal: hosted integration is not allowlistable and cannot reach this database. **No query or dump succeeded.** No data/table counts, source schema, RPO/RTO or actual restore state were observed.
- Connected Render actions expose PostgreSQL inventory and read-only queries but do **not** provide a `pg_dump`, logical backup export, restore or allowlist management operation. No privilege escalation or paid plan was invoked.
- [Render free plan policy](https://render.com/docs/free): 30-day expiry; once expired, free DB inaccessible without upgrade; additional 14-day upgrade grace before deletion; no managed backups. This is not a recovery guarantee.
- [Render Postgres backup and restore documentation](https://render.com/docs/postgresql-backups): free plans have no managed backups/PITR; use **local `pg_dump` while still accessible** or upgrade with separate spending approval. `pg_restore` to an *empty isolated target* verifies a logical backup.
- [Render Postgres connection and IP allowlist documentation](https://render.com/docs/postgresql-creating-connecting): same-region internal service can connect privately; external clients need a currently permitted IP and credentials. An empty allowlist blocks this agent's remote connection.

## Preflight decision tree (no destructive action)

1. **Check whether the certification data are disposable** by the PCV-03F owner: identify migrations, test identities, fixture provenance, current authorized data subjects and any irreplaceable state *without copying records*. Do not infer that a certification database is synthetic or safe to delete by its name.
2. **If data matter and no verified backup exists**, select a human-controlled authorized export route **before 2026-11-08T11:53:54Z**. Prefer a current trusted laptop with PostgreSQL 17 client utilities and an owner-approved temporary narrow **single-IP /32** allowlist for that machine; remove it immediately afterward. Do **not** open `0.0.0.0/0`. If external access must remain disabled, an already-authorized same-region Render application could run a scoped internal export **only if** its actual command/runtime permissions and secure private output path are proven; none was observed here.
3. **If a live export is not possible**, record an unrecoverable-risk/owner decision. A paid compute upgrade is an option under Render policy, but requires explicit authorization and should not be represented as a backup. A new free database from migrations is acceptable only once irreversible data loss is explicitly assessed and accepted.

## Operator-controlled logical export (Linux laptop, PostgreSQL 17 tools)

Never paste credentials, connection URLs, `.pgpass`, database dumps or unredacted query output into ChatGPT, GitHub, PRs, logs or workflow artifacts. Keep the dump outside checked-out repositories. Use a private password store or a separate mode-0600 `PGPASSFILE`. These are instructions **to be executed by an authorized operator**, not commands executed in this session.

1. From the Render database's **Connect** menu, obtain the *external host, port, database and user* privately. Set local session variables `PGHOST`, `PGPORT`, `PGDATABASE`, `PGUSER`, `PGSSLMODE=require` using private values (not a command-line URL containing a password). Arrange noninteractive authentication through a private `PGPASSFILE` with mode `0600`; never commit it.
2. Only with authorization, configure an external allowlist entry for the trusted operator machine's current public IP `/32`; confirm ordinary connection with `psql --no-psqlrc -X -c 'SELECT 1'`, without selecting application rows. If this fails, **stop**; do not widen access blindly.
3. Run the following commands in an empty **private, encrypted local backup directory**, outside the repo:

```bash
set -euo pipefail
umask 077
mkdir -p "$HOME/multiversal-private-backups"
cd "$HOME/multiversal-private-backups"
archive="pcv03f-cert-$(date -u +%Y%m%dT%H%M%SZ).dump"
pg_dump --format=custom --no-owner --no-acl --file "$archive"
test -s "$archive" || { echo 'EMPTY/FAILED backup; STOP' >&2; exit 1; }
pg_restore --list "$archive" > "$archive.toc.private.txt"
sha256sum "$archive" > "$archive.sha256"
sha256sum --check "$archive.sha256"
```

4. Confirm `pg_dump` exit zero, archive size greater than zero, archive SHA-256, and `pg_restore --list` success. **This proves archive structure, not recoverability.** Immediately remove the temporary IP allowlist exception and ensure backups remain encrypted/offsite according to approved retention.

## Isolated restore proof (operator only)

Use an empty local PostgreSQL 17 instance unrelated to the certification database. Clear remote `PGHOST`, `PGPORT`, `PGUSER`, `PGDATABASE` and `PGSSLMODE=require` from the shell first; local authentication and local connection policy apply independently. These commands assume local DB superuser access and a fresh unused name; reject an existing/nonempty target, and NEVER run `pg_restore` against the Render source or any production/important database.

```bash
# Use a separately configured local PostgreSQL 17 connection; not the Render PGHOST.
createdb --host=127.0.0.1 --username=postgres --template=template0 xtra02_restore_check
pg_restore --host=127.0.0.1 --username=postgres \
  --dbname=xtra02_restore_check --exit-on-error --no-owner --no-acl \
  --format=custom "$archive"
psql --host=127.0.0.1 --username=postgres --dbname=xtra02_restore_check \
  -X -v ON_ERROR_STOP=1 -c "SELECT COUNT(*) AS restored_public_tables FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';"
```

Only declare **VERIFIED_RESTORE** after `pg_restore` exit zero, expected schema objects, expected *non-sensitive* table counts or integrity checks, and one harmless app-specific certification smoke test all pass. A restore success from synthetic fixtures does not prove original data preserved. Record a hash, exact dump timestamp, target PG version, elapsed time and tested boundary in a non-sensitive receipt. No record contents in the receipt. If restore fails, preserve the failure and diagnosis; do not destroy the only dump.

## Acceptance / evidence fields

| Field | Current evidence |
| --- | --- |
| Last reachable / expires | Available by Render metadata on 2026-11-02; expires 2026-11-08T11:53:54Z |
| Export file SHA-256 / size / timestamp | **NOT_OBSERVED** |
| Independent restore / integrity | **NOT_RUN** |
| RPO achieved / RTO achieved | **NOT_MEASURED** (BRP targets are not actual SLAs) |
| Data disposition (disposable vs retained) | **UNVERIFIED** |
| Provider backup support on free | **NOT_AVAILABLE** per Render docs |
| External DB access from hosted connector | **BLOCKED**: empty IP allowlist |
| Owner/external action | Choose secure local export authorization, payment/upgrade, or explicit fixture-only data-loss disposition |
| Safety | No provider configuration or data mutation made during XTRA-02 investigation |

## Safe handoff

**Owner action is only necessary for the database data-preservation decision and enabling an authorized export route.** The XTRA program itself need not wait: XTRA-03..11 depend on XTRA-01, not on resolving this independent external prerequisite. Retain XTRA-02 as **blocked_external** until actual backup and isolated-restore proof arrive. Do not close it as verified recovery, and do not erase the blocker during later successor selections.
