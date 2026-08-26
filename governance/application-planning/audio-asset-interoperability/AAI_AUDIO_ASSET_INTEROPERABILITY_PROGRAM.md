# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** SELECTED_NOT_STARTED — AAI-04  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-03  
**Current item:** AAI-04 — Playback, Layering & Mixer Engine  
**Implementation branch:** none  
**Implementation authority:** none; AAI-04 selection/planning only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01, AAI-02 and AAI-03 are `completed_verified`. AAI-03 application PR #327 exact head `b2f5db563150e9320d58efe7ff9d277b4473bb02` passed Repository Health run `33012808198` / job `98323189866`, self-hosted Linux AAI-03 Validation Core job `98323193137`, self-hosted Windows job `98323193537`, AAI-02, AAI-01 and MIB-11/D18 regressions, and deterministic comparison job `98326093325` with receipt `cd3d7801dbc8fa9050e5cf418298de9e900aa4a20219d5333b1f0fb532dafbd8`, then squash-merged as `d6b6f4c9316e01f55611e256924b67eaf5f4b3da`. Application repair cycles: **0**.

AAI-03 delivered only provider-neutral static adapter descriptors and deterministic capability negotiation. It stores no credentials, makes no provider calls, acquires no provider content, performs no playback or semantic resolution, mutates no gameplay owner, and required no durable runtime ledger. Migration `0022` remains unreserved.

Strict forward order now selects **AAI-04 — Playback, Layering & Mixer Engine** as `selected_not_started`. AAI-04 has no implementation branch and no implementation authority. A future owner `Continue` must freshly verify then-current AIOC/application heads, re-read completed AAI-01/02/03 evidence and this program/backlog, resolve the exact playback/layering/mixer, rights/capability gating, persistence and validation contract, and only then governed-start AAI-04.

## Purpose

AAI makes external and user-owned audio usable through one provider-neutral Multiversal layer without requiring Multiversal to own, copy or redistribute commercial audio. Audio intent remains separate from provider identity and selected provider asset/reference, and audio remains presentation/support state rather than canonical gameplay truth.

## Completed AAI-01 foundation

AAI-01 established the governed provider/API/license/authority vocabulary. Capability evidence states are exactly `supported-documented`, `supported-user-controlled`, `provider-contact-required`, `planned-not-current`, `unsupported-by-terms`, `not-publicly-documented`, `unknown-unverified` and `not-applicable`. Unsupported/unknown evidence remains fail closed; no provider/catalog is canonical; local file possession does not imply redistribution, public-performance or commercial rights; scraping/reverse engineering workarounds remain prohibited.

## Completed AAI-02 foundation

AAI-02 established canonical provider-neutral `AudioProvider`, `AudioSource`, `AudioAsset`, `MusicTrack`, `Ambience`, `OneShot`, `Soundscape`, `AudioCue`, `MixPreset`, `Playlist`, `ProviderReference` and `AudioIntent` contracts. Provider-native IDs remain separate from Multiversal identity and semantic intent. Rights for `reference`, `ingest`, `play`, `embed`, `cache`, `export`, `record`, `stream`, `redistribute` and `transform` remain explicit `allowed`, `denied`, `unknown` or `not-applicable` evidence. `unknown` is never allowed. Cue states `unresolved`, `silent` and `manual-reference` remain first-class. Owner references are non-mutating. No runtime ledger or migration `0022` was required.

## Completed AAI-03 foundation

AAI-03 established static provider-neutral adapter descriptors with adapter kinds `documented-api`, `user-controlled-app`, `external-reference`, `browser-local-companion` and `local-file`. It covers capability keys for `authentication`, `entitlement`, `catalog-search`, `playback-control`, `session-control`, `mix-volume-control`, `one-shot-control`, `remote-sync`, `local-file-access`, `streaming`, `caching` and `export`.

Every capability reuses an AAI-01 evidence state verbatim. Only `supported-documented` and `supported-user-controlled` are usable evidence. `provider-contact-required`, `planned-not-current`, `unsupported-by-terms`, `not-publicly-documented`, `unknown-unverified` and `not-applicable` remain explicit fail-closed outcomes. Negotiation respects authored candidate order or stable adapter-ID order, provider/source filters, explicit manual/external-reference outcomes and deterministic receipts.

Capability evidence never overrides AAI-02 rights matrices. Negotiation cannot create or rewrite AAI-02 provider/source/asset/reference/intent/cue/soundscape identity. MIB-11/D18 World, Scene/Tabletop, Event, Combat/Exploration, Action, Visibility/Permissions and D29 authoring-provenance remain canonical owners.

### AAI-03 exact completion evidence

- Application PR: `327`
- Exact validated head: `b2f5db563150e9320d58efe7ff9d277b4473bb02`
- Repository Health: run `33012808198`, job `98323189866`
- Validation Core run: `33012808538`
- Linux job/artifact: `98323193137` / `9623279540`
- Windows job/artifact: `98323193537` / `9623551591`
- Comparison job/artifact: `98326093325` / `9623652538`
- Deterministic receipt: `cd3d7801dbc8fa9050e5cf418298de9e900aa4a20219d5333b1f0fb532dafbd8`
- Application squash merge: `d6b6f4c9316e01f55611e256924b67eaf5f4b3da`
- Application repair cycles: `0`

## AAI-04 selection contract

Selection authorizes planning resolution only. Before governed start, AAI-04 must resolve a provider-neutral playback, layering and mixer execution contract over completed AAI-02 identities and AAI-03 capability negotiation. AAI-02 rights evidence and AAI-03 capability evidence must remain independent gates; capability support cannot grant a denied or unknown right.

The future start must define explicit silent, unavailable and degraded behavior so missing or unsupported audio never blocks gameplay; deterministic layer ordering and mix behavior; separation from AAI-05 semantic availability resolution and AAI-06 provider-specific live adapters; preservation of World/Event/Scene/Combat/Action/Visibility/D29 owners; and whether any durable persistence is actually required. Migration `0022` remains unreserved unless a separately demonstrated durable schema delta requires it.

Until governed start, no playback/layer/mixer implementation, provider authentication/live catalog/provider call, provider-specific adapter, semantic resolver, acquisition/download/copying, scraping, payment, tester distribution, release or deployment is authorized.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `completed_verified`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `selected_not_started`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `planned`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `planned`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `planned`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Invariants

- AAI-01, AAI-02 and AAI-03 are `completed_verified` with no further implementation authority.
- AAI-04 is `selected_not_started` with no implementation branch or implementation authority.
- No provider/catalog is canonical and unsupported/unknown capability remains explicit and fail closed.
- AAI-02 rights evidence remains binding and cannot be upgraded by AAI-03 capability negotiation or future playback planning.
- Commercial provider audio remains controlled/referenced rather than copied absent explicit later license and authority.
- Pocket Bard scraping/reverse engineering restrictions and Tabletop Audio SoundPad site-bound restrictions remain binding.
- Audio remains presentation/support state, not canonical World/Event/Scene/Combat/Action/Visibility truth.
- AAI-05 semantic resolution and AAI-06 provider-specific live adapters remain unauthorized.
- Migration `0022` remains unreserved.
- No provider authentication/live catalog/provider calls/acquisition/download/copying/scraping/payment, tester distribution, release/deployment or real-money activation is authorized.