# MV-IA-F010 — Social Interaction Mode

**Feature ID:** MV-IA-F010  
**Feature version:** 0.1.0  
**Classification:** alpha-required  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Player, Game Master, Assistant GM, Observer  
**Stage A mapping:** A9  
**Historical module mapping:** Social Interaction Mode  
**Prepared by:** OpenAI design agent under owner authority  
**Reviewed by:** deterministic package validation and final hosted gate  
**Date:** 2026-08-06

## 1. Problem and user outcome

### Problem

Social play becomes unusable when every conversation is forced into initiative, Persuasion becomes mind control, NPC truth is mixed with Player belief, hidden motives leak into Player views, or relationship, faction standing, mood, stance, promises, inventory, clues, and combat are mutated by a private social subsystem.

### Required outcome

Players can roleplay freely, optionally use assisted Actions, or enter a structured social challenge. A Player submits intent and evidence without being forced to write full dialogue. The GM sees the full authorized context, approves, denies, modifies, or directly resolves through the shared proposal/approval contract, and commits one atomic group of domain-owned outcome Events. Player and GM receive different role-safe results, and the interaction survives reload, duplicate delivery, disconnect, reconnect, and transition to or from combat.

### Why this belongs in internal alpha

The alpha requires one social Scene that produces a persistent relationship, standing, promise, debt, access, price, clue, Condition, or other governed consequence. Social Mode is also the runtime bridge among F006 Actions, F009 relationships, F016 factions/standing, F011 investigation, F008 inventory, F005 Scenes/Sessions, and future adventure flow.

## 2. Alpha slice

### Included

- Three modes: freeform, assisted Action, and structured challenge.
- Registry-ready Social Action Definitions across fourteen categories and six timing types.
- Seven required alpha Actions: Request Information, Request Favor, Persuade, Negotiate, Deceive, Intimidate, and Insight.
- Six resolution methods and seven degree outcomes.
- Social Interaction Context, proposal extension, resolution record, challenge state, Event group, Player/GM projections, and history.
- NPC truth, knowledge, belief, mood, intent, stance, values, boundaries, authority, relationships, standing, statuses, leverage, promises, and relevant clues as separately authorized context.
- GM action inbox and Player compact/full Social Mode surfaces.
- Role-safe reveals, hidden modifiers, hidden outcomes, and player-specific knowledge.
- Atomic cross-domain consequences and compensating undo.
- Combat, trade/inventory, clue, relationship, faction, access, rumor, promise, favor, leverage, Condition, and NPC schedule adapters.
- Responsive, keyboard, screen-reader, touch, reduced-motion, and noncolor parity.

### Explicitly excluded

- Personal relationship storage and reveal ownership, owned by MV-IA-F009.
- Faction standing/influence storage, owned by MV-IA-F016.
- Investigation truth, evidence, hypothesis, and clue-board design, owned by MV-IA-F011.
- Inventory/currency ownership and transfer, owned by MV-IA-F008.
- Combat runtime, owned by MV-IA-F007.
- AI-controlled NPC portrayal or irreversible AI decisions.
- Full autonomous negotiation agents, universal social difficulty tables, and forced dialogue generation.

### Full long-term scope deferred

Advanced crowd simulation, large public-opinion campaigns, autonomous rumor networks, broad political simulation, speech/voice analysis, multiplayer simultaneous debate, and AI-operated NPCs remain deferred. The design preserves pack extension points without authorizing those systems.

## 3. Roles and authority

| Role | Allowed actions | Hidden information | Approval required |
|---|---|---|---|
| Player | Roleplay freely; draft/submit authorized social Actions; view Player-safe context, pending state, result, and history | Cannot read NPC truth, hidden modifiers, motives, secrets, lies, unrevealed relationships/standing/clues, or other Players’ private knowledge | Submitted structured consequences use shared approval or explicit GM/domain authority |
| Game Master | Start/configure interactions, inspect authorized truth, review/modify/deny/resolve proposals, select reveals and consequences, portray NPCs, transition modes/combat | May read authorized Campaign truth | Cross-domain Events must pass their owning domain validators; release/canon/spend gates remain separate |
| Owner/Admin | Governance and explicit support actions | Account role alone does not grant Campaign-hidden or Player-private social data | Existing owner/security/support/release gates apply |
| Content Creator | Define reusable Actions, resolution/outcome profiles, statuses, and pack content | Cannot mutate live Campaign interactions or promote content silently | Canonical promotion remains owner-gated |
| Assistant GM/Observer | Assistant GM acts within delegation; Observer reads observer-safe projection | Delegation and audience filtering apply before serialization | Mutation requires current delegated authority |
| Service actor or AI | Validate, project, summarize, suggest options, or draft GM-visible responses within typed authority | No bypass of visibility, truth/belief, search, export, diagnostics, or AI filtering | AI has no NPC-truth, reveal, decision, result, dialogue, romance/coercion, item/currency, combat, or canonical authority |

The GM portrays the NPC. Persuasion is not mind control. Silence is not approval.

## 4. Dependencies

### Feature dependencies

- MV-IA-F006 — First Playable Action and GM Approval Loop.
- IA-D04-002 — Proposal and Approval Shared Component.
- IA-D04-003 — Two-Device Interruption and Reconnect Matrix.
- IA-D04-004 — Authoritative Result and History Presentation.
- MV-IA-F009 — Relationship Tracker.
- MV-IA-F016 — Factions, Reputation, and Organizations.
- MV-IA-F005 — Campaign, Scene, and Session Builder.
- MV-IA-F020 — Permissions and Hidden Information.
- MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use.
- MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting.

### Shared systems

- SS-02 Universal Object Experience.
- SS-03 stable references/provenance.
- SS-06 proposal/approval.
- SS-07 permission-safe search/pickers.
- SS-08 persistence, Event groups, and history.
- SS-11 notifications/status lookup.
- SS-12 adaptive UI.
- SS-13 accessibility.
- SS-14 diagnostics/issue reports.
- SS-19 reconnect/recovery.

### Service ports and adapters

- identity, authorization, entitlement, persistence, Event group, projection, roll, rules-profile, relationship, faction standing/influence, clue/reveal, inventory/currency, access, Condition, NPC schedule, combat transition, notification, realtime, export, and diagnostics ports.

### Canonical objects and packs

- Social Action Definition;
- Resolution Profile Definition;
- Outcome Profile Definition;
- Social Interaction Context;
- Social Action Proposal as an IA-D04-002 consumer profile;
- Social Action Resolution;
- Social Challenge State;
- NPC belief/lie/rumor records where applicable;
- domain-owned relationship, standing, status, Bond, leverage, favor, promise, clue, access, price, inventory, NPC schedule, Condition, and combat records.

### Schemas and migrations

Social Action names and examples must normalize to registry definitions with stable IDs and versions. Existing NPC traits or local social wrappers remain source/provenance until mapped; ambiguous names do not become executable Actions automatically. Social Mode stores references to domain-owned state rather than copying it into one interaction document.

### Decisions and gates

Design may complete while implementation dependencies remain unfinished. Application implementation remains dependency-gated, including `P9-06-008-attempt-002`. No paid service, production credential, real-user data, deployment, release, AI authority, or canonical promotion is authorized.

## 5. Object and state model

### Reusable Definitions

- Social Action Definition with category, timing, target/input rules, eligible skills, prerequisites/restrictions, resolution profile, outcome profile, visibility, effects, and provenance;
- Resolution Profile for no-roll, fixed DC, opposed check, degree of success, extended challenge, or GM-determined resolution;
- Outcome Profile for plausible degrees, consequences, reveals, and domain adapters;
- Social Status definitions with explicit scope;
- pack-defined resources for extended challenges.

The fourteen source categories are request, persuasion, negotiation, deception, intimidation, insight, empathy, command, performance, trade, investigation, relationship, political, and custom. The six timing types are conversation, exchange, Scene, downtime, reaction, and special.

### Campaign placements or bindings

- Campaign/Scene binding for approved Social Action, resolution, outcome, status, and visibility profiles;
- active Social Interaction Context bound to Campaign, Scene, optional Encounter, participants, audience, objective, stakes, Location, culture, jurisdiction, and exact rules-profile versions;
- references to active F009 relationships, F016 standing, scoped statuses, leverage, promises/obligations, relevant clues, mood, intent, stance, and optional challenge state.

### Live instances and state

A Social Interaction Context has a stable ID, Campaign/Scene/Encounter references, mode, participants, primary NPCs, audiences, objective, stakes, context references, current NPC stance/mood, challenge state, visibility profile, lifecycle status, history Event-group IDs, aggregate version, and correlation ID.

A Social Action Proposal extends IA-D04-002 with acting actor/entity, Action definition/version, targets/audiences, stated intent, requested outcome, chosen skill, selected Abilities, offered leverage/items/currency, promise drafts, optional Player statement/notes, computed safe context, warnings, expected versions, and operation identity.

A Social Action Resolution records final proposal/decision, GM attribution, method/profile, roll/target/opposition, hidden modifiers, degree, NPC response summary, Player-safe summary, GM summary, Event drafts, reveal drafts, validation receipts, Event-group ID, and resolved timestamp.

NPC truth, objective facts, NPC beliefs, Player beliefs, lies, rumors, knowledge, motives, secrets, values, boundaries, mood, intent, stance, and relationship/standing remain distinct records or fields with separate visibility.

### Events and history

Social Mode owns interaction lifecycle and resolution Events: `SocialInteractionStarted`, `SocialParticipantAdded`, `SocialParticipantRemoved`, `SocialInteractionModeChanged`, `SocialActionProposed`, `SocialActionApproved`, `SocialActionModified`, `SocialActionDenied`, `SocialActionResolved`, `SocialChallengeStarted`, `SocialChallengeAdvanced`, `NPCStanceChanged`, `NPCMoodChanged`, `NPCResponseScheduled`, `SocialInteractionPaused`, `SocialInteractionResumed`, and `SocialInteractionEnded`.

All persistent consequences use domain-owned Events. The source enumerates twenty-nine possible outcome Event drafts, including relationship, stance, status, standing, influence, Bond, favor, promise, debt, leverage, clue, rumor, access, price, inventory, NPC schedule, quest, combat, departure, Condition, and public-opinion changes.

### Projections and indexes

- Player compact interaction projection;
- Player full Social Console;
- GM Social Operations projection;
- action inbox/review projection;
- NPC social summary;
- interaction history;
- social challenge state;
- role-safe notifications, search, exports, diagnostics, realtime, and AI context.

### Stable IDs

Display labels, dialogue text, trait names, and source examples never replace Action, profile, participant, proposal, decision, resolution, Event-group, reveal, belief, clue, item, currency, or domain-record IDs.

### Provenance

The source describes forty-nine Action forms across ten detailed action-family sections and thirty-eight command names. The 209-row social-mechanic register contains 196 unmatched local wrappers, ten exact unique resolutions, and three ambiguous exact-name cases; none become executable Action definitions automatically. The 153-row role register and visibility map provide NPC role and staged-reveal fixture coverage, not hidden motive or mechanical completion.

## 6. Primary user flow

1. The GM starts or opens a Social Interaction Context from a Scene/NPC and chooses freeform, assisted, or structured-challenge mode.
2. Player and GM receive separately authorized context projections.
3. The Player roleplays freely or selects one of the seven alpha Actions and provides intent; full dialogue is optional.
4. The client shows targets, requested outcome, relevant visible relationship/standing/status/leverage, chosen skill/Abilities, offers, warnings, and proposed resolution evidence.
5. The Player confirms and submits one idempotent shared proposal.
6. The GM inbox shows actor, Action, target, objective, statement, skill, Abilities, offered leverage/items/currency, visible and hidden modifiers, boundaries, authority, possible outcomes, and exact source/profile versions.
7. The GM approves, denies, modifies, or selects a direct GM-determined result; final values are revalidated.
8. The server atomically commits one resolution Event group and all accepted domain-owned consequences.
9. The Player sees a concise safe result; the GM sees full authorized truth and history.
10. Reload/reconnect converges by operation, decision, resolution, Event-group, and projection identity without duplicate consequences.

## 7. Alternate and secondary flows

### Alternate flow A — freeform/no-roll

1. Players and GM roleplay without opening a structured Action.
2. Freely offered information or an obvious plausible response may resolve with no roll.
3. Persistent consequences still require an attributable GM/domain command and Event group.

### Alternate flow B — hidden deception result

1. A Player submits Deceive with the false claim and intended belief.
2. The NPC belief may change while objective truth remains unchanged.
3. The Player receives only the authorized interpretation; contradictory evidence may later create a belief/history change.

### Alternate flow C — extended social challenge

1. The GM starts a profile-defined challenge with objective, stakes, resources, thresholds, participant roles, and failure/exit conditions.
2. Each exchange advances one Event-backed challenge step.
3. Completion produces one final Event group; it does not convert every conversation into initiative.

### Alternate flow D — combat transition

1. De-escalation may pause or prevent combat only when plausible and authorized.
2. A failed or escalated interaction may start combat.
3. Transition reuses existing participants, Scene, identity, Conditions, and history; it does not recreate them.

### Alternate flow E — trade or access

1. Negotiation, gift, bribe, trade, or petition creates structured terms.
2. Inventory/currency or access domains revalidate ownership, custody, price, entitlement, permission, and expected versions.
3. Social UI never edits inventory/currency or access directly.

## 8. Failure, empty, and recovery states

| State | User sees | Allowed action | Preserved data | Evidence |
|---|---|---|---|---|
| Loading | Safe participant/context placeholders without hidden counts | Cancel or continue freeform | current projection | correlation ID |
| Empty | No active authorized interaction | Start if authorized or return to Scene | draft context | projection version |
| Validation error | Field-specific target, Action, offer, skill, boundary, or profile issue | Correct draft | proposal draft | validation receipt |
| Forbidden | Not-found-or-unavailable response | Return to authorized context | no protected payload | denial code |
| Restricted entitlement | Action/profile unavailable without protected preview | Select available content | draft references | entitlement decision |
| Offline | Cached context labeled nonauthoritative; freeform/local draft only | Roleplay, inspect cache, edit draft | local draft/cache | manifest |
| Pending | Durable proposal awaits authorized decision | Cancel if allowed, check status | proposal ID | status receipt |
| Status unknown | Submission/decision/result response lost | Status lookup before retry | operation/proposal IDs | command-status receipt |
| Stale | context/proposal/domain version changed | Reload/compare/reapply | safe draft and current versions | conflict record |
| Event gap | result history is incomplete | Recover ordered Events/snapshot | durable result | recovery receipt |
| Revoked | protected context removed immediately | Return to authorized context | public-safe state only | revocation receipt |
| Recovery required | schema/pack/dependency/sequence conflict | guided recovery | authoritative server state | recovery receipt |

No pending, cached, stale, ambiguous, or partial Event group is presented as completed.

## 9. Permissions and hidden information

### Authorization questions

- NPC true identity, motives, fears, values, boundaries, intent, mood, lies, secrets, knowledge, authority, relationships, standing, faction ties, inventory/price data, clues, and hidden modifiers are field-filtered before serialization.
- Players may separately know aliases, true identity, relationship fields, standing form, clues, motives, locations, inventory/price facts, and history.
- One Player’s private reveal does not reveal to the party.
- Hidden target existence, participant counts, action options, difficulty, modifiers, outcomes, and follow-up opportunities cannot leak through API errors, counts, search, notifications, exports, diagnostics, realtime, or AI context.
- GM direct outcome selection records reasons and attribution.
- Assistant GM review/modification is limited by active delegation.
- AI context is built only from the current role-safe projection.
- Revocation clears interaction, proposal, truth, history, clue, and AI context from every device.

### Required denied-case tests

The matrix includes unauthenticated/inactive context, wrong Campaign/Scene, hidden participant/target, unauthorized Action/profile, invalid target, impossible request, boundary violation, missing GM authority, stale proposal/context/domain version, conflicting duplicate operation, hidden modifier disclosure, NPC truth disclosure, private Player knowledge disclosure, mind-control outcome, insight-as-truth-reveal, intimidation-as-loyalty, deception-rewrites-truth, automatic romance/coercion, unapproved inventory/currency/access mutation, clue reveal bypass, client authority, offline authoritative submit/decision, duplicate Event group, partial cross-domain commit, AI decision/dialogue/reveal, and pack lifecycle rewrite/delete.

## 10. Entitlements

- Access sources: installed approved social Actions/profiles, Campaign grants, free approved content, and explicit entitlements.
- Free-tier behavior: the seven alpha Actions, core profiles, Player/GM UI, and zero-AI operation remain usable without paid services.
- Campaign grants: may permit bounded use without exposing the source library broadly.
- Sponsored access: existing entitlement evaluator applies; no social bypass.
- Expiry behavior: new Action/profile use may be restricted while authorized historical interaction/result state remains readable under policy.
- Historical-state behavior: exact Action, profile, Ability, rule, pack, item, clue, relationship, standing, and Condition versions remain bound.
- Search and preview restrictions: unavailable Actions/profiles/targets are not enumerated.
- Offline snapshot behavior: authorized cache and local drafts only; no authoritative proposal, decision, resolution, reveal, transfer, or transition offline.

## 11. Persistence and history

- Draft storage: local autosave for approved context/proposal drafts, clearly nonauthoritative.
- Authoritative save: online server commands only.
- Aggregate boundary: Social Interaction Context and Challenge State; proposals/decisions use shared component; consequences remain domain-owned.
- Expected-version behavior: context, proposal, target, relationship, standing, leverage, promise, clue, inventory, currency, access, Condition, and combat versions are checked as applicable.
- Idempotency: stable operation/decision/resolution/Event-group identities prevent duplicate consequences.
- Event types: sixteen owned lifecycle Events and delegated domain Events.
- Snapshot or checkpoint behavior: preserves exact context, participants, profiles, challenge state, Event sequence, visibility, and external refs.
- Audit events: actor, authority, proposal/decision/resolution, changed paths, original/final values, hidden-field class, source/profile versions, timestamp, and correlation.
- Undo behavior: append a validated compensating Event group for reversible outcomes; never delete history or pretend irreversible external effects did not occur.
- Migration behavior: preserve source Action names/traits as provenance until uniquely mapped; ambiguous mechanics remain unresolved.
- Export behavior: same role-safe projection as interactive history.

## 12. Realtime, interruption, and reconnect

- Before local autosave: preserve editor state where possible; no authority.
- After autosave before submit: restore draft.
- After submit before response: status lookup before retry.
- While pending GM: proposal remains durable; GM disconnect does not approve/deny it.
- After decision before resolution commit: decision status is resolved before any retry.
- After Event-group commit before display: reconnect returns one committed result.
- During Event gap: do not invent missing outcomes; recover ordered Events or current snapshot plus sequence anchor.
- With stale context/domain state: fail closed and provide safe compare/reapply.
- From second device: stable IDs, expected versions, review-claim rules, and idempotency prohibit duplicate or silent last-write-wins behavior.
- After revocation: reauthorize before resubscription and purge protected context/history/AI state.

## 13. Interface and information hierarchy

### Desktop

Player full Social Console shows participant cards, current objective/stakes, authorized relationship/standing/status/leverage context, Action picker, intent/offers, warnings, pending/result summary, and accessible history. GM Social Operations shows participants, NPC truth panel, reveal panel, relationship/standing controls, action inbox, resolution controls, possible outcomes, challenge state, NPC response support, and history.

### Tablet

Participant/context pane with named sheets for Action draft, offers, proposal review, NPC truth, reveals, challenge state, and result/history.

### Mobile

A compact active panel is primary: participants, Action/intent, target, selected skill/offer, submit/pending/result. Full Console and GM Operations use single-task routes/sheets. The app never requires a graph or wide comparison to complete the alpha flow.

### Player hierarchy

Scene/participants, goal, Action/intent, target, visible context, cost/offer, warnings, confirmation, pending, and Player-safe result are foregrounded. Social log remains accessible but secondary.

### GM hierarchy

Actor, target, objective, statement, skill/Abilities, offers, visible/hidden modifiers, NPC knowledge/authority/values/boundaries, relationship/standing/status/leverage, method/DC/opposition/degree, reveals, consequences, and exact source versions are present at decision time.

## 14. Accessibility

- Semantic structure: participant, objective, Action, evidence, modifier, decision, result, and history regions use headings/landmarks.
- Keyboard flow: select participants/Actions/targets, edit intent/offers, submit, review, modify, resolve, reveal, transition, and recover without pointer input.
- Focus behavior: drawers/sheets return focus to the originating Action/proposal/participant.
- Screen-reader names and states: announce authorized participant identity, Action, target, chosen skill, offers, warnings, pending/status-unknown/stale/result state, decision, and Player-safe consequence.
- Live announcements: proposal submitted, decision made, resolution committed, challenge advanced, reveal changed, conflict, Event gap, combat transition, and revocation.
- Text scaling: no clipped statements, modifiers, options, or consequences.
- Contrast and noncolor status: stance, degree, pending, hidden/revealed, stale, conflict, and consequence use labels/icons.
- Reduced motion: transitions and challenge progress animation can be disabled.
- Touch targets: shared minimum sizes.
- Nondrag alternatives: forms/menus for ordering participants or challenge resources.
- Map/graph alternative: not required for core flow; referenced relationship/faction context has list alternatives.
- Error identification and recovery: field-specific messages with focusable actions.

## 15. Notifications and queues

| Trigger | Recipient | Message content | Action | Resolution state |
|---|---|---|---|---|
| Proposal submitted | authorized GM/Assistant GM | actor, Action, target, objective, safe offers/warnings | Open review | pending |
| Proposal modified/denied | Player and authorized staff | user-safe changed fields/reason | Review draft/result | final or resubmit |
| Resolution committed | affected authorized roles | safe degree, response, accepted consequences | Open result/history | resolved |
| Hidden reveal changed | affected audience and GM, filtered | newly available safe field | Open participant/context | resolved |
| Challenge advanced | participants and GM, filtered | current public progress/resources | Open challenge | active/resolved |
| Combat transition | authorized Scene participants | transition state and next surface | Open combat/social | resolved |
| Stale/Event gap/reconnect | affected device | safe recovery status | Recover | recovery required |
| Revocation | affected subject/devices | access changed and protected data removed | Return to authorized context | revoked |

## 16. AI involvement

**AI mode:** optional advisory, draft-only, GM-mediated

- Allowed actions: summarize visible context, highlight visible leverage, suggest plausible approaches, identify relevant Actions/Abilities/statuses, draft several GM-visible NPC response options, summarize interaction history, and convert GM notes to draft fields.
- Allowed sources: current role-safe projection plus explicitly selected source-safe records.
- Permission and entitlement checks: identical to product retrieval before AI context construction.
- Provenance: AI suggestions cite included context/profile versions and remain labeled drafts.
- Uncertainty: AI distinguishes NPC truth, belief, Player belief, inference, and missing information.
- Cost boundary: core Social Mode is complete without AI; no paid model is required.
- Non-AI fallback: GM and Players can perform every alpha flow manually.
- Prohibited behavior: decide motives, expose hidden information, speak for Players, force emotional/romantic/coercive outcomes, change relationships/standing, spend currency, transfer items, reveal clues, start/end combat, portray NPCs irreversibly, or overwrite GM notes.

## 17. Telemetry and diagnostics

- Operation IDs: interaction, proposal, decision, resolution, Event-group, reveal, challenge-step, transition, and status-lookup IDs.
- Correlation IDs: connect draft, validation, review, roll, decision, Event group, domain adapters, projections, notifications, and result UI.
- Performance measurements: context load, Action picker, validation, GM review, resolution, Event-group commit, projection, reconnect, and transition latency.
- Error events: safe validation/resolution/domain-adapter class without hidden content.
- Permission denials: surface and decision reference without protected participant/truth details.
- Reconnect events: proposal/decision/resolution status, sequence gap, recovery outcome, projection version.
- Privacy redaction: motives, secrets, lies, hidden modifiers, private notes/knowledge, unrevealed clues/relationships/standing, and dialogue content excluded by default.
- Issue-report attachment: explicit preview/consent under F025.
- Cost signals: local/server resource use and optional AI usage separately; no paid dependency required.

## 18. Test scenarios

### Unit

- Validate fourteen Action categories, six timing types, six methods, seven degrees, target/input/prerequisite rules, and profile-defined example DCs.
- Validate success against NPC knowledge, authority, values, boundaries, and circumstances.

### Contract

- Interaction Context, proposal, resolution, challenge, Event group, and domain consequence records remain distinct.
- NPC truth, belief, Player belief, lie, rumor, mood, intent, stance, relationship, and standing remain distinct.
- Shared proposal/approval and result/history fields are reused, not copied privately.

### Integration

- F009, F016, F011, F008, F005, F007, Conditions, access, and NPC schedule adapters validate before atomic commit.
- Social UI never directly edits inventory, currency, clue truth, relationships, standing, or combat state.

### End-to-end

- Request a minor favor, show authorized relationship/leverage/boundaries to GM, resolve, create one persistent favor or refusal consequence, and reload.
- Deceive: change NPC belief without changing objective truth; later evidence updates belief/history.
- De-escalate combat and preserve participants/Scene/history.

### Permission and hidden information

- Player-safe Insight does not reveal exact hidden motive.
- One Player learns a true identity/clue while others retain alias/hidden state.
- Hidden modifiers and outcomes never leak through side channels.

### Entitlement

- Unavailable Action/profile is not enumerated.
- Pack expiry restricts new use without rewriting historical interaction/result records.

### Persistence and migration

- Ambiguous source mechanic names remain unresolved.
- Pack update/removal does not rewrite/delete live interactions, statuses, promises, or history.

### Reconnect and recovery

- Lost submit/decision/result response uses status lookup and yields one Event group.
- Duplicate delivery creates no duplicate consequence/history row.
- Revocation clears protected interaction truth/history from two devices.

### Accessibility

- Screen reader completes Player submit and GM approve/modify/deny/resolve in semantic order.
- Mobile completes freeform, assisted Action, result, challenge, and combat transition without desktop layout.

### Performance

- Bounded alpha participant/context/action list remains responsive; broad crowd simulation is deferred.

### Golden or deterministic regression

- Twenty-four fixtures cover seven alpha Actions, six methods, hidden results, truth/belief, partial success, cross-domain atomicity, undo, permissions, accessibility, pack lifecycle, transition, and reconnect.

## 19. Acceptance criteria

1. **SOC-AC-001:** Freeform roleplay remains available without opening a structured Action. **Blocking:** yes.
2. **SOC-AC-002:** Assisted Action and structured challenge are optional modes, not mandatory initiative for every conversation. **Blocking:** yes.
3. **SOC-AC-003:** Players can submit intent without typing full dialogue. **Blocking:** yes.
4. **SOC-AC-004:** Action definitions are registry/version/profile based and pack-extensible. **Blocking:** yes.
5. **SOC-AC-005:** The seven required alpha Actions are complete. **Blocking:** yes.
6. **SOC-AC-006:** No-roll, fixed DC, opposed, degree, extended challenge, and GM-determined methods are represented. **Blocking:** yes.
7. **SOC-AC-007:** Source DCs are examples/profiles, never universal constants. **Blocking:** yes.
8. **SOC-AC-008:** Success is limited by NPC knowledge, authority, values, boundaries, and circumstances. **Blocking:** yes.
9. **SOC-AC-009:** Persuasion is not mind control and high rolls cannot bypass impossible boundaries. **Blocking:** yes.
10. **SOC-AC-010:** Failure and partial success move play forward with explicit consequences. **Blocking:** yes.
11. **SOC-AC-011:** NPC truth, NPC belief, Player belief, lies, rumors, motives, mood, intent, and stance remain distinct. **Blocking:** yes.
12. **SOC-AC-012:** Insight returns a Player-safe interpretation, not automatic hidden truth. **Blocking:** yes.
13. **SOC-AC-013:** Intimidation compliance, fear, hostility, standing, and relationship changes are separate Effects/Events. **Blocking:** yes.
14. **SOC-AC-014:** Romantic, intimate, or coercive outcomes are never created automatically by a roll or AI. **Blocking:** yes.
15. **SOC-AC-015:** IA-D04-002 proposal/approval, decision receipt, and history contracts are reused. **Blocking:** yes.
16. **SOC-AC-016:** GM review contains all authorized visible and hidden context required for adjudication. **Blocking:** yes.
17. **SOC-AC-017:** Persistent outcomes commit as one validated Event group or not at all. **Blocking:** yes.
18. **SOC-AC-018:** Undo uses compensating Events and never deletes history or fabricates reversal of irreversible effects. **Blocking:** yes.
19. **SOC-AC-019:** Relationship, standing, clue, inventory/currency, access, Condition, NPC schedule, and combat state remain domain-owned. **Blocking:** yes.
20. **SOC-AC-020:** Hidden NPC/player information is filtered before serialization across every surface. **Blocking:** yes.
21. **SOC-AC-021:** Player-specific reveals remain scoped to the authorized Player. **Blocking:** yes.
22. **SOC-AC-022:** Lost responses use status lookup before retry and duplicate proposals/Event groups/consequences are suppressed. **Blocking:** yes.
23. **SOC-AC-023:** Combat transition preserves participants, Scene, state, and history. **Blocking:** yes.
24. **SOC-AC-024:** Pack update/removal cannot silently rewrite/delete live social state or history. **Blocking:** yes.
25. **SOC-AC-025:** Mobile, keyboard, screen-reader, touch, scaling, contrast, and reduced-motion flows preserve full alpha capability. **Blocking:** yes.
26. **SOC-AC-026:** Optional AI has no truth, reveal, decision, dialogue, consequence, transfer, transition, romance/coercion, or canonical authority. **Blocking:** yes.
27. **SOC-AC-027:** Zero-paid-service and zero-AI core operation is possible. **Blocking:** yes.
28. **SOC-AC-028:** The exact next design item is IA-D05-004 — MV-IA-F011 Investigation and Clue Board. **Blocking:** yes.

Evidence is the packet, matrix, source-coverage record, deterministic fixtures, validator, exact final-head hosted CI, and squash merge.

## 20. Fixtures and approved alpha content

- Required identities: approved Characters/Actors and NPC Definitions/Variants/live instances, including alias and hidden-truth cases.
- Required Campaign/Scene: bounded social Scene with GM, Assistant GM, Observer, at least two Players, optional combat Encounter, Location/culture/jurisdiction context.
- Required Actions/profiles: seven alpha Actions; six resolution methods; degree/outcome profiles; example DC profiles labeled nonuniversal.
- Required context: relationships, standing, statuses, leverage, favors, promises/debts, clues, items/currency, access, Conditions, NPC schedule, combat transition.
- Required hidden information: motive, fear, boundary, lie, secret, hidden modifier, hidden result, private Player knowledge, unrevealed clue/relationship/standing.
- Required history: proposal, decision, resolution, Event group, reveal, challenge, belief change, transition, compensating undo.
- Required failure fixtures: impossible request, invalid target/profile, stale domain version, duplicate operation, lost response, Event gap, revocation, entitlement restriction, ambiguous mechanic, pack incompatibility.

The 153-role/visibility records and 209-mechanic register support fixtures and provenance; they do not supply hidden motives or automatically executable Actions.

## 21. Security, privacy, cost, and risk

### Security

- Default-deny server authorization for context, participant, action, proposal, truth, modifier, reveal, consequence, history, search, export, realtime, and AI surfaces.
- Expected versions, idempotency, final revalidation, and atomic Event groups prevent partial or duplicate outcomes.

### Privacy

- Filter before serialization and redact dialogue, Player notes, motives, secrets, private knowledge, hidden modifiers, and clue truth by default in diagnostics.
- Issue reports require explicit preview/consent.

### Cost

- Core Social Mode uses provider-neutral local/open components and existing ports.
- No paid AI, speech, graph, simulation, or analytics service is required.

### Material risks

- mind-control interpretation;
- hidden truth/modifier leakage;
- partial cross-domain commit;
- direct inventory/clue/combat mutation from social UI;
- belief/truth and relationship/standing/mood/stance collapse;
- forced Player dialogue;
- automatic romance/coercion;
- Event-group undo erasing history;
- pack lifecycle rewriting live state;
- AI taking irreversible NPC control.

### Stop conditions

Stop for owner decision if a proposal widens visibility, automates romance/coercion or Player dialogue, grants AI decision/portrayal authority, requires paid services, changes canon, collects real-user voice/dialogue data, or changes release scope.

## 22. Owner review points

- Design approval required: final merge evidence records implementation-ready design; no additional decision is required for this bounded packet.
- Scope decision required: none within the source-defined alpha slice.
- Canon decision required: new Actions/profiles/statuses or synthetic fixtures remain separate and owner-gated for promotion.
- Spending/provider decision required: none; paid services remain unauthorized.
- Alpha release decision required: yes, later under existing release gates.

Silence is not approval.

## 23. Implementation handoff

**Target repository:** `cybalicistjt-stack/Multiversal-app` after P9 and dependency prerequisites  
**Registered work type:** dependency-gated feature implementation  
**Decision level:** routine within locked contracts; owner gate for scope/canon/spend/release changes  
**Risk class:** high for hidden truth, Player agency, and multi-domain atomicity  
**Suggested work-order title:** Implement MV-IA-F010 Social Interaction Mode  
**Expected branches or files:** Action/profile schemas, interaction/resolution/challenge domain services, shared proposal consumer adapter, Event-group coordinator, role-safe projections, Player/GM UI, tests/fixtures, accessibility, diagnostics  
**Required reviewers:** social-domain, proposal/approval, permission/hidden-information, persistence/recovery, cross-domain adapters, accessibility  
**Required gates:** P9 dependencies, F009/F016 contracts, deterministic validator, authorization/side-channel tests, atomicity/undo tests, two-device recovery, pack lifecycle, final CI  
**Rollback/recovery:** reversible migrations, preserved Event groups/snapshots, feature/route disable, compensating Events, no history deletion  
**Evidence outputs:** changed-path inventory, schema/profile versions, tests, fixture results, PR, exact final-head CI, squash merge

The implementation remains dependency-gated and does not resume or supersede `P9-06-008-attempt-002`.

## 24. Readiness decision

- [x] All required sections complete.
- [x] Dependencies identified.
- [x] Shared-system impacts identified.
- [x] Permissions complete.
- [x] Persistence and recovery complete.
- [x] Accessibility complete.
- [x] Tests and acceptance criteria measurable.
- [x] Explicit exclusions complete.
- [x] Owner decisions identified.
- [x] Implementation handoff complete.

**Final design status:** implementation-ready; dependency-gated  
**Reviewer:** deterministic package validator and hosted repository gate  
**Date:** 2026-08-06  
**Packet digest:** recorded by source-control merge evidence
