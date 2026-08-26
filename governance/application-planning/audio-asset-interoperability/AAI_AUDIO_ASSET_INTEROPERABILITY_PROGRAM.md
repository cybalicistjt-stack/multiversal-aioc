# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-03  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-02  
**Current item:** AAI-03 — Provider Adapter & Capability-Negotiation Framework  
**Implementation branch:** `integration/aai-03-provider-adapter-capability-negotiation-framework`  
**Implementation authority:** bounded AAI-03 provider-neutral adapter/capability-negotiation framework only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 and AAI-02 are `completed_verified`. AAI-02 application PR #326 exact head `4be81b04e60a85fbcd79edeb544f3cf6abfb2bb1` passed Repository Health run `33007345783` / job `98304422388`, self-hosted Linux AAI-02 Validation Core job `98304425118`, self-hosted Windows job `98304425046`, AAI-01 and MIB-11/D18 regressions, and deterministic comparison job `98309792352` with receipt `3859de8ca241498df77bafec3d37aaddcca0995dff603ed421d526f963e6f041`, then squash-merged as `c7e763f4e9a7cf64c3936a4d67203a1cd6c6ef22`. Repair cycles: **1**.

Owner `Continue` on 2026-08-26 freshly verified AIOC main `ba935731e3db086ae27d99cb08135eddd580f7c0` and application main `c7e763f4e9a7cf64c3936a4d67203a1cd6c6ef22`, re-read the AAI program/backlog, the AAI-03 selection checkpoint, the completed AAI-02 checkpoint and the AAI-01 provider/API/license registry in the application repository, and resolved the bounded AAI-03 adapter/capability-negotiation/persistence/validation contract before governed start.

AAI-03 may implement only provider-neutral **static adapter descriptors**, deterministic **capability negotiation**, governed documentation, focused integration/verifier evidence and Validation Core/workflow wiring. It may not implement live provider-specific adapters, credentials/authentication, live catalog/search, provider calls, content acquisition/download/copying, playback/layering/mixing, semantic availability resolution, payment, tester distribution, release or deployment. No durable runtime ledger is required; migration `0022` remains unreserved.

## Purpose

AAI makes external and user-owned audio usable through one provider-neutral Multiversal layer without requiring Multiversal to own, copy or redistribute commercial audio. Audio intent remains separate from provider identity and selected provider asset/reference, and audio remains presentation/support state rather than canonical gameplay truth.

## Completed AAI-01 foundation

AAI-01 established the governed provider/API/license/authority vocabulary. Capability evidence states are exactly `supported-documented`, `supported-user-controlled`, `provider-contact-required`, `planned-not-current`, `unsupported-by-terms`, `not-publicly-documented`, `unknown-unverified` and `not-applicable`. Unsupported/unknown evidence remains fail closed; no provider/catalog is canonical; local file possession does not imply redistribution, public-performance or commercial rights; scraping/reverse engineering workarounds remain prohibited.

## Completed AAI-02 foundation

AAI-02 established canonical provider-neutral `AudioProvider`, `AudioSource`, `AudioAsset`, `MusicTrack`, `Ambience`, `OneShot`, `Soundscape`, `AudioCue`, `MixPreset`, `Playlist`, `ProviderReference` and `AudioIntent` contracts. Provider-native IDs remain separate from Multiversal identity and semantic intent. Rights for `reference`, `ingest`, `play`, `embed`, `cache`, `export`, `record`, `stream`, `redistribute` and `transform` remain explicit `allowed`, `denied`, `unknown` or `not-applicable` evidence. `unknown` is never allowed. Cue states `unresolved`, `silent` and `manual-reference` remain first-class. Owner references are non-mutating. No runtime ledger or migration `0022` was required.

## AAI-03 governed framework contract

### Adapter descriptors

AAI-03 defines static provider-neutral adapter descriptors with stable `adapterId`, optional `providerId`, adapter kind, evidence reference and capability map. Adapter kinds are `documented-api`, `user-controlled-app`, `external-reference`, `browser-local-companion` and `local-file`.

Descriptors are **evidence**, not live sessions. They store no credentials and perform no provider calls. Adapter/session/authentication/entitlement capability remains separate from AAI-02 provider/source/reference identity and semantic `AudioIntent`.

### Capability vocabulary

AAI-03 covers descriptor keys for `authentication`, `entitlement`, `catalog-search`, `playback-control`, `session-control`, `mix-volume-control`, `one-shot-control`, `remote-sync`, `local-file-access`, `streaming`, `caching` and `export`.

Every capability reuses an AAI-01 evidence state verbatim. Only `supported-documented` and `supported-user-controlled` are usable evidence. `provider-contact-required`, `planned-not-current`, `unsupported-by-terms`, `not-publicly-documented`, `unknown-unverified` and `not-applicable` remain explicit fail-closed outcomes.

### Deterministic negotiation

Negotiation requests name a capability plus optional authored adapter candidates, provider filter and source-kind filter. Authored candidates are evaluated in authored order; otherwise registered adapters are evaluated in stable `adapterId` order. The framework may return `available-documented`, `available-user-controlled`, `manual-external-reference`, explicit unavailable states, `not-applicable` or `no-compatible-adapter`.

`user-controlled-app` and `external-reference` descriptors may produce `manual-external-reference`; AAI-03 does not automate provider applications. A provider filter cannot be silently crossed. Unsupported or unknown capability can never fall back to scraping, reverse engineering or prohibited copying.

Negotiation receipts record request/capability, evaluated adapter IDs and evidence/outcome, selected adapter or null, filters and fixed authority flags. Platform paths, clocks, credentials, provider responses and network state are excluded from deterministic receipts.

### Rights and owner boundaries

Capability evidence never overrides AAI-02 rights matrices. A technically advertised operation still requires separately granted rights evidence under later execution authority. Negotiation cannot create or rewrite AAI-02 provider/source/asset/reference/intent/cue/soundscape identity.

MIB-11/D18 World, Scene/Tabletop, Event, Combat/Exploration, Action, Visibility/Permissions and D29 authoring-provenance remain canonical owners. AAI-03 references are non-mutating and cannot create gameplay truth.

### Persistence

AAI-03 needs no durable runtime persistence. Static adapter descriptors and deterministic negotiation are repository/runtime-pure contracts; credentials and live sessions are explicitly excluded. Migration `0022` remains unreserved.

## AAI-03 completion gate

The application candidate must add:

- `governance/application-planning/audio-asset-interoperability/AAI-03_PROVIDER_ADAPTER_CAPABILITY_NEGOTIATION_FRAMEWORK.md`
- `packages/contracts/src/audio-asset-interoperability/provider-adapter-capability-negotiation-contracts.ts`
- `packages/contracts/src/audio-asset-interoperability/aai-03-starter-adapter-registry.ts`
- `apps/client-ui/src/aai/aai-03.provider-adapter-capability-negotiation-framework.integration.test.ts`
- `tools/verify_aai_03.py`
- `governance/application-planning/validation-core/profiles/AAI-03.json`
- canonical Repository Health/self-hosted workflow registration.

The exact candidate head must pass the focused AAI-03 verifier, AAI-02 and AAI-01 predecessor verifiers, MIB-11/D18 World-owner regression, client typecheck/integration regression, Repository Health, self-hosted Linux and Windows AAI-03 Validation Core and deterministic cross-platform comparison before merge.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `in_progress`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `planned`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `planned`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `planned`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `planned`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Invariants

- AAI-01 and AAI-02 are `completed_verified` with no further implementation authority.
- AAI-03 authority is limited to static provider-neutral adapter/capability-negotiation contracts and deterministic evidence.
- No provider/catalog is canonical and unsupported/unknown capability remains explicit and fail closed.
- AAI-02 rights evidence remains binding and cannot be upgraded by capability negotiation.
- Commercial provider audio remains controlled/referenced rather than copied absent explicit later license and authority.
- Pocket Bard scraping/reverse engineering restrictions and Tabletop Audio SoundPad site-bound restrictions remain binding.
- Audio remains presentation/support state, not canonical World/Event/Scene/Combat/Action/Visibility truth.
- AAI-04 playback/layering/mixing and AAI-05 semantic resolution remain unauthorized.
- Migration `0022` remains unreserved.
- No provider authentication/live catalog/provider calls/acquisition/download/copying/scraping/payment, tester distribution, release/deployment or real-money activation is authorized.
