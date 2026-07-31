# Multiversal AIOC Authoring and Pack List Architecture

## Core rule

Every Multiversal authoring workflow must produce two synchronized outputs:

1. **Authoring Entry** — the human-readable working record used for drafting, notes, review, iteration, provenance, and collaboration inside AIOC.
2. **Game Object** — the normalized machine-readable object shaped for Multiversal schemas and ready to enter a Pack List.

An authoring record is never considered complete if it has only narrative notes. A game object is never considered ready if it lacks its linked authoring entry, validation state, source/provenance, and revision history.

## Pack List definition

A **Pack List** is a grouped collection of validated or in-progress game objects waiting to be compiled into a final Multiversal-app-importable `.pack` file.

A Pack List is not itself the final pack. It is the staging and review layer between object creation and pack compilation.

## Required object lifecycle

`Draft Entry -> Generated Game Object -> Validation -> Pack List -> Cross-object Review -> Pack Compilation -> Final .pack`

Each object must carry:

- stable draft ID;
- proposed canonical object ID;
- object type;
- schema version;
- title/name;
- source and provenance;
- status: draft, incomplete, review-ready, validated, blocked, deprecated;
- dependencies and referenced object IDs;
- tags/domains;
- authoring-entry link;
- Pack List memberships;
- validation errors, warnings, and suggestions;
- revision history;
- export-ready normalized payload.

## Authoring builder behavior

Each builder must use game-aware guided steps rather than generic title/description forms.

### Shared steps

1. **Identity** — name, object type, source world/pack, stable ID suggestion, aliases.
2. **Concept** — purpose, fiction, role in play, player/GM visibility.
3. **Rules** — object-specific mechanics, resources, actions, effects, conditions, scaling, restrictions.
4. **Connections** — abilities, species, worlds, items, scenes, factions, relationships, dependencies.
5. **Presentation** — player text, GM text, short description, tags, art brief, accessibility text.
6. **Validation** — required fields, IDs, duplicate detection, missing references, schema checks, balance warnings.
7. **Outputs** — save authoring entry, generate/update game object, add to one or more Pack Lists, export JSON.

## Object-aware builders

The first complete builder set should cover:

- worlds/settings;
- environments and adaptations;
- species;
- creatures and NPCs;
- abilities;
- actions;
- effects;
- conditions;
- resources;
- items;
- vehicles;
- factions;
- locations;
- quests/adventures;
- scenes and encounters;
- dialogue and social content;
- relationships;
- rules profiles and progression objects.

Each builder may expose different fields, but all must output the same shared lifecycle metadata.

## Pack List workspace

The AIOC must include a dedicated Pack List workspace with:

- create, rename, duplicate, archive, and delete Pack Lists;
- add/remove game objects without deleting their authoring entries;
- object counts grouped by type and status;
- readiness percentage;
- missing dependency list;
- duplicate ID and conflicting-version detection;
- unresolved validation warnings;
- object ordering and grouping;
- Pack List notes, intended audience, source set, dependencies, and target schema;
- preview of the future pack manifest;
- export of the Pack List as review JSON;
- later compilation into a final `.pack` once the canonical compiler is available.

## Dual-save behavior

Saving from a builder must perform one transaction:

1. save/update the authoring entry;
2. generate/update the normalized game object;
3. run local validation;
4. optionally add the object to selected Pack Lists;
5. record the revision and validation results;
6. show both outputs to the user.

The interface should clearly distinguish:

- **Entry view** — readable, editable design record;
- **Object view** — structured game data;
- **Pack view** — grouped release preparation.

## Validation levels

- **Draft validation:** required concepts and minimum fields.
- **Object validation:** schema shape, types, IDs, enums, references.
- **Rules validation:** incompatible mechanics, missing resources/actions/effects, unresolved scaling.
- **Pack List validation:** dependency closure, duplicates, version conflicts, prohibited objects, missing provenance.
- **Pack compilation validation:** manifest, checksums, stable paths, installation/uninstallation behavior, final schema compliance.

## Mobile UX principles

- short guided steps;
- plain-language questions with examples from Multiversal;
- expandable advanced fields;
- searchable selectors for existing game objects;
- save-and-resume at every step;
- visible completion and validation state;
- no giant undifferentiated form;
- preview the resulting object before adding it to a Pack List;
- permit fast idea capture, followed by later completion through the same builder.

## Implementation priority

1. Pack List data model and workspace.
2. Shared authoring-entry/game-object lifecycle.
3. Ability builder.
4. Creature/NPC builder.
5. Item and vehicle builders.
6. Species builder.
7. World/environment builder.
8. Quest, scene, dialogue, and relationship builders.
9. Cross-object validation and dependency graph.
10. Canonical `.pack` compiler integration when the final Multiversal pack schemas and compiler are bound.
