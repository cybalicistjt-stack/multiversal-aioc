# Multiversal Hybrid Extraction Pipeline v3.1

Status: Parallel evaluation; not canonical authority

## Purpose

Convert hierarchical source evidence into database-ready game-object candidates while preserving tables, forms, parent-child context, provenance, uncertainty, and human authority.

## Production sequence

1. Ingest authoritative PDFs and CSVs.
2. Normalize text and remove repeated boilerplate without destroying page provenance.
3. Reconstruct document hierarchy, reading order, tables, lists, and key-value structures.
4. Run deterministic extraction for reliable syntax: headings, named blocks, dice, DCs, ranges, costs, durations, stat labels, prerequisites, and explicit relationships.
5. Map evidence into family-specific schemas.
6. Route ambiguous blocks to an optional provider-neutral probabilistic extractor contract.
7. Run an independent verifier and normalizer.
8. Deduplicate by object identity plus source context, not bare headings.
9. Route low-confidence, conflicting, or incomplete records to human review.
10. Permit downstream staging only after schema, provenance, relationship, duplicate, and approval gates pass.

## Object schemas

Every candidate uses a common envelope:

- candidateId
- objectType
- name
- status
- authority
- provenance[]
- parentContext
- sourceEvidence[]
- extractionMethod[]
- confidence
- fieldConfidence
- specification
- relationships[]
- validation
- reviewRoute

Family-specific specifications are defined for rule, ability, creature, item, species, npc, vehicle, environment, world, faction, and adventure.

## Table and form reconstruction

Tables are retained as:

- tableId and source provenance;
- caption and surrounding heading path;
- header rows;
- ordered rows and cells;
- row/column spans where available;
- inferred column roles;
- cell confidence;
- key-value projections only when the relationship is defensible.

A flattened table row may provide evidence but cannot independently become an object identity.

## Hybrid extraction policy

Deterministic extraction is authoritative for explicit syntax. A probabilistic extractor may propose missing fields only when:

- the target schema is supplied;
- the exact evidence block is supplied;
- output is constrained to the schema;
- every field includes evidence spans and confidence;
- unsupported fields are null rather than invented;
- the result is independently verified.

No external model is required for the deterministic pipeline. Provider-specific inference is an optional adapter.

## Two-pass verification

The verifier must not reuse the extractor's conclusion as its sole evidence. It checks:

- identity validity and parent context;
- family consistency;
- schema conformance;
- required fields;
- evidence support for every populated field;
- value types and normalized units;
- table/header relationships;
- relationship targets versus scalar mechanics;
- duplicate and conflict indicators;
- provenance completeness.

## Review routes

- `ready-for-expert-sample`: high confidence, valid schema, complete evidence, no conflicts.
- `human-review`: plausible but ambiguous, incomplete, or verifier-disputed.
- `rejected-evidence-only`: heading, container, table fragment, boilerplate, or unsupported claim.

No route authorizes canonical ingestion.

## Evaluation gates

Before replacing Baseline v2, v3.1 must demonstrate:

- container and empty-heading identity rate below 0.5%;
- duplicate candidate rate below 2%;
- scalar values never emitted as relationship targets;
- at least five object families in the high-confidence sample;
- complete provenance for all candidates;
- schema-valid rate above 95% for the high-confidence tier;
- table reconstruction samples preserving headers and row associations;
- owner/expert acceptance of a stratified sample.
