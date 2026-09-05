# Application Implementation Roadmap — VTI-02 Governed Start

**Date:** 2026-09-05  
**Status:** canonical governed-start supplement

## VTI-02 — Multiversal External Game Projection Contract

VTI-02 is governed-started from exact application main `027fad06d0bac3a20d56f0cc2a674581662cd1b9` on registered application branch `integration/vti-02-multiversal-external-game-projection-contract`.

The tranche is bounded to a deterministic provider-neutral projection contract for Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference objects. Multiversal remains the canonical rules/campaign authority; external VTTs consume projections only at this boundary.

The contract may carry opaque canonical source-object references, deterministic fields and object ordering, explicit projection availability (`present`, `redacted`, `unsupported`), and metadata preserving visibility scope, ownership reference, consent requirement and GM-authority requirement. These fields preserve constraints; they do not implement a later permission engine.

External-object mappings, fingerprints, version negotiation, stale/conflict handling, reconnect, deduplication and tombstones remain reserved to VTI-03. Rules actions, rolls, attacks, checks, powers, resources, conditions, initiative, reactions and GM adjudication bridging remain reserved to VTI-04. Provider-specific schemas and platform selection remain deferred.

## Authority at governed start

- implementation branch: `integration/vti-02-multiversal-external-game-projection-contract`
- implementation authority: `true`
- branch creation authority: `true`
- acceptance-package authority: `true`
- production-mutation authority: `false`
- matching acceptance RED observed: `false`

Production mutation remains locked until a genuine matching application acceptance RED is sealed on self-hosted Linux and Windows with deterministic comparison evidence.

## Closed boundaries

No vendor selection, ranking or provider-specific schema is authorized. No credential use, external account mutation, provider activation, adapter implementation, external synchronization mutation, canonical game-state mutation, package publication, tester distribution, release or deployment is authorized. Visibility, ownership, consent, hidden-information filtering and GM authority may not be bypassed.

No durable VTI persistence, new migration or external synchronization ledger is authorized. VTI-03+ and SGC-01+ remain unauthorized until their own governed selections and starts.
