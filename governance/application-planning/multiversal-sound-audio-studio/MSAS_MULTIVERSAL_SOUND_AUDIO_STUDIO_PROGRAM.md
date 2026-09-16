# MSAS — Multiversal Sound & Audio Studio

**Program ID:** MSAS  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; PDCP-REDUCED; NOT STARTED  
**Activation:** after MAS-21  
**Successor:** MRCS-01  
**Implementation authority:** none

## Purpose

MSAS is the creator-facing studio for producing, editing, composing, mixing, directing, previewing and binding Multiversal music, ambience, sound effects and voice without becoming a second AAI runtime, gameplay-state authority, generic DAW/DSP engine, asset-governance system or provider-generation framework.

Semantic direction remains:

`World / Environment / Scene / Adventure / Combat / Dialogue / Event projections → AAI semantics → MSAS authored audio assets/behaviors → runtime audio renderer`

Prepared audio state never proves canonical gameplay occurrence.

## PDCP reduction

Historical baseline: **21 tranches**.  
Effective implementation/proof plan: **11 tranches**.

Reduction receipt: `governance/application-planning/preimplementation-design-closure/PDCP_MSAS_REDUCTION_RECEIPT.json`  
Family design closure: `governance/application-planning/preimplementation-design-closure/PDCP_MSAS_FAMILY_DESIGN_CLOSURE.md`

### Effective tranche order

1. **MSAS-01 — Audio Studio Workspace, Session Graph & Authority** — absorbs historical 01+02.
2. **MSAS-03 — Waveform, Timeline, Multitrack & Nonlinear Editing**.
3. **MSAS-04 — Mixing, Routing, DSP Intent, Metering & Master/Accessibility Validation** — absorbs 04+16.
4. **MSAS-05 — Music Composition & Adaptive-Music Authoring** — absorbs 05+06.
5. **MSAS-07 — SFX, Foley, Procedural One-Shot, Ambience & Soundscape Production** — absorbs 07+08.
6. **MSAS-09 — Semantic Audio Direction: Event/World/Combat Cue & State Graphs** — absorbs 09+10+11.
7. **MSAS-12 — Dialogue, Voice, Pronunciation, Localization & Alternate-Voice Production** — absorbs 12+13.
8. **MSAS-14 — Spatial Audio, Emitters, Zones, Occlusion & Listener Preview**.
9. **MSAS-15 — Session Soundboard, Cue Stack, Playlist & Live-GM Audio Control**.
10. **MSAS-18 — Audio Asset Lifecycle, Interchange, Rights, Review & Publication** — absorbs 18+19+20 plus historical 17 lifecycle residuals.
11. **MSAS-21 — Golden Adaptive Audio Capability & Semantic-Integration Proof**.

Historical `MSAS-17` no longer survives as a standalone generation engine. Generic generation orchestration belongs to PCA-09 and reusable voice/SFX production primitives to PCA-08; MSAS retains domain briefs, preview/review, acceptance, binding, provenance display and provider-off fallback in the appropriate surviving tranches.

## Authority boundaries

- **AAI** remains authoritative for audio source/asset/cue/soundscape semantics, playback/layering, provider capability/availability, event bindings, permissions, sync, recording/streaming boundaries and provider-neutral interoperability.
- **DWC speech** remains constructed-language pronunciation/exact-ID/acoustic-model authority.
- **ARI/PCA** retain generic identity, rights, derivative provenance, review/version/import-export and production governance.
- **PCA-07** supplies reusable adaptive-audio authoring/profiling, preview and diagnostics primitives.
- **PCA-08** supplies reusable voice/speech/SFX production primitives.
- **PCA-09** owns generic generation orchestration.
- **PCA-13** owns generic localization-production infrastructure.
- **Packet 07** owns generic preview/dry-run/commit/live-GM intervention/debug/recovery semantics.
- World, Environment, Scene, Adventure, Combat, Dialogue and Action/Event remain canonical gameplay/world-state owners.

## Product doctrine

1. Local-first blocking workflows work with paid/cloud providers disabled.
2. Semantic audio intent stays distinct from files, providers and derivatives.
3. Audio may react to canonical state but may not grant, infer or mutate that state.
4. Timeline/multitrack production and state/event-driven adaptive structures share one studio but remain semantically distinct.
5. Soundscapes remain layered/variable systems rather than requiring flattened loops.
6. Voice keeps speaker identity, consent, language, pronunciation, takes and usage rights explicit.
7. Generated outputs remain candidates until accepted and ARI-registered.
8. Spoken/meaningful sonic information has transcript/caption or non-audio alternatives where applicable.
9. Unsupported import/middleware/round-trip behavior remains explicit.
10. Commodity DSP/codecs/plugin hosting/transforms use lawful replaceable libraries where practical.

## Important non-merges

`MSAS-03` and `MSAS-04` remain separate because timeline editing and mix/routing/master validation are materially different kernels. `MSAS-14` remains separate because spatial audio has geometry/listener integration risk. `MSAS-15` remains separate because live-GM audio control has a distinct permission/interaction surface. Voice remains separate from music/SFX because identity, consent, pronunciation and localization make it materially different.

## Golden proof

`MSAS-21` must prove the 48 vectors closed by `PDCP_MSAS_FAMILY_DESIGN_CLOSURE.md`, including original Multiversal world/location ambience, adaptive exploration/combat music, SFX/foley, dialogue VO and DWC pronunciation, spatial audio, live-GM control, editing/mixing/master validation, captions/non-audio descriptions, local-provider-off operation, ARI provenance/rights, deterministic preview where claimed, structured interchange/round-trip loss reporting and explicit cue-vs-gameplay-truth separation.

## Execution rule

Each surviving tranche targets 24 active minutes or less and preserves at least 8 minutes for validation/reconciliation/closeout. Split oversized work before governed start rather than overrunning a one-Continue tranche.

## Non-activation boundary

This planning reduction does not reopen completed AAI, start MSAS implementation, activate providers, authorize paid spend, grant recording/streaming/publication rights, change gameplay truth or mutate `operations/CURRENT.json`.

## Completion standard

MSAS completes when the 11 surviving tranches are `completed_verified` and `MSAS-21` demonstrates production-to-adaptive-runtime continuity across music/SFX/ambience/voice while AAI/DWC/ARI/PCA/canonical-owner boundaries, accessibility, rights/consent and local-first operation remain intact.
