# AAI-07 Governed Start — 2026-08-27

AAI-07 — Game Event, Scene & Automation Binding — is governed-started from AIOC `ca9d9b71ccc6456b4ec7d269a8f3992ac928eb63` and application `fb8cae52fd5bf9eaf0cf826bd9f19dd65a9e4884` after fresh verification and the required AAI-01..06 re-read.

The bounded implementation branch is `integration/aai-07-game-event-scene-automation-binding`.

AAI-07 may consume existing canonical gameplay owner references and immutable caller-supplied gameplay signals, and map them to existing AAI-02 cue/soundscape identities and completed AAI-04/05/06 audio behavior. Audio output is presentation/support state only and may not create, rewrite, advance, cancel, or otherwise mutate World, Scene/Tabletop, Event, Combat/Exploration, Action, Visibility/Permissions, or D29 authoring-provenance truth.

## Resolved deterministic binding contract

- Supported gameplay signal classes are `event`, `scene-enter`, `scene-exit`, and `automation-output`; every signal carries an existing AAI-02 owner reference and stable caller signal identity.
- Bindings target only existing AAI-02 `cueId` or `soundscapeId`; no provider-native identity becomes gameplay identity.
- Matched bindings execute in ascending authored `order`, with stable `bindingId` as deterministic tie-break.
- Idempotency is keyed by stable `signalId + bindingId`; caller-supplied previously-applied keys produce explicit nonblocking duplicate receipts and no second audio action.
- Scene-enter may start a scene-lifetime binding. Scene-exit may cancel only caller-supplied active audio handles previously associated with the same canonical Scene/Tabletop owner reference; cancellation cannot mutate scene state.
- Explicit cancellation produces presentation-only stop requests. Missing/unknown active handles fail closed as nonblocking no-op receipts.
- Unresolved or unavailable audio remains nonblocking. AAI-05 semantic selection and AAI-04 playback outcomes remain binding; AAI-07 cannot promote rights, capability, terms/entitlement, semantics, runtime availability, or AAI-06 adapter authority.
- No provider call, content acquisition, credential storage, scraping, reverse engineering, payment, release, or deployment is authorized.

## Persistence decision

No durable canonical AAI-07 runtime ledger is required. Authored binding definitions are repository/caller-owned declarative configuration; applied idempotency keys and active audio handles are ephemeral/caller-owned runtime inputs. Migration `0022` remains unreserved.

## Acceptance

The exact final application candidate must pass focused AAI-07 invariant verification, client typecheck, focused integration regression, AAI-06/05/04/03/02/01 predecessor verifiers, MIB-11/D18 World-owner regression, Repository Health, self-hosted Linux and Windows AAI-07 Validation Core, and deterministic Windows/Linux cross-platform comparison before merge.
