# P9-03 Technology and Service Decision Brief

## Status

Technology comparison is complete. No architecture, vendor, spending, or implementation selection has been made.

## Recommendation

Use a **Postgres-centered managed backend** as the bounded internal-alpha foundation for:

- identity and authentication;
- entitlements and sponsored-month rules;
- canonical persistence;
- session checkpoints and reconnect recovery;
- provenance-bearing pack and object relationships.

Keep all session commands, persistence, identity, entitlement, and transport access behind provider-neutral interfaces. Do not embed vendor-specific objects in canonical game records.

## Why this leads

The existing Multiversal architecture has complex relationships, strict provenance requirements, server-authoritative hidden information, entitlement state, and a future local-capable path. A relational source of truth provides the strongest combined fit while remaining exportable and testable.

## Bounded alpha shape

1. Managed Postgres-centered service for authentication, authorization, entitlements, persistence, and checkpoint storage.
2. Server-side authoritative command handlers for all protected game actions.
3. Realtime delivery used as transport, never as the authority boundary.
4. Provider-neutral adapters for identity, persistence, realtime, and transport.
5. Two-device online internal-alpha test before adding specialized edge-session infrastructure.

## Alternatives retained

- A document-centered managed platform remains the fastest synchronization alternative but carries greater data-model and migration risk.
- A self-hostable backend remains the strongest sovereignty/local-path alternative but adds unacceptable owner operations burden for the first alpha.
- An edge durable-session platform remains a later optimization for high-frequency room coordination, not the initial system of record.

## Approval gate

Owner approval is required before selecting an architecture, creating vendor commitments, spending money, or beginning implementation.

The recommended owner action is:

> Approve Candidate A, the Postgres-centered managed-backend approach, for a bounded two-device internal-alpha architecture, subject to provider-neutral adapters and no paid commitment without a separate cost gate.
