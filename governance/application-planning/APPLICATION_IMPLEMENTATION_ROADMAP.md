# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.26.0  
**Status:** MIB ACTIVE AT MIB-13 — ICF OWNER-APPROVED INTERSTITIAL — SMB + MCB OWNER-APPROVED PLANNED  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-20

## Authority and operating rule

Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence. The strict APW/CSW/APM predecessor sequence remains **COMPLETED_VERIFIED**.

Approved forward programs:
1. **MIB — Multiversal Implementation Backbone** — active.
2. **ICF — Ingredient, Cultivation & Foodcraft Foundation** — owner-approved planned interstitial subproject after MIB-13 and before MIB-14.
3. **SMB — System Maturation & Buildout** — owner-approved planned post-MIB successor.
4. **MCB — Market Capture & Brand Backbone** — owner-approved planned commercial-preparation program; bounded early parallel work requires separate owner routing.

Roadmap presence does not auto-select ICF, SMB or MCB. **MIB-13 is the sole current implementation item.**

## MIB current state

Completed verified through MIB-12. Most recent completion:
- **MIB-12 — Crafting Deterministic Engine** — App PR #238; exact validated head `20d607a39d73085567bb44c7f5a6c4fb26ef33ec`; repository health `32349057025` PASS; Windows `96363989252` PASS; Linux `96363989039` PASS; deterministic comparison `96364257006` PASS; no timing retry; squash merge `9325cf5b1595853c77e07cd209ac1e08b6c4db90`; migration head remains `0021_apm_autogm_mini_campaign_director.json`; migration `0022` was neither created nor reserved.

Current:
- **MIB-13 — Economy and Trade Deterministic Engine**
- Attempt: `MIB-13-attempt-001`
- State: **selected_not_started**

MIB-13 covers currency definitions/conversion contracts, deterministic price/modifier pipelines, merchant/service availability, buy/sell/barter/trade validation, reservation/contract/settlement receipts, inventory/economy authority boundaries and deterministic local-market fixtures. Real-money/payment integration remains outside scope.

## Effective implementation order

MIB numbering remains stable, but the owner-approved ICF subproject is now a mandatory roadmap insertion after MIB-13 and before MIB-14:

`MIB-13 → ICF-01 → ICF-02 → ICF-03 → ICF-04 → ICF-05 → ICF-06 → ICF-07 → ICF-08 → ICF-09 → ICF-10 → ICF-11 → ICF-12 → ICF-13 → MIB-14 → MIB-15 → MIB-16 → MIB-17 → MIB-18`

MIB-14 does not begin until ICF is completed unless the owner explicitly re-routes the roadmap.

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
| **ICF-07 — Creature Harvest, Butchery & Biological Ingredient System** | **planned — added owner-approved tranche** |
| ICF-08 — Preparation, Processing & Derived Ingredients | planned |
| ICF-09 — Alchemical Ingredient Rules & Formula Grammar | planned |
| ICF-10 — Culinary & Magical Culinary Rules | planned |
| ICF-11 — Agriculture, Foraging, Husbandry & Production Integration | planned |
| ICF-12 — Recipe Corpus & Recipe-Generation Foundation | planned |
| ICF-13 — Content Packs, Validation, Search & Workbench | planned |

**Protected numbering rule:** the originally approved **ICF-06 remains Magical, Exotic & Multiversal Ingredients**. Creature harvesting/butchery does not replace it; that work is **ICF-07**.

### ICF architecture and scale

One canonical ingredient definition can carry physical, ecological/agricultural, economic, culinary, magical-culinary and alchemical profiles. Source-derived terminology/provenance stays traceable. Live inventory/Asset Instances remain owned by the existing inventory authority.

The first-party foundation targets approximately **700–1,000 primary ingredients** plus **300–500 derived preparations**, spanning mundane crops/plants, herbs/spices/fungi/forage, livestock/animal/aquatic outputs, basic reagents and magical/exotic/multiversal ingredients.

Any authored creature may expose a governed harvest profile through the existing creature `loot or harvest references` seam. Harvest profiles may produce canonical food, alchemical or crafting ingredients/materials; renewable harvests and post-mortem butchery/extraction are distinct. Yield/quality may account for creature biology/condition, cause of death, decomposition/contamination, tools/workstation, harvester knowledge/skill and procedure. Harvestability never silently grants edibility, legality, cultural acceptability or safety, and harvested outputs enter the normal owner-domain Asset/inventory system rather than a parallel creature-loot ledger.

## MIB tranche roadmap

| Tranche | State |
|---|---|
| MIB-01 through MIB-11 | completed_verified |
| **MIB-12 — Crafting Deterministic Engine** | **completed_verified** |
| **MIB-13 — Economy and Trade Deterministic Engine** | **selected_not_started** |
| MIB-14 — Vehicle, Platform and Base Engine Foundations | planned_after_icf |
| MIB-15 — AI Provider Abstraction, Fake Provider and Context/Proposal Pipeline | planned |
| MIB-16 — Diagnostics, Provenance, Dependency and Search Engineering Surfaces | planned |
| MIB-17 — Family Safety Capability and Policy Foundation | planned |
| MIB-18 — Backbone Integration, Portability and Gated-Work Readiness Handoff | planned |

## Planned successor — SMB

SMB remains owner-approved post-MIB. **SMB-08 — Core Content Production** remains the major later expansion point for broad first-party content; it will consume the ICF ingredient/recipe architecture rather than inventing a separate ingredient ontology.

## Planned commercial preparation — MCB

MCB remains owner-approved planned commercial-preparation work and is not selected by this roadmap change.

## Shared rules and preserved work

- Visibility filtering precedes aggregation/counts/search/AI/diagnostics/UI disclosure.
- Reference adapters are non-production and do not select providers.
- Migrations `0001`–`0021` are immutable; `0022` is not reserved and requires a demonstrated durable schema delta.
- Crafting mechanics reuse owning inventory/item/action/World authority; no second inventory/item/crafting truth ledger.
- Economy/trade mechanics remain in-game only and may not introduce real-money/payment integration.
- ICF uses one canonical ingredient definition layer with domain profiles rather than separate Cooking and Alchemy ingredient ledgers.
- ICF creature harvest profiles reference canonical creature definitions and canonical output definitions; actual recovered outputs remain normal owner-domain Asset/inventory instances.
- ICF harvestability does not imply edibility, legality, cultural acceptability, sapience treatment or safety.
- ICF preserves source provenance/terminology and explicitly reconciles conflicts/aliases rather than silently overwriting source data.
- **ICF-06 is protected as Magical, Exotic & Multiversal Ingredients; creature harvesting is ICF-07.**
- Optional AI remains non-authoritative; blocking paths pass without AI.
- Normal product acceptance is exact-head repository health + self-hosted Windows + self-hosted Linux + deterministic comparison where applicable.
- **CCTI-12-T04:** deferred until September 2026; PR #191 preserved.
- **WP-011:** dormant pending required Apple/Mac environment; PR #61 preserved.
- **DS-008:** blocked non-owner exact-byte transfer/validation.
- Tester distribution, release/deployment and paid-provider activation remain separately owner-gated.
- Product voice remains warm, knowledgeable, encouraging and restrained; never obsequious.
- Future family controls keep guardian authority distinct from GM/Campaign/private creative authority.

“Continue” from this state means execute **MIB-13** through its bounded completion gate. After MIB-13 is `completed_verified`, select and execute **ICF-01**; finish ICF-01 through ICF-13 before MIB-14 unless the owner explicitly changes the sequence.
