# MSLR — Multiversal Spatial Law Runtime

**Program ID:** MSLR  
**Status:** OWNER-APPROVED — PLANNED  
**Activation:** after MBES-24 under `ROADMAP_DEPENDENCY_GRAPH.json`  
**Successor:** MSWI-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-15

## Purpose

MSLR turns Multiversal's existing non-standard spatial representation into reusable gameplay. It consumes completed SSA topology semantics, ENV multiversal/environment context, MCS cartographic projections, GPR execution primitives and MBES built-space definitions. It does not replace any of them.

The family exists because Multiversal must support more than visually unusual maps. Campaigns may contain non-Euclidean adjacency, looping and shifting labyrinths, fuzzy Reality borders, dimensional bleed without traversable portals, nested or bigger-inside spaces, recursive scale, local gravity/orientation changes, curved or distorted distance metrics, observer-dependent connections, memory/knowledge-dependent routes, temporal or dream spatial laws, and spaces whose true topology cannot be represented faithfully by a single Euclidean map.

The design principle is: **impossible space should have discoverable laws rather than arbitrary behavior.** Players need ways to observe, hypothesize, test, map, exploit, resist, stabilize and sometimes alter those laws. Abstract checks remain supported, but they are not the only interaction model.

## Placement

Effective planned sequence for this portion of the roadmap:

`GPR → MERA → MBES → MSLR → MSWI → SMB-08`

The placement is deliberately after MBES rather than between GPR and MERA. MSLR benefits from the completed gameplay runtime, map/spatial semantics, environment overlays and the full built-environment vocabulary. MSWI then consumes MSLR's typed spatial events and observations when propagating consequences into world systems.

## Tranche execution contract

Each tranche targets a 24-minute total execution envelope with at least 8 minutes reserved for focused validation, durable-evidence verification, reconciliation and successor marking. Active implementation scope is therefore capped at 16 minutes by design unless a tranche is split before governed start. Once governed-started, one owner `Continue` carries the whole bounded tranche through closeout unless an OPS3 owner-only boundary or genuine external blocker is reached.

## Tranches

### MSLR-01 — Spatial-Law Authority, Capability Crosswalk & Runtime Contract

Define the owner-domain crosswalk across SSA, ENV, MCS, GPR, MBES, World/Reality, Scene, Exploration, Transition/Portal, Visibility/Knowledge and Action/Event. Establish the runtime boundary between reusable spatial-law definitions and live Campaign spatial state.

Acceptance: no duplicate spatial ledger; authoritative owner for every input/output is explicit; spatial-law definition and live state are separate; unsupported concepts remain unresolved rather than invented.

### MSLR-02 — Spatial-Law Profiles, Scope, Invariants, Discoverability & Composition

Define a reusable profile describing which spatial dimensions are non-standard: topology, metric, orientation, containment/scale, layer overlap, observer predicates, temporal recurrence, stability and discoverability. Profiles declare invariants, triggers, clues, counterplay and resolution modes.

Acceptance: normal Euclidean space is a valid default; profiles may compose without collapsing dimensions; profile scope is explicit; contradictory laws fail deterministically or require an authored resolution rule.

### MSLR-03 — Dynamic Topology State, Edge Mutation, Event Trace, Replay & Recovery

Add live state for active edges, redirected exits, permutations, folds, collapsed links, phase relationships and law-state variables. Changes occur through typed events with source, time, reversibility and version data.

Acceptance: topology can change without rewriting reusable Location/World definitions; replay/recovery reconstructs the same declared-deterministic state; stale or unauthorized mutation is rejected.

### MSLR-04 — True, Observable, Known & Suspected Topology Projections

Separate authoritative topology from currently observable topology, participant-known topology and player-authored/suspected topology. Permission filtering occurs before counts, search, route diagnostics, AI context and export.

Acceptance: a player can possess an incomplete or wrong map without corrupting true topology; hidden edge cardinality does not leak; multiple participants may legitimately hold different knowledge projections.

### MSLR-05 — Spatial Observation, Hypothesis, Experiment & Law-Discovery Gameplay

Create gameplay operations for leaving marks, walking controlled routes, timing loops, comparing maps, testing thresholds, observing repetition, measuring distance, checking echoes, watching transitions and forming spatial hypotheses. Skill checks may expose clues or confidence but do not have to replace direct play.

Acceptance: a representative impossible space can be solved by accumulated observations and experiments; failed checks need not create dead ends; discoveries create governed knowledge/evidence state rather than rewriting the law.

### MSLR-06 — Governed Topology Operations, Triggers, Preview, Undo & Counterplay

Define shared operations such as connect, disconnect, redirect, permute, wrap, fold, unfold, nest, unnest, phase, collapse, stabilize and sever where owner contracts permit them. Support preview/counterfactual evaluation before commit.

Acceptance: spells, devices, environmental events, puzzles and GM operations may reuse the same typed spatial operations; undo/reversal obeys event/version constraints; presentation input alone cannot commit a topology change.

### MSLR-07 — Fuzzy Boundaries, Reality Seams, Bleed Gradients & Traversability Separation

Represent boundary regions as scoped mixtures or gradients rather than mandatory lines. Track which Reality/Environment properties overlap, their provenance and local stability. Preserve the existing ENV distinction between Reality Instability, Dimensional Bleed and Portal Activity.

Acceptance: a bleed can be perceptible and mechanically consequential without being traversable; a portal can exist without broad bleed; access/traversal remains Transition/Portal/Access-owned.

### MSLR-08 — Metric Geometry Profiles: Euclidean, Hyperbolic, Spherical & Distorted Distance

Add optional metric profiles distinct from topology. Govern distance, range, area, path length, line-of-sight and related calculations under Euclidean, hyperbolic, spherical, anisotropic or source-defined local-distortion rules.

Acceptance: non-Euclidean topology does not automatically change distance; metric changes are explicit and testable; tactical and abstract resolution use compatible semantic results without requiring identical visual rendering.

### MSLR-09 — Recursive Scale, Nested Worlds, Bigger-Inside & Containment Transforms

Extend containment with explicit scale relationships and transforms. Support pocket spaces, worlds within objects, interiors larger than exteriors, recursive structures and transitions between local scales while preserving stable entity/location identity.

Acceptance: `contains`, `nested in`, `same scale` and `bigger inside` remain distinguishable; carried/nested spaces do not duplicate their contents; exit/entry transforms are explicit and recoverable.

### MSLR-10 — Orientation, Gravity Frames, Surface-Local Up & Transition Semantics

Represent local orientation frames and changing gravity directions independently of map coordinates. Support surface-local up, rotating frames, zero-g transitions and authored reorientation at edges or zones.

Acceptance: movement, falls, projectiles and scene projections can consume a declared orientation frame; orientation change never silently changes location identity or topology.

### MSLR-11 — Observer, Knowledge, Memory & Perception-Dependent Connectivity

Allow explicit predicates where route availability or resolution depends on an observer state, possessed knowledge, remembered fact, sensory relationship or other owner-authorized participant context.

Acceptance: the predicate and authority source are explicit; client observation alone cannot self-authorize a route; memory/perception effects use owning participant/knowledge systems; accessibility-equivalent evidence is possible.

### MSLR-12 — Temporal, Dream, Causal, Looping & Recurrence Spatial Laws

Support loops, recurrence, reset points, time-dependent exits, oneiric/symbolic relationships and source-defined causal spatial rules. Keep Temporal Instability and Dream Influence as environment contexts rather than universal formulas.

Acceptance: a looping corridor or dream route can have a learnable condition for change/escape; recurrence preserves or resets only declared state; no universal time ratio or dream rule is invented.

### MSLR-13 — Anchors, Markers, Mapping, Stabilization, Navigation Aids & Counterplay

Define interactions for chalk/markers, ropes, beacons, memory anchors, clocks, drones, wards, stabilizers, route tokens and equivalent setting-specific aids. Spatial laws may preserve, move, duplicate, erase, corrupt or reject anchors only when authored.

Acceptance: navigation equipment and abilities can materially interact with spatial laws; counterplay creates decisions beyond repeated skill checks; anchors preserve provenance and ownership.

### MSLR-14 — Constraint-Driven Procedural Impossible-Space Generation & Solvability Proof

Generate semantic topology/laws from constraints before presentation. Support loop requirements, unstable edges, nested regions, gravity frames, false endpoints, layer overlap and authored invariants. Require reachability/solvability checks for required objectives before promotion.

Acceptance: seeded output is deterministic where declared; generated spaces cannot silently enter canonical state; required start/objective/escape constraints are machine-checkable; inaccessible or unsolved generations are rejected or surfaced for GM repair.

### MSLR-15 — Liminal Sensory Anomaly Grammar, Detection & Accessible Equivalent Cues

Define reusable cue families across sight, sound, touch, temperature, smell, text/signage, timing, repetition, social behavior and map contradiction. Separate cue evidence from hidden truth and support equivalent semantic cues for accessibility.

Acceptance: anomaly play does not require a single sensory channel; subtle cues can be authored without leaking the answer; player detection can feed MSLR-05 evidence/hypothesis state.

### MSLR-16 — Multi-Resolution & Cross-System Spatial Gameplay Runtime

Execute the same spatial law through abstract travel/theater-of-the-mind, topology/tactical views and rendered scenes. Integrate movement, combat, range, pursuit, stealth, vehicles/mounts, encounters, exploration, settlement access and other owner systems through GPR-compatible typed outcomes.

Acceptance: changing presentation mode does not change authoritative meaning; a representative law affects at least exploration, combat/movement and one non-combat system through explicit owner operations; no cross-system consequence is invented outside its owner.

### MSLR-17 — GM/Creator Spatial-Law Studio, Diagnostics, Simulation & Specialized Map Views

Provide authoring and diagnostic projections for law profiles, topology graphs, layer graphs, route histories, gravity frames, confidence/knowledge maps, contradiction overlays and solvability tests. MCS remains the cartographic/presentation owner.

Acceptance: creators can build and test an impossible space without editing raw state; diagnostics identify unreachable objectives, contradictory invariants, hidden-information leaks and unstable mutation cycles; all consequential authoring remains proposal/acceptance governed.

### MSLR-18 — Golden Impossible-Space Proof & MSWI Handoff

Prove the family with a clean-room scenario battery covering: non-adjacent topology, shifting/looping liminal maze, fuzzy Reality seam with nontraversable bleed, explicit metric distortion, recursive bigger-inside containment, gravity-frame transition, observer/knowledge-dependent route, topology manipulation, accessible anomaly discovery and deterministic procedural solvability.

Acceptance: exact-head validation passes; event/recovery proof is deterministic where declared; owner boundaries hold; MSLR observations/events/deltas are consumable by MSWI; no benchmark-specific protected expression appears in production artifacts.

## Golden design invariants

- Impossible does not mean arbitrary: authored/generated anomalous spaces expose consistent discoverable laws unless the source explicitly establishes nondeterminism.
- A map is a projection of spatial truth, not spatial truth itself.
- Topology and metric geometry are different dimensions.
- Fuzzy boundary and portal are different concepts.
- A participant may know less than the system without hidden truth leaking through diagnostics.
- A skill check may summarize spatial gameplay, but detailed interactive resolution must also be possible where the profile supports it.
- Spatial change must be attributable, recoverable and permission-checked.
- Accessibility preserves the puzzle by providing equivalent evidence, not by revealing protected answers.
- MSLR never creates a second World/Reality/Scene/Map/Environment ledger.
