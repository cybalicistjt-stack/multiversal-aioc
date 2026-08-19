# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.17.0  
**Status:** MIB ACTIVE AT MIB-04 — SMB + MCB OWNER-APPROVED PLANNED  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-19

## Authority and operating rule

Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence. Historical detail remains in Git history and completed checkpoints rather than being recopied into every roadmap revision.

The strict APW/CSW/APM 21-slice combined implementation sequence is **COMPLETED_VERIFIED** through APW-I07.

Approved forward programs:
1. **MIB — Multiversal Implementation Backbone** — active.
2. **SMB — System Maturation & Buildout** — owner-approved planned post-MIB successor.
3. **MCB — Market Capture & Brand Backbone** — owner-approved planned commercial-preparation program; bounded early parallel work requires separate owner routing.

Roadmap presence does not auto-select SMB or MCB. **MIB-04 is the sole current implementation item.**

## MIB current state

Completed verified:
- **MIB-01 — Canonical Registry, Data Dictionary and Stable Identity Foundation** — App PR #227, merge `8adff394bda40ca72dfd15bd459f98dae43a08c2`.
- **MIB-02 — Query, Index, Dependency and Search Projection Manifest** — App PR #228, merge `8173a4b589b2256dbac6ef5d8a485ea4b317eca0`.
- **MIB-03 — Deterministic Runtime Primitives Library** — App PR #229 exact validated head `81126a12e29cba8317b88328a5c7b326d991d05b`; repository health `32310944787` PASS; Windows `96254345413` PASS; Linux `96254343980` PASS after the one standing-policy unchanged A2 timing retry; deterministic comparison `96254443333` PASS; squash merge `618809b6fdbd7e2211ec37f65789ae9b3a601f65`; migration head remains `0021_apm_autogm_mini_campaign_director.json`; migration `0022` was not created or reserved.

Current:
- **MIB-04 — Adapter Compliance Kit and Reference Persistence Layer**
- Attempt: `MIB-04-attempt-001`
- State: **selected_not_started**
- Objective: provider-neutral persistence/query adapter contracts, deterministic non-production reference persistence, and one reusable compliance suite proving MIB-01 registry, MIB-02 query/visibility and MIB-03 runtime semantics without selecting a production provider.

## MIB tranche roadmap

| Tranche | State |
|---|---|
| MIB-01 — Canonical Registry, Data Dictionary and Stable Identity Foundation | completed_verified |
| MIB-02 — Query, Index, Dependency and Search Projection Manifest | completed_verified |
| MIB-03 — Deterministic Runtime Primitives Library | completed_verified |
| **MIB-04 — Adapter Compliance Kit and Reference Persistence Layer** | **selected_not_started** |
| MIB-05 — Content Pack Compiler, Linter, Importer and Starter Libraries | planned |
| MIB-06 — Fixture Factory, Golden Campaign and Performance Corpus | planned |
| MIB-07 — Multiversal UI Workbench and Shared Interaction Components | planned |
| MIB-08 — Integrity, Schema Compatibility and Migration Engineering Toolkit | planned |
| MIB-09 — Relationship and Reputation Engine | planned |
| MIB-10 — Investigation and Clue Graph Engine | planned |
| MIB-11 — World, Reality and Multiverse Taxonomy Engine | planned |
| MIB-12 — Crafting Deterministic Engine | planned |
| MIB-13 — Economy and Trade Deterministic Engine | planned |
| MIB-14 — Vehicle, Platform and Base Engine Foundations | planned |
| MIB-15 — AI Provider Abstraction, Fake Provider and Context/Proposal Pipeline | planned |
| MIB-16 — Diagnostics, Provenance, Dependency and Search Engineering Surfaces | planned |
| MIB-17 — Family Safety Capability and Policy Foundation | planned |
| MIB-18 — Backbone Integration, Portability and Gated-Work Readiness Handoff | planned |

Strict MIB order:
`MIB-01 → MIB-02 → MIB-03 → MIB-04 → MIB-05 → MIB-06 → MIB-07 → MIB-08 → MIB-09 → MIB-10 → MIB-11 → MIB-12 → MIB-13 → MIB-14 → MIB-15 → MIB-16 → MIB-17 → MIB-18`

## Planned successor — SMB

`SMB-01 Production Platform Realization → SMB-02 Remote Live Multiplayer & Presence → SMB-03 Organizations/Factions/Settlements/Kingdoms → SMB-04 Exploration/Travel/Survival → SMB-05 Full Base & Housing → SMB-06 Full Vehicle → SMB-07 Deep Cross-System Simulation → SMB-08 Core Content Production → SMB-09 Complete First-Party Campaign → SMB-10 Full Player/GM/Creator Product UX → SMB-11 Content Creation & Sharing Pipeline → SMB-12 Real Optional AI Integrations → SMB-13 Remote Internal Alpha Productization → SMB-14 Security/Privacy/Family Safety Hardening → SMB-15 Stabilization & Scale → SMB-16 Accessibility/Localization/Device Completion → SMB-17 External Beta & Community Foundations → SMB-18 Release Engineering & Commercial Productization`

Central SMB proof remains: four ordinary users on separate devices/locations can create/sign into accounts, join a Campaign, build/use Characters, play a complete live session, continue asynchronously, use major systems, recover from disconnects, and return later without developer intervention.

## Planned commercial preparation — MCB

`MCB-01 Market Definition/Category/Positioning → MCB-02 Customer Segment/Persona/JTBD Registry → MCB-03 Customer Research System → MCB-04 Competitive Intelligence & Market Observatory → MCB-05 Brand Strategy → MCB-06 Brand Identity System → MCB-07 Messaging Architecture → MCB-08 Claims/Proof/Evidence Registry → MCB-09 Product Demonstration & Media Capture → MCB-10 Website & Landing-Page Architecture → MCB-11 Search/SEO/Evergreen Content Knowledge Graph → MCB-12 Content Production Engine → MCB-13 Acquisition Channel Strategy & Experiment Library → MCB-14 Creator/GM/Influencer/Partner Network → MCB-15 Community Architecture → MCB-16 Waitlist/Alpha Recruitment/Audience Seeding → MCB-17 CRM/Lifecycle/Customer Communication → MCB-18 Analytics/Attribution/Experiment Registry → MCB-19 Pricing/Packaging/Value Architecture → MCB-20 Acquisition Economics & Market-Capture Model → MCB-21 Referral/Virality/Growth-Loop Design → MCB-22 Launch Narrative/PR/Press Kit → MCB-23 Trust/Privacy/AI/Family Communication → MCB-24 Launch Simulation & Commercial Readiness → MCB-25 Market-Capture & Expansion Playbook`

MCB must preserve hypothesis/evidence status and may not fabricate customers/testimonials/performance, make unsupported capability claims, lock final pricing, scale paid acquisition or launch publicly without required evidence and owner routing.

## Shared implementation/evidence rules

- Prefer registration, composition and adapters over foundational rewrites.
- Every common primitive has a named owner, contract tests and authority boundaries.
- Visibility filtering precedes aggregation, counts, search projection, AI context, diagnostics and support evidence.
- Stable operation identity, expected versions and durable owner receipts remain retry/recovery basis.
- Reference adapters are explicitly non-production and do not silently select production providers.
- Optional AI remains advisory/candidate only; blocking paths pass with AI disabled.
- Normal product acceptance is exact-head repository health + self-hosted Windows + self-hosted Linux + deterministic comparison where outputs should agree.
- Existing migrations `0001` through `0021` remain immutable; migration `0022` is not reserved and requires a demonstrated durable schema delta.
- No program may create a parallel Campaign, Session, Action, Event, Character, asset, relationship, investigation, World, Adventure, creator or automation truth ledger.

## Preserved/deferred work

- **CCTI-12-T04:** owner-deferred until September 2026; App PR #191 preserved.
- **WP-011:** dormant until required Apple/Mac environment exists; App PR #61 preserved.
- **DS-008:** blocked non-owner exact-byte transfer/validation.
- Tester distribution, release/deployment and paid-provider activation remain separately owner-gated.

## Product-wide approved concerns

- **TODO-UX-VOICE:** knowledgeable, creative companion; warm, welcoming, encouraging, clear and restrained; never obsequious.
- **TODO-FSF:** parental controls govern Multiversal-controlled capability/exposure; guardian authority remains distinct from GM/Campaign authority and does not imply access to private creative work.

“Continue” from this state means execute MIB-04 through its bounded completion gate before advancing to MIB-05. SMB and MCB remain planned until separately selected.
