# Multiversal Player Species (MVPS) Program

**Program ID:** MVPS  
**Family:** Multiversal Player Species  
**Status:** ACTIVE PROGRAM / MVPS-10 completed_verified / MVPS-11 in_progress  
**Operational authority:** none outside `operations/CURRENT.json`

## Mission

Make every playable species a first-class, executable Multiversal game object rather than a flavor record or stat package.

A conforming species must be selectable, validated, composed with lineages/forms/adaptations, projected into runtime capabilities, equipped, advanced where applicable, exposed to environments, referenced by social/knowledge systems, serialized, migrated, authored, inspected, and reused by NPC/creature-facing systems without species-specific application code.

## Core object principle

Species describe and grant capabilities. They should not own bespoke mechanics when a shared Character, Ability, Action, Effect, Condition, Resource, Modifier, Equipment, Environment, Progression, Knowledge, or Presentation contract already exists.

## Canonical aggregate target

`SpeciesDefinition` owns or references:
- identity, versioning, provenance, taxonomy and setting scope;
- biology descriptor and lifecycle metadata;
- morphology/body-plan and scale profiles;
- fixed and selectable choice schema;
- sense, movement, adaptation and capability grants;
- equipment/body compatibility rules;
- lineage and form references;
- optional progression hooks;
- social/language/knowledge identity hooks;
- presentation/assets;
- validation profile and extension data.

A character stores a `CharacterSpeciesSelection` receipt rather than copying the definition:
- species/version;
- lineage/form selections;
- selected trait/adaptation choices;
- substitutions and adjudications;
- campaign overrides;
- grant/provenance receipts.

## Boundaries

MVPS owns species-specific contracts, adapters, validators, fixtures and acceptance proof.

MVPS consumes shared owner contracts. It does not silently rewrite:
- Character/Ability/Equipment capability owners active in MNCS or their successors;
- environment/location owners;
- character-presentation owners;
- generic progression, action/effect, knowledge, inventory or migration engines.

If an MVPS tranche discovers a necessary shared-owner change, record it as an explicit dependency and coordinate it through OPS3 rather than crossing lane ownership.

## Parallel execution

MVPS is a persistent lane independent of MSAS and MRCS. Each persistent lane uses its own implementation branch. Same-repository publication is serialized by the OPS3 FIFO merge-lease protocol and exact-base validation rules.

## Acceptance doctrine

The final golden proof must run one common species contract against radically different fixtures including at least:
1. ordinary human;
2. winged humanoid;
3. aquatic non-humanoid;
4. centaur-like quadruped;
5. construct/android;
6. multi-form shapeshifter;
7. incorporeal being;
8. radically alien body plan.

All eight must create, validate, equip or explicitly reject equipment through common compatibility rules, advance where applicable, transform where applicable, interact with environments, enter shared gameplay systems, serialize, migrate and render without species-specific application branches.

## Source basis

The program is grounded in the approved 2026-09-18 player-species completeness audit and the OPS3 reference corpus: Project Bible character lifecycle/composition/progression/action/effect/resource/ability contracts, Feature Bible integration principles, UI/Screen character-builder contracts, and sanitized DB-004 game-framework references.
