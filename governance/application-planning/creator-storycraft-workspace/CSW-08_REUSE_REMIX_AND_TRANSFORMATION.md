# CSW-08 — Reuse, Remix and Transformation

**Work item:** CSW-08  
**Program:** CSW — Creator Storycraft Workspace  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

Reuse in Multiversal creates **new, independently versioned derivative creative work** with explicit provenance. It does not create live synchronization between source and derivative, does not silently mutate a source, and does not grant a derivative the source's authority, visibility, ownership, Campaign membership, publication state, or governed truth status.

CSW-08 defines a reusable transformation layer over the CSW-01/02 creative object model, CSW-05 narrative structure and CSW-07 exact writing revisions. It allows creators to clone, adapt, template, fork, remix and transform material into useful new creative artifacts while preserving where each result came from and what has changed since derivation.

The governing principle is:

`Source snapshot → explicit derivative operation → new identity/version → independent editing → optional later compare/manual adaptation`

Never:

`Source changes → silent derivative mutation`.

## 2. Derivative relationship vocabulary

### 2.1 Clone
A near-copy used as an independent starting point. The clone receives a new object ID and retains a provenance edge to the exact source object/version.

### 2.2 Adapt
A derivative intentionally changed for a different context, setting, system, audience, Campaign or purpose. Adaptation records the target context and creator-confirmed transform decisions.

### 2.3 Template
A reusable creator-owned pattern whose instances receive independent identity. A template may contain prompts, placeholders, structure and defaults but carries no executable/game authority merely because it is reusable.

### 2.4 Fork
A deliberate alternate development line intended to diverge from the source while preserving ancestry. Fork is descriptive provenance, not a Git workflow requirement for the user.

### 2.5 Remix
A derivative composed from two or more authorized sources. Each source/version is separately attributed; the remix receives one new independent identity.

### 2.6 Transform
A change in creative form or purpose, for example NPC history → rumor seeds, lore → handout candidates, plot thread → scene seeds, Character motivation → conflict hooks, or exact prose span → alternate voice treatment.

All six relationships are provenance relationships, not inheritance of authority.

## 3. Stable derivative identity

Every derivative operation records at minimum:

- `derivativeObjectId` and version;
- derivative relationship kind;
- source object IDs and exact source versions;
- source revision/span where CSW-07 prose is involved;
- initiating subject;
- origin Personal/Project/Campaign context classification;
- destination context and ownership;
- transform recipe/profile ID and version when structured;
- creator-confirmed transform inputs;
- optional AI provider/model/task provenance where used;
- creation timestamp and correlation ID;
- inherited-reference manifest;
- compatibility evidence snapshot;
- authorization/visibility evidence appropriate to the operation.

A derivative must never reuse the source object's stable ID.

## 4. Source snapshot rule

Derivation consumes an exact authorized source snapshot. After creation:

1. source and derivative evolve independently;
2. editing the derivative does not alter the source;
3. editing the source does not alter the derivative;
4. later source changes may produce a **source-changed advisory**, never an automatic update;
5. the creator may ignore, compare, manually adapt, or create an explicit rebase candidate.

This rule applies equally to creative fragments, writing revisions, plot structures, templates, Campaign-safe clones and governed-object references.

## 5. Reusable transformation families

The first design contract supports bounded families including:

- NPC/Character concept → hooks, rumors, conflicts, secrets, scene seeds or relationship prompts;
- location → encounters, rumors, sensory descriptions, hooks, complications or travel/event seeds;
- faction → conflicts, agendas, rumors, NPC roles, missions or alliance/tension seeds;
- lore/history → rumors, handouts, mysteries, revelations, scene prompts or alternate interpretations;
- plot/Adventure structure → reusable premise, arc, encounter, branch or scene-pattern templates;
- prose revision/span → summary, pitch, handout candidate, alternate tone, shorter/longer form, style experiment or reusable phrasing pattern;
- mystery material → design-only mystery seed or clue-pattern template without copying runtime clue discovery state;
- encounter concept → reusable encounter seed/template without copying live encounter state;
- Campaign experience/material → governed reusable clone/proposal where authorization permits.

Transform outputs remain pre-authoritative creative artifacts unless an owning-domain incorporation/publish/install action later accepts them.

## 6. Runtime/Campaign → reusable boundary

Live Campaign/runtime state is not a general creative library.

A runtime-to-reusable operation must:

1. identify the exact source object/state projection permitted for reuse;
2. reauthorize the requesting subject;
3. apply visibility/privacy/ownership rules before extraction;
4. exclude secrets or other participants' private material unless separately authorized;
5. distinguish creator-owned reusable source from Campaign-owned/runtime-only truth;
6. create a new Personal/Project reusable derivative or governed proposal;
7. retain provenance to the permissible source reference/version;
8. avoid creating a backward synchronization channel into the live Campaign.

Where the subject lacks unilateral extraction authority, the operation is proposal/review-required or prohibited.

Runtime Events, clue discovery, relationship state, resource state, Character advancement and other live authoritative state do not become reusable definitions merely because a creator selects them.

## 7. Cross-Project, World and Campaign adaptation

Cross-context reuse must never imply cross-context authority.

### Personal/Project → Personal/Project
Normally creator-controlled when ownership/visibility permits. New derivative identity is mandatory.

### Personal/Project → Campaign
Creates a Campaign-side proposal/incorporation candidate or independent Campaign-bound creative derivative according to owning-domain rules. It does not silently become Campaign truth.

### Campaign → Personal/Project
Requires extraction/reuse authority and privacy-safe projection. A Personal derivative does not retain Campaign authority.

### Campaign A → Campaign B
Requires authorization independently in both source and destination contexts. The destination receives an independent derivative/proposal; Campaign A permissions do not transfer.

### World A → World B
World references must be either remapped, intentionally retained as external references where allowed, or represented as unresolved adaptation tasks. Copying content cannot silently create missing World entities.

## 8. Inherited references

A derivative may contain references to governed or creative objects. Each inherited reference is classified:

- retained and accessible;
- retained but destination-incompatible;
- inaccessible in destination;
- intentionally detached;
- remapped to a destination object;
- converted to descriptive text by explicit creator choice;
- unresolved and requires review.

Unauthorized reference targets are not exposed merely to explain a missing link. The UI may say that a source reference cannot be carried into the destination without revealing protected identity/cardinality/details.

A derivative cannot rely on a reference to acquire permissions it does not have.

## 9. Multi-generation provenance

Derivation chains remain traceable without forcing the user to manage a graph manually.

A derivative keeps immediate source edges plus sufficient lineage metadata to answer:

- what was this made from?;
- which exact versions were used?;
- which transforms were creator-authored, deterministic, or AI-assisted?;
- what other derivatives share ancestry?;
- did this result incorporate multiple sources?;
- has a source changed since derivation?

Lineage must not imply endorsement, truth or publication status.

## 10. Source-change behavior

When a source changes after derivation, the system may surface an advisory state:

- source unchanged;
- source changed, derivative not reviewed;
- source changed, differences reviewed;
- source change intentionally ignored;
- manual adaptation in progress;
- explicit rebase candidate prepared;
- derivative intentionally detached from future source comparison.

There is no automatic merge.

### 10.1 Compare
Show semantic/textual/structured differences between the exact old source snapshot, current source and derivative where meaningful.

### 10.2 Manual adapt
Let the creator apply selected source changes deliberately to the derivative as ordinary derivative edits with provenance.

### 10.3 Rebase candidate
For compatible structured material, the system may generate a candidate derivative version based on the newer source plus the derivative's recorded transform decisions. The candidate is nonauthoritative and must be compared/applied by the creator.

“Rebase” is an advanced capability label; ordinary UX should use clearer wording such as **Review source updates** or **Bring selected updates into this copy**.

## 11. Compatibility analysis

Cross-setting/system/schema/pack reuse may produce advisory compatibility findings such as:

- missing referenced definition/pack;
- destination schema cannot represent a source field;
- rules/mechanics dependency does not exist in destination;
- World/setting terminology mismatch;
- unresolved destination reference;
- visibility/ownership mismatch;
- template version mismatch;
- target form lacks a required structural element.

Compatibility findings must include evidence and recommended options. They are not destructive blockers unless an owning-domain incorporation operation genuinely requires compatibility.

Creative adaptation may proceed with explicit unresolved warnings where no authoritative operation is being attempted.

## 12. Templates and starter kits

Creator templates/starter kits are reusable creative definitions with stable IDs and versions. Instantiating one:

- records exact template version;
- creates independent instance identities;
- copies only permitted defaults/content;
- preserves provenance;
- does not create live synchronization;
- does not grant Campaign/runtime authority;
- does not silently install paid/protected dependencies;
- records unresolved dependency requirements explicitly.

Updating a template affects only future instances unless an existing instance explicitly reviews source updates.

## 13. CSW-07 writing integration

Writing transforms reference exact `WritingDocument`, branch, revision and optionally span anchors.

A transform can:

- summarize;
- expand;
- shorten;
- change tone/voice;
- turn prose into a handout/pitch/rumor/scene seed;
- extract candidate terminology/style patterns;
- convert prose structure into a creative outline candidate.

The source writing revision is immutable evidence. Applying a transformed result to another document is a separate explicit write/revision command.

## 14. CSW-05 structure integration

Narrative structure may be cloned/adapted at semantic role/edge level without duplicating D28 authority. A copied CSW plot graph remains a creative derivative. If it later becomes an Adventure definition, the existing CSW-05 governed handoff is required.

Alternate-route, pacing and agency annotations remain advisory after reuse.

## 15. Optional assistance

Deterministic/non-AI assistance may provide:

- transform recipes;
- mapping checklists;
- reference remap tables;
- source-change diffs;
- compatibility checks;
- structured conversion templates;
- deterministic random variation tables where appropriate.

Optional AI may:

- propose adaptations;
- rewrite/summarize/expand authorized content;
- suggest remaps;
- identify likely compatibility concerns;
- create variant candidates;
- explain source/destination differences.

Optional AI may not:

- access unauthorized source material;
- mutate source or derivative automatically;
- resolve protected references by invention;
- publish/promote/incorporate automatically;
- decide Campaign extraction authority;
- grant itself wider context or tools.

Every AI-derived material result remains a candidate until explicitly accepted.

## 16. Privacy and visibility

Authorization filtering occurs before:

- source previews;
- lineage graphs;
- similarity search;
- transform suggestions;
- compatibility analysis requiring source content;
- AI context;
- exports;
- destination reference mapping.

A user cannot discover protected source existence, cardinality or contents through derivative tooling.

If a derivative was validly created earlier and the creator later loses access to a source, the derivative's own permitted content remains governed by its current ownership/visibility while source-detail refresh/comparison is disabled unless authorization returns.

## 17. Collaboration and attribution

Multi-author derivatives retain contributor provenance for accepted changes where the broader CSW/project model supports collaboration. Reuse never erases original source attribution metadata required by policy/licensing/creator governance.

Attribution does not transfer edit or ownership rights.

## 18. Recovery and concurrency

All derivative-creation and update commands use stable operation IDs and optimistic expected versions.

Recovery requirements:

- duplicate create requests return the existing derivative/receipt rather than duplicate it;
- interrupted transformations preserve source snapshot and candidate status;
- applying transform candidates is idempotent;
- concurrent edits never silently overwrite a derivative;
- source update during transformation causes stale-source review when the exact snapshot no longer matches;
- offline-created derivative drafts remain nonauthoritative until synchronized/authorized according to workspace policy.

## 19. Accessible and mobile interaction

All derivative workflows must be possible without drag-and-drop, graph manipulation, hover, color-only state or large-screen side-by-side layouts.

Required alternatives include:

- source/destination summary cards;
- ordered relationship lists;
- textual lineage breadcrumbs;
- table/list reference mapping;
- sequential compare views;
- keyboard/screen-reader actions for keep/remap/detach/resolve;
- explicit status text for source-changed and compatibility states;
- mobile-safe staged transformation review.

## 20. Product voice

Reuse assistance should feel exploratory and empowering rather than corrective. Prefer:

- “This copy was made from an older version. Review what changed?”
- “Three references do not map cleanly to this project.”
- “Want a few ways to adapt this faction for the new setting?”

Avoid implying that divergence from a source is wrong. A derivative is allowed to become something entirely different.

## 21. Acceptance invariants

CSW-08 is design-complete only if:

1. every derivative has independent identity/version;
2. exact source versions and transform provenance are retained;
3. source edits never silently propagate;
4. Campaign/runtime extraction is explicitly authorized and privacy-filtered;
5. cross-context reuse does not transfer permissions/authority;
6. inherited references are explicitly classified/remapped/detached/unresolved;
7. source-change compare/manual-adapt/rebase-candidate paths are non-destructive;
8. compatibility findings are evidence-backed/advisory except where an owning domain requires them;
9. CSW-07 exact revision/span provenance is preserved;
10. optional AI remains candidate-only and authorization-filtered;
11. no-AI reuse remains useful;
12. recovery/idempotency/concurrency are defined;
13. accessible/mobile/nonvisual parity is complete;
14. no derivative automatically becomes Campaign/World/Adventure/canonical truth.

## 22. Downstream handoff

CSW-08 hands reusable, provenance-safe creative artifacts to:

- APW-05 Creator Workshop / Sandbox for experimentation and testing;
- CSW-09 Creator Command Center for rediscovery/resume/related-work projections;
- CSW-10 implementation handoff for persistence, UI and acceptance placement.

It grants none of those tranches implementation or publication authority by itself.