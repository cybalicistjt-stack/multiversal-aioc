# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** OWNER-APPROVED — AAI-02 SELECTED_NOT_STARTED  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-01  
**Current item:** AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema  
**Implementation branch:** none  
**Implementation authority:** none until future governed start  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 is `completed_verified`. Application PR #325 exact head `578710ded940fe35792d4bab383bf35935fac8cf` passed Repository Health, self-hosted Linux and Windows AAI-01 Validation Core, the focused survey/authority verifier, MAI-10 predecessor regression, MIB-11/D18 World-owner regression and deterministic cross-platform comparison with receipt `1e491160d1ec6e211728a29e6c11b1dd6d641c62167980f648fdf70420494092`, then squash-merged as `b39770127e10f6fb7b364847d22d1a594e822770`.

The strict successor **AAI-02** is selected as `selected_not_started` only. The selection checkpoint is `governance/ai/work-state/AAI-02-attempt-001.json`. Selection does **not** authorize an implementation branch, runtime schema code, provider adapter, provider authentication/catalog work, acquisition/download/copying, playback, migration `0022`, payment, tester distribution, release or deployment. A future owner **Continue** must freshly verify then-current AIOC/application heads, re-read AAI-01 completed evidence and resolve the exact AAI-02 schema/persistence/validation contract before a governed start.

## Purpose

AAI makes external and user-owned audio usable through one provider-neutral Multiversal layer without requiring Multiversal to own, copy or redistribute commercial audio. It covers music, ambience, environmental beds, one-shots, adaptive soundscapes, playlists, cue boards and future spatial audio while preserving source entitlement, provenance, licensing and provider capability boundaries.

The core rule is that **audio intent is separate from provider identity and the selected provider asset/reference**. A Scene/Event/World state may request semantic audio such as `forest/night/rain`, `tavern/crowded`, `combat/desperate`, `portal/open` or `cozy/fireplace`; later AAI tranches may resolve that intent only against permitted and actually supported sources.

## Completed AAI-01 foundation

AAI-01 established the governed provider/API/license/authority evidence layer that all later AAI tranches must consume rather than reinterpret:

- capability states are explicit: `supported-documented`, `supported-user-controlled`, `provider-contact-required`, `planned-not-current`, `unsupported-by-terms`, `not-publicly-documented`, `unknown-unverified`, and `not-applicable`;
- user-owned local files/folders require explicit source/provenance/license evidence; file possession alone does not prove redistribution, public-performance or commercial-use rights;
- common local format families such as WAV/PCM, MP3, AAC/M4A, Ogg/Vorbis or Opus and FLAC are candidates only; future playback/import must runtime-probe actual platform codec/container support;
- Syrinscape has documented public HTTP plus iframe and JavaScript/Web Audio integration surfaces, but those capabilities do not imply entitlement or content-copy rights;
- TableTone direct developer API/SDK capability remains `not-publicly-documented`/`provider-contact-required` in the surveyed official evidence rather than inferred;
- Pocket Bard public evidence remains app/desktop-oriented; its terms prohibit ripping/redistribution, automated scraping and reverse engineering, and no public developer API/SDK was located in the surveyed official evidence;
- Tabletop Audio browser SoundPads and local companion control are documented, while SoundPad sounds remain site-bound and are not ingestible/rehostable under AAI-01 authority;
- unsupported, unavailable, planned, unknown, entitlement-denied and license-restricted capability remains explicit and fail closed;
- no provider/catalog is canonical and no provider is assumed complete;
- audio remains presentation/support state and cannot create or replace canonical World, Event, Scene, Combat, Action or other gameplay truth;
- AAI-01 created no runtime provider/audio ledger, reserved no migration `0022`, made no provider-authenticated calls and acquired/copied no provider content.

## AAI-02 selection contract

A future governed start must resolve, from current repository state and the completed AAI-01 evidence:

- provider-neutral identities and relationships for `AudioProvider`, `AudioSource`, `AudioAsset`, `MusicTrack`, `Ambience`, `OneShot`, `Soundscape`, `AudioCue`, `MixPreset`, `Playlist` and `ProviderReference`;
- explicit separation among semantic audio intent, provider identity and provider asset/reference identity;
- stable deterministic IDs, versioning/serialization rules and explicit unresolved, silent and manual states;
- provenance, source, entitlement, license, attribution, recording/streaming, caching and export evidence fields without inferring rights from possession or availability;
- capability/compatibility references that preserve AAI-01 supported, unsupported, unavailable and unknown/fail-closed evidence rather than invent provider operations;
- compatibility with existing canonical World/Event/Scene/Combat/Action owners so audio schema remains presentation/support state only;
- whether durable runtime persistence is actually required; migration `0022` may be considered only if a separately demonstrated schema delta requires it;
- exact deliverables, validator/tests, migration compatibility and acceptance criteria before an implementation branch is created.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
   Provider-neutral static evidence for local/user-owned audio and current external provider capabilities, terms, entitlement/license/provenance and authority boundaries.

2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `selected_not_started`  
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

- AAI-01 is `completed_verified` with no further implementation authority.
- AAI-02 is selection-only until a future governed start.
- Audio is presentation/support state, not canonical World/Event/Scene/Combat/Action truth.
- Audio intent, provider identity and selected provider asset/reference remain separable.
- No provider or catalog becomes Multiversal's canonical audio model.
- No provider is assumed to support every capability.
- User entitlement/license/provenance is preserved and checked where technically available.
- Commercial audio is controlled/referenced rather than copied unless explicit license allows ingestion.
- Missing audio never blocks play; GM/user manual control and silence remain first-class.
- Hidden/GM-only cues and metadata remain permission-scoped.
- Recording/streaming/caching/export/attribution permissions are explicit capability/license decisions, not inferred.
- Migration `0022` remains unreserved until a separately demonstrated durable schema delta requires it.
- AAI-03+, provider acquisition/download/authentication/scraping/payment, tester distribution, release/deployment and real-money activation remain unauthorized.
