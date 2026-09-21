# PDCP MSLR Family Design Closure

**Project:** PDCP — Preimplementation Design Closure Project  
**Family:** MSLR — Multiversal Spatial Law Runtime  
**Status:** DESIGN CLOSED FOR ROADMAP REDUCTION  
**Baseline:** 18 planned tranches  
**Proposed surviving implementation tranches:** 9  
**Implementation authority:** none  
**MAS:** excluded and not reopened

## 1. Closure purpose

This package closes the product-design obligations that were previously distributed across MSLR-01..18 so later OPS3 product execution can implement a smaller, non-overlapping family without reopening benchmark research, ownership questions, spatial-law semantics, UX intent, permission rules, recovery rules or validation design.

MSLR remains a specialist runtime. It is not a second World, Reality, Scene, Map, Environment, Transition/Portal, Knowledge, Action/Event or Campaign-state ledger.

The reduction is not based on deleting capability. It is based on three facts:

1. the original 18 tranches separated many adjacent design questions that now share one implementation seam;
2. PDCP Packets 04, 07 and 08 already close generic affordance, creator/GM execution and simulation/formal-validation semantics that MSLR should consume instead of rebuilding;
3. MCS, GPR, PCA, SSA, ENV and canonical owner domains already own generic cartography, gameplay execution, production recipes, analysis infrastructure, semantic topology and environment contexts.

## 2. Canonical owner crosswalk

| Concern | Canonical owner / reusable owner | MSLR responsibility |
|---|---|---|
| semantic locations, regions, adjacency primitives, anchors | SSA / World / Scene | bind executable anomalous spatial laws to accepted spatial identities |
| Reality/Branch identity and environmental contexts | World / Reality / ENV | consume explicit contexts; never infer hidden causes |
| cartographic geometry, map/interior editing and projections | MCS | request and bind specialist projections; never make drawing canonical truth |
| generic gameplay operations, Action/Event execution, replay | GPR + Action/Event | provide specialist spatial-law operations and deltas through generic execution |
| portals, access and traversal authority | Transition/Portal/Access | evaluate spatial-law preconditions; never grant traversal merely from bleed or visibility |
| participant knowledge, memory, visibility and permissions | Knowledge/Visibility owners | define spatial predicates and projections referencing owner state |
| built spaces and settlement/infrastructure truth | MBES | apply spatial laws to accepted spaces without rebuilding construction |
| shared semantic affordances and Effect composition | MRCS/GPR + PDCP Packet 04 | supply spatial context/profile effects only |
| preview, explanation, diagnostics, intervention, compensation | shared owner operations + PDCP Packet 07 | domain-specific adapters and specialist views only |
| reusable solver/simulation workbench | PCA-12 + PDCP Packet 08 | domain model adapter, spatial constraints and interpretation only |
| procedural graph/recipe substrate | PCA-02/PCA-03 | spatial-law recipes, constraints and domain generators only |
| broader ecology/economy/faction/settlement consequence fan-out | MSWI | emit typed spatial Events/observations/deltas; do not invent downstream state |
| audio/visual/nonvisual presentation | MCS/MSAS/presentation/accessibility owners | expose semantic cue requirements and bindings only |

## 3. State and data model

### 3.1 SpatialLawProfile

Reusable definition describing one or more non-standard spatial dimensions.

Required fields:

- `profileId`
- `version`
- `scopeSelector`
- `dimensionRules[]`
- `invariants[]`
- `triggerBindings[]`
- `discoverabilityProfile`
- `resolutionDepths[]`
- `sourceRefs[]`
- `provenance`

Optional fields include authored nondeterminism policy, counterplay bindings, generator compatibility, presentation hints and setting-specific vocabulary.

A profile is a reusable definition, not live Campaign state.

### 3.2 SpatialLawDimensionRule

Typed law component. Supported dimension classes are:

- `topology`
- `metric`
- `containment_scale`
- `orientation_gravity`
- `layer_boundary`
- `observer_predicate`
- `temporal_recurrence`
- `causal_symbolic`
- `stability`
- `discoverability`
- `custom_owner_defined`

The dimension classes remain separable. Non-Euclidean topology does not imply a non-Euclidean metric; a fuzzy layer boundary does not imply traversability; an orientation change does not change location identity.

### 3.3 SpatialLawRuntimeInstance

Campaign-scoped live state for an accepted profile binding.

Required fields:

- `instanceId`
- `profileRef`
- `scopeRefs[]`
- `campaignRef`
- `activeLawState`
- `stateVersion`
- `createdByEventRef`
- `lastMutationEventRef`
- `determinismClass`
- `recoveryClass`

The instance stores only MSLR-owned law state. Location identity, World state, participant knowledge and portal/access state remain references to their owners.

### 3.4 TopologyState

Stores runtime-only anomalous relation state such as:

- active/disabled semantic edges;
- redirected exits;
- permutations;
- folds/wraps;
- phase relationships;
- recurrence counters;
- law-state variables;
- explicit transition transforms.

It never clones the canonical Location/World graph.

### 3.5 SpatialProjection

A non-authoritative view derived from an authorized basis.

Projection kinds:

- `true_authoritative`
- `observable`
- `participant_known`
- `participant_suspected`
- `historical_as_of`
- `counterfactual_preview`
- `creator_diagnostic`

Every projection records the basis version, audience/permission context and omitted/unknown status. A participant-authored suspected map may be wrong without corrupting true topology.

### 3.6 SpatialObservation and SpatialHypothesis

Observation records reference real perception/evidence operations and source Events. Hypotheses are participant/GM/creator interpretations and never become truth merely because a confidence field increases.

Observations may include route traversal, timing, recurrence, distance comparison, marker state, cue detection, environmental contradiction and transition outcome.

### 3.7 SpatialPredicateBinding

Route/law behavior may depend on explicit owner state such as:

- observer identity/role;
- possessed Knowledge;
- remembered fact;
- sensory capability/state;
- explicit belief/claim state when an owner permits it;
- Campaign time/Event/milestone;
- Reality/environment context;
- carried anchor/token/Item state.

Predicates are references to owner-authorized inputs. Client observation never self-authorizes a route.

### 3.8 MetricTransformProfile

Defines source-backed or setting-authored distance/range/area/path/line-of-sight transforms. It may identify Euclidean, spherical, hyperbolic, anisotropic or custom metrics, but MSLR does not invent mathematical behavior where the profile is incomplete.

### 3.9 ContainmentScaleTransform

Defines relationships among exterior/interior/nested spaces while preserving stable identities.

Required distinctions:

- contains;
- nested in;
- same scale;
- scale transform;
- bigger-inside relationship;
- recursive containment;
- explicit entry/exit transform.

Contents are never duplicated merely because a containing space has anomalous scale.

### 3.10 OrientationFrame

Defines local up/gravity/orientation independently from map coordinates. Movement, projectiles and other systems consume the frame by reference. Crossing a boundary can apply an explicit frame transform without changing topology unless a topology operation also occurs.

### 3.11 ContextualLawBinding

Represents fuzzy seams, layer overlap, temporal recurrence, dream/causal conditions and other contextual law behavior. It records contributing Reality/Environment/source profiles, local intensity/state and explicit traversability/access references where relevant.

### 3.12 NavigationAnchorBinding

Binds Items, marks, ropes, beacons, clocks, drones, wards, memory anchors, route tokens or setting-specific aids to declared spatial-law responses. An anchor can be preserved, moved, copied, erased, corrupted or rejected only by an authored rule.

### 3.13 SpatialAnomalyCue

Semantic evidence cue, not truth. Cue channels can include visual, audio, tactile, thermal, olfactory, text/signage, timing/repetition, social behavior or map contradiction. Equivalent nonvisual/non-audio/non-color cues are required when the cue is progression-relevant.

### 3.14 SpatialGenerationSpec

Proposal-only specification for generated impossible spaces. It contains:

- generator/recipe/profile versions;
- seed;
- node/region requirements;
- topology constraints;
- dimension-law constraints;
- required starts/objectives/escapes;
- permitted instability/nondeterminism;
- solvability obligations;
- presentation-independent invariants.

Generated output is ephemeral/proposed until explicit owner-authorized promotion.

### 3.15 SpatialAnalysisReceipt

MSLR-specific interpretation of the shared Packet-08/PCA-12 analysis envelope. It may contain reachability witnesses, counterexamples, contradictory invariants, cycles, route coverage and solver status. Formal claims are scoped to declared model/version/assumptions/bounds. Solver `unknown`, timeout or exhausted bound is inconclusive.

## 4. Operations and lifecycle

### 4.1 Profile binding

`bind_spatial_law_profile(profileRef, scopeRefs, campaignRef)` validates authority, scope compatibility and invariants before creating a runtime instance. Failure leaves no partial canonical law state.

### 4.2 Topology operations

MSLR defines specialist semantic operations including:

- connect / disconnect;
- redirect;
- permute;
- wrap / unwrap;
- fold / unfold;
- nest / unnest;
- phase / dephase;
- collapse / restore where owner rules permit;
- stabilize / destabilize;
- sever;
- apply/remove explicit transform.

These are semantic requests routed through Action/Event/GPR owner operations. They do not bypass canonical owner permissions.

### 4.3 Preview and commit

Preview/counterfactual evaluation uses a pinned `ExecutionContextSnapshot` from Packet 07. Preview does not reserve, consume, reveal or commit live state. Commit revalidates versions, permissions, predicates and resources before any mutation.

### 4.4 Reversal and recovery

Committed spatial Events are immutable history. Reversal uses:

- owner-defined inverse operation;
- compensating operation;
- explicit recovery/snapshot restoration where supported;
- GM adjudication when the owning rule requires it;
- `irreversible` when no safe inverse exists.

There is no history-deleting undo.

### 4.5 Observation and experiment

Players/GM/automation may perform authorized observation operations: mark, measure, traverse, compare, time, probe, listen, inspect, repeat, test threshold, compare maps or examine anchors. Outcomes create observations/evidence/knowledge proposals through existing owners.

### 4.6 Observer-dependent evaluation

A route predicate reads an authorized owner projection at evaluation time. It records which owner versions formed the basis. Hidden predicate truth is filtered before player diagnostics.

### 4.7 Contextual seam and recurrence evaluation

Fuzzy boundary/bleed/temporal/dream/causal state can modify spatial-law evaluation only when the relevant profile explicitly binds it. Bleed alone never grants access. Recurrence/reset preserves or resets only declared state categories.

### 4.8 Anchor/counterplay interaction

Anchor interactions are ordinary governed operations against the law profile. Failure or interference produces typed outcomes; it does not silently destroy equipment or fabricate a law response.

### 4.9 Generation and promotion

Generation is deterministic for declared deterministic recipes/seeds. Solvability checks occur before promotion where required. A failing, inconclusive or unsupported proof leaves the candidate unpromoted and exposes repair diagnostics rather than silently accepting it.

## 5. Resolution depths

MSLR uses one semantic law identity across three execution depths:

1. **abstract** — travel/theater-of-the-mind outcomes, coarse path and condition resolution;
2. **topology/tactical** — explicit nodes, edges, transforms, ranges, frames and route predicates;
3. **rendered/specialized projection** — MCS/scene/rendering surfaces visualize the same accepted semantics.

Refinement may add representation detail but cannot change the law merely because a different UI is open. Unsupported deeper detail remains unresolved.

## 6. Player / GM / creator UX

### Player

- sees only authorized observable/known/suspected projections;
- can record observations, marks, hypotheses and route notes;
- receives equivalent semantic cues when a sensory channel is unavailable;
- can preview an authorized operation only when the owning rule permits preview;
- never receives hidden edge counts or protected solution topology through diagnostics.

### GM

- can inspect true state when role/permissions allow;
- receives explicit distinction among true, observable, known and suspected topology;
- uses typed interventions rather than arbitrary field mutation;
- can examine Event history, law versions, route predicates and repair options;
- can promote generated spaces only through governed acceptance.

### Creator

- authors profiles, scopes, invariants, cues, counterplay and generator constraints;
- uses graph/map/frame/route projections supplied through MCS/shared studio components;
- uses PCA-12 analysis through MSLR model adapters;
- can run preview/dry-run/diagnostic sessions without changing live Campaign truth.

## 7. Permission and hidden-information contract

Filtering occurs before:

- map node/edge construction;
- route/path queries;
- counts and statistics;
- search;
- solvability/diagnostic model extraction;
- export;
- optional-AI context.

A privileged topology graph cannot be built and then merely relabeled for a Player. Unauthorized nodes/edges/predicates must be absent from that audience's model/projection.

## 8. Provenance and replay

Every consequential spatial mutation records:

- initiating actor/agent/source;
- Action/Event reference;
- profile/version;
- previous state/version;
- resulting state/version;
- relevant predicate/environment versions;
- deterministic seed where used;
- recovery/reversibility classification.

Replay reconstructs declared deterministic MSLR state from accepted profile versions plus Event history. Nondeterministic profiles record enough sampled/random state to replay the committed outcome where the owner contract requires it.

## 9. Failure and edge-case rules

- contradictory profile laws fail validation unless an explicit precedence/composition rule exists;
- missing metric/containment/orientation behavior remains unresolved rather than using common-sense physics;
- stale preview receipts cannot be committed without revalidation;
- route predicates with unavailable required owner data return unresolved/blocked according to the authored policy, never invented truth;
- recursive containment is cycle-checked and bounded by explicit owner rules;
- mutation cycles and runaway trigger cascades are bounded and diagnostic;
- solver timeout/unknown is inconclusive;
- generated spaces missing required objective/escape reachability remain proposals;
- hidden topology never leaks via route counts, graph shape, debug overlays or AI;
- presentation failure cannot mutate semantic state;
- provider/tool unavailability falls back to local/manual supported workflows;
- no progression-critical anomaly requires color, vision, hearing, motion or precision dragging as its sole channel.

## 10. Intra-family overlap resolution

The original 18-tranche plan contained six implementation-overlap clusters:

1. **MSLR-01 + 02** both establish definition/runtime boundaries and profile composition. They become one profile/runtime-core tranche.
2. **MSLR-03 + 06** both implement live topology mutation, Event trace, preview, commit and reversal. They become one state/operation tranche.
3. **MSLR-04 + 05 + 11** all depend on true/observable/known/suspected projections, participant context and discovery. They become one knowledge/observer/discovery tranche.
4. **MSLR-07 + 12** both execute contextual Reality/environment/time/dream/causal law conditions. They become one contextual-law tranche.
5. **MSLR-08 + 09 + 10** are coordinate/transform dimensions consumed by movement/range/scene systems. They become one metric/scale/orientation transform tranche.
6. **MSLR-13 + 15** both implement player-observable counterplay/cues/navigation aids. They become one counterplay/cue tranche.
7. **MSLR-14 + 17** both need creator authoring, diagnostics, simulation and solvability infrastructure. Shared Packet-07/PCA-12 services allow one domain-specific authoring/generation tranche.

MSLR-16 remains a distinct integration tranche because actual cross-system adapters still require runtime work. MSLR-18 remains a distinct golden proof because it is the DAG-preserved completion barrier and MSWI handoff.

## 11. Cross-family overlap resolution

### Generic preview/debug/GM operations

Owned by Packet 07/shared owner operations. MSLR implements only domain requests, traces and specialist lenses. MSLR-17 therefore does not build another debugger/editor framework.

### Solver/simulation/formal validation

Owned by PCA-12 + Packet 08. MSLR-14 supplies model extraction, domain constraints and interpretation. It does not ship a second SAT/SMT/graph/Monte-Carlo framework.

### Procedural graph/recipe execution

Owned by PCA-02/PCA-03. MSLR-14 supplies impossible-space recipe nodes/profiles and validators, not another generic DAG scheduler/cache/provenance engine.

### Cartographic projection

Owned by MCS. MSLR supplies semantic topology/frame/layer/knowledge projections and bindings; MCS draws/edits them.

### Gameplay execution/replay

Owned generically by GPR/Action/Event. MSLR supplies specialist spatial semantics and state.

### Audio/visual cue production

Owned by MSAS/MCS/presentation systems. MSLR supplies semantic anomaly/counterplay cue requirements.

### Systemic consequence propagation

Owned by MSWI. MSLR outputs typed spatial changes and observations; it does not directly mutate ecology, economy, faction or settlement state.

## 12. Surviving implementation tranches

### MSLR-01 — Spatial-Law Profile & Runtime Core

Absorbs baseline MSLR-01 and MSLR-02.

Implement:

- reusable `SpatialLawProfile` and dimension-rule schemas;
- live `SpatialLawRuntimeInstance` boundary;
- scope/invariant/composition validation;
- owner-reference bindings and compatibility/version checks;
- baseline normal/Euclidean profile;
- migration/version hooks;
- tests for duplicate-ledger prevention and contradiction handling.

### MSLR-03 — Dynamic Topology State & Governed Spatial Operations

Absorbs baseline MSLR-03 and MSLR-06.

Implement:

- live anomalous topology state;
- typed spatial operations;
- Action/Event/GPR integration;
- preview/dry-run/revalidation;
- Event trace/replay;
- inverse/compensation/recovery classifications;
- stale/concurrent mutation rejection.

### MSLR-04 — Knowledge, Observer & Spatial Discovery Runtime

Absorbs baseline MSLR-04, MSLR-05 and MSLR-11.

Implement:

- true/observable/known/suspected projections;
- observer/knowledge/memory/perception predicates;
- observation/hypothesis/experiment operations;
- role-safe route explanations;
- hidden-topology filtering before route/search/diagnostic contexts;
- evidence/knowledge handoffs to existing owners.

### MSLR-07 — Reality-Seam, Temporal/Dream & Contextual Spatial Laws

Absorbs baseline MSLR-07 and MSLR-12.

Implement:

- fuzzy layer/boundary/bleed state bindings;
- explicit traversal/access separation;
- temporal recurrence/reset conditions;
- dream/causal/symbolic route predicates;
- environment/Reality owner bindings;
- context-state replay and explanation.

### MSLR-08 — Metric, Scale, Containment & Orientation Transform Runtime

Absorbs baseline MSLR-08, MSLR-09 and MSLR-10.

Implement:

- metric transforms;
- recursive/nested/bigger-inside containment transforms;
- scale relationships;
- orientation/gravity frames;
- entry/exit transform semantics;
- movement/range/projectile/scene adapters;
- identity-preserving nesting tests.

### MSLR-13 — Navigation Aids, Anchors, Sensory Cues & Counterplay

Absorbs baseline MSLR-13 and MSLR-15.

Implement:

- navigation/anchor bindings;
- governed law responses to aids;
- anomaly cue grammar bindings;
- accessible equivalent cue contracts;
- MCS/MSAS/presentation handoffs;
- counterplay provenance and owner-operation routing.

### MSLR-14 — Procedural Impossible-Space Authoring, Solvability & Diagnostics

Absorbs baseline MSLR-14 and MSLR-17.

Implement:

- MSLR recipe/profile nodes over PCA-02/PCA-03;
- generator constraints and seeded candidate outputs;
- MSLR model adapter over PCA-12;
- reachability/solvability/contradiction/cycle diagnostics;
- Packet-07 creator preview/explanation/step-through adapters;
- MCS specialist map/graph/frame views;
- governed promotion of valid candidates.

### MSLR-16 — Multi-Resolution Cross-System Spatial Runtime Integration

Retains baseline MSLR-16.

Implement explicit adapters proving the same spatial law can affect abstract travel, topology/tactical movement, combat/range and at least one non-combat owner system without changing semantic meaning across presentation modes.

### MSLR-18 — Golden Impossible-Space Proof & MSWI Handoff

Retains baseline MSLR-18 and the existing DAG golden gate.

Automate/prove the full family battery, exact-head validation, deterministic replay where declared, provider-off operation, permission filtering, accessible cue parity, clean-room boundaries, and typed handoff to MSWI.

## 13. Implementation-ready golden vectors

### Profile/runtime core

- **PDCP-MSLR-001:** default Euclidean profile validates with no anomalous law state.
- **PDCP-MSLR-002:** topology and metric rules compose independently.
- **PDCP-MSLR-003:** contradictory rules without precedence are rejected deterministically.
- **PDCP-MSLR-004:** a profile references canonical World/Scene IDs without cloning them.
- **PDCP-MSLR-005:** unsupported property remains unresolved rather than inferred.

### Dynamic topology and operations

- **PDCP-MSLR-006:** authorized redirect creates one Event-traced state-version transition.
- **PDCP-MSLR-007:** stale preview cannot commit after topology version changes.
- **PDCP-MSLR-008:** inverse operation restores state while preserving both Events in history.
- **PDCP-MSLR-009:** unauthorized topology mutation is rejected before state change.
- **PDCP-MSLR-010:** deterministic replay reconstructs the same declared topology state.

### Knowledge/observer/discovery

- **PDCP-MSLR-011:** Player suspected map may contain a false edge without changing true topology.
- **PDCP-MSLR-012:** hidden edge cardinality does not leak through Player route diagnostics.
- **PDCP-MSLR-013:** two participants with different Knowledge obtain different authorized route projections.
- **PDCP-MSLR-014:** experiment creates evidence/knowledge output without rewriting the law.
- **PDCP-MSLR-015:** observer predicate reads owner state and records its basis version.

### Contextual laws

- **PDCP-MSLR-016:** dimensional bleed produces effects/cues while traversal remains denied.
- **PDCP-MSLR-017:** portal traversal can exist without broad bleed.
- **PDCP-MSLR-018:** loop reset preserves only the state categories declared by the profile.
- **PDCP-MSLR-019:** dream/causal route condition is learnable and replayable without a universal dream formula.
- **PDCP-MSLR-020:** missing ENV/Reality context produces unresolved/blocked behavior rather than invented context.

### Metric/scale/orientation transforms

- **PDCP-MSLR-021:** curved metric changes path length without changing adjacency.
- **PDCP-MSLR-022:** bigger-inside structure preserves one stable interior identity and one set of contents.
- **PDCP-MSLR-023:** recursive containment cycle is rejected or bounded by explicit policy.
- **PDCP-MSLR-024:** gravity-frame transition changes local up without changing Location identity.
- **PDCP-MSLR-025:** abstract and tactical range resolution consume the same metric profile version.

### Navigation/cues/counterplay

- **PDCP-MSLR-026:** chalk mark persists under a profile that preserves anchors.
- **PDCP-MSLR-027:** authored law moves/corrupts an anchor with attributable Event evidence.
- **PDCP-MSLR-028:** progression-relevant visual anomaly has an equivalent nonvisual semantic cue.
- **PDCP-MSLR-029:** audio anomaly has caption/text/timing equivalent without revealing hidden truth.
- **PDCP-MSLR-030:** navigation aid failure does not invent Item damage unless an owner rule emits it.

### Procedural authoring/analysis

- **PDCP-MSLR-031:** same deterministic recipe/profile/seed produces same semantic candidate.
- **PDCP-MSLR-032:** unreachable required escape keeps candidate unpromoted.
- **PDCP-MSLR-033:** solver timeout/UNKNOWN reports inconclusive, not valid/invalid.
- **PDCP-MSLR-034:** Player-visible diagnostic model is built without protected hidden nodes/edges.
- **PDCP-MSLR-035:** generated candidate promotion records recipe, seed, profile/version and acceptance Event.

### Cross-system integration

- **PDCP-MSLR-036:** one law produces compatible abstract-travel and tactical-movement results.
- **PDCP-MSLR-037:** metric/orientation context reaches combat/range through explicit owner adapters.
- **PDCP-MSLR-038:** pursuit/vehicle or another non-combat system consumes the same accepted law state.
- **PDCP-MSLR-039:** downstream system rejects stale law-state version rather than guessing.
- **PDCP-MSLR-040:** presentation-mode change alone does not mutate law state.

### Golden family proof

- **PDCP-MSLR-041:** non-adjacent topology and dynamic redirect replay correctly.
- **PDCP-MSLR-042:** shifting/looping maze can be solved through observations/counterplay without hidden-answer leak.
- **PDCP-MSLR-043:** fuzzy nontraversable bleed, metric distortion, bigger-inside containment and gravity transition coexist without dimension collapse.
- **PDCP-MSLR-044:** observer/knowledge-dependent route and accessible anomaly cues preserve permissions and semantic parity.
- **PDCP-MSLR-045:** MSLR typed Events/observations/deltas are consumable by MSWI while MSLR never mutates MSWI-owned ecology/economy/faction/settlement state.

## 14. Completion statement

All baseline MSLR design questions are sufficiently closed for reduction. No owner decision remains. The family can be reduced from 18 planning tranches to 9 implementation/proof tranches without losing accepted capability, provided the reduction receipt and backlog reconciliation preserve the mappings in this document.

This design closure does not implement MSLR, does not start MSLR, does not alter `operations/CURRENT.json`, and grants no product implementation authority.


## 15. Owner-approved spatial architecture amendment — 2026-09-21

During the governed MSLR-01 causal-RED phase, the owner approved a family-wide architecture refinement after review of interactive hyperbolic tiling material and HyperRogue's generalized multi-geometry/projection architecture. This amendment strengthens the existing design closure; it does not add tranches, reopen upstream families, or grant authority beyond the active MSLR-01 tranche.

### 15.1 Three-layer spatial model

MSLR must explicitly distinguish:

1. **intrinsic spatial law / geometry** — canonical MSLR law semantics such as metric, topology, containment/scale and orientation;
2. **spatial substrate / discretization** — optional cells, semantic adjacency complexes, quotient identifications, local frames or procedurally addressed neighborhoods used for gameplay/runtime computation;
3. **projection / presentation** — Poincaré, Klein, Euclidean-map, graph, schematic, rendered or other views supplied through MCS/presentation owners.

Changing only the projection MUST NOT change canonical location identity, intrinsic distance, adjacency, containment, orientation or accepted law state. Screen/pixel coordinates are never canonical spatial identity.

### 15.2 Identity, extent and addressing

Canonical World/Reality/Scene/Location identity remains owner-backed and stable independently of MSLR coordinates, tiling-cell addresses or projection coordinates.

Profiles MAY declare explicit extent/addressing semantics such as:

- finite;
- quotient/identified;
- unbounded;
- procedurally addressed / lazy-local expansion.

Unbounded or exponentially growing spaces must support bounded neighborhood evaluation and lazy addressability; implementations must not require exhaustive world enumeration.

### 15.3 Tranche refinements

- **MSLR-01:** add first-class intrinsic-law / substrate / projection separation, projection-invariance proof, stable identity independent of coordinates, and extent/addressing semantics.
- **MSLR-03:** add edge/region identifications, quotient topology, orientation-reversing connections where authored, local walker/frame state, and bounded/lazy neighborhood expansion.
- **MSLR-04:** observer/navigation knowledge may include local-frame, orientation and discovered-identification state without changing true topology.
- **MSLR-08:** make isometries and frame transport explicit; continuous geometry and discrete traversal substrates may realize the same accepted law; returning to one canonical location may yield a different local frame when the authored law permits it.
- **MSLR-13:** navigation aids may bind to local frames, anchors, breadcrumbs and authored geometry-law responses rather than assuming global compass semantics.
- **MSLR-14:** add fundamental-domain + transformation/group generation as a reusable MSLR authoring pattern over PCA-02/PCA-03. A regular Schläfli `{p,q}` tiling validator is permitted as one specialized generator family only; its curvature relation is not a universal MSLR rule.
- **MSLR-16:** explicitly prove pathfinding/pursuit/travel, tactical movement and combat/range consume the same accepted law semantics rather than treating geometry as rendering.
- **MSLR-18:** golden proof adds projection invariance, true hyperbolic tiling, quotient/non-orientable topology, bounded lazy unbounded-space operation, and discrete-vs-continuous realization of the same accepted law.

### 15.4 Clean-room and source boundary

The external systems are architecture/research references only. Protected source code, assets, level layouts, UI expression, save formats and proprietary/private protocols are not copied. HyperRogue's GPL-2.0 implementation is not incorporated into Multiversal by this amendment. MSLR remains a Multiversal-native abstraction over canonical owner contracts.
