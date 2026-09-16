# PDCP Packet 04 — Semantic Affordances & Composable Effects Design Closure

**Project:** PDCP — Preimplementation Design Closure Project  
**Packet:** 04 — Semantic Affordances & Composable Effects  
**Status:** DESIGN_CLOSED  
**Closed:** 2026-09-16  
**Implementation authority:** none  
**Roadmap-count mutation:** none in this packet

## 1. Closure statement

Packet 04 closes the benchmark-derived product-design questions raised by Noita, Caves of Qud, Cataclysm:DDA, Vintage Story and related systemic-interaction references without creating a second rules engine, physics engine, material ledger, crafting engine, engineering engine, construction engine, Effect ledger or universal pseudo-realism model.

Multiversal already has the relevant authoritative foundations:

- Action/Event and Effect/Condition/Resource owners retain runtime semantics and canonical mutation authority;
- MIB-12 retains committed crafting, repair, refurbishment and transformation transaction authority;
- Item/Asset, Character/NPC/Creature, Vehicle/Base, World/Environment and other owner domains retain target identity and live state;
- MRCS is the future reusable rule/content-definition authoring surface;
- GPR is the future reusable gameplay-pattern execution/composition substrate;
- MERA is the future engineering/refit/repair orchestration owner;
- MBES is the future built-environment/construction/settlement orchestration owner;
- MSLR owns non-standard spatial-law semantics where spatial law changes an interaction context;
- MSWI owns cross-domain systemic consequence propagation rather than base interaction semantics.

The missing capability is a reusable semantic contract that lets those owners describe and execute shared interactions without bespoke one-off logic for every target type.

Packet 04 therefore closes six reusable contracts:

1. semantic affordance definitions;
2. target interaction-capability bindings;
3. source/setting-governed response profiles;
4. effect-interaction/composition rules;
5. multi-resolution interaction execution;
6. deterministic propagation/bounding/explanation semantics.

No new implementation family or standalone roadmap tranche is required.

---

## 2. Authority and ownership

### 2.1 Owner table

| Concern | Canonical owner / rule |
|---|---|
| Action declaration, authorization, runtime occurrence and Event history | Existing Action/Event owner |
| Reusable Effect/Condition/Resource definitions and future authoring | Existing owners; MRCS authors compatible reusable definitions |
| Item/Asset identity, condition, durability, containment and installed state | Existing Item/Asset owner |
| Character/NPC/Creature body/state | Existing Character/NPC/Creature owners |
| Vehicle/Base/Platform component and operational state | Existing vehicle/platform/base owners |
| World/Environment canonical state and setting/reality laws | Existing World/Environment/Reality owners |
| Crafting/repair/refurbishment/transformation transactions | MIB-12 |
| Engineering/refit/disassembly/diagnostics | MERA |
| Construction/material/facility gameplay | MBES |
| Semantic rule/content authoring | MRCS |
| Runtime semantic-operation execution/composition | GPR |
| Non-standard spatial-law modifications to interaction context | MSLR |
| Cross-domain consequence fan-out | MSWI |
| Visibility, knowledge and protected weaknesses/properties | existing Permission/Visibility/Knowledge owners |

### 2.2 Packet-owned design contracts

Packet 04 defines interoperability semantics only. It does not own live target state.

The reusable definitions are:

- `SemanticAffordanceDefinition`
- `InteractionCapabilityBinding`
- `InteractionResponseProfileDefinition`
- `EffectInteractionRule`
- `InteractionResolutionProfile`
- `InteractionEvaluationReceipt`
- `EffectCompositionReceipt`
- `InteractionPropagationReceipt`

These may be authored/validated through MRCS and executed through GPR or specialist owners, but they do not themselves become a new canonical live-state ledger.

### 2.3 Explicit non-ownership

Packet 04 does **not** define:

- universal material properties;
- universal physics constants;
- universal damage formulas;
- universal temperature, electricity, corrosion, pressure or combustion models;
- universal anatomy;
- universal structural-engineering assumptions;
- universal magical interaction rules;
- automatic real-world behavior for source-unspecified substances;
- a second crafting/repair transaction system;
- a second Effect/Condition runtime;
- a global mutable `affordance_state` store.

Unknown or source-unspecified behavior remains unresolved unless an authorized rule/profile provides it.

---

## 3. Semantic affordance model

### 3.1 `SemanticAffordanceDefinition`

A reusable affordance describes **what kind of governed interaction is being attempted**, not whether it automatically succeeds.

Required fields:

- `affordance_id`: stable namespaced identifier;
- `semantic_class`: generalized operation family;
- `action_ref`: governed Action definition or Action-family reference;
- `target_capability_requirements`: one or more required target capability predicates;
- `actor_or_tool_requirements`: optional capability/resource/tool predicates;
- `context_requirements`: optional environment/spatial/access predicates;
- `effect_refs`: zero or more governed Effects proposed on successful/partial resolution;
- `outcome_classes`: permitted typed outcomes;
- `resolution_profiles`: supported abstract/standard/detailed execution modes;
- `scope`: core/setting/campaign/adventure/playtest/custom governed scope;
- `version` and provenance.

Optional fields may include cost/resource consumption, duration/project handoff, prerequisite access/isolation, consequence hooks, accessible presentation cues and specialist-owner routing.

### 3.2 Baseline semantic classes

The shared registry must support generalized operation classes including, but not limited to:

- `cut`
- `pierce`
- `crush`
- `break`
- `breach`
- `seal`
- `open`
- `close`
- `move`
- `lift`
- `push`
- `pull`
- `attach`
- `detach`
- `connect`
- `disconnect`
- `power`
- `depower`
- `heat`
- `cool`
- `burn`
- `extinguish`
- `freeze`
- `thaw`
- `melt`
- `solidify`
- `corrode`
- `clean`
- `contaminate`
- `repair`
- `restore`
- `patch`
- `dismantle`
- `assemble`
- `fabricate`
- `harvest`
- `extract`
- `transfer`
- `contain`
- `release`
- `stabilize`
- `destabilize`
- `calibrate`
- `disable`
- `enable`
- `inspect`
- `custom_governed_affordance`.

This vocabulary is extensible. The semantic ID is not a claim that every setting or target supports the operation.

### 3.3 Operation parity rule

The same semantic affordance may target any entity whose owner exposes compatible capabilities.

Example: `cut` may be used against a rope, cloth, vegetation, creature tissue, cable, barrier or reality-authored filament **only if** the relevant target owner/profile exposes a compatible capability and an authorized Action can attempt it.

Target type does not require a new bespoke verb when the semantic intent is the same. Domain-specific behavior remains in target/response profiles and owner resolution.

---

## 4. Target interaction capabilities

### 4.1 `InteractionCapabilityBinding`

A target definition or live instance may expose governed capability bindings such as:

- `cuttable`
- `pierceable`
- `breakable`
- `breachable`
- `sealable`
- `movable`
- `attachable`
- `connectable`
- `powerable`
- `heatable`
- `coolable`
- `combustion_reactive`
- `freeze_reactive`
- `melt_reactive`
- `corrosion_reactive`
- `repairable`
- `dismantlable`
- `harvestable`
- `extractable`
- `containable`
- `stabilizable`
- `inspectable`
- custom setting/domain capabilities.

A binding contains:

- stable capability ID;
- owning definition/entity reference;
- applicable target facet(s);
- visibility/knowledge classification;
- required response-profile references;
- optional prerequisite/access/tool constraints;
- source/provenance/version.

### 4.2 Target facets

An interaction may target:

- whole entity;
- named component;
- assembly/subassembly;
- surface/layer;
- connection/interface;
- network;
- zone/room/terrain patch;
- body part/anatomical component where an authorized anatomy owner provides it;
- semantic spatial feature where MSLR/SSA provides it;
- unresolved target detail.

A lower-detail facet may not be fabricated merely because the detailed UI wants one.

### 4.3 Capability is not outcome

`cuttable` means an attempt can be meaningfully evaluated. It does not mean a cut always succeeds.

Outcome may depend on explicit authored rules for actor/tool capability, target response, access, resource state, environment, magic/technology law, conditions and selected resolution profile.

---

## 5. Interaction response profiles

### 5.1 `InteractionResponseProfileDefinition`

A response profile specifies how an owned target/material/environment/property set responds to one or more semantic affordance or Effect categories.

Fields:

- `response_profile_id`;
- owner/domain and scope;
- target selectors/capability selectors;
- triggering affordance/effect classes;
- preconditions;
- explicit outcomes for success/partial/failure where applicable;
- emitted Effect/Condition/Resource/owner-operation references;
- transformation/substitution result references if authorized;
- propagation rules if any;
- reversibility/recovery references;
- unsupported/unresolved behavior;
- version/provenance.

### 5.2 No universal material table

Multiversal may author materials and material-like properties, but Packet 04 creates no global real-world table saying, for example, that every wood burns, every metal conducts, every liquid freezes at a particular point, every stone resists cutting, or every biological tissue behaves identically.

Such behavior exists only when supplied by:

- source/canon data;
- accepted setting/reality/environment rules;
- accepted material/content definitions;
- explicit owner-authored defaults at a governed scope.

A lower scope may override or specialize a higher-scope definition only through the existing explicit compatibility/precedence system.

### 5.3 Reality/environment contextualization

Response resolution may consume World/Environment/Reality/Branch state. A material that burns in one world may not burn in another; gravity, atmosphere, magic, dream law or non-standard spatial law may alter applicability.

The environment does not silently change the underlying definition. It contributes context to resolution.

### 5.4 Unknown behavior

If no applicable response rule exists, the result is one of:

- `unsupported_by_definition`;
- `insufficient_known_detail`;
- `requires_owner_adjudication`;
- `requires_refinement` where a permitted refinement source exists.

The engine may not silently infer a result from real-world common sense.

---

## 6. Effect composition

### 6.1 `EffectInteractionRule`

Effect composition is explicit and scope-aware.

A rule identifies:

- one or more incoming/active Effect classes/IDs;
- context/target predicates;
- interaction mode;
- explicit resulting Effect/Condition/Resource/owner-operation references;
- ordering/precedence requirements where necessary;
- propagation bounds;
- duration/termination behavior where relevant;
- version/provenance.

### 6.2 Interaction modes

Supported semantic modes include:

- `coexist`
- `suppress`
- `cancel`
- `replace`
- `transform`
- `amplify`
- `attenuate`
- `trigger`
- `propagate`
- `merge_into_named_effect`
- `conflict_requires_resolution`
- `no_defined_interaction`.

No interaction mode implies a universal numeric formula.

### 6.3 Ordering

Effect resolution order comes only from explicit dependencies, owner-defined precedence, Action/Event ordering, or the selected deterministic runtime contract.

Stable ID ordering may be used solely as deterministic receipt ordering when effects are semantically commutative; it may not invent mechanical priority.

### 6.4 Cycles and cascades

Propagation/composition must be bounded by an explicit rule such as:

- finite target set;
- finite propagation depth;
- per-Event visited interaction key;
- explicit resource/quantity exhaustion;
- owner-defined fixed point;
- explicit maximum iteration count whose mechanical meaning is authored.

A detected unbounded/circular interaction fails closed or stops at the last valid committed state with a diagnostic receipt. The runtime may not spin indefinitely or silently drop consequences.

### 6.5 Concurrency

Concurrent effects/operations use the owning runtime's authority/version/precondition checks. If state changed between preview and commit, the operation is revalidated. Conflicting noncommutative Effects require explicit owner resolution or rejection.

---

## 7. Interaction execution contract

### 7.1 Stages

A consequential interaction proceeds as:

`declare → authorize → resolve target/facet → discover applicable capability → resolve context → choose supported resolution depth → evaluate response/effect interactions → preview where available → commit through canonical owner(s) → emit Event/receipts → propagate typed downstream consequences`.

### 7.2 `InteractionEvaluationReceipt`

The evaluation receipt records enough information to explain the result without duplicating canonical state:

- operation/Action/Event ID;
- affordance definition/version;
- actor/tool references where visible/authorized;
- target/facet reference;
- selected capability binding;
- response profile IDs/versions;
- relevant context profile IDs/versions;
- selected resolution profile;
- applicable effect-interaction rule IDs;
- result class;
- proposed/committed owner deltas by reference;
- unresolved/rejected reasons;
- deterministic seed if one was legitimately used;
- provenance and permission-safe explanation data.

### 7.3 Outcome classes

At minimum:

- `success`
- `partial`
- `failure`
- `blocked_by_precondition`
- `unsupported_by_target`
- `unsupported_by_definition`
- `insufficient_known_detail`
- `conflict_requires_resolution`
- `stale_revalidate`
- `cancelled_or_interrupted`.

### 7.4 Commit authority

Evaluation never grants mutation authority. Actual changes route to the canonical target/transaction owners.

Examples:

- crafting/transformation → MIB-12;
- Asset condition/install/uninstall → Asset owner/MIB-12/MERA as applicable;
- Character/Creature condition/body change → respective owner + Action/Effect;
- Environment/World change → Environment/World owner;
- construction damage/repair → MBES plus existing owners;
- engineering change → MERA plus MIB-12/Asset/vehicle owners;
- spatial-law change → MSLR/Transition/World owners as applicable.

---

## 8. Resolution depth

### 8.1 Shared semantic model

The same affordance ID survives all supported resolutions.

#### Abstract

Use the minimum supported semantic contract: actor intent, target, capability, governing response profile and typed outcome/delta. Appropriate for tabletop, offscreen or quick GM resolution.

#### Standard

Expose important target facet(s), tools/resources, major intermediate Conditions/Effects and visible consequences.

#### Detailed

May resolve named components/interfaces/material layers/networks/propagation steps only where authoritative definitions support them.

### 8.2 Refinement

Refinement is allowed when:

- the owner already has finer canonical detail; or
- an authorized deterministic/seed-governed generation/refinement contract can create proposed detail and the owning workflow explicitly accepts/promotes it.

Otherwise finer detail remains unresolved.

### 8.3 Collapse

Detailed execution collapses back to owner state plus Event/receipts. It must not leave a shadow per-pixel/per-component ledger that contradicts the owner.

Information such as exact component lineage, contamination history, donor provenance, or causal Event history is not discarded merely because a higher-level projection summarizes it.

---

## 9. Specialist-domain semantics

### 9.1 MRCS

MRCS authors and validates affordance definitions, capability bindings, response profiles and effect-interaction rules. It provides schema-aware forms, dependency inspection, compatibility/versioning and simulation previews. It does not execute live world mutation.

### 9.2 GPR

GPR imports semantic IDs and executes reusable interaction patterns across delivery modes. It owns deterministic command/runtime composition, not target-domain truth. GPR-15 conformance should validate that registered semantic operations behave consistently across supported variants without requiring every target to support every operation.

### 9.3 MERA

MERA consumes shared semantics for inspect, isolate, depower, disconnect, dismantle, repair, patch, replace, connect, power, calibrate, stabilize and related engineering operations. MERA-specific safety/access/compatibility/topology remains MERA-owned and profile-driven.

### 9.4 MBES

MBES consumes shared semantics for construction/material/environment interactions, utilities, excavation, damage/fire/failure/repair and infrastructure. MBES material behavior remains authored/profile-driven rather than universal physics.

### 9.5 MSLR

MSLR may contribute context that changes applicability or response: gravity frame, metric geometry, containment/scale, spatial-law constraints, reality seams or authored impossible-space rules. MSLR does not redefine the generic affordance registry.

### 9.6 MSWI

MSWI consumes committed typed deltas/events and propagates explicitly authorized systemic consequences. It does not calculate the base interaction merely to create more fan-out.

---

## 10. Player / GM / creator UX

### 10.1 Five-second interaction surface

When an interaction is available, the user should be able to see, subject to permissions:

- semantic action name;
- target/facet;
- whether it is currently available, blocked, unsupported or uncertain;
- obvious required tool/resource/access condition;
- selected resolution depth;
- previewable major consequences when rules allow them.

### 10.2 Explanation

An inspector can answer:

- why is this action available/unavailable?;
- which capability made it applicable?;
- which response/environment/spatial rules were used?;
- what Effect interactions occurred?;
- what owner actually committed the resulting state?;
- what remains unknown?;
- why did a seemingly similar target behave differently?

Protected weakness/property information is filtered before explanation.

### 10.3 Creator authoring

Creator workflows provide:

- reusable affordance selection rather than free-text-only verbs;
- capability/target selector authoring;
- response-profile authoring;
- effect-composition rule authoring;
- scope/precedence/version review;
- conflict/cycle diagnostics;
- abstract/standard/detailed preview;
- test-vector execution;
- dependency/impact view.

### 10.4 GM control

The GM may select resolution depth, choose among legal adjudication options where the rules delegate choice, approve proposed custom interactions, and author setting-specific rules. GM intervention still uses canonical owner operations and Event history; it does not bypass ownership.

### 10.5 Accessibility

No consequential affordance may require a visual animation, color-only state, precision drag, audio-only cue or haptic-only cue as its sole semantic channel. Operation availability, target state, rule interaction, outcome and conflicts require text/structured equivalents suitable for keyboard and assistive technologies.

---

## 11. Permission, visibility and knowledge

Filtering occurs before:

- affordance menus;
- target-facet disclosure;
- weakness/resistance explanation;
- response-profile details;
- effect-composition graphs;
- search/counts;
- previews;
- diagnostics;
- exports;
- simulation/advisory input;
- optional-AI context.

A player may be allowed to attempt an operation without being told the target's hidden resistance or exact response rule.

The engine can produce a permission-safe result such as `attempt_allowed; response_detail_hidden` without leaking hidden rules.

---

## 12. Provenance, history, replay and recovery

Every consequential committed interaction is attributable to:

- source Action/Event;
- actor/initiator where applicable;
- affordance definition/version;
- target capability/response profile versions;
- context/spatial/environment profile versions;
- effect-interaction rule versions;
- deterministic seed where authorized;
- canonical owner operations/deltas;
- resulting Event/receipt IDs.

Editing a reusable profile is prospective unless an explicit migration/reconstruction process is invoked. Historical Events retain the profile/version actually used.

Undo is not assumed. Where an owner supports reversal, a compensating/reversal operation creates new Event history rather than erasing the original occurrence.

---

## 13. Failure and edge-case closure

### Missing target capability
Return `unsupported_by_target`; do not fabricate capability.

### Capability exists but no response rule
Return `unsupported_by_definition` or `requires_owner_adjudication`; do not infer real-world behavior.

### Hidden response property
Allow or reject the attempt using authorized internal resolution while filtering protected explanation.

### Contradictory scoped response rules
Use existing explicit scope/precedence/compatibility semantics; unresolved conflict blocks automatic resolution.

### Circular effect interaction
Detect before or during bounded propagation and fail closed/stop at the last valid state with diagnostic evidence.

### Target changes between preview and commit
Return `stale_revalidate`; re-resolve against current owner state.

### Partial multi-owner commit
Use existing transaction/compensation rules. Never report an atomic success if only some authoritative owner mutations committed.

### Unsupported detailed resolution
Fall back only if the selected rules allow a coarser equivalent. Otherwise report unsupported depth.

### Provider/tool unavailable
Blocking interaction resolution remains local/rule-driven. Optional AI/tools are advisory only.

### Spatial-law contradiction
MSLR/World/Transition owner rules determine the interaction context; generic affordance logic does not overrule spatial authority.

### Source-unspecified fantastical property
Remain unresolved until authored/accepted. Do not map by superficial similarity to a real-world substance.

---

## 14. Golden validation vectors

Future implementation must automate equivalent proofs. IDs are stable PDCP design references.

| ID | Fixture / operation | Required proof |
|---|---|---|
| PDCP-AFF-001 | Rope exposes `cuttable`; valid cutting tool | same `cut` affordance resolves through governed Action/Effect and target owner |
| PDCP-AFF-002 | Steel door lacks authored cutting response | engine does not invent real-world cutting behavior |
| PDCP-AFF-003 | Two targets share `cuttable` but different response profiles | same affordance produces profile-specific outcomes without bespoke verbs |
| PDCP-AFF-004 | Hidden creature resistance | attempt may resolve without leaking hidden resistance in UI/receipt projection |
| PDCP-AFF-005 | `burn` against authored combustible target | governed Effect created and target/environment owner receives typed delta |
| PDCP-AFF-006 | `burn` against source-unspecified fantasy material | unresolved/unsupported rather than assumed combustion |
| PDCP-AFF-007 | World profile disables ordinary combustion | contextual response overrides ordinary scoped default through explicit precedence |
| PDCP-AFF-008 | `freeze` + active heat Effect has explicit cancellation rule | composition follows named rule and receipt cites it |
| PDCP-AFF-009 | Two Effects have no interaction rule | no invented cancellation/amplification occurs |
| PDCP-AFF-010 | Effect A transforms Effect B into named Effect C | resulting Effect C and causal receipt are deterministic |
| PDCP-AFF-011 | Cyclic A→B→A trigger rules | cycle is bounded/rejected; no infinite loop |
| PDCP-AFF-012 | Propagation across finite adjacent target set | each target processed once per authored propagation contract |
| PDCP-AFF-013 | `repair` on repairable Item | mutation routes to MIB-12/Asset owner rather than generic affordance ledger |
| PDCP-AFF-014 | `repair` without required tool/resource | blocked precondition produces no owner mutation |
| PDCP-AFF-015 | Engineering `depower→disconnect→repair→connect→power` | MERA sequencing composes shared semantic operations without losing specialist authority |
| PDCP-AFF-016 | MBES damaged wall `patch` at abstract resolution | same semantic operation yields summarized owner delta/Event |
| PDCP-AFF-017 | Same wall at detailed component resolution | detailed facet used only when authoritative detail exists |
| PDCP-AFF-018 | Detailed UI requests nonexistent wall-layer data | unresolved/fallback; no fabricated layer |
| PDCP-AFF-019 | `breach` against vehicle component | target component owner/vehicle authority commits result, not GPR |
| PDCP-AFF-020 | `connect` incompatible interfaces | MERA/compatibility rule rejects; affordance does not invent adapter |
| PDCP-AFF-021 | Valid explicit adapter | same `connect` affordance succeeds through governed compatibility path |
| PDCP-AFF-022 | `power` target with unavailable resource network | precondition blocks with permission-safe explanation |
| PDCP-AFF-023 | MSLR gravity/spatial context alters movement interaction | spatial owner context changes applicability without rewriting affordance definition |
| PDCP-AFF-024 | Reality law changes material response | versioned contextual profile governs result and is cited in receipt |
| PDCP-AFF-025 | Preview then concurrent target change | commit returns `stale_revalidate` and does not apply stale result |
| PDCP-AFF-026 | Multi-owner operation partially fails | transaction reports partial/compensated state; no false atomic success |
| PDCP-AFF-027 | Abstract and detailed modes replay same accepted semantic intent | both map to the same affordance identity and owner outcome class |
| PDCP-AFF-028 | Effect interaction order is semantically commutative | deterministic receipt ordering does not create false mechanical priority |
| PDCP-AFF-029 | Noncommutative effects lack explicit precedence | automatic resolution blocks with conflict diagnostic |
| PDCP-AFF-030 | `dismantle` produces salvage candidates | dismantle routes through MERA/MIB-12/LSS owner boundaries; no duplicate loot creation |
| PDCP-AFF-031 | `harvest` creature with authored anatomy/yield | uses existing anatomy/harvest owner definitions and Event provenance |
| PDCP-AFF-032 | `harvest` creature lacking anatomy/yield | unresolved rather than invented organs/materials |
| PDCP-AFF-033 | hidden target facet exists | unauthorized search/count/graph does not reveal it |
| PDCP-AFF-034 | creator edits response profile v2 | old Event replay still references v1; new interactions use v2 prospectively |
| PDCP-AFF-035 | explicit compensating reversal | original Event remains; reversal creates new Event/receipt |
| PDCP-AFF-036 | optional AI recommends interaction | recommendation cannot create capability, response rule or commit mutation |
| PDCP-AFF-037 | custom setting affordance | namespaced extension passes registry/version/ownership validation |
| PDCP-AFF-038 | unsupported custom affordance on target | rejected without fallback to string-matching heuristics |
| PDCP-AFF-039 | effect propagation creates systemic world consequence | base interaction commits first; MSWI consumes typed event/delta afterward |
| PDCP-AFF-040 | accessibility projection | keyboard/text/structured explanation provides full consequential semantics without visual/audio-only dependency |

---

## 15. Residual implementation mapping

Packet closure does not alter tranche counts. It pre-closes design obligations to be absorbed into existing implementation tranches.

### MRCS

Primary targets:

- MRCS-02 — registry/schema-aware representation;
- MRCS-04 — predicates/selectors/expression constraints;
- MRCS-05 — Action/Effect/Condition/Resource authoring;
- MRCS-10 — Item/equipment capability/response binding;
- MRCS-11 — supernatural interaction profiles;
- MRCS-13 — vehicle/construct/component bindings;
- MRCS-14 — environment/hazard/material response authoring;
- MRCS-16 — scope/override/compatibility semantics;
- MRCS-17 — dependency/conflict/cycle impact analysis;
- MRCS-18 — simulation/playtest harness;
- MRCS-20 — version/provenance/diff;
- MRCS-21 — cross-domain golden proof.

### GPR

Primary targets:

- GPR-02 — semantic registry/import;
- GPR-03 — target/entity/runtime state seam;
- GPR-04 — interaction core;
- GPR-06 — specialist modules consuming shared affordances;
- GPR-08 — pattern composer/data-driven schema;
- GPR-09 — resolution/delivery-mode parity;
- GPR-12 — deterministic event trace/replay;
- GPR-13 — persistence/version compatibility;
- GPR-14 — creator/GM interaction UX;
- GPR-15 — semantic-operation conformance;
- GPR-16 — cross-system proof.

### MERA

Primary targets:

- MERA-03/04 — preview and compatibility;
- MERA-06 — isolation/access/disassembly sequencing;
- MERA-07 — repair classes;
- MERA-10/11 — dependencies/networks;
- MERA-17/18 — damage/salvage/refurbishment;
- MERA-20 — bypass/jury-rigging;
- MERA-22 — validation/test bench;
- MERA-24 — golden proof.

### MBES

Primary targets:

- MBES-03 — materials/structural properties;
- MBES-08/09 — utilities and condition→action networks;
- MBES-12/13 — terrain/hydrology interactions;
- MBES-15/16 — world/environment conditions;
- MBES-18/19 — damage/fire/failure/repair/hazard response;
- MBES-24 — golden proof.

### MSLR

Direct contextual integration only:

- MSLR-02 — scoped law composition;
- MSLR-06 — governed spatial operations;
- MSLR-08/10/12 — metric/orientation/causal contexts where they alter interaction applicability;
- MSLR-16 — cross-system multi-resolution integration;
- MSLR-18 — golden proof.

MSLR does not own the generic affordance registry.

### MSWI

Primary consumption/proof targets:

- MSWI-03 — consequence routing;
- MSWI-07/08 — anatomy/embodied modification where owner definitions exist;
- MSWI-10 — profession/daily-life composition;
- MSWI-15 — persistent environment-state presentation from committed changes;
- MSWI-17 — interaction/fan-out diagnostics;
- MSWI-18 — systemic golden proof.

### No direct new Packet-04 obligation

MCS, MCCS, MNCS and MSAS require no standalone Packet-04 implementation tranche. They may consume the shared semantics through their existing integration contracts. MAS is excluded from PDCP and remains completed.

---

## 16. Roadmap-reduction implication

Packet 04 requires:

- **0 new families**;
- **0 new standalone tranches**;
- **0 immediate roadmap-count mutations**.

The packet materially pre-closes design obligations inside MRCS, GPR, MERA, MBES, MSLR and MSWI. Those obligations become candidates for merge/absorption during later family-specific PDCP reduction receipts.

No tranche may be removed solely because Packet 04 exists; each family reduction must prove that code/UI/schema/integration/migration/performance/golden obligations are preserved by surviving implementation tranches.

---

## 17. Acceptance conclusion

All benchmark-derived Packet-04 product questions have an implementation-ready disposition:

- reusable affordances are semantic operations, not automatic outcomes;
- target support is capability/profile-driven;
- material/environment behavior is source/setting/reality-governed, not universal pseudo-physics;
- effect composition is explicit, versioned and bounded;
- abstract/tabletop and detailed runtime modes share one semantic contract;
- unknown lower-level properties remain unknown;
- canonical mutation always remains with existing owners;
- visibility filtering precedes explanation, diagnostics and AI context;
- replay cites the actual definition/profile versions used;
- 40 golden vectors define future proof obligations;
- no owner decision remains open;
- no new family or standalone tranche is required.

**PDCP Packet 04 is DESIGN_CLOSED.**
