# PCM — Proprietary Capability Mining Report

**Status:** OWNER-APPROVED PLANNING EVIDENCE  
**Owner and final authority:** John Brandon Turner  
**Approved / surveyed:** 2026-09-09  
**Implementation authority:** none  
**Catalog:** `PCM_PRODUCT_CAPABILITY_CATALOG.json`  
**Rights control:** `PCM_CLEAN_ROOM_AND_RIGHTS_RULES.md`

## Objective

Survey best-in-class proprietary/non-open-source game-development products to identify capabilities that could materially accelerate Multiversal, reduce recurring provider/AI-credit cost, improve local/offline production, or remove repetitive human work. The survey classifies products as `USE_AS_IS`, `LICENSE_TEMPORARILY`, `STUDY_PATTERNS`, `BUILD_MULTIVERSAL_NATIVE`, or `IGNORE`, then routes native-worthy capabilities to existing Multiversal owners or to one bounded production-acceleration family.

PCM is a planning/research namespace, not an execution family and not a procurement approval.

## Survey coverage

The catalog records 48 representative products across:

- narrative authoring and systems simulation;
- procedural terrain/world/vegetation/urban generation;
- materials, texture baking, VFX and 3D asset generation;
- character creation, rigging, motion capture, animation and facial performance;
- interactive audio, voice and speech production;
- NPC/character AI and real-time AI orchestration;
- localization management;
- asset-heavy version control and production tracking;
- automated QA and human playtesting.

The survey deliberately includes overlapping competitors because agreement across products is useful evidence that a workflow solves a real production problem. Overlap does **not** imply Multiversal should implement multiple competing versions.

## Strongest recurring commercial patterns

### 1. Parameterized production recipes

Houdini-class tools demonstrate that the durable asset is often not a single output but a reusable recipe with inputs, parameters, deterministic regeneration and baked outputs. Gaea, World Machine, SpeedTree and CityEngine reinforce the same pattern for terrain, vegetation and urban forms.

**Multiversal implication:** preserve semantic owner truth, then compile it through reusable procedural production recipes. A World/environment definition should be able to drive many compliant terrain/settlement/flora derivatives without authoring each asset from scratch.

### 2. Authoring surfaces over structured runtime data

articy:draft X and Arcweave show the leverage of visual graph authoring, object databases, validation, localization context and engine export. Multiversal already has the underlying CNI direction; the missing leverage is a first-class authoring workbench rather than editing structured files by hand.

### 3. Interactive media as governed event/state orchestration

FMOD and Wwise show that high-value interactive audio is primarily an authoring/orchestration problem: events, parameters, states, variation, adaptive music, profiling and live iteration. Multiversal already has AAI audio identity and soundscape semantics, so rebuilding a DSP engine would be wasteful. The native opportunity is the production/authoring layer over AAI.

### 4. Performance capture as a normalization pipeline

Rokoko, Cascadeur, Move AI, DeepMotion, Faceware and iClone converge on capture → skeleton/face solve → retarget → cleanup/constraints → standardized clip export. The valuable native subset is normalization, retargeting, foot/root/hand constraints, physics/balance checks, looping/transition repair and provenance—not recreating every commercial animator.

### 5. Provider-neutral generation workflows

Scenario, Meshy and Kaedim demonstrate that production value comes from repeatable briefs, style constraints, batch workflows, review/retry and export as much as from one generation model. Multiversal should own the workflow, manifests, style/reference contracts, provider abstraction and validation so individual models/providers remain replaceable.

### 6. Character AI must bind to live game truth and typed actions

Convai/Inworld-class systems highlight dynamic game context, grounded knowledge/memory, speech and tool/action invocation. Multiversal already has stronger canonical owner boundaries than generic NPC platforms. The native opportunity is a character-intelligence presentation/orchestration layer that reads permitted projections and can only act through governed Action/Event capabilities.

### 7. Localization is stateful production, not final string replacement

Phrase, Crowdin, Lokalise and memoQ converge on stable keys, translation memory, terminology, context/screenshots, stale detection, review state, QA and automation. CNI-10 and SMB-16 already own the structural/final product boundaries; PCA should add the production acceleration between them rather than a duplicate localization authority.

### 8. Asset-heavy production needs governance around VCS, not a new VCS

Perforce and Unity Version Control demonstrate the value of binary locks, artist-safe workflows, large-file awareness and branch/stream coordination. Multiversal should not build another source-control system. PCA should provide ARI-aware asset locks/status, provenance, dependency impact, generated-vs-source distinction and review/approval over Git/LFS/P4-compatible backends.

### 9. QA can become an active content-production participant

modl.ai and GameDriver demonstrate automated gameplay traversal and evidence-rich regression. Multiversal's native opportunity is internal autonomous QA that uses deterministic fixtures plus visual/interaction agents to discover regressions and emit reproducible bug bundles. External human-panel recruitment remains better licensed than recreated.

## Existing-owner reconciliation

The survey does **not** authorize duplicate systems.

- **ARI** remains resource identity, byte/reference state, derivative lineage, rights/use capability and shared discovery authority.
- **SSA / World / Environment / Scene owners** retain semantic spatial/environment truth; procedural tools emit resources/proposals/derivatives from those owners.
- **CAPP / Character / Species/Form owners** retain appearance/body truth; character-production tools compile compatible assets/rigs/LODs only.
- **AAI** remains audio asset/cue/soundscape semantics; PCA adds production authoring, voice generation and profiling over it.
- **DWC speech** remains the governed constructed-language pronunciation/acoustic workstream; PCA-08 may provide reusable production tooling but does not redefine DWC phonology.
- **CNI** remains content/narrative runtime/interoperability; PCA-10 supplies higher-level visual authoring/inspection UX over CNI contracts.
- **APM / Action/Event / SMB-12** retain automated-play and live-AI authority; PCA-11 cannot create unrestricted NPC mutation.
- **SMB-16** remains final product-wide localization/accessibility/device completion.
- **SMB-13 / BRP** retain external tester/product-readiness authority. PCA-14 is internal developer/creator QA only.
- **SMB-11** retains creator sharing/interchange; PCA production tools do not create marketplace/public-sharing authority.

## Resulting implementation family

PCM creates one owner-approved planned family:

**PCA — Production Capability Acceleration**

Placement:

`SMB-07 → CNI-01..13 → PCA-01..16 → SMB-08`

The placement is intentional. SMB-01..07 provide mature production/runtime owners; CNI provides content/narrative interoperability; PCA then builds the production acceleration layer immediately before SMB-08 begins substantial first-party content production.

PCA is not a new canonical state engine. It is a collection of authoring, compilation, generation, validation, production and QA tools over existing owners.

## Cost/credit leverage conclusions

The highest expected recurring savings come from:

1. local procedural asset/world generation from reusable recipes instead of repeated one-off AI generation;
2. local style/reference manifests and batch production so expensive model calls are targeted and cached;
3. local voice/motion/material preprocessing and QA on the established RTX workstation rather than repeated cloud services;
4. deterministic authoring/validation tools that let lower-intelligence automation execute mechanical work safely;
5. local simulation/balance sweeps rather than conversationally reasoning through every parameter change;
6. autonomous regression/playtest agents that discover failures before human review;
7. reusable translation memory/glossary/context rather than retranslating unchanged content;
8. persistent production manifests and asset dependency graphs that prevent rediscovery/re-ingestion.

The native systems should still permit commercial tools/providers when they are economically superior. The strategic goal is **provider independence and owned workflow**, not refusing useful third-party software.

## Items explicitly not worth recreating wholesale

- a full ZBrush-class sculpt engine;
- a full cloth/garment physics package;
- a production-quality general fluid simulator purely to replace EmberGen;
- a full commercial VCS to replace Git/P4/Plastic;
- a recruited human playtest-panel business;
- proprietary vendor marketplaces, training corpora or hosting networks.

These may be used/licensed where justified while Multiversal owns the higher-level workflow and exit path.

## Planning outcome

Durable PCA program/backlog and a roadmap amendment are the authoritative implementation-plan outputs of PCM. This survey does not alter the active ARI-04 implementation pointer, does not grant PCA implementation authority, and does not authorize paid services or proprietary-content extraction.
