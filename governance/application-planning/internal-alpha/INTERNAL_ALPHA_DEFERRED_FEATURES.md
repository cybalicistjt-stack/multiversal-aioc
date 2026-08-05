# Features Previously Deferred to Internal Alpha

**Program:** MV-IA-001  
**Version:** 0.1.0  
**Status:** HISTORICAL RECONCILIATION AND CURRENT CLASSIFICATION

## 1. Purpose

This record answers which feature modules had been intentionally left for internal-alpha planning or later implementation, reconciles the earlier `feature-modules.html` tracker with the approved Stage A program, and prevents those features from being lost or mistaken for already implemented work.

## 2. Historical current modules

The earlier Feature Module Roadmap treated three modules as current build or active restoration rather than deferred modules:

1. Combat and Action Resolution.
2. Character Creation and Advancement.
3. Pack Import, Validation, and Registry.

Their architecture or early foundations existed, but the complete product workflows still require Stage A implementation and internal-alpha validation.

## 3. Historical early-preparation modules

These were the features most directly described as work that could be designed early but would become active in or approaching internal alpha:

1. **Campaign, Scene, and Session Builder**
   - Campaign planning;
   - maps or visuals;
   - environments;
   - creatures;
   - traps;
   - notes;
   - objectives;
   - Session state.

2. **Relationship Tracker**
   - directional relationships;
   - relationship history;
   - thresholds;
   - visibility;
   - obligations;
   - promises and debts;
   - mechanical consequences.

3. **Social Interaction Mode**
   - structured conversations;
   - influence;
   - negotiation;
   - reputation;
   - relationship change;
   - social Conditions.

4. **Investigation and Clue Board**
   - clues;
   - hypotheses;
   - evidence links;
   - discoveries;
   - permissions;
   - unresolved questions;
   - false leads.

5. **Inventory, Ownership, and Shared Assets**
   - items and containers;
   - loadouts;
   - ownership and custody;
   - permissions;
   - shared vehicles;
   - transfers;
   - audit history.

6. **World and Setting Builder**
   - Worlds;
   - Regions;
   - Locations;
   - factions;
   - Environments;
   - timelines;
   - connected content.

7. **Encounter Builder and Balance Lab**
   - encounter composition;
   - pressure estimation;
   - deterministic or seeded simulation;
   - dependency validation;
   - uncertainty and warning presentation.

These seven modules are the clearest historical answer to “the features we were putting off until alpha.”

## 4. Historical future-plan modules

The same tracker listed nine additional modules as future work targeted at the internal-alpha horizon or after their prerequisites:

1. **Vehicle, Mecha, and Starship Operations**
2. **Maps, Zones, and Tactical Positioning**
3. **Downtime, Crafting, and Projects**
4. **Factions, Reputation, and Organizations**
5. **Adventure and Story Flow Runtime**
6. **Content Library and Entitlements**
7. **Accessibility and Adaptive Interface**
8. **Offline Play and Synchronization**
9. **Governed AI Assistance**

## 5. Current reconciliation

The approved Stage A program changed how several historical future modules must be treated.

### Promoted to entry-critical foundations

These cannot wait until late alpha because other features depend on them:

- Content Library and Entitlements;
- Accessibility and Adaptive Interface;
- bounded autosave, reconnect, recovery, and offline behavior;
- permissions and hidden-information controls;
- application shell and workspace navigation;
- universal object experience;
- onboarding, diagnostics, and issue reporting.

### Alpha-required

These remain the major product features intentionally designed for internal alpha:

- Relationship Tracker;
- Social Interaction Mode;
- Investigation and Clue Board;
- Inventory, Ownership, and Shared Assets;
- Campaign, Scene, and Session Builder;
- Encounter Builder and Balance Lab;
- Factions, Reputation, and Organizations;
- Adventure and Story Flow Runtime;
- bounded World and Setting Builder;
- bounded combat and Character workflows.

### Experimental in alpha

The narrow alpha slice may be tested while the complete feature remains deferred:

- advanced maps and tactical positioning;
- full vehicle, mecha, and starship station operations;
- broad offline synchronization;
- full Downtime, Crafting, and Project breadth;
- governed AI assistance;
- advanced simulations and content drafting.

### Deferred beyond internal alpha

- public marketplace;
- creator payouts;
- production billing;
- public community discovery and moderation;
- public App Store distribution;
- production-scale support and reliability guarantees;
- autonomous AI mutation;
- complete implementation of every optional setting and subsystem.

## 6. Scope-splitting rule

A feature does not have to be classified entirely as included or excluded.

Examples:

- basic vehicle ownership and Scene use are alpha features; full starship station operations are experimental;
- save, reconnect, and recovery are entry-critical; broad conflict-aware offline editing is experimental;
- basic Location or faction authoring is alpha-required; a public creator marketplace is deferred;
- source-linked read-only AI assistance may be experimental; autonomous AI mutation is deferred.

## 7. Terminology correction

There is no prophecy feature or prophecy content category in the internal-alpha program. Any such wording came from an autocorrect error for **project** and must be ignored or corrected rather than interpreted as a requirement.

## 8. No-loss rule

A feature previously deferred to internal alpha remains represented in the registry even when:

- its classification changes;
- only a narrow slice is included;
- its full scope remains deferred;
- prerequisites are not yet implemented.

The project must not silently drop the Relationship Tracker or other deferred modules merely because the implementation roadmap is organized differently.