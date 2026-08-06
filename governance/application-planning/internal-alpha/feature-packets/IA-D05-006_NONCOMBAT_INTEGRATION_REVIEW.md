# IA-D05-006 — Noncombat Integration Review

**Program:** MV-IA-001  
**Owner:** John Brandon Turner  
**Status:** implementation-ready design integration  
**Scope:** MV-IA-F009, MV-IA-F016, MV-IA-F010, MV-IA-F011, and IA-D05-005

## 1. Purpose

This review proves that Relationship, Faction/Reputation/Organization, Social Interaction, Investigation/Clue Board, and graph/list accessibility contracts form one coherent noncombat runtime without merging distinct domain authority or exposing hidden information.

## 2. Governing authority model

Each domain owns its durable records and validates its own mutations. A noncombat coordinator may assemble one atomic outcome group, but it cannot overwrite domain authority.

- Relationship owns directional dimensions, bonds, promises, favors, debts, leverage, and relationship history.
- Faction owns membership, rank, office, standing, influence, agendas, operations, and services.
- Social owns interaction context, proposals, decisions, challenge progress, NPC stance, mood, and response scheduling.
- Investigation owns clues, observations, claims, evidence, hypotheses, connections, questions, conclusions, and discovery history.
- Shared graph/list accessibility owns no gameplay truth; it renders authorized semantic projections only.

## 3. Required concept separations

The integrated runtime must keep separate:

- objective truth, GM conclusion, clue, observation, claim, rumor, lie, Player belief, hypothesis, deduction, and false lead;
- relationship, temporary stance, mood, intent, faction standing, faction influence, membership, rank, and office;
- discovery, reveal, sharing, inference, acceptance, and durable conclusion;
- source Definition, Campaign-local instance, live state, Event, projection, and presentation layout;
- authority, permission, visibility, ownership, custody, control, and participation.

No score, graph position, social result, or Player deduction may collapse those distinctions.

## 4. Integrated journey

1. A Player inspects an authorized Relationship, Faction, Social, or Investigation surface.
2. Server-side projection filters hidden nodes, edges, counts, labels, search results, notifications, exports, diagnostics, and optional-AI context before rendering.
3. The Player may propose a Social Action, create a private hypothesis, connect visible clues, share an authorized discovery, or inspect relationship/faction context.
4. The owning domain validates identity, role, Campaign, Scene, target, source version, expected version, visibility, and entitlement.
5. GM-only modifiers, truths, motives, hidden links, unrevealed clues, faction operations, and private knowledge remain absent from unauthorized payloads.
6. A shared proposal/approval decision may authorize one atomic outcome group.
7. Domain adapters commit their own Events or reject the entire coordinated mutation; partial cross-domain success is prohibited.
8. Role-safe projections refresh through ordered Event recovery and status lookup.
9. History preserves original proposal, decision, source versions, accepted effects, denied effects, and compensating undo.

## 5. Cross-domain outcome rules

A single accepted Social or Investigation outcome may draft changes for multiple domains, including relationship dimension change, temporary stance, standing, influence, clue reveal, rumor creation, access grant, favor/debt/promise creation, or NPC scheduling. The coordinator must:

- validate every draft against the current owning-domain version;
- commit all accepted drafts in one atomic group or none;
- retain per-domain Event identity and provenance;
- produce one group receipt linking every committed Event;
- expose only role-authorized receipt fields;
- use compensating Events for undo and never delete durable history.

## 6. Relationship and faction integration

Relationship and faction state may influence Social or Investigation resolution only through explicit versioned modifiers. Standing does not imply membership, rank, office, ownership, equipment, permission, personal trust, affection, fear, or obligation. Relationship dimensions do not automatically change faction standing. Any conversion requires a declared rule/profile and attributable Event.

## 7. Social and investigation integration

Social Actions may reveal clues, create claims or rumors, schedule follow-up witnesses, or change access. Investigation may provide authorized evidence or leverage to Social Actions. Neither domain may:

- treat Persuasion as mind control;
- treat Insight as exact truth revelation;
- convert a hypothesis into fact because of a successful roll;
- reveal hidden clues or links through counts, graph shape, search, export, diagnostics, or AI context;
- let Player-authored text mutate NPC truth, objective truth, faction authority, or canonical content.

## 8. Accessibility integration

All integrated operations must be available through equivalent list, outline, table, detail, graph, and nonvisual navigation paths where applicable. Geometry, color, line shape, animation, hover, drag, or precision pointer movement cannot be the only carrier of meaning or the only way to act.

Keyboard, screen-reader, touch, text scaling, high-contrast, reduced-motion, focus restoration, and mobile layouts must preserve identical authorization and mutation semantics.

## 9. Recovery and concurrency

Every mutation uses idempotency keys and expected versions. Lost responses require status lookup before retry. Reconnect restores current role-safe projections and ordered Event gaps. Revocation invalidates cached protected records, graph topology, counts, search results, exports, and optional-AI context. Offline authoritative mutation is prohibited; bounded private drafts may resume only after revalidation.

## 10. Pack and provenance lifecycle

Pack updates cannot rewrite live Campaign state. Durable records retain exact source identifiers, source versions, snapshots, and provenance. Pack removal leaves tombstones sufficient to preserve history, labels, receipts, and relationships without granting continued executable access.

## 11. Optional AI boundary

AI may summarize or propose only from already authorized projections. It has no authority to reveal hidden information, resolve Social Actions, establish truth, accept hypotheses, create faction membership, change relationships, commit Events, or promote canonical content. AI output remains labeled, attributable, dismissible, and nonauthoritative.

## 12. Implementation slices

1. Shared semantic identifiers and projection envelopes.
2. Cross-domain authority and adapter interfaces.
3. Relationship/faction modifier bindings.
4. Social/investigation proposal and outcome coordination.
5. Role-safe graph/list/search/export/diagnostic projections.
6. Recovery, revocation, idempotency, and Event-gap handling.
7. Pack lifecycle, provenance, tombstones, and compensating undo.
8. Deterministic integration fixtures and acceptance harness.

## 13. Blocking acceptance criteria

1. Domain ownership is explicit and non-overlapping.
2. Objective truth is never derived from Player belief or hypothesis.
3. Relationship, stance, mood, standing, influence, membership, rank, and office remain separate.
4. Hidden nodes and edges are removed before counts or layout.
5. Search cannot enumerate hidden topology.
6. Export and diagnostics use the same role-safe projection rules.
7. Optional AI receives no broader context than the requesting role.
8. Graph geometry is never authoritative.
9. List and nonvisual paths provide full operation parity.
10. Social success cannot bypass impossible boundaries.
11. Insight cannot disclose exact hidden truth automatically.
12. Investigation success cannot convert hypothesis into fact automatically.
13. Cross-domain effects commit atomically or not at all.
14. Every committed effect has owning-domain provenance.
15. Duplicate submit cannot duplicate effects.
16. Lost response uses status lookup before retry.
17. Stale versions are rejected with recoverable current state.
18. Revocation removes cached protected information.
19. Offline drafts cannot become authoritative without revalidation.
20. Compensating undo preserves history.
21. Pack update cannot rewrite live state.
22. Pack removal cannot delete durable history.
23. Standing does not grant membership or permission.
24. Relationship does not grant ownership or control.
25. Player text cannot mutate NPC or objective truth.
26. AI cannot decide, reveal, commit, or promote.
27. All fixtures preserve `P9-06-008-attempt-002` as unfinished parallel work.
28. Zero unresolved blocking findings remain.

## 14. Resolved findings

- **NCI-FND-001:** Similar social concepts risked collapsing into one attitude value. Resolved by explicit domain records and versioned adapters.
- **NCI-FND-002:** Graph topology could leak hidden records. Resolved by filtering before search, counts, traversal, layout, export, diagnostics, and AI context.
- **NCI-FND-003:** Social outcomes could partially mutate several domains. Resolved by one atomic outcome group with owning-domain commits.
- **NCI-FND-004:** Investigation hypotheses could be mistaken for truth. Resolved by separate record types and explicit promotion authority.
- **NCI-FND-005:** Standing and relationship could accidentally grant authority. Resolved by separating social state from membership, role, ownership, and permission.
- **NCI-FND-006:** Accessibility alternatives could become read-only. Resolved by full semantic operation parity across views.
- **NCI-FND-007:** AI assistance could gain hidden or final authority. Resolved by role-filtered, draft-only, nonauthoritative boundaries.

## 15. Result

The IA-D05 tranche is coherent at design level. Relationship, faction, social, investigation, and accessible graph/list contracts can share identifiers, projections, proposal/approval, Event recovery, and outcome coordination without merging authority or weakening hidden-information rules.

## 16. Boundaries

Design only. Application implementation remains dependency-gated by P9 foundations. `P9-06-008-attempt-002` remains unfinished and unmodified. No paid service, production credential, real-user data collection, internal-alpha release, deployment, public release, AI authority, or canonical promotion is authorized.

## 17. Next work item

IA-D06-001 — MV-IA-F007 Full Combat Interface.
