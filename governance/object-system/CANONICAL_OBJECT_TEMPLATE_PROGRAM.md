# Canonical Object Template Program

**Milestone:** 8E-009  
**Status:** ACTIVE — OWNER APPROVED  
**Owner and final authority:** John Brandon Turner  
**Repository:** `cybalicistjt-stack/multiversal-aioc`

## Objective

Build the canonical object-family hierarchy, parameter sets, capability modules, templates, validators, Design Studio form definitions, and gold-standard examples required before bulk source-to-object conversion resumes.

## Mandatory sequencing rule

Never begin large-scale extraction or conversion for an object family until its canonical template, validation rules, and representative examples exist.

Required order:

1. Discover object families from source material.
2. Separate objects from actions, effects, rules, facilities, services, modifications, materials, creatures, and artificial beings.
3. Build the canonical type hierarchy.
4. Extract every source-supported parameter by family.
5. Normalize reusable capability modules without erasing domain meaning.
6. Assemble family templates from those modules.
7. Define field-level provenance and completion requirements.
8. Build validators.
9. Build schema-driven Design Studio forms.
10. Create gold-standard example objects.
11. Pilot conversion in staging.
12. Resume bulk conversion only after owner approval.

## Sub-phases

- **8E-009A — Object Family Discovery**
- **8E-009B — Canonical Type Hierarchy**
- **8E-009C — Shared Capability Modules**
- **8E-009D — Item Template Registry**
- **8E-009E — Creature Template Registry**
- **8E-009F — NPC Template Registry**
- **8E-009G — Vehicle Template Registry**
- **8E-009H — World and Setting Template Registry**
- **8E-009I — Design Studio Dynamic Form Registry**
- **8E-009J — Canonical Validators**
- **8E-009K — Gold-Standard Example Objects**
- **8E-009L — Bulk Conversion Framework**

## Immediate active scope

Begin with the Item Template Registry using all available item-related source PDFs, including weapons, firearms, armor and shields, EVA suits, computers, living spellbooks, magic charge holders, magitech, materials, symbiotes, miscellaneous items, and related sources already supplied.

Initial item families include:

- melee weapons;
- ranged weapons;
- firearms;
- energy weapons;
- ammunition;
- armor;
- shields;
- powered armor;
- EVA suits;
- ordinary containers;
- fluid containers;
- extra-dimensional storage;
- charge holders;
- spell-storage items;
- consumables;
- potions;
- poisons;
- oils and coatings;
- powders and dusts;
- scrolls;
- spell orbs;
- mundane tools;
- scanners and sensors;
- communication and navigation devices;
- medical and crafting devices;
- traps and deployables;
- computers;
- computer modules;
- software;
- wands;
- staves;
- rods;
- tomes;
- spellbooks;
- living spellbooks;
- charms;
- talismans;
- rings;
- relics;
- modular upgrades;
- magitech devices and disciplines;
- sentient items;
- symbiotes;
- raw and refined materials;
- crafting components;
- fuels and catalysts.

Clones are not item objects. Clone bodies and identities belong to a separate artificial-being/clone family; cloning devices, facilities, services, and modifications are modeled separately.

## Universal object envelope

Every governed object must support:

- stable identity;
- display name;
- object type and subtype;
- lifecycle stage;
- description;
- tags;
- source provenance;
- field-level provenance where available;
- relationships;
- governance state;
- owner-review state;
- unresolved ambiguities;
- version and migration metadata.

## Template registry contract

Each template must define:

- template ID;
- display name;
- parent family;
- required fields;
- optional fields;
- allowed capability modules;
- allowed subtypes;
- compatible modifications;
- source-supported parameters;
- validation rules;
- completion scoring;
- Design Studio sections;
- runtime behaviors;
- known ambiguities;
- at least one complete representative object.

## Completion standard

An object is not complete merely because a JSON body exists. Completion is measured against required and source-supported fields. Empty wrappers containing only identity, type, stage, and provenance must remain classified as stubs.

## Current next executable action

Complete **8E-009A — Item Family Discovery** by inventorying all available item-related sources and producing the first governed item-family hierarchy and parameter matrix.
