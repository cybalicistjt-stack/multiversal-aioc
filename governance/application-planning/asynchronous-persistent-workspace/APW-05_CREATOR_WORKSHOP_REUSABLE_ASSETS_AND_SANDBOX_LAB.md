# APW-05 — Creator Workshop, Reusable Assets and Sandbox/Lab

**Work item:** APW-05  
**Program:** APW — Asynchronous Play & Persistent Workspace  
**Status:** DESIGN CONTRACT — READY FOR GOVERNED REVIEW  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

Multiversal exposes creation as a general account capability through a **Creator Workshop** inside the Personal experience. The Workshop is not a new authority context, second content engine, or shortcut around owning-domain validation. It is an orchestration surface over creator-owned reusable definitions, drafts, templates, CSW work, references and governed authoring entry points.

A **Sandbox/Lab** provides deliberately disposable, noncanonical experimentation. Sandbox results do not silently become reusable definitions, Campaign state, progression, rewards, publication or canonical content. Keeping useful Sandbox work always requires an explicit save, clone or proposal operation with current validation and provenance.

Controlling distinction:

`creator draft ≠ reusable definition ≠ template ≠ Campaign variant ≠ live instance ≠ published/canonical content ≠ Sandbox experiment`.

## 2. Personal-context authority

Creator Workshop is a Personal-context surface defined by APW-04. It does not create a permanent Creator role or separate `CreatorContext`.

Entering the Workshop grants no authority over a Campaign, another user's library, global/canonical content, unavailable dependencies or protected source material. Campaign roles remain contextual metadata.

The Workshop may surface creator-owned assets, templates, drafts, CSW Projects/Library work, permitted references, governing authoring entry points, Campaign destinations the subject can currently access, and Personal Sandbox sessions.

## 3. Information architecture

The first design contract organizes the Workshop by intent:

- **Create** — governed creation entry points supported by owning domains.
- **Your Reusable Library** — reusable definitions, templates, starter kits, saved configurations and derivatives.
- **Projects / Storycraft** — deep links to CSW Project, Story Bible, Writing, Plot, Continuity and Reuse tools.
- **Sandbox / Lab** — disposable experimentation and comparison.
- **Needs Review** — validation, dependency, source-change, unresolved-reference and incorporation issues.
- **Recent / Continue** — role-safe navigation projections, never authority.

## 4. Supported reusable families

The Workshop may coordinate creator-owned reusable material for supported domains including Character concepts/templates, Worlds/Locations, NPC/creature definitions, content definitions such as items or abilities where authoring is supported, encounters, Adventures/modules, vehicles/bases, relationship/faction setup, crafting/configuration templates, creator workflow templates and CSW derivatives.

APW-05 does not redefine those domains. The owning domain remains responsible for identity, legality, mechanical meaning, validation, dependencies, publication/install authority and live-instance creation.

If a family does not yet support governed authoring, the Workshop may provide a creative draft path or planned state; it must not emulate authoritative authoring in parallel.

## 5. Lifecycle classes

### Draft
Creator-owned editable material that may be incomplete or fail target validation.

### Reusable definition
Creator-owned material intended for repeated use and validated for a declared use under its owning domain.

### Template / starter kit
A reusable pattern. Instantiation creates new independent identities and records exact template-version provenance.

### Campaign variant
A Campaign-bound adaptation created through explicit Campaign authority. It can derive from a Personal source but evolves independently.

### Live instance
Runtime state owned by its operational domain. Live state never becomes a reusable definition merely because it originated from one.

### Published/canonical/installable content
A status conferred only through the separately governed content/publication domain. APW-05 cannot grant it.

### Sandbox experiment
Personal disposable noncanonical state with no direct authority over any other class.

## 6. Identity and provenance

Workshop projections retain stable object ID/version, owning domain, lifecycle class, Personal/Project scope, owner/authorship, source/template/CSW-08 derivation provenance, dependencies, validation evidence, origin classification, permitted usage links and recovery metadata.

The Workshop aggregates these projections; it is not an alternate source-of-truth store.

## 7. Creation entry points

A Workshop entry point launches or deep-links into the owning authoring domain. It may prefill authorized template defaults, creator references, CSW material, Project organization, rules/system profile or starting configuration.

It may not bypass validation, fabricate mechanical meaning or treat a creative draft as a valid governed definition.

## 8. Campaign transfer verbs

These operations are explicitly different:

- **Link** — reference the same permissible reusable definition only where an owning domain supports reference-style use. A Campaign gains no edit authority over the Personal source.
- **Copy / clone** — create an independent derivative with exact source/version provenance; no later automatic propagation.
- **Instantiate** — create runtime state through the owning domain after current authority, dependency and validation checks.
- **Import** — bring external/exported material into an untrusted review/draft flow; import is not installation or truth.
- **Propose** — send immutable source evidence for Campaign review using governed proposal/decision behavior.
- **Adopt / incorporate** — an owning-domain Campaign command that accepts material into Campaign-bound configuration/truth. APW-05 can launch this flow but cannot self-approve it.

A creator cannot force Personal material into a Campaign. A Campaign GM cannot edit another user's Personal library merely because the material is used there.

## 9. Source and Campaign independence

When one reusable definition is used in multiple Campaigns:

- each Campaign variant/instance is separately governed;
- Personal source updates do not silently mutate Campaigns;
- Campaign edits do not silently mutate Personal sources;
- source/version provenance remains visible where authorized;
- update/adaptation is always explicit.

This preserves the CSW-08 independent-derivative rule.

## 10. Sandbox/Lab model

A Sandbox session is a Personal-owned experiment record with stable `sandboxSessionId`, initiating subject, exact input versions, governing rules/system/dependency profile, optional deterministic seed evidence, experiment purpose, experiment state, timestamps and explicit noncanonical classification.

A Sandbox is not a Campaign, Campaign Session, Adventure run, alternate Character save universe or second rules engine.

Supported experiments may include comparing Character builds/configurations, testing encounter setups, comparing reusable configurations, previewing owning-domain calculation results, testing vehicle/base arrangements, trying templates/CSW derivatives, or examining dependency/validation consequences.

Where mechanics are involved, Sandbox evaluation calls the existing owning-domain deterministic rules rather than duplicating them.

## 11. Sandbox isolation

Sandbox operations may not directly:

- modify a live Character or Campaign resource;
- change Campaign, Scene, Session, investigation, relationship or World runtime truth;
- award progression, currency, loot, entitlements or Campaign project progress;
- publish or promote content;
- alter ownership/permissions;
- emit records that masquerade as live authoritative Events.

This remains true even when an experiment produces a result that would be legal in a live Campaign.

## 12. Saving useful Sandbox work

Supported exits include discard, archive experiment metadata where policy permits, save selected configuration as a Personal draft, save as template, clone a selected result into a reusable-definition candidate, create a Campaign proposal, or export a nonauthoritative report/fixture where permitted.

The save operation explicitly identifies preserved inputs/output and creates the appropriate new identity. Sandbox runtime-like state is never converted wholesale into live Campaign state.

## 13. Comparison seams

The Workshop/Sandbox may compare builds/configurations, encounter composition, resource/cost requirements, dependencies, reusable-definition versions, templates and CSW source/derivative states.

Mechanical calculations come from owning-domain deterministic services and retain rule/schema/dependency/version evidence. Comparison is a projection and cannot create a parallel rules authority or declare subjective creative choices objectively superior.

## 14. Validation and origin presentation

User-visible states distinguish at least:

- draft/incomplete;
- validated for a declared use;
- invalid for target use with evidence;
- stale validation;
- missing/incompatible dependency;
- compatibility warning;
- imported/unreviewed;
- creator-owned reusable;
- Campaign-bound variant;
- Sandbox-only;
- published/installable when separately authoritative;
- generated/assisted provenance where applicable.

“Valid” is always scoped to an exact target/validator/version and never means canonical endorsement.

## 15. Dependencies and entitlements

Reusable assets record rules/schema/pack/definition dependencies explicitly. A destination missing a dependency does not cause silent rewriting. The system offers permitted remap/adaptation options and fails Campaign instantiation safely when the owning domain requires the missing dependency.

No purchase, installation or entitlement change occurs automatically.

## 16. Archive, deletion and reference integrity

Archive/delete behavior distinguishes organization links from underlying objects. Before destructive deletion, authorized inbound references may be shown without exposing protected Campaign details.

Independent Campaign variants/instances and CSW-08 derivatives are not silently deleted when a Personal source is archived or removed. Tombstones or deletion prevention may be used where owning-domain reference integrity requires durable identity.

## 17. CSW integration

CSW-08 derivatives enter the Workshop with exact source/version, transform relationship, source-change advisory, reference status, compatibility evidence and creator/assistance provenance.

CSW creative fragments, Story Bible entries, plot structures and writing documents remain CSW-owned. The Workshop organizes and deep-links them; it does not flatten them into a second generic content store.

## 18. Promotion/publication boundary

The Workshop may offer **Save as template**, **Prepare for review**, **Propose to Campaign**, or **Open publication/promotion flow** when a governing domain exists. It may not self-approve canonical promotion, public sharing, global installation, official status or licensing/provenance review.

Public creator marketplace/community sharing remains outside APW scope.

## 19. Optional assistance

Useful non-AI support includes templates, deterministic generators/tables where governed, validation explanations, dependency options, comparison reports and search/filter over authorized creator content.

Optional AI may suggest draft variants, adaptations, names/descriptions, explain evidence, transform authorized CSW content or suggest experiment setups. AI cannot own mechanics, make invalid content valid, mutate live state, publish/promote or automatically apply changes.

## 20. Recovery and concurrency

Create/update/instantiate/save-from-sandbox commands use stable idempotency keys and expected versions. Ambiguous failures use status lookup. Concurrent edits produce conflict/review behavior rather than silent overwrite. Stale validation/dependency evidence is rechecked at authoritative use time.

Offline status never broadens authority, and offline Sandbox work cannot commit live Campaign mutations.

## 21. Privacy-safe search and usage

Workshop search, counts, tags, recents, similarity and “used in” projections filter authorization before aggregation. Protected Campaign existence/cardinality/content cannot be inferred through creator-library metadata.

## 22. Accessibility and mobile parity

Every Workshop/Sandbox capability has a nonvisual path: list/table/card alternatives, keyboard-accessible operations, screen-reader-readable lifecycle/origin/validation status, textual comparisons, no color-only meaning, mobile staged workflows and clear Personal/Campaign/Sandbox context labels.

## 23. Product voice

The Workshop should feel like a welcoming workbench. Technical provenance and validation detail is progressively available without dominating the creator's task.

Examples:

- “Try it in the Sandbox.”
- “Save this setup as a reusable template.”
- “This version needs a dependency that isn’t available here.”
- “Nothing in the Sandbox changes your campaign unless you choose a separate save or proposal action.”

## 24. Acceptance invariants

APW-05 is design-complete only if:

1. Workshop remains a Personal-context orchestration surface;
2. owning domains retain validation/mechanical/runtime truth;
3. draft/reusable/template/Campaign-variant/live-instance/published/Sandbox classes remain distinct;
4. Campaign authority cannot edit another user's Personal library;
5. Personal ownership cannot force Campaign incorporation;
6. transfer verbs have explicit different semantics;
7. Sandbox cannot award or mutate live state;
8. saving from Sandbox is explicit and creates a governed new draft/template/proposal identity;
9. mechanical comparison reuses owning-domain deterministic logic;
10. provenance, dependencies, validation and origin are visible;
11. source edits never silently propagate;
12. publication/promotion stays separately governed;
13. optional AI stays candidate-only and nonauthoritative;
14. recovery/idempotency/conflict behavior is explicit;
15. search/usage metadata cannot leak protected Campaign information;
16. accessibility/mobile/nonvisual parity is complete.

## 25. Downstream handoff

APW-05 supplies Creator Workshop/Sandbox surfaces and reusable-asset metadata to CSW-09, context/origin/destination metadata to APW-06, persistence/recovery cases to APW-07, and implementation destinations to APW-08.

No application implementation is authorized by this design tranche.