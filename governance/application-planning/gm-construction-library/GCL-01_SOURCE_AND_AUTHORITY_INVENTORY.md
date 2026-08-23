# GCL-01 — Source and Authority Inventory

**Work item:** GCL-01 — Construction Taxonomy & Reusable Template Grammar  
**Attempt:** GCL-01-attempt-001  
**Classification:** governed design foundation  
**Status:** in progress

## Purpose

This inventory establishes the authority boundaries that the GCL shared grammar must preserve. It is not a new gameplay authority and does not reinterpret completed source systems.

## Controlling GCL source

`GCL_GM_CONSTRUCTION_LIBRARY_PROGRAM.md` requires GCL-01 to define template families, shared metadata, compatibility, slot semantics, provenance, dual ready-to-use/construction-material projections, composition contracts and an import/export shape. GCL is reusable GM construction substrate, not a Campaign Builder, Encounter Builder, AutoGM, Plot Lab, canon system or universal balance authority.

## Authorities consumed

### Campaign, Scene and Session authority — MV-IA-F005

GCL inherits the separation between reusable Definitions, Campaign-local placements/bindings and live Session state. A reusable GCL record may be selected by stable identity and adapted into a Campaign-local draft, but the GCL record itself does not become Campaign, Scene or Session truth. Launch snapshots and live Session state remain owned by F005 and downstream runtime authorities.

Required carry-forward rules:

- stable IDs and explicit versions;
- source Definition versus local placement separation;
- local overrides never mutate source Definitions;
- visibility and hidden-information scope remain explicit;
- incorporation into Campaign/Scene state requires an owning-domain action;
- AI/proposal material has no launch authority.

### Encounter composition and advisory authority — MV-IA-F012

GCL may supply encounter archetypes, objectives, complications, difficulty-shaping suggestions and later adversary role kits, but F012 owns Encounter draft composition analysis, comparison, approval and Scene attachment.

Required carry-forward rules:

- no single difficulty number may certify an encounter;
- evidence quality, uncertainty, assumptions and omitted variables remain visible;
- source Definitions remain immutable;
- local normalization cannot become canon;
- approval/attachment remains explicit human action in the owning domain;
- hidden content is filtered before serialization or recommendation.

### Encounter methodology — PPIA-11

GCL-01 adopts the PPIA-11 factor families as referenced pressure dimensions rather than converting them into weights or a scalar. In particular, action economy, output pressure, survivability/recovery, resources, range/mobility/access, environment/terrain, objectives/time/failure, hazards, mixed scale, waves/escalation, retreat alternatives, information/uncertainty and provenance remain independently visible.

GCL difficulty records may reference these factors later; GCL-01 does not assign universal weights, target scores or guaranteed outcome bands.

### Creator/GM assistance authorities

GCL is designed to feed CSW inspiration/guided creation/plot-adventure workflows, Campaign/Scene/Session preparation, Encounter Builder, AutoGM and future ISE/WCI consumers. Those systems remain owners of their respective workflows and runtime state. GCL exports reusable proposals and construction material only.

## GCL-01 authority model

A GCL template has three independent concepts that must never be conflated:

1. **Library authority** — whether the reusable record itself is an approved GCL library record, draft, retired variant or synthetic fixture.
2. **Content provenance** — whether individual material is source-backed fact, authored reusable template material, GM-authored customization, AI-generated candidate, Campaign-local adaptation, canonical/promoted content from an external owning domain, or synthetic fixture data.
3. **runtime/canon authority** — remains external to GCL and requires explicit incorporation/promotion by the owning domain.

An approved GCL library record therefore still has no automatic Campaign, Scene, Encounter, Session or canon authority.

## GCL-01 nonauthorization

This tranche does not authorize:

- GCL-02 or later production library quantities;
- runtime Campaign/Scene/Encounter/Session mutation;
- new universal gameplay mechanics;
- a universal Challenge Rating or balance scalar;
- automatic hidden-information access;
- entitlement bypass;
- automatic AI filling of missing source facts;
- automatic canon promotion or publication;
- silent conflict reconciliation or source correction.

## Foundation outputs

GCL-01 is complete only when the governed branch contains mutually consistent artifacts for:

- stable construction-family taxonomy;
- common reusable-template grammar/schema;
- typed slot and compatibility semantics;
- provenance and authority classification;
- ready-to-use and construction-material projections;
- composition and derivation lineage;
- versioned import/export package behavior;
- synthetic proof fixtures that exercise the grammar without becoming production library content;
- exact-head repository-health validation and review receipt.
