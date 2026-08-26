# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-05 selected_not_started  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-04  
**Current item:** AAI-05 — Semantic Audio Taxonomy & Availability Resolver  
**Implementation branch:** none  
**Implementation authority:** none; AAI-05 selection/planning resolution only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 through AAI-04 are `completed_verified`. AAI-04 application PR #328 exact head `b6b82dd1e6dc352b36e06fff236031253fc2b41b` passed Repository Health run `33016658926` / job `98336521739`, self-hosted Linux AAI-04 Validation Core job `98336523738`, self-hosted Windows job `98336523736`, AAI-03, AAI-02, AAI-01 and MIB-11/D18 regressions, and deterministic comparison job `98337821873` with receipt `30359a5e508a83efb75471e95e93037569be2664678b6978e6318c4656695bd1`, then squash-merged as `e8c0161e325a9d59b061a61c47d9b620a492cb03`. Application repair cycles: **0**.

The strict successor **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** is now `selected_not_started`. It has no implementation branch and no implementation authority. Selection authorizes only future fresh-read contract resolution after another owner `Continue`; it does not authorize semantic-resolver code, AAI-06 provider-specific live adapters, provider authentication/live catalogs/provider calls, provider content acquisition/copying, scraping/reverse engineering, payment, migration `0022`, tester distribution, release or deployment.

## Purpose

AAI makes external and user-owned audio usable through one provider-neutral Multiversal layer without requiring Multiversal to own, copy or redistribute commercial audio. Audio intent remains separate from provider identity and selected provider asset/reference, and audio remains presentation/support state rather than canonical gameplay truth.

## Completed AAI-01 foundation

AAI-01 established the governed provider/API/license/authority vocabulary. Capability evidence states are exactly `supported-documented`, `supported-user-controlled`, `provider-contact-required`, `planned-not-current`, `unsupported-by-terms`, `not-publicly-documented`, `unknown-unverified` and `not-applicable`. Unsupported/unknown evidence remains fail closed; no provider/catalog is canonical; local file possession does not imply redistribution, public-performance or commercial rights; scraping/reverse engineering workarounds remain prohibited.

## Completed AAI-02 foundation

AAI-02 established canonical provider-neutral `AudioProvider`, `AudioSource`, `AudioAsset`, `MusicTrack`, `Ambience`, `OneShot`, `Soundscape`, `AudioCue`, `MixPreset`, `Playlist`, `ProviderReference` and `AudioIntent` contracts. Provider-native IDs remain separate from Multiversal identity and semantic intent. Rights for `reference`, `ingest`, `play`, `embed`, `cache`, `export`, `record`, `stream`, `redistribute` and `transform` remain explicit `allowed`, `denied`, `unknown` or `not-applicable` evidence. `unknown` is never allowed. Cue states `unresolved`, `silent` and `manual-reference` remain first-class. Owner references are non-mutating.

## Completed AAI-03 foundation

AAI-03 established static provider-neutral adapter descriptors with adapter kinds `documented-api`, `user-controlled-app`, `external-reference`, `browser-local-companion` and `local-file`, plus capability keys for `authentication`, `entitlement`, `catalog-search`, `playback-control`, `session-control`, `mix-volume-control`, `one-shot-control`, `remote-sync`, `local-file-access`, `streaming`, `caching` and `export`.

Only `supported-documented` and `supported-user-controlled` capability evidence is usable. Provider-contact-required, planned, unsupported-by-terms, not-publicly-documented, unknown-unverified and not-applicable states remain explicit fail-closed outcomes. Negotiation respects authored candidate order or stable adapter-ID order, provider/source filters, manual external-reference outcomes and deterministic receipts. Capability evidence never overrides AAI-02 rights matrices.

## Completed AAI-04 foundation

AAI-04 defines three provider-neutral request families: `asset-playback`, `one-shot` and `soundscape`, with first-class outcomes `controlled`, `manual-external`, `silent`, `unavailable-rights`, `unavailable-capability`, `unavailable-reference` and `degraded`.

Every audible asset requires AAI-02 `play` rights exactly `allowed`; `denied`, `unknown` and `not-applicable` fail closed. Provider/external controlled playback consumes AAI-03 capability negotiation and capability support never grants or upgrades a denied/unknown right. User-owned local playback additionally requires usable AAI-03 `local-file-access` evidence and an explicit supported AAI-04 runtime media probe.

AAI-04 follows only explicit AAI-02 identities. `unresolved` cues remain degraded, `silent` cues remain silent, and manual references remain manual. Soundscape layers are evaluated in ascending authored order with stable `layerId` tie-breaking. Effective gain is deterministic layer gain multiplied by matching AAI-02 mix-group gain; mute is inherited from either layer or group. Silent, missing, rights-denied and capability-unavailable layers never block gameplay or other eligible layers.

AAI-04 produces deterministic provider-neutral command/state receipts only. It introduced no semantic tag/intent/provider resolver, provider-specific live transport, authentication, live catalog call, provider content acquisition/copying, recording/streaming automation, owner mutation or gameplay truth. No durable runtime persistence was required; migration `0022` remains unreserved.

### AAI-04 exact completion evidence

- Application PR: `328`
- Exact validated head: `b6b82dd1e6dc352b36e06fff236031253fc2b41b`
- Repository Health: run `33016658926`, job `98336521739`
- Validation Core run: `33016658862`
- Linux job/artifact: `98336523738` / `9624857047`
- Linux artifact digest: `sha256:87a56c5a48fdf40ce05c9e33d3ec642b684cb30d16360525a0a126de3f7cd4a2`
- Windows job/artifact: `98336523736` / `9624931521`
- Windows artifact digest: `sha256:585d25b20cee0382ae62493f768928d99c398f404e79c1d098c43d546b44a020`
- Comparison job/artifact: `98337821873` / `9625102229`
- Comparison artifact digest: `sha256:802290da263e1a8153a8f51e190d9604b95af90719c09f1c0f2a1519935a29d3`
- Deterministic receipt: `30359a5e508a83efb75471e95e93037569be2664678b6978e6318c4656695bd1`
- Application squash merge: `e8c0161e325a9d59b061a61c47d9b620a492cb03`
- Application repair cycles: `0`

## AAI-05 selected successor contract

AAI-05 is selection-only. On the next owner `Continue`, a governed start must freshly verify then-current AIOC and application heads and re-read AAI-01 through AAI-04 completion evidence, this program, the backlog, and `governance/ai/work-state/AAI-05-attempt-001.json`.

Before implementation authority can exist, that governed start must resolve the exact provider-neutral semantic taxonomy and availability model; how semantic compatibility remains independent from AAI-02 rights and AAI-03 capability evidence; deterministic unresolved/manual/silent/unavailable behavior compatible with completed AAI-04 playback; provenance and owner boundaries; persistence and any actual schema delta; deliverables, focused verifier/tests, predecessor regressions and exact-head self-hosted acceptance gate.

AAI-05 selection does not authorize an implementation branch. It does not authorize AAI-06 provider-specific live adapters, provider authentication, live catalogs, provider calls, content acquisition/copying/caching, scraping/reverse engineering, payment, recording/streaming automation, migration `0022`, tester distribution, release or deployment.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `completed_verified`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `completed_verified`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `selected_not_started`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `planned`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `planned`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Invariants

- AAI-01 through AAI-04 are `completed_verified` with no further implementation authority.
- AAI-05 is `selected_not_started` with no implementation branch or implementation authority.
- No provider/catalog is canonical and unsupported/unknown capability remains explicit and fail closed.
- Semantic compatibility, AAI-02 rights evidence and AAI-03 capability evidence remain independent; none can silently upgrade another.
- AAI-04 provider-neutral playback/layer/mixer outcomes and nonblocking behavior remain binding predecessor evidence.
- Commercial provider audio remains controlled/referenced rather than copied absent explicit later license and authority.
- Pocket Bard scraping/reverse engineering restrictions and Tabletop Audio SoundPad site-bound restrictions remain binding.
- Audio remains presentation/support state, not canonical World/Event/Scene/Combat/Action/Visibility truth.
- AAI-06 provider-specific live adapters remain unauthorized.
- Migration `0022` remains unreserved.
- No provider authentication/live catalog/provider calls/acquisition/download/copying/scraping/payment, tester distribution, release/deployment or real-money activation is authorized.
