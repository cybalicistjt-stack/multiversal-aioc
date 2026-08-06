# MV-IA-F011 Investigation and Clue Board

**Work item:** IA-D05-004  
**Feature:** MV-IA-F011  
**Version:** 0.1.0  
**Status:** implementation-ready design; dependency-gated  
**Owner:** John Brandon Turner

## 1. Purpose

Provide a permission-safe investigation workspace where Players discover, review, connect, and discuss clues without exposing GM truth. Facts, observations, claims, hypotheses, false leads, deductions, and GM conclusions remain distinct records.

## 2. Authority principles

1. The server owns clue identity, discovery state, reveal policy, source/version evidence, and durable history.
2. A Player-visible clue is an authorized projection, not proof of objective truth.
3. Hypotheses never become facts merely because Players link clues or vote for them.
4. GM truth, hidden links, unrevealed clues, concealed sources, and private Character knowledge are filtered before query, search, export, realtime, diagnostics, or optional-AI use.
5. Realtime delivery is advisory. Durable Events and current projections control after interruption.
6. AI may organize authorized material or draft labels; it may not reveal, invent as canonical, resolve, promote, or mutate authoritative investigation state.

## 3. Core records

- **Investigation:** Campaign-scoped container with status, participants, visibility profile, active questions, and version.
- **Clue Definition:** reusable source-backed description, categories, tags, provenance, and default reveal policy.
- **Campaign Clue:** live instance with discovery status, authorized audiences, discovered-by evidence, confidence presentation, and source snapshot.
- **Observation:** what an authorized subject perceived; it may be incomplete or mistaken.
- **Claim:** attributable statement by a witness, document, sensor, or participant.
- **Evidence Item:** reference to an owning-domain Asset, Location, Character, Event, document, image, sample, or record; the clue board does not duplicate ownership.
- **Hypothesis:** Player- or GM-authored proposition with status and supporting, contradicting, or neutral links.
- **Connection:** directional typed edge between board nodes with author, visibility, rationale, and version.
- **Question:** unresolved investigative question with optional owners and status.
- **Conclusion:** GM-controlled resolution record; Player deductions remain hypotheses unless explicitly promoted by authorized GM action.

## 4. Required separations

The implementation must keep separate: objective truth; GM conclusion; clue text; observation; claim; rumor; lie; witness belief; Player belief; hypothesis; deduction; false lead; contradiction; confidence; relevance; authenticity; admissibility; and source reliability.

## 5. Investigation lifecycle

`draft`, `active`, `paused`, `resolved`, `archived`.

Clue lifecycle: `unregistered`, `registered-hidden`, `discoverable`, `discovered-private`, `discovered-shared`, `withheld`, `superseded`, `revoked`, `archived`.

Hypothesis lifecycle: `draft`, `shared`, `contested`, `supported`, `weakened`, `rejected-by-author`, `resolved-by-gm`, `archived`.

No lifecycle transition deletes durable history.

## 6. Discovery and reveal

Discovery is an attributable Event produced by an owning workflow such as social interaction, search, examination, research, exploration, combat aftermath, Asset inspection, or GM reveal. Each discovery records Campaign, Scene/Session when applicable, actor/controller, method, source and profile versions, authoritative result/Event reference, reveal audience, and idempotency key.

Reveal policies support: GM-only; specific Player; specific Character/controller; party; role; Scene participants; Campaign members; and explicit custom audience. Shared-board visibility is never implied by possession of a private clue.

## 7. Board operations

Authorized users may create or edit personal notes, create hypotheses, add typed links, group nodes, pin questions, filter, sort, search authorized projections, and propose sharing. Sharing protected clues or notes uses the shared proposal/approval contract when policy requires GM review.

Typed links include: supports, contradicts, explains, caused-by, leads-to, same-source, same-subject, temporal-before, temporal-after, located-at, owned-by, witnessed-by, derived-from, duplicate-of, and custom.

The board must support list, outline, table, and nonvisual relationship views. Spatial placement is presentation state and cannot be the only carrier of meaning.

## 8. GM workspace

The GM can register hidden clues, bind discoverability rules, inspect source evidence, preview each audience, reveal or withhold clues, correct misconfigured visibility, resolve an investigation, and record a conclusion. The GM can see Player hypotheses only when their visibility permits; private Player notes are not automatically GM-readable unless Campaign policy explicitly states otherwise and the interface discloses that policy.

## 9. Player workspace

Players see only authorized clues, their own notes, shared hypotheses, visible connections, open questions, provenance allowed by policy, and clear states for pending share, stale data, revoked access, missing history, and reconnect recovery. The interface must never label a hypothesis as confirmed fact without an authorized conclusion projection.

## 10. Events

Owned Events include `InvestigationCreated`, `InvestigationActivated`, `InvestigationPaused`, `InvestigationResolved`, `ClueRegistered`, `ClueDiscoverabilityChanged`, `ClueDiscovered`, `ClueShared`, `ClueWithheld`, `ClueSuperseded`, `ClueAccessRevoked`, `ObservationRecorded`, `ClaimRecorded`, `HypothesisCreated`, `HypothesisShared`, `HypothesisStatusChanged`, `ConnectionCreated`, `ConnectionChanged`, `ConnectionRemoved`, `QuestionCreated`, `QuestionStatusChanged`, `ConclusionRecorded`, and `InvestigationArchived`.

Cross-domain effects must be delegated to owning adapters and committed atomically where one accepted action produces several durable outcomes.

## 11. Recovery and conflicts

Every mutation uses idempotency and expected-version checks. Lost responses require status lookup before retry. Duplicate discovery cannot create duplicate clue instances or duplicate rewards. Reconnect performs Event-gap recovery followed by a fresh role-safe projection. Revocation invalidates protected caches, exports, search indexes, notifications, and optional-AI context.

Conflicts are explicit: stale board version; stale node version; concurrent connection edit; revoked audience; removed Campaign membership; missing source version; duplicate operation; and archived investigation. Silent last-write-wins is prohibited.

## 12. Pack lifecycle

Pack update does not rewrite live Campaign clues, hypotheses, notes, or conclusions. Live instances retain exact source/version snapshots. Pack removal cannot delete Campaign investigation history; unavailable source material is represented by a tombstone or retained lawful snapshot according to entitlement and retention policy.

## 13. Accessibility

All functions require keyboard, screen-reader, touch, text-scaling, reduced-motion, and noncolor status parity. Every graph edge has a textual predicate, source node, target node, author, visibility, and rationale. Focus order follows logical reading order rather than canvas coordinates. Dragging has command and form alternatives.

## 14. Deterministic acceptance fixtures

The companion matrix defines 24 fixtures covering private discovery, party reveal, hidden-link protection, conflicting hypotheses, false leads, witness claims, duplicate delivery, lost response, reconnect, revocation, pack update/removal, exports, search, diagnostics, optional AI, keyboard use, screen-reader list parity, and investigation resolution.

## 15. Implementation slices

1. `INV-S01` — registries, schemas, source/version bindings.
2. `INV-S02` — Investigation, Clue, Observation, Claim, Evidence, Question, and Conclusion stores.
3. `INV-S03` — discovery/reveal authority and shared proposal integration.
4. `INV-S04` — hypothesis and typed-connection services with version conflicts.
5. `INV-S05` — Player/GM projections, search, export, diagnostics, and privacy filters.
6. `INV-S06` — accessible list/outline/table/graph presentations.
7. `INV-S07` — Events, idempotency, reconnect, revocation, and pack lifecycle.
8. `INV-S08` — deterministic fixtures, observability, and acceptance gate.

## 16. Blocking acceptance criteria

1. GM truth is never inferred from Player-visible clue presence.
2. Unrevealed clues and hidden links cannot be enumerated through any surface.
3. Hypotheses, observations, claims, rumors, and facts remain distinct.
4. Private clue possession does not imply party sharing.
5. Sharing honors Campaign policy and approval requirements.
6. Discovery is attributable and idempotent.
7. Duplicate delivery cannot duplicate clues, rewards, or Events.
8. Lost responses require status lookup before retry.
9. Reconnect converges to ordered Events and current projections.
10. Revocation invalidates every protected derivative.
11. Search, export, diagnostics, notifications, and AI use identical authorization filters.
12. Connections are typed, attributable, versioned, and permission-safe.
13. Spatial layout is never the only meaning carrier.
14. Keyboard and nonvisual users can perform every board operation.
15. Player deductions are not auto-promoted to fact.
16. GM conclusions are attributable and durable.
17. False leads can exist without corrupting objective truth.
18. Witness claims preserve speaker and source reliability separately.
19. Evidence references owning-domain records rather than duplicating authority.
20. Cross-domain commits are atomic or compensating.
21. Pack update cannot rewrite live state.
22. Pack removal cannot erase history.
23. Archived investigations reject ordinary mutations.
24. Stale versions fail explicitly.
25. AI remains optional, authorized-context-only, draft-only, and nonauthoritative.
26. Private Player notes follow explicit disclosed Campaign policy.
27. No paid service, credential, deployment, release, or canonical promotion is implied.
28. `P9-06-008-attempt-002` remains unfinished and unmodified.

## 17. Resolved findings

- Graph layouts risk making spatial position authoritative; textual typed edges and alternate views are mandatory.
- Clues risk being treated as facts; clue, observation, claim, hypothesis, and conclusion are separated.
- Shared boards risk leaking private discoveries; reveal audience is explicit per record and derivative.
- Investigation mechanics risk duplicating Asset, Character, Location, or Event authority; evidence uses references and owning adapters.
- Undo risks erasing mystery history; corrections and revocations use new Events.
- Search/export/AI surfaces risk bypassing hidden information; one authorization projection contract governs all.
- Pack churn risks rewriting mystery state; exact snapshots and tombstones preserve live history.

## 18. Boundaries

This package is design only. Application implementation remains dependency-gated by P9 foundations and related feature contracts. It authorizes no paid service, production credential, real-user data collection, internal-alpha release, deployment, public release, AI authority, or canonical promotion.