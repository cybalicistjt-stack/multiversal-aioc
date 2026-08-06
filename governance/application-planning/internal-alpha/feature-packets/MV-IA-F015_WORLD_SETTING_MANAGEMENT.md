# MV-IA-F015 — World and Setting Management

**Work item:** IA-D07-001  
**Owner:** John Brandon Turner  
**Status:** COMPLETE DESIGN / IMPLEMENTATION-READY  
**Boundary:** Internal-alpha design only; implementation remains dependency-gated by P9-06.

## Purpose

Define the authoritative internal-alpha experience for creating, organizing, versioning, permissioning, linking, importing, exporting, and using Worlds and Settings without conflating canonical source material, Campaign-local adaptations, unpublished drafts, or Player-visible projections.

## Core model

A `World` is a stable governed container for setting material. A `SettingEntry` is a versioned object within a World. Entries may represent regions, settlements, cultures, species, organizations, environments, histories, calendars, cosmology, technology levels, magic paradigms, laws, languages, currencies, travel networks, hazards, encounters, Assets, Creatures, NPCs, Adventures, and reference media.

Every object has a stable ID, exact source/version provenance, lifecycle state, visibility policy, authority owner, parent World, optional Campaign-local overlay, dependency references, and tombstone behavior.

## Lifecycle

Worlds and entries move through `draft`, `review`, `approved`, `published`, `deprecated`, `disabled`, and `tombstoned`. Publishing does not imply canonical promotion outside the governed repository. Campaign-local overlays never silently rewrite source entries.

## Authority and permissions

Creation, edit, review, publish, deprecate, import, export, reveal, and delete are independent permissions. Hidden entries are filtered before search, counts, maps, graph edges, exports, diagnostics, notifications, and optional-AI context. Players see only authorized projections; GMs may maintain secret facts, unrevealed variants, and future-state notes.

## Structure and linking

Worlds support folders, tags, typed relations, semantic geography, timelines, calendars, dependency graphs, and cross-entry references. Relations are typed and directional. Deleting or disabling a source never silently destroys dependent history; references become governed tombstones with remediation guidance.

## Editing and versioning

All mutations use expected versions and idempotency keys. Autosave creates bounded drafts. Explicit publish creates immutable version snapshots. Conflicts return current versions and field-level merge guidance. Reconnect uses snapshot-plus-tail recovery.

## Campaign-local overlays

Campaigns may pin a source version and layer local additions, redactions, renamed labels, state changes, secrets, and consequences. Overlays preserve source identity and record divergence explicitly. A Campaign may later adopt a newer source version through a reviewed migration, never an automatic rewrite.

## Import, export, and pack lifecycle

Imports require schema validation, stable-ID collision handling, provenance, dependency inspection, permission review, and bounded preview. Exports are role-filtered and include exact versions and checksums. Pack disablement blocks new use but preserves prior interpretation through snapshots and tombstones.

## Accessibility

World management must support list, tree, table, detail, timeline, semantic map outline, keyboard, touch, screen reader, high contrast, reduced motion, responsive layouts, and nonvisual operation parity. Dragging, canvas precision, color, hover, or animation is never required.

## Optional AI boundary

AI may summarize, suggest tags, propose links, detect gaps, or draft text only when authorized. AI receives permission-filtered context, records provenance and cost, cannot publish or reveal hidden information, and must degrade safely when unavailable.

## Implementation slices

- WSM-S01 — World, entry, lifecycle, and version foundations.
- WSM-S02 — hierarchy, tags, typed relations, and semantic geography.
- WSM-S03 — permissions, hidden-information projection, and reveal controls.
- WSM-S04 — draft, review, publish, conflict, and migration flows.
- WSM-S05 — Campaign-local overlays and source-version pinning.
- WSM-S06 — import, export, pack lifecycle, provenance, and tombstones.
- WSM-S07 — accessibility, search, diagnostics, and recovery.
- WSM-S08 — deterministic fixtures, observability, and implementation handoff.

## Acceptance

WSM-AC-001 through WSM-AC-028 are blocking and enumerated in the readiness record. Zero blocking findings remain.

## Exclusions

No deployment, public release, paid service, production credential, real-user data, irreversible deletion, autonomous AI publication, or canonical promotion is authorized. `P9-06-008-attempt-002` remains unfinished and unmodified.

## Decision

IA-D07-001 is implementation-ready. The next work item is **IA-D07-002 — MV-IA-F017 Adventure and Module Management**.