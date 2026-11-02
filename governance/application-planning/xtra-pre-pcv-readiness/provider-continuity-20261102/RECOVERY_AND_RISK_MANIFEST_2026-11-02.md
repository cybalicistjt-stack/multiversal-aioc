# XTRA-02: Provider continuity risk preservation — 2026-11-02

**Status: SAFE CONFIGURATION SNAPSHOTS COMMITTED; LIVE DATA BACKUP NOT PERFORMED.**  
**Canonical authority:** `operations/BOOTSTRAP.md` → `operations/CURRENT.json`; existing XTRA-02 remains `blocked_external` until backup/isolated restore proof. This is an evidence appendix, not a new selected work item, CI acceptance, or migration approval.

## Contents and provenance

- `render-inventory.redacted.json`: inventory for ten Render resources (4 web services, 4 static sites, 1 PostgreSQL database, 1 key-value service), including source branches, nonsecret build/start commands, service IDs, plans, location, expiry and provider URLs. Retrieved read-only from the connected Render team workspace **Raven's workspace** on 2026-11-02.
- `railway-inventory.redacted.json`: two Railway projects, five service slots (including one staged-only create), source/deployment configuration, domains, shared/individual environment variable **names** (never values), and pending patch metadata. Retrieved read-only through connected Railway on 2026-11-02.
- `pcv03f_render_backup.sh`: vetted *operator-only* logical PostgreSQL 17 export helper; it does not run on GitHub and contains no secrets.
- `FREE_NO_TRIAL_INFRASTRUCTURE_OPTIONS_2026-11-02.md`: source-linked options and requirements fit for eventual provider migration.

## Exact risk inventory

| Resource | Status / risk | Recovery |
| --- | --- | --- |
| `multiversal-pcv03f-certification` Render PG17 | **P0. Expires 2026-11-08 11:53:54 UTC / 05:53:54 CST.** Free plan; no backups, replicas or HA. DB available at metadata read. Actual records/schema/size **not inspected**. | Secure operator `pg_dump` → independent `pg_restore`; only after that consider external DB migration. |
| `multiversal-pcv03f-session` Render Node web | Latest deploy `dep-dbg6o1psrm7s73cmael0`, commit `a70a5f6cebb6ea520ef45b9a8f7acc61ef8af449`, marked live 2026-10-27. Reads `DATABASE_URL` and fails startup without PostgreSQL. Free service spins down when idle; code in `Multiversal-app`. | Keep durable DB outside ephemeral service. Repoint only after backup/restore, schema/connection tests and reversible cutover. |
| `multiversal-signaling` Render Node | Free web. Code `apps/signaling/server.mjs` has process-memory Maps and TTLs. No durable session guarantee; not the chosen service-first PCV-03F authority. | Source already in application Git; ephemeral state not representable as permanent backup. |
| `multiversal-gatx-remote` Render Python | Free web for synthetic Guided Alpha. Source in app Git. | Rebuild from checked-in code/config if needed; no persisted disk claimed. |
| `playmultiversal-signup-preview` Render web | Free; `work/playmultiversal-v1-site` branch. No independent DB backing confirmed. | Rebuild from app source and documented provider configuration. |
| Four Render static sites | Free; original branch/publication paths preserved. | Rebuild from existing Git source. |
| `multiversal-rendezvous` Render key-value | Free, **persistenceMode=off**; may lose entries upon restart. | Only ephemeral signaling/rendezvous state should be stored; do not claim backup of its contents. |
| Railway Guided Alpha Remote | Three live-config service slots + one staged-create, no running latest deployments. A pending patch dates to Aug 16. No volumes/buckets. | Build/deploy configuration preserved in JSON. No provider-side stateful volume data to copy. |
| Railway AIOC Bridge | One service slot, no running latest deployment, no volumes/buckets. | Build/deploy configuration preserved in JSON. Source in AIOC Git. |

## Critical scope and safety boundary

**This repository is PUBLIC.** Never place `pg_dump` files, raw table rows, user identities, encryption keys, DB connection strings, access tokens, Render/Railway environment variable values, or other subscriber data here — even under a feature branch or PR. Branch protection or a draft PR does not make contents private. If accidentally committed, assume exposed and rotate/remove appropriately.

This snapshot covers **recoverable configuration**, not database contents or Redis memory. It is not a service failover, transaction checkpoint, data backup, or proof that migrations will work.

Connected Render read-only SQL query failed with explicit provider error: the database's external allowlist is empty, and its hosted connector IP cannot be allowlisted. The connected Render actions have no logical export, `pg_dump`, or restore operation. Render free web instances do not provide shell access. Therefore **no genuine source database export is possible through the connected provider actions available in this session**.

## Action sequence before Nov 8

1. On a trusted Linux host with PostgreSQL 17 tools, prepare a private encrypted backup volume, password file mode 0600, and **single-host** temporary Render IP allowlist as owner/operator. Details: `../XTRA-02_RENDER_CERTIFICATION_RECOVERY_2026-11-02.md`.
2. Run `pcv03f_render_backup.sh` locally, then test isolated `pg_restore` against a fresh private PostgreSQL 17 target and record only a non-sensitive restore receipt in the repo. Do not push the dump. Revoke the temporary allowlist entry afterward.
3. Choose an approved non-expiring target for **data**, restore there, test account/session/allowance/continuity and cross-device acceptance, then cut over `DATABASE_URL` securely with rollback. Preserve source until completion and do not claim zero downtime without measured proof.
4. Only after the data path is safe, evaluate replacement of the Node web host and decommission unused Railway resources. Do not automatically activate staged deployments, purchase compute, or rotate/change secrets during inventory collection.

## Source anchors

- Render dashboard database: https://dashboard.render.com/d/dpg-db4dbknlot8c738kn0k0-a
- Render session service: https://dashboard.render.com/web/srv-db4dhb7lot8c738l8e10
- PCV service source: https://github.com/cybalicistjt-stack/Multiversal-app/blob/work/pcv-03f-service-first-certification/apps/session-service/server.mjs
- PostgreSQL adapter: https://github.com/cybalicistjt-stack/Multiversal-app/blob/work/pcv-03f-service-first-certification/apps/session-service/postgres-persistence.mjs
- Render terms: https://render.com/docs/free
- Original recovery evidence: ../XTRA-02_RENDER_CERTIFICATION_RECOVERY_2026-11-02.md

## Evidence/acceptance receipt

| Gate | 2026-11-02 |
| --- | --- |
| Render provider inventory | Read-only, snapshot included |
| Railway provider inventory | Read-only, snapshot included |
| DB reachable from hosted SQL integration | **No** (external allowlist) |
| Actual database backup SHA256 | **UNAVAILABLE / NOT RUN** |
| Isolated restore | **NOT RUN** |
| Web deploy | Last `live` record October 27; not independent health proof |
| Costs / account/network modifications | None |
| Current recovery classification | **EXTERNAL BLOCKER OPEN** |
