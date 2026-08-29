# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-10 proof-integrity recovery
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-09  
**Current item:** AAI-10 — Multi-Provider Golden Audio Proof  
**Implementation branch:** `codex/aai-10-proof-integrity-repair`
**Implementation authority:** bounded AAI-10 only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 through AAI-09 are `completed_verified`.

AAI-09 merged through application PR #335 after exact-head Repository Health run `33105829485` and bounded current-tranche Validation Core run `33105829803` passed on candidate `d68ce494e6b97a6bc6b7b6d60f58d2985f3bfac2`. Linux job `98635420855`, Windows job `98635420917`, and deterministic cross-platform comparison job `98635585515` all succeeded, with zero unrelated historical profile fanout. Its application merge is `b670368ca91778802867a1a4b8d963c3a3ea8875`.

Subsequent repository-health maintenance advanced live application `main` to `d007dc980c63a7beab4ab9a4ddbc67525f8d7003` without changing AAI-09 completion. AIOC `main` at governed start is `a1af60bf66399654091de1cf3cdc0a9eb2084459`.

Application PR #338 merged its first AAI-10 candidate as `58fabcf29e164fd4e3eb278334d385dd9970159d`, but an owner-reported platform usage-ceiling interruption ended the prior execution before AIOC closeout. The original implementation branch was deleted while AIOC still selected it as `in_progress`, creating a stop-the-line `repository_state` defect.

Independent review then found three bounded proof-integrity gaps: `pathId` was not bound to its governed source/adapter pair; duplicate scenario IDs could make receipt order input-dependent; and the starter proof omitted capability/entitlement fail-closed outcomes plus explicit negative evidence for every path family. AAI-10 therefore remains `in_progress` with recovery authority only on `codex/aai-10-proof-integrity-repair`. Unrelated feature starts remain blocked until the repaired exact head passes the one AAI-10 profile, merges, and AIOC records `completed_verified` plus ISE-01 `selected_not_started`.

## Completed AAI-09 boundary

AAI-09 established deterministic, non-authoritative multiplayer audio permission, presentation-only remote-synchronization, and recording/streaming boundary decisions over completed AAI-01..08 and canonical A5/Visibility permission evidence.

- Audio cannot grant, revoke, infer, or mutate gameplay, identity, session, or permission truth.
- Remote sync remains deterministic presentation intent only, with duplicate/stale suppression and no peer, network, or provider transport.
- Recording remains capability-unmodeled and fail closed because AAI-03 defines no recording capability key.
- Streaming may become intent-ready only with independent AAI-02 stream rights, selectable AAI-03 capability, canonical permission, and explicit participant consent. Intent-ready is not media-capture or transmission authority.
- Export and redistribution remain independent rights and are not implied by record/stream permission.
- Raw consent text, credentials, tokens, recordings, and media bytes remain outside deterministic receipts.
- No new durable AAI-09 canonical persistence was required; migration `0022` remains unreserved.

AAI-09 required two concrete evidence-driven repairs before final validation: deterministic receipt ordering was made total by adding `requestId` as the final tie-break, then the focused regression was corrected to prohibit an actual serialized `rawConsentText` field without rejecting the explicit safe marker `rawConsentTextStored:false`. The final exact head passed all governed gates before merge.

## AAI-10 governed start contract

AAI-10 proves interoperability across independently governed audio source/provider paths without weakening any completed AAI boundary. Its exact provider/source matrix is frozen as follows, with **all paths proven through repository fixtures/test doubles only**:

1. **User-owned local audio** — positive local import/reference semantics with explicit rights and a supported runtime probe; unknown runtime or downstream rights fail closed. No user media bytes are committed.
2. **Syrinscape documented API path** — positive provider link/reference request semantics using documented capability evidence, but no token or network execution. Existing canonical AAI-02 playback rights remain unknown and cannot be upgraded by capability evidence.
3. **Tabletop Audio browser/local companion** — positive browser/local companion control-plan semantics only. SoundPad content remains site-bound; control does not imply extraction, download, cache, rehosting or redistribution.
4. **TableTone** — manual external-reference/app-handoff only. No public programmatic API, external playback, extraction or content acquisition is inferred.
5. **Pocket Bard** — manual external-reference/app-handoff only. Current tabletop recording/streaming license evidence does not create programmatic API authority; ripping, scraping, reverse engineering and redistribution remain prohibited/fail closed.

Fresh public provider evidence was reviewed on 2026-08-28. That review may confirm or narrow governed evidence but cannot promote canonical rights by inference.

The canonical multi-provider scenario set carries existing provider-neutral semantic intents — including `intent:cozy-fireplace`, `intent:forest-night-rain` and `intent:combat-desperate` — through distinct governed source/adapter paths. It compares canonical intent preservation, source/provenance identity, adapter identity, operation rights, capability/terms/entitlement/runtime evidence and the resulting controlled/manual/fail-closed outcome. It does not compare provider media bytes or audible waveform identity.

Credentials, tokens, provider responses, machine-local paths, raw media/content bytes, recordings and raw consent text remain outside committed deterministic evidence. Provider references never imply entitlement, ownership or broader rights.

No new durable canonical AAI-10 persistence is required. Golden scenarios and receipts are deterministic derived proof/evidence over completed AAI contracts and fixtures. Migration `0022` remains unreserved.

AAI-10 does **not** authorize paid provider activation, live credentials, provider network execution, provider content acquisition/copy/extraction/cache/rehosting, scraping/ripping/reverse engineering, rights/capability promotion, gameplay-owner mutation, actual recording/streaming/export/redistribution execution, migration `0022`, tester distribution, release or deployment.

## AAI-10 acceptance state

AAI-10 must deliver exactly this bounded proof surface:

- `governance/application-planning/audio-asset-interoperability/AAI-10_MULTI_PROVIDER_GOLDEN_AUDIO_PROOF.md`
- `packages/contracts/src/audio-asset-interoperability/multi-provider-golden-audio-proof.ts`
- `packages/contracts/src/audio-asset-interoperability/aai-10-starter-golden-audio-scenarios.ts`
- `apps/client-ui/src/aai/aai-10.multi-provider-golden-audio-proof.integration.test.ts`
- `tools/verify_aai_10.py`
- `governance/application-planning/validation-core/profiles/AAI-10.json`

The current AAI family contract seals AAI-01..09 at application baseline `b670368ca91778802867a1a4b8d963c3a3ea8875`. Exactly one governed `AAI-10` current-family profile must prove deterministic provider-neutral intent preservation across all five source/provider paths; authorized positive local/link/local-companion/manual-reference outcomes; explicit rights/capability/terms/entitlement/runtime fail-closed outcomes; zero live provider/network/content execution; nonblocking unavailable audio; and deterministic input-order-independent receipts. It contains only the AAI-10 invariant verifier, workspace install, client typecheck and focused AAI-10 regression. Historical AAI-01..09 and MIB-11 verifier reruns remain retired at zero; the selector proves sealed-baseline ancestry instead.

The exact candidate head must pass current application Repository Health, self-hosted Linux, self-hosted Windows and deterministic cross-platform comparison before merge.

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
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `in_progress_recovery`

## Invariants

- AAI-01 through AAI-09 remain `completed_verified` with no further implementation authority.
- AAI-10 recovery implementation authority exists only on `codex/aai-10-proof-integrity-repair`.
- Completed AAI permission, rights, capability, availability, provider, binding, preparation, multiplayer, sync, consent and capture boundaries remain independently authoritative and fail closed.
- User-owned local audio and provider-backed audio converge only through canonical AAI contracts and explicit provenance/right/capability evidence.
- Provider playback, reference or control success cannot imply broader rights, terms, entitlement, remote-sync, recording, streaming, export, redistribution or payment authority.
- Unavailable audio remains nonblocking.
- Paid provider activation, live credential use, provider network execution, scraping/reverse engineering and unauthorized content-byte acquisition remain forbidden.
- Migration `0022` remains unreserved.
- No tester distribution, release/deployment or real-money provider activation is authorized.
