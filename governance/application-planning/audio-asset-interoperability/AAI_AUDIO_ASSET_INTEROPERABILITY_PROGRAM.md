# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** OWNER-APPROVED — AAI-01 SELECTED_NOT_STARTED  
**Activation:** MAI-10 completed_verified  
**Current item:** AAI-01 — Audio Ecosystem, API, License & Authority Survey  
**Implementation branch:** none  
**Implementation authority:** none until future governed start  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-10 completed the predecessor Map & Visual Asset Interoperability program and squash-merged application PR #321 as `da9314298c104723ff3b04e12b1df1e264d55300`. AAI-01 is now selected as `selected_not_started` only. The selection checkpoint is `governance/ai/work-state/AAI-01-attempt-001.json`.

Selection does **not** authorize an implementation branch, provider adapter, provider account/authentication work, acquisition, download, caching, scraping, payment or integration code. A future owner **Continue** must freshly verify then-current AIOC/application heads and current provider/API/terms/license/entitlement facts, resolve the exact AAI-01 survey evidence and authority contract, and only then governed-start implementation.

## Purpose

AAI makes external and user-owned audio usable through one provider-neutral Multiversal layer without requiring Multiversal to own, copy or redistribute commercial audio. It covers music, ambience, environmental beds, one-shots, adaptive soundscapes, playlists, cue boards and future spatial audio while preserving source entitlement, provenance, licensing and provider capability boundaries.

The core rule is that **audio intent is separate from the selected provider asset**. A Scene/Event/World state may request semantic audio such as `forest/night/rain`, `tavern/crowded`, `combat/desperate`, `portal/open` or `cozy/fireplace`; the resolver may satisfy that intent from any permitted connected source, offer GM choices, fall back to another source, use an explicit placeholder/silent state, or remain unresolved.

Multiversal must not scrape, cache, export, redistribute or impersonate provider-owned audio unless the provider/license explicitly permits that operation. Provider connections control or reference the user's legitimate entitlement; raw commercial audio remains with its owner/provider unless separately licensed for local ingestion.

## Provider posture

AAI is capability-driven rather than vendor-hardcoded. Candidate sources include user-owned local files and folders, Syrinscape, TableTone, PocketBard, Tabletop Audio and future providers. AAI-01 must reverify current APIs, terms, account/entitlement rules and technical capabilities before implementation decisions.

A provider may expose any subset of: catalog search, metadata, authenticated playback, embedded playback, external-app launch, session control, mood/soundset/preset control, one-shots, layered mixing, per-layer volume, remote synchronization, entitlement verification, local caching, export, attribution requirements and recording/streaming permissions. Unsupported capability must remain explicit rather than being emulated by prohibited scraping or copying.

## AAI-01 selection contract

The future governed start must resolve, from current evidence:

- user-owned local audio authority, supported formats, provenance and ingestion boundaries;
- Syrinscape, TableTone, PocketBard, Tabletop Audio and other then-current candidate provider APIs/SDKs, terms, accounts, entitlement and license behavior;
- supported versus unsupported catalog/search, authentication, playback, embed/external-app, session, mix, one-shot, remote synchronization, caching, export, attribution and recording/streaming capabilities;
- explicit fail-closed handling for unavailable, unsupported, unknown, entitlement-denied and license-restricted capabilities;
- provider-neutral source/capability evidence that does not make a provider or catalog canonical;
- separation between semantic audio intent and a selected provider asset/reference;
- authority boundaries proving audio remains presentation/support state and never creates World, Event, Combat or other gameplay truth;
- exact AAI-01 survey artifacts, verifier and acceptance criteria before an implementation branch is created.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `selected_not_started`  
   Survey local/user-owned audio and current external providers including Syrinscape and TableTone. Record APIs, SDKs, embedding, remote control, catalog/search, authentication, entitlement, caching, redistribution, attribution, recording/streaming and commercial-use constraints. Establish audio-vs-game-state authority boundaries.

2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `planned`  
   Define provider-neutral `AudioProvider`, `AudioSource`, `AudioAsset`, `MusicTrack`, `Ambience`, `OneShot`, `Soundscape`, `AudioCue`, `MixPreset`, `Playlist`, `ProviderReference`, provenance/license metadata and semantic intent records. Provider asset identity remains separate from gameplay/event identity.

3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `planned`  
   Define adapters that advertise only supported operations: native/embedded/external playback, catalog access, search, authentication, entitlement, sessions, mix/volume, one-shots, remote sync, local files, streaming, caching and export. Unsupported operations stay unavailable without hacks.

4. **AAI-04 — Playback, Layering & Mixer Engine** — `planned`  
   Support music, ambience, environmental layers and one-shots with loops, fades, crossfades, ducking, intensity, volume groups, mute/solo, transition rules and interruption behavior. Preserve a path for later spatial/positional audio without making it a prerequisite.

5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `planned`  
   Describe requested mood/environment/action semantics separately from provider assets. Resolve against sources the GM/user is actually permitted to use; support source/style lock, ranked choices, cross-provider fallback, manual override, explicit silence/placeholders and unresolved needs.

6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `planned`  
   Implement user-owned local audio/folder adapters, common compatible audio formats, a Syrinscape capability adapter, a TableTone capability adapter and a generic external-provider/reference adapter. Integration depth follows verified provider capabilities; no provider-specific workaround may bypass terms or entitlement.

7. **AAI-07 — Game Event, Scene & Automation Binding** — `planned`  
   Bind optional audio cues to existing canonical Scene/Event/World/Combat/Weather/Travel/Vehicle/Magic/Cozy states and transitions without moving gameplay authority into audio. Support enter/exit, combat start/end, spell/power, portal, vehicle, weather, stress/horror, downtime and GM-authored cues. GM manual override and disable remain first-class.

8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`  
   Provide connected-source search, permission-aware preview, cue boards, scene soundscapes, intensity/mood controls, preset preparation, fallbacks, provenance/license display and manual assignment. The GM works from semantic intent rather than provider-specific catalog IDs whenever possible. Preserve a compact controller/deck projection suitable for later ISE native Scene use.

9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
   Define GM-device, player-device, provider-session and external-app playback modes; reconnect/rejoin behavior; player volume controls; GM-only/spoiler-safe cues; remote-alpha synchronization; attribution; and explicit recording/streaming restrictions. Hidden cue metadata must not leak to players.

10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`  
    Prove one campaign can mix local user-owned audio, provider-controlled ambience, one-shots, unavailable-provider fallbacks, unresolved cues, remote players and deterministic cue state while respecting entitlements and permissions. The game must remain fully usable with all audio disabled.

## Downstream relationship

ISE follows AAI and consumes its provider-neutral cues, soundscapes, playback controls and entitlement-safe references in the native Scene/tabletop experience. ISE may present a simpler Scene Audio Deck and bind audio intent to regions/events, but AAI remains the canonical audio interoperability/playback owner.

## Invariants

- AAI-01 is selection-only until a future governed start.
- Audio is presentation/support state, not canonical World/Event/Combat truth.
- Audio intent and selected provider asset remain separable.
- No provider or catalog becomes Multiversal's canonical audio model.
- No provider is assumed to support every capability.
- User entitlement/license/provenance is preserved and checked where technically available.
- Commercial audio is controlled/referenced rather than copied unless explicit license allows ingestion.
- Missing audio never blocks play.
- GM/user manual control and silence are first-class.
- Hidden/GM-only cues and metadata remain permission-scoped.
- Recording/streaming/export permissions are explicit capability/license decisions, not inferred.
- AAI consumes MAI's provider-neutral interoperability patterns but remains a separate audio program.
- ISE, WCI, SCL and VTI consume AAI rather than creating parallel audio ownership or playback ledgers.
- No provider acquisition/download/authentication/scraping/payment, tester distribution, release/deployment or real-money activation is authorized by AAI-01 selection.
