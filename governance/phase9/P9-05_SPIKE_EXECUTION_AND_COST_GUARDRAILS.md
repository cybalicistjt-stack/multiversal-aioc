# P9-05 — Bounded Technical Spike and Cost Envelope

## Status

Complete and validated as a local, ephemeral, provider-neutral architecture exercise. This package does not create a vendor account, provision a paid service, handle production credentials, deploy infrastructure, or authorize application implementation.

## Purpose

Verify that the selected Postgres-centered architecture can support the two-device internal-alpha requirements inherited from P9-01 through P9-04 while keeping owner cost, operational burden, vendor coupling, and recovery risk bounded.

## Executed model

The spike represents two actors, one GM and one player, communicating through provider-neutral service ports. It exercises identity resolution, campaign membership, entitlement evaluation, authoritative commands, ordered realtime events, hidden-information filtering, reconnect and checkpoint recovery, migrations, backup and restore, and provider-exit export.

The evidence set contains 36 deterministic scenario runs. Eight intentional failures cover unauthorized reads, stale commands, duplicate command IDs, sequence gaps, invalid sponsored-month states, damaged checkpoints, failed migration rollback, and incomplete exports. All eight were detected and rejected. No unexpected failure, source-truth change, or uninstall residue was recorded.

## Alpha capacity envelope

The bounded internal-alpha planning ceiling is:

- 10 concurrent sessions;
- 50 concurrent users;
- 200 monthly active users;
- 1,200 accepted or rejected commands per session-hour;
- 3,600 realtime events per session-hour;
- 30-second checkpoint interval;
- 14-day checkpoint retention;
- 5 GiB database storage;
- 10 GiB object storage;
- 25 GiB monthly egress.

These are planning limits, not production promises. Crossing a limit requires measurement and review rather than silent scaling.

## Cost envelope

The preferred internal-alpha operating target is USD 0–25 per month across database, identity, realtime, server functions, storage, egress, logs, and backups. Any forecast above USD 35 per month is a mandatory owner review gate before commitment.

Paid observability, premium support, edge-session coordination, custom domains, and production redundancy remain excluded unless separately approved.

## Mandatory controls

Usage alerts must trigger at 50%, 75%, and 90% of each metered allowance. Session commands and realtime events require rate limits. Debug payloads must be bounded and scrubbed of secrets. Checkpoint retention must be enforced. Cost estimates must identify assumptions and cannot be represented as vendor quotes.

## Exit test

A clean local Postgres target must accept the logical schema, canonical data, entitlement history, identity mappings, event journals, and checkpoints without provider-specific runtime dependencies. The bounded restore rehearsal passes this condition.

## Decision

The architecture is feasible for the bounded internal alpha. No live vendor selection or spending is required at this stage.

## Next governed step

P9-06 — Implementation Backlog and Acceptance-Gate Package. It must convert P9-01 through P9-05 into sequenced, independently verifiable implementation slices without authorizing deployment or spending.
