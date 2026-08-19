# CSW-10 — Integration, Acceptance and Implementation Handoff

**Work item:** CSW-10  
**Attempt:** CSW-10-attempt-001  
**Status:** design-complete candidate; repository validation required  
**Owner/final authority:** John Brandon Turner  
**Scope:** governance/design handoff only; no application implementation is activated by this document.

## 1. Decision

CSW-01 through CSW-09 form one creator-development system whose application implementation is divided into eight additive slices, `CSW-I01` through `CSW-I08`. These slices reuse existing Stage A/A10/APW authority and persistence rather than creating a second authoring engine, creator account model, Campaign state engine, notification engine, or canonical publication path.

The implementation handoff preserves the full creator loop:

`Capture → Develop → Connect → Structure → Write → Check → Use → Reuse`

The loop remains pre-authoritative until an explicit owning-domain incorporation operation succeeds. A creator draft, Story Bible reference, narrative plan, prose document, derivative, Workshop asset, continuity candidate, Command Center projection or assistant candidate is never itself governed World, Adventure, Campaign, Character, investigation, relationship/faction or canonical content truth.

## 2. Non-reopening rule

CSW implementation is additive successor work. It must not invalidate or reopen completed Stage A evidence merely because a creator-facing representation is added.

In particular:

- A10 remains governed authoring/content truth authority.
- D18 remains World/Location/semantic-geography authority.
- D28 remains reusable Adventure/Module and Campaign run-local Adventure authority.
- D29 remains drafts, proposals, authoring provenance, local authoring workflow, import mappings and source-migration decision authority.
- D05 remains authorization-safe projection authority before search, counts, topology, previews, exports, notifications or optional-AI context.
- D07 remains reusable definition/version/variant/dependency identity authority where governed reusable definitions are involved.
- D06 remains pack lifecycle authority.
- D13 remains media/attachment payload authority.
- A9 runtime social/investigation/relationship/faction state remains in its owning domains; CSW may reference it only through authorized projections and explicit clone/propose transitions.
- Character, Campaign, Scene, Session, Action/proposal, combat and Asset/economy/ownership domains retain their existing authority.

A CSW implementation defect may require fixing an additive CSW adapter or UI surface. It does not, by itself, erase predecessor completion evidence.

## 3. Persistence disposition

### 3.1 Initial-alpha decision

No new top-level creative persistence domain is authorized by CSW-10.

Initial CSW persistence is implemented as bounded additive authoring-support records under D29 `authoring-provenance`, because the revalidated A10 contract already assigns D29 drafts, proposals, review decisions, publication provenance, creator/local authoring workflow, import mappings and source-migration decisions.

CSW-specific records may therefore be modeled as D29-owned namespaces/tables/documents for:

- `CreativeFragment` identity/lifecycle/provenance;
- creator project/library membership and organization;
- Story Bible reference sets and pinned-reference metadata;
- guided-workflow run state and saved creator responses;
- narrative-plan structures that remain pre-authoritative;
- continuity/open-thread review dispositions;
- writing documents, revisions, branches and checkpoints;
- derivation/remix lineage and source-version observations;
- creator resume/return tokens where not already provided by shell/navigation infrastructure.

### 3.2 What D29 must not copy

D29 CSW records store stable references, source versions, creator notes, provenance and explicit transformation receipts. They do not duplicate authoritative payloads owned by D18, D28, Character, Campaign, A9 relationship/faction/investigation, Assets or other domains.

### 3.3 When a new seam could be proposed later

A new bounded creative-support persistence seam may be proposed only if implementation evidence demonstrates a D29 limitation that cannot be solved without violating D29 ownership or causing unacceptable coupling. Such a proposal requires separate governance and migration authority. CSW-10 itself does not authorize it.

## 4. Cross-domain incorporation contract

Every governed incorporation uses an explicit operation with:

- creator source object ID and exact source version;
- target context/domain;
- caller/subject authority;
- expected target version where applicable;
- selected fields/material, not implicit whole-project copying;
- authorization-filtered referenced context;
- transformation/incorporation receipt;
- resulting governed object/version IDs;
- failure/stale/conflict result that leaves source creative material intact.

After incorporation:

- later CSW edits do not silently mutate governed targets;
- later governed-target edits do not silently rewrite CSW source material;
- refresh/rebase/adapt is an explicit creator operation;
- hidden or revoked references are reauthorized before use.

## 5. A10 integration map

### D18 World/Location

CSW can develop locations, world/culture material, setting notes, histories, hooks and related prose. Incorporation into World/Location truth is an explicit D18/D29 authoring operation. CSW never writes D18 tables directly.

### D28 Adventure/Module

CSW-05 narrative plans may propose Adventure nodes, edges, branch structure, hooks, revelations, scenes and other D28 material. The handoff records source narrative IDs and versions. D28 owns the resulting reusable Adventure definition/version and Campaign run-local progression.

### D29 Authoring provenance

D29 owns CSW durable creative-support records, incorporation/proposal receipts, lineage and local authoring workflow. Published governed definitions remain immutable according to A10 rules.

### D05 Visibility projection

Authorization and visibility filtering occur before:

- Story Bible lookup;
- Command Center counts;
- search/autocomplete;
- continuity analysis;
- relationship/dependency topology;
- Campaign-usage projections;
- notifications/badges;
- assistant context or AI prompts;
- export/handout projections.

### D07/D06 reusable content and packs

When a creator artifact becomes a governed reusable definition or pack-bound resource, D07/D06 public contracts own identity/dependency/package lifecycle. CSW derivative identity is not a substitute for governed D07 version identity.

### D13 media

CSW may attach/reference media through D13 contracts. It must not embed duplicate media authority into creative records.

## 6. APW integration map

### APW-04 Personal Workspace

Personal Home owns the account-level entry experience. CSW contributes creator continuation/library projections; it does not create a fourth authority context.

### APW-05 Creator Workshop / Sandbox

Workshop is the general reusable creation and experimentation surface. CSW contributes idea, narrative, writing, continuity and derivation capabilities. Sandbox state remains explicitly noncanonical. Save-out creates a new durable Personal/reusable artifact through an explicit operation rather than promoting the sandbox state in place.

### APW-06 Shell / Navigation / Notifications

CSW Command Center, attention items, deep links and creator reminders obey the APW-06 context anchor, visibility classes, attention orchestration, authorization-before-aggregation and noncoercive notification rules. CSW does not implement a parallel global navigation or notification authority.

## 7. Character, Campaign and A9 integration

### Character

Backstory, personality notes, goals, relationships and alternate concepts remain creative material until an owning Character-domain operation explicitly accepts applicable fields. Character mechanics, inventory, advancement and authoritative stats are never derived by prose mutation.

### Campaign / Scene / Session

Campaign-bound creative work may reference Campaign-private context only after authorization filtering. Copying Campaign-private material to Personal/reusable work requires explicit selection and safe extraction. Live Campaign state never updates because a creator document changed.

### Investigation / clue / mystery

Mystery plans, clue routes and revelation structures remain pre-authoritative. They do not become A9 runtime evidence, objectives, hypotheses or discovered clues until the owning investigation contracts perform an explicit transition.

### Relationship / faction / social

Creative relationship/faction possibilities and prose never represent human consent or runtime social truth. Existing A9/runtime relationship/faction authority remains controlling.

### Future AI

AI remains optional presentation/proposal assistance. It receives only authorized selected context, emits candidate output, cannot auto-apply, cannot incorporate/publish/canonicalize, and has a deterministic/no-AI fallback for every core workflow.

## 8. Final implementation slices

### CSW-I01 — Creative identity, lifecycle and provenance foundation

**Depends on:** D29/A10 authority, APW-01 identity/context.  
**Implements:** CreativeFragment identity, lifecycle, creator ownership, project membership, references, provenance, archive/tombstone, stable versioning.  
**Persistence:** D29 additive namespace.  
**Gate:** no creative object is mistaken for governed truth; provenance and ownership survive reload/recovery.

### CSW-I02 — Creative Library, Story Bible and Project Memory

**Depends on:** CSW-I01, D05.  
**Implements:** library organization, project memory graph, Story Bible projections, governed-current/pinned references, authorization-safe search.  
**Gate:** hidden/revoked references cannot leak through counts/search/topology and governed facts are referenced rather than copied.

### CSW-I03 — Idea Inbox and Inspiration Engine

**Depends on:** CSW-I01/I02.  
**Implements:** rapid capture, deterministic Inspiration primitives, ephemeral candidates, explicit save/discard, bounded optional AI.  
**Gate:** seed remains unchanged unless creator explicitly applies/saves a candidate; useful no-AI operation exists.

### CSW-I04 — Guided Creation Workflows and templates

**Depends on:** CSW-I01–I03.  
**Implements:** reusable step primitives, optional guided runs, skip/revisit/reorder/branch/freeform escape, template version pinning, explicit durable-answer storage.  
**Gate:** novice guidance and expert bypass reach the same underlying creator capabilities with no workflow-as-truth semantics.

### CSW-I05 — Plot/Adventure Lab plus continuity/open-thread analysis

**Depends on:** CSW-I02/I04, D28/D05/A9 projections.  
**Implements:** narrative graph/outline/board/timeline projections, branch/choice/consequence semantics, clue/reveal planning, continuity/open-thread candidates, advisory agency/pacing checks.  
**Gate:** all projections share stable semantics; nonvisual topology parity exists; advisory analysis never rewrites truth; D28 incorporation is explicit.

### CSW-I06 — Writing Studio and revision workspace

**Depends on:** CSW-I02/I05.  
**Implements:** documents, revisions, branches, compare/apply, factual reference panel, autosave/recovery, exports/handout boundary.  
**Gate:** accepted edits are creator-controlled; factual references remain links; exact revision export is reproducible.

### CSW-I07 — Reuse, Remix and Transformation

**Depends on:** CSW-I01/I02/I05/I06, APW-05.  
**Implements:** clone/adapt/fork/remix lineage, independent derivative versions, Campaign-to-Personal safe extraction, template instantiation, source-drift review.  
**Gate:** no silent propagation; privacy filtering precedes extraction; descendants remain independently editable.

### CSW-I08 — Creator Command Center, Workshop/shell integration and end-to-end acceptance

**Depends on:** CSW-I01–I07, APW-05/APW-06.  
**Implements:** Continue Writing, Ideas to Develop, Open Threads, Needs Attention, Recent, Unused, Drafts, Story Bible, Campaign usage, creator search/commands, resume/deep links, visible assistance scope.  
**Gate:** a returning creator can resume exact authorized work across Personal/Project/Campaign contexts with no hidden-count leakage or coercive engagement logic.

## 9. Feature flags and fallback rules

Implementation should allow independent staged activation of the eight CSW slices. A later slice must degrade gracefully when an optional earlier enhancement is off, but may not pretend a required persistence/authority dependency is satisfied.

Suggested planning handles:

- `csw_creative_foundation`
- `csw_library_story_bible`
- `csw_inspiration`
- `csw_guided_creation`
- `csw_narrative_continuity`
- `csw_writing_studio`
- `csw_reuse_remix`
- `csw_command_center`

These names are handoff handles, not activated configuration authority.

AI/provider unavailability never disables core creator operations. Assistant entry points disappear or fall back to deterministic tools without corrupting saved work.

## 10. UI and navigation contract

Implementation must provide responsive and nonvisual-equivalent routes for:

- Personal Home → Create / Continue / Library;
- Creator Command Center;
- Idea Inbox;
- Creative Library and Story Bible;
- Guided Creation run;
- Plot/Adventure Lab in outline, board, timeline, graph and semantic-outline views;
- Continuity/Open Threads review;
- Writing Studio document/revision compare;
- Reuse/Remix lineage and source-change review;
- Creator Workshop/Sandbox entry and save-out;
- explicit incorporation/proposal review surfaces.

Context identity and visibility classification come from APW-06. A graph or board is never the only way to access topology/order/branch/dependency semantics. Reordering has keyboard/touch alternatives; reduced motion is respected; screen-reader labels expose context, state and relationship meaning.

## 11. Migration and compatibility plan

CSW implementation must first inspect the then-current application migration head. CSW-10 does not reserve a numeric migration filename.

Compatibility rules:

1. do not rewrite existing Stage A migrations;
2. add D29 records/tables only through new additive migrations if persistence is required;
3. preserve existing A10 published-definition/version contracts;
4. use adapters/public contracts rather than direct cross-domain storage access;
5. old Campaigns and authoring content remain readable with CSW disabled;
6. disabling a CSW feature never deletes durable creative data;
7. unknown/newer creative record versions fail safely and remain recoverable/exportable where possible;
8. feature rollback hides or deactivates UI behavior but preserves compatible stored records.

## 12. Internal Alpha placement recommendation

CSW application implementation should not activate immediately from this governance tranche. The safest dependency position is after the remaining APW/APM planning handoffs have closed overlapping persistence/recovery seams, with exact activation performed by the governing application roadmap.

Within the eventual application work, implement `CSW-I01 → I08` in dependency order, using focused deterministic checks during construction and the broad CSW end-to-end proof only after the bounded slices exist.

This recommendation avoids colliding with APW-07 persistence/recovery decisions and APW-08 final stage/alpha integration authority.

## 13. Deterministic acceptance families

The companion acceptance matrix covers at minimum:

- lifecycle/provenance persistence;
- authorization-before-search/count/topology;
- Story Bible governed reference behavior;
- deterministic Inspiration/no-AI path;
- guided-workflow skip/revisit/branch/freeform parity;
- narrative multi-view semantic equivalence;
- nonvisual branch/dependency access;
- agency/pacing checks remain advisory;
- mystery plan does not create A9 clue/evidence truth;
- writing autosave/revision/compare/apply/recovery;
- derivative independence and source-drift review;
- Campaign-private extraction safety;
- Command Center exact resume;
- stale/revoked deep-link recovery;
- Sandbox distinction;
- optional-AI candidate-only behavior;
- explicit D18/D28 incorporation;
- no silent propagation after incorporation;
- offline/reconnect/conflict recovery;
- mobile/keyboard/screen-reader/reduced-motion parity;
- complete haunted-lighthouse proof.

## 14. Haunted-lighthouse end-to-end proof

The final proof begins with the literal seed `haunted lighthouse` and must demonstrate:

1. capture as a private CreativeFragment;
2. deterministic and optionally assisted alternate hook/conflict/secret/question development;
3. creation/linking of NPC, location, lore/history and reference material;
4. Story Bible/project-memory links without copied governed truth;
5. a branching narrative plan with scenes/revelations/choices/consequences;
6. continuity/open-thread candidates with evidence and creator disposition;
7. location/NPC/hook/scene prose drafting with recoverable revisions;
8. creator-controlled compare/apply of suggested revisions;
9. explicit incorporation of selected location/World material to D18 and selected Adventure material to D28 through D29 provenance receipts;
10. unused ideas and alternates retained in the creator library;
11. a later derivative/remix in another Personal project with exact lineage and independent editing;
12. Command Center resume to both original and derivative work without hidden-context leakage.

Passing the proof means the creator workflow is integrated; it does not authorize canonical promotion, publication, release or deployment.

## 15. Implementation handoff gate

CSW-10 can be `completed_verified` when this design package and companion matrices pass AIOC repository health and merge. That status means the **planning/handoff is ready**. It does not mean `CSW-I01..I08` are implemented.

No application branch, migration, release, provider activation, public publication or canonical promotion is authorized by CSW-10 alone.