# AAI — Audio Asset & Soundscape Interoperability

**Program ID:** AAI  
**Status:** IN PROGRESS — AAI-06  
**Activation:** MAI-10 completed_verified  
**Completed through:** AAI-05  
**Current item:** AAI-06 — Import/Link Framework & Initial Provider Adapters  
**Implementation branch:** `integration/aai-06-import-link-initial-provider-adapters`  
**Implementation authority:** bounded AAI-06 only  
**Successor:** ISE-01  
**Owner and final authority:** John Brandon Turner

## Current state

AAI-01 through AAI-05 are `completed_verified`. AAI-06 is governed-started `in_progress` after fresh verification of AIOC `356fe15b165cfa6e58e0f2c1e77be2bb67717557` and application `511f9566af10f0defa703350ac4ffa6db0c0c4e7`, the required predecessor reread, and a fresh provider API/terms evidence check.

AAI-06 authority is limited to provider-safe import/link planning and the initial adapter set below. Rights/provenance, capability, current provider terms/entitlement, semantic compatibility and runtime availability remain independent fail-closed evidence dimensions.

## Completed foundation

- **AAI-01:** provider/API/license/authority evidence and fail-closed capability states.
- **AAI-02:** canonical provider/source/asset/reference/intent/cue identities and operation-specific rights.
- **AAI-03:** provider-neutral adapter descriptors and capability negotiation.
- **AAI-04:** provider-neutral playback/layer/mixer outcomes; unavailable audio remains nonblocking.
- **AAI-05:** deterministic provider-neutral semantic taxonomy and availability resolution.

AAI-05 exact completion remains application PR #329, validated head `22ed48f92ee72be2e136e780e24236dd37e2fb4d`, deterministic receipt `7e55e9ed29f8fefb42ab8244cafed057631f5cf8c63efee0b95a29d1d668b85e`, squash merge `511f9566af10f0defa703350ac4ffa6db0c0c4e7`.

## AAI-06 governed contract

### Import versus link

`local-import` is limited to caller-selected user-owned local content/reference where AAI-02 `reference` and `ingest` evidence is explicitly allowed. Local possession never grants export, record, stream, redistribution, public-performance or commercial rights. Runtime media probing and provenance/license evidence remain required.

`provider-link` preserves AAI-02 provider/source/reference identities or explicit caller-supplied non-secret provider identifiers. A link never implies entitlement, ownership, play rights, ingest rights or copy rights.

Every operation remains independently mapped to its AAI-02 right: reference→`reference`, local import→`ingest`, playback/control→`play`, cache→`cache`, export→`export`, record→`record`, stream→`stream`, redistribution→`redistribute`, transform→`transform`.

### Initial adapter set

1. **User-owned local audio — local-file import.** Explicit provenance/license evidence and runtime media probe required. No inferred downstream rights.
2. **Syrinscape — documented API link/control.** Current official HTTP/iframe/JavaScript API evidence was rechecked at governed start. Runtime token/session material is caller-supplied and never stored in source, deterministic receipts or persistence. Catalog/search/session/playback descriptors remain independently rights/capability/entitlement gated. Background or bulk crawling is outside authority. The existing starter Syrinscape asset remains non-playable where its AAI-02 `play` right is `unknown`.
3. **Tabletop Audio — browser-local companion control.** Authority is limited to the documented localhost companion/control path. SoundPad audio remains site-bound and may not be downloaded, extracted, cached, copied or rehosted.
4. **TableTone — manual external reference only.** Current terms keep provider assets played through TableTone and prohibit extraction/external playback. No public API is inferred.
5. **Pocket Bard — manual external reference only.** Current terms do not authorize ripping, scraping or reverse engineering. Record/stream rights do not create programmatic API capability.

### Credentials and transport

AAI-06 deterministic code produces request plans/descriptors and uses injected transports. CI uses provider-safe fakes only and performs no live provider authentication or calls. Credential material, provider responses, wall-clock/network state and machine secrets are excluded from deterministic receipts.

### Semantic and gameplay boundaries

AAI-05 semantic selection remains provider-neutral input. An adapter cannot alter semantic ranking, silently substitute another provider asset, grant rights/capability or create gameplay truth. World, Event, Scene, Combat, Action, Visibility/Permissions and D29 owners remain canonical. AAI-07 remains the owner of later event/scene/automation binding.

### Persistence

No durable AAI-06 canonical persistence is required. Import/link plans, provider request descriptors and receipts are derived runtime/caller-owned values over existing AAI-02 identities. Migration `0022` remains unreserved.

## Explicit exclusions

AAI-06 does not authorize TableTone or Pocket Bard API automation; scraping, reverse engineering or ripping; provider content extraction/copying/caching absent explicit independent rights and a separately authorized path; credential persistence; background catalog crawling; payment/subscription activation; AAI-07 gameplay binding; migration `0022`; tester distribution; release or deployment.

## Validation acceptance

AAI-06 completion requires the exact candidate head to pass focused `tools/verify_aai_06.py`, client TypeScript typecheck, focused AAI-06 Vitest regression, AAI-05/04/03/02/01 predecessor verifiers, MIB-11/D18 World-owner regression, application Repository Health, self-hosted Linux and Windows AAI-06 Validation Core, and deterministic cross-platform comparison. Validation remains provider-account/network independent.

## Tranches

1. **AAI-01 — Audio Ecosystem, API, License & Authority Survey** — `completed_verified`  
2. **AAI-02 — Canonical Audio Source, Asset, Cue & Soundscape Schema** — `completed_verified`  
3. **AAI-03 — Provider Adapter & Capability-Negotiation Framework** — `completed_verified`  
4. **AAI-04 — Playback, Layering & Mixer Engine** — `completed_verified`  
5. **AAI-05 — Semantic Audio Taxonomy & Availability Resolver** — `completed_verified`  
6. **AAI-06 — Import/Link Framework & Initial Provider Adapters** — `in_progress`  
7. **AAI-07 — Game Event, Scene & Automation Binding** — `planned`  
8. **AAI-08 — GM Audio Workbench, Scene Presets & Campaign Preparation** — `planned`  
9. **AAI-09 — Multiplayer, Permissions, Remote Sync & Recording/Streaming Boundaries** — `planned`  
10. **AAI-10 — Multi-Provider Golden Audio Proof** — `planned`

## Invariants

- AAI-01 through AAI-05 are `completed_verified` with no further implementation authority.
- AAI-06 is `in_progress` only on `integration/aai-06-import-link-initial-provider-adapters`.
- AAI-02 operation rights/provenance, AAI-03 capability, current provider terms/entitlement, AAI-05 semantic compatibility and runtime availability remain independently fail closed.
- No provider/catalog is canonical and a provider reference never implies entitlement or ownership.
- Unsupported operations cannot be emulated by scraping, reverse engineering or prohibited copying.
- Audio remains presentation/support state, not canonical World/Event/Scene/Combat/Action/Visibility truth.
- Migration `0022` remains unreserved.
- No payment/subscription activation, tester distribution, release/deployment or real-money provider activation is authorized.
