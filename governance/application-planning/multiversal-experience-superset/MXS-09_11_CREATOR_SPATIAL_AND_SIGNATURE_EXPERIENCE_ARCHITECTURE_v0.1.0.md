# MXS-09 through MXS-11 — Creator, Spatial and Signature Experience Architecture

**Version:** 0.1.0  
**Status:** STRATEGY DESIGN / PREIMPLEMENTATION  
**Prepared:** 2026-08-13

## Purpose

This document defines three mutually reinforcing advantages:

1. **MXS-09:** Multiversal as a creator/publisher/rules platform rather than a closed game application.
2. **MXS-10:** a staged hybrid/VTT strategy that delivers value before full spatial parity and does not fork canonical truth.
3. **MXS-11:** signature experiences that become defensible because they depend on the same connected object/event/provenance architecture.

The central strategic rule is that extensions, maps, AI and creator tooling must all consume the same canonical world rather than creating parallel application silos.

---

# MXS-09 — Creator, Publisher and Rules Ecosystem

## Competitive lesson

Current VTT ecosystems demonstrate that extensibility is strategically powerful. Foundry distinguishes Game Systems, Modules and Worlds; its modules may add content, UI, functionality or translations, while game-system development can implement an entire RPG. Fantasy Grounds supports custom rulesets and separately activated extensions. Owlbear Rodeo exposes a TypeScript SDK for extensions that can add tools, context-menu actions, custom UI and Scene interaction.

The opportunity for Multiversal is not merely to replicate a plug-in model. Current extensibility ecosystems often require programming knowledge and may give extensions broad runtime behavior. Multiversal should support **two different extensibility tiers**:

1. safe declarative creation for the large majority of tabletop content/rules;
2. tightly governed executable extensions only where declarative contracts are insufficient and the security/compatibility cost is justified.

## Creator capability ladder

### Level C0 — Campaign-local creation
Target: ordinary GM/player.

Create within one Campaign:
- NPCs;
- creatures;
- items;
- clues;
- relationships;
- locations;
- Scenes;
- adventures/encounters;
- tables/oracles;
- house rules;
- custom tags/resources;
- presentation assets.

Requirements:
- guided forms;
- Generic fallback where specialized UI is unavailable;
- source/provenance distinction between copied, derived and original material;
- explicit visibility and ownership;
- validation before authoritative use.

### Level C1 — Reusable content pack authoring
Target: experienced GM/community creator.

Adds:
- stable namespace;
- dependency declaration;
- semantic versioning;
- reusable Definitions;
- cross-object references;
- media/assets;
- migration notes;
- validation fixtures;
- localization metadata;
- compatibility declarations.

### Level C2 — Rules Profile authoring
Target: system designer.

Declaratively define/configure:
- attributes/resources;
- Actions;
- outcome models;
- Effects/Conditions;
- progression;
- equipment/slot behavior;
- derived values;
- roll/resolution formulas;
- turn/phase rules;
- object capability requirements;
- migration/version behavior.

A creator should not need to implement search, permissions, provenance, networking, autosave, history, accessibility, mobile layout, export or campaign recovery from scratch merely to define an RPG.

### Level C3 — Play Experience Profile authoring
Target: advanced system/adventure designer.

Configure:
- active universal play primitives;
- pacing/phase model;
- role/authority profile;
- required screens/panels;
- progressive-complexity defaults;
- presentation profile;
- spatial abstraction;
- AI/manual-assistance permissions;
- conformance tests.

This allows a creator to build an investigation-focused, heist-focused, tactical, rules-light, solo, domain-level or other experience without forking the core application.

### Level C4 — Publisher integration
Target: professional publisher/licensor.

Adds:
- source ingestion pipelines;
- source-field provenance;
- publisher namespace and signing/identity;
- release manifests;
- entitlement bindings;
- review/certification;
- migration guarantees;
- errata/update channels;
- compatibility certification;
- support/revocation policy;
- attribution/licensing requirements.

### Level C5 — Governed executable extension
Target: specialist developer.

Only when necessary. Requires:
- explicit capability manifest;
- sandbox/process boundary where feasible;
- minimum permissions;
- no implicit access to hidden Campaign/user data;
- version/API compatibility;
- deterministic or auditable behavior where it affects authoritative operations;
- review/signing/trust tier;
- failure isolation;
- ability to disable extension without making existing historical records uninterpretable.

Executable extension support is **not** an early dependency for creator success.

## Content authority tiers

Multiversal should distinguish at least:

1. `private_draft`
2. `campaign_local`
3. `workspace_shared`
4. `community_package`
5. `publisher_package`
6. `multiversal_canonical`

Moving upward is never inferred from popularity, installation count or AI assessment.

Canonical promotion remains a separate explicit owner/governance operation.

## Rules Profile architecture requirements

A Rules Profile should expose a declarative contract for:
- identity/version;
- compatible schema range;
- registered primitives;
- field/value types;
- derived calculations;
- action/outcome/effect graph;
- lifecycle/state machines;
- visibility/authority extensions;
- required assets/content dependencies;
- Character creation/progression rules;
- validation suite;
- migration rules;
- unsupported semantics;
- extension hooks;
- human-readable documentation/provenance.

### Rule-resolution transparency
Any authoritative result should be able to answer:
- what Rules Profile/version governed this?
- what inputs were used?
- what modifiers/rules applied?
- what random/deterministic inputs were used?
- what result was produced?
- who approved/committed it?

## Creator test harness

A creator/publisher should receive automated checks for:
- schema validity;
- stable IDs;
- dependency integrity;
- cycles/orphans;
- permissions/hidden-information leakage;
- deterministic replay where required;
- migration forward/backward expectations;
- uninstall/disable behavior;
- accessibility metadata;
- localization fallbacks;
- UI Generic fallback;
- Rules/Play Experience Profile conformance;
- large-corpus performance budgets;
- all-optionals-off operation;
- unsupported-version behavior.

## Marketplace strategy

A marketplace may eventually improve discovery/distribution but is not architectural authority.

The architecture should work first for:
- local/private pack;
- direct package transfer;
- Campaign/workspace installation;
- publisher distribution.

Later marketplace services may add:
- discovery;
- ratings/reviews;
- purchase/licensing;
- update channels;
- publisher identity;
- dependency resolution.

Avoid making commercial distribution a prerequisite for portable creation.

## Creator ecosystem strategic advantage

The target value is:

> **Build the tabletop game/content; inherit the platform.**

A creator should spend effort on the rules, setting and experience they care about rather than reimplementing the software substrate of modern TTRPG play.

---

# MXS-10 — VTT Bridge, Hybrid Table and Spatial Strategy

## Strategic premise

Multiversal should not delay its core product value until it can outbuild mature VTTs at dynamic spatial rendering.

The authoritative application model must remain useful with:
- no map;
- an abstract map;
- an external VTT;
- printed physical play;
- a shared TV/table display;
- native Multiversal spatial surfaces as they mature.

Spatial representation is a **projection/control surface**, not the source of truth for Characters, Assets, rules or Campaign history.

## Spatial maturity ladder

### S0 — Nonspatial / theater of the mind
Capabilities:
- Scene cast;
- current location/zone labels;
- scene image/background;
- music/ambience hooks;
- Scene notes;
- current clocks/resources/relationships;
- Actions without coordinates.

This must support complete play where the Rules/Play Experience Profile does not require tactical positioning.

### S1 — Abstract spatial relations
Capabilities:
- zones;
- range bands;
- adjacency;
- relative positions;
- fronts/backlines/engagement state;
- vehicle compartments or abstract areas.

### S2 — Static 2D tabletop
Capabilities:
- map/image;
- token placement;
- pan/zoom;
- grid optional;
- manual reveal/fog;
- pings;
- basic labels/markers;
- map-linked objects.

### S3 — Tactical 2D
Adds:
- measurement;
- movement paths;
- area templates;
- elevation/height metadata where required;
- token facing/size if profile uses them;
- rules-aware distance/range.

### S4 — Dynamic visibility
Adds:
- walls/doors;
- vision sources;
- dynamic fog;
- lighting;
- permission-safe player view;
- visibility debugging for GM.

### S5 — Deep spatial automation
Adds:
- path/terrain costs;
- collision/occupancy;
- automatic range/line checks;
- zone/aura Effects;
- spatial triggers;
- tactical replay/evidence.

### S6 — Advanced/3D adapters
Optional:
- 3D scene projection;
- advanced lighting/visibility;
- elevation/volume;
- immersive display/AR/other future surfaces.

These must not force canonical data into renderer-specific geometry.

## Near-term VTT bridge

Until native maturity reaches the requirements of a table, Multiversal should export/bridge:

### Scene/encounter manifest
- Scene stable ID/version;
- participant IDs;
- display names permitted for export;
- portrait/token derivatives;
- sizes/categories;
- disposition/team;
- starting abstract or coordinate placement if available;
- initiative/order if the target workflow needs it;
- status/condition display projection;
- source/provenance IDs where safe.

### Token/portrait derivatives
Use CAPP export contracts for Character/NPC presentation while keeping appearance truth separate from target-VTT image files.

### Read-only companion overlay
Potentially expose:
- initiative/status;
- selected Character details;
- action/result history;
- clues/social state;
- rule references;
- Campaign/session state;
without requiring external VTT to become canonical authority.

### Import/reconciliation boundary
External spatial updates may return bounded facts only through explicit mappings/commands. Never accept a foreign token label or arbitrary plugin state as canonical Character/Asset identity.

## Hybrid / in-person table

Multiversal should deliberately support physical tables.

### Player phone/tablet
- Character workspace;
- rules lookup;
- action proposal;
- private notes/secrets;
- inventory;
- dice/manual result entry where allowed;
- handouts/clues;
- accessibility controls.

### GM laptop/tablet
- Contextual GM Cockpit;
- decision queue;
- Scene controls;
- hidden state;
- world memory;
- optional spatial surface.

### Shared table/TV display
A permission-safe projection containing only shared information:
- scene art;
- tactical/abstract map;
- initiative/current turn;
- public clocks;
- handouts;
- shared notes/objectives;
- ambient media.

The display must be a distinct projection role, never a logged-in GM screen mirrored accidentally.

## Spatial object model requirements

A native map should reference:
- canonical Location/Scene IDs;
- placement IDs distinct from source Definition IDs;
- SpatialRelation/geometry projection;
- reveal/knowledge state;
- layer/presentation metadata;
- map asset provenance/version;
- renderer-specific state outside canonical game truth.

Destroying/moving/interacting with an object on the map becomes canonical only through a governed operation in the relevant domain.

## Interoperability principle

Design bridge adapters around **Multiversal stable IDs and typed projections**, not screen scraping.

The bridge contract should be capable of targeting multiple external tabletop environments because extension ecosystems expose programmatic scene/item/tool integration. Current examples include Foundry packages/modules and Owlbear Rodeo's extension SDK/item APIs. Specific integrations remain later product decisions.

---

# MXS-11 — Multiversal Unique Experience Layer

## Defensibility standard

A signature capability is strategically defensible when:

1. it solves an important tabletop problem;
2. it becomes substantially better because multiple Multiversal domains share identity/history;
3. implementing a superficial copy without that architecture would produce an obviously weaker result;
4. it has an achievable staged version before every future system is complete.

## Signature 1 — World Pulse

### User problem
Campaigns accumulate state faster than humans can remember it.

### Multiversal capability
Generate permission-filtered, evidence-grounded summaries of what changed in:
- Characters;
- relationships/reputation;
- clues/mysteries;
- factions/organizations;
- Assets/crafting/projects;
- locations/settlements;
- campaign/world events;
- unresolved promises/goals.

### Defensibility
A generic note summarizer can summarize prose. World Pulse can query actual typed changes and distinguish direct events, rules-derived effects and inference.

### Staging
- MVP: event/change digest;
- Alpha: cross-domain grouped pulse + re-entry views;
- Later: causal chains/relevance ranking and world-simulation deltas.

## Signature 2 — Causal Campaign Graph / Why Engine

### User problem
Current state is easy to display; explaining *why it became true* is much harder.

### Capability
Traverse provenance/events/relationships/dependencies to answer:
- why does this NPC distrust us?
- when/why did this Item change owner?
- what made this faction hostile?
- why is this rule/effect active?
- what caused this settlement shortage?

### Defensibility
Depends on durable typed identity, provenance and cross-domain events, not only an LLM conversation history.

### Staging
- MVP: per-object history and provenance;
- Alpha: explicit cross-object relation/event paths;
- Later: bounded causal graph with inference labels.

## Signature 3 — Play Experience Profiles

### User problem
RPG software often assumes one style of play even when tabletop games vary radically.

### Capability
Select the mechanics, pacing, authority, cognitive depth and UI relevant to the current mode while preserving canonical objects.

### Defensibility
Requires generic primitives, generic object presentation, profile-aware UI, rules engines and authority layers to work together.

### Staging
- MVP: profile-aware UI/presentation metadata;
- Alpha: several built-in profiles over shared primitives;
- Later: creator-authored certified profiles and cross-profile transitions.

## Signature 4 — Progressive Complexity

### User problem
Powerful TTRPG software either overwhelms newcomers or hides too much from experts.

### Capability
Guided, Standard, Advanced and Diagnostic/GM views of the same authoritative operation.

### Defensibility
Works best when actions and rules are structured/traceable rather than hard-coded into bespoke sheets.

## Signature 5 — Contextual GM Cockpit

### User problem
GM attention is the scarce live-session resource.

### Capability
Assemble the current Scene, participants, hidden facts, pending decisions, relevant rules, relationships, clues, clocks and unresolved threads into a context-specific decision surface.

### Defensibility
Requires cross-domain context plus permission-aware relevance, not another static dashboard.

## Signature 6 — Consequence Preview

### User problem
Interconnected worlds are powerful but can become opaque/unmanageable.

### Capability
Before an authoritative change, preview bounded *classes of likely affected state*:
- relationships;
- reputation;
- resource/cost Effects;
- faction projects;
- inventory;
- world clocks;
- notifications/history.

Preview is noncanonical, version-bound and explicitly uncertain where rules are incomplete.

### Defensibility
Uses typed dependency/event contracts rather than AI guessing alone.

## Signature 7 — Living World Fabric

### User problem
Campaign worlds often feel static outside the players' immediate Scene.

### Capability
Factions, organizations, settlements, economies, projects and world events can progress through governed rules/events when the Campaign enables them.

### Important boundary
This is not an autonomous AI storyteller silently changing canon. World simulation uses deterministic/governed processes, GM-approved events where required and inspectable provenance.

### Staging
- MVP: explicit faction/project clocks and scheduled events;
- Alpha: cross-domain event subscriptions and GM preview/approve batches;
- Later: configurable world simulation cycles with bounded automation.

## Signature 8 — Governed AI over Structured Truth

### User problem
AI tabletop tools are useful but can hallucinate, leak secrets or blur suggestion with canon.

### Capability
AI receives a permission-filtered projection of canonical data and may retrieve, explain, cite, summarize, compare, draft and propose. Structured output is validated before it can become a normal governed operation.

### Defensibility
The advantage is not merely model quality. It is the context/provenance/permission/action substrate around the model.

## Signature 9 — Universal Creator Layer

### User problem
Building a digital implementation of an RPG often requires recreating character sheets, rules automation, permissions, content storage, campaign tooling and VTT behavior.

### Capability
Creators define rules/content/play profiles and inherit common Multiversal platform services.

### Defensibility
Network effects compound with common primitives, validation, compatibility and portable content rather than isolated code modules.

## Signature 10 — Campaign Re-entry / Continuity Engine

### User problem
Long campaigns die partly because context is expensive to recover after interruptions.

### Capability
Role-safe “return to campaign” packet:
- last known state;
- where the Character is;
- active goals;
- important relationships;
- unresolved clues/promises;
- recent changes;
- relevant rules/abilities;
- GM prep cues.

Works deterministically without AI; AI may improve narrative summarization.

## Signature 11 — Cross-scale continuity

### User problem
Many games support Character-scale play or domain-scale play, but transitions are cumbersome.

### Capability
The same event fabric can connect:
Character action → relationship/reputation → faction project → settlement/economic change → future Scene.

Likewise:
vehicle damage → resource/repair project → economy/crafting demand → travel capability.

### Defensibility
Requires a common identity/event model across gameplay domains.

## Signature 12 — The Table Operating System

This is the synthesis, not a separate screen.

Multiversal's long-term identity should be:

> **A tabletop operating environment where rules, content, Characters, worlds, live play, creation, history and optional AI share one governed reality.**

The strategic advantage is cumulative. Each new domain makes existing signature features richer because it becomes another connected source of context and consequence.

---

# Defensibility matrix

| Signature | Main architectural dependencies | Superficial-copy weakness |
|---|---|---|
| World Pulse | event history, permissions, cross-domain IDs | becomes generic text summary |
| Why Engine | provenance, event graph, versions | cannot reliably explain causality |
| Play Experience Profiles | universal primitives, profile-aware UI/rules | becomes cosmetic layout switch |
| Progressive Complexity | structured Actions/rules/provenance | becomes separate simplified app |
| GM Cockpit | cross-domain relevance + hidden projection | becomes another static dashboard |
| Consequence Preview | typed dependencies/rules | becomes ungrounded AI prediction |
| Living World Fabric | domain engines + governed events | becomes opaque GM emulator |
| Governed AI | permissions/provenance/action validation | becomes chatbot/sidebar |
| Creator Layer | generic object/rule/profile platform | creators still rebuild software stack |
| Campaign Re-entry | structured history/notes/goals | becomes transcript summary |
| Cross-scale continuity | shared event/object architecture | systems remain isolated minigames |

# Product sequencing consequences

1. Do not delay A2 for a native VTT. A2's generic object experience is foundational to nearly every signature.
2. A3/A5 must carry Rules Profile, Play Experience Profile and Authority Profile context forward.
3. A6 action/result semantics must remain generic enough for multiple outcome models.
4. A9 social/investigation becomes a major early differentiator because it works without mature spatial rendering.
5. A10 creator architecture should absorb MXS-09 instead of producing a one-off content editor.
6. A11 should treat governed AI as a platform service over authorized projections.
7. A12 hardening should validate multiple profile types, hybrid modes, re-entry and creator-content isolation.
8. Native VTT maturity should proceed as a separate staged spatial track whose output plugs into existing Scene/placement/object contracts.

# Current external evidence

Current official extensibility documentation demonstrates the baseline ecosystem expectation: Foundry modules can add content, UI and functionality and complete Game Systems can be developed; Fantasy Grounds rulesets/extensions modify rules/application behavior; Owlbear Rodeo extensions use a manifest/SDK to add custom tools, UI and Scene interaction. These examples support the need for creator extensibility while also illustrating why Multiversal should offer a safer declarative path that does not require every creator to write application code.
