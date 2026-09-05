# Application Implementation Roadmap — VTI-03 Governed Start

**Date:** 2026-09-05  
**Work item:** VTI-03 — Stable Identity, Versioning & Synchronization  
**Application baseline:** `01aa25d60ad71e5ed318b9680f859c6927a90541`  
**Registered branch:** `integration/vti-03-stable-identity-versioning-synchronization`

## Governed-start result

VTI-03 is `in_progress` from the exact completed VTI-02 application merge. Branch creation, bounded implementation authority and acceptance-package authority are open. Production mutation remains locked until a genuine matching Linux/Windows RED is sealed.

## Authorized acceptance surface

The VTI-03 acceptance package may require and prove only:

- provider-neutral stable external-object mappings between canonical Multiversal source references and derivative external-object identities;
- deterministic fingerprints and version negotiation;
- stale and conflict detection;
- reconnect behavior;
- deduplication and tombstones;
- MIB-03 retry/recovery semantics;
- visibility, ownership, consent, hidden-information filtering and GM-authority preservation in synchronization metadata;
- deterministic normalization, invariant validation and receipts.

## Explicitly blocked

VTI-03 does not authorize rules-action/roll bridging, provider-specific schemas, vendor selection/ranking, VTI-09 platform commitment, credentials, external accounts, adapter implementation, live external synchronization mutation, canonical game-state mutation, durable VTI persistence, a new migration, provider activation, tester distribution, release, deployment, VTI-04+ or SGC-01+ implementation.

## Execution contract

1. Create the registered application branch from exact main `01aa25d60ad71e5ed318b9680f859c6927a90541`.
2. Add only the VTI-03 acceptance package and validation profile.
3. Produce genuine matching RED on self-hosted Linux and Windows at the same exact head, with deterministic comparison evidence and zero unrelated historical profile fanout.
4. Seal that RED in governance before production mutation is unlocked.
5. Implement only the bounded VTI-03 contract necessary to satisfy the accepted RED.
6. Prove exact-head repository health, Linux GREEN, Windows GREEN and deterministic cross-platform comparison.
7. Merge the application PR, terminally retire VTI-03 implementation authority, and select VTI-04 as `selected_not_started` from the exact application merge.

The owner’s `Continue` instruction authorizes this entire bounded execution chain. The tranche must not stop at an intermediate phase unless a genuine external blocker prevents forward progress.
