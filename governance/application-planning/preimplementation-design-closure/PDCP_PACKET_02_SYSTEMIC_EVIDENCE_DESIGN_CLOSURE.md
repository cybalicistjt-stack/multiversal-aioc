# PDCP Packet 02 — Systemic Investigation & Evidence Design Closure

**Project:** PDCP — Preimplementation Design Closure Project  
**Packet:** 02 — Systemic Investigation & Evidence  
**Status:** DESIGN_CLOSED  
**Date:** 2026-09-16  
**Implementation authority:** none  
**Roadmap-count mutation:** none in this packet  
**MAS:** explicitly excluded

## 1. Closure conclusion

Multiversal already has a completed, implementation-ready Investigation & Mystery authoring foundation in **PPIA-09** / **MV-IA-F011**. PPIA-09 already closes the majority of the benchmark comparison raised by Shadows of Doubt, Ultima Ratio Regum and systemic detective-game patterns:

- objective truth, GM solution, clue, observation, claim, evidence, hypothesis and Player knowledge are separately typed;
- evidence references source-domain objects instead of taking ownership from them;
- unreliable witnesses, false evidence, red herrings, contradictions and uncertainty are supported;
- timeline/alibi review and typed semantic connections are supported;
- reveal/withhold/revoke and role-safe projections are governed;
- clue-board graph position is presentation-only;
- solvability/redundancy/stall diagnostics are read-only;
- dynamic/extra clues carry trigger/delivery/provenance information;
- permission filtering precedes counts, search, exports, diagnostics, realtime, notifications and AI context;
- deterministic reference cases, recovery semantics and nonvisual equivalents already exist.

Therefore Packet 02 does **not** create a second Investigation system, a new evidence ledger, a new roadmap family or a standalone implementation tranche.

The residual gap is narrower and cross-systemic:

> ordinary canonical Actions/Events should be able to leave source-domain-owned traces that later become discoverable evidence without requiring every clue to be separately hand-authored into a case.

Packet 02 closes that gap through four implementation-ready contracts:

1. **Event-to-trace emission definitions and receipts**;
2. **trace-carrier ownership and lifecycle mutation semantics**;
3. **witness/record/systemic trace formation and discovery handoff into PPIA-09**;
4. **live evidence-route availability diagnostics over current world state without truth mutation or automatic mystery solving**.

No owner decision remains for this packet.

## 2. Existing authority absorbed rather than duplicated

### 2.1 PPIA-09 / MV-IA-F011 — Investigation authority

PPIA-09 remains authoritative for:

- Investigation case definition;
- GM truth/solution material;
- clue definition and Campaign clue state;
- observation, claim and statement records;
- Investigation-local evidence bindings/roles/notes;
- witness/source reliability and authenticity annotations;
- hypothesis, theory and deduction records;
- typed semantic clue/evidence/hypothesis connections;
- questions, leads and next steps;
- case-local timeline/alibi records;
- contradiction, false-lead and uncertainty records;
- discovery conditions, reveals and knowledge audiences;
- solvability/redundancy/stall-recovery diagnostics;
- conclusion, outcome and Investigation history;
- Investigation UI/projections including clue boards and accessible linear equivalents.

Packet 02 does not redefine any of those objects.

### 2.2 Action/Event — occurrence authority

Canonical occurrence remains owned by the existing Action/Event contracts. A systemic evidence trace can be caused by an Event but never becomes proof that an Event occurred merely because a trace definition exists.

An Event remains authoritative for its own identity, actor/source, time, scope, causal links and accepted domain consequences.

Packet 02 may attach trace-emission semantics to accepted Action/Event definitions and runtime results, but does not create a second Event stream.

### 2.3 Source-domain owner authority

Trace carriers remain owned by the domain that owns the thing or state carrying the trace. Examples include:

- Item/Asset for an object, tool, damaged lock, moved possession or material-bearing item;
- Character/NPC/Creature for memory, belief, testimony source, injury or carried state;
- Location/World/Environment for environmental marks, changed local conditions or location-linked state;
- Economy/Transaction for purchases, transfers, invoices, service records or other governed transaction records;
- Communication/Knowledge owners for messages, calls, transmissions or received information records;
- Project/Time/Schedule owners for appointments, shifts, planned presence and time-linked activity;
- Vehicle/Base/Settlement/Organization owners for logs, custody, access, operational records or domain-specific state;
- other canonical owners where the trace-bearing state already belongs.

Packet 02 does not copy these records into an Investigation ledger.

### 2.4 Visibility / Knowledge authority

Discovery, knowledge and visibility remain separate from objective existence.

A trace can exist canonically while:

- no Player knows it exists;
- only some Characters witnessed it;
- the trace is not currently observable;
- the trace is visible but its significance is unknown;
- the trace is discovered but its authenticity remains unresolved;
- different participants hold different interpretations.

Packet 02 cannot bypass existing permission or Knowledge rules.

### 2.5 World/Setting chronology authority

World/Setting chronology remains owned outside Investigation. Trace emission may reference canonical Event time and source-domain history; PPIA-09 may create case-local timeline/alibi projections without taking chronology ownership.

## 3. Benchmark lesson retained

The benchmark-derived improvement is not “simulate every forensic detail.” The useful capability is:

- routine world activity creates inspectable state and records;
- investigators can reason from those records instead of following only authored clue chains;
- evidence can survive, degrade, be obscured, contaminated, altered, relocated, destroyed or forged according to explicit rules;
- multiple independent source domains may corroborate or contradict one another;
- the world does not generate a conclusion for the Player.

The Multiversal form must remain more general than any benchmark game because it must support fantasy, historical, contemporary, science-fiction, supernatural and non-Euclidean settings without assuming modern surveillance, fingerprints, network logs, universal chemistry or other setting-specific forensic infrastructure.

## 4. New reusable definition contract

### 4.1 `EvidenceTraceProfileDefinition`

A reusable definition describing how a class of accepted Action/Event or owner-domain transition can leave one or more potential traces.

Required semantic fields:

- `traceProfileId` — stable definition identity;
- `version`;
- `scope` — core/setting/campaign/adventure/playtest or other governed rule scope;
- `triggerEventTypeIds` or bounded trigger predicate references;
- `emissionRules[]`;
- `sourceProvenance`;
- compatibility/enablement metadata;
- permission class for authoring/diagnostic visibility;
- deterministic/random policy when applicable.

A profile is reusable content/rules definition. It is not live evidence and does not prove an Event occurred.

### 4.2 `TraceEmissionRule`

Each emission rule defines one potential trace result.

Fields/dimensions:

- `traceKindId` — registry/extensible semantic kind;
- `carrierOwnerDomain`;
- `carrierSelector` or creation target contract;
- `creationPredicate`;
- `emissionCardinality` where meaningful;
- `commitMode`;
- `lifecycleProfileRef`;
- `observabilityProfileRef` where governed;
- optional `analysisProfileRef`;
- optional seeded choice/variation contract;
- resulting owner-domain operation template/reference;
- trace-origin visibility classification;
- unresolved/unsupported behavior.

### 4.3 Trace-kind taxonomy

Packet 02 does not freeze one universal exhaustive taxonomy. A minimal cross-setting registry should be able to represent categories such as:

- physical mark;
- material transfer/residue;
- environmental change;
- possession/custody change;
- location/path/presence trace;
- witness perception/memory;
- communication record;
- transaction/service record;
- schedule/attendance record;
- access/control/log record;
- device/system/telemetry record;
- administrative/document record;
- setting-specific supernatural/magical/psychic trace;
- custom governed trace kind.

These categories are semantic routing aids, not claims that every setting supports every category.

### 4.4 No pseudo-forensic invention

A profile may only create detail supported by accepted rules/content and owner-domain capabilities.

Examples:

- a medieval tavern purchase does not automatically create an electronic payment log;
- a fantasy world does not automatically produce fingerprints unless its rules/content establish such traces;
- a magical divination residue does not exist merely because the system has a supernatural trace category;
- a camera record requires an actual authorized camera/surveillance source and its operational state;
- a witness memory requires an eligible perceiver and an accepted perception/knowledge path.

Unknown or unsupported trace behavior stays unknown/unsupported.

## 5. Live trace and receipt contract

Packet 02 deliberately avoids one monolithic global Evidence table.

### 5.1 `EvidenceTraceEmissionReceipt`

A durable causal receipt links an accepted source Event to the owner-domain trace state it caused or attempted to cause.

Required fields:

- `traceReceiptId`;
- `sourceEventId`;
- `traceProfileId` + exact version;
- `emissionRuleId`;
- `commitMode`;
- `ownerDomain`;
- resulting `ownerObjectId` / `ownerStateId` / domain record reference when creation succeeded;
- `carrierObjectVersion` or equivalent accepted version;
- causal correlation/Event-group identity;
- deterministic seed/input snapshot when required;
- emission result: created / linked-existing / not-applicable / rejected / failed-followup;
- failure/rejection receipt where applicable;
- provenance/created timestamp;
- protected truth visibility class.

The receipt explains why the source-domain trace exists. It does not replace the trace carrier.

### 5.2 Stable trace identity

Where an owner domain supports a distinct persistent trace-bearing record, that record has its own stable owner-domain identity.

Where evidence is simply an existing canonical record—such as a transaction, message or schedule entry—the trace receipt references that existing record rather than cloning it.

### 5.3 Claimed origin versus actual provenance

For records or traces that may be forged, the system separates:

- actual creation/provenance Event and owner-domain history;
- in-world claimed author/source/time/origin;
- visible presentation to a particular participant;
- authenticity analysis state;
- Player/GM interpretations.

A forgery can successfully mislead Characters without rewriting protected actual provenance.

## 6. Trace emission operation semantics

### 6.1 Originating Event evaluation

After or during validation of a consequential Action/Event:

1. resolve the accepted Event type and exact active rules/profile versions;
2. find enabled trace profiles without exposing protected information to unauthorized clients;
3. evaluate each bounded emission predicate against authorized canonical server state;
4. produce an explicit proposed trace-emission set;
5. validate each destination owner-domain operation;
6. commit according to each rule's `commitMode`;
7. emit `EvidenceTraceEmissionReceipt` records;
8. expose only audience-safe projections.

### 6.2 Commit modes

Every emission rule chooses one of two governed modes.

#### `atomic_with_origin`

The trace consequence is part of the accepted Event transaction/Event group.

If a required owner-domain trace operation fails validation or cannot commit, the originating Event group does not report success.

Use when the trace/record is an intrinsic governed consequence of the operation and atomicity is required for consistency.

#### `causal_followup`

The source Event may commit first. A causally linked follow-up operation then attempts to create/update the trace carrier.

If follow-up fails:

- the original Event remains true;
- no trace is falsely projected as existing;
- a durable failed-followup receipt records the missing consequence;
- diagnostics/recovery can retry only under ordinary idempotent/version rules;
- retry must not duplicate an already-created trace.

There is no unrecorded “best effort” mode.

### 6.3 No automatic Investigation case creation

A world Event that emits traces does **not** automatically:

- create an Investigation case;
- mark the trace as a clue;
- reveal it to Players;
- create a hypothesis;
- declare relevance;
- declare authenticity;
- declare guilt/responsibility;
- schedule an investigation.

It merely leaves governed world state that may later be investigated.

## 7. Trace lifecycle semantics

### 7.1 Lifecycle is owner-domain state

A trace's current condition belongs to its carrier/source owner.

Generic lifecycle verbs may include:

- remain/persist;
- degrade;
- obscure;
- clean/erase;
- destroy;
- contaminate;
- alter/transform;
- relocate;
- separate/merge where source-supported;
- restore/recover where source-supported.

These verbs route to owner-domain operations. Packet 02 defines no universal physical formula.

### 7.2 `TraceLifecycleProfileDefinition`

Optional reusable lifecycle profile fields:

- eligible trace kinds/carriers;
- supported lifecycle transitions;
- transition triggers/predicates;
- time/environment/event dependencies;
- deterministic or seeded transition behavior;
- owner-domain operation mapping;
- observability consequences;
- provenance/history requirements;
- unsupported/unknown transitions.

### 7.3 No universal decay clock

There is no universal evidence half-life, degradation formula or automatic disappearance schedule.

A trace changes only when:

- an accepted lifecycle profile says it does;
- an owner-domain Event/condition changes the carrier;
- an explicit setting/system rule governs the transition.

### 7.4 Destruction does not delete history

Destroying or erasing a current trace:

- makes the current carrier/state unavailable according to owner semantics;
- creates a new Event/history entry;
- does not delete the original source Event or emission receipt;
- does not retroactively make prior discoveries invalid;
- may affect later observation or analysis opportunities.

### 7.5 Contamination

Contamination adds or mixes attributable state according to owner rules.

It does not silently overwrite the trace's prior history. A Player may not know which contributors are genuine, but GM/owner provenance remains recoverable under authorized views.

### 7.6 Forgery/falsification

Forgery is an Event that creates or alters a trace/record so that its **claimed** origin/content differs from protected actual provenance.

Rules:

- objective Event history is never rewritten;
- the forged carrier can be canonically real as an object/record;
- the claim represented by that carrier can be false;
- authenticity may be unknown to investigators;
- discovery does not automatically expose the forgery;
- analysis may change an Investigation-local authenticity annotation or reveal only through governed rules;
- a forged record can generate contradictions without auto-resolving them.

## 8. Witness and memory trace contract

### 8.1 Witness eligibility

A Character/NPC/Creature becomes a potential witness only through an explicit perception/information path governed by existing Scene/Location/sensory/Knowledge rules.

Mere co-presence does not automatically mean accurate perception.

### 8.2 `WitnessPerceptionReceipt`

Where the runtime needs durable causal explanation, an accepted Event may create a perception receipt containing:

- source Event;
- perceiver entity;
- applicable perception/sensory relation/profile;
- observed semantic facts or bounded observation reference;
- exact rules/profile versions;
- resulting Knowledge/Memory owner operation;
- protected visibility class;
- success/not-perceived/partial/unresolved outcome.

The receipt itself does not give Players access to the witness's memory.

### 8.3 Memory ownership

NPC/Character Knowledge, belief, memory, suspicion, reliability and misinformation remain owned by their existing/future owner contracts, including MNCS where it constructs/visualizes these states.

Packet 02 does not create Investigation-owned witness memory.

### 8.4 Testimony

A witness statement/testimony is a **claim**, not objective truth.

The statement may derive from:

- actual memory;
- mistaken perception;
- incomplete memory;
- belief or inference;
- deliberate deception;
- coercion/social context;
- copied rumor/second-hand information.

PPIA-09 remains responsible for claim/evidence/hypothesis handling after testimony enters a case.

## 9. Existing records as evidence

### 9.1 Transactions

A purchase, transfer, payment, invoice, service or economy record remains Economy/Transaction-owned.

Investigation may bind that exact record as evidence if discovered/authorized.

### 9.2 Communications

Messages, calls, transmissions and similar records remain owned by the applicable communication/knowledge/content domain.

Investigation references the record and its visible metadata/content; it does not clone it.

### 9.3 Schedules and presence

Appointments, work shifts, Projects, travel windows, duty schedules and similar records remain Project/Time/Profession/owner state.

A case may compare those records with other evidence without turning a schedule into proof that the scheduled activity actually occurred.

### 9.4 Access, telemetry and system logs

Logs exist only where the source system actually defines and emits them.

A log entry may itself be genuine, missing, altered, forged or incomplete according to owner rules.

### 9.5 Custody and possession

Item/Asset custody/location history can become evidence without Investigation taking inventory authority.

## 10. Discovery and PPIA-09 handoff

### 10.1 Observation/discovery operation

Finding a trace uses the applicable owner/rules operation—searching, inspecting, scanning, interviewing, researching, divining or other setting-supported method.

The operation may result in:

- no observation;
- partial observation;
- an observation with unresolved significance;
- a discovered owner-domain record/object;
- an accepted PPIA-09 evidence binding if the Investigation context is authorized.

### 10.2 `SystemicEvidenceBinding`

This is **not a new evidence owner object**. It is a named PPIA-09-compatible binding shape documenting what an Investigation reference must preserve:

- Investigation/case ID;
- owner domain;
- owner object/state/record ID;
- owner object version observed where applicable;
- originating trace receipt/Event ID if authorized/known to the GM system;
- discovery Event/operation ID;
- observer/discoverer identity;
- observed snapshot/semantic notes allowed by PPIA-09;
- Investigation-local evidence role/tags;
- visibility/audience;
- provenance references.

PPIA-09's existing evidence authority owns the accepted Investigation binding.

### 10.3 Discovery is not truth promotion

A discovered trace can be:

- authentic;
- forged;
- contaminated;
- incomplete;
- irrelevant;
- misleading;
- related to a different Event;
- unresolved.

Discovery alone never converts it into objective truth or guilt.

## 11. Participant-known evidence versus world truth

The system preserves at least these distinctions:

1. source Event / objective world history;
2. current trace-carrier state;
3. GM-authorized actual provenance/authenticity information;
4. participant observation;
5. participant knowledge/belief;
6. PPIA-09 evidence binding;
7. participant hypothesis/conclusion.

No layer silently overwrites another.

## 12. Hypothesis and case-board behavior

Packet 02 adds no new hypothesis ledger.

PPIA-09 remains authoritative for:

- hypothesis creation;
- typed evidence/hypothesis connections;
- contradictions;
- clue-board presentation;
- timeline/alibi presentation;
- conclusions.

A Player may connect the wrong evidence to the wrong theory. That is valid Player state and does not mutate source truth.

## 13. Live evidence-route diagnostics

PPIA-09 already owns authored revelation-route solvability/redundancy diagnostics. Packet 02 adds a separate **current-world availability** input to those diagnostics.

### 13.1 `EvidenceRouteAvailabilityDiagnostic`

A read-only diagnostic may combine:

- PPIA-09 authored required revelations/routes;
- currently existing authorized trace carriers;
- known destroyed/unavailable traces;
- explicit discoverability operations/conditions;
- witness/record availability;
- role/permission constraints;
- current route dependencies.

Outputs can include:

- currently reachable route;
- currently unavailable route;
- single surviving route;
- route blocked by destroyed/unavailable trace;
- route blocked by permission/knowledge prerequisites;
- unresolved due to unknown owner state;
- recovery route explicitly authored;
- no currently demonstrated route.

### 13.2 Diagnostic boundaries

The diagnostic:

- does not solve the mystery;
- does not reveal hidden truth to unauthorized viewers;
- does not invent new evidence;
- does not resurrect destroyed evidence;
- does not declare a clue true;
- does not guarantee Player discovery;
- does not create a universal evidence-count rule;
- does not auto-author a recovery clue;
- does not mutate the case or world.

### 13.3 Trace-coverage authoring diagnostic

Creators/GM-authorized views may also inspect whether important event types or required revelations have declared trace routes.

A warning such as “this required revelation currently has one trace route” is advisory, analogous to PPIA-09's existing redundancy warning. It does not force a particular number of traces.

## 14. Dynamic and recovery evidence

PPIA-09 already permits dynamic/extra clues with explicit trigger/delivery provenance.

Packet 02 clarifies that a recovery clue may be:

- a newly authored clue accepted by the GM;
- an owner-authorized new world Event that creates a new trace;
- discovery of an already-existing systemic trace;
- reanalysis/reinterpretation of existing evidence;
- a new witness/record becoming available through a canonical Event.

The system may suggest recovery options but may not silently fabricate a trace or claim a past Event left evidence that was never emitted.

## 15. Resolution-depth contract

### 15.1 Detailed resolution

At detailed resolution, a profile may emit individually addressable trace carriers/records with explicit owner references.

### 15.2 Aggregate/offscreen resolution

Offscreen or aggregate simulation need not create every microscopic trace.

It may emit an `AggregateTraceBundleReceipt` that records only source-supported semantic trace categories/owner references needed at that resolution.

Fields include:

- source Event/group;
- trace profile/version;
- aggregate scope;
- declared trace categories;
- owner-domain aggregate state references;
- deterministic seed where refinement is supported;
- refinement capability flag;
- unresolved-detail marker.

### 15.3 Refinement

An aggregate trace bundle may be expanded into detailed trace instances only if the governing profile declares deterministic/seed-governed refinement rules.

Refinement must:

- preserve the original Event facts;
- preserve aggregate constraints;
- use the recorded profile/version/seed;
- create no detail outside the profile's allowed space;
- record the refinement operation/provenance.

If no refinement contract exists, missing detail stays unresolved. The system does not fabricate exact footprints, camera angles, transaction line items, witness positions or similar specifics after the fact.

### 15.4 Collapse

Detailed traces may be summarized for offscreen/display/performance purposes without deleting the underlying canonical owner state or historical receipts.

## 16. Versioning, migration and replay

### 16.1 Profile snapshot/version binding

Every trace receipt stores the exact profile/rule version used.

Updating a trace profile changes future applicable Events; it does not silently change what old Events emitted.

### 16.2 No retroactive trace invention

Installing or enabling a profile after an Event does not automatically create traces for historical Events.

### 16.3 Explicit backfill/reconstruction

If a migration, recovery or GM-authorized reconstruction legitimately needs historical traces, it uses an explicit operation that records:

- source historical Event(s);
- reconstruction reason;
- old/new profile references;
- authoritative source data used;
- generated owner-domain operations;
- operator/authority;
- whether the result is reconstructed, simulated or canonical according to the owner contract.

Backfill never masquerades as an original emission.

### 16.4 Replay

Where deterministic replay is declared, identical accepted Event state + exact profile version + deterministic seed/input must reproduce the same trace-emission receipt set.

Replay/projection does not duplicate already committed owner-domain traces.

## 17. Concurrency, idempotency and recovery

All consequential trace mutations use the owning domain's expected-version/idempotency semantics.

Examples:

- investigator discovers a trace while another actor destroys it;
- two actors attempt to clean/contaminate the same carrier;
- a lost response occurs after a trace creation committed;
- a witness-memory write times out;
- the originating Event committed but a causal follow-up trace failed.

Required behavior:

- status/current-version lookup before retry;
- no blind duplicate trace creation;
- stale operations fail or re-evaluate according to owner rules;
- partial cross-domain state is never presented as an atomic success;
- failed causal follow-up is explicit and recoverable when permitted.

## 18. Visibility, privacy and hidden-information contract

Filtering occurs before:

- trace existence lookup;
- trace counts;
- source/carrier resolution;
- witness lists;
- search/suggestions;
- route-availability diagnostics;
- graph topology;
- exports;
- realtime/notifications;
- diagnostics/issue reports;
- simulation inputs;
- AI context.

A Player who is not authorized to know that a hidden camera exists must not learn it from “3 undiscovered traces,” route counts, diagnostics or AI suggestions.

GM/admin account status alone does not bypass Campaign/participant privacy rules beyond existing authorized scope.

Revocation removes protected projections/caches/context while preserving authorized audit history.

## 19. Player / GM / creator UX contract

### 19.1 Player investigation view

Players interact primarily through existing PPIA-09 surfaces.

They may see, when authorized:

- discovered evidence;
- their observations;
- evidence provenance that their Character actually knows;
- current observed condition of a trace;
- analysis results;
- claims/testimony;
- hypotheses/connections;
- uncertainty/contradiction annotations;
- accessible linear equivalents.

They do not see undiscovered trace counts or protected actual provenance.

### 19.2 GM trace inspector

Authorized GM surfaces may show:

- source Event;
- trace profile/rule version;
- actual carrier owner/reference;
- current lifecycle state;
- emission and later mutation Events;
- actual versus claimed origin where authorized;
- witness-perception/memory handoffs;
- discovered-by/audience state;
- current Investigation bindings;
- replay/recovery receipts;
- route availability diagnostics.

### 19.3 Creator trace-profile authoring

MRCS-compatible authoring should provide:

- trigger selection;
- trace-kind/carrier selection;
- bounded predicates;
- commit mode;
- lifecycle profile binding;
- observability/analysis profile references;
- deterministic/seed policy;
- source/domain validation;
- preview using proposed/sample Events;
- impact/reference analysis;
- simulation/golden-vector harness.

Preview never commits live traces.

### 19.4 Event trace preview

GM/creator tooling may preview what traces a proposed Event **would** emit using current authorized state.

Preview must be labeled nonauthoritative and cannot be used to infer protected trace sources outside the viewer's scope.

## 20. Accessibility

Systemic evidence must preserve PPIA-09's semantic nonvisual authority.

Requirements:

- every graph/clue-board relation has list/table/linear semantic form;
- trace lifecycle state is available in text/structured semantics, not color alone;
- source/provenance chains can be traversed by keyboard and screen reader;
- timelines have ordered textual equivalents;
- contamination/contradiction/authenticity distinctions are not encoded solely by color, spatial placement or animation;
- drag/drop is never the sole method for linking evidence;
- route diagnostics expose structured findings and reasons.

## 21. Optional AI boundary

AI may:

- summarize authorized discovered evidence;
- suggest Investigation-local hypotheses/connections as proposals;
- suggest trace-profile definitions to a creator;
- flag possible missing trace routes in authorized authoring context;
- suggest recovery-clue options;
- explain diagnostics from role-safe data.

AI may not:

- create canonical historical traces merely to make a mystery solvable;
- reveal undiscovered/unauthorized traces;
- decide objective truth;
- mark a forged trace genuine;
- mutate evidence/carrier state;
- destroy/clean/contaminate/forge traces;
- accept a hypothesis/conclusion as canonical truth;
- commit owner-domain Events without ordinary authority;
- use hidden counts/topology as leakage.

## 22. Failure and edge cases closed

### Missing trace owner

If an emission rule cannot resolve a valid owner/carrier contract, validation fails rather than inventing a generic evidence object.

### Unsupported trace kind

The rule remains invalid/unavailable for the current setting/profile; no fallback pseudo-forensic trace is invented.

### Missing carrier after Event

Atomic mode fails the Event group. Causal-followup mode records explicit follow-up failure.

### Carrier deleted/archived by owner

Investigation preserves historical references/tombstone-safe provenance according to owner rules and does not pretend the carrier is still observable.

### Contradictory traces

Both remain; PPIA-09 records contradiction/uncertainty without automatic truth adjudication.

### Same trace used in multiple cases

Each case holds its own PPIA-09 binding to the same owner-domain trace/record. The trace is not cloned.

### Same world Event relevant to multiple cases

Each case may independently discover/reference it according to permission/knowledge state.

### Trace profile disabled mid-Campaign

Existing traces/history remain governed by the version used at emission. Future Events obey active rules.

### Event imported from legacy history without trace receipts

No traces are inferred unless an explicit reconstruction/backfill operation is authorized.

### Destroyed evidence previously photographed/copied

The original carrier may be gone while a separately owned derivative/record can remain if such a derivative was canonically created. Investigation references each separately.

### Witness dies/leaves/becomes unavailable

Existing memory/history remains owner-governed; availability for interview changes through canonical state rather than deleting prior witness provenance.

### Witness changes their story

Each statement is a separately attributable claim/Event. Later testimony does not rewrite prior testimony.

### Record corrected by ordinary business process

The correction is a new owner-domain record/history transition; Investigation can compare versions when authorized.

### Player guesses an undiscovered trace correctly

A hypothesis may match truth without becoming knowledge or revealing the trace.

### GM intentionally authors a mystery with no systemic traces

Allowed. Packet 02 is a capability, not a mandatory realism rule. PPIA-09 authored clues may remain the only routes.

## 23. Golden implementation vectors

Future implementation should automate these expected behaviors rather than rediscover them.

### `PDCP-EVD-001` — physical trace emission

An accepted Event with an enabled atomic physical-trace rule creates the owner-domain carrier/state and one emission receipt in the same successful Event group. The Event does not create an Investigation case or Player clue automatically.

### `PDCP-EVD-002` — existing transaction record reference

A purchase Event produces/references its canonical transaction record. Later Investigation discovery binds that exact record; no duplicate Investigation transaction is created.

### `PDCP-EVD-003` — witness perception succeeds

An eligible witness with an accepted perception path receives a Knowledge/Memory owner update causally linked to the source Event. No Player receives the witness memory merely because it exists.

### `PDCP-EVD-004` — witness did not perceive

A co-present NPC who fails/does not satisfy the applicable perception path receives no witness-memory trace. The system does not assume omniscient witnessing.

### `PDCP-EVD-005` — hidden witness nonleakage

A Player without authority cannot infer the existence/count/identity of a protected witness through search, diagnostics, route counts, exports or AI context.

### `PDCP-EVD-006` — schedule is not occurrence proof

A schedule record says an NPC was assigned to work at a location. Investigation can use it as evidence, but it does not automatically prove the NPC was physically present.

### `PDCP-EVD-007` — discovery binding preserves owner identity

Discovering an Item/record/trace creates a PPIA-09 evidence binding referencing owner domain/object/version and discovery Event; it does not copy ownership or objective truth.

### `PDCP-EVD-008` — undiscovered trace remains unknown

A canonical trace exists, but no authorized discovery occurred. Player projections, counts and clue boards do not reveal it.

### `PDCP-EVD-009` — profile-driven degradation

A trace with an explicit lifecycle rule degrades after the governed trigger. An identical trace with no such rule does not decay merely because time passed.

### `PDCP-EVD-010` — contamination preserves provenance

A later Event contaminates a trace with a second contributor/state. The original source history remains; the current observed trace may become ambiguous.

### `PDCP-EVD-011` — cleaning/destruction is a new Event

A trace is cleaned/destroyed. Current discoverability changes, but the originating Event/emission receipt and any prior accepted discovery remain historically attributable.

### `PDCP-EVD-012` — forged record separates claim from provenance

An actor creates a forged record claiming an earlier/different origin. Player-safe content can present the false claim while GM-authorized provenance shows the actual creation Event. No Event history is rewritten.

### `PDCP-EVD-013` — contradiction does not adjudicate truth

Two evidence sources conflict. PPIA-09 receives a contradiction/uncertainty relationship; no automatic winner or guilt conclusion is produced.

### `PDCP-EVD-014` — hypothesis cannot mutate truth

A Player links evidence to an incorrect suspect theory. The hypothesis persists as Player state without changing source Events, evidence carriers or NPC truth.

### `PDCP-EVD-015` — cross-case correlation references one source

Two cases discover the same owner-domain record/trace. Each has its own Investigation binding; the source record remains one canonical object/state.

### `PDCP-EVD-016` — protected route diagnostics

A GM diagnostic can see a currently surviving hidden trace route. A Player-safe diagnostic cannot reveal that route, its count or hidden source.

### `PDCP-EVD-017` — destroyed-route availability finding

A required authored revelation had two routes; one systemic trace was destroyed. The diagnostic reports one surviving route to an authorized GM but does not create replacement evidence.

### `PDCP-EVD-018` — recovery suggestion is proposal-only

AI/tooling suggests a new witness/record/recovery clue. Nothing becomes canonical until a GM/owner-authorized ordinary operation/Event accepts or creates it.

### `PDCP-EVD-019` — aggregate offscreen trace bundle

An offscreen Event emits a profile-authorized aggregate trace bundle rather than arbitrary microscopic details. The bundle preserves source Event/profile/version/seed and declared categories.

### `PDCP-EVD-020` — deterministic refinement

A bundle whose profile supports refinement is expanded later using the recorded version and seed. Repeating the refinement yields the same permitted detailed trace set without changing historical Event facts.

### `PDCP-EVD-021` — unresolved detail stays unresolved

An aggregate bundle lacks a refinement contract. A later detailed Investigation cannot fabricate exact positions, identities or record contents; those details remain unresolved unless another owner source establishes them.

### `PDCP-EVD-022` — profile update is prospective

Trace profile v2 is enabled after an old Event. The old Event keeps v1 emission semantics; v2 does not silently add/remove historical traces.

### `PDCP-EVD-023` — explicit historical reconstruction

A GM-authorized migration reconstructs a trace from sufficient canonical history. The resulting receipt is labeled reconstruction/backfill with source Event/profile/operator provenance and is not represented as an original historical emission.

### `PDCP-EVD-024` — deterministic replay without duplicate commit

Replaying/projection-validating an Event with its original profile version and seed reproduces the expected emission-receipt result but does not commit duplicate carrier records.

### `PDCP-EVD-025` — causal follow-up failure is explicit

The source Event commits, but a `causal_followup` trace operation fails. The system records failed follow-up state; it does not show the trace as existing and does not roll back the already-accepted Event.

### `PDCP-EVD-026` — lost-response idempotency

A trace-creation response is lost after commit. Status/current-version lookup finds the existing result; retry converges rather than creating a duplicate trace.

### `PDCP-EVD-027` — accessible nonvisual parity

A screen-reader/keyboard user can inspect evidence source, lifecycle, contradiction, chronology and semantic relationships without graph position, color, hover or drag-and-drop.

### `PDCP-EVD-028` — GM-only authenticity truth

A forged/altered trace's actual provenance/authenticity is visible to an authorized GM but remains unresolved in Player evidence projections until a governed discovery/analysis/reveal makes it known.

## 24. Future family implementation mapping

Packet 02 creates no new family and no standalone tranche. Residual implementation is absorbed into already-planned families.

### MNCS

Relevant future implementation obligations:

- **MNCS-07** — witness Knowledge/Belief/Memory/Suspicion/Reliability/Misinformation handoff; witness-memory origin/provenance support;
- **MNCS-09** — schedule/life-context records remain canonical sources usable by Investigation without being copied;
- **MNCS-18** — witness identity/secrets/reveal-safe Investigation handoff;
- **MNCS-20** — NPC Event/history/continuity interaction with witness memories and changing testimony availability;
- **MNCS-22** — runtime Investigation handoff for NPC testimony, Knowledge and source references;
- **MNCS-24** — golden continuity proof should include at least one permission-safe Investigation/witness handoff.

MNCS does not become an Evidence ledger.

### MRCS

Relevant future implementation obligations:

- **MRCS-05** — author `EvidenceTraceProfileDefinition`, emission rules, lifecycle profiles and bounded triggers/effects as governed reusable definitions;
- **MRCS-14** — setting/environment/hazard trace-bearing content where those owners expose applicable semantic definitions;
- **MRCS-17** — reference/impact analysis for trace profiles, event triggers, carrier owners and lifecycle dependencies;
- **MRCS-18** — simulation/validation harness for trace-emission definitions, conflicting profiles and route-coverage diagnostics;
- **MRCS-20** — exact version/provenance/pack semantics for trace profiles;
- **MRCS-21** — cross-domain golden proof includes trace-definition → runtime emission → Investigation binding without owner duplication.

MRCS remains definition/authoring authority only.

### GPR

Relevant future implementation obligations:

- **GPR-04** — execute accepted interaction/Action consequences that may trigger trace profiles through Action/Event owner contracts;
- **GPR-05** — consume existing Inventory/Economy/World-route records as trace carriers without duplicating them;
- **GPR-08** — data-driven pattern/loop schema can reference accepted trace profiles where gameplay patterns require them;
- **GPR-12** — deterministic Event-trace emission/replay receipts and multiplayer authority semantics;
- **GPR-13** — persistence/snapshot/migration behavior for trace receipts and aggregate bundles;
- **GPR-14** — GM/creator preview and trace-inspection surfaces over governed definitions/state;
- **GPR-16** — golden proof includes a systemic Event leaving a trace later consumed by Investigation.

GPR does not own Investigation truth or source-domain carrier state.

### MSWI

Relevant future implementation obligations:

- **MSWI-03** — cross-system consequence routing includes profile-governed trace emission/lifecycle follow-up with reversibility/recovery semantics;
- **MSWI-10** — systemic profession/enterprise/daily-life composition may expose canonical records/schedules/transactions as potential evidence through their existing owners;
- **MSWI-17** — interaction-density/effect-fan-out diagnostics can identify missing/dead trace consequence routes and live route availability without inventing evidence;
- **MSWI-18** — systemic golden proof includes Event → trace → later discovery → Investigation reference and at least one trace lifecycle mutation.

MSWI does not become a generic evidence or Event ledger.

### No direct new Packet-02 obligation

Packet 02 adds no standalone implementation requirement to:

- MCS;
- MCCS;
- MSAS;
- MERA;
- MBES;
- MSLR.

Those domains may naturally own source records/objects/states that become evidence, but Packet 02 does not expand their planned product surfaces solely for Investigation.

### MAS boundary

MAS is explicitly outside PDCP and is not reopened. MAS-06/related Adventure investigation authoring may consume PPIA-09/systemic evidence capabilities, but Packet 02 creates no MAS change.

## 25. Roadmap reduction implication

Packet 02 closes product-design research that otherwise could have expanded MNCS/MRCS/GPR/MSWI implementation tranches or produced a new “systemic investigation” family.

Current disposition:

- new family required: **No**;
- new standalone tranche required: **No**;
- current family tranche counts changed now: **No**;
- design obligations removed from future implementation scope: **Yes**;
- residual code/UI/integration/test obligations mapped to existing future tranches: **Yes**.

Family-level PDCP reduction receipts will later decide whether the affected baseline tranches can be merged or removed after all packets/family design obligations are closed.

## 26. Capability-loss check

Packet closure preserves:

- all PPIA-09 truth/belief/evidence/hypothesis distinctions;
- source-domain ownership;
- Action/Event occurrence authority;
- hidden-information filtering;
- chronology ownership;
- deterministic provenance/replay;
- dynamic clue/recovery capability;
- contradiction/uncertainty semantics;
- accessible nonvisual Investigation;
- GM authority;
- optional-AI advisory-only boundaries.

No accepted capability is intentionally removed.

## 27. Final packet invariants

1. A trace is world/source-domain state, not automatically a clue.
2. A clue/evidence binding is Investigation state, not source-domain ownership.
3. Discovery is not truth promotion.
4. Testimony is a claim, not objective truth.
5. Schedule is not proof of attendance.
6. A record can exist and still be false, forged, incomplete or misleading.
7. Forgery changes in-world claims/content but never rewrites protected actual provenance.
8. Trace destruction changes current availability but does not delete history.
9. Contamination adds attributable history rather than silently replacing it.
10. No universal trace taxonomy, decay formula, forensic model, clue count or evidence threshold is invented.
11. Trace emission is either atomic or explicitly causally linked; never hidden best effort.
12. Profile version changes are prospective unless explicit reconstruction/backfill occurs.
13. Aggregate simulation may stay aggregate; detailed evidence is never fabricated during later refinement without a declared refinement contract.
14. Permission filtering precedes trace counts, source resolution, witness lists, diagnostics and AI context.
15. PPIA-09 remains the Investigation/clue/evidence/hypothesis authority.
16. Source owners retain their records, objects and state.
17. Action/Event remains canonical occurrence authority.
18. Diagnostics may identify route availability and gaps but never solve a case or invent evidence.
19. AI cannot create historical evidence merely to repair a mystery.
20. Packet 02 grants no product implementation authority and changes no live OPS3 selector.

## 28. Closure receipt

**Packet status:** `design_closed`  
**Owner decision remaining:** false  
**New implementation family required:** false  
**New standalone implementation tranche required:** false  
**Golden vectors:** 28  
**Affected future families:** MNCS, MRCS, GPR, MSWI  
**No-direct-obligation families:** MCS, MCCS, MSAS, MERA, MBES, MSLR  
**Excluded program:** MAS  
**Capability loss detected:** false  
**Roadmap count changed by this packet:** false
