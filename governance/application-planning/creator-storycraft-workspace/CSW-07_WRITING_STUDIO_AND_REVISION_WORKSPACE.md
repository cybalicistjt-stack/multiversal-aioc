# CSW-07 — Writing Studio and Revision Workspace

**Work item:** CSW-07  
**Program:** CSW — Creator Storycraft Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

CSW-07 defines a creator-controlled **Writing Studio and Revision Workspace** for prose that ranges from a single paragraph to long-form documents.

The Writing Studio is not a second Story Bible, World database, Adventure definition, Campaign truth store, publication system or AI author. It is a durable writing environment that composes:

- writer-authored prose;
- Creative Fragments and CSW-04 guided-workflow outputs;
- CSW-02 Story Bible and Project Memory references;
- CSW-06 continuity/open-thread evidence;
- authorized governed-object references;
- explicit revision history, branches and comparison;
- optional deterministic or AI-assisted writing suggestions.

The central invariant is:

> **Writing is editable creative expression; governed truth remains owned by its governing domain.**

A sentence can accurately describe a governed fact without becoming the authority for that fact. A draft can speculate, fictionalize, contradict, summarize, simplify or intentionally obscure. Therefore a prose document must never be treated as canonical truth merely because it is polished, exported, shared, marked final by its author, or assisted by AI.

## 2. Product outcome

A creator should be able to:

1. start from blank prose, a fragment, an outline, a workflow answer or a selection of authorized references;
2. draft freely without completing a mandatory template;
3. keep many documents and sections open across a project;
4. autosave without destroying named checkpoints;
5. branch an alternative version without duplicating unrelated project state;
6. compare two revisions or branches and selectively carry text between them;
7. see Story Bible/governed references beside the writing surface without flattening reference classes into “facts”;
8. receive continuity or stale-reference warnings without the system editing the prose automatically;
9. request bounded transforms such as rephrase, shorten, expand, clarify or adjust tone and inspect the proposed diff before applying it;
10. export or prepare a handout through explicit visibility/redaction checks;
11. recover from disconnect, stale edits or conflicts without silently losing authored text;
12. perform all essential editing, comparison, history and review operations without drag-only, canvas-only or pointer-only UI.

## 3. Scope and non-goals

### In scope

- long-form and short-form prose documents;
- structured sections and headings;
- drafts, autosaves, named checkpoints and immutable revision receipts;
- branches/alternates and branch comparison;
- outline/fragment/workflow-to-draft provenance;
- Story Bible and governed-reference side context;
- explicit links from prose spans/sections to project and governed references;
- continuity/open-thread notices;
- reusable style/voice/terminology guidance;
- optional transformation suggestions with preview/apply/reject;
- print/export/handout preparation boundaries;
- collaborative conflict/recovery rules;
- accessibility/mobile/nonvisual parity.

### Not in scope

- automatic publication;
- automatic promotion of prose to World/Adventure/Campaign truth;
- automatic rewriting to satisfy continuity checks;
- autonomous AI acceptance of its own edits;
- live simultaneous rich-text implementation details;
- final public marketplace/content-sharing architecture;
- application implementation or persistence migration.

## 4. Core object model

CSW-07 separates **document identity**, **editable working state**, and **historical revision evidence**.

### 4.1 WritingDocument

A `WritingDocument` is the durable creator-owned or Campaign-bound writing container.

Conceptual fields:

- `documentId` — stable identity;
- `documentVersion` — optimistic-concurrency metadata/version for document-level settings;
- `ownerSubjectId`;
- attributable author/contributor references;
- `contextBinding` — Personal or bounded Campaign creative context;
- optional `campaignId`;
- optional `projectId`;
- document title/label;
- `documentKind`;
- visibility policy;
- active branch reference;
- section/order metadata;
- style/voice/terminology profile references;
- source/provenance references;
- governed-object links;
- export/handout settings references;
- created/updated metadata;
- archive/tombstone metadata.

A WritingDocument does not contain `objectiveTruth:true`, Campaign Event authority, World canonical status, Adventure runtime state, clue truth, publication authority or automatic incorporation semantics.

### 4.2 DocumentBranch

A `DocumentBranch` is an independently editable line of prose history inside one document identity.

Conceptual fields:

- `branchId`;
- `documentId`;
- branch label;
- `derivedFromRevisionId`;
- branch lifecycle (`active`, `parked`, `merged-by-author`, `superseded`, `archived`);
- head revision reference;
- creator annotations;
- created/updated metadata.

Branching does not branch Story Bible truth, Campaign state, World state or other linked resources. It branches only the WritingDocument’s prose lineage.

### 4.3 WorkingDraft

A `WorkingDraft` represents the current recoverable editing state for a branch.

It may update frequently and may be represented operationally by patches, blocks or editor operations, but conceptually retains:

- branch/document IDs;
- base revision ID;
- local/current working generation/version;
- current content structure;
- autosave sequence;
- pending conflict/recovery metadata;
- last durable-save evidence.

A WorkingDraft is not a historical checkpoint merely because autosave occurred.

### 4.4 DocumentRevision

A `DocumentRevision` is an immutable historical snapshot/receipt of a branch at a deliberate or system-defined durability boundary.

Required conceptual evidence:

- `revisionId`;
- document and branch IDs;
- parent revision(s);
- author/committer subject;
- exact content snapshot or deterministic reconstruction reference;
- revision reason/type;
- source reference versions where relevant;
- assistance/provenance receipts referenced by accepted changes;
- created timestamp;
- checksum/content identity where implementation later requires it.

Revision history is append-only. Editing a revision creates a new working state/revision; it never mutates prior historical evidence in place.

## 5. Document kinds

Initial descriptive kinds include:

- `freeform-prose`;
- `character-backstory`;
- `lore-entry`;
- `location-description`;
- `npc-description`;
- `scene-text`;
- `encounter-description`;
- `adventure-pitch`;
- `campaign-pitch`;
- `rumor-or-legend`;
- `letter-or-message`;
- `journal-or-diary`;
- `player-handout`;
- `gm-note`;
- `session-or-story-summary`;
- `dialogue-or-monologue`;
- `reference-article`;
- `other`.

Document kind configures useful defaults and available guidance. It does not create truth or publication authority.

## 6. Document structure

The writing model supports both simple and structured prose.

A document may contain ordered blocks/sections such as:

- heading;
- prose paragraph;
- list;
- quote/epigraph;
- callout/annotation;
- section break;
- linked reference marker;
- image/media placeholder where future implementation permits;
- table or structured note where supported.

Stable section/block identity is preferred so comments, references, compare results and recovery can attach to semantic content rather than raw character offsets alone.

Writers may also use a plain linear editing projection. Structure is assistance, not a mandatory composition method.

## 7. Autosave, checkpoints and revision history

### 7.1 Autosave

Autosave exists to prevent loss, not to flood history with meaningless “versions.”

Requirements:

- persist recoverable working state frequently enough for bounded data loss;
- maintain a clear `saved`, `saving`, `offline-local`, `conflict`, or `recovery-required` status;
- never imply remote durability when only a local/offline copy exists;
- make repeated autosave idempotent where content/generation is unchanged;
- preserve exact authored text even if reference refresh/analysis fails.

### 7.2 Named checkpoint

A creator may create a named checkpoint such as “Before rewrite,” “Player handout draft,” or “Session 8 recap.”

A checkpoint creates an immutable `DocumentRevision` and optional creator label/note.

### 7.3 Meaningful automatic revision boundaries

An implementation may create revisions at high-value durability boundaries such as:

- explicit save/checkpoint;
- branch creation;
- before applying a large transformation;
- after accepting a multi-span transformation;
- before resolving a collaborative conflict;
- before a handout/export snapshot;
- recovery from a stale/offline branch.

These boundaries must be deterministic and understandable. Autosave frequency itself does not define user-facing revision granularity.

## 8. Branching, alternatives and merge-by-author

Creators often need alternate wording, scene versions or competing directions.

Branch operations:

- create branch from current or historical revision;
- rename/annotate branch;
- park or archive branch;
- compare branches;
- copy selected spans/sections from one branch to another;
- optionally produce a new author-merged branch/revision.

There is no automatic semantic “best branch.” AI may not choose a winner.

### Branch merge rule

A branch merge is a **creator-authored prose operation**. It does not merge linked governed objects and does not resolve Story Bible or continuity conflicts. If source references differ between branches, the resulting revision records which source evidence contributed to accepted text where available.

## 9. Compare and revision review

Comparison must work at multiple useful levels:

- document/section added, removed or reordered;
- paragraph/block change;
- word/phrase change;
- assistance-specific proposed change;
- branch-to-branch comparison;
- revision-to-revision comparison.

The UI must distinguish:

- source/current text;
- proposed replacement;
- insertion;
- deletion;
- move/reorder where determinable;
- unchanged surrounding context.

A creator can accept/reject per proposal or selection. “Accept all” is permitted only as an explicit human action after the complete proposal set is reviewable.

Comparison is content evidence, not a quality score.

## 10. Outline-to-draft and fragment-to-draft

CSW-04/05 material can seed prose without losing identity.

### 10.1 Source-preserving creation

Starting a document from an outline, Creative Fragment, workflow answer, OpenThread or Plot Lab node creates:

- a new WritingDocument/branch;
- provenance edges to exact source IDs/versions;
- optionally copied starting text or generated scaffold clearly marked as document content;
- no mutation of the source object.

Editing the resulting prose never silently edits the source fragment/outline.

### 10.2 Multiple sources

A document may be seeded from several fragments/sections. Provenance should preserve source contribution at document, section or span level where useful rather than pretending the document has one origin.

### 10.3 Reverse handoff

A writer may explicitly create a new Creative Fragment from selected prose or propose incorporation into an owning domain. This is a new governed action with provenance. The writing text does not silently become the downstream object.

## 11. Story Bible and governed-reference side context

CSW-07 uses CSW-02 reference classes rather than flattening all context into “facts.”

The writing surface may show nearby context with labels such as:

- **Governed current reference**;
- **Governed pinned reference**;
- **Campaign-private governed reference**;
- **Creative possibility**;
- **Creator note**;
- **Open question/thread**;
- **Historical/unavailable reference**.

### Side-context rule

Reference content is read through the subject’s **current authorized projection**. Search, suggestion and AI context are filtered before ranking/snippets/generation.

Campaign-private or GM-only context may assist only users who are currently authorized to receive it and only within compatible document visibility/context.

## 12. Linked governed objects and stale-reference behavior

A prose span/section/document may link to a governed object using a stable reference containing, where appropriate:

- target domain/type;
- stable object ID;
- current or pinned version mode;
- optional exact pinned version;
- relationship/purpose label;
- visibility requirements;
- provenance metadata.

### Current reference

A current reference resolves to the latest projection the viewer is authorized to see. The prose itself does not automatically rewrite when the referenced fact changes.

### Pinned reference

A pinned reference preserves the version the author intentionally relied on. The system may say a newer version exists without replacing the pinned source.

### Stale warning

When linked evidence materially changes, CSW-07 may surface:

- “Source updated since this paragraph was written”;
- the old/new reference evidence;
- affected linked prose spans where explicitly associated.

It may not rewrite the paragraph or label it objectively wrong without suitable evidence.

## 13. CSW-06 continuity integration

CSW-06 candidates appear as advisory side evidence.

Examples:

- terminology drift;
- possible timeline mismatch;
- setup/payoff candidate;
- unresolved thread referenced by this section;
- source version drift;
- possible contradiction.

Rules:

1. a candidate never edits prose;
2. dismiss/snooze/intentionally-unresolved state from CSW-06 is respected;
3. resolving a prose issue does not automatically resolve the CSW-06 candidate unless the creator explicitly records that disposition;
4. a changed document revision may cause candidate re-evaluation through CSW-06’s own detector/version rules;
5. the Writing Studio may link to evidence but does not duplicate the continuity truth model.

## 14. Style, voice and terminology guidance

Creators may maintain reusable guidance profiles for a project or document.

Possible profile dimensions:

- point of view;
- tense;
- tone descriptors;
- formality;
- intended audience;
- vocabulary/terminology preferences;
- naming/spelling conventions;
- accessibility/plain-language preferences;
- dialogue conventions;
- formatting conventions;
- words/phrases to prefer or avoid;
- reference excerpts/examples owned or authorized for use.

These are **creator preferences**, not objective correctness rules.

A deliberate deviation does not create an error. The system may offer “This differs from your project preference” and let the creator ignore/dismiss it.

## 15. Optional writing assistance

Writing assistance may be deterministic, local/tool-based, or optional AI-backed depending on the operation.

Initial assistance families:

- rephrase;
- shorten;
- expand;
- clarify;
- simplify;
- adjust tone;
- adjust point of view/tense;
- generate alternatives;
- improve transition/flow;
- summarize;
- convert outline/notes to a prose candidate;
- extract a possible outline from prose;
- check terminology against creator preferences;
- identify sentences that may conflict with linked reference constraints;
- suggest headings/title options.

### Assistance contract

Every mutating suggestion follows:

`Select scope → Choose assistance → Build authorized context → Generate/calculate candidate → Compare → Human apply/reject/partial apply → Create provenance/revision evidence`

The candidate is never automatically the document.

### Factual constraint contract

Where an assistance operation is asked to preserve facts:

- the system supplies only authorized, relevant references;
- source classes remain distinguishable;
- speculative notes cannot silently be elevated to hard constraints;
- the assistance result remains a candidate even if it claims compliance;
- deterministic/reference checks may flag apparent deviations after generation;
- uncertain conflicts must be presented as uncertainty, not silently “fixed.”

### AI boundaries

Optional AI may not:

- auto-apply its generated text;
- promote prose to governed truth;
- invent inaccessible Campaign-private facts;
- resolve continuity candidates or OpenThreads on behalf of the creator;
- publish or share externally;
- change visibility/ownership;
- overwrite history;
- represent a stylistic preference as objective quality;
- require AI for basic editing, history, branching, compare, export or reference browsing.

## 16. Transform receipts

Accepted assistance should preserve sufficient provenance to answer:

- what operation was requested;
- which document/revision/range was selected;
- which context/reference versions were supplied;
- whether optional AI was used and provider/model metadata where policy permits/requires;
- candidate result identity;
- whether the user accepted all, part or none;
- resulting revision ID.

Rejected candidates need not remain indefinitely as full text if retention policy does not require it, but the system may retain a minimal privacy-safe operation receipt where useful.

## 17. Collaboration and authorship

CSW-07 supports attributable contribution without collapsing authorship, ownership and authority.

A collaborator may be authorized to:

- view;
- comment/annotate;
- edit a branch;
- create a branch;
- suggest changes;
- create checkpoints;
- export;
- manage visibility;

as independent permissions/policies.

Edit permission does not imply share/export/publish/incorporate authority.

## 18. Concurrent edit and conflict model

The durable write path uses expected versions/generations.

When concurrent edits can be merged without ambiguity, implementation may produce a deterministic merged working state. When they cannot:

1. preserve both authored variants;
2. do not last-writer-wins silently;
3. create a recovery/conflict branch or comparison state;
4. show affected sections;
5. require an authorized human to choose/carry forward text;
6. create a revision receipt for the resolved result.

Conflict recovery never discards a contributor’s unique prose merely to simplify state.

## 19. Offline editing and reconnect

### Personal context

A Personal document may support bounded offline/local editing if implementation can preserve:

- local change identity;
- base revision;
- local durability status;
- reconnect conflict detection;
- no false “synced” state.

On reconnect, edits reconcile idempotently or branch for human resolution.

### Campaign-bound context

Campaign authority/visibility is revalidated before upload/reconciliation. If access was revoked:

- the client cannot write back to the Campaign document;
- protected Campaign content is removed/handled according to cache/security policy;
- Personal ownership is not silently created for Campaign-private content;
- any permissible local recovery is governed separately and must not leak protected information.

## 20. Recovery after interruption

Recovery must be able to answer:

- what document/branch was open;
- the last durable remote revision;
- whether newer local/autosaved text exists;
- whether an assistance candidate was generated but not accepted;
- whether a reference changed while away;
- whether a conflict exists;
- what safe actions are available now.

An unaccepted assistance candidate never becomes accepted merely because the client crashed after generation.

## 21. Export, print and handout projections

Export is a **projection/copy operation**, not publication or canonical promotion.

Initial output families may include:

- plain text;
- Markdown;
- rich/print-friendly document;
- PDF/print projection where product implementation later supports it;
- copy-to-clipboard;
- player-handout projection;
- GM-private export.

### Export gate

Before creating a shareable/handout projection the system must apply:

1. current subject authorization;
2. document visibility policy;
3. referenced governed-content visibility/redaction rules;
4. Campaign hidden-information rules;
5. explicit export target/profile;
6. optional creator review of redactions/warnings.

A reference that the creator may view is not automatically safe to expose to the handout audience.

### Handout snapshot

A handout export should point to an exact document revision/export receipt so later document edits do not silently rewrite what recipients previously received.

## 22. Relationship between “final draft” and authority

Creators may use editorial labels such as:

- rough;
- draft;
- revised;
- ready-for-review;
- final-by-author;
- archived.

`final-by-author` means editorial intent only. It does not mean:

- canonical;
- published;
- Campaign-approved;
- D28 Adventure-incorporated;
- World truth;
- player-visible;
- safe to share.

Those remain separate governed actions.

## 23. Search and discovery

Writing search may include authorized:

- title/body;
- document kind;
- project/context;
- author/contributor safe projection;
- branch/revision labels;
- linked fragment/reference IDs;
- style/voice tags;
- OpenThread/continuity associations;
- updated time;
- archive state.

Authorization filters precede snippets, counts, ranking, similarity and AI context.

## 24. Mobile behavior

Mobile must support the full semantic workflow, even when layout is simplified.

Required capabilities:

- edit prose;
- navigate sections/headings;
- autosave/status visibility;
- create named checkpoint;
- browse revision history;
- compare current text with a prior revision/candidate;
- accept/reject suggested changes;
- open Story Bible/reference context;
- inspect continuity evidence;
- branch/rename/switch branches;
- resolve conflicts;
- export where authorized.

Dense sidebars may become drawers/sheets, but capabilities may not disappear.

## 25. Accessibility and nonvisual parity

The Writing Studio must not depend on color, visual diff markings, drag, canvas geometry or hover-only affordances.

### Revision comparison

Screen-reader/keyboard users receive an ordered semantic change list including:

- location/section;
- change type;
- old text where applicable;
- proposed/new text;
- surrounding context on request;
- accept/reject/next/previous actions.

### Structure navigation

- headings/sections expose semantic navigation;
- branches and revisions are ordinary named lists/trees;
- reordering offers move-before/move-after/move-to commands;
- reference classes have textual labels;
- save/sync/conflict status is programmatically exposed;
- comments/candidates have stable focus targets;
- keyboard shortcuts have menu equivalents.

All essential operations are available without drag-and-drop.

## 26. Privacy and AI context

The assistance context builder obeys the same authorization-first rule as CSW-02/03/06:

1. resolve subject/context;
2. filter authorized document scope and selected text;
3. resolve only authorized references;
4. apply Campaign/private visibility rules;
5. apply AI-provider eligibility/privacy policy;
6. construct the smallest useful prompt/context;
7. record permitted provenance;
8. discard/transiently handle data according to policy.

Similarity/search/AI may not infer the existence of protected content through counts, labels, snippets or suggestions.

## 27. No-AI operation

Core Writing Studio remains useful without AI:

- direct writing/editing;
- autosave/history;
- named checkpoints;
- branches;
- deterministic diff/compare;
- source links/provenance;
- Story Bible/reference browsing;
- deterministic terminology checks;
- CSW-06 evidence display;
- exports;
- collaborative conflict recovery;
- accessibility/mobile operations.

AI unavailability must not corrupt or lock the document.

## 28. Warm creator-facing voice

CSW-07 follows the approved Multiversal personality: warm, encouraging and mentor-like without flattery or coercion.

Preferred patterns:

- “This source changed since you wrote this section. Want to compare?”
- “There are two versions of this paragraph. Both are preserved.”
- “This wording differs from your project terminology. Keep it or review the alternatives.”
- “That continuity note is still unresolved; it may be intentional.”

Avoid:

- “Your writing is wrong.”
- mandatory quality grades;
- streak pressure;
- “AI fixed your prose” framing;
- shame for abandoned drafts;
- hidden auto-rewrites.

## 29. Deterministic acceptance scenarios

The implementation handoff must eventually prove at least:

1. **Autosave recovery** — unsent/local working text survives interruption with truthful sync status.
2. **Checkpoint immutability** — later edits do not mutate a named revision.
3. **Branch isolation** — editing branch B does not change branch A or linked source objects.
4. **Compare/apply partial** — user applies one proposed change while rejecting another; only accepted text enters the new revision.
5. **Crash-before-accept** — generated assistance candidate remains unaccepted after recovery.
6. **Source provenance** — fragment/outline-derived prose retains source IDs/versions while source edits do not silently rewrite prose.
7. **Governed reference update** — current reference changes, writer receives stale evidence, prose remains untouched.
8. **Pinned reference stability** — pinned evidence remains resolvable while newer source is separately indicated.
9. **Continuity advisory** — CSW-06 candidate is visible but does not auto-edit or auto-resolve.
10. **Hidden reference isolation** — unauthorized viewer cannot discover private Campaign content through search, snippets, counts, AI or export.
11. **Handout redaction** — GM-visible linked material is not included in a player-handout projection unless explicitly safe.
12. **Concurrent conflict preservation** — two incompatible authored edits are both preserved for comparison instead of last-writer-wins loss.
13. **Offline Campaign revocation** — reconnect after authorization loss does not upload protected edits or transfer Campaign-private ownership.
14. **No-AI parity** — core edit/history/branch/compare/export succeeds with AI disabled.
15. **Nonvisual compare** — a screen-reader/keyboard user can inspect and accept/reject the same proposal set as a visual user.
16. **Export snapshot** — exported handout points to an exact revision and remains historically attributable after later edits.

## 30. Downstream handoff to CSW-08

CSW-08 Reuse, Remix and Transformation may consume:

- exact WritingDocument revisions;
- selected spans/sections;
- provenance graph;
- branch ancestry;
- style/voice profile references;
- reference constraints;
- transformation receipts;
- visibility/context policy.

CSW-08 must preserve CSW-07’s core rule that a transformation creates a new candidate/derived object and never mutates source history or authoritative domains implicitly.

## 31. Completion gate

CSW-07 design is complete when the governance package proves:

- stable document/branch/revision identity;
- non-destructive autosave/history/checkpoints;
- source-preserving outline/fragment-to-draft flows;
- branch and comparison semantics;
- reference class/Story Bible support without truth flattening;
- stale governed-reference behavior;
- CSW-06 advisory integration;
- creator-controlled assistance with compare/apply/reject;
- no-AI core operation;
- collaboration/offline/recovery conflict preservation;
- export/handout authorization and snapshot semantics;
- mobile/accessibility/nonvisual parity;
- no automatic prose acceptance, truth promotion, publication or CCTI-12-T04 work.
