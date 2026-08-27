# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-06 selected_not_started  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-05  
**Current item:** AAI-06 — Import/Link Framework & Initial Provider Adapters  
**Implementation branch:** none  
**Implementation authority:** none; AAI-06 selection/planning resolution only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 through AAI-05 are `completed_verified`.

AAI-05 application PR #329 exact head `22ed48f92ee72be2e136e780e24236dd37e2fb4d` passed Repository Health run `33030607196` / job `98382007560`, self-hosted Linux AAI-05 Validation Core job `98382008814`, self-hosted Windows job `98382008826`, AAI-04, AAI-03, AAI-02, AAI-01 and MIB-11/D18 regressions, and deterministic comparison job `98384564046` with receipt `7e55e9ed29f8fefb42ab8244cafed057631f5cf8c63efee0b95a29d1d668b85e`. Linux artifact `9630182458` has digest `sha256:d0b31b60d56955f260c26fe7e07fd1237073e50c2d69a9504d66fcd91d44b3c6`; Windows artifact `9630359600` has digest `sha256:49e8bedd7a1828caeefcf1bc490d42636eaa953d1879d619bfd233b84a6fdb14`; comparison artifact `9630372033` has digest `sha256:c8bd25426416fe37163668329edacb75a87b7d91c0862837c83f2242a2dc999a`. The exact validated head then squash-merged as `511f9566af10f0defa703350ac4ffa6db0c0c4e7`. Application repair cycles: **0**.

The AAI-05 closeout repairs a governance projection inconsistency from its governed start: the checkpoint, pointer, registry and backlog were correctly moved to `in_progress`, while this CURRENT program prose remained at `selected_not_started`. That stale prose did not change application authority, implementation head or validation evidence and is corrected by this closeout.

The strict successor **AAI-06 — Import/Link Framework & Initial Provider Adapters** is now `selected_not_started`. It has no implementation branch and no implementation authority. Selection authorizes only future fresh-read contract resolution after another owner `Continue`; it does not authorize provider-specific adapter code, authentication, live catalogs/provider calls, provider content acquisition/copying/caching, scraping/reverse engineering, payment, migration `0022`, tester distribution, release or deployment.

## Purpose

AAI makes external and user-owned audio usable through one provider-neutral Multiversal layer without requiring Multiversal to own, copy or redistribute commercial audio. Audio intent remains separate from provider identity and selected provider asset/reference, and audio remains presentation/support state rather than canonical gameplay truth.

## Completed foundation

### AAI-01 — ecosystem, API, license and authority

AAI-01 established evidence states and provider/license boundaries. Unsupported, undocumented, provider-contact-required and unknown evidence remains explicit and fail closed; no provider/catalog is canonical; local possession does not imply redistribution, public-performance or commercial rights; scraping/reverse engineering workarounds remain prohibited.

### AAI-02 — canonical audio identities and rights

AAI-02 established provider-neutral provider/source/asset/music/ambience/one-shot/soundscape/cue/mix/playlist/reference/intent identities and explicit rights for reference, ingest, play, embed, cache, export, record, stream, redistribute and transform. Provider-native IDs remain separate from Multiversal identity and semantic intent. `unknown` rights are never allowed; unresolved, silent and manual-reference cues remain first-class.

### AAI-03 — provider adapter and capability negotiation

AAI-03 established provider-neutral adapter descriptors and evidence-driven capability negotiation. Only supported-documented and supported-user-controlled evidence is usable. Capability evidence never overrides AAI-02 rights; manual external-reference outcomes remain manual.

### AAI-04 — playback, layering and mixer

AAI-04 established provider-neutral playback/layer/mixer outcomes and deterministic state/receipts. Every audible asset remains rights/capability gated, local playback requires explicit runtime media-probe evidence, and silent/unresolved/manual/unavailable/degraded outcomes remain nonblocking. Provider-specific live transport remains later authority.

### AAI-05 — semantic taxonomy and availability resolver

AAI-05 establishes provider-neutral semantic normalization/matching/ranking over existing AAI-02 intent and asset semantic evidence, with provider identity excluded as a ranking signal. Candidate selection requires independent semantic compatibility, AAI-02 rights/provenance, AAI-03 capability and explicit runtime availability evidence. Unknown, denied, unavailable or incompatible evidence fails closed. Manual-reference and silent cues remain explicit; resolver output selects only an existing asset ID or null and never mutates canonical cues or gameplay owners.

AAI-05 introduced no provider authentication, live catalog/provider call, content acquisition/copying/caching, scraping/reverse engineering workaround, payment, recording/streaming automation, gameplay owner mutation or durable schema. Migration `0022` remains unreserved.

### AAI-05 exact completion evidence

- Application PR: `329`
- Exact validated head: `22ed48f92ee72be2e136e780e24236dd37e2fb4d`
- Repository Health: run `33030607196`, job `98382007560`
- Validation Core run: `33030607248`
- Linux job/artifact: `98382008814` / `9630182458`
- Linux artifact digest: `sha256:d0b31b60d56955f260c26fe7e07fd1237073e50c2d69a9504d66fcd91d44b3c6`
- Windows job/artifact: `98382008826` / `9630359600`
- Windows artifact digest: `sha256:49e8bedd7a1828caeefcf1bc490d42636eaa953d1879d619bfd233b84a6fdb14`
- Comparison job/artifact: `98384564046` / `9630372033`
- Comparison artifact digest: `sha256:c8bd25426416fe37163668329edacb75a87b7d91c0862837c83f2242a2dc999a`
- Deterministic receipt: `7e55e9ed29f8fefb42ab8244cafed057631f5cf8c63efee0b95a29d1d668b85e`
- Application squash merge: `511f9566af10f0defa703350ac4ffa6db0c0c4e7`
- Application repair cycles: `0`

## AAI-06 selected successor contract

AAI-06 is selection-only. On the next owner `Continue`, a governed start must freshly verify then-current AIOC and application heads and re-read AAI-01 through AAI-05 completion evidence, this program, the backlog, and `governance/ai/work-state/AAI-06-attempt-001.json`.

Before implementation authority can exist, that governed start must resolve provider-neutral import-versus-link semantics; the bounded initial adapter set; current provider rights, terms and capability evidence; authentication/entitlement/credential handling; live catalog/control boundaries; independent content-acquisition/cache/export/record/stream/redistribution rights; persistence and any actual schema delta; provider-safe test doubles/fixtures; exact deliverables, focused verifier/tests, predecessor regressions and exact-head self-hosted acceptance gate.

Syrinscape, TableTone, PocketBard, Tabletop Audio and other candidate providers remain evidence subjects rather than presumed-authorized integrations. Commercial provider audio remains controlled/referenced unless current verified rights explicitly authorize another operation. Lack of a public API or written expanded permission remains nonauthorization. Unsupported operations cannot be emulated by scraping, reverse engineering or prohibited copying.

AAI-06 selection does not authorize an implementation branch, provider authentication, live catalogs/provider calls, content acquisition/download/copying/caching, payment, recording/streaming automation, migration `0022`, tester distribution, release or deployment.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `completed_verified`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `completed_verified`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `completed_verified`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `selected_not_started`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `planned`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Invariants

- AAI-01 through AAI-05 are `completed_verified` with no further implementation authority.
- AAI-06 is `selected_not_started` with no implementation branch or implementation authority.
- No provider/catalog is canonical and unsupported/unknown capability remains explicit and fail closed.
- AAI-02 rights/provenance, AAI-03 capability, AAI-05 semantic compatibility and runtime availability remain independent; none can silently upgrade another.
- AAI-04 playback/layer/mixer and AAI-05 semantic resolver outcomes remain binding completed predecessor evidence.
- Commercial provider audio remains controlled/referenced rather than copied absent explicit current license and authority.
- Unsupported operations cannot be emulated by scraping, reverse engineering or prohibited content copying.
- Audio remains presentation/support state, not canonical World/Event/Scene/Combat/Action/Visibility truth.
- Migration `0022` remains unreserved.
- No provider authentication/live catalog/provider calls/acquisition/download/copying/caching/scraping/payment, tester distribution, release/deployment or real-money activation is authorized by AAI-06 selection.
