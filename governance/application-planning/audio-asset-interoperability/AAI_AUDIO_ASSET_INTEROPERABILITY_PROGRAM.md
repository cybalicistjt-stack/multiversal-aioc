# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-08 SELECTED  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-07  
**Current item:** AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation  
**Implementation branch:** none — selected_not_started  
**Implementation authority:** none until governed AAI-08 start  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 through AAI-07 are `completed_verified`. AAI-07 application PR #331 was validated at `839cf64a241a1dde966791f054c5b3549792cd90` and merged to application `main` as `016bd57181cccf8b9446dd1b6f9fd793618d9f40`. Repository Health run `33070840112` and self-hosted validation run `33070840352` completed successfully.

AAI-08 is the strict successor and is now `selected_not_started`. Selection grants planning-resolution authority only. A governed start must freshly verify canonical heads, resolve the exact workbench/preset/campaign-preparation contract, decide persistence/migration need, and declare the exact acceptance gate before an implementation branch is created.

## AAI-07 completed contract

AAI-07 consumes immutable existing gameplay signals from canonical owners and binds them deterministically to existing AAI cue/soundscape behavior. Audio remains presentation/support state and never creates, rewrites, advances, cancels or persists gameplay truth. Rights/provenance, capability, provider terms/entitlement, semantic compatibility, runtime availability and adapter restrictions remain independent fail-closed gates. Unavailable audio remains nonblocking. Migration `0022` remains unreserved.

## AAI-08 selection boundary

AAI-08 covers GM-facing audio workbench behavior, scene presets and campaign preparation over completed AAI-01..07 foundations. Selection does not yet decide durable persistence and does not authorize implementation. Any eventual authored preparation state must preserve canonical gameplay owners and all prior rights/provider boundaries.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `completed_verified`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `completed_verified`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `completed_verified`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `completed_verified`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `completed_verified`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `selected_not_started`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Acceptance

AAI-08 acceptance must be resolved at governed start. The normal final active-code gate remains self-hosted Windows + self-hosted Linux + deterministic cross-platform comparison, together with focused AAI-08 and declared predecessor regressions. Historical/full-profile validation may be retained for periodic/manual independent audit rather than unnecessary ordinary-PR fanout where governance maintenance proves that narrowing is safe.

## Invariants

- AAI-01 through AAI-07 are `completed_verified` with no further implementation authority.
- AAI-08 is `selected_not_started`; no implementation branch or implementation authority exists yet.
- Audio/workbench preparation may consume canonical gameplay truth but cannot create or mutate it.
- Rights/provenance, capability, terms/entitlement, semantic compatibility, runtime availability and provider restrictions remain independently fail closed.
- Unavailable audio remains nonblocking.
- Migration `0022` remains unreserved unless a separately demonstrated durable canonical schema delta requires it.
- No payment/subscription activation, tester distribution, release/deployment or real-money provider activation is authorized.
