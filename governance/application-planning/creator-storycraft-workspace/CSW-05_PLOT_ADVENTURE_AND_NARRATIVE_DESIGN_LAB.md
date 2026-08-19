# CSW-05 — Plot, Adventure and Narrative Design Lab

**Work item:** CSW-05  
**Program:** CSW — Creator Storycraft Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

CSW-05 defines a **nonlinear tabletop narrative design lab** over CSW-01 Creative Fragments, CSW-02 Project Memory/Story Bible and CSW-04 Guided Creation. It helps creators plan hooks, threads, beats, scenes, revelations, choices, consequences, payoffs, optional content, alternate routes and failure states without pretending speculative planning is an incorporated Adventure or Campaign.

The controlling rule is:

> **Plan richly, branch freely, analyze advisory structure, and cross into governed Adventure/Campaign truth only through an explicit handoff.**

CSW-05 does not replace D28 Adventure authority, A5 Campaign/Scene/Session authority, A9 runtime clues/hypotheses, or D29 authoring provenance. It projects and organizes pre-authoritative structure and later records explicit incorporation receipts.

## 2. Structural model

The Lab uses a semantic graph whose nodes remain CSW structures or references until incorporation.

Baseline structural roles:

- `hook` — reason to engage;
- `thread` — through-line connecting several elements;
- `beat` — meaningful dramatic/gameplay change;
- `scene-seed` — possible playable situation, not a live Scene;
- `encounter-seed` — possible encounter, not an authoritative encounter instance;
- `revelation` — planned information change;
- `choice` — meaningful player decision point;
- `consequence` — possible outcome linked to a choice/action/condition;
- `setup` and `payoff` — proposed expectation/return relationship;
- `prerequisite` — structural condition for access or comprehension;
- `optional-content` — material intentionally not required for progress;
- `failure-state` — planned non-success continuation or termination state;
- `endpoint` — proposed completion/exit state;
- `open-question` — intentionally unresolved creator decision;
- `note` — pacing, pressure, spotlight, tone or implementation annotation.

These roles may be represented by CSW-01 fragments plus Lab-local structural edges. They do not create D28 node identity merely by being placed on the board.

## 3. Edge semantics

Baseline edges:

- `may-follow`;
- `requires`;
- `unlocks`;
- `choice-leads-to`;
- `failure-leads-to`;
- `reveals`;
- `sets-up`;
- `pays-off`;
- `supports-thread`;
- `contrasts-with`;
- `optional-after`;
- `converges-with`;
- `branches-from`;
- `alternate-route-to`;
- `references`;
- `incorporated-as`.

Edges are structural proposals. A relation such as `reveals` does not assert that a runtime clue was discovered; `choice-leads-to` does not assert that a player made the choice.

## 4. Nonlinear route contract

The Lab must support:

- divergent branches;
- convergent branches;
- optional side routes;
- gated routes;
- multiple valid endpoints;
- loops when explicitly intended;
- fail-forward routes;
- hard failure/end routes;
- hidden creator-only alternatives;
- mutually exclusive branches;
- unresolved branches still under design.

The tool must never require one golden path. A creator may intentionally design a linear segment or entire experience; the Lab may show advisory concentration warnings but does not reject linear design.

## 5. Choice and consequence

A `choice` records candidate options or a freeform decision surface and links each option to possible consequences. Consequences may be immediate, delayed, conditional, hidden, reversible or terminal.

Rules:

1. the Lab does not require exhaustive prediction of player behavior;
2. an unmodeled action remains possible in actual play;
3. consequences are plans until incorporated/resolved by owning domains;
4. choices may have overlapping or converging outcomes;
5. labels such as “good/bad” are optional creator annotations, never system truth;
6. optional AI may suggest alternatives but may not select the canonical branch.

## 6. Revelation, clue and mystery planning

CSW-05 can plan revelations and clue coverage while preserving A9 boundaries.

A creator may link:

- a proposed revelation;
- one or more possible clue/source fragments;
- prerequisite knowledge;
- scenes/routes where a clue might be encountered;
- redundancy/alternate clue paths;
- false/misleading possibilities;
- payoff or consequence of learning/not learning something.

These links are design intent only. They do not create runtime clue ownership, discovery state, objective truth or hypothesis resolution. CSW-06 later adds deeper continuity/open-thread analysis.

## 7. Views share one semantic model

The Lab offers equivalent projections of the same structure:

### Outline
Hierarchical/ordered textual projection grouped by thread, route, chapter/phase or creator-defined section.

### Board
Cards/columns for flexible spatial planning. Board position is presentation metadata, not narrative truth unless explicitly translated into an order/relation.

### Timeline
Shows proposed chronology, relative ordering, deadlines or temporal windows where the creator provides them. Absence from the timeline does not mean unordered material is invalid.

### Graph
Shows nodes, branches, prerequisites and convergence. Graph geometry is not semantic; edges and accessible labels are.

### Nonvisual semantic outline
A first-class keyboard/screen-reader structure lists every node, role, incoming/outgoing edges, prerequisites, branch alternatives, unresolved warnings and actions. Every graph/board operation has a textual equivalent. Drag-and-drop is never required.

All views operate on stable identities and explicit semantic relations; rearranging one projection must not silently alter semantics unless the user performs an explicit reorder/link operation.

## 8. Pacing, pressure and spotlight notes

Creators may annotate structure with nonauthoritative planning metadata:

- expected intensity/pressure;
- estimated session/minute scale;
- investigation/exploration/social/combat emphasis;
- spotlight target(s);
- rest/breathing-room intent;
- urgency source;
- reveal density;
- expected resource pressure;
- tone/mood.

These are creator notes, not mechanics and not objective quality scores. The system may summarize distributions and flag abrupt concentration/gaps, but it must frame them as candidates for review.

## 9. Advisory analysis

Deterministic analysis may surface:

- a required node with no reachable route;
- an endpoint with no incoming route;
- a choice whose alternatives immediately reconverge without meaningful difference;
- a payoff with no recorded setup;
- a setup with no recorded payoff;
- a revelation required by later structure but with only one fragile source;
- optional content accidentally marked as prerequisite;
- branch explosion beyond creator-set complexity preference;
- a long sequence with no explicit choice point;
- a route that bypasses all planned clues for a required revelation;
- unresolved references or missing target nodes.

Warnings are advisory. A creator may mark them `intentional`, `dismissed`, `deferred` or `resolved` with a note. CSW-06 may later reuse those dispositions.

## 10. Reusable Adventure planning vs Campaign-specific planning

### Reusable planning

A Personal/creator-owned Lab plan can target a reusable Adventure concept. It may reference World definitions or reusable creator material but must not contain copied Campaign-private runtime truth.

### Campaign-specific planning

A Campaign-bound plan may reference authorized Campaign context, current state, private notes or active Characters. It remains pre-authoritative preparation material.

Transition rules:

- reusable → Campaign uses explicit clone/bind/propose semantics with provenance;
- Campaign → reusable requires an explicit safe clone/adaptation that removes or replaces private/run-specific dependencies;
- no automatic propagation in either direction;
- access revocation removes protected payload from later views/AI context even if a structural pointer remains as an unavailable reference.

## 11. CSW-04 and CSW-03 integration

Guided Adventure/quest output may open in the Lab as fragments and initial suggested relationships. Workflow step order is **not** automatically chronology or graph order.

CSW-03 Inspiration may generate:

- alternate hooks;
- branch options;
- consequences;
- setbacks/failure routes;
- reveal sources;
- payoff variants;
- scene/encounter seeds;
- route combinations.

Generated candidates remain ephemeral until explicitly saved and linked. The Lab never silently inserts generated content into the graph.

## 12. Story Bible/context safety

Story Bible references are authorization-filtered before search, graph expansion, counts, similarity, suggestions or optional-AI context. Hidden nodes must not leak through “missing link,” degree/count, autocomplete, route analysis, embeddings or ranking.

A Lab plan may pin an authorized governed reference/version for reproducibility. Pinning does not copy ownership or authority.

## 13. D28 governed handoff

The Lab hands material to Adventure authority through an explicit incorporation/proposal operation.

A conceptual handoff includes:

- source plan ID/version;
- selected source node/edge IDs and versions;
- target Adventure/creator context;
- requested node/edge mapping;
- unresolved items intentionally excluded;
- source Story Bible/governed references;
- initiator and authorization evidence;
- provenance/correlation ID;
- preview/diff of created or proposed D28 structure.

The owning domain validates target legality and creates D28 identities. CSW records `incorporated-as`/receipt references afterward.

Later CSW edits do not silently update the Adventure. Later Adventure edits do not silently rewrite the Lab plan. A future explicit rebase/compare flow may be added, but propagation is never implicit.

## 14. Recovery and versioning

Structural edits use stable IDs, optimistic versions and idempotent operation identity. Interrupted edits resume from durable state; unsynced local drafts never override newer server structure silently.

Branch operations preserve the source. Deleting a node with incoming/outgoing edges requires a clear impact preview and either edge cleanup, reattachment or tombstone behavior. History retains enough provenance to understand structural changes.

## 15. Accessibility/mobile

Required parity includes:

- keyboard creation/linking/reordering;
- screen-reader semantic outline of routes and branches;
- textual edge labels rather than line/color-only meaning;
- non-drag move/link controls;
- mobile focused-node mode with incoming/outgoing relationships;
- zoom/large-text support without hiding semantics;
- reduced-motion transitions;
- explicit branch names and breadcrumb/return-to-parent controls;
- warnings tied to named nodes/edges, not canvas coordinates.

## 16. Optional AI boundary

Optional AI may suggest structures, alternative routes, summaries, names or prose descriptions from explicitly authorized context. It may not:

- mutate the graph without explicit save/apply;
- decide objective continuity truth;
- create runtime clues/discovery;
- publish/incorporate automatically;
- bypass hidden-information filtering;
- mark an Adventure “good,” “balanced” or “complete” as objective truth.

The deterministic/manual Lab remains fully usable without AI.

## 17. Acceptance contract

CSW-05 is design-complete when the following are defined and reviewable:

- stable pre-authoritative structural roles/edges;
- divergent/convergent/optional/gated/failure routes;
- explicit choice/consequence/revelation semantics;
- shared outline/board/timeline/graph model;
- semantic nonvisual parity;
- advisory pacing/agency/mystery analysis with creator dispositions;
- Personal/reusable vs Campaign-specific boundary;
- CSW-03/04 and Story Bible integration;
- explicit D28 handoff with provenance/no silent propagation;
- deterministic recovery/version rules;
- optional AI candidate-only boundary.

No application implementation, migration, release/deployment, canonical promotion or CCTI-12-T04 work is authorized by this contract.