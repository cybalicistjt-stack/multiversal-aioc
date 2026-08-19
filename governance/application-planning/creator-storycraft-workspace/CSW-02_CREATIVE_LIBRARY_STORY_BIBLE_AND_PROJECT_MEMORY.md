# CSW-02 — Creative Library, Story Bible and Project Memory

**Work item:** CSW-02  
**Program:** CSW — Creator Storycraft Workspace  
**Version:** 0.1.0  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

## 1. Decision

CSW-02 defines the durable creator-memory experience built on CSW-01 stable pre-authoritative Creative Fragments and explicit owning-domain references.

It introduces three coordinated projections:

1. **Creative Library** — the creator's findable collection of authorized Creative Fragments, projects, collections, tags, references and derived/incorporated relationships.
2. **Story Bible** — a project-scoped knowledge projection that helps a creator understand important Characters/NPCs, locations, factions, lore, terminology, themes, timeline facts and creator notes by composing CSW material with authorized governed-object references.
3. **Project Memory** — durable provenance/history/backlink/open-work projection answering what was created, how it changed, what uses it, what derives from it, what remains unfinished and what became unavailable or superseded.

These are **projections and organizational structures**, not alternate truth stores. Story Bible entries do not copy and supersede D18 World, D28 Adventure, A4 Character, A5 Campaign, A9 investigation/social, D29 publication or other owning-domain truth. Governed facts remain references to current authorized projections from the owning domain.

## 2. Core product outcome

A creator returning after days, months or years should be able to answer:

- What was I working on?
- What ideas/fragments exist for this project?
- Which material is Personal, Campaign-bound, incorporated, archived or superseded?
- Where is this fragment used?
- What was derived from it?
- Which governed World/Adventure/Character/Campaign objects does it reference?
- What changed and why?
- What remains unresolved or unfinished?
- What disappeared because it was archived, tombstoned, revoked or no longer authorized?
- Which items look similar enough that I may have accidentally duplicated work?

The system must answer these questions without relying on the creator's memory and without leaking material the current subject may not discover.

## 3. Creative Library information architecture

The Creative Library is a **permission-safe organizational projection** over CSW fragments and authorized governed references.

### Primary library views

- **All creative material** — authorized active fragments/references.
- **Inbox** — CSW-01 `inbox` fragments awaiting triage.
- **Developing** — scratch/developing material.
- **Ready to use** — `ready` fragments; label must not imply approved/published.
- **Incorporated** — fragments with one or more incorporation receipts.
- **Open / unresolved** — open questions, unresolved threads and creator-marked unfinished material.
- **Recently changed** — authorized recent creator activity.
- **Archived** — archived material, separately surfaced.
- **Projects** — project-scoped collections and Story Bibles.
- **Collections / saved views** — organizational projections.
- **Tags** — creator-defined or governed project tags.
- **References** — authorized external/governed references collected for creative work.

Tombstoned material is not normally in active library results; it appears only when needed to preserve authorized reference/history integrity.

### Organizational structures

CSW-02 supports:

- project;
- collection;
- folder-like grouping;
- tag;
- saved filter/view;
- pinned/favorite marker;
- ordered outline/list projection.

These structures **do not change ownership, visibility, Campaign membership, target-domain authority or truth status**. Moving a fragment into a “Canon Ideas” folder cannot make it canonical. Moving a governed World reference into a Personal project cannot copy or transfer its ownership.

## 4. Project model

A **Creator Project** is an organizational/context object for creative work, not a World, Adventure or Campaign.

Conceptual fields:

- `projectId`;
- owner subject and explicit collaborators;
- name/description;
- Personal or Campaign creative context binding;
- optional Campaign reference when Campaign-bound;
- visibility policy;
- project status (`active`, `paused`, `completed-by-creator`, `archived`, `tombstoned`);
- default Story Bible configuration;
- collection/tag/saved-view references;
- project provenance/history references;
- created/updated timestamps.

A project may contain references to several Worlds/Adventures/Campaigns or none. A project is not itself a source of World/Adventure/Campaign truth.

## 5. Story Bible model

The Story Bible is a **curated project-memory projection**, not a duplicate database of facts.

### Story Bible sections

The baseline section taxonomy is:

- Characters & NPCs;
- Locations;
- Factions & organizations;
- Lore & setting concepts;
- Terminology & names;
- Themes & motifs;
- Timeline & chronology;
- Mysteries / questions / secrets;
- Plot threads / arcs / hooks;
- Relationships;
- Rules / constraints / project conventions;
- References & inspiration;
- Creator notes.

Sections may contain:

1. **Creative Fragment entries** — CSW-01 pre-authoritative material.
2. **Governed-object references** — live/pinned references to authorized target-domain objects/projections.
3. **Pinned fact references** — an explicit project note that points to a particular governed object/version/field/provenance as the source of a fact.
4. **Creator annotations** — pre-authoritative notes about a governed reference, stored separately from the governed object.

### Fact/reference rule

A Story Bible must visually and semantically distinguish at least:

- `creative-possibility` — fragment/assertion not authoritative;
- `creator-note` — commentary/interpretation;
- `governed-current-reference` — current authorized target-domain projection;
- `governed-pinned-reference` — explicitly version-pinned target evidence;
- `campaign-private-reference` — governed reference whose visibility depends on Campaign authorization;
- `historical-unavailable-reference` — retained pointer/tombstone where source content is no longer available to the viewer.

The Story Bible cannot flatten these into undifferentiated “facts.”

## 6. Project memory graph

Project Memory composes a permission-filtered graph over stable IDs.

### Node classes

- Creative Fragment;
- Creator Project;
- collection/tag/saved-view reference;
- incorporation receipt;
- governed object reference;
- publication/review/provenance receipt reference;
- tombstone/unavailable reference;
- creator history/change event projection.

### Relationship classes

CSW-01 relationships remain available:

- related-to;
- inspired-by;
- derived-from;
- branch-of;
- alternate-of;
- supports;
- contrasts-with;
- foreshadows;
- pays-off;
- supersedes;
- references;
- used-in.

CSW-02 adds organizational/memory relations:

- member-of-project;
- member-of-collection;
- tagged-with;
- pinned-in-story-bible;
- annotated-by;
- incorporated-via;
- created-from-governed-source;
- replaced-by;
- archived-with;

### Backlink rules

Backlinks are generated from explicit stable relationships and receipts. They are never inferred as authoritative relationships from text similarity.

Examples:

- “Used in Adventure X” comes from an incorporation/target reference.
- “Derived from Idea Y” comes from explicit provenance.
- “Referenced by note Z” comes from a stored reference edge.

Similarity may offer a **candidate** relation, but no backlink becomes authoritative project-memory structure until accepted or otherwise explicitly recorded.

## 7. History and provenance

Project Memory maintains a creator-readable timeline over attributable changes.

Required history families:

- fragment created/revised/reclassified;
- branch/clone/alternate created;
- relationship added/removed;
- project/collection/tag membership changed;
- Story Bible pin/annotation changed;
- incorporation proposed/accepted/rejected/withdrawn;
- governed reference pinned/unpinned;
- fragment superseded/archived/restored/tombstoned;
- collaborator/visibility changes where authorized;
- import/export/recovery events;
- optional AI suggestion accepted/rejected/branched where governing AI provenance records exist.

History is not a replacement for owning-domain Event history. For governed objects it stores/project references to the target domain's provenance or version evidence rather than re-authoring the event as CSW truth.

## 8. Search and filtering

Search must apply authorization/visibility **before** counts, facets, rankings, snippets, similarity, graph expansion and pagination.

### Searchable Creative Library fields

Where permitted:

- title/label/body/content;
- fragment kind;
- lifecycle;
- project/collection/tag;
- author/owner/collaborator-safe projection;
- source/inspiration references;
- relationship types;
- incorporated target type/status;
- created/updated time;
- archive/open/unresolved markers;
- governed reference safe label/type/provenance projection.

### Filters

Baseline filters:

- project;
- Personal vs Campaign creative context;
- fragment kind;
- lifecycle;
- tag/collection;
- incorporated/not incorporated;
- unresolved/open status;
- author/owner where authorized;
- recently changed;
- archived;
- target domain/type;
- has backlinks/derivatives;
- has potential duplicate candidates.

### Saved views

A saved view stores query/filter/sort/layout preferences. It does not store a bypassable result set or authorization grant. On every open, results are re-evaluated against current authority.

## 9. Graph and outline projections

Creators may use list, table, outline, timeline and graph presentations.

Graph/outline requirements:

- authorization filtering occurs before node/edge selection and before degree/count calculation;
- hidden nodes do not appear as anonymous gaps whose count leaks existence;
- relation counts are computed from the already-permitted projection;
- unavailable/tombstoned nodes appear only when the viewer is authorized to know a retained reference exists;
- every visual graph has a semantic nonvisual list/outline equivalent;
- graph layout/visual prominence is presentation only and never authority.

## 10. Story Bible timeline and factual chronology

CSW-02 allows a creator to organize chronology without inventing a second runtime timeline.

Timeline entries may be:

- creative proposed date/sequence (`creative-possibility`);
- creator note;
- governed World/Adventure/Character/Campaign fact reference;
- Campaign-runtime Event reference;
- uncertain/range/relative chronology.

Each timeline entry retains its source/evidence class. A speculative date and a governed Event date must be distinguishable in UI, export and analysis.

Later continuity analysis may compare them, but CSW-02 does not silently reconcile contradictions.

## 11. Duplicate and near-duplicate discovery

Duplicate discovery is advisory.

A candidate duplicate record includes:

- candidate IDs/versions;
- comparison basis (exact content digest, normalized label, explicit metadata overlap, deterministic similarity or optional AI/similarity service if later authorized);
- confidence/reason;
- visibility-safe evidence;
- disposition: `unreviewed`, `not-duplicate`, `related`, `merge-manually`, `supersedes`, `dismissed`.

There is **no silent merge**.

If two fragments are consolidated, the creator explicitly chooses a surviving/new fragment and creates provenance/supersedes/derived-from relationships. Existing IDs/receipts remain resolvable or tombstoned according to CSW-01 integrity rules.

Governed objects from owning domains are never merged by CSW duplicate tooling.

## 12. Open, unresolved, unused and dormant material

Project Memory may derive creator-attention projections such as:

- open questions;
- unresolved threads;
- foreshadow without recorded payoff;
- payoff without visible setup;
- ready material not incorporated anywhere;
- fragments with no project/collection placement;
- incorporated source whose target is unavailable/retired;
- dormant material not touched within creator-selected windows;
- fragments with no inbound/outbound relations;
- superseded material still referenced by active fragments.

These are **attention candidates**, not correctness judgments. They may be dismissed, snoozed or marked intentionally unresolved in later CSW work.

No “unused” status should expose a hidden Campaign target or unauthorized backlink. The calculation runs on the authorized graph only.

## 13. Archive and rediscovery

Archive removes material from ordinary active views without deleting it or breaking references.

Rediscovery surfaces may include:

- archived material related to current work;
- older alternatives;
- forgotten ready fragments;
- source fragments behind currently used material;
- dormant projects/collections;
- “you used this before” backlinks.

Rediscovery is subject to current authorization and creator-configured preferences. It cannot resurrect revoked Campaign-private content into Personal results.

## 14. Import

Import creates attributable local creative material/references and never silently overwrites existing objects.

Import requires:

- import operation ID/idempotency;
- source type/manifest/version where available;
- stable incoming IDs or generated import-scoped IDs;
- collision mapping;
- visibility/ownership assignment;
- provenance;
- unresolved reference list;
- creator review before conflictful mappings are accepted.

An imported fragment remains pre-authoritative. Imported governed content must use the owning domain's existing import/proposal/install path; CSW cannot launder imported text into World/Adventure/Campaign truth.

## 15. Export

Export may include authorized:

- fragments and versions;
- project/collection/tag metadata;
- relationships/backlinks;
- Story Bible structure/annotations;
- incorporation/provenance references;
- authorized governed-reference labels/IDs/evidence according to export policy;
- tombstone placeholders where necessary and permitted.

Export does not grant the recipient authority in Multiversal and must not embed hidden content merely because a visible fragment references it.

The export format should preserve stable IDs/provenance sufficiently for re-import/reconciliation without requiring the creator to understand internal database storage.

## 16. Recovery

CSW-02 reuses ordinary recovery principles:

- optimistic versions and expected-version conflict behavior;
- idempotent operations;
- operation status lookup after ambiguous failure;
- explicit import/export receipts;
- durable provenance and tombstones;
- no blind overwrite after reconnect;
- current permission/visibility re-evaluation;
- local unsaved drafts remain distinct from durable Project Memory.

Recovery may rebuild search/graph projections from durable fragment/reference/provenance state; projections themselves are not canonical truth.

## 17. Cross-project reuse boundary

A fragment may belong to or be referenced by multiple projects when authority permits. Project membership is organizational and does not fork identity.

When independent adaptation is desired, the creator branches/clones the fragment per CSW-01 rather than editing one shared source and assuming project-specific divergence.

A governed World/Adventure/Character reference can appear in multiple Story Bibles without copying its authoritative state. Each project may attach separate creator annotations/fragments.

## 18. Optional AI and similarity assistance

Optional AI may help:

- summarize a project from authorized material;
- suggest tags/collections;
- propose possible relationships;
- identify possible duplicates;
- surface forgotten related material;
- create a draft Story Bible summary;
- explain “where this is used” from explicit evidence.

AI output remains proposal/advisory. It cannot:

- create hidden backlinks from inaccessible material;
- silently merge duplicates;
- promote a creator note to governed fact;
- rewrite target-domain truth;
- override visibility;
- use private material outside authorized project context.

Core library/search/filter/history/linking must remain usable without an AI provider.

## 19. Minimum end-to-end proof

A future implementation proof for CSW-02 must show:

1. Creator has a Personal project with five CSW-01 fragments and two authorized governed references.
2. Fragments can be organized into collections/tags without changing authority or truth status.
3. Story Bible displays a creative possibility, a creator annotation and a governed World fact reference as visibly different evidence classes.
4. One fragment is branched; project memory shows source/branch history.
5. One fragment is incorporated into an Adventure proposal; `used-in` backlink derives from the receipt.
6. Later source edit does not alter the incorporated target.
7. Search/facets exclude a Campaign-private fragment the subject cannot currently access, including counts.
8. Graph projection omits hidden node/edge existence and has nonvisual equivalent.
9. Duplicate candidate is suggested and dismissed without merging identities.
10. Archived material leaves active views but remains retrievable and keeps backlinks.
11. Tombstoned source remains as a safe retained reference where required.
12. Export/import round trip preserves stable creative IDs/provenance or explicit mapping without creating authoritative domain content.
13. Recovery after ambiguous save uses operation status/versions rather than blind retry.
14. AI unavailable still leaves full core Library/Story Bible organization usable.

## 20. Additive touch points

CSW-02 identifies, but does not implement:

1. CSW-01 future fragment/provenance seam — project membership, collection/tag and relationship metadata.
2. D05 — visibility-safe library/search/count/graph/timeline projections.
3. A2 Universal Object Experience — reusable search/filter/inspect/link presentation where applicable.
4. APW Personal Workspace/Creator Workshop — project/library entry and Personal/Campaign context switching.
5. D18/D28/D29/A4/A5/A9 — governed-reference adapters; no copied truth.
6. History/provenance — creator-readable activity projection referencing owning-domain evidence.
7. Export/import/recovery — portable project-memory receipts and collision mapping.
8. CSW-03 — Idea Inbox consumes Library/inbox/project placement.
9. CSW-06 — continuity/open-thread analysis consumes evidence-classed Story Bible and authorized graph.
10. CSW-09 — Creator Command Center consumes recently changed/open/unused/continue projections.

## 21. Nonauthorization

CSW-02 does not authorize:

- application implementation/migration;
- a new persistence root;
- copying governed truth into CSW as independent authority;
- silent duplicate merging;
- AI-authored truth or publication;
- canonical promotion;
- public marketplace/community publication;
- paid provider use;
- production credentials;
- release/deployment/tester access;
- CCTI-12-T04 before September 2026.

## 22. Completion gate

CSW-02 is substantively complete when:

- Creative Library, Creator Project, Story Bible and Project Memory roles are unambiguous;
- organizational structure cannot alter authority/truth;
- Story Bible evidence classes distinguish possibility/note/governed reference;
- stable graph/backlinks/history derive from explicit relationships/receipts;
- governed target-domain truth remains referenced rather than duplicated;
- search/count/graph/similarity apply visibility before topology/cardinality;
- duplicate discovery is advisory and never silently merges;
- archive/tombstone/rediscovery/import/export/recovery preserve integrity;
- open/unused/dormant projections are advisory and visibility-safe;
- core capability remains useful without AI;
- implementation remains additive and unactivated.

Final `completed_verified` requires exact-head AIOC repository-health and merged PR evidence.
