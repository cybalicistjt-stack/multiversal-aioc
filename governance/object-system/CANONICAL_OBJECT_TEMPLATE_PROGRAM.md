# Canonical Object Template Program

**Milestone:** 8E-009  
**Status:** ACTIVE — OWNER APPROVED  
**Owner and final authority:** John Brandon Turner  
**Repository:** `cybalicistjt-stack/multiversal-aioc`  
**Last updated:** 2026-08-04

## Objective

Build the canonical object-family hierarchy, parameter sets, capability modules, templates, validators, Design Studio form definitions, representative examples, and governed conversion pipeline required before bulk source-to-object promotion resumes.

## New source strategy

A structured CSV bundle supplied by the owner materially changes the execution path. The project must now use a **CSV-first, source-verified intake model**:

- preserve the original CSV bundle as immutable source evidence;
- use CSV rows as the initial structured extraction layer;
- use source PDFs for verification, missing fields, images, ambiguous mechanics, and field-level provenance;
- never treat a CSV row as canonical merely because it is structured;
- never silently repair, default, merge, or promote unsupported values.

This replaces most PDF-by-PDF manual extraction with controlled audit, mapping, reconciliation, validation, and enrichment. The canonical template architecture remains mandatory.

## Mandatory sequencing rule

Never begin large-scale conversion or canonical promotion for an object family until its canonical template, mapping contract, validation rules, representative examples, staging behavior, and owner approval exist.

## Revised execution sequence

1. Preserve the original CSV bundle and generate an immutable file manifest with hashes, encodings, delimiters, row counts, column counts, and source status.
2. Run a complete CSV data-quality and source-fidelity audit.
3. Register every CSV against its canonical domain and identify mixed-domain files.
4. Measure corpus coverage against the current type hierarchy, templates, fields, capability modules, and validators.
5. Reconcile genuine hierarchy or template gaps before record conversion.
6. Define deterministic, versioned CSV-column-to-canonical-field mapping contracts.
7. Build a cross-file identity, overlap, variant, and deduplication index.
8. Reconstruct representative objects from CSV rows plus exact PDF evidence and field-level provenance.
9. Run a bounded 50–100 record pilot across simple, complex, overlapping, magical, technological, living, modular, storage, consumable, and material objects.
10. Correct systemic mapping, parsing, provenance, classification, unit, identity, and runtime failures.
11. Freeze version 1 of the intake and mapping contracts.
12. Convert by bounded domain batches with validation reports and ambiguity queues.
13. Promote only records that pass all canonical, provenance, deduplication, runtime, staging, and owner-approval gates.

## Sub-phases

- **8E-009A — Object Family Discovery** — substantially complete for the item domain.
- **8E-009B — Canonical Type Hierarchy** — item hierarchy established; CSV coverage reconciliation pending.
- **8E-009C — Shared Capability Modules** — item capability registry established; frequency and coverage verification pending.
- **8E-009D — Item Template Registry** — initial 11-template registry established; CSV gap analysis pending.
- **8E-009E — Creature Template Registry**
- **8E-009F — NPC Template Registry**
- **8E-009G — Vehicle Template Registry**
- **8E-009H — World and Setting Template Registry**
- **8E-009I — Design Studio Dynamic Form Registry** — initial item forms established.
- **8E-009J — Canonical Validators** — initial item validators and completion scoring established.
- **8E-009K — Gold-Standard Example Objects** — source-backed selections underway.
- **8E-009L — Bulk Conversion Framework** — revised to begin with CSV intake governance, mapping contracts, deduplication, and pilot conversion.

## Current item foundation

Repository-backed item work already includes:

- authoritative PDF source inventory and family discovery;
- canonical item type hierarchy;
- shared capability-module registry;
- initial 11-template Item Template Registry;
- item validators and completion scoring;
- schema-driven Item Design Studio form registry;
- representative-object evidence and selection plans;
- source-backed example selection work, including rendered-page firearm verification.

These artifacts remain the architectural authority. The CSV bundle is structured source input that must be audited and mapped into them.

## Expected CSV domain routing

The intake registry must distinguish at least:

- melee, ranged, firearm, energy weapon, ammunition, and weapon-modification records;
- armor, shields, powered armor, EVA suits, and EVA modules;
- ordinary items, storage, consumables, tools, traps, deployables, and devices;
- computers, components, programs, software, networking, automation, and AI functions;
- magic implements, charge holders, spell storage, magitech items, and magitech disciplines;
- living spellbooks, sentient items, symbiotes, cybernetics, implants, and bonded objects;
- materials, components, fuels, catalysts, bases, facilities, and services;
- vehicles, mecha, spacecraft, and their components;
- spells and abilities, which must route to their existing canonical systems rather than the ordinary item converter.

Clones are not item objects. Clone bodies and identities belong to a separate artificial-being/clone family; cloning devices, facilities, services, and modifications are modeled separately.

## Universal object envelope

Every governed object must support stable identity, display name, object type and subtype, lifecycle stage, description, tags, source provenance, field-level provenance, relationships, governance state, owner-review state, unresolved ambiguities, and version/migration metadata.

## Template registry contract

Each template must define its template ID, display name, parent family, required and optional fields, allowed capability modules and subtypes, compatible modifications, source-supported parameters, validation and completion rules, Design Studio sections, runtime behaviors, known ambiguities, and at least one representative source-backed object.

## CSV mapping contract

Every registered CSV must define:

- source file and immutable file hash;
- source status and provenance expectations;
- row identity fields;
- column-to-canonical-field mapping;
- deterministic transformations;
- unit and value parsers;
- classification rules;
- direct, deterministic-mapped, inferred, owner-resolved, and unresolved evidence states;
- duplicate and variant matching rules;
- rejected or out-of-domain row routing;
- validation and completion effects;
- exact registry and mapping fingerprints.

## Promotion gates

A CSV-derived record may not become canonical unless it has:

- stable identity;
- successful canonical classification;
- required-field coverage;
- field-level source evidence;
- no unresolved blocking ambiguity;
- resolved duplicate/variant status;
- template and runtime validation where applicable;
- staging PASS;
- exact registry and mapping fingerprints;
- owner approval.

A structured row or JSON wrapper is not a complete object.

## Current next executable action

Begin **8E-009L1 — Governed CSV Intake and Data-Quality Audit**:

1. preserve the supplied CSV bundle;
2. create its immutable manifest;
3. inventory every CSV and its headers;
4. measure row/column counts and populated-field rates;
5. detect duplicate identities, malformed values, mixed object types, inconsistent categories, source-reference gaps, and cross-file overlaps;
6. classify each dataset as usable as-is, usable after normalization, source-verification required, or unsuitable for bulk import;
7. produce the initial CSV Source Registry and Item Template Coverage Matrix.

Do not begin mass conversion until this audit, mapping contracts, representative examples, bounded pilot, staging validation, and owner approval are complete.
