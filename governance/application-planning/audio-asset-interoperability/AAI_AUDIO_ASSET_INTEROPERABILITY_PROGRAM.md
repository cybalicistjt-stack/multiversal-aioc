# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-01  
**Activation:** MAI-10 completed_verified  
**Current item:** AAI-01 — Audio Ecosystem, API, License & Authority Survey  
**Implementation branch:** `integration/aai-01-audio-ecosystem-api-license-authority-survey`  
**Implementation authority:** bounded AAI-01 survey/evidence only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-10 is `completed_verified` and application main is `da9314298c104723ff3b04e12b1df1e264d55300`. Owner `Continue` on 2026-08-26 freshly verified that application head and AIOC main `e0fbf5259a59c5ee70f87f86c241092b6da0b7db`, re-read the AAI program/backlog and MAI-10 closeout, and freshly surveyed current provider/API/terms/license/entitlement evidence before governed-starting AAI-01.

AAI-01 is intentionally a **static survey/evidence tranche**. It may add governed documentation, machine-readable evidence, a focused verifier and Validation Core wiring. It may not authenticate to providers, enumerate a user's commercial catalog, acquire/download/cache/copy provider audio, implement provider adapters/playback, create the AAI-02 canonical schema, make purchases or activate production integrations.

## Purpose

AAI makes external and user-owned audio usable through one provider-neutral Multiversal layer without requiring Multiversal to own, copy or redistribute commercial audio. It covers music, ambience, environmental beds, one-shots, adaptive soundscapes, playlists, cue boards and future spatial audio while preserving source entitlement, provenance, licensing and provider capability boundaries.

The core rule is that **audio intent is separate from the selected provider asset**. A Scene/Event/World state may request semantic audio such as `forest/night/rain`, `tavern/crowded`, `combat/desperate`, `portal/open` or `cozy/fireplace`; later AAI tranches may resolve that intent only against permitted and actually supported sources.

## AAI-01 governed survey contract

The survey records capability using explicit evidence states: `supported-documented`, `supported-user-controlled`, `provider-contact-required`, `planned-not-current`, `unsupported-by-terms`, `not-publicly-documented`, `unknown-unverified`, and `not-applicable`. Unsupported, unknown, planned, unavailable, entitlement-denied or license-restricted capability remains explicit and cannot be promoted to supported by inference, scraping or reverse engineering.

### User-owned local audio

User-selected local files/folders are a distinct provider-neutral source class. AAI-01 surveys common candidate format families such as WAV/PCM, MP3, AAC/M4A, Ogg/Vorbis or Opus and FLAC but does not claim universal support across the web, desktop and mobile runtimes. Future ingestion/playback must use runtime capability probing or an equivalent native platform capability seam. File possession alone does not prove redistribution, public-performance or commercial-use rights; source/provenance/license evidence remains explicit.

### Syrinscape

Current official integration documentation exposes a public HTTP API plus iframe and JavaScript/Web Audio integration surfaces. The HTTP reference documents authenticated configuration/session identity, soundset/mood/element listing and search, play/stop controls and volume controls. The iframe and JavaScript documentation describes embedded player/GM surfaces and custom UI/player integration.

Evidence observed 2026-08-26:
- `https://docs.syrinscape.com/`
- `https://docs.syrinscape.com/http-reference/`
- `https://docs.syrinscape.com/iframe-player/`
- `https://docs.syrinscape.com/javascript-player/`

AAI-01 records these as documented capabilities only. It does not obtain/store live auth tokens, inspect a user's paid library, acquire audio or call provider endpoints.

### TableTone

Current official evidence documents the TableTone app, account/content-pack workflow and adaptive presets/scenes. The current how-it-works page states that loading user-owned sounds/playlists is not currently supported and that a browser-compatible server/client host solution is planned. Current store terms are dated 2025-11-05 and govern the app/store asset packages. No public developer API/SDK documentation was located in the surveyed official sources; this means direct programmatic integration is `not-publicly-documented`/`provider-contact-required`, not that a private or future interface is impossible.

Evidence observed 2026-08-26:
- `https://www.tabletone.app/how-tabletone-works`
- `https://store.tabletone.app/policies/terms-of-service`
- `https://account.tabletone.app/register`

No scraping or reverse-engineered workaround is authorized.

### Pocket Bard

Current official evidence shows mobile and desktop app delivery with adaptive music states, ambiences and one-shots. Terms of Service last updated 2026-08-14 grant a bounded license for tabletop gaming/streaming use with required credit when shared to an audience and explicitly prohibit copying/ripping/redistribution, automated scraping and reverse engineering. No public developer API/SDK documentation was located in the surveyed official sources.

Evidence observed 2026-08-26:
- `https://www.pocketbard.app/`
- `https://www.pocketbard.app/download`
- `https://www.pocketbard.app/terms-of-service.html`

Until a current public/partner interface is verified, future integration remains external-app/manual-reference or provider-contact-required rather than an invented API.

### Tabletop Audio

Current official evidence documents browser-hosted 10-minute ambiences, layered SoundPads and a local Stream Deck companion/control surface using localhost HTTP GET requests. The site's license states that 10-minute ambiences are CC BY-NC-ND 4.0 and that SoundPad sounds are not meant to be downloaded or used outside `tabletopaudio.com`.

Evidence observed 2026-08-26:
- `https://tabletopaudio.com/about.html`
- `https://tabletopaudio.com/soundpad.html`
- `https://tabletopaudio.com/sd_helper.html`

The local control helper is evidence for user-side browser control; it is not permission to extract or rehost SoundPad content.

## Authority and licensing boundaries

- Audio is presentation/support state, never canonical World/Event/Scene/Combat/Action/gameplay truth.
- Audio intent, provider identity and provider asset/reference identity remain separate.
- No provider or catalog is canonical, and no provider is assumed to support every capability.
- Commercial provider audio is controlled/referenced through legitimate entitlement unless explicit license evidence permits local ingestion.
- Missing or disabled audio never blocks play.
- Hidden/GM-only cue metadata remains permission-scoped.
- Recording, streaming, caching, export, attribution and redistribution permissions are explicit provider/license evidence, never inferred.
- User-owned file possession does not by itself prove public-performance, redistribution or commercial rights.
- AAI-01 creates no runtime provider/audio ledger and reserves no migration `0022`.

## AAI-01 completion gate

The bounded application candidate must add the governed survey, machine-readable registry, `tools/verify_aai_01.py`, Validation Core `AAI-01` profile and required workflow wiring. The exact candidate head must pass focused AAI-01 verification, MAI-10 predecessor regression, MIB-11/D18 World-owner regression, Repository Health, self-hosted Linux and Windows AAI-01 Validation Core, and deterministic cross-platform comparison before merge.

AAI-02 remains unauthorized until AAI-01 is separately closed `completed_verified` and the strict successor is selected.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `in_progress`
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `planned`
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

AAI-01 is survey/evidence only on its governed branch. Audio intent and provider asset identity remain separable. No provider/catalog is canonical. Unsupported/unknown capability remains explicit. Commercial provider audio is not copied absent explicit permission. Missing audio never blocks play. Audio never becomes World/Event/Scene/Combat/gameplay truth. AAI-02+, provider acquisition/download/authentication/scraping/payment, tester distribution, release/deployment and real-money activation remain unauthorized.
