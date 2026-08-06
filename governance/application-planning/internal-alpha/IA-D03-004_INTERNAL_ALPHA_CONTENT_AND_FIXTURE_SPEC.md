# IA-D03-004 — Internal Alpha Content and Deterministic Fixture Specification

**Document ID:** MV-IA-CONTENT-FIXTURES-002  
**Version:** 0.1.0  
**Status:** IMPLEMENTATION-READY DESIGN  
**Work item:** IA-D03-004  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-05

## 1. Purpose and required outcome

This specification defines the bounded content and deterministic fixtures required by the completed shared-foundation, Character, Campaign, Scene, Session, Encounter, permission, recovery, pack, diagnostic, and accessibility designs.

The required result is a small, reproducible, version-pinned corpus that can drive local development, CI, migration, recovery, and two-device acceptance tests without loading or claiming to represent the complete Multiversal game.

## 2. Non-negotiable boundary

The fixture catalog is:

- a design and test corpus;
- not a canonical content release;
- not the complete game;
- not permission to discard, merge, rewrite, or deprioritize unselected source material;
- not permission to promote synthetic records;
- not production data or real-user data;
- not an internal-alpha release authorization.

Source-backed fixtures preserve immutable source truth. Synthetic fixtures are explicitly labeled `synthetic-contract-fixture` and remain noncanonical unless separately governed and approved.

## 3. Governing source authorities

The source-backed portion consumes:

- `governance/balance/8D-007_GOLDEN_CORPUS_CONTRACT.json` version 0.1.0;
- `governance/balance/8D-007_GOLDEN_CORPUS_MANIFEST.json` version 0.1.0;
- the 20-dataset, 19,199-promoted-record source corpus;
- reconciliation artifact SHA-256 `112ef5116b4090cc266eefe36e1c539b6567f022d6b857db6e1d2bdd77e30e40`;
- executable baseline SHA-256 `676e14fe50b708c02a175cad88bdb7962fcb9b92ed4afb62b9148648206e2f3c`.

The catalog inherits all 36 golden fixtures by exact fixture ID and does not copy or mutate their source claims.

## 4. Fixture pack topology

Five exact-version fixture packs are specified:

1. `multiversal.golden.8d007@0.1.0` — source-backed selector overlay containing 36 inherited golden fixtures.
2. `multiversal.alpha.identity@0.1.0` — synthetic identities and authority states.
3. `multiversal.alpha.core-content@0.1.0` — synthetic noncanonical Definitions needed where no bounded source selection has yet been approved.
4. `multiversal.alpha.scenarios@0.1.0` — Campaign, Character, Scene, Action, permission, Asset, relationship, investigation, and Encounter workflows.
5. `multiversal.alpha.failures@0.1.0` — deterministic failure injection, corruption, migration, backup, and provider-exit cases.

Dependencies, install order, and manifest checksums are recorded in `INTERNAL_ALPHA_FIXTURE_CATALOG.json`.

## 5. Identity, version, and checksum rules

Every fixture has a stable fixture ID. Synthetic fixture groups additionally record:

- category and governing contract;
- exact fixture pack and schema version;
- stable fixture IDs;
- source/synthetic status;
- migration path;
- cleanup behavior;
- deterministic fixture-checksum derivation;
- a group SHA-256 over canonical UTF-8 JSON with sorted keys and compact separators.

Every synthetic fixture identity therefore has a reproducible derived checksum from its immutable group contract and stable ID. The catalog and coverage matrix have independent SHA-256 values. Any field change requires a version or checksum change and a reviewed regression update.

## 6. Source-backed fixture selection

The catalog inherits the exact 36 8D-007 fixtures spanning:

- general items;
- melee and ranged weapons;
- ammunition;
- computers and software;
- cybernetics and symbiotes;
- EVA suits and modules;
- magitech;
- vehicles;
- mecha;
- spacecraft;
- bases and facilities;
- materials, agriculture, and homesteading;
- Abilities;
- spells;
- spellbooks and charge holders;
- hazards;
- traps.

Their deterministic selectors, source coordinates, scenarios, and expected outcomes remain controlled by the 8D-007 manifest.

## 7. Synthetic content Definitions

Synthetic Definitions provide bounded contract data for source families not selected by the 8D-007 corpus:

- species and forms;
- attributes and derived values;
- skills and proficiencies;
- Actions, Effects, Conditions, and Resources;
- creatures and NPCs;
- environments and adaptations;
- factions and relationship types;
- Locations;
- clues and evidence;
- objectives and rewards;
- adventure routes and consequences.

These records exist solely to exercise schemas and workflows. Each group records `canonicalContent: false` and may later be replaced by a separately approved source-backed selection without changing fixture-purpose identity.

## 8. Identity and Campaign fixtures

The catalog defines nine actor identities:

- Owner/Admin;
- primary GM;
- delegated Assistant GM;
- primary and secondary Players;
- content creator;
- revoked former participant;
- service actor;
- AI service actor with no mutation authority.

`IA-CAMPAIGN-01` is the core journey Campaign. `IA-CAMPAIGN-02` proves search, count, notification, export, and AI-context isolation across Campaigns.

## 9. Character fixtures

Eight Character fixtures cover:

- valid free or Campaign-granted content;
- valid approved higher-tier access;
- missing prerequisite;
- active Conditions and depleted Resources;
- personal and shared Assets;
- relationship history;
- retired lifecycle;
- migration history with stable ID preservation.

Characters are synthetic authoritative-state fixtures, not canonical pregenerated Characters.

## 10. Scene and Action fixtures

Five Scenes cover social, investigation, combat, travel/vehicle, and recovery.

Eleven Action scenarios cover no-roll, rolled, target choice, multiple targets, Resource cost, prerequisite failure, Condition output, relationship output, GM modification, duplicate command suppression, and stale expected version.

Expected Events and authoritative results are controlled by each synthetic group contract and the coverage matrix.

## 11. Permission and hidden-information fixtures

Ten fixtures cover Player-safe extensions, unrevealed clues, Player-private notes, GM notes, hidden NPC motives, restricted content, Campaign grants, revocation, wrong-Campaign access, and an AI hidden-content query.

Denials must be safe: no hidden existence, count, facet, stable ID, relationship, warning, diagnostic, or export leakage.

## 12. Asset, relationship, and investigation fixtures

Twelve Asset fixtures cover ownership, custody, equipment, quantity, containers, borrowing, repair, consumption, crafting, shared vehicles, blocked transfer, split/merge history, and anti-duplication.

Ten relationship fixtures preserve direction, thresholds, promises, debts, motives, reveals, hypotheses, and multi-Scene history.

Eleven investigation fixtures preserve clues, witnesses, evidence, false leads, questions, hypotheses, contradictions, GM truth, and reveal Events.

## 13. Encounter fixtures

The catalog reuses all ten exact F012 scenario identities:

- `EBL-FIX-VALID-MIXED`;
- `EBL-FIX-PACK-INVALID`;
- `EBL-FIX-UNCERTAIN`;
- `EBL-FIX-HIDDEN-WAVE`;
- `EBL-FIX-ACTION-ECONOMY`;
- `EBL-FIX-STALE`;
- `EBL-FIX-RECONNECT`;
- `EBL-FIX-CORRUPT`;
- `EBL-FIX-SIM-REPLAY`;
- `EBL-FIX-ATTACHMENT-INVALIDATED`.

These are synthetic Encounter contract fixtures and cannot certify balance, fairness, safety, victory, survival, or optimality.

## 14. Failure and recovery fixtures

Fourteen deterministic failure cases cover unavailable packs, invalid IDs, stale versions, failed saves, Event gaps, corrupted drafts and snapshots, missing media derivatives, invalid entitlements, mid-screen revocation, duplicate Actions, migration interruption, backup checksum mismatch, and provider-exit import mismatch.

Each group contract defines the protected state, deterministic failure class, and required recovery or rollback evidence.

## 15. Pack lifecycle and residue

Nine ordered scenarios cover clean install, repeated install, update with migration, dependency conflict, blocked dependent removal, safe unused removal, reinstall, export/import, and zero unintended residue.

Source truth, fixture definitions, Events, and immutable receipts remain unchanged by install/uninstall exercises.

## 16. Accessibility stress data

The bounded corpus includes stressors for long names and descriptions, many Conditions, dense relationship graphs, large inventories, nested objects, localized or unusual characters, high zoom, narrow mobile width, map alternative text, and multi-field validation errors.

Accessibility stressors are fixture requirements, not optional sample content.

## 17. Expected Events and results

Synthetic fixture expectations are encoded as deterministic group contracts and requirement-family coverage rows. A fixture may not claim success merely because a UI rendered. Acceptance requires the configured Event, denial, checksum, recovery, projection, migration, or cleanup invariant for that fixture family.

## 18. Migration, export, cleanup, and privacy

Every synthetic fixture group declares a stable-ID/schema-version migration path and cleanup behavior. Export and backup retain fixture identity, source/synthetic status, versions, permissions, expected contracts, and checksums.

Cleanup deletes only derived test state and restores the fixture baseline. It never deletes source content, historical receipts, or unrelated Campaign state.

No fixture contains credentials, production endpoints, real personal data, or unrestricted diagnostic payloads.

## 19. Blocking acceptance criteria

- **ACF-AC-001 — Blocking:** Catalog identity, version, owner, checksum, and bounded-coverage statement are present.
- **ACF-AC-002 — Blocking:** All 36 governed 8D-007 fixtures are inherited by exact fixture ID and source manifest.
- **ACF-AC-003 — Blocking:** Every synthetic fixture is explicitly grouped as synthetic and noncanonical.
- **ACF-AC-004 — Blocking:** Identity fixtures cover Owner, GM, Assistant GM, two Players, creator, revoked, service, and AI actors.
- **ACF-AC-005 — Blocking:** Campaign fixtures cover the core journey and cross-Campaign isolation.
- **ACF-AC-006 — Blocking:** Character fixtures cover valid, invalid, conditioned, Asset, history, retired, and migrated states.
- **ACF-AC-007 — Blocking:** Every required content family is covered by source-backed or explicitly synthetic fixtures.
- **ACF-AC-008 — Blocking:** Scene fixtures cover social, investigation, combat, travel/vehicle, and recovery.
- **ACF-AC-009 — Blocking:** Action fixtures cover rolls, targeting, costs, failures, outputs, GM modification, duplicates, and stale versions.
- **ACF-AC-010 — Blocking:** Permission fixtures cover hidden fields, notes, motives, entitlements, revocation, Campaign isolation, and AI denial.
- **ACF-AC-011 — Blocking:** Asset fixtures cover ownership, custody, equipment, quantity, sharing, repair, consumption, crafting, vehicles, transfer, history, and anti-duplication.
- **ACF-AC-012 — Blocking:** Relationship and investigation fixtures preserve direction, history, hypotheses, hidden truth, and reveal Events.
- **ACF-AC-013 — Blocking:** All ten F012 Encounter scenario IDs and expected invariants are present.
- **ACF-AC-014 — Blocking:** Failure fixtures cover pack, identity, version, save, reconnect, corruption, media, entitlement, revocation, duplicate, migration, backup, and provider-exit cases.
- **ACF-AC-015 — Blocking:** Pack lifecycle covers install, repeat, migrate, conflict, removals, reinstall, export/import, and zero residue.
- **ACF-AC-016 — Blocking:** Accessibility stress data covers every declared stress class.
- **ACF-AC-017 — Blocking:** Every synthetic fixture group defines a stable contract, migration, cleanup, deterministic checksum derivation, and exact fixture identities.
- **ACF-AC-018 — Blocking:** Fixture packs are exact-versioned, dependency-ordered, and checksum-bound.
- **ACF-AC-019 — Blocking:** Validation rejects checksum drift, duplicate IDs, missing dependencies, implicit promotion, and complete-game claims.
- **ACF-AC-020 — Blocking:** The package passes deterministic validation and hosted CI before implementation handoff.

## 20. Coverage limits and replacement policy

The selected source-backed corpus is strongest in the 18 golden domains. Species, creatures, NPCs, environments, relationships, investigation, and adventure flow currently use synthetic contract fixtures for internal-alpha design.

This is an explicit limit, not a content-quality judgment. A later source-selection work item may replace a synthetic Definition with a source-backed record only when stable identity, provenance, permissions, pack version, expected outcomes, migration, and regression evidence are all recorded.

## 21. Implementation handoff

Implementation consumes:

- `INTERNAL_ALPHA_FIXTURE_CATALOG.json`;
- `INTERNAL_ALPHA_FIXTURE_COVERAGE_MATRIX.json`;
- `IA-D03-004_IMPLEMENTATION_TRACEABILITY.json`;
- the 8D-007 source artifacts;
- the completed F004, F005, and F012 packets;
- P9-06 seed/reset, migration, backup, restore, and export foundations.

Suggested implementation slices:

1. fixture schema and checksum library;
2. source-selector resolver;
3. synthetic fixture-pack loader;
4. deterministic seed/reset;
5. Campaign/Character/Scene/Encounter graph assembly;
6. denial and failure injection;
7. migration and provider-exit replay;
8. accessibility data generator;
9. cleanup and zero-residue verification;
10. CI artifact and evidence reporting.

## 22. Owner and release gates

Owner approval remains required for canonical promotion, paid services, production credentials, real-user data, internal-alpha release, production deployment, and public release.

No synthetic fixture may be used as proof that a game rule or canonical object is complete or balanced.

## 23. Readiness decision

The specification is implementation-ready as a design artifact when the catalog, coverage matrix, traceability, review/readiness/completion records, validator, CI, backlog, indexes, and continuity state agree and all checks pass.

Implementation remains dependency-gated by P9-06.

## 24. Exact next design action

**IA-D03-005 — Character/Campaign integration review.**

That review must verify F004, F005, F012, and this fixture specification as one coherent preparation path before the first-playable-loop tranche begins.
