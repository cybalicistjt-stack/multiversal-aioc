# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-07  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-06  
**Current item:** AAI-07 — Game Event, Scene & Automation Binding  
**Implementation branch:** `integration/aai-07-game-event-scene-automation-binding`  
**Implementation authority:** bounded AAI-07 only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 through AAI-06 are `completed_verified`. AAI-07 is governed-started `in_progress` after fresh verification of AIOC `ca9d9b71ccc6456b4ec7d269a8f3992ac928eb63` and application `fb8cae52fd5bf9eaf0cf826bd9f19dd65a9e4884`, the required predecessor reread, and resolution of the bounded deterministic gameplay-signal-to-audio binding contract.

## AAI-07 governed contract

AAI-07 may consume immutable existing gameplay signals from canonical World, Scene/Tabletop, Event, Combat/Exploration, Action, Visibility/Permissions and D29 authoring-provenance owners. Supported signal classes are `event`, `scene-enter`, `scene-exit`, and `automation-output`. Every signal carries a stable caller `signalId` and an existing AAI-02 owner reference. Audio remains presentation/support state and never creates, rewrites, advances, cancels or persists gameplay truth.

Bindings match explicit canonical owner authority/stable ID plus signal class and target only existing AAI-02 `cueId` or `soundscapeId`. Matched bindings execute in ascending authored `order` with stable `bindingId` tie-break. Provider-native identities never become gameplay binding keys.

Idempotency is deterministic and caller-fed: `signalId + bindingId`. Previously applied keys produce explicit duplicate-suppressed nonblocking receipts. AAI-07 owns no durable idempotency ledger.

Scene-enter may start scene-lifetime presentation behavior. Scene-exit may generate presentation-only stop requests only for caller-supplied active audio handles associated with the same canonical Scene/Tabletop owner reference. Missing, unknown or mismatched handles fail closed to nonblocking no-op receipts and cannot mutate scene state.

AAI-05 semantic resolution and AAI-04 playback/layer/mixer outcomes remain binding. Unresolved, silent, manual, unavailable and degraded audio remain nonblocking. AAI-02 rights/provenance, AAI-03 capability, current provider terms/entitlement, AAI-05 semantic/runtime evidence and AAI-06 adapter/provider restrictions remain independent and fail closed.

No durable AAI-07 canonical runtime persistence is required. Authored binding definitions are repository/caller-owned declarative configuration; applied idempotency keys and active audio handles are ephemeral/caller-owned runtime inputs. Migration `0022` remains unreserved.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `completed_verified`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `completed_verified`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `completed_verified`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `completed_verified`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `in_progress`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Acceptance

AAI-07 completion requires the exact candidate head to pass focused AAI-07 invariant verification, client TypeScript typecheck, focused AAI-07 integration regression, AAI-06/05/04/03/02/01 predecessor verifiers, MIB-11/D18 World-owner regression, application Repository Health, self-hosted Linux and Windows AAI-07 Validation Core, and deterministic cross-platform comparison.

## Invariants

- AAI-01 through AAI-06 are `completed_verified` with no further implementation authority.
- AAI-07 is `in_progress` only on `integration/aai-07-game-event-scene-automation-binding`.
- Audio may react to canonical gameplay truth but cannot create or mutate it.
- Rights/provenance, capability, terms/entitlement, semantic compatibility, runtime availability and AAI-06 provider restrictions remain independently fail closed.
- Unavailable audio remains nonblocking.
- Migration `0022` remains unreserved.
- No payment/subscription activation, tester distribution, release/deployment or real-money provider activation is authorized.
