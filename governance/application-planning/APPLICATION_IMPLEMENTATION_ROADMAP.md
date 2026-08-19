# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.13.0  
**Status:** MIB — MULTIVERSAL IMPLEMENTATION BACKBONE ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-19

## Authority and operating rule

Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence. Historical detail remains in Git history and completed checkpoints rather than being recopied into every roadmap revision.

The strict APW/CSW/APM 21-slice combined implementation sequence is **COMPLETED_VERIFIED** through APW-I07. The owner has now explicitly approved **MIB — Multiversal Implementation Backbone** as the active next subproject. MIB is an implementation-accelerator series over the completed architecture: shared registries, indexes, runtime primitives, adapters, content tooling, fixtures, UI components, engineering tools and bounded domain engines that reduce future feature work to registration, composition and adapter-specific implementation wherever possible.

## Completed verified baseline

Phase 9 through P9-06-023, DT-001–DT-010, Stage A A0–A12, Internal Alpha tester/GATX T01–T08, PPIA-01–16, CAPP-01–12, CCTI-01–11 plus CCTI-12 T01–T03, VCH-01–06, CRS-01–06, POST-GATX-SUCCESSOR and the full APW/APM/CSW design series are **COMPLETED_VERIFIED**.

The prior combined implementation sequence is also **COMPLETED_VERIFIED**:

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Final predecessor application evidence:
- App main: `ecbca5720f4ec2d9dc518a2d3ece8752b7dc9a9e`;
- migration head: `0021_apm_autogm_mini_campaign_director.json`;
- APW-I07 PR #226 exact validated head `eb9e7379d459e11617844706c2fba4ba85b25331`;
- repository-health run `32297933654` PASS;
- product run `32297933813` PASS on self-hosted Windows, self-hosted Linux and deterministic comparison;
- 25 focused APW-I07 tests PASS.

## Active next subproject — MIB

**MIB — Multiversal Implementation Backbone** is the sole active product implementation program.

Program: `governance/application-planning/multiversal-implementation-backbone/MIB_MULTIVERSAL_IMPLEMENTATION_BACKBONE_PROGRAM.md`  
Backlog: `governance/application-planning/multiversal-implementation-backbone/MIB_PROGRAM_BACKLOG.json`  
Current tranche: **MIB-01**  
Attempt: `MIB-01-attempt-001`  
State: `selected_not_started`

### MIB tranche roadmap

| Tranche | Purpose | State |
|---|---|---|
| **MIB-01 — Canonical Registry, Data Dictionary and Stable Identity Foundation** | Establish one provider-neutral registration/data vocabulary for reusable definitions, versions, lifecycle, provenance, dependencies, tags and visibility. | **selected_not_started** |
| MIB-02 — Query, Index, Dependency and Search Projection Manifest | Define one logical retrieval/index/search vocabulary, reverse-reference model and visibility-safe query projection before physical provider selection. | planned |
| MIB-03 — Deterministic Runtime Primitives Library | Consolidate stable operations, expected versions, idempotency, reservations, receipts, deterministic hashing/serialization, recovery and replay primitives. | planned |
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

### Strict MIB execution order

`MIB-01 → MIB-02 → MIB-03 → MIB-04 → MIB-05 → MIB-06 → MIB-07 → MIB-08 → MIB-09 → MIB-10 → MIB-11 → MIB-12 → MIB-13 → MIB-14 → MIB-15 → MIB-16 → MIB-17 → MIB-18`

The first eight tranches deliberately maximize leverage for everything after them. Later MIB tranches must consume the common registry/index/runtime/adapter/content/fixture/UI/tooling foundations rather than inventing competing one-off equivalents.

## MIB-01 current operation

MIB-01 must begin by re-fetching App main and migration head and inventorying live reusable-definition/reference seams across existing domains. It then implements the smallest canonical Registry/Data Dictionary foundation supported by those seams.

Required MIB-01 boundaries:
- reusable definitions remain distinct from live instances, templates, Campaign variants and projections;
- stable IDs, versions, lifecycle, source, provenance, dependencies, tags and visibility metadata have one common contract;
- registry resolution may reference owner-domain objects but may not copy their live truth into a new ledger;
- deterministic serialization/checksum behavior is cross-platform;
- migration `0022` is added only if live inspection proves a genuine durable schema delta; it is not reserved by the MIB program;
- no production database/search/AI provider is selected;
- no AI is required for blocking acceptance;
- normal exact-head repository health and self-hosted Windows/Linux/deterministic validation remain required before merge.

## MIB shared implementation rules

- Prefer registrations, composition and adapters over foundational rewrites.
- Every common primitive must have a named owner, contract tests and explicit authority boundaries.
- Visibility filtering happens before aggregation, counts, search projection, AI context, diagnostics or support evidence.
- Stable operation identity, expected-version checks and durable owner-domain receipts remain the basis of retries/recovery.
- Reference adapters are non-production test/reference implementations and must not silently select a production provider.
- Starter content is governed data with stable identity/version/provenance rather than code-hardcoded game truth.
- UI Workbench components must expose equivalent keyboard/touch/screen-reader/nonvisual state.
- Optional AI remains candidate/advisory only and all blocking paths must pass with AI disabled.
- Cross-platform deterministic evidence remains the default final product gate where outputs should agree.

## Migration and ownership policy

- migrations `0001` through `0021` are immutable predecessors;
- migration `0022` does not exist and is not reserved;
- each MIB tranche rechecks current App main/migration head once before mutation;
- a future migration requires a demonstrated durable schema delta, not merely a new library, query manifest, fixture, UI component or reference adapter;
- MIB may not absorb Campaign, Session, Action, Event, Character, asset, relationship, investigation, World, Adventure, creator or automated-play truth into a parallel ledger;
- provider-neutral logical contracts remain authoritative until a later separately authorized production-provider decision.

## Preserved/deferred work

- **CCTI-12-T04:** owner-deferred until September 2026; preserve App PR #191 and branches. It does not preempt MIB before its routing condition.
- **WP-011:** dormant until the required special Mac/Apple environment is available.
- **DS-008:** blocked non-owner exact-byte transfer/validation; never reconstruct checksum-bound bytes from excerpts, OCR or memory.
- **Tester distribution:** remains separately owner-gated.
- **Release/deployment:** remains unauthorized absent separate owner routing.
- **Paid-provider activation:** remains separately owner-gated.

MIB-18 specifically prepares portable contracts, fixtures, evidence packages and readiness checklists for these constraints where that preparation is safe, but it does not bypass them.

## Permanent validation rules

Only evidence-backed `completed_verified` is complete. A failed required gate leaves work unfinished. Normal App/package acceptance is self-hosted Windows + self-hosted Linux + deterministic comparison where outputs should agree, plus exact-head repository health. AIOC repository health validates governance state; it does not substitute for product validation.

## Product-wide approved concerns

- **TODO-UX-VOICE:** knowledgeable, creative companion; warm, welcoming, encouraging, clear, confident and restrained; never obsequious. MIB-07 incorporates this into reusable shared UI/copy primitives.
- **TODO-FSF:** parental controls govern Multiversal-controlled capability/exposure; guardian authority remains distinct from GM/Campaign authority and does not imply access to private creative work. MIB-17 is the implementation foundation for this concern.

## Nonauthorization

MIB activation does not authorize CCTI-12-T04 before September 2026, WP-011 without its environment, DS-008 byte reconstruction, tester distribution, release/deployment, paid-provider activation, public matchmaking/community publishing, broad offline authoritative mutation, real-money integration, production provider selection, or AI mechanical/canonical/permission/consent/adjudication authority.

“Continue” from this state means execute the next verified unfinished MIB operation, beginning with MIB-01, and continue through its bounded completion gate before advancing to MIB-02.
