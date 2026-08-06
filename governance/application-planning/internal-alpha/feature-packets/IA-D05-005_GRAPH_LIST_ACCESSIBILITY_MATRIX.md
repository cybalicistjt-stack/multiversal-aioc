# IA-D05-005 Graph/List Accessibility Matrix

**Program:** MV-IA-001  
**Work item:** IA-D05-005  
**Version:** 0.1.0  
**Status:** implementation-ready design; dependency-gated  
**Owner:** John Brandon Turner

## 1. Purpose

Define one cross-feature accessibility contract for relationship networks, faction structures, social participant/context relationships, and investigation clue boards. A visual graph may enhance comprehension, but no fact, status, action, warning, permission, or relationship may exist only through position, shape, color, animation, line routing, or drag interaction.

## 2. Covered consumers

- MV-IA-F009 Relationship Tracker;
- MV-IA-F016 Factions, Reputation, and Organizations;
- MV-IA-F010 Social Interaction Mode where participant or consequence relationships are shown;
- MV-IA-F011 Investigation and Clue Board;
- later World, Adventure, Project, and optional-AI surfaces that adopt this contract.

## 3. Canonical semantic model

Every projected node has a stable authorized ID, type, primary label, status, visibility scope, source/version evidence when permitted, and current version. Every projected edge has a stable authorized ID, source node, target node, direction, predicate, status, author or authority, visibility scope, rationale when permitted, and current version.

Canvas coordinates, grouping position, zoom, routing, and collapsed state are presentation preferences only. They cannot alter semantic identity, ordering, permission, or authority.

## 4. Equivalent views

Each graph surface must provide:

1. **List view:** nodes with expandable incoming and outgoing relationships.
2. **Outline/tree view:** a selected root and deterministic traversal, with repeated-node references rather than false hierarchy.
3. **Table view:** sortable/filterable nodes and edges with explicit columns.
4. **Graph view:** visual layout with textual labels and noncolor indicators.
5. **Detail view:** complete authorized node/edge information and actions.
6. **Nonvisual relationship navigator:** keyboard and screen-reader traversal by direction, predicate, type, status, and destination.

All views operate on the same server-authorized projection and expose the same permitted operations.

## 5. Focus and navigation

- One logical focus enters the graph region; arrow or command navigation moves among authorized nodes without forcing traversal of every decorative line.
- Users can jump to search, filters, selected-node details, incoming edges, outgoing edges, warnings, and actions.
- Focus order is deterministic and independent of current canvas coordinates.
- Virtualized content preserves announced position, set size where knowable, selection, expansion, and focus restoration.
- Zoom and pan never trap keyboard or screen-reader focus.
- Reconnect, refresh, filtering, and layout changes restore focus to the same semantic object when still authorized; otherwise focus moves to a disclosed safe fallback.

## 6. Create and edit parity

Every drag operation has a command/form alternative. Users can create a relationship by selecting source, predicate, destination, visibility, and rationale. Reordering or grouping has move commands. Multi-select has keyboard commands and an explicit selection summary. Destructive or visibility-expanding operations use the same proposal/approval and confirmation rules as visual operation paths.

## 7. Status communication

Selection, direction, positive/negative polarity, confidence, conflict, hidden/restricted state, stale state, pending approval, validation error, and severity require text or icon-plus-label equivalents. Color is supplemental only. Animation is optional and respects reduced motion. Dense edge crossings cannot be the sole warning of ambiguity.

## 8. Responsive behavior

Desktop may default to split graph/detail. Tablet may use graph plus drawer. Mobile defaults to list or outline with an optional graph preview. Feature completeness, permission filtering, history, search, filters, actions, and recovery remain equal. No mobile user is required to manipulate a precision canvas.

## 9. Hidden information

The server filters nodes and edges before counts, topology, search, traversal, grouping, layout, exports, diagnostics, notifications, or optional-AI context are generated. The client must not receive hidden placeholders, stable IDs, degree counts, empty gaps, routing hints, or layout coordinates that reveal concealed structure.

When an authorized visible edge points to an unauthorized object, policy must either suppress the edge entirely or provide an explicitly approved redacted endpoint that does not permit correlation. The default is suppression.

## 10. Loading, stale, and recovery states

All views distinguish loading, empty-authorized-result, filtered-empty, offline draft, stale projection, reconnecting, history gap, access revoked, source unavailable, and error. A partial visual graph cannot be presented as complete. After Event-gap recovery, view equivalence and selected-object focus are revalidated against the fresh projection.

## 11. Performance budgets

Implementations must support progressive rendering and virtualization without losing semantic order. Large graphs use server-side authorized filtering, bounded neighborhoods, pagination, and explicit result limits. Performance degradation may reduce decorative effects or automatic layout quality, but cannot remove accessible views or permission checks.

## 12. Testing contract

Testing covers keyboard-only operation, screen-reader traversal, touch, 200% text scaling, reflow, high contrast, reduced motion, noncolor status, focus restoration, virtualization, mobile parity, hidden-topology resistance, and equivalent create/edit/delete/share workflows.

Automated checks supplement but do not replace structured manual accessibility review before internal-alpha release. This design package does not authorize that release.

## 13. Implementation slices

1. `GLA-S01` — semantic node/edge projection contract.
2. `GLA-S02` — equivalent list, outline, table, graph, and detail adapters.
3. `GLA-S03` — keyboard, focus, selection, and nonvisual navigator.
4. `GLA-S04` — create/edit/group/share operation parity.
5. `GLA-S05` — status, responsive, text-scaling, contrast, and reduced-motion behavior.
6. `GLA-S06` — hidden-topology filtering and derivative-surface parity.
7. `GLA-S07` — virtualization, performance budgets, reconnect, and focus recovery.
8. `GLA-S08` — deterministic fixtures, automated checks, and manual-review handoff.

## 14. Blocking acceptance criteria

1. No semantic fact exists only in graph geometry.
2. Every node and edge has a textual authorized representation.
3. List, outline, table, graph, detail, and nonvisual navigation use one projection.
4. All permitted operations have non-drag alternatives.
5. Keyboard users can complete every workflow.
6. Screen-reader users can traverse incoming and outgoing edges by predicate.
7. Focus order is independent of canvas coordinates.
8. Focus survives safe refresh and reconnect.
9. Revocation removes focus and protected derivatives safely.
10. Hidden nodes and edges cannot be inferred from counts or topology.
11. Hidden structure cannot leak through layout coordinates or routing.
12. Search and filters operate only on authorized data.
13. Exports and diagnostics match on-screen authorization.
14. Optional AI receives the same authorized projection only.
15. Direction and polarity are not color-only.
16. Conflict, stale, pending, and error states are not color-only.
17. Reduced motion removes nonessential animation.
18. 200% text scaling preserves operation access and readable reflow.
19. High-contrast mode preserves status and selection.
20. Mobile supplies full list/outline workflow parity.
21. Touch targets and alternatives do not require precision dragging.
22. Virtualization preserves semantic order and focus context.
23. Bounded neighborhoods disclose result limits and incompleteness.
24. Loading or partial data is never represented as complete.
25. Repeated nodes in outline traversal are references, not false duplicates.
26. Destructive or visibility-expanding actions retain approval safeguards.
27. Automated checks and manual-review requirements are both recorded.
28. `P9-06-008-attempt-002` remains unfinished and unmodified.

## 15. Boundaries

Design only. Application implementation remains dependency-gated by P9 foundations and the covered feature contracts. No paid service, production credential, real-user data collection, internal-alpha release, deployment, public release, AI authority, or canonical promotion is authorized.
