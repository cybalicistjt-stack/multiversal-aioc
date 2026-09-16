# PDCP — MSAS Family Design Closure

**Family:** MSAS — Multiversal Sound & Audio Studio  
**PDCP phase:** family reduction  
**Status:** design_closed_for_reduction  
**Implementation authority:** none  
**Historical baseline:** 21 tranches  
**Reduced implementation/proof plan:** 11 tranches  
**Capability loss detected:** false

## 1. Reduction result

MSAS remains the creator-facing integrated audio-production and adaptive-direction studio. It does not become a second AAI runtime, generic DAW/DSP engine, generic asset-governance system, generic generation orchestrator, localization authority, or gameplay-state owner.

The safe reduced strict order is:

`MSAS-01 → MSAS-03 → MSAS-04 → MSAS-05 → MSAS-07 → MSAS-09 → MSAS-12 → MSAS-14 → MSAS-15 → MSAS-18 → MSAS-21`

This is a 21 → 11 reduction.

## 2. Existing-owner absorption

- **AAI** remains authoritative for audio assets, semantic intents, cues, soundscapes, playback/layering/mixer semantics, provider capability/availability, event binding, permissions, remote sync, recording/streaming boundaries and provider-neutral interoperability.
- **DWC speech** remains pronunciation/exact-ID/acoustic-model authority for constructed languages.
- **ARI + PCA-01/PCA-15** remain generic resource identity, rights/use capability, derivative lineage, provenance, review/locking/dependency and asset-governance owners.
- **PCA-07** supplies reusable adaptive-audio authoring/profiling, preview, performance and loudness primitives over AAI.
- **PCA-08** supplies reusable voice/speech/SFX production primitives, take/version workflows, pronunciation handoff and ARI registration.
- **PCA-09** owns generic provider-neutral generation orchestration, seeds/batches/retries/cost budgets/cache/provenance.
- **PCA-13** owns generic localization production infrastructure.
- **PDCP Packet 07** owns generic preview/dry-run/commit/explanation/live-GM intervention/debug/recovery semantics.
- **World/Environment/Scene/Adventure/Combat/Dialogue/Action/Event** remain canonical gameplay/world-state owners. Audio mappings never prove occurrence truth.

## 3. Intra-family folds

### `MSAS-01 + MSAS-02 → MSAS-01`
One opening audio-studio/session model: workspace authority plus Session/Clip/Stem/Take/Region/Collection projections are implemented together because the document/session graph is the substrate of every later editor.

### `MSAS-04 + MSAS-16 → MSAS-04`
Mixing, buses, routing, sends, effects, metering, loudness, dynamics, EQ, safe-level/accessibility checks and mix/master validation are one production/validation kernel. Generic DSP is library-backed and replaceable rather than reimplemented.

### `MSAS-05 + MSAS-06 → MSAS-05`
Composition/MIDI/tempo/meter/key/arrangement and adaptive segments/layers/transitions/intensity are one music-authoring seam over PCA-07/AAI. Static composition and adaptive structure remain separate concepts inside one bounded editor/runtime-integration tranche.

### `MSAS-07 + MSAS-08 → MSAS-07`
Foley/SFX/procedural/layered one-shots and ambience/weather/ecology soundscapes share the same source/clip/layer/envelope/variation production substrate. Soundscape semantics remain AAI-owned.

### `MSAS-09 + MSAS-10 + MSAS-11 → MSAS-09`
Event→cue/state/switch/parameter/variation graphs, world/location/scene bindings and combat/tension/encounter-phase/stinger direction are one adaptive semantic-direction seam. Canonical state remains outside audio.

### `MSAS-12 + MSAS-13 → MSAS-12`
Dialogue casting/takes/lines/performance plus pronunciation, constructed-language handoff, localization and alternate-voice binding are one voice-production seam. DWC and PCA-13 retain pronunciation/localization infrastructure authority.

### `MSAS-18 + MSAS-19 + MSAS-20 → MSAS-18`
Version/variant/localization review, structured interchange/round-trip, middleware bridges, rights/consent/provenance/sample/voice identity and publication form one asset-lifecycle seam. Generic rights/provenance/version/review infrastructure remains ARI/PCA-owned.

## 4. Cross-family absorption

### Historical `MSAS-17`
No standalone MSAS generation engine survives. Generic music/SFX/voice generation orchestration belongs to PCA-09, with voice/SFX production primitives in PCA-08. Residual MSAS work is distributed to `MSAS-05`, `MSAS-07`, `MSAS-12`, and `MSAS-18`: domain briefs, preview/review, acceptance, semantic binding, provenance display and provider-off fallback.

### Packet-07 live-GM semantics
`MSAS-15` stays because a soundboard/cue-stack/playlist live-control surface is real audio-domain UI, but it consumes Packet-07 typed intervention/preview/commit/receipt semantics rather than inventing generic GM-control authority.

### Specialist ownership
MSAS binds maps, characters, adventures, dialogue, NPCs and rules from MCS/MCCS/MNCS/MAS/MRCS but does not become their editor.

## 5. Surviving implementation seams

1. `MSAS-01` — Audio Studio Workspace, Session Graph & Authority
2. `MSAS-03` — Waveform, Timeline, Multitrack & Nonlinear Editing
3. `MSAS-04` — Mixing, Routing, DSP Intent, Metering & Master/Accessibility Validation
4. `MSAS-05` — Music Composition & Adaptive-Music Authoring
5. `MSAS-07` — SFX, Foley, Procedural One-Shot, Ambience & Soundscape Production
6. `MSAS-09` — Semantic Audio Direction: Event/World/Combat Cue & State Graphs
7. `MSAS-12` — Dialogue, Voice, Pronunciation, Localization & Alternate-Voice Production
8. `MSAS-14` — Spatial Audio, Emitters, Zones, Occlusion & Listener Preview
9. `MSAS-15` — Session Soundboard, Cue Stack, Playlist & Live-GM Audio Control
10. `MSAS-18` — Audio Asset Lifecycle, Interchange, Rights, Review & Publication
11. `MSAS-21` — Golden Adaptive Audio Capability & Semantic-Integration Proof

## 6. Important non-merges

- `MSAS-03` does not merge into `MSAS-04`: destructive/nonlinear timeline editing and mix/routing/master validation are different implementation kernels and together would exceed the intended tranche bound.
- `MSAS-14` remains distinct: spatial emitter/zone/occlusion/listener-preview integration is materially different from general cue/state authoring.
- `MSAS-15` remains distinct: live session control and GM-safe triggering has a separate interaction/permission surface even though it consumes Packet-07 semantics.
- `MSAS-12` does not merge with general SFX/music authoring because voice identity, consent, line/take, pronunciation and localization constraints are materially different.

## 7. State and authority rules

- A prepared cue, adaptive state, playlist item, soundboard trigger, spatial emitter or simulated transition is noncanonical audio-authoring state until a canonical owner Event/state drives runtime playback.
- MSAS may preview canonical-owner inputs through permission-filtered projections; it may not infer hidden gameplay state from audio configuration.
- Provider/media unavailability remains nonblocking where AAI says audio is optional.
- Unsupported import, middleware, plugin or round-trip semantics remain explicit loss/unknown states.
- Generated audio remains candidate content until explicit owner/user acceptance and ARI registration.
- Voice identity/cloning requires explicit consent/right evidence; absence of evidence fails closed.
- Meaningful spoken/sonic information requires transcript/caption or semantic non-audio alternatives where applicable.
- Local-first blocking production remains viable with paid/cloud providers disabled.

## 8. Golden vectors

The final `MSAS-21` proof must cover at least these 48 vectors:

1. create/open/save an audio-studio session without mutating gameplay truth;
2. session graph distinguishes Clip, Stem, Take, Region and Collection identities;
3. source resource IDs and ARI provenance survive edit projections;
4. unsupported source bytes/reference state fails closed;
5. waveform edit preserves source/derivative distinction;
6. nondestructive trim/split/move/loop round-trips deterministically;
7. multitrack ordering and timing survive save/reload;
8. edit history/recovery cannot fabricate canonical gameplay Events;
9. bus/routing graph detects invalid/circular unsupported routes;
10. send/effect intent remains distinct from provider/plugin implementation;
11. metering/loudness receipts are deterministic for the declared fixture;
12. safe-level/accessibility warnings do not silently alter master truth;
13. music tempo/meter/key/MIDI/arrangement state round-trips;
14. adaptive music segment/layer transitions are authorable without a second gameplay-state machine;
15. horizontal transition preview is driven by synthetic/permitted state only;
16. vertical-layer intensity preview preserves AAI semantic intent;
17. local/provider-off music workflow remains blocking-capable;
18. SFX one-shot layer/variation definitions round-trip;
19. Foley source and derivative provenance remains visible;
20. ambience soundscape supports layered weather/ecology variation;
21. missing ambience resource remains explicit and nonblocking;
22. procedural/generated SFX candidate is not autoaccepted;
23. event→cue graph binds canonical Event IDs without granting occurrence authority;
24. world/environment/location/scene binding consumes owner projections only;
25. combat phase/intensity/stinger mapping cannot mutate combat state;
26. unknown source state remains unknown rather than inferred from cue configuration;
27. cue/state variation selection is deterministic where a seed/policy claims determinism;
28. dialogue line/casting/take/version workflow preserves speaker identity;
29. alternate take does not overwrite prior accepted lineage;
30. DWC pronunciation handoff uses exact governed pronunciation identity;
31. localization/alternate-voice binding preserves language and speaker distinctions;
32. missing consent/right evidence blocks impersonation/cloning publication;
33. captions/transcripts accompany meaningful spoken content where required;
34. spatial emitter placement is a presentation projection, not World placement truth;
35. zone/listener/occlusion preview handles unsupported geometry explicitly;
36. spatial preview remains usable without proprietary middleware;
37. live-GM soundboard uses typed audio-domain trigger operations;
38. soundboard preview/dry-run is visibly noncommitting;
39. GM trigger cannot manufacture a canonical gameplay Event;
40. playlist/cue-stack recovery preserves ordering and receipts;
41. asset version/variant review preserves provenance and accepted/rejected states;
42. structured import/export reports unsupported/lossy semantics explicitly;
43. middleware round-trip keeps canonical semantic IDs where supported;
44. generic rights/provenance data delegates to ARI rather than duplicating truth;
45. generated music/SFX/voice candidate workflow uses PCA generation adapters and remains optional;
46. provider-off/local-first path completes golden production flow;
47. accessibility path offers non-audio equivalents for meaningful sonic cues;
48. final end-to-end proof binds original Multiversal world/adventure/combat/dialogue inputs through MSAS into AAI runtime semantics without authority bleed.

## 9. Reduction conclusion

All 21 historical tranches retain an explicit implementation/proof destination. No accepted capability is deleted. The reduced 11-tranche family is bounded, implementation-oriented, owner-safe and compatible with the existing `MSAS-21` downstream gate, so no DAG milestone rewrite is required.