# IA-D07-005 — Authoring Integration Review

**Owner:** John Brandon Turner  
**Status:** COMPLETE DESIGN / IMPLEMENTATION-READY  
**Boundary:** Internal-alpha design only; implementation remains dependency-gated by P9-06.

## Purpose

Integrate IA-D07-001 through IA-D07-004 into one coherent authoring and runtime model spanning Worlds and Settings, Adventures and Modules, Creator/Campaign-local Content, and cross-domain authority.

## Integrated model

Canonical source definitions, creator releases, Campaign-local objects, overlays, published adventures, Campaign runs, and historical tombstones retain stable identities, immutable published versions, exact provenance, explicit authority, and role-filtered projections.

## End-to-end authoring flow

1. Author creates a private draft.
2. Validation checks schemas, references, processor allowlists, dependencies, permissions, hidden-information behavior, and resource bounds.
3. Reviewer evaluates immutable proposal revisions and records rationale.
4. Authorized publisher creates an immutable release.
5. Campaign authority installs and pins an allowed release or canonical source version.
6. Local overlays express explicit differences without mutating upstream source.
7. Runtime authority reveals and advances Campaign state through atomic result groups.
8. Source updates require explicit reviewed migration.
9. Disablement blocks new use while snapshots and tombstones preserve history.
10. Canonical promotion remains an owner-only gate outside internal alpha.

## Integrated journeys

The review proves eight journeys: canonical World authoring to Campaign use; branching Adventure publication and run; creator Item proposal and install; Campaign-local Creature overlay; source migration with divergence; hidden GM content reveal; disabled pack with historical replay; and import/export with collision resolution.

## Domain adapters

Eleven adapters connect authoring to identity/versioning, permissions, proposal/review, Worlds, Adventures, Campaigns, Assets, combat, maps/vehicles, import/export, and Event/recovery infrastructure.

## Authority and integrity

Ownership, authorship, edit, review, publish, install, enable, reveal, runtime advance, export, import, deprecate, delete, and canonical-promotion authority remain distinct. Publish, install, migrate, reveal, advance, reward, disable, import, and export create one authoritative result group with expected versions and idempotency.

## Hidden information

Filtering occurs before search, counts, totals, dependency graphs, branch graphs, map outlines, previews, exports, diagnostics, notifications, and optional-AI context. Unauthorized absence cannot be distinguished from hidden presence through side channels.

## Accessibility

List, tree, table, detail, timeline, diff, dependency outline, branch graph, semantic map outline, review queue, keyboard, touch, screen-reader, responsive, high-contrast, reduced-motion, and nonvisual flows provide semantic parity.

## Recovery and lifecycle

Lost responses require status lookup before retry. Event gaps use snapshot-plus-tail repair. Conflicts return current versions and safe refresh instructions. Reversal uses compensating Events. Pack disablement/removal preserves exact historical interpretation.

## Implementation slices

AI-S01 shared identities and versions; AI-S02 authoring/review; AI-S03 publication/dependencies; AI-S04 Campaign installation/overlays; AI-S05 runtime reveal/advance; AI-S06 projections/accessibility; AI-S07 import/export/recovery; AI-S08 fixtures/implementation handoff.

## Decision

IA-D07 is complete and implementation-ready with zero blocking findings. The next canonical phase is **IA-D08 — Optional AI and experimental systems**. `P9-06-008-attempt-002` remains unfinished and unmodified.