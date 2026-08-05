# P9-03A Owner Technology Selection Record

**Decision authority:** John Brandon Turner  
**Decision command:** `Continue` issued after the P9-03 owner approval gate  
**Selected architecture class:** Candidate A — Postgres-centered managed backend  
**Decision status:** APPROVED FOR ARCHITECTURE PLANNING  

## Scope of approval

The owner approves Candidate A as the architecture class for the bounded two-device internal-alpha plan.

This approval authorizes:

- architecture-contract definition;
- provider-neutral service-boundary design;
- schema and migration planning;
- security, entitlement, session-authority, checkpoint, reconnect, and observability planning;
- bounded vendor evaluation against the approved architecture class;
- local test harness and implementation-readiness work that creates no paid service or production commitment.

This approval does **not** by itself authorize:

- paid-plan enrollment or spending;
- production deployment;
- irreversible vendor-specific coupling;
- use of owner credentials not already governed and available;
- application implementation beyond a separately governed implementation gate.

## Required architecture properties

1. PostgreSQL is the canonical persistence foundation.
2. Identity, entitlement, sponsored-month, campaign-grant, and access-policy data remain relational and auditable.
3. Session commands are server authoritative.
4. Realtime transport, identity provider, storage, and session coordination are behind replaceable interfaces.
5. Checkpoints and event records support reconnect and deterministic recovery.
6. Hidden GM information is never exposed through client-readable state.
7. Pack and canonical-object data remain portable and exportable.
8. Database migrations, backup/restore, and provider-exit drills are mandatory before production readiness.

## Next governed work item

**P9-04 — Postgres-Centered Architecture Contract and Bounded Implementation-Readiness Package**

P9-04 must produce executable contracts and validation evidence without creating a paid vendor commitment or production deployment.