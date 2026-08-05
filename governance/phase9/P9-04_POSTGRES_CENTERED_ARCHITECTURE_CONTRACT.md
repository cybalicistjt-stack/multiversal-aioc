# P9-04 — Postgres-Centered Architecture Contract

**Status:** implementation-readiness complete; implementation not authorized  
**Owner:** John Brandon Turner  
**Selected architecture class:** Postgres-centered managed backend  
**Scope:** bounded two-device online internal alpha

## Authority boundary

The server is authoritative for identity, entitlements, campaign membership, session commands, hidden information, canonical state transitions, checkpoints, and audit events. Clients submit commands and render authorized projections; they do not directly write authoritative game state.

## Provider-neutral service boundaries

1. `IdentityPort` — authenticate users and resolve stable subject IDs.
2. `EntitlementPort` — evaluate subscription, sponsored-month, campaign-grant, pack, and ability-tier access.
3. `PersistencePort` — transactional canonical data and append-only audit events.
4. `SessionCommandPort` — validate, authorize, execute, and idempotently record session commands.
5. `RealtimePort` — publish authorized projections and command outcomes.
6. `CheckpointPort` — create, verify, restore, and export deterministic checkpoints.
7. `ObjectStoragePort` — maps, images, pack archives, and large immutable artifacts.
8. `TelemetryPort` — structured logs, metrics, traces, security events, and cost signals.

No domain service may depend directly on a named vendor SDK outside an adapter package.

## Core relational contract

Required logical tables:

- `subjects`, `identities`, `sessions`, `refresh_tokens`
- `products`, `plans`, `subscriptions`, `entitlement_grants`, `sponsored_months`, `entitlement_evaluations`
- `campaigns`, `campaign_members`, `campaign_roles`
- `content_packs`, `pack_versions`, `pack_installations`, `canonical_objects`, `object_relationships`
- `game_sessions`, `session_participants`, `session_commands`, `session_events`, `session_projections`
- `checkpoints`, `checkpoint_objects`, `restore_attempts`
- `audit_events`, `security_events`, `outbox_events`, `schema_migrations`

Every tenant- or campaign-scoped row carries its scope identifier. Every mutable authoritative row carries version, created-at, updated-at, and actor metadata. Canonical objects preserve source and provenance coordinates.

## Identity and authorization

Stable application subject IDs are independent of provider user IDs. Authorization is deny-by-default. Database row-level policies and service authorization must agree; service checks are not a substitute for database isolation. Privileged service credentials never reach clients.

## Entitlement evaluation

Entitlements are derived from immutable grants and revocations, not editable booleans. Evaluation records capture subject, resource, decision, reason codes, evaluated inputs, ruleset version, and timestamp. Sponsored months and campaign grants follow the completed P9-01 contracts without reinterpretation.

## Authoritative session execution

Each command includes command ID, session ID, actor, expected state version, command type, payload schema version, and client timestamp. Execution occurs in one transaction:

1. authenticate and authorize;
2. reject duplicate or stale commands safely;
3. validate domain preconditions;
4. lock or compare the session version;
5. append command and resulting events;
6. update canonical state/projections;
7. enqueue realtime notifications through a transactional outbox;
8. commit and return the authoritative result.

Commands are idempotent by `(session_id, command_id)`. Hidden data is excluded before publication, not filtered only in the UI.

## Realtime and reconnect

Realtime delivery is advisory; committed database state is authoritative. Clients track the last acknowledged event sequence. On gaps or reconnect, they fetch a permitted projection or checkpoint plus subsequent events. Ordering is monotonic per session. Duplicate delivery is expected and harmless.

## Checkpoints and recovery

Checkpoints contain session version, event sequence, ruleset and pack versions, canonical state digest, authorized object references, creation reason, and SHA-256. Restore is rehearsable, logged, and produces a new recovery event rather than erasing history.

## Security

Mandatory controls include least privilege, row-level isolation, secret rotation, parameterized queries, schema validation, rate limits, command-size limits, audit retention, encryption in transit and at rest, dependency scanning, backup encryption, and tested incident revocation. Security-sensitive events are append-only.

## Migration and compatibility

All schema changes are ordered, repeatable, reviewed migrations. Destructive changes require expand–migrate–contract sequencing, verified backups, rollback or forward-repair instructions, and compatibility with the currently supported client version. Pack and object schema versions remain independently migratable.

## Backup and restore

The alpha requires automated database backups, point-in-time recovery where available, encrypted artifact backups, periodic export to provider-neutral formats, documented recovery objectives, and a successful restore drill before live internal-alpha data is trusted.

## Observability and cost controls

Structured telemetry must expose command latency and failures, authorization denials, realtime lag, reconnect success, checkpoint duration, restore outcomes, database saturation, storage growth, outbound bandwidth, and estimated service cost. Personally sensitive or hidden game content must not be logged by default.

## Provider exit

Exit capability requires SQL schema and data export, object-storage export, identity mapping export, migration history, environment-independent fixtures, adapter contract tests, and a documented replacement-adapter procedure. Provider-specific features must have a fallback or an explicit accepted-exit cost.

## Explicit non-authorization

This contract does not authorize vendor account creation, paid services, production deployment, credentials, live schema application, or application feature implementation.

## Completion gate

P9-04 passes when schemas, contracts, security rules, migration/backup/restore procedures, provider-exit evidence, deterministic contract tests, and CI validation exist and preserve all P9-01/P9-02 constraints.