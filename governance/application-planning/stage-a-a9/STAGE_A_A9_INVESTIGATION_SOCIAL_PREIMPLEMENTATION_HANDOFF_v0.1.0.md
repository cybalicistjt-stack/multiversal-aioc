# STAGE-A-A9 Investigation and Social Workspaces — Preimplementation Handoff v0.1.0

**Status:** PREIMPLEMENTATION COMPLETE — A9 NOT ACTIVATED  
**Application baseline:** `cybalicistjt-stack/Multiversal-app` main `dced7f92163050690c807c1fda937146bb8dce85`  
**Current application sequence:** A2 remains current; A3–A9 are not activated  
**Owner/final authority:** John Brandon Turner

## Prepared package

`STAGE_A_A9_INVESTIGATION_SOCIAL_PREIMPLEMENTATION_v0.1.0.zip`

SHA-256: `95d11bc619bbe48d7ede9565c0c5f8abbb9ccdd9e4386959bbc01cbf6a0e2e11`

Validator result:

`STAGE-A-A9 INVESTIGATION/SOCIAL PREIMPLEMENTATION v0.1.0: PASS`

Validated totals:

- six preserved completed source families: `REL`, `FRO`, `SOC`, `INV`, `GLA`, `NCI`;
- 144 deterministic fixtures total;
- 48 source implementation slices total;
- 168 blocking source acceptance criteria total;
- 21 explicit concept-separation rules;
- 20 additional A9 packaging gates;
- zero blocking findings across the six governing source packages.

## Canonical Stage A9 scope

Stage A9 is **Investigation and Social Workspaces**.

Investigation covers clues, evidence, witnesses, documents, discoveries, hypotheses, false leads, hidden/known states, relationships, notes, and non-linear progress.

Social covers NPC attitudes, relationships, faction standing, influence, reputation, promises, debts, social conditions, and GM-only information.

Exit condition: **structured non-combat scenes produce persistent consequences without exposing hidden information.**

## Governing completed source families

1. **MV-IA-F009 — Relationship Tracker** (`REL-S01`–`REL-S08`)
   - fourteen relationship dimensions;
   - seven independently authorized reveal layers;
   - directional Campaign-scoped edges;
   - Bonds, leverage, favors, promises, debts, oaths, obligations;
   - 24 deterministic fixtures and 28 blocking `REL-AC` criteria.

2. **MV-IA-F016 — Factions, Reputation, and Organizations** (`FRO-S01`–`FRO-S08`)
   - sixteen contract families;
   - nine membership statuses;
   - nine visibility layers;
   - standing, influence, membership, rank/office, agendas, operations, alert, services and external-domain references;
   - seven governed source faction profiles and 956 source canonical progression records that create no automatic authority grants;
   - 24 deterministic fixtures and 28 blocking `FRO-AC` criteria.

3. **MV-IA-F010 — Social Interaction Mode** (`SOC-S01`–`SOC-S08`)
   - freeform, assisted and structured-challenge modes;
   - fourteen Action categories, 49 source Action forms and seven required alpha Actions;
   - six resolution methods and seven degree outcomes;
   - eighteen shared Effect processors and 29 possible cross-domain outcome Event drafts;
   - shared GM proposal/review/modify/decision authority and atomic persistent outcomes;
   - 24 deterministic fixtures and 28 blocking `SOC-AC` criteria.

4. **MV-IA-F011 — Investigation and Clue Board** (`INV-S01`–`INV-S08`)
   - ten core record types and fifteen typed connection forms;
   - server-authoritative discovery/reveal;
   - strict truth/claim/observation/hypothesis/conclusion separation;
   - durable correction/revocation rather than history deletion;
   - 24 deterministic fixtures and 28 blocking numbered source criteria.

5. **IA-D05-005 — Graph/List Accessibility** (`GLA-S01`–`GLA-S08`)
   - one semantic node/edge projection;
   - six equivalent views: list, outline, table, graph, detail and nonvisual navigator;
   - complete keyboard, screen-reader, touch, text-scaling, high-contrast, reduced-motion, virtualization, hidden-topology and reconnect parity;
   - 24 deterministic fixtures and 28 blocking numbered source criteria.

6. **IA-D05-006 — Noncombat Integration Review** (`NCI-S01`–`NCI-S08`)
   - five preserved domain authorities: relationship, faction, social, investigation and semantic projection;
   - eight integrated noncombat journeys;
   - eleven explicit cross-domain adapters;
   - atomic domain outcomes, recovery, provenance and optional-AI boundaries;
   - 24 deterministic fixtures and 28 blocking `NCI-AC` criteria.

## Frozen authority and concept-separation rules

- Relationship, faction standing/reputation, influence, membership, rank/office, mood, intent, stance, belief, clue, hypothesis, conclusion, permission, ownership and control are not one state.
- Relationship edges are directional unless explicitly paired.
- Titles, occupations, species, progression or role labels do not synthesize faction membership or faction identity.
- Social interaction is roleplay-first. Freeform interaction may remain unstructured.
- Persuasion is not mind control; deception cannot rewrite objective truth; insight does not automatically disclose exact hidden motive.
- Persistent social outcomes are delegated to their owning domains and commit as one accepted Event group or none.
- A Player-visible clue is not proof of objective truth.
- Player hypotheses never become facts merely through links, support, votes or confidence.
- GM conclusions are attributable durable records rather than silent truth rewrites.
- Investigation evidence references owning-domain Asset, Character, Location, Event, document, image, sample or record authority rather than duplicating it.
- Graph geometry, coordinates, grouping, zoom and routing are presentation state only.
- Hidden nodes, edges, counterpart identities, faction operations, clues, topology and related aggregate counts are filtered before layout, search, traversal, counts, export, diagnostics, notifications or optional-AI context.
- Realtime remains advisory; durable Events and current server projections control after interruption.
- Lost responses use original operation status lookup before retry; stale versions fail explicitly.
- Revocation invalidates protected caches and derivative surfaces on every device.
- Pack update/removal preserves live state, exact source snapshots, tombstones and durable history.

## A9 / A10 boundary

F016 is mapped to A9/A10. A9 may implement persistent Campaign faction membership/standing/influence and noncombat runtime interactions required by structured play.

Reusable general Faction/World/Location authoring remains **A10 / MV-IA-F015** work and must not be pulled forward into A9 implementation.

## Explicit nonauthorization

This preparation does **not**:

- activate A9;
- create an A9 application branch;
- modify the application repository;
- supersede A2 as current work;
- implement A3–A8;
- authorize AI NPC truth, social decision, hidden reveal or investigation-resolution authority;
- authorize automatic romance/coercion or mind-control behavior;
- authorize canonical promotion;
- authorize real-user dialogue/voice collection;
- authorize paid services, production credentials, internal-alpha release, deployment, production or public release.

## Exact next preparation step

Build the **A9 repository-compatibility + implementation-contract package** against the current application repository.

Map all 48 source slices onto the canonical repository domain boundaries and existing P9 foundations, with special attention to:

- `social-relations` and `investigation` canonical domain roots;
- faction runtime ownership versus future A10/F015 authoring;
- permission/hidden-information filtering before graph/search/count/AI derivatives;
- A6 shared proposal/approval and atomic Event-group integration;
- A8 Asset/economy transfers and A7 combat-transition adapters;
- relationship/faction/social/investigation persistence and additive migration boundaries;
- semantic graph/list shared contracts and accessibility;
- status lookup, Event-gap recovery, revocation and pack lifecycle;
- exact changed-path and CI plan.

Do not activate A9 as part of that audit.
