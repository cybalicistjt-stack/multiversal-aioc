# IA-D07-002 — MV-IA-F017 Adventure and Module Management

**Program:** MV-IA-001  
**Owner:** John Brandon Turner  
**Status:** COMPLETE DESIGN / IMPLEMENTATION-READY  
**Boundary:** Internal-alpha design only; implementation remains dependency-gated by P9-06.

## Purpose

Define a governed authoring and runtime contract for adventures, modules, chapters, scenes, encounters, investigations, rewards, prerequisites, branching outcomes, reusable content references, and campaign instantiation.

## Core model

`Adventure`, `AdventureVersion`, `ModuleNode`, `ModuleEdge`, `ModuleBinding`, `ModuleRun`, and `ModuleRunEvent` use stable identifiers. Published versions are immutable. Drafts, reviewed candidates, published releases, deprecated releases, campaign instances, and tombstones are distinct states.

## Authority

Create, edit, review, publish, instantiate, reveal, advance, rewind by compensating event, export, import, deprecate, and delete are separate permissions. AI may suggest content but cannot publish, reveal, or advance authoritative state.

## Structure and branching

Typed nodes include chapter, scene, encounter, social challenge, investigation, travel, downtime, choice, gate, reward, and ending. Edges declare prerequisites, visibility, transition effects, repeatability, failure behavior, and fallback routing. Branch evaluation is server-authoritative and versioned.

## Runtime

Campaign runs pin exact adventure versions and create run-local state rather than mutating source definitions. Progression, scene activation, clue discovery, encounter results, rewards, consequences, and branch choices commit through atomic authoritative result groups.

## Hidden information

Unrevealed nodes, branches, prerequisites, outcomes, rewards, clues, NPCs, maps, and future scenes are filtered before search, counts, graph views, exports, diagnostics, notifications, previews, and optional-AI context.

## Reuse and dependencies

Modules may reference World entries, Characters, Creatures, Items, Vehicles, Maps, Factions, Rules Profiles, and other modules through versioned bindings. Dependency previews identify missing, incompatible, hidden, or deprecated references before publish or instantiate.

## Import, export, and provenance

Imports use collision-safe identifiers and explicit mapping. Exports are role-filtered and provenance-complete. Historical runs retain exact source IDs, versions, checksums, and bounded snapshots.

## Accessibility

List, outline, table, detail, timeline, branch graph, semantic map outline, keyboard, touch, screen-reader, responsive, high-contrast, reduced-motion, and nonvisual operation have semantic parity.

## Recovery

Mutations use idempotency keys and expected versions. Lost responses require status lookup. Event gaps trigger bounded snapshot-plus-tail repair. Reversal uses compensating events; history is never silently rewritten.

## Implementation slices

AM-S01 identities and lifecycle; AM-S02 node/edge authoring; AM-S03 dependency bindings; AM-S04 publish/review; AM-S05 campaign instantiation/runtime; AM-S06 hidden projections/accessibility; AM-S07 import/export/recovery; AM-S08 fixtures and handoff.

## Decision

IA-D07-002 is implementation-ready. The next work item is **IA-D07-003 — bounded MV-IA-F018 Creator and Campaign-local Content**. `P9-06-008-attempt-002` remains unfinished and unmodified.