# PDCP Packet 05 — Persistent History, Legacy, Succession & Delayed Consequence — Design Closure

**Project:** PDCP — Preimplementation Design Closure Project  
**Packet:** PDCP-PACKET-05  
**Status:** DESIGN_CLOSED  
**Date:** 2026-09-16  
**Implementation authority:** none  
**Roadmap-count mutation:** none  
**MAS:** excluded and not reopened

## 1. Purpose

Close the benchmark-derived product-design questions exposed by Wildermyth, Unexplored 2, Six Ages, Soulash 2 and similar persistent-world/generational patterns without creating a second Event/history ledger, a universal inheritance ledger, a universal memory ledger, or a background-time engine.

The packet defines reusable contracts for:

1. Event-derived legacy/scar projections;
2. explicit cross-owner succession handoff;
3. governed delayed consequences;
4. institutional/cultural memory projections and explicit memory transformation;
5. historical/current/as-of projections;
6. proposal-only history burn-in and promotion.

## 2. Existing authority absorbed rather than duplicated

Packet 05 consumes and preserves the following existing authorities.

| Concern | Preserved authority/boundary |
|---|---|
| Historical occurrence | **Action/Event and owning-domain Events** remain canonical. Historical facts are not rewritten because a later projection, chronicle or legend changes. |
| Exact historical provenance | Existing authoritative-result/history contracts preserve exact action/proposal definition, source/version/rules/schema/provenance used at the time. |
| Campaign-local history and Session boundaries | **PPIA-08 Campaign/Scene/Session** remains authoritative for Campaign-local placement/history, immutable launch snapshots, governed live amendment and post-session recovery evidence. |
| History/timeline/chronicle views | Completed **WCI-02** remains the history/calendar/timeline/chronicle/reality-explorer surface; WCI does not become a parallel history database. |
| Continuity/consequence analysis | Completed **WCI-05** remains advisory creator/campaign continuity and consequence analysis over canonical owners. |
| Campaign/project time | **APW/D26 Project/time** remains long-running activity/task/campaign-time authority. Wall clock is not Campaign time unless an explicit owner profile says otherwise. |
| Organization succession | Completed **ODL-04** remains role/delegation/communication/succession projection authority. It does not by itself transfer system permission, Assets, relationships or ownership. |
| Character/NPC/Creature identity | Existing Character/NPC/Creature owners retain identity, state, retirement/death/continuity and live-instance truth. |
| Relationship/reputation | **MIB-09** remains relationship/reputation mutation authority. No inherited reputation is assumed. |
| Assets/economy/custody | Item/Asset/Inventory/Economy owners retain ownership, custody, estate, transfer and value truth. |
| Organization/Faction/Religion/Culture | Their existing owners retain institutional state, doctrine, membership, law, custom and knowledge truth. |
| Future NPC continuity tooling | **MNCS** may author/generate/project continuity and succession support, but cannot mint a second live entity/history ledger. |
| Reusable definition authoring | **MRCS** authors reusable legacy, deferred-consequence, succession and history-generation profiles. |
| Runtime composition/persistence | **GPR** executes accepted semantic operations and replay/persistence contracts; it does not own history truth. |
| Cross-domain persistent consequence | **MSWI** composes persistent world consequences across owners; it does not become a second World/Event ledger. |

### 2.1 Foundational invariants

1. **Past Events are immutable evidence.** Corrections, revelations, invalidations, retcons authorized by an owner, restoration and reinterpretation are represented by later governed records/events rather than destructive rewriting of prior evidence.
2. **Current state and historical state are different questions.** Current owner state is canonical for the present; historical/as-of views are projections from history/snapshots and may be incomplete where historical data was not captured.
3. **A legacy/scar is not automatically a mechanic.** Persistent mechanical consequences live in their owning domains (Condition, Character, relationship, Asset, World, etc.). A legacy projection references those facts; it does not duplicate them.
4. **Succession is transfer, not cloning.** A successor does not automatically inherit a predecessor's identity, memories, relationships, reputation, Assets, abilities, permissions, debts, obligations, titles or projects.
5. **Institutional memory is not omniscience.** It is a permission-filtered projection from actual records, witnesses, knowledge, doctrine and accepted historical sources available to the institution/culture.
6. **Forgetting does not erase truth.** Forgetting, mythologizing, censorship, propaganda, archive loss and legend transformation modify knowledge/claims/records through explicit governed rules/events; they do not rewrite the underlying historical Event.
7. **Delayed consequence is orchestration, not mutation authority.** Trigger evaluation may request owner operations. Only owners commit resulting state.
8. **No hidden real-time simulation.** Delayed consequence and generational progress use canonical Campaign/project time or explicit governed Events/state triggers.
9. **History burn-in is proposed until promoted.** Generated prehistory is never canonical merely because simulation completed.
10. **No common-sense inheritance fallback.** If a source/profile does not say what survives or transfers, the value stays unresolved/no-transfer rather than guessed.

## 3. Canonical distinctions

Packet 05 uses the following layers and does not collapse them:

- **historical Event/fact** — canonical occurrence owned by Event/domain owners;
- **current owner state** — present authoritative state;
- **historical/as-of projection** — derived read model at a chosen historical boundary;
- **knowledge/record/claim** — what a Character, organization, culture or archive knows/records/claims;
- **legacy/scar projection** — event-backed interpretation/summary of enduring significance;
- **succession plan** — proposed/accepted transfer orchestration, not completed transfer;
- **succession handoff receipt** — references exact owner-confirmed transfer results;
- **deferred consequence definition** — reusable rule/content describing future eligibility/trigger and requested owner effects;
- **deferred consequence instance** — Campaign-scoped armed/suspended/resolved orchestration state;
- **history burn-in proposal** — generated candidate Events/state with no canonical authority;
- **promoted historical Event/state** — owner-authorized accepted result after validation.

## 4. Reusable data contracts

### 4.1 `LegacyProfileDefinition`

Reusable MRCS-authored definition describing how a source Event or Event pattern may be presented as a legacy/scar/precedent without inventing new mechanics.

Minimum fields:

- `legacyProfileId` and version;
- stable semantic kind (`scar`, `achievement`, `precedent`, `legend`, `trauma`, `institutional_precedent`, `world_change_marker`, `custom_governed`);
- applicable source Event/action/effect tags or owner predicates;
- allowed subject scopes (Character, NPC, Creature, Organization, Faction, Culture, Settlement, Location, World, Campaign, etc.);
- optional minimum persistence/significance predicates;
- label/summary template references;
- allowed enduring owner-state references;
- inheritance/succession eligibility **only as an explicit request class**, never as implied transfer;
- visibility/knowledge policy;
- retention/archive policy;
- source/rules/provenance/version metadata.

A `LegacyProfileDefinition` cannot apply a Condition, reputation change, title, Asset transfer or other mechanic by itself.

### 4.2 `EventLegacyBinding`

Campaign/world-scoped binding between immutable historical evidence and a legacy profile.

Fields include:

- `bindingId`;
- source Event IDs and exact versions/provenance;
- subject/entity refs;
- `legacyProfileId` + version;
- optional current enduring-consequence refs owned elsewhere;
- scope (Campaign/World/Organization/etc.);
- visibility/knowledge policy;
- created-by/operation/correlation metadata;
- optional invalidation/supersession reference.

A binding never replaces the source Event.

### 4.3 `LegacyProjectionReceipt`

Read-only/versioned result used by Character history, WCI timelines, GM views, campaign summaries and later creator surfaces.

It records:

- source binding/profile versions;
- exact Event refs;
- current surviving consequence refs;
- historical-only consequences that no longer persist;
- who can see which fields;
- projection timestamp/as-of boundary;
- missing/unavailable historical evidence explicitly;
- provenance of any generated summary text.

### 4.4 `SuccessionPlanDefinition`

A reusable or Campaign-specific plan listing **independent owner-domain handoffs** that may be requested when a predecessor retires, dies, abdicates, is replaced, fragments, recombines, or otherwise leaves a role.

A plan may contain typed entries for:

- organization role/title/delegation;
- system permission/control role;
- Campaign participant/Character control assignment;
- Asset/property/custody transfer;
- Project/task responsibility;
- obligations/contracts/debts where the owning contract permits assignment;
- explicit knowledge/record communication or archive access;
- relationship/reputation association rule requests;
- faction/culture/religion membership/office;
- named legacy references;
- setting-specific owner handoffs.

Every entry identifies its canonical owner, required authorization, preconditions and failure behavior.

### 4.5 `SuccessionHandoffRequest`

Transactional orchestration request containing:

- predecessor and successor IDs (distinct unless an owner explicitly models a same-identity transformation);
- plan/profile version;
- source cause Event(s);
- handoff entry list;
- expected owner versions;
- authority/permission evidence;
- stable operation/correlation IDs;
- requested atomicity group where supported;
- preview/dry-run result refs.

### 4.6 `SuccessionHandoffReceipt`

Records what actually happened, per owner entry:

- committed;
- rejected;
- not_applicable;
- blocked_pending_human;
- blocked_pending_gm;
- stale_revalidation_required;
- compensated/reversed where supported.

The receipt references owner Events/transactions; it does not become ownership truth itself.

Partial succession is valid. A successor may inherit a role but not a sword, a business but not a friendship, an archive but not the predecessor's private memories.

### 4.7 `DeferredConsequenceDefinition`

Reusable MRCS-authored rule describing a possible later consequence.

Minimum semantics:

- `definitionId` and version;
- source eligibility (Event/action/effect/content tags);
- trigger family;
- trigger predicate and authorized input domains;
- earliest/latest Campaign-time or milestone window where applicable;
- reevaluation cadence/event triggers where applicable;
- requested owner-operation templates;
- success/partial/failure/cancel/expire behavior;
- stacking/coalescing/exclusivity rules;
- visibility/telegraphing policy;
- human/GM choice requirements;
- reversibility/compensation references;
- replay/determinism/seed policy where relevant;
- migration behavior across definition versions.

No definition may use hidden wall-clock elapsed time by default.

### 4.8 `DeferredConsequenceInstance`

Campaign-scoped orchestration state created only when an eligible source occurrence is accepted.

Lifecycle:

`proposed → armed → eligible → evaluating → awaiting_owner_commit → resolved`

with optional branches:

`paused`, `blocked`, `suspended`, `cancelled`, `expired`, `stale`, `recovery_required`, `failed_safe`.

Fields include:

- instance ID;
- source Event/cause chain refs;
- definition/version;
- Campaign/World scope;
- subject/target refs;
- canonical-time/milestone refs;
- current lifecycle state;
- last evaluation inputs/version;
- owner-operation request/result refs;
- visibility/telegraph state;
- operation/correlation/recovery metadata.

Lifecycle state alone never applies mechanics.

### 4.9 `DeferredConsequenceEvaluationReceipt`

Records a deterministic/replayable evaluation:

- exact definition/version;
- exact current owner-state versions/predicate inputs used;
- result (`not_eligible`, `eligible_request_emitted`, `blocked`, `cancelled`, `expired`, `stale`, `error_safe`);
- generated owner-operation requests;
- human/GM decision requirements;
- next reevaluation trigger if any;
- permission-filtered explanation surfaces.

### 4.10 `InstitutionalMemoryProjection`

Read-only projection for an Organization/Faction/Culture/Religion/Settlement/etc. from actual authorized inputs such as:

- Events;
- archives/records;
- member/witness knowledge;
- doctrine/law/custom;
- official histories/claims;
- known legacy bindings;
- destroyed/lost/censored records where discoverable to the viewing role.

It distinguishes at minimum:

- underlying historical fact where viewer is authorized;
- official institutional claim;
- current known/believed account;
- disputed account;
- forgotten/unavailable record;
- myth/legend/propaganda representation;
- provenance/source confidence where defined.

It cannot infer hidden truth from data merely because the engine can access it.

### 4.11 `MemoryTransformationRule`

Optional, explicitly governed rule for changes to knowledge/records over time or events, such as:

- archive loss/destruction;
- intentional censorship;
- oral-tradition drift;
- ritual preservation;
- propaganda/reframing;
- ordinary forgetting where a setting/rules profile explicitly models it;
- rediscovery/restoration.

The rule acts on owner-backed knowledge/claim/record state. It never deletes canonical historical Events.

### 4.12 `HistoricalStateProjectionRequest` / `HistoricalStateProjectionReceipt`

Read-only request/receipt for `current`, `as_of_event`, `as_of_campaign_time`, `snapshot`, or explicitly authored `alternate/hypothetical` projections.

Rules:

- current state comes from current owners;
- historical projection uses retained Events/snapshots/version history;
- missing historical facts remain `unknown/not_retained`;
- alternate/hypothetical projections are visibly noncanonical;
- replay cannot invent values that were never captured or derivable;
- permissions filter before aggregation, graph expansion, counts or optional-AI context.

### 4.13 `HistoryBurnInPlanDefinition`

Proposal-only generator/simulator contract for pre-campaign history.

Fields include:

- plan ID/version;
- target World/Setting/Campaign preparation scope;
- start/end horizon and calendar/time profile;
- seed and deterministic method/version;
- allowed actor/entity definitions and owner domains;
- allowed operation/event templates;
- constraints/invariants;
- desired resolution depth;
- stop conditions and resource/performance budgets;
- permission/source visibility boundaries;
- required post-generation validation;
- promotion policy.

### 4.14 `HistoryBurnInProposalSet`

Contains generated candidate Events and proposed owner-state deltas with:

- stable proposal IDs;
- causal/dependency graph;
- source plan/seed/version;
- proposed actors/entities, including explicit generated-definition refs where allowed;
- requested owner operations;
- validation findings;
- unresolved gaps;
- optional alternative branches;
- no canonical mutation authority.

### 4.15 `HistoryBurnInPromotionReceipt`

Promotion is explicit and owner-authorized.

Requirements:

1. selected proposal subset must be dependency-closed, or the system must surface broken causal dependencies for explicit repair;
2. every canonical owner revalidates its requested operations at promotion time;
3. stable identities are minted only by their owners;
4. promoted Events retain burn-in plan/seed/version/proposal provenance;
5. rejected/unpromoted proposals remain noncanonical evidence only;
6. retries are idempotent and cannot duplicate historical Events or Assets.

## 5. Delayed consequence trigger families

Supported trigger classes are semantic categories, not a universal scheduler implementation:

1. `canonical_campaign_time`;
2. `project_or_plan_milestone`;
3. `canonical_event_occurrence`;
4. `owner_state_predicate`;
5. `knowledge_or_discovery_change`;
6. `location_or_presence_condition`;
7. `relationship_or_organization_state`;
8. `resource_or_economy_state`;
9. `explicit_gm_or_owner_release`;
10. `custom_governed_trigger`.

A trigger definition must declare which owner facts it is allowed to inspect. Protected or GM-only facts cannot leak through player-visible eligibility/countdown UI.

## 6. Persistence boundaries

### 6.1 What persists by default

Only already-canonical owner records/Events and explicit persistent orchestration records persist. A UI summary, generated story, speculative consequence or AI narration does not become history merely because it was shown.

### 6.2 Across Sessions

Campaign-local canonical Events, owner state, PPIA-08 history/snapshots and active governed Projects/deferred-consequence instances survive according to their owner retention rules.

### 6.3 Across Adventures within one Campaign

Campaign/World owner state persists according to Campaign rules. Adventure source definitions remain distinct from Campaign-run state.

### 6.4 Across generations/successors

The World/Campaign history remains. A replacement protagonist or NPC receives only explicitly owner-authorized transferred state. Historical relation to a predecessor may be linked without copying identity.

### 6.5 Across separate Campaigns

No automatic transfer of live Campaign state, reputation, Assets, knowledge or legacy mechanics. Reuse requires explicit template/import/clone/adaptation rules with provenance and Campaign-local acceptance.

## 7. Succession semantics

### 7.1 Identity preservation

A successor is normally a distinct identity with a `predecessor/successor` historical relationship. Identity merge or reincarnation/continuity-of-self requires an explicit Character/Species/Form/setting owner rule.

### 7.2 Role succession

ODL/organization owners decide whether a role is vacant, inherited, elected, appointed, contested, temporary, shared or abolished. A Packet-05 plan may orchestrate the request but cannot decide the result without owner rules.

### 7.3 Assets/property

No generic estate law is invented. Asset/economy/legal-setting owners decide transfer eligibility, debts, liens, confiscation, inheritance or abandonment.

### 7.4 Relationships and reputation

Direct relationships do not copy. Any family-name, office, faction, dynasty, predecessor-association or inherited-standing effect must be an explicit MIB-09/owner rule and must remain distinguishable from direct reputation.

### 7.5 Knowledge and memory

Private memory never teleports to a successor. Transfer requires communication, archive access, teaching, magical/technological transfer or another explicit owner mechanism. Institutional records may outlive individuals without becoming individual memories.

### 7.6 Abilities/progression

No automatic inheritance of Character abilities, XP, advancement, conditions or build state. Reusable training traditions or lineage packages are definitions; acquisition still follows progression rules.

### 7.7 Obligations/contracts/projects

Assignment or succession is owner-specific. Nonassignable personal obligations remain with the predecessor/estate/status defined by the owner.

## 8. Legacy/scar semantics

Legacy is an **event-backed projection of significance and enduring consequence**, not a universal stat.

A legacy projection can show:

- source Event(s);
- who/what was involved;
- current persistent consequences;
- resolved/historical consequences;
- public versus private/GM interpretations;
- institutional/cultural recollections;
- successor/dynasty/organization references;
- related locations/items/projects;
- later Events caused by or responding to the original occurrence.

If a setting wants a mechanical `Scar`, `Legend`, `Dynasty`, `Veteran`, `Trauma`, `Renown` or similar mechanic, that mechanic must be authored as an explicit owner-domain Effect/Condition/Resource/relationship/etc. Packet 05 supplies the history linkage and orchestration, not the mechanic itself.

## 9. Memory, forgetting and legend transformation

### 9.1 Separate truth from remembered story

At all times distinguish:

- what historically occurred;
- what a particular actor knew at a given time;
- what a record said;
- what an institution officially claims;
- what a culture remembers/tells;
- what a current viewer is permitted to know.

### 9.2 No universal decay clock

There is no built-in rule that memories become false after N years. Decay, archival survival, oral drift or immortal perfect memory are setting/profile-specific.

### 9.3 Transformation creates new evidence

A later legend, propaganda text, censored archive, memorial, revised doctrine or rediscovered chronicle is new record/knowledge/history evidence with its own provenance. It does not replace the original Event.

## 10. Delayed consequence execution

Flow:

`source Event → eligibility/profile match → DeferredConsequenceInstance armed → governed trigger occurs → evaluate against current authorized owner state → preview/explain → human/GM gate if required → emit owner-operation request(s) → owners revalidate/commit → resulting Events recorded → instance resolved/continued`.

Important rules:

- arming is not resolution;
- eligibility can become stale before commit;
- current state is revalidated at trigger/commit time;
- one consequence may emit multiple owner requests but cannot claim atomicity if owners cannot provide it;
- partial commit produces explicit partial/recovery state;
- stable operation IDs prevent duplicate firing after ambiguous responses;
- cancellation/expiration never deletes the source Event;
- definition upgrades do not retroactively change already-resolved consequences;
- migration of still-active instances must be explicit, previewable and versioned;
- a hidden consequence may remain hidden, but unauthorized users must not learn its existence through counts, timers, diagnostics or AI context.

## 11. History burn-in semantics

### 11.1 Why proposal-only

Burn-in is useful for producing a lived-in prehistory, but generated causality can touch every owner domain. Therefore it cannot directly write canonical history.

### 11.2 Burn-in stages

1. choose accepted source definitions/setting constraints;
2. choose time horizon, resolution and seed;
3. simulate/generate candidate Events through only permitted operation templates;
4. produce causal graph and proposed owner deltas;
5. run constraint/continuity/permission diagnostics;
6. GM/creator inspects summaries and drill-down;
7. select a dependency-closed proposal set or repair dependencies;
8. owner domains revalidate and commit promotion;
9. record canonical Events with exact burn-in provenance;
10. retain rejected alternatives as noncanonical proposals only if user chooses.

### 11.3 No retroactive fake evidence

Promotion may create canonical historical Events as an explicit worldbuilding act before play begins, but the system must record that they originated from accepted burn-in generation. It may not silently insert fake prior Events into an already-played Campaign to explain current state.

Backfill after play begins requires an explicit owner/GM-authorized historical reconstruction workflow with contradiction diagnostics and affected-current-state review.

## 12. Resolution depth

The same semantics support multiple history scales:

### `summary`

Major events, succession transitions, legacy markers and consequence milestones only.

### `standard`

Named important actors/organizations, key cause chains, owner-state transitions and deferred consequences.

### `detailed`

Finer Event chains and actor actions only where source/generated detail is supported and performance/permissions allow.

Rules:

- refinement cannot fabricate details absent from source/generation evidence;
- collapse preserves stable Event/subject references and major consequence provenance;
- a summary legacy never becomes a replacement Event;
- detailed burn-in may aggregate later, but re-expanding an aggregate cannot claim exact individuals/events that were never generated and promoted.

Packet 06 will extend aggregate simulation/refinement; Packet 05 defines only history/legacy semantics that Packet 06 must preserve.

## 13. Player / GM / creator UX contract

### 13.1 Five-second history surface

A permitted viewer can quickly distinguish:

- **what happened**;
- **when/where**;
- **who was involved**;
- **what still matters now**;
- **what is merely remembered/claimed**;
- **what future consequences are visible/telegraphed**;
- **what succession handoffs completed or failed**.

### 13.2 History explorer

WCI-compatible history view supports current/as-of/snapshot/hypothetical modes with explicit noncanonical labeling for hypothetical views.

### 13.3 Legacy card

Shows source Event, enduring consequence references, later related Events and visibility-safe interpretations. It never substitutes a mechanical Character sheet/Condition/relationship value.

### 13.4 Succession preview

Before commit, show handoff entries grouped by owner:

- guaranteed valid under current owner state;
- requires human/GM decision;
- blocked/invalid;
- nontransferable;
- unresolved because owner data is missing.

The UI cannot imply that one “inherit all” click bypasses owner rules.

### 13.5 Deferred-consequence inspector

Shows definition/version, source cause, current lifecycle, visible trigger conditions, owner targets and last evaluation receipt. Hidden trigger predicates are redacted before display/diagnostics.

### 13.6 Burn-in studio

Creator can preview horizon, seed, resolution, proposed event counts/categories, causal graph, contradictions, owner-domain impact and selected promotion set. Every graph operation has a textual/nonvisual equivalent.

## 14. Permission / visibility / knowledge

Filtering occurs before:

- history search;
- event counts/statistics;
- lineage/succession graph expansion;
- legacy lists;
- deferred-consequence counts/timers;
- institutional memory projections;
- burn-in context and generated proposals;
- current/as-of comparisons;
- exports;
- diagnostics;
- optional-AI context.

A hidden heir, secret marriage, covert succession rule, classified archive, unknown historical perpetrator or GM-only delayed trigger may not leak through cardinality, labels, dependency edges or error messages.

## 15. Provenance / replay / migration

Every consequential Packet-05 receipt identifies, where applicable:

- source Event/cause chain;
- definition/profile/version;
- seed/method version for generation;
- initiator/authorized actor;
- Campaign/World scope;
- exact owner versions inspected;
- requested operations;
- committed owner Event/result refs;
- previous/resulting orchestration state;
- visibility policy;
- operation/correlation IDs;
- supersession/migration/compensation refs.

Historical projections and delayed consequence evaluation must be reproducible for declared deterministic profiles from the same retained inputs. If an input was not retained, the system says replay is incomplete rather than fabricating it.

## 16. Concurrency and recovery

1. Succession handoff uses expected versions per owner entry; stale entries revalidate.
2. A successor cannot receive the same exclusive Asset/role twice through retry; operation IDs are idempotent.
3. Two competing succession plans may coexist as proposals but owners arbitrate mutually exclusive commits.
4. Deferred consequence evaluation and commit are separate; state can change between them and invalidate the request.
5. Ambiguous owner responses require status lookup before retry.
6. Partial cross-owner commit enters explicit recovery state; no orchestrator lies that all effects succeeded.
7. Burn-in promotion uses stable proposal IDs; retry cannot duplicate canonical Events.
8. A definition/profile version change cannot silently reinterpret already-promoted historical Events.

## 17. Failure and edge cases

Packet 05 explicitly closes these cases:

- source Event missing/deleted/unavailable → binding/projection reports broken/unavailable provenance; no invented replacement;
- historical state not retained → `unknown/not_retained`;
- predecessor and successor accidentally identical → reject unless owner explicitly supports same-identity transformation;
- successor lacks role eligibility → role transfer rejected while other handoffs may proceed;
- Asset already transferred/consumed → stale handoff fails safely;
- obligation is nonassignable → do not transfer;
- hidden heir/succession rule → filtered before unauthorized graph/count output;
- delayed consequence trigger becomes impossible → profile determines cancelled/expired/blocked; no silent infinite polling;
- source Event later reversed/compensated → delayed instance re-evaluates according to explicit profile rather than assuming cancellation;
- multiple compatible delayed consequences → apply explicit coalescing/stack rules; no universal stacking;
- delayed consequence uses old definition version → pinned version remains unless explicit migration accepted;
- Campaign paused/archived → no wall-clock progression;
- current owner state conflicts with planned narrative consequence → owner state wins; consequence blocks/revalidates;
- institutional record conflicts with Event truth → show claim conflict to authorized roles; do not overwrite truth;
- archive destroyed → knowledge/record availability changes via Event; source history remains;
- memory decay rule absent → do not decay;
- burn-in proposes unsupported owner operation → validation failure; proposal cannot promote;
- burn-in causal cycle → diagnose; no automatic promotion;
- partial burn-in selection breaks dependency closure → block until dependency repair/revalidation;
- burn-in generates identity collision → owner identity resolver rejects/renames/remaps through explicit workflow;
- burn-in references hidden source not authorized for creator → filtered before generation;
- hypothetical history accidentally opened in live view → must retain explicit noncanonical mode label and cannot commit without promotion workflow;
- optional AI unavailable → all manual/deterministic history, succession, deferred consequence and burn-in workflows remain functional.

## 18. Accessibility

Required nonvisual parity:

- textual chronological history list with semantic relationships;
- keyboard-accessible as-of controls;
- lineage/succession lists and owner-grouped handoff previews that do not depend on graph geometry;
- delayed consequence state/trigger explanation in text, not color/timer alone;
- burn-in causal/dependency graph represented as navigable semantic outline;
- explicit labels for canonical/current/historical/hypothetical/proposed states;
- screen-reader announcements for blocked/stale/partial owner handoffs;
- no animation, audio or visual-only memorial/legacy cue may be the sole carrier of consequential information.

## 19. Golden vectors

Future implementation must automate or equivalently prove these cases.

### Legacy/history

- **PDCP-HIS-001** — an accepted Event produces a legacy binding; source Event remains unchanged.
- **PDCP-HIS-002** — an enduring Character Condition appears as a referenced current consequence, not copied into the legacy record.
- **PDCP-HIS-003** — Condition later resolves; legacy still shows historical consequence plus resolved status.
- **PDCP-HIS-004** — source Event definition later changes version; historical view preserves version used at occurrence.
- **PDCP-HIS-005** — missing historical field returns `unknown/not_retained`, not reconstructed fiction.
- **PDCP-HIS-006** — current and `as_of_event` projections differ while sharing stable entity identity.
- **PDCP-HIS-007** — hypothetical alternate history is visibly noncanonical and cannot mutate current state.
- **PDCP-HIS-008** — unauthorized user cannot infer hidden historical Event from legacy counts or relationship edges.

### Institutional/cultural memory

- **PDCP-HIS-009** — organization remembers a battle through retained archive/event refs without gaining hidden GM truth.
- **PDCP-HIS-010** — official account conflicts with protected actual Event; permitted GM view sees both, ordinary member sees only authorized claim.
- **PDCP-HIS-011** — archive-destruction Event removes access to a record but does not delete historical occurrence.
- **PDCP-HIS-012** — no memory-decay profile exists; system does not invent forgetting.
- **PDCP-HIS-013** — authored oral-tradition rule creates a later transformed claim with its own provenance.
- **PDCP-HIS-014** — rediscovery restores access/knowledge through a new Event, not by rewriting prior ignorance.

### Succession

- **PDCP-HIS-015** — retiring leader transfers an ODL role but no Assets or relationships absent owner rules.
- **PDCP-HIS-016** — successor receives a named Asset through Asset-owner transfer; retry does not duplicate ownership.
- **PDCP-HIS-017** — private predecessor memory is not copied to successor.
- **PDCP-HIS-018** — archive access is granted to successor; institutional records become readable without becoming personal memories.
- **PDCP-HIS-019** — faction rule grants predecessor-association standing; MIB-09 keeps it distinct from direct reputation.
- **PDCP-HIS-020** — one handoff entry fails eligibility while independent entries succeed; receipt records partial outcome.
- **PDCP-HIS-021** — hidden successor identity is filtered before unauthorized succession graph/cardinality output.
- **PDCP-HIS-022** — two competing succession plans race; owner expected-version checks prevent double-exclusive role commit.
- **PDCP-HIS-023** — nonassignable obligation remains with predecessor/estate owner state rather than transferring silently.
- **PDCP-HIS-024** — reincarnation/same-identity continuity is rejected by default and accepted only under explicit Character/setting rule.

### Deferred consequences

- **PDCP-HIS-025** — Event arms a consequence for Campaign day 30; closing app for 30 real days does not fire it.
- **PDCP-HIS-026** — canonical Campaign time reaches threshold; evaluation emits owner request but does not mutate until owner commit.
- **PDCP-HIS-027** — target state changes between evaluation and commit; owner revalidation blocks stale request.
- **PDCP-HIS-028** — hidden delayed consequence does not leak through player-visible count/timer/AI context.
- **PDCP-HIS-029** — ambiguous owner response is recovered by operation-status lookup without duplicate effect.
- **PDCP-HIS-030** — cancelled consequence retains source Event/history and cancellation provenance.
- **PDCP-HIS-031** — definition version updates while instance is armed; pinned instance does not silently change semantics.
- **PDCP-HIS-032** — explicit migration previews and records conversion to new definition version.

### History burn-in

- **PDCP-HIS-033** — fixed seed/profile produces reproducible proposal graph where determinism is declared.
- **PDCP-HIS-034** — burn-in proposal changes no canonical World/Character/Event state before promotion.
- **PDCP-HIS-035** — unsupported owner operation is surfaced and blocks affected proposal promotion.
- **PDCP-HIS-036** — partial selection that breaks causal dependency closure is rejected until repaired.
- **PDCP-HIS-037** — dependency-closed selected history promotes through owners and records exact plan/seed/proposal provenance.
- **PDCP-HIS-038** — retrying promotion does not duplicate promoted Events/entities/Assets.
- **PDCP-HIS-039** — post-play historical backfill that contradicts current canonical evidence requires explicit contradiction review and cannot silently insert history.
- **PDCP-HIS-040** — burn-in causal graph has a complete keyboard/screen-reader semantic outline with canonical/proposed status labels.

## 20. Future-family implementation mapping

Packet 05 creates **no new family and no standalone tranche**. Residual implementation fits existing planned scopes.

### MNCS

- `MNCS-04` — origin/lineage references during construction without identity cloning;
- `MNCS-07` — knowledge, belief, memory and misinformation projections;
- `MNCS-09` — household/project/life context that may survive or hand off;
- `MNCS-15` / `MNCS-16` — group/organization/population continuity references;
- `MNCS-20` — continuity, Events, advancement and life/ecology change over time;
- `MNCS-21` — promotion/demotion/retirement and simulation-resolution management;
- `MNCS-23` — provenance/import/export/review;
- `MNCS-24` — golden Campaign-continuity proof.

### MRCS

- `MRCS-02` — schema-aware authoring for legacy/deferred/succession/burn-in definitions;
- `MRCS-05` — Action/Effect/Condition/Resource/trigger authoring for delayed consequence outputs;
- `MRCS-08` — Culture/Faction/social-package authoring for memory/succession rules;
- `MRCS-16` — scoped extension/override/version/migration semantics;
- `MRCS-17` — dependency/impact analysis for causal history and deferred consequence references;
- `MRCS-20` — versioning/diff/provenance/publication;
- `MRCS-21` — cross-domain golden proof.

### GPR

- `GPR-05` — objective/world-route/progression integration with persistent consequences;
- `GPR-08` — data-driven pattern composition for deferred consequences and succession orchestration;
- `GPR-09` — delivery-mode parity for history/legacy interactions;
- `GPR-12` — replay/determinism/Event trace;
- `GPR-13` — persistence/snapshot/migration/version compatibility;
- `GPR-14` — Creator/GM inspection, preview and world binding;
- `GPR-16` — golden runtime proof/handoff.

### MSWI

- `MSWI-02` — persistent world-transformation attribution/history;
- `MSWI-03` — delayed/cross-system propagation, reversibility and recovery;
- `MSWI-09` — doctrine/ideology/organization historical consequences and institutional memory;
- `MSWI-10` — downtime/life loop consequences over Campaign time;
- `MSWI-13` — long-lived world-project milestones and successors;
- `MSWI-15` — current/historical visible World/Scene variants;
- `MSWI-16` — transformation Campaign templates, including generational/legacy profiles;
- `MSWI-17` — causal fan-out/loop/dead-route diagnostics;
- `MSWI-18` — golden systemic proof.

### No direct new Packet-05 obligation

`MCS`, `MCCS`, `MSAS`, `MERA`, `MBES`, and `MSLR` may consume historical/current projections through their normal owner seams but receive no standalone Packet-05 implementation obligation.

`MAS` remains outside PDCP and is not reopened.

## 21. Roadmap-reduction implication

Packet 05 closes the product semantics before future family execution. Family reduction reviews may therefore remove or merge future tranche work whose only remaining obligation was to decide:

- how legacy/scars persist;
- whether successors copy predecessor state;
- where delayed consequence timing lives;
- whether culture/organization memory is a new ledger;
- how as-of/current history differs;
- whether history burn-in can write canonical state directly.

Those questions are now closed. Surviving tranches need only implement schemas/UI/runtime adapters/migrations/tests/performance and exact-head validation needed by their existing owners.

## 22. Closure result

**Result:** `design_closed`

- New family required: **no**.
- New standalone tranche required: **no**.
- Owner decision remaining: **no**.
- Roadmap count changed by this packet: **no**.
- Capability loss detected: **no**.
- Golden vectors closed: **40**.
- Affected future families: **MNCS, MRCS, GPR, MSWI**.
- Next benchmark packet: **PDCP Packet 06 — Multi-Resolution Simulation & Autonomous World Evolution**.
