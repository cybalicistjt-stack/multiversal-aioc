# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-10 governed-started  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-09  
**Current item:** AAI-10 — Multi-Provider Golden Audio Proof  
**Implementation branch:** `integration/aai-10-multi-provider-golden-audio-proof`  
**Implementation authority:** bounded AAI-10 only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 through AAI-09 are `completed_verified`. AAI-10 is now `in_progress` after the owner `Continue` command completed its required planning/start resolution against fresh application main `d007dc980c63a7beab4ab9a4ddbc67525f8d7003` and AIOC main `a1af60bf66399654091de1cf3cdc0a9eb2084459`.

AAI-09 merged through application PR #335 after exact-head Repository Health run `33105829485` and bounded current-tranche Validation Core run `33105829803` passed on candidate `d68ce494e6b97a6bc6b7b6d60f58d2985f3bfac2`. Its permission, remote-sync, recording/streaming and nonblocking-audio boundaries remain binding.

## AAI-10 governed proof matrix

AAI-10 proves interoperability across five independently governed source/provider paths, all through repository fixtures/test doubles only:

1. **User-owned local audio** — positive local import/reference semantics with explicit rights and a supported runtime probe; unknown runtime or downstream rights fail closed. No user media bytes are committed.
2. **Syrinscape documented API path** — positive provider link/reference request semantics using documented capability evidence, but no token or network execution. Existing canonical AAI-02 playback rights remain unknown and cannot be upgraded by capability evidence.
3. **Tabletop Audio browser/local companion** — positive browser/local companion control-plan semantics only. SoundPad content remains site-bound; control does not imply extraction, download, cache, rehosting or redistribution.
4. **TableTone** — manual external-reference/app-handoff only. No public programmatic API, external playback, extraction or content acquisition is inferred.
5. **Pocket Bard** — manual external-reference/app-handoff only. Current tabletop recording/streaming license evidence does not create programmatic API authority; ripping, scraping, reverse engineering and redistribution remain prohibited/fail closed.

Fresh public provider evidence was reviewed on 2026-08-28. That review may confirm or narrow governed evidence, but cannot promote canonical rights by inference.

## Canonical golden scenario rule

Each golden scenario carries an existing provider-neutral AAI semantic intent plus one governed source/adapter path. The proof compares canonical intent preservation, source/provenance identity, adapter identity, operation rights, capability/terms/entitlement/runtime evidence and the resulting controlled/manual/fail-closed outcome. It does **not** compare provider media bytes or audible waveform identity.

The governed semantic intent set includes `intent:cozy-fireplace`, `intent:forest-night-rain` and `intent:combat-desperate`. Missing or unavailable audio remains nonblocking.

## Live-versus-fixture authority

AAI-10 completion requires no live provider account. All provider/source proofs use repository fixtures/test doubles. Live credentials, subscriptions, provider network requests, authenticated catalog calls, playback calls and provider content-byte transfers are not authorized and are excluded from deterministic evidence.

## Persistence

AAI-10 introduces no new durable canonical persistence. Golden scenarios and receipts are deterministic derived proof/evidence over completed AAI contracts and fixtures. Migration `0022` remains unreserved.

## Security, rights and owner boundaries

Credentials, tokens, provider responses, machine-local paths, raw media/content bytes, recordings and raw consent text remain outside committed deterministic evidence. Provider references never imply entitlement, ownership or broader rights. Rights, capability, terms, entitlement, semantic/runtime availability, canonical permission and capture boundaries remain independent and fail closed. Audio cannot create or mutate World, Event, Scene, Combat, Action, identity, session, permission or other gameplay truth.

AAI-10 does not authorize provider authentication/network execution, paid provider activation, provider content acquisition/copy/extraction/cache/rehosting, scraping/ripping/reverse engineering, rights/capability promotion, actual recording/streaming/export/redistribution, migration `0022`, tester distribution, release or deployment.

## AAI-10 acceptance contract

AAI-10 must deliver exactly the bounded proof surface declared in its checkpoint:

- `governance/application-planning/audio-asset-interoperability/AAI-10_MULTI_PROVIDER_GOLDEN_AUDIO_PROOF.md`
- `packages/contracts/src/audio-asset-interoperability/multi-provider-golden-audio-proof.ts`
- `packages/contracts/src/audio-asset-interoperability/aai-10-starter-golden-audio-scenarios.ts`
- `apps/client-ui/src/aai/aai-10.multi-provider-golden-audio-proof.integration.test.ts`
- `tools/verify_aai_10.py`
- `governance/application-planning/validation-core/profiles/AAI-10.json`

Exactly one governed `AAI-10` Validation Core profile must run the focused regression plus AAI-09 through AAI-01 predecessor verifiers and MIB-11/D18 World-owner regression. The exact candidate head must pass current application Repository Health, self-hosted Linux, self-hosted Windows and deterministic cross-platform comparison before merge.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `completed_verified`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `completed_verified`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `completed_verified`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `completed_verified`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `completed_verified`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `completed_verified`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `completed_verified`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `in_progress`

## Invariants

- AAI-01 through AAI-09 remain `completed_verified` with no further implementation authority.
- AAI-10 implementation authority exists only on `integration/aai-10-multi-provider-golden-audio-proof`.
- User-owned local audio and provider-backed audio converge only through canonical AAI contracts and explicit provenance/right/capability evidence.
- Provider success cannot imply broader rights, terms, entitlement, remote-sync, recording, streaming, export, redistribution or payment authority.
- Unavailable audio remains nonblocking.
- Paid provider activation, live credential use, provider network execution, scraping/reverse engineering and unauthorized content-byte acquisition remain forbidden.
- Migration `0022` remains unreserved.
- No tester distribution, release/deployment or real-money provider activation is authorized.
