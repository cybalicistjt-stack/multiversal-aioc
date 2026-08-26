# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-04  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-03  
**Current item:** AAI-04 — Playback, Layering & Mixer Engine  
**Implementation branch:** `integration/aai-04-playback-layering-mixer-engine`  
**Implementation authority:** bounded AAI-04 provider-neutral playback/layer/mixer state-and-command engine only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01, AAI-02 and AAI-03 are `completed_verified`. AAI-03 application PR #327 exact head `b2f5db563150e9320d58efe7ff9d277b4473bb02` passed Repository Health run `33012808198` / job `98323189866`, self-hosted Linux AAI-03 Validation Core job `98323193137`, self-hosted Windows job `98323193537`, AAI-02, AAI-01 and MIB-11/D18 regressions, and deterministic comparison job `98326093325` with receipt `cd3d7801dbc8fa9050e5cf418298de9e900aa4a20219d5333b1f0fb532dafbd8`, then squash-merged as `d6b6f4c9316e01f55611e256924b67eaf5f4b3da`. Application repair cycles: **0**.

Owner `Continue` on 2026-08-26 freshly verified AIOC main `54482405620eaf136a79d99a4ccb7edf609bcfaa` and application main `d6b6f4c9316e01f55611e256924b67eaf5f4b3da`, re-read AAI-01 provider/API/license evidence, AAI-02 canonical audio schema, AAI-03 adapter/capability-negotiation evidence, the AAI-04 selection checkpoint and this program/backlog, and resolved the bounded AAI-04 playback/layering/mixer, rights/capability-gating, persistence and validation contract before governed start.

AAI-04 may implement only a provider-neutral playback/layer/mixer **runtime state and command engine** over completed AAI-02 identities and AAI-03 capability negotiation. It may produce deterministic local-media or abstract adapter-control command descriptors and ephemeral playback/mixer state. It may not implement AAI-05 semantic availability resolution or AAI-06 provider-specific live transports/adapters, authenticate to providers, enumerate live catalogs, acquire/copy provider content, scrape/reverse engineer, record/stream/export provider content, spend money, distribute to testers, release or deploy. No durable runtime ledger is required; migration `0022` remains unreserved.

## Purpose

AAI makes external and user-owned audio usable through one provider-neutral Multiversal layer without requiring Multiversal to own, copy or redistribute commercial audio. Audio intent remains separate from provider identity and selected provider asset/reference, and audio remains presentation/support state rather than canonical gameplay truth.

## Completed AAI-01 foundation

AAI-01 established the governed provider/API/license/authority vocabulary. Capability evidence states are exactly `supported-documented`, `supported-user-controlled`, `provider-contact-required`, `planned-not-current`, `unsupported-by-terms`, `not-publicly-documented`, `unknown-unverified` and `not-applicable`. Unsupported/unknown evidence remains fail closed; no provider/catalog is canonical; local file possession does not imply redistribution, public-performance or commercial rights; scraping/reverse engineering workarounds remain prohibited.

## Completed AAI-02 foundation

AAI-02 established canonical provider-neutral `AudioProvider`, `AudioSource`, `AudioAsset`, `MusicTrack`, `Ambience`, `OneShot`, `Soundscape`, `AudioCue`, `MixPreset`, `Playlist`, `ProviderReference` and `AudioIntent` contracts. Provider-native IDs remain separate from Multiversal identity and semantic intent. Rights for `reference`, `ingest`, `play`, `embed`, `cache`, `export`, `record`, `stream`, `redistribute` and `transform` remain explicit `allowed`, `denied`, `unknown` or `not-applicable` evidence. `unknown` is never allowed. Cue states `unresolved`, `silent` and `manual-reference` remain first-class. Owner references are non-mutating.

## Completed AAI-03 foundation

AAI-03 established static provider-neutral adapter descriptors with adapter kinds `documented-api`, `user-controlled-app`, `external-reference`, `browser-local-companion` and `local-file`, plus capability keys for `authentication`, `entitlement`, `catalog-search`, `playback-control`, `session-control`, `mix-volume-control`, `one-shot-control`, `remote-sync`, `local-file-access`, `streaming`, `caching` and `export`.

Only `supported-documented` and `supported-user-controlled` capability evidence is usable. Provider-contact-required, planned, unsupported-by-terms, not-publicly-documented, unknown-unverified and not-applicable states remain explicit fail-closed outcomes. Negotiation respects authored candidate order or stable adapter-ID order, provider/source filters, manual external-reference outcomes and deterministic receipts. Capability evidence never overrides AAI-02 rights matrices.

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

## AAI-04 governed engine contract

### Execution surface

AAI-04 defines three request families: `asset-playback`, `one-shot` and `soundscape`. First-class outcomes are `controlled`, `manual-external`, `silent`, `unavailable-rights`, `unavailable-capability`, `unavailable-reference` and `degraded`.

The engine produces deterministic provider-neutral command descriptors and in-memory playback/layer/mixer state. `controlled` means the governed gates allow a provider-neutral local-media or adapter-control command descriptor; it does not mean AAI-04 has introduced a provider-specific live transport. `manual-external` preserves the AAI-03 manual external-reference path without automating the provider application. Silent, unavailable and degraded outcomes are valid and never block gameplay.

### Independent rights and capability gates

Every audible asset must have AAI-02 `play` rights exactly `allowed`. `denied`, `unknown` and `not-applicable` fail closed. Capability support can never grant or upgrade a denied/unknown right.

Provider/external controlled playback consumes AAI-03 `playback-control`, `one-shot-control` or `mix-volume-control` negotiation as applicable. Only AAI-03 selectable outcomes may produce controlled/manual execution; unsupported-by-terms, not-publicly-documented, unknown-unverified, planned-not-current, provider-contact-required and not-applicable evidence remains unavailable.

User-owned local playback additionally requires usable AAI-03 `local-file-access` evidence and an explicit AAI-04 runtime media probe state of supported. The runtime probe is per execution input and does not rewrite AAI-01/03 evidence or silently turn an unknown capability into a documented capability.

### Cue and reference rule

AAI-04 follows only explicit AAI-02 identities: direct asset IDs, soundscape layer asset IDs, or `manual-reference` cue asset/source references. An `unresolved` cue remains `degraded`; a `silent` cue remains `silent`. AAI-04 performs no semantic tag matching, intent-to-asset search, provider matching, availability resolver or other AAI-05 behavior.

### Layering and mixer semantics

Soundscape layers are evaluated in ascending authored `order`, with stable `layerId` as deterministic tie-break. A layer asset kind maps only to the existing AAI-02 mix groups `music`, `ambience` or `one-shot`. A missing matching group uses gain `1` and muted `false` without inventing a group.

Effective gain is `layer gain × matching mix-group gain`. Effective mute is true if either the layer or its matching mix group is muted. A silent, missing, rights-denied or capability-unavailable layer produces its own explicit receipt and does not block any other eligible layer or gameplay.

### Deterministic receipts

AAI-04 receipts preserve stable request, soundscape, layer, cue, asset, source and adapter IDs where applicable; AAI-02 play-right state; AAI-03 negotiation outcome; local runtime-probe state when applicable; effective gain/mute state; final execution outcome; and a provider-neutral command descriptor or null. Platform paths, wall-clock timing, credentials, live provider responses, network state and machine identity are excluded.

### Owner and identity boundaries

AAI-02 provider/source/asset/reference/intent/cue/soundscape/mix identities are inputs and are never rewritten by playback. MIB-11/D18 World, Scene/Tabletop, Event, Combat/Exploration, Action, Visibility/Permissions and D29 authoring-provenance remain canonical owners. Playback/mixer state is presentation/support state and cannot create World/Event/Scene/Combat/Action/Visibility truth.

### Persistence

AAI-04 requires no durable runtime persistence. Playback/layer/mixer state and deterministic receipts are ephemeral or caller-owned runtime values derived from canonical inputs. Migration `0022` remains unreserved.

## AAI-04 completion gate

The application candidate must add:

- `governance/application-planning/audio-asset-interoperability/AAI-04_PLAYBACK_LAYERING_MIXER_ENGINE.md`
- `packages/contracts/src/audio-asset-interoperability/playback-layering-mixer-engine.ts`
- `packages/contracts/src/audio-asset-interoperability/aai-04-starter-playback-scenarios.ts`
- `apps/client-ui/src/aai/aai-04.playback-layering-mixer-engine.integration.test.ts`
- `tools/verify_aai_04.py`
- `governance/application-planning/validation-core/profiles/AAI-04.json`
- canonical Repository Health/self-hosted workflow registration.

The exact candidate head must pass the focused AAI-04 verifier, AAI-03, AAI-02 and AAI-01 predecessor verifiers, MIB-11/D18 World-owner regression, client typecheck/integration regression, Repository Health, self-hosted Linux and Windows AAI-04 Validation Core and deterministic cross-platform comparison before merge.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `completed_verified`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `in_progress`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `planned`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `planned`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `planned`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Invariants

- AAI-01, AAI-02 and AAI-03 are `completed_verified` with no further implementation authority.
- AAI-04 authority is limited to provider-neutral playback/layer/mixer state/command logic and deterministic evidence.
- No provider/catalog is canonical and unsupported/unknown capability remains explicit and fail closed.
- AAI-02 rights evidence remains binding and cannot be upgraded by AAI-03 capability negotiation or AAI-04 playback.
- Local runtime media support must be explicit per execution and does not rewrite governed provider/capability evidence.
- Commercial provider audio remains controlled/referenced rather than copied absent explicit later license and authority.
- Pocket Bard scraping/reverse engineering restrictions and Tabletop Audio SoundPad site-bound restrictions remain binding.
- Audio remains presentation/support state, not canonical World/Event/Scene/Combat/Action/Visibility truth.
- AAI-05 semantic resolution and AAI-06 provider-specific live adapters remain unauthorized.
- Migration `0022` remains unreserved.
- No provider authentication/live catalog/provider calls/acquisition/download/copying/scraping/payment, tester distribution, release/deployment or real-money activation is authorized.
