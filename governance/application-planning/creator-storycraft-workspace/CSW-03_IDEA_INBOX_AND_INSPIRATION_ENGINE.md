# CSW-03 — Idea Inbox and Inspiration Engine

**Work item:** CSW-03  
**Program:** CSW — Creator Storycraft Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

## 1. Decision

CSW-03 defines a **near-zero-friction Idea Inbox** and a **bounded Inspiration Engine** that turn a fleeting thought into durable, attributable, pre-authoritative Creative Fragments without forcing the creator to decide structure, canon, project placement, genre, or final meaning at capture time.

The core contract is:

> **Capture first; structure later; generate candidates, never truth; preserve the seed; make every accepted development attributable and reversible.**

The Idea Inbox uses CSW-01 Creative Fragment identity/lifecycle and CSW-02 Creative Library/Project Memory. It does not create a second creative-object type or truth store.

The Inspiration Engine must remain useful with no external AI provider. Its deterministic tools—prompt matrices, combinators, constraint flips, contrast/connection operators, seeded tables, question ladders, variation transforms, structure lenses, and source-safe remix prompts—are first-class capability. Optional AI may enrich those tools with suggestions, but every AI output remains a candidate until the user explicitly saves, applies, branches, or incorporates it through governed paths.

## 2. Product outcome

A creator should be able to:

- capture “lighthouse that only appears during storms” in seconds;
- close the app and find it later;
- leave it completely unclassified if desired;
- triage it later into `location-seed`, `mystery-seed`, `hook`, `secret`, or another CSW-01 kind;
- attach it to a Creator Project without changing authority;
- ask deterministic inspiration tools for useful directions;
- optionally ask AI for alternatives using only authorized context;
- save one or several alternatives as branches/derived fragments without overwriting the seed;
- discover that a related older idea already exists;
- explicitly relate, branch, supersede, or dismiss the duplicate suggestion;
- preserve provenance to references and generator inputs;
- keep every generated possibility visibly distinct from governed World/Adventure/Campaign truth.

## 3. Capture-first model

### 3.1 Minimum capture

The minimum durable capture requires only:

- creator subject identity;
- Personal or currently authorized Campaign creative context;
- content text or supported minimal payload;
- capture timestamp;
- stable `fragmentId`/operation identity assigned by the durable save path;
- visibility policy from the selected context/default;
- provenance identifying the capture source/channel.

Everything else may be deferred.

Default lifecycle after durable quick capture is `inbox`.

Default kind may be:

- explicitly selected by the creator; or
- omitted/unclassified in the capture UI and normalized to `idea` only as a presentation-compatible fallback if the future schema requires one primary kind.

The system must not force title, project, tags, genre, World, Adventure, Character, Campaign, hook type, plot role, or canonical status before the creator can save the thought.

### 3.2 Capture channels

Future implementation may support equivalent capture through:

- full desktop/web composer;
- compact quick-add control;
- mobile quick capture;
- keyboard-first command/shortcut;
- share/import handoff from text the user explicitly sends into Multiversal;
- offline local draft capture under existing recovery rules;
- optional voice transcription only when separately authorized by platform/privacy policy.

All channels produce the same governed Creative Fragment boundary after durable save. A faster capture surface cannot weaken ownership, visibility, provenance, or context rules.

### 3.3 Capture is not triage

Saving an Inbox item does not imply:

- that the idea is good;
- that it belongs in a project;
- that it is unique;
- that it is fact;
- that it should be developed;
- that it should be incorporated;
- that a suggested classification is correct.

The creator may leave Inbox material untouched indefinitely, subject only to ordinary retention policy.

## 4. Inbox triage

Triage is optional organization, not a gate to using the system.

For one or more Inbox items, the creator may:

- edit content;
- choose/change primary CSW-01 kind;
- add tags;
- add to one or more authorized Creator Projects/collections;
- mark `scratch` or `developing`;
- leave as `inbox`;
- archive;
- tombstone/delete under CSW-01 integrity rules;
- relate to another fragment;
- branch/clone;
- mark as an alternate;
- attach authorized references/inspiration sources;
- open Inspiration tools;
- inspect possible related/duplicate material;
- explicitly incorporate later through an owning-domain bridge.

Triage never changes `authorityClass=pre-authoritative`.

### 4.1 Suggested triage

Deterministic rules or optional AI may suggest:

- fragment kind;
- tags;
- project/collection placement;
- related fragments;
- possible next development question.

Suggestions are never applied silently. Batch suggestions require an explicit review/apply interaction and retain attribution to the suggestion mechanism where meaningful.

## 5. Inspiration Engine principles

The Inspiration Engine exists to **increase useful possibility density without drowning the creator in noise**.

It follows these rules:

1. **Seed-preserving** — the source fragment/version remains unchanged unless the user explicitly edits it.
2. **Candidate-producing** — generators return candidate ideas, questions, structures, constraints or alternatives, not authoritative content.
3. **Bounded** — each request returns a small declared number of candidates; recursive “generate more” is explicit.
4. **Explainable** — deterministic tools can expose the transformation/prompt basis; optional AI retains request/provenance metadata.
5. **Genre-flexible** — tools operate on storycraft functions rather than assuming fantasy, sci-fi, horror, romance, farming, combat, etc.
6. **Context-safe** — only authorized visible inputs may influence output.
7. **Creator-controlled** — discard, save, branch, combine, rewrite or ignore are always available.
8. **No silent overwrite** — applying a development creates an edit only after explicit confirmation; alternatives usually become branches/derived fragments.
9. **No authority escalation** — repetition, confidence, ranking or AI fluency cannot turn a possibility into fact.
10. **No engagement spam** — the engine does not manufacture endless tasks, streaks or urgency merely to keep the user generating.

## 6. Deterministic inspiration primitives

The following primitives are first-class and should work without AI.

### 6.1 Question ladder

Given a fragment, surface a bounded set of creator questions such as:

- What is the most interesting consequence?
- Who wants this and why?
- Who is harmed or threatened by it?
- What makes this difficult, costly, secret or unstable?
- What changes if the obvious assumption is false?
- What does the audience/player believe at first?
- What would make this matter later?
- What evidence/setup would support a payoff?

Question sets are tagged by creative function rather than genre.

### 6.2 Constraint flip

Take one explicit/implicit property and propose bounded transforms:

- invert it;
- remove it;
- exaggerate it;
- make it scarce;
- make it common;
- make it conditional;
- change who controls it;
- move the cost elsewhere;
- make the apparent benefit the source of a problem.

The tool outputs transformed candidates, not edits.

### 6.3 Contrast pair

Combine the seed with an intentionally contrasting dimension:

- safe / dangerous;
- public / secret;
- ancient / new;
- intimate / enormous;
- mundane / impossible;
- desired / feared;
- controlled / unstable;
- sincere / deceptive;
- temporary / permanent.

The axes are authoring prompts, not game mechanics.

### 6.4 Connection bridge

Given two authorized fragments, propose ways they might be related:

- causal;
- thematic;
- shared origin;
- mutual consequence;
- opposition;
- dependency;
- false connection;
- foreshadow/payoff;
- same actor/organization/location;
- temporal sequence.

The result is a relation candidate. The user must explicitly record a CSW relationship.

### 6.5 Role lens

View a seed as a possible:

- hook;
- conflict;
- secret;
- twist;
- foreshadow;
- payoff;
- beat;
- scene seed;
- encounter seed;
- mystery seed;
- location/NPC/faction/world seed;
- motivation/backstory element.

This helps reframe one idea without changing the source kind automatically.

### 6.6 Stakes/consequence ladder

Generate bounded consequences at different scales:

- immediate personal;
- relationship/social;
- local/community;
- organizational/faction;
- setting/world;
- long-term thematic.

No consequence is authoritative until incorporated into an owning-domain design.

### 6.7 Variation matrix

Cross two or more creator-selected axes to produce a small matrix, for example:

- motive × obstacle;
- secret-holder × consequence;
- location function × mood;
- faction goal × method;
- hook × urgency source;
- clue source × reliability;
- payoff × prior setup.

The system must cap combinations before explosion and allow the user to choose axes/count.

### 6.8 Random/seeded table draw

A deterministic table generator may use:

- explicit table ID/version;
- seed/entropy value;
- draw count;
- selected filters;
- provenance.

The same table version + seed + parameters reproduces the same draws. A user may choose unseeded convenience mode, but the generated candidate still records the table/version and enough evidence to explain the source where practical.

### 6.9 Combine/remix prompt

Select two or more authorized fragments/references and request a bounded combination candidate. The result preserves source IDs/versions in provenance and does not mutate sources.

### 6.10 Negative-space prompt

Ask what is missing:

- unused role;
- unanswered question;
- unsupported payoff;
- absent opposition;
- unclear cost;
- missing personal stake;
- missing sensory/social/setting contrast;
- untested assumption.

This is advisory. CSW-06 later owns evidence-backed continuity/open-thread analysis.

## 7. Generator request and candidate identity

A generator run is nonauthoritative but should be reproducible/auditable enough for creative trust.

Conceptual `InspirationRequest` fields:

- `requestId`;
- initiating subject;
- Personal/Campaign creative context;
- source fragment IDs/versions;
- authorized governed-reference IDs/versions where used;
- generator type/version;
- selected parameters/axes/count;
- seed/entropy reference when deterministic randomization is used;
- optional AI task/provider/model provenance where applicable;
- visibility/projection policy version;
- created timestamp/correlation ID.

Each returned `InspirationCandidate` includes:

- candidate ID local to the request;
- candidate content/structured payload;
- source request ID;
- transformation/reason code when deterministic;
- rank/order presentation metadata if any;
- `saved=false` by default.

Candidates are **ephemeral suggestions** until explicitly saved.

## 8. Explicit save/apply dispositions

For each candidate, the creator may:

- **dismiss** — no Creative Fragment created;
- **save-new** — create a new CSW-01 fragment with `derived-from`/`inspired-by` provenance;
- **branch-source** — create a new fragment with `branch-of` provenance;
- **save-as-alternate** — create a new fragment and `alternate-of` relation;
- **append-to-source** — explicit edit/revision of source after showing the change;
- **replace-source-content** — explicit revision only, never default; previous version retained;
- **relate-only** — save a new candidate fragment and explicit relationship;
- **copy-to-project-note** — creates nonauthoritative project/annotation content;
- **discard-all**.

No candidate is automatically incorporated into D18/D28/A9/Character/Campaign or canonical content.

## 9. Alternatives and branching

The engine should encourage alternatives without making the creator manage Git-like mechanics.

When the user says “give me three motives,” the system may return three ephemeral candidates. Saving all three creates three distinct fragments/branches or alternates according to user choice.

Rules:

- source identity remains stable;
- each saved alternative gets its own stable identity;
- source version used is recorded;
- later edits to one alternative do not mutate others;
- selecting a preferred alternative does not delete the rest;
- `supersedes` is explicit if the creator later wants one to replace another in working memory;
- incorporation receipts identify exactly which branch/version was used.

## 10. Duplicate and related-material assistance

CSW-03 consumes CSW-02 advisory duplicate/related discovery.

Before or after saving a new item, the system may surface authorized candidates such as:

- same/near-identical content;
- same normalized label;
- overlapping tags/kind/project;
- explicit shared references;
- deterministic similarity;
- optional AI similarity where separately enabled.

The creator can:

- ignore;
- mark `not-duplicate`;
- relate;
- branch from existing;
- manually merge content into a new/surviving fragment;
- supersede;
- dismiss the candidate.

There is no silent deduplication and no automatic deletion. Existing IDs/provenance remain intact.

Similarity is computed only after authorization filtering. Hidden material cannot affect counts, “you already have something like this” hints, embeddings, ranking, autocomplete, or AI context.

## 11. Source and inspiration provenance

A creator may attach a source/reference/inspiration pointer, but CSW must distinguish **reference metadata** from copied source content.

Provenance may record:

- source URL/document/object reference when the user is authorized to retain it;
- source title/creator safe metadata;
- user note about why it inspired them;
- excerpt/content only when the user has supplied it and retention/use is allowed by applicable product policy;
- accessed/added timestamp;
- source version/checksum when relevant;
- relationship such as `inspired-by` or `references`.

A source reference does not make source claims authoritative in Multiversal.

Protected Campaign/governed material may be referenced only through the visibility-safe governed-reference model. The system must not copy hidden payload into a Personal fragment merely to make Inspiration work later.

## 12. Optional AI assistance

Optional AI can provide:

- alternative ideas;
- “develop this” questions;
- reframes;
- combinations;
- names/phrasing;
- short hook/premise variants;
- structural possibilities;
- summaries of authorized selected material;
- candidate tags/kinds/relationships.

### AI input boundary

Before prompt construction:

- resolve exact selected context;
- filter every fragment/reference/source by current authorization;
- respect Personal/Campaign separation;
- exclude tombstoned/unavailable content unless the viewer may know it and the task requires only safe metadata;
- apply AI consent/provider/cost/retention rules;
- include only the task-relevant selected scope.

### AI output boundary

AI output is:

- ephemeral until explicitly saved;
- pre-authoritative when saved;
- attributable to request/provider/model/task provenance as existing AI policy requires;
- never silently applied to source content;
- never automatically incorporated/published/canonical-promoted;
- never allowed to assert inaccessible source material as fact.

If AI is unavailable, deterministic/manual tools remain fully usable.

## 13. Bounded “develop this” loops

“Develop this” must not become an unbounded recursive generator.

A development session has explicit or default bounds:

- candidate count per step;
- maximum chained steps before returning control;
- selected source scope;
- selected development lens;
- optional stop after a branch/save;
- optional novelty/duplicate threshold;
- optional token/provider/cost budget under existing AI policy.

After the bound, the system summarizes what was generated/saved and asks the creator to choose a direction rather than silently continuing.

The creator can always stop, undo the latest explicit apply where the owning edit model permits it, return to the original seed, or start a new branch.

## 14. Deterministic reproducibility

For deterministic tools, a saved generated fragment should be able to retain enough provenance to answer:

- Which generator/tool/version produced this?
- Which source fragment versions were inputs?
- Which parameters/axes were selected?
- Which seed/table version was used if randomization mattered?
- Was the output edited by the creator afterward?

Reproduction is for trust/debugging/creative reuse, not for claiming the output is objective or canonical.

## 15. Offline capture and recovery

Offline use is intentionally narrow.

### Offline allowed

Under existing cache policy, the client may create/edit unsynced **local draft captures** with:

- local temporary ID;
- local timestamp;
- selected Personal context or last-proven safe draft context;
- draft content;
- local provenance/channel metadata.

### Offline not allowed by CSW-03

Offline capture cannot:

- create authoritative Campaign membership/visibility;
- persist a durable Campaign-bound fragment without current server authorization;
- fetch hidden references;
- run provider AI that requires network/authorization the client does not have;
- silently incorporate/publish.

### Reconnect

On reconnect:

1. reauthenticate/reauthorize context;
2. validate ownership/visibility/project placement;
3. assign durable operation/fragment identity;
4. reconcile duplicates/idempotency;
5. save once or surface conflict;
6. keep failed local drafts recoverable until explicit discard/retention expiry.

If the Campaign context is no longer authorized, the system must not silently upload the draft into that Campaign. It may offer a safe Personal save only if the content itself does not contain protected Campaign material and policy permits that transition; otherwise retain a protected local recovery state or require explicit deletion/export according to policy.

## 16. Accessibility and mobile-first capture

Quick capture must be fully usable without precision pointing or visual-only context.

Requirements for future implementation:

- keyboard-accessible quick add and submission;
- screen-reader-announced saved/draft/recovery state;
- meaningful labels for kind/project/tag suggestions;
- no drag-only triage;
- mobile capture with one primary text field and optional metadata expansion;
- clear unsynced/offline indicator that does not rely on color alone;
- deterministic candidate lists with semantic headings/actions;
- alternative/branch relation explained in plain language;
- generator controls operable by keyboard/touch/screen reader;
- reduced-motion compatibility;
- candidate count/bounds visible before repeated generation;
- destructive archive/tombstone actions separated from ordinary dismiss.

## 17. Warm companion behavior

CSW-03 is one of the clearest places for Multiversal’s approved product voice.

The UI/assistant should feel like a knowledgeable, creative older-sibling/gentle-mentor collaborator:

- curious and encouraging;
- willing to offer possibilities;
- clear when something is only a suggestion;
- respectful when the creator rejects an idea;
- never implying the user must keep generating;
- never treating one suggestion as “the correct story”;
- never praising automatically or excessively;
- comfortable with “leave this unresolved for now.”

The system should help the creator think, not compete with them for authorship.

## 18. Minimum acceptance scenarios

1. User opens quick capture, types one sentence, saves with no project/title/tags → durable `inbox` Creative Fragment created with provenance.
2. User captures offline → local draft survives restart; reconnect creates at most one durable fragment.
3. User triages `idea` to `location-seed` and Project X → identity preserved and authority remains pre-authoritative.
4. Deterministic question ladder returns four questions → none saved as fragments until user acts.
5. Seeded variation tool repeated with same tool version/seed/inputs → same candidate set/order where the tool contract promises determinism.
6. User saves three motive candidates → three stable alternatives/branches, original seed unchanged.
7. User applies one candidate into source → explicit diff/revision; old version remains history.
8. Duplicate discovery finds an older authorized fragment → user can relate/dismiss/branch; no silent merge.
9. Similar hidden Campaign fragment exists but user lacks access → no duplicate hint/count/ranking leak.
10. Personal idea references a currently authorized Campaign object, then access is revoked → protected payload disappears; Personal fragment remains without leaked copy.
11. AI gets two selected authorized fragments → prompt excludes unrelated Personal/Campaign content.
12. AI returns five hooks → all ephemeral until explicit save; saved hook has AI provenance and remains pre-authoritative.
13. AI unavailable → deterministic question/contrast/variation/table tools still support development.
14. “Develop this” reaches configured step/candidate bound → stops and returns control rather than recursively generating.
15. User dismisses every suggestion → source fragment remains intact and no hidden state mutation occurs.
16. Mobile screen-reader user captures and triages without drag or visual-only controls.
17. User saves generated fragment into Campaign-bound project → current Campaign authoring/visibility authorization is revalidated.
18. Generated secret/twist is never surfaced as World/Campaign truth until explicit owning-domain incorporation succeeds.

## 19. Additive implementation touch points

CSW-03 does not authorize implementation. Future CSW-10 handoff may include:

1. quick-capture/local-draft/durable-save contract over CSW-01 fragment identity;
2. Inbox triage actions and batch review;
3. deterministic generator registry with generator ID/version/parameter schemas;
4. seeded table/randomization helper with provenance;
5. InspirationRequest/InspirationCandidate ephemeral session model;
6. explicit candidate disposition/apply/branch APIs;
7. CSW-02 duplicate/related suggestion adapter;
8. governed-reference/source provenance adapter;
9. optional AI suggestion adapter with existing permission/provenance/cost boundaries;
10. bounded development-session coordinator;
11. offline local capture reconciliation/idempotency;
12. accessibility/mobile quick-capture surfaces;
13. tests for no-auto-save, source preservation, hidden duplicate leakage, offline replay, AI failure, reproducible seed, bounded recursion and Campaign revocation.

## 20. Nonauthorization

CSW-03 does not authorize:

- application implementation/migration;
- a new authoritative content type;
- automatic saving/applying of generated candidates;
- automatic World/Adventure/Character/Campaign/incorporation;
- autonomous AI authorship/publication;
- silent duplicate merging;
- copying protected source/Campaign content into Personal storage;
- canonical promotion;
- public marketplace/community publication;
- training on private user creative material;
- release/deployment/tester access;
- CCTI-12-T04 before September 2026.

## 21. Completion gate

CSW-03 is substantively complete when:

- capture requires minimal metadata and defers structure;
- Inbox triage maps cleanly to CSW-01/02 without authority change;
- deterministic no-AI inspiration primitives are explicit and cross-genre;
- seeded tools have reproducibility/provenance rules;
- alternatives/branches never overwrite the seed silently;
- duplicate/related discovery is advisory and visibility-safe;
- source/reference provenance does not copy protected payload;
- optional AI inputs are filtered and outputs remain ephemeral/pre-authoritative until explicit save;
- “develop this” sessions are bounded and creator-controlled;
- offline draft capture/reconnect is safe/idempotent;
- accessibility/mobile capture requirements are explicit;
- product voice supports creator agency without obsequiousness;
- implementation remains additive and unactivated.

Final `completed_verified` requires exact-head AIOC repository-health and merged PR evidence.
