# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-02  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-01  
**Current item:** AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema  
**Implementation branch:** `integration/aai-02-canonical-audio-source-asset-cue-soundscape-schema`  
**Implementation authority:** bounded AAI-02 schema/contract/evidence only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 is `completed_verified`. Application PR #325 exact head `578710ded940fe35792d4bab383bf35935fac8cf` passed exact-head Repository Health, self-hosted Linux and Windows AAI-01 Validation Core, the focused survey/authority verifier, MAI-10 predecessor regression, MIB-11/D18 World-owner regression and deterministic cross-platform comparison with receipt `1e491160d1ec6e211728a29e6c11b1dd6d641c62167980f648fdf70420494092`, then squash-merged as `b39770127e10f6fb7b364847d22d1a594e822770`.

Owner `Continue` on 2026-08-26 freshly verified AIOC main `7e68d898b3ef1fb73ca748596f633e588b26d001` and application main `b39770127e10f6fb7b364847d22d1a594e822770`, re-read the AAI program/backlog, AAI-01 completed checkpoint and AAI-01 closeout, and resolved the bounded AAI-02 schema/persistence/validation contract before governed start.

AAI-02 may implement only provider-neutral TypeScript contracts, deterministic starter/integration evidence, governed schema documentation, a focused verifier and Validation Core/workflow wiring. It may not implement provider adapters, authentication/live catalogs, content acquisition/copying, playback/layering/mixing, semantic resolution, game-event automation, GM workbench UI, multiplayer audio runtime, payment, release/deployment or tester distribution. No durable runtime audio ledger is required for this tranche, so migration `0022` remains unreserved.

## Purpose

AAI makes external and user-owned audio usable through one provider-neutral Multiversal layer without requiring Multiversal to own, copy or redistribute commercial audio. It covers music, ambience, environmental beds, one-shots, adaptive soundscapes, playlists, cue boards and future spatial audio while preserving source entitlement, provenance, licensing and provider capability boundaries.

The core rule is that **audio intent is separate from provider identity and the selected provider asset/reference**. Scene/Event/World state may request semantic audio, but AAI records remain presentation/support state and cannot create or replace canonical World, Event, Scene, Combat, Action or other gameplay truth.

## Completed AAI-01 foundation

AAI-01 established the provider/API/license/authority evidence layer that AAI-02 must consume rather than reinterpret:

- capability evidence states are explicit: `supported-documented`, `supported-user-controlled`, `provider-contact-required`, `planned-not-current`, `unsupported-by-terms`, `not-publicly-documented`, `unknown-unverified`, and `not-applicable`;
- local file possession does not prove redistribution, public-performance or commercial-use rights;
- common local format families remain candidates whose actual codec/container compatibility must be runtime-probed later;
- Syrinscape documented HTTP/iframe/JavaScript surfaces do not imply entitlement or content-copy rights;
- TableTone direct developer API/SDK capability remains not-publicly-documented/provider-contact-required in surveyed evidence;
- Pocket Bard public evidence remains app-oriented and its terms prohibit ripping/redistribution, automated scraping and reverse engineering;
- Tabletop Audio SoundPad content remains site-bound even though local browser control is documented;
- unsupported, unavailable, planned, unknown, entitlement-denied and license-restricted capability remains explicit and fail closed;
- no provider/catalog is canonical and no provider is assumed complete;
- audio remains presentation/support state and AAI-01 created no runtime ledger or migration `0022` reservation.

## AAI-02 governed schema contract

### Canonical record kinds

AAI-02 defines provider-neutral records for `AudioProvider`, `AudioSource`, `AudioAsset`, `MusicTrack`, `Ambience`, `OneShot`, `Soundscape`, `AudioCue`, `MixPreset`, `Playlist`, `ProviderReference` and `AudioIntent`.

Every record has a stable explicit Multiversal ID. Provider-native IDs or URLs are carried only inside `ProviderReference`; they never become gameplay identity, canonical provider truth or evidence of content ownership.

### Source and asset model

`AudioSource` distinguishes `user-owned-local`, `provider-controlled` and `external-reference` sources. Every source carries provenance, license/entitlement and compatibility evidence. `AudioAsset` records are typed as `music-track`, `ambience` or `one-shot` and reference a source plus optional provider reference. Commercial provider bytes remain outside Multiversal unless a later separately authorized tranche has explicit ingestion rights.

### Intent, cue and soundscape model

`AudioIntent` is semantic presentation metadata, separate from provider/source/asset identity and from canonical gameplay owner state. `AudioCue` supports exactly the first-class declarative states `unresolved`, `silent` and `manual-reference`; AAI-02 does not perform semantic resolution or playback. `Soundscape`, `MixPreset` and `Playlist` carry deterministic declarative references/order/gain intent only. Playback/layering/mixing behavior belongs to later tranches.

### Rights and capability evidence

Rights operations are explicit for `reference`, `ingest`, `play`, `embed`, `cache`, `export`, `record`, `stream`, `redistribute` and `transform`, each with state `allowed`, `denied`, `unknown` or `not-applicable`. `unknown` is never treated as allowed, and one allowed operation never implies another.

Compatibility/capability evidence reuses the AAI-01 evidence vocabulary unchanged. AAI-02 cannot upgrade unsupported/unknown/provider-contact-required capability by inference, scraping or reverse engineering.

### Owner references

AAI-02 may carry stable references to established owners such as MIB-11/D18 World, Scene/Tabletop, Event, Combat/Exploration, Action, Visibility/Permissions and D29 authoring-provenance. These references are non-mutating. Audio metadata cannot create or replace owner truth.

### Determinism and persistence

Validation requires unique stable IDs, referential integrity, explicit rights/capability evidence, provider/asset/intent separation and fail-closed unresolved/silent/manual states. Authored ordered arrays preserve authored order; unordered diagnostics use stable ID sorting. Platform timing, local paths, credentials and provider responses are excluded from deterministic receipts.

AAI-02 requires no durable runtime ledger. Repository TypeScript contracts and deterministic starter/integration evidence are sufficient; migration `0022` remains unreserved.

## AAI-02 completion gate

The application candidate must add:

- `governance/application-planning/audio-asset-interoperability/AAI-02_CANONICAL_AUDIO_SOURCE_ASSET_CUE_SOUNDSCAPE_SCHEMA.md`
- `packages/contracts/src/audio-asset-interoperability/canonical-audio-source-asset-cue-soundscape-contracts.ts`
- `packages/contracts/src/audio-asset-interoperability/aai-02-starter-library.ts`
- `apps/client-ui/src/aai/aai-02.canonical-audio-source-asset-cue-soundscape-schema.integration.test.ts`
- `tools/verify_aai_02.py`
- `governance/application-planning/validation-core/profiles/AAI-02.json`
- canonical Repository Health/self-hosted workflow registration.

The exact candidate head must pass the focused AAI-02 verifier, the AAI-01 predecessor verifier, the MIB-11/D18 World-owner regression, Repository Health, self-hosted Linux and Windows AAI-02 Validation Core and deterministic cross-platform comparison before merge.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `in_progress`
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `planned`
4. **AAI-04 — Playback, Layering & Mixer Engine** — `planned`
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `planned`
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `planned`
7. **AAI-07 — Game Event, Scene & Automation Binding** — `planned`
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Downstream relationship

ISE follows AAI and consumes its provider-neutral cues, soundscapes, playback controls and entitlement-safe references in the native Scene/tabletop experience. ISE may present a simpler Scene Audio Deck and bind audio intent to regions/events, but AAI remains the canonical audio interoperability/playback owner.

## Invariants

- AAI-01 is `completed_verified` with no further implementation authority.
- AAI-02 authority is limited to its governed schema/contract/evidence branch.
- Audio intent, provider identity and selected provider asset/reference remain separable.
- No provider or catalog becomes Multiversal canonical audio truth.
- Unsupported/unknown capability and rights remain explicit and fail closed.
- Commercial provider audio is controlled/referenced rather than copied unless explicit license later permits ingestion.
- User-owned file possession does not infer redistribution/public-performance/commercial rights.
- Audio remains presentation/support state, not canonical World/Event/Scene/Combat/Action truth.
- Missing audio never blocks play; unresolved, silence and manual reference are first-class.
- Migration `0022` remains unreserved.
- AAI-03+, provider acquisition/download/authentication/scraping/payment, tester distribution, release/deployment and real-money activation remain unauthorized.
