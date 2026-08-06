# Internal Alpha Content and Fixture Baseline

**Program:** MV-IA-001  
**Version:** 0.2.0  
**Status:** IMPLEMENTATION-READY DESIGN  
**Owner:** John Brandon Turner

## 1. Purpose

Define the bounded, deterministic content and fixture corpus required to implement and validate internal-alpha workflows without exposing or claiming to represent the complete Multiversal game.

The detailed IA-D03-004 package is:

- `IA-D03-004_INTERNAL_ALPHA_CONTENT_AND_FIXTURE_SPEC.md`;
- `INTERNAL_ALPHA_FIXTURE_CATALOG.json`;
- `INTERNAL_ALPHA_FIXTURE_COVERAGE_MATRIX.json`;
- `IA-D03-004_IMPLEMENTATION_TRACEABILITY.json`;
- `IA-D03-004_REVIEW_RECEIPT.md`;
- `IA-D03-004_READINESS_RECORD.md`;
- `IA-D03-004_COMPLETION_RECORD.json`.

## 2. Current bounded corpus

The catalog contains:

- **36 source-backed** fixtures inherited exactly from the governed 8D-007 golden corpus;
- **119 synthetic** contract and workflow fixtures;
- **155 total** fixture identities;
- five exact-version fixture packs;
- fifteen requirement-family coverage rows;
- twenty blocking acceptance criteria;
- nine pack-lifecycle scenarios;
- eleven accessibility stressors.

## 3. Source-backed boundary

The source-backed fixtures cover 18 golden domains across the 20-dataset, 19,199-promoted-record CSV registry. Source truth, source coordinates, selectors, expected outcomes, and executable-baseline evidence remain controlled by 8D-007.

The alpha package does not copy, rewrite, rebalance, or promote those sources.

## 4. Synthetic boundary

Synthetic fixtures cover identity, Campaign, Character, content Definitions not selected by 8D-007, Scenes, Actions, permissions, Assets, relationships, investigation, Encounters, failures, recovery, and accessibility.

Every synthetic record is labeled `synthetic-contract-fixture`. Synthetic data is not canonical content and is not evidence that the corresponding complete game domain has been sourced, balanced, or finalized.

## 5. Determinism and ownership

Every synthetic fixture group identifies:

- exact stable fixture IDs;
- a category-specific expected contract;
- exact pack and schema version;
- source/synthetic and canonical-content boundaries;
- migration and cleanup behavior;
- deterministic per-fixture checksum derivation;
- a group SHA-256.

Every fixture therefore has a reproducible derived checksum. Every pack, the full catalog, and the coverage matrix are independently checksum-bound.

## 6. Required fixture families

The bounded corpus covers:

- Owner, GM, Assistant GM, Player, creator, revoked, service, and AI identities;
- core and isolation Campaigns;
- valid, invalid, conditioned, Asset-bearing, historical, retired, and migrated Characters;
- source-backed items, weapons, ammunition, software, cybernetics, EVA, magitech, vehicles, mecha, spacecraft, facilities, materials, Abilities, spells, spellbooks, hazards, and traps;
- synthetic species, attributes, skills, Actions, Effects, Conditions, Resources, creatures, NPCs, environments and adaptations, factions, relationships, Locations, clues, objectives, and adventure routes;
- social, investigation, combat, travel/vehicle, and recovery Scenes;
- Action, permission, Asset, relationship, investigation, Encounter, failure, pack-lifecycle, and accessibility scenarios.

## 7. Global invariants

- stable IDs and source truth remain immutable;
- permissions are evaluated before projection;
- synthetic records are never promoted implicitly;
- expected versions and idempotency are enforced;
- Events are append-only;
- reconnect and retry do not duplicate accepted effects;
- migration, backup, restore, export, and import verify checksums;
- install/uninstall leaves zero unintended residue;
- the core fixture path requires no paid service and no AI.

## 8. Coverage limits

The corpus is intentionally small. Species, creatures, NPCs, environments, relationships, investigation, and adventure flow currently use synthetic contract fixtures unless and until a separately governed source-backed selection is approved.

Unselected source material remains part of the broader Multiversal program and is not discarded or deprioritized by this baseline.

## 9. Implementation and release boundary

This baseline authorizes design and later governed fixture implementation only. It does not authorize:

- canonical content promotion;
- production credentials or services;
- real-user data;
- internal-alpha release;
- production deployment;
- public release.

## 10. Next design action

**IA-D03-005 — Character/Campaign integration review.**
