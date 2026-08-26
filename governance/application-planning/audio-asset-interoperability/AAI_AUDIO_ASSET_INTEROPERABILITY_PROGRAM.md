# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** OWNER-APPROVED — AAI-03 SELECTED_NOT_STARTED  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-02  
**Current item:** AAI-03 — Provider Adapter & Capability-Negotiation Framework  
**Implementation branch:** none  
**Implementation authority:** none until future governed start  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 and AAI-02 are `completed_verified`. AAI-02 application PR #326 exact head `4be81b04e60a85fbcd79edeb544f3cf6abfb2bb1` passed Repository Health run `33007345783` / job `98304422388`, self-hosted Linux AAI-02 Validation Core job `98304425118`, self-hosted Windows job `98304425046`, the focused AAI-02 schema verifier, AAI-01 predecessor regression, MIB-11/D18 World-owner regression and deterministic cross-platform comparison job `98309792352` with receipt `3859de8ca241498df77bafec3d37aaddcca0995dff603ed421d526f963e6f041`, then squash-merged as `c7e763f4e9a7cf64c3936a4d67203a1cd6c6ef22`.

The first AAI-02 candidate `22a0a9cb655d156df472ccd2f6123c96828a8d24` failed the focused Linux invariant because its starter fixture did not exercise the declared MIB-11/D18 owner reference. The bounded repair added a non-mutating World reference without weakening the verifier, producing validated head `4be81b04e60a85fbcd79edeb544f3cf6abfb2bb1`. Repair cycles: **1**.

The strict successor **AAI-03** is selected as `selected_not_started` only. Its selection checkpoint is `governance/ai/work-state/AAI-03-attempt-001.json`. Selection does **not** authorize an implementation branch, provider adapter code, authentication/live catalog access, provider calls, playback, acquisition/download/copying, scraping, payment, migration `0022`, tester distribution, release or deployment. A future owner **Continue** must freshly verify then-current AIOC/application heads, re-read completed AAI-01/AAI-02 evidence and resolve the exact adapter/capability-negotiation/persistence/validation contract before a governed start.

## Purpose

AAI makes external and user-owned audio usable through one provider-neutral Multiversal layer without requiring Multiversal to own, copy or redistribute commercial audio. It covers music, ambience, environmental beds, one-shots, adaptive soundscapes, playlists, cue boards and future spatial audio while preserving source entitlement, provenance, licensing and provider capability boundaries.

The core rule is that **audio intent is separate from provider identity and the selected provider asset/reference**. Audio remains presentation/support state and cannot create or replace canonical World, Event, Scene, Combat, Action or other gameplay truth.

## Completed AAI-01 foundation

AAI-01 established the governed provider/API/license/authority evidence vocabulary. Capability evidence remains explicit: `supported-documented`, `supported-user-controlled`, `provider-contact-required`, `planned-not-current`, `unsupported-by-terms`, `not-publicly-documented`, `unknown-unverified`, and `not-applicable`. Local file possession does not prove redistribution, public-performance or commercial-use rights. Unsupported/unknown capabilities remain fail closed; no provider/catalog is canonical.

## Completed AAI-02 foundation

AAI-02 established provider-neutral records for `AudioProvider`, `AudioSource`, `AudioAsset`, `MusicTrack`, `Ambience`, `OneShot`, `Soundscape`, `AudioCue`, `MixPreset`, `Playlist`, `ProviderReference` and `AudioIntent`.

Its binding rules are:

- stable Multiversal IDs remain separate from provider-native IDs and semantic intent;
- source classes distinguish `user-owned-local`, `provider-controlled` and `external-reference`;
- rights operations `reference`, `ingest`, `play`, `embed`, `cache`, `export`, `record`, `stream`, `redistribute` and `transform` each carry explicit `allowed`, `denied`, `unknown` or `not-applicable` evidence;
- `unknown` is never treated as allowed and one granted right never implies another;
- cue states `unresolved`, `silent` and `manual-reference` are first-class declarative states;
- owner references are non-mutating and may not create gameplay truth;
- no durable runtime ledger was required, so migration `0022` remains unreserved;
- AAI-02 implemented no provider adapter, authentication/catalog access, playback/layering/mixing, semantic resolver, workbench or provider content acquisition.

## AAI-03 selection contract

A future governed start must resolve, from current repository state and completed AAI-01/AAI-02 evidence:

- a provider-neutral adapter interface whose advertised operations are grounded in capability evidence;
- explicit negotiation outcomes preserving supported, unsupported, unknown, not-publicly-documented and provider-contact-required states fail closed;
- separation among adapter/session/authentication/entitlement capability, provider/source/asset/reference identity and semantic audio intent;
- capability descriptors for authentication, entitlement, catalog/search, playback-control, session, mix/volume, one-shots, remote sync, local files, streaming, caching and export without inventing unsupported operations;
- deterministic adapter-selection/negotiation receipts and explicit unavailable/manual/external-reference outcomes;
- a prohibition on scraping, reverse engineering, prohibited content copying or provider-specific hacks as substitutes for unsupported capabilities;
- compatibility with existing World/Event/Scene/Combat/Action/Visibility/D29 owners;
- whether durable runtime persistence is actually required; migration `0022` may be considered only if a separately demonstrated schema delta requires it;
- exact deliverables, focused tests/verifier, predecessor regressions and exact-head self-hosted acceptance criteria before an implementation branch is created.

AAI-03 may not implement AAI-04 playback/layering/mixing or AAI-05 semantic resolution under selection authority.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `selected_not_started`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `planned`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `planned`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `planned`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `planned`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Downstream relationship

ISE follows AAI and consumes its provider-neutral cues, soundscapes, playback controls and entitlement-safe references in the native Scene/tabletop experience. AAI remains the canonical audio interoperability/playback owner.

## Invariants

- AAI-01 and AAI-02 are `completed_verified` with no further implementation authority.
- AAI-03 is selection-only until a future governed start.
- Audio intent, provider identity and selected provider asset/reference remain separable.
- No provider or catalog becomes Multiversal canonical audio truth.
- Unsupported/unknown capability and rights remain explicit and fail closed.
- Commercial provider audio is controlled/referenced rather than copied unless explicit license later permits ingestion.
- User-owned file possession does not infer redistribution/public-performance/commercial rights.
- Pocket Bard scraping/reverse engineering restrictions and Tabletop Audio SoundPad site-bound restrictions remain binding evidence.
- Audio remains presentation/support state, not canonical World/Event/Scene/Combat/Action truth.
- Missing audio never blocks play; unresolved, silence and manual reference remain first-class.
- Migration `0022` remains unreserved.
- AAI-04+, provider acquisition/download/authentication/live catalog/scraping/payment, tester distribution, release/deployment and real-money activation remain unauthorized.
