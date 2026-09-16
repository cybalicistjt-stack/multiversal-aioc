# PDCP Packet 06 — Multi-Resolution Simulation & Autonomous World Evolution — Design Closure

**Project:** PDCP — Preimplementation Design Closure Project  
**Packet:** PDCP-PACKET-06  
**Status:** DESIGN_CLOSED  
**Date:** 2026-09-16  
**Implementation authority:** none  
**Roadmap-count mutation:** none  
**MAS:** excluded and not reopened

## 1. Purpose

Close the benchmark-derived design gap exposed by Songs of Syx, Soulash 2, X4, Rain World and agent-based simulation practice without creating a second World, Environment, Character/NPC/Creature, Population, Organization, Settlement, Economy, Project/Time, Action/Event or history ledger.

Packet 06 defines the reusable contracts that let Multiversal vary **simulation resolution** safely:

- summarize large populations, organizations, settlements, ecological cohorts and economic/world processes without materializing every individual;
- refine selected aggregates into cohorts or persistent individuals when play needs detail;
- collapse active detail later without deleting canonical identities or history;
- advance offscreen/large-scale state through bounded owner-approved aggregate transitions;
- interact across detailed and aggregate layers without double counting;
- preserve uncertainty honestly instead of turning rough population bands into fake exactness;
- enforce simulation/performance budgets without skipping required owner commits;
- compose world evolution across owner domains through attributable Events and MSWI consequence routing.

The packet is a **resolution/orchestration contract**, not a universal life simulator.

## 2. Existing authority absorbed rather than duplicated

Packet 06 consumes and preserves existing authority.

| Concern | Preserved authority/boundary |
|---|---|
| NPC/creature/group/population progressive detail | **MNCS** already defines progressive NPC/person and creature resolution, settlement/organization population generation, herd/pack/swarm/ecosystem cohorts, promotion/demotion/retirement and continuity. |
| Autonomous decisions and offscreen action | **PDCP Packet 03** already defines actor-relative autonomy, legal operations, canonical-time triggers, offscreen batch receipts and the rule that aggregate resolution may not fabricate individual actions. |
| Historical truth and burn-in | **PDCP Packet 05** already defines immutable Event history, history-resolution semantics, delayed consequences and proposal-only seeded burn-in. Packet 06 may refine simulation state but cannot retroactively manufacture history. |
| Profession, enterprise, household and life context | Completed **DPL** retains profession, business, workforce, household/family, production and life-loop owner seams. |
| Organization state and GM simulation-depth presentation | Completed **ODL** retains organization capacity, coordination, resources, roles, crisis/recovery and read-only GM simulation-depth/advisory presentation. ODL-08 does not create a second simulation engine. |
| Strategic conflict/command | Completed **SCL** retains strategic command, formations, order resolution and strategic consequence authority. |
| World/environment/place truth | **World / Environment / Reality / Branch / Settlement** owners remain canonical for place, climate, ecology, demographics, settlement state and world facts. |
| Economy/resources/assets | **MIB-13 / Economy / Resource / Inventory / Asset** owners retain prices, markets, ownership, quantities, transfers, production resources and economic truth. |
| Campaign/project time | **APW/D26 Project/time** remains canonical for campaign time, long-running work and bounded task progression. |
| Canonical mutation/history | **Action/Event and each owning domain** remain the only authoritative commit paths for consequential state. |
| Variable-resolution built environment | **MBES** already defines settlement/district→site→structure→room→component/network resolution and upward settlement/services/logistics/economy integration. |
| Definition/profile authoring and evidence | **MRCS** remains the future authoring surface for reusable rules/profiles and simulation evidence. |
| Deterministic execution, replay and persistence | **GPR** remains the future reusable runtime for deterministic state, bounded gameplay execution, replay, snapshots and migration. |
| Cross-system world response | **MSWI** already owns planned world-transformation routing, ecology succession/population bands, migration/food webs, grand Projects and interaction-loop diagnostics. |

## 3. Foundational invariants

1. **Aggregate state is not a hidden crowd of invented people.** An aggregate is owner-backed summarized state or a governed projection. Unmaterialized individuals have no private exact biography, inventory, wounds, conversations or memories unless an owner actually created that data.
2. **Refinement cannot retroactively invent history.** When a cohort or individual is refined after aggregate simulation, the system may generate current candidate detail under a declared profile, but it may not claim that exact personal events happened in the past unless those Events were actually generated/accepted then.
3. **Persistent identity is owner-minted.** Only the canonical Character/NPC/Creature/other identity owner creates a persistent entity identity. A sampled representative, statistical exemplar or UI row is not automatically a person.
4. **Collapse reduces active detail, not identity.** Once a persistent identity exists, lowering simulation resolution may make it dormant/archived/summarized but cannot silently dissolve it back into anonymity or erase its Event history.
5. **No double counting across resolutions.** A person, creature, Asset, resource quantity, workforce capacity or other owner-defined exclusive unit may not simultaneously remain in an aggregate remainder and count again as an individualized/refined unit.
6. **Uncertainty cannot become false precision.** A range, band, distribution or unknown aggregate remains that uncertain until an owner-backed operation legitimately resolves more detail.
7. **No universal population physics.** Birth, death, migration, employment, prices, production, carrying capacity, disease, predation and other processes use explicit owner/rules profiles. Packet 06 invents no generic formulas.
8. **Canonical time, not wall clock, drives world evolution.** Closing the app for a week does not advance the Campaign unless a separately governed Campaign-time policy says so.
9. **Aggregate advancement is still canonical work.** Batching or bulk resolution may reduce event/detail volume only where the owner supports an aggregate operation. It is not permission to skip validation or owner commits.
10. **Performance pressure never grants authority.** A budget can reduce nonessential detail, defer work, request GM adjudication or fail safely. It cannot fabricate a result simply because detailed simulation is expensive.
11. **Cross-domain evolution is attributable.** Economy/ecology/settlement/organization/world interactions route through explicit owner operations and Events, with MSWI coordinating fan-out rather than becoming a new world ledger.
12. **Player-facing resolution must not leak hidden truth.** Refinement priority, hidden population partitions, secret actors and aggregate counts are filtered before display/search/AI/diagnostics.

## 4. Canonical distinctions

Packet 06 keeps these concepts separate:

- **owner state** — canonical state held by an existing owner;
- **aggregate projection/state** — summarized owner-backed representation at a chosen resolution;
- **cohort** — explicit owner/profile-defined subgroup with shared relevant properties, not necessarily a persistent entity;
- **representative sample** — noncanonical exemplar used for presentation/preview/statistical illustration;
- **persistent individual** — owner-minted stable identity with its own history/state;
- **resolution profile** — rules for how much identity/state/time/space/causality/record detail is active;
- **refinement** — move from coarser to finer representation;
- **individualization/promotion** — explicit owner operation that creates/accepts a persistent identity from eligible aggregate provenance;
- **collapse** — reduce active simulation detail while preserving canonical identities/history;
- **aggregate transition** — owner-approved summarized state transition;
- **offscreen catch-up** — bounded advancement across canonical time/Event distance using declared detailed or aggregate methods;
- **world evolution step** — orchestration receipt linking owner transitions and cross-system consequences;
- **simulation budget** — performance/complexity bounds, never game authority.

## 5. Resolution model

Packet 06 does not impose one universal hierarchy on every domain. Instead, a `SimulationFidelityProfileDefinition` declares supported modes and dimensions.

Common semantic modes are:

1. `projection_only` — read-only summary; no autonomous advancement;
2. `aggregate` — owner-backed summarized state and bulk transitions;
3. `cohort` — several explicit subgroups without mandatory individual identity;
4. `individual` — persistent individual entities and individual operations where supported;
5. `adaptive_mixed` — different parts of the same scope use different modes concurrently.

A domain may map these to its own existing ladder. Examples:

- MNCS person: population member → extra → minor → recurring → full/major;
- MNCS creature: population → herd/pack/swarm → encounter member → persistent individual;
- MBES: settlement/district → site → structure → room → component/network;
- an economy may support sector/market/merchant/item detail without pretending those are the same kind of hierarchy.

### 5.1 Fidelity dimensions

A profile may independently control:

- `identity` — aggregate/cohort/individual identity detail;
- `state` — how many owner-backed state dimensions are actively represented;
- `temporal` — event-driven, interval-batched or stepwise advancement;
- `spatial` — region/site/local/exact-owner positioning as supported;
- `causal` — net effect, typed transition or explicit operation chain;
- `recording` — summary receipt, grouped Events or individual Event detail.

Increasing one dimension does not require increasing all others.

## 6. Reusable contracts

### 6.1 `SimulationFidelityProfileDefinition`

Reusable MRCS/owner-authored definition describing allowed resolution for a scope.

Minimum semantics:

- stable profile ID/version;
- applicable owner/entity/process kinds;
- supported resolution modes;
- fidelity dimensions and permitted values;
- canonical trigger/cadence rules;
- allowed aggregate transition definitions;
- allowed refinement and collapse rules;
- uncertainty/quantity representation policy;
- identity-promotion policy;
- persistent-identity pinning rules;
- interaction-forces-refinement rules where applicable;
- performance/budget profile reference;
- deterministic seed/version policy where stochastic behavior exists;
- visibility/knowledge filtering policy;
- recovery/migration behavior;
- provenance/source/rules metadata.

A profile does not itself mutate owner state.

### 6.2 `ResolutionScopeBinding`

Binds a fidelity profile to a Campaign/World/Region/Settlement/Organization/ecosystem/market/population/etc. scope.

It records:

- scope owner reference and version;
- active profile/version;
- optional GM pins/overrides within authorized bounds;
- inherited/default profile source;
- active resolution mode(s);
- effective budget profile;
- canonical time/event boundary;
- visibility policy;
- operation/provenance metadata.

Changing a binding may affect future simulation detail but does not rewrite past Events.

### 6.3 `AggregatePartitionDefinition`

Defines how an owner-backed aggregate may be partitioned without inventing unsupported categories.

Possible partition keys include only accepted owner facts such as:

- species/form/stage;
- role/profession/job;
- household/crew/group affiliation;
- location/site/region;
- faction/organization membership;
- ecological role;
- age/lifecycle band where defined;
- service/housing/employment class where defined;
- resource/product category;
- setting-specific governed dimensions.

Every partition declares quantity semantics: `exact`, `range`, `band`, `distribution` or `unknown`.

Partitioning does not create persistent members by itself.

### 6.4 `AggregateStateProjection`

Read-only or owner-produced summarized state for a scope.

It may contain:

- aggregate/cohort IDs where the owner supplies them;
- owner scope/version;
- partition/profile version;
- exact/range/band/distribution/unknown quantities;
- summarized owner-backed capabilities/state;
- individualized/pinned-member exclusion refs;
- aggregate remainder quantity/state;
- current canonical time/Event bound;
- source/provenance;
- visibility filtering.

A projection must disclose uncertainty class. UI rounding may not silently turn a range into an exact count.

### 6.5 `AggregateTransitionDefinition`

Defines an owner-approved summarized transition, such as population growth/decline, migration pressure, production/consumption, service-capacity change, workforce reassignment, ecological recovery, market shortage response or settlement occupancy shift.

Required semantics:

- transition ID/version;
- owner domain;
- eligible aggregate scopes;
- required inputs and owner versions;
- method class;
- deterministic formula/rules reference or seeded stochastic policy where applicable;
- canonical time/Event step semantics;
- preconditions and constraints;
- allowed output deltas/bands;
- threshold/event emission rules;
- interaction with individualized exclusions;
- uncertainty propagation rules;
- blocked/unresolved behavior;
- provenance/replay metadata.

Permitted method classes are:

- `deterministic_rule`;
- `seeded_stochastic`;
- `owner_bulk_resolver`;
- `gm_adjudicated`;
- `advisory_only`;
- `custom_governed`.

There is no universal demographic, ecology or economic equation.

### 6.6 `AggregateAdvanceReceipt`

Records one owner-backed aggregate transition evaluation/commit.

It includes:

- scope and input owner versions;
- profile/transition version;
- canonical start/end Event/time bounds;
- method and seed where used;
- input quantity certainty;
- individualized exclusion set;
- proposed and committed owner changes;
- grouped/summary Events produced;
- threshold crossings;
- unresolved/blocked outputs;
- resulting aggregate projection ref;
- replay/provenance.

The receipt cannot later be expanded into exact unnamed individual Events that were never resolved.

### 6.7 `RefinementRequest`

Requests finer representation for a bounded part of an aggregate.

Trigger classes may include:

- direct Player/GM interaction;
- Scene/Encounter placement;
- selected/targeted individual or subgroup;
- named/unique/important persistent entity requirement;
- owner Event requiring finer resolution;
- threshold/exception rule;
- creator/GM inspection;
- explicit simulation-quality request;
- custom governed trigger.

The request identifies the aggregate/partition, requested detail, reason, authorization, profile version and expected owner versions.

### 6.8 `RefinementReceipt`

Records how finer detail was produced.

Possible results:

- expose already-existing persistent identities;
- split one aggregate into owner-backed cohorts;
- generate noncanonical representative candidates;
- request owner individualization/promotion;
- return partial detail because some fields remain unknown;
- reject because refinement is unsupported/unauthorized/stale.

A refinement receipt must retain the parent aggregate/partition provenance and quantity/accounting relationship.

### 6.9 `IndividualizationPromotionRequest`

Requests creation/acceptance of a persistent identity from eligible aggregate provenance.

Minimum semantics:

- source aggregate/cohort and profile/version;
- candidate/current detail supported by source data;
- owner identity type requested;
- atomic membership/allocation semantics;
- fields that are accepted facts versus generated candidates versus unresolved;
- exact quantity impact when the source aggregate is exact and exclusive;
- expected owner versions;
- authorization/GM acceptance where required;
- stable operation/correlation ID.

The identity owner may reject, modify or require human choice.

### 6.10 `IndividualizationPromotionReceipt`

On success, records:

- newly minted persistent owner identity;
- source aggregate/cohort provenance;
- exact accepted definition/profile versions;
- aggregate remainder update or explicit nondepleting rule;
- inherited aggregate facts that legitimately apply;
- unresolved personal facts;
- owner Event/result IDs;
- operation/idempotency evidence.

The receipt never claims individual historical experiences absent canonical history.

### 6.11 `CollapseRequest`

Requests lower active simulation detail for a detailed scope or persistent identity set.

Reasons may include leaving active play, distance, inactivity, GM choice, budget pressure or profile transition.

A collapse request must identify:

- identities/cohorts/scope;
- target resolution;
- facts/history that must remain pinned;
- aggregate owner target if reintegration is supported;
- expected versions;
- pending operations that prevent collapse;
- visibility/provenance.

### 6.12 `CollapseReceipt`

Records detail reduction without identity loss.

Rules:

1. persistent identities remain persistent IDs;
2. canonical Event history remains accessible under retention/visibility rules;
3. unique/named/individually significant state is not averaged away into anonymous aggregate truth;
4. owner-supported summary fields may roll up into aggregate state;
5. exclusive membership/accounting is updated exactly once;
6. dormant/archived identities remain excluded from aggregate remainder where owner semantics require it;
7. re-expansion resolves the same identity, not a regenerated replacement.

### 6.13 `RepresentationCoverageReceipt`

A read-only accounting proof for mixed-resolution scopes.

It records:

- aggregate scope/version;
- aggregate remainder quantity/certainty;
- cohort partitions;
- individualized persistent-member refs;
- nondepleting representative refs, clearly marked;
- exclusions/reservations;
- total-accounting check where an exact total exists;
- overlap/duplicate diagnostics;
- unresolved coverage gaps.

This is not a second population/resource ledger. It proves that the owner projection is represented coherently.

### 6.14 `CrossResolutionInteractionRequest`

Represents an interaction where participants/targets exist at different resolutions.

Examples:

- a detailed Character buys from an aggregate market;
- a combat/harvest Event affects an aggregate creature population;
- a settlement policy affects summarized households;
- a storm affects a region while only some named NPCs are individualized;
- a detailed factory consumes from an aggregate regional supply projection.

The request must choose one of:

1. use an explicit owner aggregate operation;
2. force bounded refinement before resolving;
3. resolve only the detailed participants while emitting an aggregate owner consequence;
4. block/require GM adjudication when no lawful cross-resolution rule exists.

### 6.15 `CrossResolutionInteractionReceipt`

Records:

- detailed and aggregate participants;
- governing profile/rule versions;
- whether refinement occurred;
- exact owner operations issued;
- quantity/accounting effects;
- Event IDs;
- unresolved detail intentionally left unknown;
- evidence/provenance.

Mass effects cannot assign named injuries, deaths, inventory losses or memories to previously unmaterialized individuals unless the owner rule explicitly resolves those identities.

### 6.16 `OffscreenCatchUpPlan`

A bounded plan for advancing from canonical boundary A to B.

It specifies:

- scope(s) and owner domains;
- start/end canonical time or Event boundary;
- active fidelity profiles;
- transition/cadence sequence;
- deterministic seeds/method versions;
- threshold/interruption points that force segmentation/refinement;
- owner dependencies/order constraints;
- performance budget;
- maximum aggregate/refinement fan-out;
- failure/defer/GM-required behavior;
- checkpoint strategy.

Wall-clock elapsed time is never substituted for Campaign time.

### 6.17 `OffscreenCatchUpReceipt`

Records:

- exact canonical bounds advanced;
- owner transitions attempted/committed;
- aggregate versus detailed steps;
- seeds/profile versions;
- threshold/refinement stops;
- deferred/blocked work;
- grouped and individual Events actually created;
- checkpoints;
- replay/recovery evidence;
- resulting owner versions.

Catch-up may be intentionally incomplete. The system reports the unadvanced remainder rather than pretending completion.

### 6.18 `SimulationBudgetProfile`

Defines technical/complexity limits independently from game-world facts.

Possible limits include:

- active detailed identities;
- active cohorts/aggregate scopes;
- refinement fan-out per operation;
- aggregate transition count per bounded advance;
- maximum catch-up segments;
- event/receipt expansion limits;
- memory/storage budget classes;
- deterministic work-unit limits;
- optional compute-time watchdogs that affect execution control only, never Campaign time.

Budget policy also defines degradation order.

### 6.19 `SimulationBudgetDecisionReceipt`

When a budget changes execution detail, record:

- requested fidelity;
- available budget/profile;
- protected/pinned identities and owner operations;
- reduction/defer/collapse choice;
- affected scopes;
- unprocessed work;
- whether GM attention is required;
- no-authority-bypass proof.

Safe degradation preferences are profile-defined, but commonly favor preserving directly interacted, persistent/named, Scene-active, unresolved-consequence and GM-pinned entities over background detail.

Hidden priority reasons are filtered from unauthorized users.

### 6.20 `WorldEvolutionStepReceipt`

A cross-domain orchestration receipt used when one accepted change propagates into several owners.

It records:

- initiating Event/time boundary;
- owner transitions evaluated;
- dependency/order graph/version;
- each owner request/result;
- aggregate/detailed resolution used per domain;
- MSWI consequence-route refs;
- threshold/loop/cycle diagnostics;
- deferred/blocked paths;
- resulting canonical Events and owner versions.

It is not a world-state ledger. The receipt only links what canonical owners actually committed.

## 7. Aggregate membership, partitioning and accounting

### 7.1 Exact totals

When an owner has an exact population/resource/capacity total and partitions are exclusive, splits and individualization must reconcile exactly:

`total = aggregate remainder + exclusive cohorts + individualized exclusive members`

The equation is an accounting invariant, not a universal biological/economic law.

### 7.2 Ranges, bands and distributions

If the owner knows only `40–60`, `scarce`, a distribution, or `unknown`, refinement cannot claim an exact total without a legitimate resolving operation.

A generated individual may be created from such a population only if the owner/profile permits it; the aggregate uncertainty must be updated conservatively rather than falsely producing exact arithmetic.

### 7.3 Overlapping facets

Some groupings overlap: one person can be both a farmer and militia member; one Asset can serve two capabilities. Such facets are not summed as exclusive partitions. The partition definition must mark exclusivity/overlap semantics.

### 7.4 Representative samples

A UI may show “typical resident,” “typical wolf,” “representative worker” or similar noncanonical examples. These are explicitly marked `representative_sample` and cannot be targeted, killed, paid, promoted, remembered or counted as a real individual until a governed individualization step occurs.

## 8. Refinement and identity semantics

### 8.1 Refinement sources

Refinement may use only:

- already-authoritative owner facts;
- accepted definitions/profile constraints;
- retained aggregate history/context;
- deterministic/seeded generation rules declared by the profile;
- explicit GM/player choices;
- optional AI candidate suggestions from authorized context.

### 8.2 What refinement may not invent

Refinement may not silently manufacture:

- prior conversations;
- exact prior injuries/deaths;
- exact item ownership;
- hidden relationships;
- personal memories;
- exact schedules/actions during an aggregate period;
- individual blame/credit for aggregate outcomes;
- precise ancestry/lineage;
- secret knowledge;
- historical witnesses.

Those require actual owner data, accepted generated history or explicit reconstruction/promotion under Packet 05.

### 8.3 Stable identity after promotion

Once owner-minted:

- the same identity is reused in later Scenes/Encounters;
- regeneration cannot replace accepted lived facts;
- collapse/dormancy cannot destroy identity;
- aggregate provenance remains queryable;
- if the identity changes cohort/settlement/faction, owner operations update membership rather than minting a clone.

## 9. Collapse and reintegration

Collapse is allowed only when pending owner operations and required high-detail resolution are settled or explicitly carried forward.

A persistent individual may become:

- dormant;
- archived;
- offscreen summarized;
- cohort-associated;
- represented through a compact continuity projection.

But the system retains enough information to recover the same identity and historical state.

If an owner allows reintegration into an aggregate quantity, it must define whether the persistent individual remains separately enumerable/excluded or becomes an included named member while still retaining identity. Packet 06 does not assume one model.

## 10. Aggregate transition and world-evolution semantics

### 10.1 Owner-specific transitions

Population/economy/ecology/world evolution uses explicit owner rules. Examples may include:

- migration;
- recruitment/attrition;
- reproduction/lifecycle transitions;
- harvest/overhunting recovery;
- resource production/consumption;
- market shortage/surplus response;
- staffing/workforce changes;
- settlement occupancy/service demand;
- construction/logistics capacity changes;
- disease/hazard spread;
- habitat suitability change;
- organization growth/fragmentation;
- strategic conflict consequences.

No example implies a required universal formula.

### 10.2 Thresholds and discontinuities

A bulk step must stop, segment or emit an explicit threshold Event when crossing a rule-defined discontinuity that changes later legality/behavior.

Examples: capacity exhausted, habitat becomes unsuitable, settlement loses required service, faction breaks apart, route closes, extinction/local extirpation occurs, or a named Project milestone completes.

A bulk resolver may not average across a threshold when the owner rules require different behavior on each side.

### 10.3 Cross-domain sequencing

When one domain feeds another, MSWI supplies the integration route. Packet 06 requires:

1. explicit dependency/order information;
2. bounded cycle handling;
3. no arbitrary UI-list iteration order;
4. owner revalidation before commit;
5. Event/provenance linkage;
6. loop diagnostics rather than hidden infinite reaction chains.

## 11. Offscreen advancement

### 11.1 Canonical cadence

Advancement occurs through canonical Event/time/project triggers. A scope may be event-driven, interval-batched, GM-stepped or owner-bulk-resolved.

### 11.2 Catch-up choices

For a long canonical interval the runtime may:

- execute every due detailed transition;
- use one or more owner-approved aggregate transitions;
- partition into segments around thresholds/events;
- refine only exceptional entities;
- defer selected domains;
- request GM adjudication;
- stop safely when budget or owner data is insufficient.

### 11.3 No retroactive personal detail

If five campaign months were resolved as population bands and grouped Events, later refining one resident does not reveal an exact five-month personal action log. The individual may inherit legitimate current context and aggregate historical facts, but personal history remains unknown unless separately established.

## 12. Interaction across resolutions

A high-detail participant can affect low-detail state only through an explicit cross-resolution rule.

Examples:

- a Character purchases a commodity from an aggregate market: Economy owner commits the transaction and updates market/stock projection as defined;
- a party hunts an aggregate herd: exact killed/captured individuals are created only when the owner requires individual identity; otherwise an aggregate population consequence may suffice;
- a fire affects a settlement district: detailed named residents retain owner identities, while aggregate resident impact uses an owner bulk rule; no invented casualty list;
- a strike affects a workforce cohort: Organization/Economy/Project owners handle capacity/attendance consequences; the system does not invent exact worker motivations.

If no aggregate operation exists and individual resolution is required, the system must refine or stop.

## 13. Fidelity and performance budgets

### 13.1 Fidelity is gameplay-independent control

Fidelity controls how much simulation detail is active. It must not silently change core game rules, probabilities or player-facing mechanical outcomes unless an owner profile explicitly defines resolution-equivalent approximations.

### 13.2 Protected detail

Profiles may pin detail for:

- active Scene/Encounter participants;
- persistent/named entities;
- direct Player targets/contacts;
- unresolved legal/resource/ownership commitments;
- current Project participants;
- imminent rule thresholds;
- GM-pinned entities;
- identities with owner rules that forbid collapse.

### 13.3 Degradation order

When over budget, the system may, according to profile:

1. reduce nonessential presentation detail;
2. batch eligible low-impact transitions;
3. collapse eligible inactive cohorts/entities;
4. defer noncritical offscreen advancement;
5. reduce diagnostic/event expansion while retaining canonical receipts;
6. request GM attention;
7. fail safe.

It may not skip a required cost, transfer, death, ownership change or other canonical consequence while claiming the simulation completed.

## 14. Determinism, stochastic behavior and replay

Where determinism is claimed, replay binds:

- exact owner input versions;
- profile/transition version;
- canonical time/Event bounds;
- partition/refinement rules;
- seed stream;
- budget decisions;
- threshold segmentation;
- owner operation results.

A seeded stochastic aggregate transition may produce a deterministic replay of the same **aggregate result** without implying that every possible member-level history was generated.

Changing a transition/profile later does not rewrite historical receipts.

## 15. Historical integration with Packet 05

Packet 05 remains authoritative for history semantics.

- aggregate Events can be canonical if the owning domain explicitly supports grouped/summary Event semantics;
- refinement cannot turn one grouped Event into invented exact member Events;
- burn-in may run at aggregate/cohort/individual fidelity under Packet-05 proposal-only rules;
- promoted burn-in history records exact resolution/profile/seed used;
- later collapse preserves history references;
- `as_of` projections must state when only aggregate historical evidence exists.

## 16. Autonomous integration with Packet 03

Packet 03 remains authoritative for actor/process autonomy.

Packet 06 adds:

- which actors/processes are actively individualized versus aggregate;
- when an aggregate bulk resolver may stand in for many Packet-03 decision cycles;
- how exceptional members force refinement;
- how offscreen batch receipts preserve resolution provenance;
- how population/world processes advance without fabricating per-actor choices.

An aggregate faction/economy/ecology step is not permission to invent individual motives or conversations.

## 17. Security, permissions and hidden information

Authorization filters apply before:

- aggregate counts;
- partition lists;
- refined-member lists;
- refinement priority explanations;
- individualization candidates;
- hidden faction/creature populations;
- simulation diagnostics;
- catch-up previews;
- budget/pinning explanations;
- exports;
- optional-AI context.

A user cannot infer a secret NPC, hidden army, undiscovered settlement, concealed species population or GM-only plan merely because a mixed-resolution accounting screen contains an extra row/count.

## 18. Failure and recovery semantics

- **Stale aggregate version:** reject/recompute before split, advance or promotion.
- **Identity collision:** canonical identity owner resolves; no duplicate entity is silently created.
- **Exact total mismatch:** block commit and surface accounting conflict.
- **Unknown quantity:** preserve uncertainty; do not coerce to zero or guessed count.
- **Unsupported refinement:** explicit unsupported/GM-required result.
- **Unsupported collapse:** keep current detail or request GM; never delete identity.
- **Pending detailed operation:** collapse waits or explicitly carries state according to owner rules.
- **Budget exceeded:** reduce/defer/fail safely according to profile; no incomplete hidden commit.
- **Bulk step crosses threshold:** segment/stop and reevaluate under new owner state.
- **Cycle across domains:** MSWI-17-compatible loop diagnostic; bounded reaction cap/failure-safe behavior.
- **Ambiguous commit response:** status lookup before retry; no duplicate population/resource mutation.
- **Catch-up interruption:** durable checkpoint and unadvanced remainder.
- **Profile version changes mid-catch-up:** pin current segment/version; new version applies only through explicit migration/restart policy.
- **Player enters an offscreen scope during catch-up:** owner/runtime barrier resolves committed work, then refinement uses the resulting exact canonical boundary.

## 19. Accessibility and creator/GM UX

Essential operations require nonvisual parity:

- hierarchical list/tree view of World→scope→aggregate→cohort→persistent members;
- textual exact/range/band/unknown quantity labels;
- keyboard-accessible refine/collapse/pin/defer controls;
- semantic accounting view showing aggregate remainder versus individualized members;
- text explanation of why a scope is detailed/aggregated/deferred;
- deterministic seed/profile/version display;
- catch-up plan and receipt as ordered text, not animation only;
- threshold/blocked/accounting errors announced without relying on color;
- cross-resolution interaction preview with owner operations listed;
- screen-reader equivalent for graphs, population partitions and evolution fan-out.

Optional AI may summarize authorized simulation receipts or suggest candidate profiles, but all blocking behavior is deterministic/manual-capable and AI cannot create identities, resolve hidden truth, spend resources or commit owner state.

## 20. Golden vectors

Future implementation must automate or equivalently prove these cases.

### Aggregate state and accounting

- **PDCP-SIM-001** — exact population aggregate exists with zero materialized individuals; no hidden personal records are invented.
- **PDCP-SIM-002** — a population known only as a range remains a range in projection and UI.
- **PDCP-SIM-003** — exclusive cohort split preserves an exact owner total.
- **PDCP-SIM-004** — overlapping profession/militia facets are not incorrectly summed as exclusive partitions.
- **PDCP-SIM-005** — representation coverage detects an individualized member still counted in an exclusive aggregate remainder.
- **PDCP-SIM-006** — a nondepleting representative sample is clearly noncanonical and does not change population count.
- **PDCP-SIM-007** — unknown aggregate quantity is not coerced to zero or an invented estimate.
- **PDCP-SIM-008** — hidden aggregate/cohort cannot leak through unauthorized counts or accounting rows.

### Refinement and individualization

- **PDCP-SIM-009** — aggregate settlement resident refines to cohorts without minting NPC identities.
- **PDCP-SIM-010** — fixed-seed candidate refinement reproduces where the profile declares determinism.
- **PDCP-SIM-011** — individualization mints one stable NPC identity and atomically updates exclusive aggregate accounting.
- **PDCP-SIM-012** — retrying individualization cannot mint a duplicate identity or double-decrement the aggregate.
- **PDCP-SIM-013** — refined NPC inherits legitimate settlement/culture facts but receives no invented private memories.
- **PDCP-SIM-014** — a creature promoted from a summarized pack keeps pack/population provenance.
- **PDCP-SIM-015** — unsupported personal field remains unresolved instead of being generated as fact.
- **PDCP-SIM-016** — refinement after five aggregate months does not fabricate a five-month individual action log.

### Collapse and identity continuity

- **PDCP-SIM-017** — recurring NPC collapses to dormant summary while retaining the same persistent identity.
- **PDCP-SIM-018** — re-expanding a dormant NPC returns the same ID and Event history.
- **PDCP-SIM-019** — named unique entity cannot be silently dissolved into anonymous population state.
- **PDCP-SIM-020** — collapse rolls up only owner-supported summary fields and preserves unsupported individual facts separately.
- **PDCP-SIM-021** — pending owner transaction prevents unsafe collapse.
- **PDCP-SIM-022** — two collapse retries cannot double-return an exclusive member to aggregate accounting.

### Aggregate advancement and offscreen catch-up

- **PDCP-SIM-023** — closing the app for real-world time does not advance a Campaign population.
- **PDCP-SIM-024** — canonical Campaign-time advance runs an owner-approved aggregate transition.
- **PDCP-SIM-025** — seeded stochastic aggregate transition reproduces the same aggregate result without inventing member histories.
- **PDCP-SIM-026** — a bulk step encountering an owner threshold segments/stops before applying post-threshold rules.
- **PDCP-SIM-027** — stale owner state invalidates a pending aggregate transition before commit.
- **PDCP-SIM-028** — interrupted catch-up records a checkpoint and exact unadvanced remainder.
- **PDCP-SIM-029** — replay binds the historical transition/profile version rather than current rules.
- **PDCP-SIM-030** — aggregate offscreen combat/ecology result does not fabricate exact unnamed wounds, witnesses or conversations.

### Cross-resolution world evolution

- **PDCP-SIM-031** — detailed Character purchase changes Economy owner state and aggregate market projection through explicit owner operations.
- **PDCP-SIM-032** — hunting an aggregate herd produces a governed population consequence without requiring identities for every animal.
- **PDCP-SIM-033** — when a rule requires a specific target animal, the runtime refines/individualizes before individual combat resolution.
- **PDCP-SIM-034** — settlement housing/service capacity changes feed resident/population projections without duplicating Character or settlement ledgers.
- **PDCP-SIM-035** — habitat degradation routes through Environment→MSWI ecology population-band consequences with provenance.
- **PDCP-SIM-036** — economy/settlement/ecology reaction loop hits a declared bounded-cycle diagnostic instead of recursing indefinitely.

### Budgets, security and accessibility

- **PDCP-SIM-037** — budget pressure collapses eligible background detail while preserving active Scene participants and persistent pinned identities.
- **PDCP-SIM-038** — budget exhaustion defers/fails safely rather than skipping a required owner mutation and claiming completion.
- **PDCP-SIM-039** — optional AI disabled: refinement, aggregate advance, catch-up, replay and budget handling still function.
- **PDCP-SIM-040** — aggregate/cohort/member tree, accounting state, catch-up plan and fan-out diagnostics have keyboard and screen-reader semantic equivalents.

## 21. Future-family implementation mapping

Packet 06 creates **no new family and no standalone implementation tranche**. Residual implementation fits existing planned scopes.

### MNCS

- `MNCS-01` — progressive resolution ladder/no-duplicate-identity contract;
- `MNCS-02` — deterministic generation/seed/provenance for refinement candidates;
- `MNCS-03` — authorized World/Location/Environment/settlement constraint inputs;
- `MNCS-09` — household/work/economy/schedule/project aggregate context;
- `MNCS-12` — ecology/habitat/lifecycle inputs;
- `MNCS-13` — creature behavior/social-group inputs;
- `MNCS-15` — household/crew/crowd/social-group cohorts;
- `MNCS-16` — settlement/organization/population generation and individualization;
- `MNCS-17` — herd/pack/swarm/colony/ecosystem population generation;
- `MNCS-20` — continuity and life/ecology change over time;
- `MNCS-21` — promotion/demotion/retirement/simulation-resolution management;
- `MNCS-22` — runtime handoff at current resolution;
- `MNCS-23` — batch/profiles/review/provenance;
- `MNCS-24` — golden progressive-resolution and continuity proof.

### MRCS

- `MRCS-02` — schema-aware fidelity/partition/transition profile authoring;
- `MRCS-04` — bounded predicates/selectors for partitions, thresholds and refinement triggers;
- `MRCS-12` — creature/population behavior definition bindings;
- `MRCS-14` — environment/hazard/world aggregate transition definitions;
- `MRCS-16` — scoped overrides/profile compatibility and version behavior;
- `MRCS-18` — simulation/evidence harnesses for aggregate/detailed equivalence and stability;
- `MRCS-20` — profile versioning/diff/provenance/publication;
- `MRCS-21` — cross-domain profile/runtime proof.

### GPR

- `GPR-03` — deterministic state kernel and bounded entity/state execution;
- `GPR-05` — economy/objective/world-route aggregate interactions;
- `GPR-07` — AI/encounter pacing with bounded non-omniscient resolution hooks;
- `GPR-08` — data-driven runtime/profile composition;
- `GPR-09` — delivery-mode parity without a rules fork;
- `GPR-12` — deterministic replay/Event traces and authority;
- `GPR-13` — snapshot/migration/recovery/version compatibility;
- `GPR-14` — GM/creator refine/collapse/catch-up inspection and dry run;
- `GPR-15` — conformance/regression coverage for resolution changes;
- `GPR-16` — golden cross-system runtime proof.

### MBES

- `MBES-01` — built-environment/settlement resolution ladder and summary↔detail rules;
- `MBES-10` — logistics/network aggregate capacity and routing interactions;
- `MBES-11` — aggregate production/processing/manufacturing chain interactions;
- `MBES-14` — environmental externality aggregates and owner consequence handoff;
- `MBES-17` — residents/households/crews/staffing at mixed resolution;
- `MBES-20` — settlement/district/city growth, capacity and service summaries;
- `MBES-21` — transportation/access/capacity/congestion aggregate projections;
- `MBES-22` — construction/market/labor/economy owner integration;
- `MBES-23` — multi-settlement/regional networks and specialization;
- `MBES-24` — golden cross-scale settlement/environment proof.

### MSWI

- `MSWI-02` — persistent world-transformation state feeding resolution-aware evolution;
- `MSWI-03` — cross-system consequence propagation/recovery;
- `MSWI-04` — ecology succession, carrying capacity, habitat suitability and population-band runtime;
- `MSWI-05` — food-web/migration/invasion/extinction/recovery consequences;
- `MSWI-10` — daily-life/downtime adapters over Project/time;
- `MSWI-13` — grand/world Projects and contribution aggregation;
- `MSWI-14` — seeded procedural scope assembly with ephemeral/proposed/persistent distinction;
- `MSWI-17` — fan-out/loop/dead-route diagnostics;
- `MSWI-18` — golden systemic proof.

### Existing completed owners consumed, not reopened

DPL, ODL, SCL, Action/Event, APW/D26, Character/NPC/Creature/Species/Form, World/Environment/Reality/Branch/Settlement, MIB-13/Economy/Resource/Inventory/Asset, PPIA visibility/permission foundations and PDCP Packets 03 and 05 remain their respective authorities.

### No direct new Packet-06 obligation

`MCS`, `MCCS`, `MSAS`, `MERA`, and `MSLR` may consume resolution-aware projections through normal owner seams but receive no standalone Packet-06 implementation obligation.

`MAS` remains outside PDCP and is not reopened.

## 22. Roadmap-reduction implication

Packet 06 closes a cross-family design uncertainty; it does not alter the roadmap count by itself.

No separate “world simulation” family is justified. The accepted capability decomposes cleanly into:

- MNCS identity/group/population refinement and resolution management;
- MRCS reusable profile/transition authoring and simulation evidence;
- GPR deterministic mixed-resolution runtime/replay/persistence;
- MBES settlement/logistics/economy mixed-resolution consumers;
- MSWI ecology/world-evolution and cross-system consequence routing.

Any future family reduction must occur only through the full family-level PDCP disposition review after all relevant packets are closed.

## 23. Completion statement

PDCP Packet 06 is design-closed when this package, its machine-readable closure record, the benchmark register transition and focused regression are durable and validated.

No application implementation, schema migration, roadmap-count mutation, OPS3 selector change, CNI-13 authority change, release/deployment, provider activation or owner-domain mutation is authorized by this closure.
