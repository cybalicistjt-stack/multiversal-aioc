# IA-D08-003 — Advanced Map and Vehicle Deferral Package

**Owner:** John Brandon Turner  
**Status:** COMPLETE DEFERRAL DESIGN / IMPLEMENTATION-READY BOUNDARY  
**Boundary:** Internal-alpha design only; implementation remains dependency-gated by P9-06.

## Purpose

Define exactly which advanced map, tactical, vehicle, mecha, and starship capabilities are deferred beyond internal alpha, while preserving stable seams, safe data retention, user-facing expectations, and migration paths.

## Deferred map capabilities

Continuous freeform measurement, full 3D terrain, volumetric line of sight, dynamic lighting simulation, fog-of-war painting, physics-driven collision, real-time pathfinding across massive maps, procedural terrain generation, collaborative vector editing, high-volume animated tokens, GIS-grade coordinates, and unrestricted custom map scripts are deferred.

## Deferred vehicle capabilities

Continuous Newtonian flight, full orbital mechanics, subsystem circuit simulation, real-time crew station concurrency at scale, detailed power-grid routing, structural finite-element damage, atmospheric transition simulation, carrier fleet command, autonomous drones, programmable vehicle AI, full interior/exterior synchronized geometry, and unrestricted custom vehicle processors are deferred.

## Internal-alpha retained contract

Semantic zones, anchors, typed adjacency, bounded distance/elevation/cover, deterministic area snapshots, hazards, annotations, stable vehicle classes, stations, command authority, bounded Resources, damage states, docking/boarding, carried craft, hidden-information filtering, accessibility, provenance, and recovery remain supported.

## Deferral behavior

Deferred fields may be retained as opaque, versioned extension data but cannot affect authoritative resolution. Unsupported imported features produce explicit compatibility reports, preserved source payloads, and safe degradation. No silent approximation, data deletion, or unsupported processor execution is allowed.

## Upgrade seams

Stable extension namespaces, capability negotiation, schema-version ranges, processor allowlists, projection adapters, fixture reservations, migration receipts, and tombstones permit future implementation without rewriting historical results.

## User experience

The interface labels deferred capabilities, explains bounded alternatives, prevents configuration that appears active but is ignored, and offers export-preserving workflows. List and nonvisual alternatives remain available for every retained capability.

## Implementation slices

AMV-S01 capability registry; AMV-S02 import compatibility; AMV-S03 opaque extension retention; AMV-S04 degradation reports; AMV-S05 map upgrade seams; AMV-S06 vehicle upgrade seams; AMV-S07 accessibility/provenance; AMV-S08 fixtures/handoff.

## Decision

IA-D08-003 is implementation-ready as a deferral boundary. Next: **IA-D08-004 — broad offline deferral package**. `P9-06-008-attempt-002` remains unfinished and unmodified.