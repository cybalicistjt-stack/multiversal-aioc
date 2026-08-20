# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.28.0  
**Status:** ICF ACTIVE AT ICF-09 — MIB PAUSED AFTER MIB-13 — CEL OWNER-DIRECTED INTERSTITIAL — SMB + MCB OWNER-APPROVED PLANNED  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-20

## Authority and operating rule

Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence. This roadmap owns milestone order and dependency intent; it does not override the runtime selector when status prose ages.

The strict APW/CSW/APM predecessor sequence remains **COMPLETED_VERIFIED**.

Approved/directed forward programs:
1. **MIB — Multiversal Implementation Backbone** — completed verified through MIB-13; paused for ICF.
2. **ICF — Ingredient, Cultivation & Foodcraft Foundation** — active interstitial subproject after MIB-13 and before MIB-14.
3. **CEL — Cozy Economy & Life Loop** — owner-directed planned interstitial subproject after MIB-14 and before MIB-15.
4. **SMB — System Maturation & Buildout** — owner-approved planned post-MIB successor.
5. **MCB — Market Capture & Brand Backbone** — owner-approved planned commercial-preparation program; bounded early parallel work requires separate owner routing.

The runtime selector currently identifies **ICF-09 — Creature Catalog Harvest Crosswalk & Signature Ingredient Library** as the sole implementation item, state `selected_not_started`.

## MIB current state

MIB is **completed_verified through MIB-13**.

Most recent MIB completion:
- **MIB-13 — Economy and Trade Deterministic Engine** — App PR #239; squash merge `3d484d186a7589bbbf1c9585541bcbc42e04fd51`.
- The Application repository later advanced through owner-source intake PR #240 to main `f66f550c246d77ea84237511330cac36674b6e25`; that intake has no runtime implementation authority.
- Migration head remains `0021_apm_autogm_mini_campaign_director.json`; migration `0022` is not reserved.

MIB resumes at **MIB-14 — Vehicle, Platform and Base Engine Foundations** only after ICF-15 is completed unless the owner explicitly re-routes the roadmap.

## Effective implementation order

MIB numbering remains stable, with the owner-approved ICF and owner-directed CEL subprojects inserted as mandatory roadmap sequences unless the owner explicitly re-routes them:

`MIB-13 → ICF-01 → ICF-02 → ICF-03 → ICF-04 → ICF-05 → ICF-06 → ICF-07 → ICF-08 → ICF-09 → ICF-10 → ICF-11 → ICF-12 → ICF-13 → ICF-14 → ICF-15 → MIB-14 → CEL-01 → CEL-02 → CEL-03 → CEL-04 → CEL-05 → CEL-06 → MIB-15 → MIB-16 → MIB-17 → MIB-18`

MIB-14 does not begin until ICF is completed. CEL does not begin until MIB-14 is completed. MIB-15 does not begin until CEL is completed, unless the owner explicitly re-routes the roadmap.

## ICF — Ingredient, Cultivation & Foodcraft Foundation

**Program:** `governance/application-planning/ingredient-cultivation-foodcraft/ICF_INGREDIENT_CULTIVATION_FOODCRAFT_PROGRAM.md`  
**Backlog:** `governance/application-planning/ingredient-cultivation-foodcraft/ICF_PROGRAM_BACKLOG.json`  
**State:** in progress  
**Activation:** after completed MIB-13  
**Resume MIB:** MIB-14 after ICF completion

ICF creates one canonical ingredient ecology shared by agriculture, foraging, livestock, creature harvesting/butchery, cooking, magical cooking, alchemy, medicine, ritual, crafting, trade and later base/settlement production. It consolidates the approved Cooking, Agriculture and Alchemy source packages, existing CSV/material/facility content, governed starter packs and creature harvest/loot references.

### ICF tranche roadmap

| Tranche | State |
|---|---|
| ICF-01 — Source Inventory & Reconciliation | completed_verified |
| ICF-02 — Canonical Ingredient Schema & Taxonomy | completed_verified |
| ICF-03 — Mundane Crop & Staple Plant Library | completed_verified |
| ICF-04 — Herbs, Spices, Fungi & Wild Forage | completed_verified |
| ICF-05 — Livestock, Animal & Aquatic Ingredient Library | completed_verified |
| **ICF-06 — Magical, Exotic & Multiversal Ingredients** | **completed_verified — protected original tranche** |
| **ICF-07 — Creature Harvest, Butchery & Biological Ingredient System** | **completed_verified — protected approved tranche** |
| **ICF-08 — Creature Part Effect Taxonomy & Affinity Grammar** | **completed_verified** |
| **ICF-09 — Creature Catalog Harvest Crosswalk & Signature Ingredient Library** | **selected_not_started — current** |
| ICF-10 — Preparation, Processing & Derived Ingredients | planned |
| ICF-11 — Alchemical Ingredient Rules & Formula Grammar | planned |
| ICF-12 — Culinary & Magical Culinary Rules | planned |
| ICF-13 — Agriculture, Foraging, Husbandry & Production Integration | planned |
| ICF-14 — Recipe Corpus & Recipe-Generation Foundation | planned |
| ICF-15 — Content Packs, Validation, Search & Workbench | planned |

**Protected numbering rule:** the originally approved **ICF-06 remains Magical, Exotic & Multiversal Ingredients** and **ICF-07 remains Creature Harvest, Butchery & Biological Ingredient System**. Creature-part grammar and catalog crosswalk remain ICF-08 and ICF-09; later preparation/rules/integration/content-pack work remains ICF-10 through ICF-15.

### ICF current implementation boundary

ICF-09 walks the governed creature catalog and binds authored creatures and variants to:
- ICF-07 harvest profiles and deterministic harvest/butchery boundaries;
- ICF-08 part baselines, body-plan/type profiles and trait/affinity tendencies;
- canonical ingredient/material definitions and stable IDs;
- exact-creature signature ingredients where authored evidence supports them;
- explicit coverage-gap records where anatomy, effects, edibility, legality, harvest procedure or lore is not supported by governed evidence.

ICF-09 must not infer anatomy or exact effects from broad creature types, folklore, genre tropes or same-named organs. Harvestability never silently grants edibility, safety, legality or cultural acceptability.

### ICF creature/effect architecture

Creature ingredients use the governed inheritance pattern:

`part baseline → body-plan/creature-type profile → creature affinity/trait profile → explicit species/variant override → harvested-instance quality/condition`

Broad part classes define reusable culinary/alchemical/magical/crafting tendencies only. They do not authorize fabricated creature anatomy, exact effects or lore.

### ICF Downtime/Cozy integration

Long-running or repeated cultivation, husbandry, gathering, harvesting, butchery, preservation, processing, cooking, brewing, alchemy and production reuse existing Downtime/Project activity semantics. ICF may publish Cozy-eligibility metadata for routine deterministic operations, but APM retains delegation/authorization/budget/stop-condition authority and wall-clock time does not become game progress by default.

### ICF architecture and scale

One canonical ingredient definition can carry physical, ecological/agricultural, economic, culinary, magical-culinary and alchemical profiles. Source-derived terminology/provenance stays traceable. Live inventory/Asset Instances remain owned by the existing inventory authority.

The first-party foundation targets approximately **700–1,000 primary ingredients** plus **300–500 derived preparations**, spanning mundane crops/plants, herbs/spices/fungi/forage, livestock/animal/aquatic outputs, basic reagents and magical/exotic/multiversal ingredients.

ICF-03 through ICF-06 currently establish **964 primary ingredient definitions** before the ICF-09 creature-catalog crosswalk adds or binds supported signature creature ingredients.

## MIB-14 dependency bridge

**MIB-14 — Vehicle, Platform and Base Engine Foundations** follows ICF. Besides vehicle/platform work, its base/facility/storage/workstation/resource-accounting foundations become required inputs to CEL. CEL does not invent Cozy-only home/base truth.

## CEL — Cozy Economy & Life Loop

**Program:** `governance/application-planning/cozy-economy-life-loop/CEL_COZY_ECONOMY_LIFE_LOOP_PROGRAM.md`  
**Backlog:** `governance/application-planning/cozy-economy-life-loop/CEL_PROGRAM_BACKLOG.json`  
**State:** owner-directed planned; not yet selected  
**Activation:** after MIB-14 completion  
**Resume MIB:** MIB-15 after CEL completion

CEL turns the existing Cozy Solo/Connected Cozy and Downtime/Project systems into a directed game experience by composing MIB-13 economy, ICF production/foodcraft/alchemy, MIB-14 base/facility foundations, MIB-12 crafting and other owning domains. Cozy remains setting-independent and remains an orchestration experience, not a second rules engine.

The CEL loop is:

`Orient → choose meaningful goal/order/project → plan time/resources → perform or bounded-automate routine work → stop at decision/opportunity/constraint → commit owner-domain result → use/sell/trade outputs → pay costs/reinvest/improve → progress governed goals/options → summarize/continue`

### CEL tranche roadmap

| Tranche | State |
|---|---|
| CEL-01 — Goals, Routines & Cozy Life Loop Foundation | planned |
| CEL-02 — Personal Economy, Demand, Orders & Reinvestment Loop | planned |
| CEL-03 — Home/Base, Production, Hospitality & Resource Loop | planned |
| CEL-04 — Bounded Routine Automation & In-World Simulation | planned |
| CEL-05 — Opportunities, Complications, Relationships & Progression Hooks | planned |
| CEL-06 — Integrated Cozy Game Experience, Balance & Connected-Cozy Proof | planned |

### CEL automation and anti-aimlessness rules

CEL reuses existing APM Cozy automation: one-step, until-next-choice, bounded-batch and separately permitted bounded-background operations. Every step rechecks authorization, versions, resource/time/currency budgets and stop conditions. Automation stops for human/GM choices, consent, new unapproved costs, ownership changes, irreversible advancement, publication, stale/recovery conditions and other existing mandatory barriers.

Wall-clock elapsed time is not game progress by default. CEL may simulate explicitly authorized **in-world** Downtime blocks/routines where the owning rules define the time and effects.

A complete CEL experience must always expose a meaningful current goal, legal next actions, why those actions matter, an approaching decision or constraint, and an evidence-backed return summary. It must not rely on coercive streaks, punitive absence, fake urgency, meaningless click repetition or indefinite autonomous play.

## MIB tranche roadmap

| Tranche | State |
|---|---|
| MIB-01 through MIB-13 | completed_verified |
| MIB-14 — Vehicle, Platform and Base Engine Foundations | planned_after_icf |
| MIB-15 — AI Provider Abstraction, Fake Provider and Context/Proposal Pipeline | planned_after_cel |
| MIB-16 — Diagnostics, Provenance, Dependency and Search Engineering Surfaces | planned |
| MIB-17 — Family Safety Capability and Policy Foundation | planned |
| MIB-18 — Backbone Integration, Portability and Gated-Work Readiness Handoff | planned |

## Planned successor — SMB

SMB remains owner-approved post-MIB. **SMB-07 — Deep Cross-System Simulation** and **SMB-08 — Core Content Production** remain later expansion points; they consume ICF/CEL rather than reinventing the ingredient or Cozy life-loop foundations.

## Planned commercial preparation — MCB

MCB remains owner-approved planned commercial-preparation work and is not selected by this roadmap.

## Shared rules and preserved work

- Visibility filtering precedes aggregation/counts/search/AI/diagnostics/UI disclosure.
- Reference adapters are non-production and do not select providers.
- Migrations `0001`–`0021` are immutable; `0022` is not reserved and requires a demonstrated durable schema delta.
- Crafting mechanics reuse owning inventory/item/action/World authority; no second inventory/item/crafting truth ledger.
- Economy/trade mechanics remain in-game only and may not introduce real-money/payment integration.
- MIB-13 exposes safe owner-domain economy seams for later Downtime/Cozy consumers without granting those orchestration layers economy authority.
- ICF uses one canonical ingredient definition layer with domain profiles rather than separate Cooking and Alchemy ingredient ledgers.
- ICF creature harvest profiles reference canonical creature definitions and canonical output definitions; actual recovered outputs remain normal owner-domain Asset/inventory instances.
- Generic creature-part/type affinities are tendencies/proposal inputs, not authority to invent unsupported anatomy/lore.
- ICF harvestability does not imply edibility, legality, cultural acceptability, sapience treatment or safety.
- ICF preserves source provenance/terminology and explicitly reconciles conflicts/aliases rather than silently overwriting source data.
- **ICF-06 and ICF-07 remain protected; creature effect/crosswalk work is ICF-08 and ICF-09.**
- ICF long-running/repeated work reuses Downtime/Project semantics and can publish Cozy eligibility metadata without granting automation authority.
- CEL reuses APW Downtime/Projects, APM Cozy, MIB-13 economy, ICF, MIB-14 and other owning domains rather than creating parallel truth.
- CEL wall-clock time is not game progress by default; routine automation is bounded, deterministic and stops at meaningful authority/choice boundaries.
- CEL must create consequential goals/resource/economy/improvement feedback loops and avoid coercive or aimless engagement patterns.
- Optional AI remains non-authoritative; blocking paths and CEL core play pass without AI.
- Normal product acceptance is exact-head repository health + self-hosted Windows + self-hosted Linux + deterministic comparison where applicable. Governance/document-only AIOC work uses the registered repository-health exception rather than artificial product lanes.
- **CCTI-12-T04:** deferred until September 2026; PR #191 preserved and non-authoritative.
- **WP-011:** dormant pending required Apple/Mac environment; PR #61 preserved and non-authoritative.
- **DS-008:** blocked non-owner exact-byte transfer/validation.
- Tester distribution, release/deployment and paid-provider activation remain separately owner-gated.
- Product voice remains warm, knowledgeable, encouraging and restrained; never obsequious.
- Future family controls keep guardian authority distinct from GM/Campaign/private creative authority.

“Continue” from this state means execute **ICF-09** through its bounded completion gate. After ICF-09 is `completed_verified`, select **ICF-10** as `selected_not_started` without beginning it unless the owner continues further.
