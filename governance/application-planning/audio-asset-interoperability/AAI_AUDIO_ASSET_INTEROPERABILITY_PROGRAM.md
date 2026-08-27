# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-07 selected_not_started  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-06  
**Current item:** AAI-07 — Game Event, Scene & Automation Binding  
**Implementation branch:** none  
**Implementation authority:** none; selection only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 through AAI-06 are `completed_verified`. AAI-07 is canonically selected as `selected_not_started` with no implementation branch and no implementation authority.

AAI-06 completed on application PR #330 at exact validated head `4bcf101d04f0b35c00506d0c00e4f0eff83ac83d`. Repository Health run `33054019950` passed, self-hosted Linux job `98456202797` and Windows job `98456202643` passed, deterministic comparison job `98461156230` passed with receipt `8b70c3f0d73c11faf6f168203e41bbb53e50f4abb4a12a357bb90ef6d936d97c`, and the application squash merge is `fb8cae52fd5bf9eaf0cf826bd9f19dd65a9e4884`.

## Completed foundation

- **AAI-01:** provider/API/license/authority evidence and fail-closed capability states.
- **AAI-02:** canonical provider/source/asset/reference/intent/cue identities and operation-specific rights.
- **AAI-03:** provider-neutral adapter descriptors and capability negotiation.
- **AAI-04:** provider-neutral playback/layer/mixer outcomes; unavailable audio remains nonblocking.
- **AAI-05:** deterministic provider-neutral semantic taxonomy and availability resolution.
- **AAI-06:** provider-safe local import/link planning and initial adapters for user-owned local audio, documented Syrinscape control, documented Tabletop Audio localhost companion control, and manual-only TableTone/Pocket Bard references.

## AAI-06 completed contract

AAI-06 preserves explicit operation-specific rights, provenance/license evidence, capability, current terms/entitlement, semantic compatibility and runtime availability as independent fail-closed gates. A provider reference or caller-supplied non-secret provider identifier never implies entitlement. Credentials remain caller-supplied runtime-only. Validation uses fake transports and performs no live provider calls. Tabletop Audio content remains site-bound; TableTone and Pocket Bard remain manual-only. No durable AAI-06 persistence was required and migration `0022` remains unreserved.

## AAI-07 selection boundary

AAI-07 may bind existing canonical gameplay event, scene and automation outputs to existing audio cues and playback behavior. It must not create, rewrite or replace gameplay truth. World, Event, Scene, Combat, Action, Visibility/Permissions and D29 owners remain canonical.

Before governed start, a future owner `Continue` must freshly verify current AIOC/application heads, re-read AAI-01..06 completion evidence, resolve deterministic trigger/scene lifecycle, ordering, idempotency, cancellation and unavailable-audio behavior, determine whether durable persistence is actually required, and define focused plus exact-head acceptance.

AAI-02 rights/provenance, AAI-03 capability, current provider terms/entitlement, AAI-05 semantic/runtime evidence and AAI-06 adapter/provider restrictions remain independently fail closed.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `completed_verified`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `completed_verified`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `completed_verified`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `completed_verified`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `selected_not_started`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Invariants

- AAI-01 through AAI-06 are `completed_verified` with no further implementation authority.
- AAI-07 is `selected_not_started` only; it has no implementation branch or implementation authority.
- Audio may react to canonical gameplay truth but cannot create or mutate it.
- Rights/provenance, capability, terms/entitlement, semantic compatibility and runtime availability remain independently fail closed.
- No provider/catalog is canonical and AAI-06 provider restrictions remain binding.
- Migration `0022` remains unreserved unless AAI-07 separately demonstrates a durable schema delta.
- No payment/subscription activation, tester distribution, release/deployment or real-money provider activation is authorized.
