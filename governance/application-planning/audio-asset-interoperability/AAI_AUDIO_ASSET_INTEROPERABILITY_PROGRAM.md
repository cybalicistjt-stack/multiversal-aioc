# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-08  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-07  
**Current item:** AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation  
**Implementation branch:** `integration/aai-08-gm-audio-workbench-scene-presets-campaign-preparation`  
**Implementation authority:** bounded AAI-08 only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 through AAI-07 are `completed_verified`. AAI-08 is governed-started `in_progress` after fresh verification of AIOC `598907b1d33774aa8a32cfc0aae5adf7e034b287` and application `da0841d64f43d33aa254a0868d7d393158b4e6e4`, including the bounded current-tranche CI correction.

## AAI-08 governed contract

AAI-08 implements GM-facing workbench drafts, scene presets and campaign-preparation payloads over existing AAI-02 cue/soundscape identities and completed AAI-07 binding definitions. All AAI-08 state is presentation/preparation support and may not create, rewrite, advance, cancel or otherwise mutate World, Scene, Event, Combat, Action, Visibility or automation truth.

Scene presets carry stable preset identity plus an explicit existing owner reference. Entries are deterministically ordered by authored order and stable entry ID. Targets must resolve to existing AAI cue/soundscape identities or completed binding definitions; provider-native identity never becomes gameplay truth.

Preview produces deterministic non-authoritative preview intents only. Applying a preset materializes preparation output, not scene lifecycle. Actual playback still requires completed AAI-04/05/06/07 evidence; caller/workbench ready flags cannot bypass independent rights, capability, terms/entitlement, semantic/runtime, provider or completed-evidence gates.

Campaign preparation groups ordered scene presets and optional GM notes/tags. Missing, unavailable, silent, degraded or manual audio remains explicit and nonblocking and never blocks gameplay.

No new canonical runtime persistence is required. AAI-08 outputs are deterministic caller/repository-owned declarative preparation payloads. Migration `0022` remains unreserved.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `completed_verified`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `completed_verified`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `completed_verified`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `completed_verified`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `completed_verified`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `in_progress`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Acceptance

AAI-08 completion requires the exact candidate head to pass focused AAI-08 invariant verification, client TypeScript typecheck, focused AAI-08 integration regression, AAI-07/06/05/04/03/02/01 predecessor verifiers, MIB-11/D18 World-owner regression, application Repository Health, bounded self-hosted Linux and Windows AAI-08 Validation Core, and deterministic cross-platform comparison. The bounded current-tranche selector must resolve exactly one changed `AAI-08` profile; no historical all-profile PR fanout is authorized.

## Invariants

- AAI-01 through AAI-07 are `completed_verified` with no further implementation authority.
- AAI-08 is `in_progress` only on `integration/aai-08-gm-audio-workbench-scene-presets-campaign-preparation`.
- Workbench/preset/campaign preparation may consume canonical gameplay truth but cannot create or mutate it or scene lifecycle.
- Rights/provenance, capability, terms/entitlement, semantic compatibility, runtime availability, provider restrictions and completed audio evidence remain independently fail closed.
- Unavailable audio remains nonblocking.
- Migration `0022` remains unreserved.
- No payment/subscription activation, tester distribution, release/deployment or real-money provider activation is authorized.
