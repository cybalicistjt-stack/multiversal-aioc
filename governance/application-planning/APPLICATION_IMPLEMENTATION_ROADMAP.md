# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.16.0  
**Status:** MIB ACTIVE AT MIB-03 — SMB + MCB OWNER-APPROVED PLANNED  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-19

## Authority and operating rule

Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence. Historical detail remains in Git history and completed checkpoints rather than being recopied into every roadmap revision.

The strict APW/CSW/APM 21-slice combined implementation sequence is **COMPLETED_VERIFIED** through APW-I07. The owner has explicitly approved three major forward programs:

1. **MIB — Multiversal Implementation Backbone** — active now; build reusable registries, indexes, runtime primitives, adapters, content tooling, fixtures, UI components, engineering tools and bounded engines.
2. **SMB — System Maturation & Buildout** — planned post-MIB product-completion successor; turn the MIB engine room into a complete networked, content-rich, production-grade game/app.
3. **MCB — Market Capture & Brand Backbone** — planned commercial-preparation program; build market truth, brand, acquisition, growth and launch machinery. Evidence-independent MCB tranches may later be selected in bounded parallel only through explicit owner routing.

Roadmap presence does **not** auto-select SMB or MCB. **MIB-03 is the sole current selected implementation item.**

## Completed verified baseline

Phase 9 through P9-06-023, DT-001–DT-010, Stage A A0–A12, Internal Alpha tester/GATX T01–T08, PPIA-01–16, CAPP-01–12, CCTI-01–11 plus CCTI-12 T01–T03, VCH-01–06, CRS-01–06, POST-GATX-SUCCESSOR and the full APW/APM/CSW design series are **COMPLETED_VERIFIED**.

The prior combined implementation sequence is also **COMPLETED_VERIFIED**:

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Final predecessor application evidence before MIB:
- App main: `ecbca5720f4ec2d9dc518a2d3ece8752b7dc9a9e`;
- migration head: `0021_apm_autogm_mini_campaign_director.json`;
- APW-I07 PR #226 exact validated head `eb9e7379d459e11617844706c2fba4ba85b25331`;
- repository-health run `32297933654` PASS;
- product run `32297933813` PASS on self-hosted Windows, self-hosted Linux and deterministic comparison.

## Approved program horizon

### MIB — technology/reusable implementation machine

Program: `governance/application-planning/multiversal-implementation-backbone/MIB_MULTIVERSAL_IMPLEMENTATION_BACKBONE_PROGRAM.md`  
Backlog: `governance/application-planning/multiversal-implementation-backbone/MIB_PROGRAM_BACKLOG.json`  
Lifecycle: **ACTIVE**  
Completed through: **MIB-02**  
Current tranche: **MIB-03**

### SMB — finished product/game machine

Program: `governance/application-planning/system-maturation-buildout/SMB_SYSTEM_MATURATION_AND_BUILDOUT_PROGRAM.md`  
Backlog: `governance/application-planning/system-maturation-buildout/SMB_PROGRAM_BACKLOG.json`  
Lifecycle: **OWNER-APPROVED / PLANNED POST-MIB SUCCESSOR**  
Default activation: after MIB-18 handoff unless separately rerouted by owner.

### MCB — market/brand/growth machine

Program: `governance/application-planning/market-capture-brand-backbone/MCB_MARKET_CAPTURE_AND_BRAND_BACKBONE_PROGRAM.md`  
Backlog: `governance/application-planning/market-capture-brand-backbone/MCB_PROGRAM_BACKLOG.json`  
Lifecycle: **OWNER-APPROVED / PLANNED COMMERCIAL PREPARATION**  
Parallel rule: evidence-independent early tranches may later be selected in bounded parallel by explicit owner routing; product-dependent claims/pricing/acquisition/launch work must wait for current evidence.

## Active subproject — MIB

### MIB-01 completion evidence

**MIB-01 — Canonical Registry, Data Dictionary and Stable Identity Foundation** is **COMPLETED_VERIFIED**.

- App PR #227 exact validated head: `15ac2f4ebf4b43967d689f30e9dab1636ec45db2`;
- repository-health run `32307639280`: PASS;
- product run `32307639514`: PASS;
- self-hosted Windows job `96243767363`: PASS;
- self-hosted Linux job `96243767526`: PASS;
- deterministic comparison job `96244131477`: PASS;
- squash merge: `8adff394bda40ca72dfd15bd459f98dae43a08c2`;
- migration head remains `0021_apm_autogm_mini_campaign_director.json`;
- migration `0022` was not created or reserved.

MIB-01 implemented a provider-neutral deterministic identity/reference facade rather than a second persistence ledger. Reusable definitions/templates/variants are registerable; live instances, snapshots and projections are explicitly not registry truth. Runtime Campaign/install context is not promoted into reusable identity.

### MIB-02 completion evidence

**MIB-02 — Query, Index, Dependency and Search Projection Manifest** is **COMPLETED_VERIFIED**.

- App PR #228 exact validated head: `7423759b228456dc8f17f8aa1526e788719aa432`;
- repository-health run `32309548444`: PASS;
- product run `32309548641`: PASS;
- self-hosted Windows job `96249530958`: PASS;
- self-hosted Linux job `96249530833`: PASS;
- deterministic comparison job `96249747913`: PASS;
- squash merge: `8173a4b589b2256dbac6ef5d8a485ea4b317eca0`;
- migration head remains `0021_apm_autogm_mini_campaign_director.json`;
- migration `0022` was not created or reserved.

MIB-02 established ten common logical query families over existing owner-domain records/index evidence: stable ID/version, reverse dependency, tag/category/text search, asset owner/control/location, relationship adjacency, investigation adjacency, World hierarchy/semantic location, Adventure graph/dependency, operation/status/Event cursor and source/provenance. Authorization/visibility filtering is performed before search-document construction, counts, facets, graph topology and cursor page sizing; hidden/global corpus cardinality is not exposed. The shared facade consumes MIB-01 identity and does not mutate or replay owner-domain truth.

### Current MIB operation

**MIB-03 — Deterministic Runtime Primitives Library**  
Attempt: `MIB-03-attempt-001`  
State: **selected_not_started**

MIB-03 must inventory the repeated deterministic runtime seams already present across A6/A7/A8/A9/A10/APW/APM/CSW and consolidate the smallest stable reusable library for operation identity, expected-version conflicts, idempotent replay, reservations, state transitions, Events/receipts, projections, authorization rechecks, provenance, recovery cursors, canonical serialization/hashing, dependency resolution, safe retry and replay verification. It must preserve owner-domain legality/mutation authority and may not force completed domains through incompatible rewrites merely to claim abstraction reuse.

### MIB tranche roadmap

| Tranche | Purpose | State |
|---|---|---|
| MIB-01 — Canonical Registry, Data Dictionary and Stable Identity Foundation | Establish one provider-neutral registration/data vocabulary for reusable definitions, versions, lifecycle, provenance, dependencies, tags and visibility. | **completed_verified** |
| MIB-02 — Query, Index, Dependency and Search Projection Manifest | Define one logical retrieval/index/search vocabulary, reverse-reference model and visibility-safe query projection before physical provider selection. | **completed_verified** |
| **MIB-03 — Deterministic Runtime Primitives Library** | Consolidate stable operations, expected versions, idempotency, reservations, receipts, deterministic hashing/serialization, recovery and replay primitives. | **selected_not_started** |
| MIB-04 — Adapter Compliance Kit and Reference Persistence Layer | Create storage/query interfaces, common compliance tests and deterministic reference adapters so future providers plug in without domain rewrites. | planned |
| MIB-05 — Content Pack Compiler, Linter, Importer and Starter Libraries | Make content data-driven with deterministic pack builds, validation and governed starter libraries. | planned |
| MIB-06 — Fixture Factory, Golden Campaign and Performance Corpus | Build reusable small/medium/large fixtures and the permanent Haunted Lighthouse whole-system golden Campaign. | planned |
| MIB-07 — Multiversal UI Workbench and Shared Interaction Components | Implement reusable responsive/accessibility-equivalent components and recurrent screen patterns from the UI/Screen Design Bibles. | planned |
| MIB-08 — Integrity, Schema Compatibility and Migration Engineering Toolkit | Detect broken references, schema drift, incompatible changes and migration/replay defects before production provider choices. | planned |
| MIB-09 — Relationship and Reputation Engine | Turn D25 relationship/reputation designs into deterministic attributable gameplay logic and role-safe projections. | planned |
| MIB-10 — Investigation and Clue Graph Engine | Turn D24 investigation/clue structures into a real deterministic graph/reveal/search engine with graphical/nonvisual parity. | planned |
| MIB-11 — World, Reality and Multiverse Taxonomy Engine | Implement Multiverse/Branch/Reality/Timeline classification, compatibility profiles and semantic World navigation/search. | planned |
| MIB-12 — Crafting Deterministic Engine | Implement Recipe/Material/Workstation/Modification/Crafting Job rules with deterministic reservations, output and recovery. | planned |
| MIB-13 — Economy and Trade Deterministic Engine | Implement currencies, price pipelines, merchants, trade/service contracts and settlement without real-money dependencies. | planned |
| MIB-14 — Vehicle, Platform and Base Engine Foundations | Implement vehicle/base definitions, module/facility compatibility, capacity, crew, resources, maintenance, upgrade and loadout rules. | planned |
| MIB-15 — AI Provider Abstraction, Fake Provider and Context/Proposal Pipeline | Finish provider-neutral AI integration against a deterministic fake provider while preserving no-AI blocking paths and non-authoritative AI. | planned |
| MIB-16 — Diagnostics, Provenance, Dependency and Search Engineering Surfaces | Build provenance/audit, reverse-dependency, operation/recovery and visibility-safe search engineering surfaces. | planned |
| MIB-17 — Family Safety Capability and Policy Foundation | Prepare deterministic product-controlled parental/family capability policies while keeping guardian authority distinct from Campaign/GM/private creator authority. | planned |
| MIB-18 — Backbone Integration, Portability and Gated-Work Readiness Handoff | Integrate MIB and package portable contracts, fixtures, validation evidence and readiness checklists for currently unavailable environments/providers/distribution work. | planned |

Strict MIB order:

`MIB-01 → MIB-02 → MIB-03 → MIB-04 → MIB-05 → MIB-06 → MIB-07 → MIB-08 → MIB-09 → MIB-10 → MIB-11 → MIB-12 → MIB-13 → MIB-14 → MIB-15 → MIB-16 → MIB-17 → MIB-18`

The first eight tranches deliberately maximize leverage for everything after them. Later MIB tranches must consume the common registry/index/runtime/adapter/content/fixture/UI/tooling foundations rather than inventing competing one-off equivalents.

## Planned successor — SMB

**SMB — System Maturation & Buildout** is the owner-approved product-completion successor to MIB.

| Tranche | Purpose | State |
|---|---|---|
| SMB-01 — Production Platform Realization | Select and implement production persistence/search/identity/hosting/synchronization adapters through MIB contracts. | planned |
| SMB-02 — Remote Live Multiplayer & Presence | Reliable geographically separated live/async/hybrid play, invitations, presence, reconnect and cross-device continuity. | planned |
| SMB-03 — Organizations, Factions, Settlements & Kingdoms | Complete large social/political simulation using relationship/reputation/event foundations. | planned |
| SMB-04 — Exploration, Travel & Survival | Complete travel, discovery, environments, navigation, survival, fog-of-war and encounter workflows. | planned |
| SMB-05 — Full Base & Housing System | Finish construction, ownership, facilities, storage, workforce, production, defense, utilities and upgrades. | planned |
| SMB-06 — Full Vehicle System | Finish travel, crew stations, cargo, resources, damage, maintenance, repair, upgrades and combat-support vehicle workflows. | planned |
| SMB-07 — Deep Cross-System Simulation | Connect domains so relationships, factions, economies, travel, crafting, investigation, bases, Adventures and Worlds produce governed consequences. | planned |
| SMB-08 — Core Content Production | Create substantial first-party governed game libraries, Worlds and Adventures using MIB content tooling. | planned |
| SMB-09 — Complete First-Party Campaign | Produce a polished real campaign exercising Multiversal end to end rather than merely a QA fixture. | planned |
| SMB-10 — Full Player / GM / Creator Product UX | Complete production-facing screens/workflows across major Player, GM, Personal and creator activities. | planned |
| SMB-11 — Content Creation & Sharing Pipeline | Complete private/controlled export, import, dependencies, versions, forks/remixes, provenance and sharing. | planned |
| SMB-12 — Real Optional AI Integrations | Connect approved live AI providers through MIB-15 while preserving no-AI and non-authoritative operation. | planned |
| SMB-13 — Remote Internal Alpha Productization | Make non-developer remote installation, onboarding, guided testing, evidence capture, diagnostics and updating frictionless. | planned |
| SMB-14 — Security, Privacy & Family Safety Hardening | Connect policy foundations to real account/platform infrastructure and audit security/privacy/family boundaries. | planned |
| SMB-15 — Stabilization & Scale | Stress large/long-lived Campaigns, Worlds, histories, content packs, network degradation, storage/search and migration performance. | planned |
| SMB-16 — Accessibility, Localization & Device Completion | Complete accessibility, localization, screen classes and Apple/Mac/device support where environments exist. | planned |
| SMB-17 — External Beta & Community Foundations | Support controlled external beta, private groups, moderation foundations, creator sharing and feedback/support systems. | planned |
| SMB-18 — Release Engineering & Commercial Productization | Packaging, approved billing/entitlements, operations, backups, observability, support, release channels, rollback, stores/distribution and launch readiness. | planned |

Default SMB sequence:

`SMB-01 → SMB-02 → SMB-03 → SMB-04 → SMB-05 → SMB-06 → SMB-07 → SMB-08 → SMB-09 → SMB-10 → SMB-11 → SMB-12 → SMB-13 → SMB-14 → SMB-15 → SMB-16 → SMB-17 → SMB-18`

Central SMB product proof: four ordinary users on separate devices/locations can create/sign into accounts, join a Campaign, build/use Characters, play a complete live session, continue asynchronously, exercise major game systems, recover from disconnects, return later and resume from the same authoritative history without developer intervention.

## Planned commercial preparation — MCB

**MCB — Market Capture & Brand Backbone** is the owner-approved commercial-preparation series. No MCB tranche is active now.

### Market truth

| Tranche | Purpose | State |
|---|---|---|
| MCB-01 — Market Definition, Category & Strategic Positioning | Define beachhead category, substitutes, differentiation, expansion path and defensibility. | planned |
| MCB-02 — Customer Segment, Persona & Jobs-to-be-Done Registry | Build structured segment/job/pain/trigger/outcome/objection/alternative/value/acquisition models. | planned |
| MCB-03 — Customer Research System | Build reusable interview, survey, concept, pricing and churn research with evidence scoring/repository. | planned |
| MCB-04 — Competitive Intelligence & Market Observatory | Maintain structured competitor/substitute positioning, pricing, channel, product and strategic-change intelligence. | planned |

### Brand

| Tranche | Purpose | State |
|---|---|---|
| MCB-05 — Multiversal Brand Strategy | Define promise, personality, emotional territory, vocabulary and trust/AI/family/creator language. | planned |
| MCB-06 — Brand Identity System | Define reusable logo, typography, color, imagery, iconography, media, social, press and presentation rules. | planned |
| MCB-07 — Messaging Architecture | Build canonical audience × problem × capability × benefit × emotional payoff × proof × CTA messaging. | planned |
| MCB-08 — Claims, Proof & Evidence Registry | Tie public claims to approved wording, evidence, limitations, proof strength and verification dates. | planned |
| MCB-09 — Product Demonstration & Media Capture System | Produce deterministic demo states and repeatable screenshot/video capture workflows. | planned |

### Acquisition infrastructure

| Tranche | Purpose | State |
|---|---|---|
| MCB-10 — Website & Landing-Page Architecture | Build reusable marketing-site/landing-page structures before final launch copy. | planned |
| MCB-11 — Search, SEO & Evergreen Content Knowledge Graph | Map search intent, audience, topics, content, product capabilities and calls to action. | planned |
| MCB-12 — Content Production Engine | Build reusable article/video/short/newsletter/guide/social production and repurposing workflows. | planned |
| MCB-13 — Acquisition Channel Strategy & Experiment Library | Define channel hypotheses, creative/landing tests, metrics and success/kill thresholds before significant spend. | planned |
| MCB-14 — Creator, GM, Influencer & Partner Network | Build a relationship registry for creators, reviewers, educators, publishers, conventions and advocates. | planned |
| MCB-15 — Community Architecture | Design community spaces, moderation, support/social separation, spoilers, ownership, family boundaries and recognition. | planned |
| MCB-16 — Waitlist, Alpha Recruitment & Audience Seeding | Prepare segmented recruitment/waitlist systems that support testing and market learning. | planned |

### Growth economics

| Tranche | Purpose | State |
|---|---|---|
| MCB-17 — CRM, Lifecycle & Customer Communication Model | Define visitor→interest→waitlist→invite→activation→Campaign→retention→advocate lifecycle and communications. | planned |
| MCB-18 — Analytics, Attribution & Experiment Registry | Define canonical funnels, events, attribution/UTM standards and evidence-backed experiment records. | planned |
| MCB-19 — Pricing, Packaging & Value Architecture | Research product value boundaries and pricing/packaging hypotheses without prematurely locking final prices. | planned |
| MCB-20 — Acquisition Economics & Market-Capture Model | Model CAC, activation, conversion, churn, retention, ARPU, referrals, creator acquisition and GM→Player invitation economics. | planned |
| MCB-21 — Referral, Virality & Growth-Loop Design | Design value-first Campaign invitation and creator-sharing loops without spam/dark patterns. | planned |

### Launch / market capture

| Tranche | Purpose | State |
|---|---|---|
| MCB-22 — Launch Narrative, PR & Press Kit | Prepare founder/launch narrative, press FAQ, fact sheet, media kit, review guide and announcement materials. | planned |
| MCB-23 — Trust, Privacy, AI & Family Communication | Turn privacy, ownership, AI boundaries, Campaign privacy and family safety into clear customer communication. | planned |
| MCB-24 — Launch Simulation & Commercial Readiness | Run synthetic end-to-end commercial cohorts before real-scale acquisition/launch. | planned |
| MCB-25 — Market-Capture & Expansion Playbook | Convert validated evidence into deliberate beachhead→adjacency expansion strategy. | planned |

Default MCB sequence:

`MCB-01 → MCB-02 → MCB-03 → MCB-04 → MCB-05 → MCB-06 → MCB-07 → MCB-08 → MCB-09 → MCB-10 → MCB-11 → MCB-12 → MCB-13 → MCB-14 → MCB-15 → MCB-16 → MCB-17 → MCB-18 → MCB-19 → MCB-20 → MCB-21 → MCB-22 → MCB-23 → MCB-24 → MCB-25`

MCB must distinguish hypothesis from evidence. It may prepare research/brand/acquisition systems before the product is finished, but it may not fabricate customers/testimonials/performance, make unsupported capability claims, lock final pricing, scale paid acquisition or launch publicly without the necessary evidence and owner routing.

## Shared implementation and evidence rules

- Prefer registrations, composition and adapters over foundational rewrites.
- Every common primitive must have a named owner, contract tests and explicit authority boundaries.
- Visibility filtering happens before aggregation, counts, search projection, AI context, diagnostics or support evidence.
- Stable operation identity, expected-version checks and durable owner-domain receipts remain the basis of retries/recovery.
- Reference adapters are non-production test/reference implementations and must not silently select a production provider.
- Starter content is governed data with stable identity/version/provenance rather than code-hardcoded game truth.
- UI Workbench components must expose equivalent keyboard/touch/screen-reader/nonvisual state.
- Optional AI remains candidate/advisory only and all blocking paths must pass with AI disabled.
- Cross-platform deterministic evidence remains the default final product gate where outputs should agree.
- Commercial hypotheses, research findings, product claims, pricing assumptions and growth conclusions must retain their evidence status rather than being promoted by repetition.

## Migration and ownership policy

- migrations `0001` through `0021` are immutable predecessors;
- migration `0022` does not exist and is not reserved;
- each selected implementation tranche rechecks current App main/migration head once before mutation;
- a future migration requires a demonstrated durable schema delta, not merely a new library, query manifest, fixture, UI component or reference adapter;
- no future program may absorb Campaign, Session, Action, Event, Character, asset, relationship, investigation, World, Adventure, creator or automated-play truth into a parallel ledger;
- provider-neutral logical contracts remain authoritative until a later separately authorized production-provider decision.

## Preserved/deferred work

- **CCTI-12-T04:** owner-deferred until September 2026; preserve App PR #191 and branches. It does not preempt MIB before its routing condition.
- **WP-011:** dormant until the required special Mac/Apple environment is available.
- **DS-008:** blocked non-owner exact-byte transfer/validation; never reconstruct checksum-bound bytes from excerpts, OCR or memory.
- **Tester distribution:** remains separately owner-gated.
- **Release/deployment:** remains unauthorized absent separate owner routing.
- **Paid-provider activation:** remains separately owner-gated.

MIB-18 specifically prepares portable contracts, fixtures, evidence packages and readiness checklists for these constraints where that preparation is safe, but it does not bypass them. SMB/MCB roadmap planning likewise does not bypass them.

## Permanent validation rules

Only evidence-backed `completed_verified` is complete. A failed required gate leaves work unfinished. Normal App/package acceptance is self-hosted Windows + self-hosted Linux + deterministic comparison where outputs should agree, plus exact-head repository health. AIOC repository health validates governance state; it does not substitute for product validation.

## Product-wide approved concerns

- **TODO-UX-VOICE:** knowledgeable, creative companion; warm, welcoming, encouraging, clear, confident and restrained; never obsequious. MIB-07 incorporates this into reusable shared UI/copy primitives; MCB-05 through MCB-07 extend the same identity into public brand and messaging.
- **TODO-FSF:** parental controls govern Multiversal-controlled capability/exposure; guardian authority remains distinct from GM/Campaign authority and does not imply access to private creative work. MIB-17 creates the implementation foundation; SMB-14 hardens it against production infrastructure; MCB-23 makes the customer-facing trust model understandable.

## Nonauthorization

Roadmap approval of MIB/SMB/MCB does not authorize CCTI-12-T04 before September 2026, WP-011 without its environment, DS-008 byte reconstruction, tester distribution, release/deployment, paid-provider activation, public matchmaking/community publishing, broad offline authoritative mutation, real-money integration, unsupported marketing claims, binding final pricing or AI mechanical/canonical/permission/consent/adjudication authority.

“Continue” from this state means execute the next verified unfinished MIB operation, beginning with MIB-03, and continue through its bounded completion gate before advancing according to the canonical selector. SMB and MCB remain roadmap-planned until separately selected by owner routing.
