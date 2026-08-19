# CSW-01 — Storycraft Vocabulary, Creative Object Model and Authority

**Work item:** CSW-01  
**Program:** CSW — Creator Storycraft Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

## 1. Decision

CSW introduces a **pre-authoritative creative-fragment layer** for ideas, possibilities, notes, alternates, seeds, structural thoughts and other creator material that is useful before it becomes governed game/content truth.

A Creative Fragment is never, merely by existing:

- Campaign truth;
- World or Location truth;
- an Adventure node, edge, branch or published version;
- a Character fact or advancement choice;
- a runtime clue, conclusion, relationship, reputation or faction state;
- a Scene/Session fact or Event;
- a published creator release;
- canonical content.

Creative Fragments remain pre-authoritative even when they are marked `ready`, linked to governed objects, bound to a Campaign project, generated with AI assistance, or used as source material for an explicit incorporation operation.

An owning domain gains authoritative state only through its existing or successor governed command/proposal/review/publication path. CSW may preserve a provenance link and an incorporation receipt; it does not mutate the fragment in-place into another domain's object.

This contract is additive over APW-01 universal-user/contextual authority, A10 split World/Adventure/D29 authoring provenance, A9 investigation/social runtime boundaries, A5 Campaign/Scene/Session authority, A4 Character authority, D05 visibility projection and APM-01 automation/AI boundaries.

## 2. Why a separate pre-authoritative object is necessary

A10 already owns governed authoring artifacts such as creator drafts, proposals, reviews, private releases, Campaign-local objects, World objects and Adventures. Those are intentionally closer to a target domain and carry domain/publishing semantics.

CSW must also support material that is **not yet a valid target-domain object**:

- “What if the lighthouse keeper is already dead?”
- three alternate motives for an antagonist;
- an evocative phrase;
- a possible faction conflict;
- a rumor that may or may not be true;
- a question the creator has not answered;
- a scene seed with no Adventure placement yet;
- a relationship idea that is not runtime relationship state;
- a possible twist that may be discarded later.

Forcing these into D18/D28/D29 target-domain structures prematurely would either misrepresent speculation as truth or create a monolithic storycraft persistence layer that competes with existing domain ownership. CSW-01 therefore defines a narrow pre-authoritative identity and explicit bridges into existing domains.

## 3. Canonical creative-fragment vocabulary

The normalized CSW-01 vocabulary is intentionally descriptive rather than authoritative. The `kind` answers “what creative job is this fragment doing?” It does not determine game rules, persistence ownership in a target domain, or publication status.

### Core ideation

- **idea** — general creative possibility that does not fit a narrower kind yet.
- **premise** — foundational situation, proposition or starting setup.
- **hook** — invitation, trigger or reason for engagement.
- **theme** — thematic concern, motif or recurring conceptual direction.
- **question** — creator-facing design question being explored.
- **open-question** — intentionally unresolved question that should remain visible until answered, dismissed or intentionally left open.
- **constraint** — creative limitation, requirement or boundary.
- **reference** — creator-selected reference/source/inspiration pointer, not imported truth.
- **scratch-note** — unstructured transient creative note worth retaining.

### Dramatic structure

- **conflict** — proposed tension/opposition/problem.
- **secret** — proposed concealed information; not Campaign-hidden truth until incorporated.
- **twist** — proposed reversal/reinterpretation.
- **foreshadow** — proposed setup intended to support a later reveal/payoff.
- **payoff** — proposed resolution or return on prior setup.
- **beat** — proposed narrative/gameplay beat.
- **arc** — proposed multi-beat development shape.
- **thread** — proposed or tracked creative through-line.
- **alternate** — explicit alternate version/path/possibility related to another fragment or structure.

### In-world possibility material

- **rumor** — proposed in-world statement that may be true, false, mixed or undecided; never objective truth by kind alone.
- **lore-fragment** — proposed lore text/concept not yet incorporated as World/Campaign truth.
- **character-motivation** — proposed motivation for a Character/NPC.
- **backstory-element** — proposed historical element for a Character/NPC.

### Seeds for owning domains

- **scene-seed**
- **encounter-seed**
- **mystery-seed**
- **location-seed**
- **faction-seed**
- **npc-seed**
- **world-seed**

A `*-seed` communicates that the fragment is a starting point for later explicit conversion/incorporation. It is not a partial authoritative object and does not inherit the target domain's identity.

## 4. Vocabulary rules

1. `kind` is mutable through ordinary fragment revision; changing kind does not change fragment identity by itself.
2. A fragment may have multiple semantic tags, but exactly one primary `kind` keeps search/filter behavior deterministic.
3. The vocabulary does not include authoritative object kinds such as `world`, `adventure`, `character`, `campaign`, `clue`, `relationship-state`, or `event` because those belong to owning domains.
4. “Hypothesis” is deliberately **not** a generic CSW primary kind in v0.1. A9 already owns runtime investigation hypotheses with explicit `objectiveTruth:false` and GM-authorized conclusion behavior. A creator can use `question`, `idea`, `mystery-seed`, `alternate` or `thread` for pre-runtime speculation. If a runtime A9 hypothesis is explicitly cloned into CSW for reuse, the new CSW object is a provenance-linked fragment, not the A9 hypothesis itself.
5. Future vocabulary additions must preserve the same pre-authoritative boundary and may not duplicate an owning domain merely for UI convenience.

## 5. CreativeFragment identity contract

A Creative Fragment has a stable identity independent of title, text, folder, project placement or current lifecycle.

Minimum conceptual fields:

- `fragmentId` — stable CSW identity;
- `fragmentVersion` — monotonic optimistic-concurrency version;
- `kind` — normalized primary creative kind;
- `authorityClass = pre-authoritative` — fixed semantic boundary;
- `ownerSubjectId` — resource owner under APW-01 Personal/Campaign rules;
- `authorSubjectIds` — attributable authors/contributors; authorship does not imply ownership;
- `contextBinding` — Personal or bounded Campaign creative context;
- optional `campaignId` when Campaign-bound;
- optional `projectId`/collection reference;
- optional title/label;
- `contentRef` or bounded structured payload reference;
- `lifecycleState`;
- `visibilityPolicyId`;
- `provenanceId`;
- source/inspiration references;
- fragment relationship references;
- incorporation receipt references;
- created/updated timestamps;
- tombstone metadata where applicable.

A fragment does **not** contain an `objectiveTruth:true` flag, authoritative Event sequence, Campaign runtime mutation status, canonical object ID, or target-domain version as its own authority. Target-domain references live in explicit relationship/incorporation records.

## 6. Lifecycle model

The canonical CSW-01 lifecycle is:

1. **inbox** — rapidly captured, minimally classified material awaiting triage.
2. **scratch** — intentionally rough material retained for exploration.
3. **developing** — actively being elaborated, connected or revised.
4. **ready** — creator considers the fragment suitable to use/propose/incorporate; still pre-authoritative.
5. **incorporated** — at least one explicit governed incorporation receipt exists. The fragment remains a historical/pre-authoritative source object and may continue to evolve independently.
6. **superseded** — another fragment/version has explicitly replaced this one for the creator's working purpose; references remain resolvable.
7. **archived** — intentionally removed from active work but retained and discoverable where authorized.
8. **tombstoned** — content has been deleted/withdrawn under the governed deletion policy while stable identity and minimal reference/provenance metadata remain.

### Lifecycle invariants

- `ready` never means approved/published/canonical.
- `incorporated` never means the fragment itself became authoritative.
- one fragment may be incorporated into multiple target objects/projects through separate receipts.
- incorporation never causes later fragment edits to silently propagate into targets.
- target changes never silently rewrite the source fragment.
- `superseded` does not rewrite descendants or incorporated targets.
- archive/tombstone actions cannot erase required provenance or break retained authoritative references.

## 7. Personal and Campaign-bound creative contexts

### Personal creative fragment

Default creation context. The user owns the fragment unless a separately governed collaborative ownership model applies.

Personal fragments are private by default and may be organized into creator projects/collections. A Campaign GM has no implied authority over another user's Personal fragments.

### Campaign-bound creative fragment

A fragment may be created in or explicitly bound to a Campaign creative/preparation context when the subject has appropriate Campaign authoring authority.

Campaign binding means:

- Campaign authorization/visibility governs discovery and collaboration;
- the fragment may refer to Campaign-private material;
- GM/Assistant-GM/reviewer authority may apply only according to explicit Campaign/delegation policy;
- it is still **pre-authoritative preparation material**;
- it does not become a Scene fact, clue, NPC fact, World truth, relationship state, Adventure node or Session Event simply because it is Campaign-bound.

Campaign removal/revocation may remove future access to Campaign-bound fragments. It must not silently transfer or destroy unrelated Personal creative property.

## 8. Authority dimensions

CSW distinguishes independent authority decisions:

- **own** — resource ownership where applicable;
- **author/contribute** — attributable content contribution;
- **view** — discover/read authorized projection;
- **edit** — revise content/kind/metadata;
- **link** — create/remove non-authoritative semantic references where allowed;
- **branch/clone** — create an independent derived fragment with provenance;
- **share** — change approved visibility/collaboration scope;
- **bind-to-campaign** — create an explicit Campaign creative binding;
- **propose/incorporate** — request creation/change in an owning domain through its governed path;
- **archive**;
- **tombstone/delete-content**;
- **restore** where policy permits;
- **export**.

These do not silently imply D29 `review`, `publish`, `install`, `enable`, `reveal`, `runtime-advance`, `canonical-promotion`, or any target-domain mutation authority.

Ownership does not imply publish. Authorship does not imply ownership. Edit does not imply incorporation. Campaign GM authority does not imply Personal ownership. Creator status does not imply canonical promotion.

## 9. Fragment relationships

CSW-01 defines relationship semantics that remain non-authoritative unless an owning domain explicitly consumes them:

- `related-to`
- `inspired-by`
- `derived-from`
- `branch-of`
- `alternate-of`
- `supports`
- `contrasts-with`
- `foreshadows`
- `pays-off`
- `supersedes`
- `references`
- `used-in` (projection/backlink derived from explicit target reference or incorporation receipt)

References use stable IDs and, when reproducibility matters, a source fragment version. Labels/text are never identity.

A CSW relationship saying one fragment “supports” another is a creative relationship, not an A9 evidence connection and not objective truth.

## 10. Incorporation model

**Incorporation is a governed bridge, never an in-place type conversion.**

A creator selects a fragment/version and requests a target-domain operation. The owning domain decides whether the operation is allowed, valid, reviewable, publishable or rejectable. On success CSW records an `IncorporationReceipt` linking the immutable source fragment version to the resulting target/proposal/draft identity.

Conceptual receipt fields:

- `incorporationId`;
- source `fragmentId` and `fragmentVersion`;
- target domain/key and target intent;
- target operation/proposal ID;
- resulting target object/version ID when created;
- actor subject;
- Campaign/context scope where applicable;
- decision/publication receipt references where applicable;
- provenance ID;
- timestamp;
- status (`proposed`, `accepted`, `rejected`, `withdrawn`, `superseded`).

The receipt is evidence of a bridge. It is not permission to mutate either side later.

## 11. Owning-domain incorporation boundaries

### D18 World / Location / semantic geography

A `world-seed`, `location-seed`, `lore-fragment`, `rumor`, `idea` or other fragment may seed a D18/D29 draft/proposal. D18 owns World/Location/geography truth and versioning. D29 owns authoring proposal/review/publication provenance. CSW cannot write D18 persistence directly.

### D28 Adventure / Module

Hooks, beats, arcs, twists, secrets, scene seeds, encounter seeds and similar fragments may seed D28/D29 Adventure drafts/proposals. D28 owns Adventure definitions, immutable published versions, module graph and Campaign run-local progression. CSW cannot mark an Adventure branch complete or mutate run state.

### Character domain

Motivations/backstory elements/NPC seeds may be proposed or copied into a Character/NPC-authoring workflow. The Character/creature owning domain decides whether the result is a draft, Campaign-local fact, approved advancement or other governed state. A CSW fragment is never a Character fact solely because it is linked to a Character.

### Campaign / Scene / Session

Fragments may seed Campaign preparation or Scene content through an authorized A5/D29 path. Campaign binding alone is insufficient. Session/runtime truth still requires the owning Campaign/Scene/Session/Event command path.

### Investigation

CSW mystery seeds/questions/secrets/clue ideas are authoring material. A9 runtime investigation hypotheses and conclusions remain A9 objects. A9 already proves the desired invariant: hypothesis support never auto-promotes to objective fact, and resolution requires an authorized conclusion/Event. CSW must not bypass that boundary.

A runtime A9 hypothesis/clue may be explicitly cloned/proposed into CSW for reuse; this creates a new fragment with provenance and appropriate visibility filtering. It does not move or rewrite runtime history.

### Relationship / social / faction

Creative relationship ideas, faction seeds, motivations and conflicts may seed owning-domain definitions or Campaign-runtime proposals. A9 social/reputation/faction state remains runtime authority; CSW links do not directly change affinity, reputation, faction membership, standing, disposition or other live state.

### Encounter / rules / Items / Vehicles / other domains

`encounter-seed` or general ideas may feed the corresponding owning authoring/lab flow. A10/D29 creator content already supports several mechanical content types. CSW may supply source material/provenance but cannot become the mechanics, Asset/economy or rules authority.

### Canonical content

There is **no direct CSW → canonical** operation. A fragment may feed a governed creator draft/proposal/release. Canonical promotion remains a separate explicit owner-only authority under existing governance.

## 12. Relationship to A10 D29 authoring-provenance

CSW-01 does not replace A10 D29.

Existing D29 already owns:

- creator target-domain drafts;
- authoring proposals;
- review decisions;
- publication receipts;
- Campaign-local creator objects;
- import mappings;
- operation status/recovery;
- source-migration decisions;
- authoring authority dimensions.

CSW's pre-authoritative fragment seam sits **before** those target-domain workflows. A later CSW implementation handoff should prefer one of two additive destinations:

1. a bounded D29 `creative-fragment` extension if D29 can own the generic pre-authoritative authoring provenance cleanly; or
2. a new narrowly bounded creative-support persistence seam only if CSW-10 demonstrates D29 cannot own it without violating domain cohesion.

CSW-01 does not decide or authorize that migration now. It explicitly forbids parallel writes into D18/D28/A9/A4/A5 storage.

## 13. Deletion, tombstones and reference integrity

### Soft-delete default

If a fragment has inbound fragment links, derived children, incorporation receipts, publication provenance or another retained evidentiary reference, hard deletion is not allowed as the normal operation. Content may be withdrawn/redacted according to policy, but the stable ID becomes a tombstone containing only authorized minimal metadata needed to preserve graph integrity and provenance.

### Tombstone minimum

- stable `fragmentId`;
- last known version;
- lifecycle `tombstoned`;
- owner/authority-safe deletion actor reference where permitted;
- deleted/tombstoned timestamp;
- reason category;
- replacement/superseding fragment reference if applicable;
- retained incorporation/reference IDs;
- provenance/tombstone ID;
- user-safe remediation text or status.

Tombstones must remain visibility-filtered. The existence of a deleted private fragment must not leak through counts, graph topology or search.

### Reference behavior

- dangling references render a bounded unavailable/tombstoned state, never silently retarget by title similarity;
- source deletion never deletes downstream governed targets;
- downstream target deletion never deletes the originating fragment;
- source version changes do not automatically update incorporation receipts;
- derived fragments preserve `derived-from`/`branch-of` provenance even when source content becomes unavailable to the current viewer.

## 14. Versioning and branching

Ordinary edits increment `fragmentVersion` and preserve creator history according to retention policy.

A **branch** creates a new `fragmentId` with `branch-of` provenance. Use branching when the creator wants independent alternatives that can evolve separately.

An **alternate** may be represented either by `kind=alternate` or an `alternate-of` relationship when a full independent fragment is appropriate. No branch or alternate silently replaces its source.

An incorporation receipt always pins the source fragment version used at the time of incorporation. Later edits can trigger an advisory “source has changed” projection, but never automatic target mutation.

## 15. Optional AI and deterministic assistance

Core fragment capture, classification, tagging, linking, templates, prompts, random tables, deterministic generators and organization must remain useful without an external AI provider.

When optional AI is used:

- context is filtered before prompt construction;
- the user sees/controls the relevant source scope under existing AI governance;
- generated alternatives are presented as proposals/drafts;
- accepted generated material becomes a new fragment/version/branch with AI provenance;
- source material is not overwritten silently;
- AI cannot incorporate, publish, reveal, canonical-promote or mutate Campaign/runtime state;
- AI-generated claims are never upgraded to `authoritative` because they are fluent or repeated;
- provider failure falls back to manual/deterministic workflows where supported.

APM-01 also applies: an automation controller or AutoGM cannot silently turn CSW material into authoritative story truth merely because an automated scenario consumes it.

## 16. Privacy and projection

D05/APW authorization applies before:

- search;
- counts/facets;
- autocomplete;
- graph topology/backlinks;
- Story Bible projections;
- “related/unused/forgotten material” suggestions;
- notifications;
- export;
- diagnostics;
- optional-AI/automation context.

Private Personal fragments, Campaign-bound secret preparation and deleted/tombstoned material must not leak through labels, counts, relation cardinality, similarity suggestions, embeddings, graph edges or AI context.

## 17. Minimum acceptance scenarios

1. User captures an `idea` in Personal context → it is private/pre-authoritative and usable with zero Campaigns.
2. User marks it `ready` → no World/Campaign/Adventure truth changes.
3. User branches two antagonist motives → two stable fragments preserve source provenance; neither is selected as fact automatically.
4. GM creates a Campaign-bound `secret` → it remains Campaign preparation, not Player-visible truth, until an owning-domain reveal/incorporation path says otherwise.
5. Creator incorporates a `location-seed` into a D18/D29 proposal → source version is pinned; D18/D29 owns target review/publication; later fragment edits do not change the target.
6. Player A9 hypothesis is supported by evidence → it remains `objectiveTruth:false`; CSW does not auto-convert it into lore fact.
7. A runtime hypothesis is cloned for future creator reuse → new CSW fragment has distinct ID and provenance; runtime A9 record remains unchanged.
8. Creator deletes a fragment referenced by an incorporated Adventure → target Adventure remains; source becomes a permission-safe tombstone/provenance reference.
9. AI suggests three twists → suggestions remain unaccepted proposals; accepted one becomes an attributable fragment/branch, not Campaign truth.
10. User lacks access to another creator's private fragment → search/counts/graph/AI reveal neither content nor existence.
11. Campaign GM tries to edit another user's Personal fragment through GM authority → deny.
12. Creator can export owned authorized fragments → export contains provenance/visibility-safe material only and grants no target-domain or canonical authority.

## 18. Additive implementation touch points

CSW-01 does not authorize implementation. It identifies successor design destinations:

1. D29/public contracts: optional bounded CreativeFragment identity/version/provenance extension if CSW-10 confirms ownership fit.
2. APW Personal Workspace/Creator Workshop: fragment creation/discovery/ownership/context projection.
3. D05: fragment/relationship/backlink/search/AI safe projections.
4. D18/D28/D29: incorporation/proposal receipts and pinned-source references.
5. A4/Character and NPC owning domains: explicit backstory/motivation/NPC-seed incorporation seam.
6. A5 Campaign/Scene: Campaign-bound creative-preparation references and incorporation without runtime truth bleed.
7. A9 investigation/social/faction: clone/propose boundaries and explicit non-equivalence between creative links and runtime state.
8. A10 creator content: source-fragment provenance on creator definitions/releases/Campaign-local objects.
9. CSW-02: Story Bible/library/backlink/history projections consume these stable fragment IDs and relationships.
10. AI/APM: suggestion/provenance boundaries, never direct incorporation authority.
11. Recovery/export: optimistic versions, tombstones, operation status and long-term project-memory integrity.

## 19. Nonauthorization

CSW-01 does not authorize:

- application implementation or migration;
- a new database/domain root;
- direct writes to D18/D28/D29/A9/A4/A5 persistence;
- autonomous AI authorship/publication;
- public creator marketplace/community publication;
- canonical promotion;
- paid AI/provider use;
- production credentials;
- release, deployment or tester access;
- training on private user creative material;
- CCTI-12-T04 resumption before September 2026.

## 20. Completion gate

CSW-01 is substantively complete when:

- normalized vocabulary is explicit and does not duplicate authoritative object types;
- stable pre-authoritative CreativeFragment identity/version/provenance is defined;
- lifecycle and tombstone/reference rules are deterministic;
- Personal versus Campaign-bound creative context is explicit;
- authority dimensions are separated;
- idea/possibility/rumor/seed/creative link cannot masquerade as fact/runtime state;
- incorporation is an explicit pinned-version bridge governed by the target domain;
- A10 D18/D28/D29 and A9 boundaries remain intact;
- optional AI/automation remains nonauthoritative;
- implementation touch points are additive and do not reopen completed Stage A work.

Final `completed_verified` requires governed AIOC repository-health/PR evidence recorded in the checkpoint and review receipt.
