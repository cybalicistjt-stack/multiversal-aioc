# Application Implementation Roadmap — PCM/PCA Planning Amendment — 2026-09-09

**Status:** OWNER-APPROVED PLANNING AMENDMENT  
**Owner and final authority:** John Brandon Turner  
**Runtime effect:** none; ARI-04 remains the current in-progress work under the live runtime pointer/index.  
**Implementation authority created by this amendment:** none.

## Owner decision preserved

The owner approved a formal survey of high-value proprietary/non-open-source game-development products to identify workflows and capabilities that Multiversal should independently implement where doing so materially improves production speed, local/offline capability, provider independence, recurring cost, or AI-credit efficiency.

The survey is preserved as **PCM — Proprietary Capability Mining**, a planning/research namespace only. PCM does not become an implementation family.

The survey produces one new critical-path interstitial family:

- **PCA — Production Capability Acceleration**, after **CNI-13** and before **SMB-08 — Core Content Production**.

## Corrected effective forward order

The effective future order is amended to:

`ARI-04..21 → ARI-22A/B/C → MIB-16 → MIB-17 → MIB-18 → SMB-01 → SMB-02 → SMB-03 → SMB-04 → SMB-05 → SMB-06 → SMB-07 → CNI-01..13 → PCA-01..16 → SMB-08 → SMB-09 → SAA-01..20 → SMB-10 → SMB-11 → SMB-12 → SMB-13 → SMB-14 → SMB-15 → SMB-16 → BRP-01..11 → SMB-17 → SMB-18`

Completed predecessors remain completed. This amendment does not reopen AAI, SSA, CAPP or any other completed/parallel family and does not disturb ARI-04's current implementation branch/preflight.

## Why PCA is inserted before SMB-08

SMB-08 is the first large first-party content-production tranche. Without PCA, substantial terrain/environment assets, materials, character derivatives, motion, audio/voice, narrative authoring, localization preparation, balance simulation and QA would be created before the reusable production-acceleration layer exists, causing avoidable one-off work and later migration.

CNI must remain before PCA because PCA-10's visual narrative/content workbench is an authoring surface over CNI's structured content/runtime contracts. PCA then supplies cross-media production tools before SMB-08 and SMB-09 become their first large consumers.

## PCM survey result

PCM surveyed 48 representative commercial/proprietary products across narrative authoring, systems simulation, procedural worlds, materials/VFX, 3D/character production, animation/mocap, audio/voice, NPC AI, localization, version/production tracking and QA/playtesting.

Products are classified using:

- `USE_AS_IS`
- `LICENSE_TEMPORARILY`
- `STUDY_PATTERNS`
- `BUILD_MULTIVERSAL_NATIVE`
- `IGNORE`

The durable catalog and clean-room controls are:

- `proprietary-capability-mining/PCM_PRODUCT_CAPABILITY_CATALOG.json`
- `proprietary-capability-mining/PCM_PROPRIETARY_CAPABILITY_MINING_REPORT.md`
- `proprietary-capability-mining/PCM_CLEAN_ROOM_AND_RIGHTS_RULES.md`

## PCA scope

PCA contains 16 bounded execution units:

1. common recipe/provenance/provider-adapter core;
2. reusable procedural graph/asset recipe engine;
3. terrain/ecology/flora/settlement/spatial generators;
4. material/texture/bake/VFX production pipeline;
5. character asset/rig/garment/LOD pipeline;
6. motion/facial performance factory;
7. interactive audio director/authoring workbench;
8. voice/speech/sound production factory;
9. style-locked provider-neutral generation orchestrator;
10. visual narrative/content authoring workbench over CNI;
11. governed character-intelligence orchestrator;
12. systems simulation/balance workbench;
13. localization production workbench;
14. autonomous internal QA/playtest agents;
15. asset-production governance/locking/dependency/review overlay;
16. golden local-first production acceleration proof.

Program/backlog:

- `production-capability-acceleration/PCA_PRODUCTION_CAPABILITY_ACCELERATION_PROGRAM.md`
- `production-capability-acceleration/PCA_PROGRAM_BACKLOG.json`

## Ownership / non-duplication contract

PCA does not replace existing owners:

- ARI owns resource identity, bytes/reference state, derivative lineage and rights/use capability.
- SSA/World/Environment/Scene/MAI/ISE own semantic spatial/media context.
- CAPP/Character/Species/Form/PAPT own appearance/body/art-production semantics.
- AAI owns audio cue/soundscape semantics; DWC owns constructed-language pronunciation/acoustic authority.
- CNI/CSW/Story/Adventure own structured content/narrative identity and runtime behavior.
- Action/Event/APM own canonical mutation and automated-play authority.
- MIB-15/SMB-12 own AI-provider abstraction/live integration authority.
- SMB-11 owns creator interchange/sharing.
- SMB-13/BRP own external testing/product readiness.
- SMB-16 owns final product localization/accessibility/device completion.

PCA outputs are recipes, candidates, derivatives, authoring data, production metadata and QA evidence until owning domains accept them through existing governed paths.

## Rights / clean-room boundary

The survey authorizes independent implementation of general capability/workflow requirements only. It authorizes no reverse engineering, decompilation, protected-content extraction, copied proprietary source/assets, trial-EULA violation, private-protocol recovery or assumption that public visibility grants reuse rights.

Any direct commercial/open-source SDK, code, model, asset or dataset later incorporated receives its own ARI license/rights/provenance review.

## Cost and AI-credit objective

PCA has an explicit production-cost goal. Implementations should favor reusable recipes, deterministic caches, local workstation execution, batch operations, content-addressed artifacts, provider abstraction, incremental recomputation and machine-readable execution contracts that permit lower-intelligence automation to safely perform mechanical work.

PCA must not optimize cost by weakening provenance, rights, acceptance, canonical-state or quality gates.

## Family execution rule

PCA follows the current family method: each planned execution unit targets 24 active minutes or less under a healthy environment with closeout reserve protected. An oversized unit is split before governed start.

No PCA family preflight is created by this planning amendment because ARI is active. PCA receives a sealed runtime preflight only after CNI-13 is `completed_verified` and a future governed transition selects PCA-01.

## Authority and non-activation rules

- ARI-04 remains current and retains its existing bounded application implementation authority.
- PCA cannot start before CNI-13 reaches `completed_verified` and a later governed start selects PCA-01.
- PCA-02+ remain unauthorized until strict-successor selection advances through the family.
- No paid product/subscription, proprietary provider credential, external upload, copyrighted-content extraction, public sharing, tester distribution, marketplace, canon promotion or release/deployment authority is created here.
- Commercial products may later be selected for lawful temporary/use-as-is roles only after then-current price/terms/privacy/rights review and any required owner approval.
- Removal or relocation of PCA requires a later explicit owner decision and canonical planning amendment.
