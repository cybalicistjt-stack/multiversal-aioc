# MRCS — Multiversal Rules & Content Studio

**Program ID:** MRCS  
**Program name:** Multiversal Rules & Content Studio  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; NOT STARTED  
**Activation:** after MSAS-21  
**Successor:** SMB-08  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-11  
**Implementation authority:** none

## Purpose

MRCS turns the existing Multiversal Content Forge design into the complete creator-facing environment for constructing governed rules and reusable content without requiring ordinary authors to hand-edit JSON, schemas, formulas, dependency manifests or code.

The governing flow is:

`owner-domain rules/contracts → Content Forge guided authoring → candidate definition graph → validation / balance / provenance → governed content pack → runtime consumption`

MRCS is not a new canonical rules engine and not a second content database. It converges on the existing Content Forge doctrine: **the author thinks in creative terms; the Forge translates those choices into governed records.**

A draft, generated candidate, cloned definition, house-rule overlay or packaged content object does not become canonical merely because MRCS can express it. Acceptance still follows the owning domain's governed path.

## Placement

`SMB-07 → CNI-01..13 → PCA-01..16 → MCS-01..21 → MCCS-01..21 → MAS-01..21 → MSAS-01..21 → MRCS-01..21 → SMB-08 → SMB-09 → SAA-01..20 → SMB-10`

MRCS is last in the creator-studio interstitial sequence so it can consume the finished map, entity, adventure and audio presentation/binding surfaces while still completing before SMB-08 begins substantial first-party content-library production.

## Existing foundation

MRCS extends rather than replaces the existing `docs/FORGE_SYSTEM_DESIGN_v8.md` contract and current Content Forge prototypes. The existing design already establishes guided type selection, natural-language interviews, canonical reference binding, readable/structured previews, provenance and dependency validation, Pack Lists and `.pack` compilation.

MRCS adds the missing system-construction depth: rule atoms, formulas/predicates/selectors, cross-domain definition editors, governed system/house-rule overlays, dependency impact analysis, balance/simulation evidence, bulk migration/repair and complete publication/versioning workflows.

## Authority boundaries

- **Owning gameplay/content domains** remain authoritative for the semantics of Attributes, Skills, Knowledges, Proficiencies, Abilities, Actions, Effects, Conditions, Resources, Species, Forms, Professions, Items, Magic, Creatures, Vehicles, Environments, Encounters, economies and other governed definitions.
- **CAB** remains the completed advancement/balance authority. MRCS consumes CAB rules and harnesses; it cannot silently reopen, simplify or supersede CAB.
- **CNI** remains modular conditional-content runtime authority; MRCS may author compatible definitions and packs but does not create a second narrative/content runtime.
- **ARI** owns resource identity, source/derivative lineage, rights/use capability and imported/generated asset provenance.
- **Action/Event and runtime owners** retain canonical mutation authority. Definition authoring and preview never prove that a live event occurred.
- **MCS, MCCS, MAS and MSAS** retain their specialized creator domains; MRCS may bind to their outputs without absorbing their ownership.
- **PCA** supplies reusable recipe, simulation, QA and production primitives; MRCS provides the integrated rules/content construction experience.
- Existing Content Forge files and `content-db` are foundations to converge, not legacy excuses to create a parallel authoring database.

## Core doctrines

1. **Definition is not instance.** Reusable definitions, variants, templates, forms, placements, live instances and derived projections/stat blocks remain distinct.
2. **Mechanical prose is not enough.** Where a governed Action, Effect, Condition, Resource, Ability or other shared record exists, structured references are preferred over duplicated prose.
3. **Normal creation is no-code.** Advanced creators may use bounded formulas, predicates, selectors and graphs, but unrestricted scripting is not the default authoring model.
4. **Rules are scoped.** Core rules, setting rules, campaign house rules, adventure overrides and temporary playtest rules must have explicit scope, precedence, compatibility and rollback behavior.
5. **Changes are inspectable.** Dependencies, impact, migration, version history and effective-rule resolution must be visible before publication.
6. **Balance claims require evidence.** Where CAB or another owner provides an approved harness, MRCS uses it; the studio never labels content balanced merely because it validates structurally.
7. **Provenance survives transformation.** Imports, clones, forks, repairs, AI drafts and migrations preserve source and derivative lineage.
8. **AI is optional and advisory.** AI may explain, suggest, draft and compare; it may not silently publish, canonize or mutate live state.
9. **Local-first.** Blocking authoring, validation, packaging and review remain usable without paid/cloud providers.
10. **Accessible structured alternatives.** Graphs and visual editors require list/table/tree alternatives, keyboard operation, non-color status cues and readable diagnostics.

## Content construction surface

MRCS should make ordinary construction possible for at least:

- Actions, action types, Effects, Conditions, Resources, durations and triggers;
- Ability Trees, Abilities, Prestige content, prerequisites and acquisition packages;
- Attributes, Skills, Knowledges, Proficiencies and advancement packages;
- Professions, Backgrounds, Cultures, Factions and social packages;
- Species, Forms, Archetypes, Templates, Variants and Traits;
- Items, weapons, armor, ammunition, consumables, tools, equipment slots and loadouts;
- spells, powers, casting methods and supernatural/magic-system packages;
- creatures, monsters, NPC-role packages and governed behaviors;
- vehicles, mounts, companions, constructs and modular components;
- environments, hazards, terrain rules and world-content definitions;
- encounters, challenges, rewards, loot, currencies, economies and services;
- scoped system extensions and house rules.

This list is extensible through the governed content-type registry rather than a permanently hard-coded set of screens.

## Benchmark classes

Public capability study is clean-room planning provenance only. MRCS retains useful workflow classes from:

- D&D Beyond-style guided homebrew creation and downstream integration;
- Foundry VTT game-system Data Models, package manifests, compendium/content packaging and module boundaries;
- Foundry Custom System Builder/Sandbox-style no-code custom sheets, formulas and rolls;
- Fantasy Grounds ruleset/extension/module layering and dependency concepts;
- RPG Maker-style database-centric RPG content construction;
- modular stat/inventory/quest construction tools such as Game Creator;
- event/behavior visual logic systems such as GDevelop.

MRCS does **not** copy proprietary source, assets, schemas, distinctive UI expression, private protocols or vendor-specific implementations.

## Tranches

### MRCS-01 — Rules & Content Studio Workspace, Authority & Content-Forge Convergence
Establish the product surface, workspace model, Content Forge convergence plan, ownership map, authoring-state model and definition-vs-instance invariants.

### MRCS-02 — Content-Type Registry, Schema-Aware Forms & Progressive Disclosure
Drive authoring from governed type metadata, required/optional fields, vocabularies, relationships and validation while keeping ordinary screens understandable.

### MRCS-03 — Guided Forge Interviews, Templates, Clone/Fork & Natural-Language Authoring
Generalize guided interviews, starter templates, clone/fork lineage, save-and-exit, decide-later behavior and optional advisory AI across content types.

### MRCS-04 — Rule Atom, Formula, Predicate, Selector & Expression Workbench
Provide bounded typed expressions for arithmetic, comparisons, predicates, selectors, scaling and derived values with inspectable inputs and no unrestricted-script default.

### MRCS-05 — Action, Effect, Condition, Resource, Duration & Trigger Authoring
Create reusable mechanical atoms and their references, timing, frequency, resource, stacking/interaction and trigger semantics.

### MRCS-06 — Ability, Ability Tree, Prestige, Prerequisite & Acquisition Authoring
Author trees, tiers, abilities, eligibility, acquisition, pricing evidence and prerequisite/dependency graphs while preserving CAB distinctions.

### MRCS-07 — Attribute, Skill, Knowledge, Proficiency & Advancement-Package Authoring
Author advancement-facing definitions and packages over their existing owner rules without creating alternate advancement economics.

### MRCS-08 — Profession, Background, Culture, Faction & Social-Package Authoring
Create reusable social/life-role packages with explicit mechanical and narrative references rather than opaque prose bundles.

### MRCS-09 — Species, Form, Archetype, Template, Variant & Trait Authoring
Preserve identity, inheritance, compatibility, transformation and definition-layer distinctions already required by Content Forge/PPIA/CAPP.

### MRCS-10 — Item, Equipment, Weapon, Armor, Consumable, Tool & Loadout Authoring
Create equipment families, slots, actions/effects, variants, requirements, resources and loadouts with dependency-safe reuse.

### MRCS-11 — Spell, Power, Casting Method, Magic-System & Supernatural Package Authoring
Build structured supernatural content over owning magic/resource/casting contracts without inventing a parallel magic runtime.

### MRCS-12 — Creature, Monster, NPC Role, Behavior & Combat-Package Authoring
Extend the existing creature Forge into reusable taxonomy, behavior, action, defense, resource, habitat and role packages while keeping taxonomy separate from encounter presentation.

### MRCS-13 — Vehicle, Mount, Companion, Construct & Modular-Component Authoring
Author chassis/components, attachment/slot compatibility, crews/riders, movement, resources, actions and linked entity definitions.

### MRCS-14 — Environment, Hazard, Terrain Rule, Resource & World-Content Authoring
Create reusable environment/hazard/world-facing rule definitions and compatibility metadata without silently placing them into canonical World state.

### MRCS-15 — Encounter, Challenge, Reward, Loot, Economy & Service Content Authoring
Compose encounter/challenge/reward/economic definitions and reusable tables/packages while consuming rather than replacing Encounter/economy owners.

### MRCS-16 — System Extension, House Rule, Override, Compatibility & Scope Authoring
Provide explicit core/setting/campaign/adventure/playtest scopes, compatibility declarations, precedence, enable/disable, rollback and conflict diagnostics.

### MRCS-17 — Dependency Graph, Reference Browser, Impact Analysis & Safe Refactoring
Visualize inbound/outbound references and calculate change impact; support governed rename/re-ID/replace/deprecate/migrate operations without silently breaking dependents.

### MRCS-18 — Balance Lab, Simulation, CAB Harness & Playtest Evidence
Run owner-approved deterministic/stochastic harnesses, comparisons and simulations; attach evidence and warnings without reducing Multiversal balance to one universal scalar.

### MRCS-19 — Bulk Import, Legacy Repair, Migration, Round-Trip & Batch Editing
Support spreadsheet/structured import, field mapping, legacy repair queues, provenance-preserving batch edits, aliases/history and explicit unresolved states.

### MRCS-20 — Pack Lists, Versioning, Diff/Review, Provenance, Publication & Sharing
Complete Pack List and `.pack` workflows with dependency manifests, semantic versions, diffs, approvals, rights/provenance, compatibility, install/update/rollback and sharing boundaries.

### MRCS-21 — Golden Cross-Domain Rules/Content Construction & Runtime Proof
Prove guided and advanced creation across the major rule/content families, dependency-safe changes, balance evidence, packaging/migration, local-first operation and runtime consumption without ownership bleed.

## Golden proof

MRCS-21 must demonstrate, on original Multiversal content:

- a Profession plus advancement-facing package;
- an Ability Tree with Abilities, prerequisites, resources, Actions and Effects;
- a Species/Form/Template chain;
- equipment and a loadout;
- a spell/power/casting-method package;
- a creature/monster;
- a vehicle, mount, companion or modular construct;
- an environment/hazard definition;
- an encounter with rewards/economic content;
- a scoped house-rule/system extension;
- guided and advanced authoring converging on the same governed model;
- dependency impact analysis and safe refactoring;
- CAB-backed balance evidence where applicable, without a universal scalar score;
- legacy import/repair preserving exact provenance and unresolved source gaps;
- Pack List compilation, version/update/migration and rollback evidence;
- runtime consumption that never lets authoring state claim live-instance/event truth;
- useful MCS/MCCS/MAS/MSAS bindings without absorbing their ownership;
- keyboard/non-pointer operation and structured alternatives to graph-only views;
- successful blocking workflow with optional AI and paid/cloud providers disabled.

## Family execution rule

Each MRCS tranche targets **24 active minutes or less under a healthy governed environment**, preserving normal closeout reserve. Oversized work is split before governed start. No MRCS runtime preflight or implementation authority exists now; those are created only when a future governed start selects MRCS-01.

## Non-activation boundary

This planning approval does not alter ARI authority, start MRCS implementation, change canonical game rules, reopen CAB, migrate the content database, publish content, authorize external uploads, activate paid providers, distribute to testers or release/deploy software.

## Completion standard

MRCS completes only when all 21 tranches are `completed_verified` and the golden proof shows that ordinary creators can construct, validate, compare, package and safely evolve broad Multiversal rules/content through Content Forge without hand-editing code or bypassing owner-domain authority.