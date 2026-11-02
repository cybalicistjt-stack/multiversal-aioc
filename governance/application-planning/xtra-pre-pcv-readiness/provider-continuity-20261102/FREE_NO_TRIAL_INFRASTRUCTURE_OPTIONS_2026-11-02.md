# XTRA-02: Non-expiring-free and open-source hosting alternatives — 2026-11-02

**Question:** Replace expiring Render free PostgreSQL and reduce dependence on Render/Railway for Multiversal without replacing one free trial countdown with another. **Scope:** owner decision support; no provider enrollment, payment, migration or production authorization.

## Workload from actual Multiversal source

The active PCV-03F session implementation is a Node server using `pg`, `ws`, `tsx` and PostgreSQL `DATABASE_URL`; the adapter creates `mv_pcv_records` (JSONB records) and uses SQL transactions. The source exposes HTTPS for commands, membership/account bootstrap and an advisory WebSocket; reconnect/checkpoint polling must work after transport interruptions. Other account, GM allowances and offline-entitlement machinery are present in the same service.

**Requirements:** durable PostgreSQL with external connections, recoverable backups, ordinary Node process, HTTPS+WSS, safe secrets, portability, upgradable limits, unattended health and failure notification, and a verified independent restore. Do not assume a provider having a `free` label satisfies uptime, HA, security or the eventual subscriber production SLA.

## Candidate comparison (official source verified 2026-11-02)

| Candidate | Cost/time status | Postgres compatibility | Node HTTPS/WSS app hosting | Availability / data caveat | Verdict |
| --- | --- | --- | --- | --- | --- |
| **Aiven PostgreSQL Free** | $0 with no fixed time limit; no card required | **Native PostgreSQL**, one free instance, 1 CPU, 1 GB RAM, 1 GB disk, backups offered | No application runtime in DB tier | Provider may power off on inactivity; single-node, 20 max connections, no SLA. Validate exact backup retention and major version. | **Top low-change replacement for expiring DB during certification** |
| **Neon Free** | $0, no stated 30-day DB expiry | **Native PostgreSQL**, 1 GB/project, 100 CU-h per project/mo, 5 GB network/project/mo; 6-hour restore history, one manual snapshot | Node app hosted separately; Functions not assumed compatible with persistent WebSocket server | Compute scales to zero after 5 min; exhausted compute/transfer suspends until billing period. Frequent connections can consume hours. | **Strong alternative**; profile connection/workload usage |
| **Supabase Free hosted** | $0 no 30-day expiry; 2 active free projects | **Native PostgreSQL**, 500 MB DB | Realtime exists but current Node app must still be hosted separately | Pauses after insufficient DB activity during 7 days; paused data retained; managed free backup not equivalent to independent restoration | **Viable dev sandbox**, weaker unattended continuity |
| **Oracle Cloud Always Free VM** | No fixed duration for eligible Always Free services | Self-host ordinary PostgreSQL 17 (open source) | Self-host current Node server with WSS reverse proxy | Official docs 2 total Ampere A1 OCPUs/12 GB RAM or eligible AMD micro shapes; 200 GB block allowance; shapes may be unavailable, idle instances may be reclaimed; patch/backup/security/monitoring become our work | **Best no-trial unified hosted-stack pilot**, conditional on real eligible capacity |
| **Google Cloud Always Free e2-micro VM** | Non-expiring monthly quota; billing account required | Self-host PostgreSQL or pair with Aiven/Neon | Hosts low-throughput Node with HTTPS/WSS | 1 GB RAM/0.25 fractional vCPU, 30 GB standard disk, 1 GB outbound monthly free; overage can bill on paid billing account | **Constrained fallback** for small Node service, not ideal for full PG+app |
| **Existing Render Free Web + Aiven/Neon Free DB** | No fixed web trial; managed DB no time expiry | PostgreSQL as above | Current Node app deploy is already `live`; WebSocket supported | Web spins down after 15 min no HTTP/WS traffic; cold startup ~1 min, ephemeral disk, pooled 750 hours/workspace/month | **Fastest low-change non-expiring certification configuration**, not a production SLA |
| **Koyeb Free Web + Aiven/Neon** | One ongoing free 0.1 vCPU/512 MB web service | PostgreSQL separately | Node process support; verify service config and WSS during pilot | Sleeps after 1h idle; no persistent volumes; not recommended for production | **Free backup compute option**, low performance |
| **Cloudflare Workers + Durable Objects SQLite** | Ongoing free quotas (Workers 100k requests/day, DO SQLite usage limits) | **Not PostgreSQL** natively; could use external PG via Hyperdrive, but Node socket/PG/WS behavior requires adaptation | Supports web/WS patterns via Workers+DO, not direct process hosting | Requires architectural redesign, quota-exhaustion failures, new event semantics; not a direct server.mjs replacement | **Research/long-term optimization only**, not emergency migration |
| **Home/Linux server + PostgreSQL + Cloudflare Tunnel** | Open-source app+database; $0 *hosting subscription* if existing hardware/domain/network available | Native PostgreSQL, full control | Current Node + WSS through reverse proxy/tunnel | Electric/internet/UPS/hardware/security burden; owner-controlled, no cloud provider trial; Cloudflare Tunnel supports WebSockets | **Best ownership and portability test site**; do not treat a laptop CI runner as production HA |

**Source citations (primary):**
- Aiven indefinite free PostgreSQL, backups and idle shutdown: https://aiven.io/docs/products/postgresql/concepts/pg-free-tier ; https://aiven.io/free-postgresql-database
- Neon free quota and suspend behavior, updated Oct 1 2026: https://github.com/neondatabase/website/blob/main/content/faqs/free-plan-limits-and-quotas.md
- Supabase inactivity pausing (Oct 2026): https://supabase.com/kb/faqs/platform/free-project-pausing ; https://supabase.com/pricing
- Oracle Always Free, available shapes and reclamation: https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm
- Google ongoing monthly quota: https://docs.cloud.google.com/free/docs/free-cloud-features
- Render free web/DB policies: https://render.com/docs/free
- Koyeb Free: https://www.koyeb.com/docs/reference/instances
- Cloudflare Workers and Durable Objects: https://developers.cloudflare.com/workers/platform/pricing/
- Cloudflare Tunnel WebSocket support: https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/
- Coolify open-source PaaS (software free, server not included): https://github.com/coollabsio/coolify
- Supabase self-hosting needs 4 GB minimum for complete stack: https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/self-hosting/docker.mdx
- Railway trial is 30 days, then a distinct Free plan with $1/month included credit, not a perpetually funded VM: https://docs.railway.com/pricing/free-trial

## Decision: split urgent data preservation from eventual runtime redesign

**Immediate certification target:** Aiven Free PostgreSQL first, or Neon Free second, **but only after the Render DB is exported and restored somewhere isolated**. Keep the existing Render free Node service temporarily. Its 15-minute idle shutdown is tolerable for bounded tests, but it does not guarantee no interruption. Aiven inactivity power-off is also a real service issue, so test cold resume and activity requirements; Neon uses a separate compute quota. Neither is an automatic always-on production choice.

**Longer-term zero-subscription pilot:** Oracle Always Free ARM VM with Ubuntu, PostgreSQL 17, current Node service, reverse proxy, restricted public HTTPS/WSS, firewall, least-privilege operator credentials, backups encrypted to a second independent location, external health checks, restore drills. Compare to local Linux server via Cloudflare Tunnel and to free compute plus hosted DB. Oracle is free to eligible accounts but not guaranteed to allocate capacity, stay available or avoid idle reclamation. **Open source does not eliminate infrastructure or operational cost.**

**Potential better operational choice later:** pay for a small reliable managed DB or server rather than rely on free tiers for paying subscribers; costs require separate owner approval.

## Required migration acceptance (provider-independent)

1. Securely export old PostgreSQL 17 data and independently verify restore with actual source schema (not synthetic fixtures); do not push dump or secrets to public AIOC.
2. Test the target's SSL/TLS, connection limit, major version, `pg` client behavior, migrations and JSONB schema parity.
3. Validate login/verified account migration, durable command ordering, invitation revocation, GM allowances, restricted-content entitlements, offline resumption, Android/Windows reconnect/checkpoint recovery, stale authority fencing, and WSS-reconnect+HTTPS polling fallback.
4. Exercise service restart, sleep/wake, DB disconnect, long idle, target quota exhaustion and response latency. Require no false connected state; preserve evidence with timestamps.
5. Establish encrypted offsite backups, retention/restore and ownership, independent monitoring and expiry/quota watches. A single free provider is **not** a backup.
6. Repoint production/test `DATABASE_URL` and external endpoints only via approved secure operator action and rollback plan; do not mutate live provider connections as part of research.

## Do not conflate alternative categories

- Render and Railway are *hosting platforms*. PostgreSQL is an open-source *database engine*. Aiven, Neon, Supabase are *hosted database services*, not drop-in Node WSS server hosts.
- Cloudflare Tunnel is ingress connectivity, not a server. Coolify is management software, not free compute. A self-hosted PostgreSQL instance is only as durable as its disk, backup, access policy and restoration process.
- Free-tier status can change; none of these services offers an enforceable lifetime free hosting guarantee or an appropriate production uptime SLA on the free plan.
