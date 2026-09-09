# CNI — Content & Narrative Interoperability

**Program ID:** CNI  
**Program name:** Content & Narrative Interoperability  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; NOT STARTED  
**Activation:** after SMB-07  
**Successor:** SMB-08  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-09

## Purpose

CNI gives Multiversal a governed, modular content-pack and conditional-narrative runtime before large-scale first-party content production begins. It preserves the useful architectural lessons identified in the Candlekeep Revisited / WeiDU study — modular optional components, dependency-aware installation, scoped persistent state, conditional dialogue, character-aware branching, NPC continuity, one-time/re-entry triggers, compatibility hooks and localization separation — without importing Baldur's Gate/Forgotten Realms content or assuming public repository visibility grants code/asset reuse rights.

CNI is a pattern-derived Multiversal implementation family, not a port of Candlekeep Revisited or WeiDU.

## Ownership boundaries

- **CSW / Story / Adventure owners** remain authoritative for story identity, authored narrative truth, canon and adaptation relationships.
- **Action / Event / approval owners** remain authoritative for canonical mutation. CNI conditions and dialogue nodes may select or propose governed Actions/Events; they do not create a parallel mutation path.
- **Character, Relationship, Reputation, Quest, Scene, Campaign and World owners** retain their canonical state. CNI reads approved projections and binds content behavior to them.
- **ARI** owns resource identity, bytes/reference state, derivative lineage, rights/use capability and shared resource discovery. CNI packs reference ARI resources rather than creating a second asset store.
- **SMB-08/09** consume CNI to produce first-party packs and a complete first-party campaign.
- **SMB-11** remains the owner of cross-user content interchange, packaging for sharing, forks/remixes and controlled distribution. CNI defines runtime/import compatibility contracts, not public sharing authority.
- **SMB-16** remains the final product-wide localization/accessibility/device-completion owner. CNI only ensures narrative/content text is structurally localizable and not embedded inseparably in executable logic.

## Family-execution sizing rule

Every CNI implementation tranche is designed for a **24-minute-or-less bounded execution target under a healthy governed environment**, preserving at least the normal closeout reserve. If a tranche cannot credibly fit the target at governed start, split it before implementation rather than consuming a second bare `Continue`. Final evidence is never weakened to hit the target.

A current runtime `FAMILY_EXECUTION_PREFLIGHT.json` is not created by this planning action because ARI is the active family. CNI receives its sealed current-family preflight only when CNI is later selected by governed start.

## Tranches

### CNI-01 — Content Pack Manifest, Component Identity & Typed Payload Contract
Define stable pack/component IDs, versions, declared content domains, component descriptions, required/optional payloads, ARI resource references and deterministic serialization. A pack may contain multiple independently selectable components without requiring all-or-nothing installation.

### CNI-02 — Dependency, Optional-Component & Compatibility Constraint Contract
Define required/optional dependencies, minimum/maximum compatible versions, mutually exclusive components, capability requirements and install-order constraints. Missing or incompatible dependencies must be explicit rather than discovered through runtime breakage.

### CNI-03 — Scoped Narrative State Hierarchy
Define explicit state scopes for universe/setting, World, Campaign, Session, Scene/location, entity/NPC, encounter and temporary execution state. Provide persistent, one-shot, resettable and derived state semantics with ownership/provenance so a single undifferentiated flag namespace cannot become hidden canonical truth.

### CNI-04 — Conditional Predicate & Context Query Engine
Provide deterministic, inspectable predicates over permitted projections such as story/quest state, location, time, relationships, reputation, Character traits, inventory/capabilities, prior events and pack/component state. Predicates are read-only evaluators and must expose why a branch matched or failed.

### CNI-05 — Executable Dialogue Graph & Governed Action Binding
Represent dialogue nodes, choices, conditions, speaker/participant requirements, transitions and effects as structured content. Effects bind to existing governed Action/Event proposal/execution paths; dialogue text itself never silently mutates canonical state.

### CNI-06 — Character-Aware Narrative Branching
Allow content to branch on declared Character projections including species/ancestry, background, profession/class where the owning ruleset exposes it, skills/abilities, knowledge/familiarity, equipment/capabilities, relationship/reputation state and other explicit traits. Unsupported traits remain unsupported instead of being inferred.

### CNI-07 — NPC Continuity, Relationship & Callback Binding
Provide stable NPC narrative identity, callback conditions, re-encounter references and relationship/timeline hooks so earlier interactions can matter later without duplicating Relationship, Reputation or NPC canonical state inside the content pack.

### CNI-08 — Quest/Scene Progression, One-Shot, Delay & Re-entry Triggers
Provide declarative trigger semantics for first-entry, one-time, repeatable, delayed, chapter/phase, quest-state, location-entry, party-presence and re-entry callbacks. Trigger execution must be deterministic, inspectable and idempotent where required.

### CNI-09 — Cross-Pack Extension, Patch Hook & Conflict Detection
Define explicit extension points and bounded overlays for one pack to integrate with another without destructive whole-object replacement. Detect competing patches, incompatible assumptions and ordering conflicts before activation; preserve source/package provenance for every applied extension.

### CNI-10 — Localization Resource Separation & Stable Text Keys
Separate localizable player-facing text from executable conditions/actions using stable text/resource keys, locale fallback rules, missing-translation diagnostics and deterministic locale projection. Narrative behavior must remain identical across locales except for explicitly localized presentation.

### CNI-11 — Dry-Run Apply, Validation, Transactional Activation & Rollback Receipt
Before a pack/component becomes active, calculate the dependency/apply plan, validate references/rights/compatibility, show conflicts, and support atomic activation or rollback. Produce a deterministic receipt listing activated components, versions, dependencies, extensions and failures without bypassing existing owner-domain validation.

### CNI-12 — Creator Pack / Narrative Inspector & Dependency Graph
Provide developer/creator surfaces to inspect manifests, component selection, dependency graphs, condition explanations, scoped state references, dialogue/trigger links, localization coverage, patch conflicts and provenance. This is an authoring/debugging surface, not public sharing or marketplace authority.

### CNI-13 — Golden Multi-Pack Narrative Compatibility Proof
Prove the family with multiple original Multiversal fixture/first-party packs: optional components, dependency ordering, character-aware dialogue, persistent NPC callback, quest/scene triggers, cross-pack extension, locale switch, failed compatibility dry-run, successful activation, rollback/recovery and deterministic receipts. No Candlekeep/Baldur's Gate copyrighted content is used in the proof.

## Placement rationale

CNI belongs **after SMB-07 and before SMB-08**:

1. MIB and SMB-01..07 provide the mature owner-domain contracts, production platform and cross-system simulation CNI needs to query safely.
2. CNI then establishes the modular content/narrative machinery before SMB-08 begins substantial first-party pack production.
3. SMB-09 can build the complete first-party campaign on the same pack/state/dialogue/compatibility architecture users and creators will later consume.
4. SAA remains after SMB-09 and before SMB-10; it can bind to CNI story/dialogue references where appropriate without becoming narrative authority.
5. SMB-11 later adds controlled sharing/interchange over completed CNI runtime/package compatibility contracts.

## Source-study provenance and reuse boundary

The planning source was a study of the public Candlekeep Revisited repository and its WeiDU-style structure. The useful lessons were architectural patterns: optional components, prerequisite checks, game/context predicates, persistent variables, dialogue/action binding, class-aware branches, later NPC callbacks, cross-mod integration and separated translation resources.

Candlekeep Revisited's repository did not present a root license in the inspected listing, and its subject matter depends on Baldur's Gate/Forgotten Realms intellectual property. Therefore CNI authorizes **no direct copying of its dialogue, assets, scripts or setting content**. Any future reusable code from WeiDU or another source requires its own license review before incorporation.

## Non-activation boundary

This planning program creates no application implementation authority and does not alter ARI's current pointer, branch, checkpoint or family preflight. It authorizes no provider activation, paid spend, scraping/ripping, copyrighted-content extraction, tester distribution, public sharing, marketplace behavior, canon promotion or release/deployment. CNI starts only after SMB-07 is `completed_verified` and a later governed start selects CNI-01.

## Completion standard

CNI completes only when all CNI execution units are `completed_verified`, a modular pack can be dry-run/validated/activated/recovered deterministically, conditional narrative remains explainable and owner-domain safe, optional/cross-pack integration behaves without destructive replacement, localization is structurally separated from behavior, and SMB-08/09 can consume the finished contracts without inventing a parallel content runtime.