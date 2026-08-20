# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.27.0  
**Status:** MIB ACTIVE AT MIB-13 — ICF OWNER-APPROVED INTERSTITIAL — CEL OWNER-DIRECTED INTERSTITIAL — SMB + MCB OWNER-APPROVED PLANNED  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-20

## Authority and operating rule

Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence. The strict APW/CSW/APM predecessor sequence remains **COMPLETED_VERIFIED**.

Approved/directed forward programs:
1. **MIB — Multiversal Implementation Backbone** — active.
2. **ICF — Ingredient, Cultivation & Foodcraft Foundation** — owner-approved planned interstitial subproject after MIB-13 and before MIB-14.
3. **CEL — Cozy Economy & Life Loop** — owner-directed planned interstitial subproject after MIB-14 and before MIB-15.
4. **SMB — System Maturation & Buildout** — owner-approved planned post-MIB successor.
5. **MCB — Market Capture & Brand Backbone** — owner-approved planned commercial-preparation program; bounded early parallel work requires separate owner routing.

Roadmap presence does not auto-select ICF, CEL, SMB or MCB. **MIB-13 is the sole current implementation item.**

## MIB current state

Completed verified through MIB-12. Most recent completion:
- **MIB-12 — Crafting Deterministic Engine** — App PR #238; exact validated head `20d607a39d73085567bb44c7f5a6c4fb26ef33ec`; repository health `32349057025` PASS; Windows `96363989252` PASS; Linux `96363989039` PASS; deterministic comparison `96364257006` PASS; no timing retry; squash merge `9325cf5b1595853c77e07cd209ac1e08b6c4db90`; migration head remains `0021_apm_autogm_mini_campaign_director.json`; migration `0022` was neither created nor reserved.

Current:
- **MIB-13 — Economy and Trade Deterministic Engine**
- Attempt: `MIB-13-attempt-001`
- State: **selected_not_started**

MIB-13 covers currency definitions/conversion contracts, deterministic price/modifier pipelines, merchant/service availability, buy/sell/barter/trade validation, reservation/contract/settlement receipts, inventory/economy authority boundaries and deterministic local-market fixtures. It must expose safe owner-domain price/availability/cost/settlement/status seams that existing Downtime/APW and Cozy/APM orchestration can consume later without granting those layers economy or automation authority. Real-money/payment integration remains outside scope.

## Effective implementation order

MIB numbering remains stable, but the owner-approved ICF and owner-directed CEL subprojects are mandatory roadmap insertions unless the owner explicitly re-routes them:

`MIB-13 → ICF-01 → ICF-02 → ICF-03 → ICF-04 → ICF-05 → ICF-06 → ICF-07 → ICF-08 → ICF-09 → ICF-10 → ICF-11 → ICF-12 → ICF-13 → ICF-14 → ICF-15 → MIB-14 → CEL-01 → CEL-02 → CEL-03 → CEL-04 → CEL-05 → CEL-06 → MIB-15 → MIB-16 → MIB-17 → MIB-18`

MIB-14 does not begin until ICF is completed. CEL does not begin until MIB-14 is completed. MIB-15 does not begin until CEL is completed, unless the owner explicitly re-routes the roadmap.

## ICF — Ingredient, Cultivation & Foodcraft Foundation

**Program:** `governance/application-planning/ingredient-cultivation-foodcraft/ICF_INGREDIENT_CULTIVATION_FOODCRAFT_PROGRAM.md`  
**Backlog:** `governance/application-planning/ingredient-cultivation-foodcraft/ICF_PROGRAM_BACKLOG.json`  
**State:** owner-approved planned; not yet selected  
**Activation:** after MIB-13 completion  
**Resume MIB:** MIB-14 after ICF completion

ICF creates one canonical ingredient ecology shared by agriculture, foraging, livestock, creature harvesting/butchery, cooking, magical cooking, alchemy, medicine, ritual, crafting, trade and later base/settlement production. It consolidates the approved Cooking, Agriculture and Alchemy source packages, existing CSV/material/facility content, governed starter packs and creature harvest/loot references.

### ICF tranche roadmap

| Tranche | State |
|---|---|
| ICF-01 — Source Inventory & Reconciliation | planned |
| ICF-02 — Canonical Ingredient Schema & Taxonomy | planned |
| ICF-03 — Mundane Crop & Staple Plant Library | planned |
| ICF-04 — Herbs, Spices, Fungi & Wild Forage | planned |
| ICF-05 — Livestock, Animal & Aquatic Ingredient Library | planned |
| **ICF-06 — Magical, Exotic & Multiversal Ingredients** | **planned — protected original tranche** |
| **ICF-07 — Creature Harvest, Butchery & Biological Ingredient System** | **planned — protected approved tranche** |
| **ICF-08 — Creature Part Effect Taxonomy & Affinity Grammar** | **planned — added owner-approved tranche** |
| **ICF-09 — Creature Catalog Harvest Crosswalk & Signature Ingredient Library** | **planned — added owner-approved tranche** |
| ICF-10 — Preparation, Processing & Derived Ingredients | planned |
| ICF-11 — Alchemical Ingredient Rules & Formula Grammar | planned |
| ICF-12 — Culinary & Magical Culinary Rules | planned |
| ICF-13 — Agriculture, Foraging, Husbandry & Production Integration | planned |
| ICF-14 — Recipe Corpus & Recipe-Generation Foundation | planned |
| ICF-15 — Content Packs, Validation, Search & Workbench | planned |

**Protected numbering rule:** the originally approved **ICF-06 remains Magical, Exotic & Multiversal Ingredients** and **ICF-07 remains Creature Harvest, Butchery & Biological Ingredient System**. The new creature-part grammar and catalog crosswalk are ICF-08 and ICF-09; the former ICF-08 through ICF-13 shift to ICF-10 through ICF-15.

### ICF creature/effect architecture

Creature ingredients use the governed inheritance pattern:

`part baseline → body-plan/creature-type profile → creature affinity/trait profile → explicit species/variant override → harvested-instance quality/condition`

Broad part classes may define reusable culinary/alchemical/magical/crafting tendencies, but they do not authorize fabricated creature anatomy or lore. ICF-09 walks the actual governed creature catalog, produces explicit signature ingredients and substitutions where supported, and records coverage gaps where source evidence is insufficient.

### ICF Downtime/Cozy integration

Long-running or repeated cultivation, husbandry, gathering, harvesting, butchery, preservation, processing, cooking, brewing, alchemy and production reuse existing Downtime/Project activity semantics. ICF may publish Cozy-eligibility metadata for routine deterministic operations, but APM retains delegation/authorization/budget/stop-condition authority and wall-clock time does not become game progress by default.

### ICF architecture and scale

One canonical ingredient definition can carry physical, ecological/agricultural, economic, culinary, magical-culinary and alchemical profiles. Source-derived terminology/provenance stays traceable. Live inventory/Asset Instances remain owned by the existing inventory authority.

The first-party foundation targets approximately **700–1,000 primary ingredients** plus **300–500 derived preparations**, spanning mundane crops/plants, herbs/spices/fungi/forage, livestock/animal/aquatic outputs, basic reagents and magical/exotic/multiversal ingredients.

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
| MIB-01 through MIB-11 | completed_verified |
| **MIB-12 — Crafting Deterministic Engine** | **completed_verified** |
| **MIB-13 — Economy and Trade Deterministic Engine** | **selected_not_started** |
| MIB-14 — Vehicle, Platform and Base Engine Foundations | planned_after_icf |
| MIB-15 — AI Provider Abstraction, Fake Provider and Context/Proposal Pipeline | planned_after_cel |
| MIB-16 — Diagnostics, Provenance, Dependency and Search Engineering Surfaces | planned |
| MIB-17 — Family Safety Capability and Policy Foundation | planned |
| MIB-18 — Backbone Integration, Portability and Gated-Work Readiness Handoff | planned |

## Planned successor — SMB

SMB remains owner-approved post-MIB. **SMB-07 — Deep Cross-System Simulation** and **SMB-08 — Core Content Production** remain later expansion points; they consume ICF/CEL rather than reinventing the ingredient or Cozy life-loop foundations.

## Planned commercial preparation — MCB

MCB remains owner-approved planned commercial-preparation work and is not selected by this roadmap change.

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
- **ICF-06 and ICF-07 remain protected; new creature effect/crosswalk work is ICF-08 and ICF-09.**
- ICF long-running/repeated work reuses Downtime/Project semantics and can publish Cozy eligibility metadata without granting automation authority.
- CEL reuses APW Downtime/Projects, APM Cozy, MIB-13 economy, ICF, MIB-14 and other owning domains rather than creating parallel truth.
- CEL wall-clock time is not game progress by default; routine automation is bounded, deterministic and stops at meaningful authority/choice boundaries.
- CEL must create consequential goals/resource/economy/improvement feedback loops and avoid coercive or aimless engagement patterns.
- Optional AI remains non-authoritative; blocking paths and CEL core play pass without AI.
- Normal product acceptance is exact-head repository health + self-hosted Windows + self-hosted Linux + deterministic comparison where applicable.
- **CCTI-12-T04:** deferred until September 2026; PR #191 preserved.
- **WP-011:** dormant pending required Apple/Mac environment; PR #61 preserved.
- **DS-008:** blocked non-owner exact-byte transfer/validation.
- Tester distribution, release/deployment and paid-provider activation remain separately owner-gated.
- Product voice remains warm, knowledgeable, encouraging and restrained; never obsequious.
- Future family controls keep guardian authority distinct from GM/Campaign/private creative authority.

“Continue” from this state means execute **MIB-13** through its bounded completion gate. After MIB-13 is `completed_verified`, select and execute **ICF-01**; finish ICF-01 through ICF-15, then MIB-14, then CEL-01 through CEL-06 before MIB-15 unless the owner explicitly changes the sequence.
