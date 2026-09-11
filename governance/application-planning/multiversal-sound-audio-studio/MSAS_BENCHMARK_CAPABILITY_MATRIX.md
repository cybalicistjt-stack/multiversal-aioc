# MSAS — Clean-Room Audio Capability Benchmark

**Date:** 2026-09-11  
**Purpose:** capability/workflow study only  
**Reuse rule:** clean-room; this document does not authorize copying proprietary source, protected audio, preset libraries, distinctive UI expression, private protocols or implementation details.

## Internal baseline

Multiversal is not starting from zero. Completed AAI already defines provider-neutral audio source/asset/cue/soundscape schemas, playback/layering/mixing, semantic availability, import/link/provider adapters, game-event/scene binding, GM preparation, permission/sync boundaries and multi-provider proof. PCA-07 plans adaptive-audio authoring/profiling over AAI; PCA-08 plans local-first voice/speech/SFX production. DWC speech retains constructed-language pronunciation/acoustic authority. MSAS therefore targets the missing integrated creator product rather than another runtime/DSP authority.

## Capability matrix

| Benchmark | Public capability lessons | MSAS requirement derived clean-room | Boundary |
| --- | --- | --- | --- |
| Audiokinetic Wwise | Interactive music hierarchies; states/switches/game syncs; random/sequence selection; events; spatial audio; simulation/profiling | state/switch/parameter-driven adaptive structures, musical transitions, spatial preview, deterministic simulation/profiling | AAI remains semantic/runtime owner; do not reproduce Wwise object model, UI or proprietary engine |
| FMOD Studio | Events, parameters, multitrack adaptive music, randomization/modulation, mixer snapshots, live update, profiler | event/parameter graph, dynamic mixing/snapshots, adaptive music authoring, live preview and performance diagnostics | keep engine/runtime replaceable; do not clone FMOD Studio or API |
| REAPER | multitrack audio/MIDI recording/editing, takes/lanes, routing/bussing, plugins, automation, batch render, LUFS/true-peak reporting | serious bounded waveform/timeline/multitrack/mixer/render/QC workflow sufficient for RPG audio production | MSAS is not a general DAW; specialist round-trip remains valid |
| Ableton Live | linear Arrangement plus nonlinear Session clips/scenes; audio/MIDI composition and performance | composition should support both timeline arrangement and reusable/launchable musical cells useful for adaptive scoring | do not reproduce Live devices/content/UI; use generic composition concepts |
| Syrinscape | layered/randomized tabletop soundscapes, music/SFX/ambience, custom uploads, GM-oriented triggering, remote listening | layered ambience/weather/ecology design and fast live GM soundboard/cue execution tied to Adventure/Scene context | existing AAI provider/rights boundaries remain; provider content is not copied or rehosted |
| QLab | ordered cue lists, cue carts, precise triggering, routing, looping, realtime levels/effects, live show execution | cue-stack and cart-style session surface with hot triggers, fades/ducking, grouping and safe live control | MSAS is not general show-control/lighting/video software |
| ElevenLabs voice/dubbing workflows | TTS/voice workflows, multi-language dubbing, speaker/timing preservation; professional voice cloning requires owner verification | governed voice profiles, take/version/localization workflow, optional provider adapters, explicit consent/identity evidence | no provider is required; voice impersonation/identity use fails closed without rights/consent |

## Official public evidence reviewed

- Audiokinetic Wwise 2025.1 documentation and learning material: interactive music, States/Switches/Game Syncs, random containers, spatial audio and profiler views.
- FMOD Studio current official product/docs: adaptive audio, events, parameters, multitrack music, mixer snapshots, live update and profiler.
- REAPER current official feature pages (7.79 dated 2026-08-17): multitrack audio/MIDI production, routing, editing, plugins, render queues and LUFS/loudness reporting.
- Ableton Live 12 official documentation: Arrangement View and nonlinear Session View with audio/MIDI clips.
- Syrinscape current official site/API docs: layered/custom tabletop soundscapes, GM-oriented playback, browser/remote play and documented player integration.
- QLab 5 official documentation: cue lists/carts, audio routing, levels/effects, timing and live cue control.
- ElevenLabs current official documentation: voice cloning/verification, dubbing/localization and speaker-preserving workflows.

## Product conclusions

### 1. Multiversal should combine DAW production and game-state authoring without becoming either product class wholesale

Creators need enough multitrack editing, composition, routing, effects, metering and mastering to finish ordinary RPG audio inside Multiversal. They also need adaptive state/parameter/event authoring that a conventional DAW does not provide. The seam between those modes is a core MSAS advantage.

### 2. Tabletop operation deserves a first-class live surface

A game master should not have to enter a production timeline during play. Prepared Adventure/Scene context should project into a fast cue stack, soundboard, playlists, moods and stingers with keyboard/touch/non-pointer alternatives and panic/stop/safe-level behavior.

### 3. Layered soundscapes are more valuable than flattened ambience

Location ambience should support independent weather, ecology, population, machinery, supernatural, interior/acoustic and transient-event layers with variation rules. Flattening remains an export option, not the authoring truth.

### 4. Adaptive music needs explicit musical semantics

Segments, stems/layers, intensity, transition points, tempo/meter, entry/exit rules, stingers and state relationships must remain editable and previewable. A combat state may drive music but does not become combat truth.

### 5. Voice is a governed identity/rights workflow, not just text-to-speech

MSAS needs casting/profile, line/take/version, pronunciation, localization, timing and approval records. Constructed-language pronunciation delegates to DWC. Voice cloning/identity use requires explicit rights/consent evidence; generated output remains an ARI-governed derivative.

### 6. Spatial authoring should be map/scene aware

MSAS should preview emitters, listeners, attenuation, zones and bounded occlusion/reverb intent against governed Scene/map geometry where available, while leaving the runtime implementation replaceable and preserving unsupported states explicitly.

### 7. Validation is part of authoring

Loudness, clipping/true peak, channel configuration, missing assets, stale bindings, unsupported codec/bridge features, excessive voice counts and inaccessible spoken/semantic content should be visible before publication.

## Clean-room rule

The benchmark products are evidence for useful capabilities, workflow classes and failure modes only. MSAS **does not copy** proprietary source code, binaries, audio libraries, presets, sample projects, trademarked content, distinctive visual expression, undocumented/private protocols or reverse-engineered implementation. Direct dependency or provider use requires its own current license/rights review and remains replaceable.