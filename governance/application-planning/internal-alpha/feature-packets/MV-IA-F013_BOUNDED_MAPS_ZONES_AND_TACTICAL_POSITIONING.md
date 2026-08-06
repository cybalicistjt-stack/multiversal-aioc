# MV-IA-F013 Bounded Maps, Zones, and Tactical Positioning

**Work item:** IA-D06-003  
**Program:** MV-IA-001  
**Owner:** John Brandon Turner  
**Status:** implementation-ready bounded design; dependency-gated  
**Version:** 0.1.0

## 1. Purpose

Define a bounded internal-alpha positioning system that supports uploaded maps or accessible abstract zones without making advanced map creation, precision token placement, or visual geometry a prerequisite for play.

## 2. Governing principle

Semantic position is authoritative. Images, pixels, token coordinates, line routing, zoom, and decoration are presentation data unless a bound rules profile explicitly converts them into validated semantic state.

## 3. Alpha scope

The alpha supports map upload, zone-only play, mixed map-plus-zone play, participants, zones, adjacency, distance bands, elevation bands, cover, hazards, visibility, movement paths, range checks, area templates, annotations, and accessible nonvisual alternatives.

## 4. Explicit deferrals

Advanced map generation, procedural terrain, 3D scenes, physics, dynamic lighting simulation, pathfinding optimization, fog painting, large-world streaming, and vendor map marketplaces remain deferred. No paid map service is required.

## 5. Dependencies

MV-IA-F002 object experience, F005 Campaign/Scene/Session, F006 Action approval, F007 combat, F008 Assets, F020 permissions, F021 recovery, and shared graph/list accessibility contracts.

## 6. Core records

- Map/Visual Asset Reference
- Positioning Profile
- Zone Definition and Zone Instance
- Adjacency Edge
- Participant Position
- Movement Proposal and Path Snapshot
- Range/Reach Evaluation
- Visibility/Concealment Evaluation
- Cover and Elevation State
- Hazard/Environment Placement
- Area Template Snapshot
- Annotation and Note
- Viewport/Token Presentation Preference

## 7. Map modes

Supported modes are `zone-only`, `image-with-zones`, `image-with-semantic-anchors`, and `accessible-outline`. A Scene may switch presentation mode without rewriting authoritative positions.

## 8. Zones

Zones have stable identities, labels, type, capacity guidance, adjacency, distance bands, elevation, cover, environment tags, access restrictions, and role-safe descriptions. Zone shape and screen size do not determine rules unless explicitly bound.

## 9. Adjacency and distance

Adjacency is a typed directional or bidirectional edge. Distance may be exact units, bands, steps, or profile-defined abstract values. Visual closeness cannot override authoritative adjacency or distance.

## 10. Participant position

A participant occupies a zone, semantic anchor, or bounded multi-zone footprint according to profile. Presentation coordinates may be stored per device or shared view, but cannot silently mutate the semantic position.

## 11. Movement

Movement proposals include actor, origin, destination, path/edge sequence, movement mode, cost, hazards, restrictions, reactions, and expected versions. Accepted movement commits atomically with costs and triggered Effects. Dragging is optional presentation input, never the only movement method.

## 12. Range, reach, and targeting

Range and reach derive from authoritative position, adjacency, distance profile, elevation, cover, visibility, Action source/version, and target state. Client previews are advisory until server validation. Hidden targets and zones cannot be enumerated through previews or failed range checks.

## 13. Visibility and hidden information

Visibility, concealment, darkness, detection, line/zone access, secret doors, hidden zones, hidden participants, and GM annotations are server-filtered before maps, lists, counts, search, minimaps, exports, diagnostics, notifications, or optional-AI context are generated.

## 14. Cover and elevation

Cover and elevation are semantic values with source/version provenance. Artwork, token overlap, or apparent line-of-sight cannot automatically create cover or elevation. Profiles define modifiers and interactions.

## 15. Hazards and environments

Hazards bind to zones, anchors, edges, paths, or scheduled pulses. Environment adaptations, movement restrictions, visibility changes, damage, Conditions, and Resource consequences use owning processors and exact versions.

## 16. Area templates

Areas use deterministic semantic snapshots: selected origin, affected zones/anchors, profile, orientation where relevant, and target set. Visual shapes assist understanding but the committed affected set is authoritative.

## 17. Annotations and notes

GM, shared, and private annotations are separate records with explicit audience. Drawing, pins, labels, measurements, and notes do not become rules truth or reveal hidden content without an authorized semantic binding.

## 18. Asset and vehicle integration

Map visuals, tokens, terrain Assets, containers, and vehicles retain F008 ownership/custody/access authority. Positioning controls location and participation only. A vehicle footprint and crew stations remain typed adapters rather than duplicated Asset records.

## 19. Combat integration

F007 owns encounter order, Action resolution, reactions, Effects, and results. F013 supplies validated semantic positioning snapshots and movement/range/visibility evaluations. Positioning cannot directly apply damage, consume Resources, or resolve Actions.

## 20. Accessibility

Every map operation has list, outline, table, relationship/adjacency, text-route, keyboard, screen-reader, touch, and nonvisual alternatives. Focus order, current zone, neighbors, occupants, hazards, routes, range, and change announcements are deterministic. Color, geometry, animation, hover, and drag are never sole carriers.

## 21. Responsive and performance boundaries

Mobile supports full semantic operation without precision zoom or canvas manipulation. Large maps use bounded neighborhoods, virtualization, progressive visual loading, and server-authorized summaries. Partial visual loading cannot imply partial authoritative state.

## 22. Recovery and concurrency

Movement, zone edits, visibility changes, and annotations use idempotency keys and expected versions. Lost responses require status lookup before retry. Reconnect restores semantic position, active movement/reaction windows, role-safe topology, and Event gaps. Offline authoritative mutation is prohibited.

## 23. Pack, export, diagnostics, and optional AI

Pack update cannot rewrite live zones or positions. Removal preserves snapshots and tombstones. Exports and diagnostics use identical role-safe projections. AI may summarize authorized zones or draft route suggestions only; it cannot reveal hidden topology, move participants, resolve range, commit Events, or create canonical maps.

## 24. Implementation and acceptance boundary

Implementation proceeds through eight slices and twenty-four deterministic fixtures. All twenty-eight acceptance criteria are blocking. Design completion authorizes no advanced map platform, paid service, credential, real-user data collection, application activation, internal-alpha release, deployment, public release, or canonical promotion. `P9-06-008-attempt-002` remains unfinished and unmodified.

## Implementation slices

1. Positioning profiles, map modes, zones, anchors, and stable identities.
2. Adjacency, distance, elevation, cover, environment, and hidden projections.
3. Participant position, movement proposals, paths, costs, and reactions.
4. Range, reach, visibility, targeting, and deterministic area snapshots.
5. Hazards, annotations, map/Asset adapters, and vehicle footprint boundary.
6. Accessible responsive views and bounded performance behavior.
7. Recovery, idempotency, pack lifecycle, exports, diagnostics, and AI boundaries.
8. Deterministic fixtures, acceptance harness, and vehicle handoff.

## Next work item

IA-D06-004 — basic MV-IA-F014 Vehicle, Mecha, and Starship Operations.
