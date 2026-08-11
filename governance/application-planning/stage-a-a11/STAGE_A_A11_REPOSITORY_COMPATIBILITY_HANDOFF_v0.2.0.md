# STAGE-A-A11 Contextual AI Interfaces — Repository Compatibility Handoff v0.2.0

Status: **REPOSITORY COMPATIBILITY PREPARATION COMPLETE — NOT ACTIVATED**

Owner and final authority: **John Brandon Turner**

Prepared against:
- Multiversal-app main: `dced7f92163050690c807c1fda937146bb8dce85`
- A11 preimplementation handoff commit: `f8181dcddb47ca17ada48ff63850e2dd1094da7d`

## Artifact

`STAGE_A_A11_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`

SHA-256: `443dc2a6f74764666dafd827edf8d4ba7e27c4143cc9d50e44261ef7b0b5e473`

Nested source package:
- `STAGE_A_A11_CONTEXTUAL_AI_PREIMPLEMENTATION_v0.1.0.zip`
- SHA-256: `d6b00706621684f568555949ddb52ea6f539c7cc15f5097d7be1992dbdc96503`

Validator result:

`STAGE-A-A11 REPOSITORY COMPATIBILITY + CONTRACTS v0.2.0: PASS`

Validated counts:
- repository/predecessor anchors: 26
- blocking gaps/risks: 24
- ownership/orchestration decisions: 12
- planned provider-neutral A11 contracts: 26
- exact future path actions: 52
- source implementation slices covered: 24
- reuse/composition decisions: 18
- validation/CI lanes: 27
- implementation invariants: 33
- repository-compatibility blocking gates: 14

## Compatibility verdict

**COMPATIBLE WITH OPTIONAL PROVIDER-NEUTRAL A11 ORCHESTRATION OVER EXISTING DOMAIN CONTRACTS.**

The canonical 33-domain architecture contains no AI source-of-truth domain. A11 therefore owns only provider-neutral optional orchestration state such as capability state, consent/context preview, request/result/status identity, provenance, cost/budget policy, fallback and optional failure classification. Gameplay/content truth remains in its existing owning domains.

## Repository-specific decisions

### D08 deterministic retrieval

The current canonical search/indexing design already owns local permission-aware rules/content search, stable references and contextual links. It explicitly does not approve vector search, remote indexing or semantic AI search as baseline technology.

A11 Internal Alpha retrieval therefore consumes deterministic A2/D08 stable-ID/title/filter/reference search with authorized source/version citations. No vector database or semantic-search service is required.

### Hidden cardinality

The P9 hidden-information filter correctly authorizes before projection but exposes `hiddenEventCount`.

A11 must suppress protected existence/cardinality/topology before retrieval, token estimation, citations, provider context, cache/log/evaluation/export/notification and response assembly. Generic hidden counts are not provider-safe context.

### Audit/telemetry

The P9 structured audit envelope is provider-neutral and bounded, but A11 adds a positive safe-metadata allowlist.

Raw prompt, response, authorized context text, source prose, clue text, NPC dialogue, private notes, hidden content, credentials and provider payloads are prohibited from A11 operational telemetry.

### Provider boundary

No AI provider is selected.

A11 implementation begins with:
- `AiProviderPort`;
- `DisabledAiProviderAdapter`;
- deterministic `FixtureAiProviderAdapter` for tests;
- complete manual fallback registry.

Any external provider adapter remains a separately owner-gated integration decision. Provider SDK types, provider-native IDs, billing state and credentials cannot enter canonical domain contracts or identities.

### Persistence and retention

Do not freeze an AI transcript table during preparation.

Provider-neutral request/result/provenance/status records may be persisted only when needed and only under an explicit retention/deletion policy. Raw prompt/transcript retention, real-user evaluation-corpus use and provider retention remain disabled absent later owner authorization.

Migration `0001` remains immutable. Any future A11 storage must be the smallest additive provider-neutral design against the then-current A2-A10 schema.

### Proposal/authority boundary

AI output is nonauthoritative.

Structured output is revalidated against current permissions, source versions, dependencies, capability state and owning-domain rules before it can become an ordinary A6/A10/governed draft or proposal. AI cannot self-approve or directly commit Character, Campaign, Scene, combat, Asset, relationship, investigation, World, Adventure, pack, permission, entitlement or canonical state.

### Cost boundary

Paid execution is a distinct permission. Provider-neutral estimates, cost bands, budget owners, remaining budgets, confirmation thresholds, hard limits and dispatch reservations may be implemented without selecting a billing provider or authorizing spend.

No silent overage, duplicate paid request, blind retry or unbounded repair loop is permitted.

### Optional isolation

A build/configuration with all I1-I3 optional/experimental capabilities disabled and no provider configuration must still pass declared Internal Alpha core journeys.

Every A11-assisted core task has a deterministic manual fallback. Optional provider/tool/telemetry failure cannot partially commit or invalidate an authoritative core transaction.

## Planned portable contract root

A11 portable orchestration contracts are planned under:

`packages/contracts/src/optional-ai/`

This root is not a new canonical gameplay/content domain. It is an application-orchestration contract layer over D05/D08/A2/A3/A4-A10 public contracts.

## Holds

This handoff does **not**:
- activate A11;
- create an A11 application implementation branch;
- advance the application current-work pointer;
- select an AI provider;
- authorize provider credentials;
- authorize paid execution, billing integration or budget commitment;
- authorize real-user prompt/transcript collection or retention;
- authorize evaluation-corpus use of real-user data;
- authorize semantic/vector/remote AI search as a baseline dependency;
- authorize autonomous mutation, approval, publication, hidden reveal, combat resolution, release, deployment or canonical promotion.

A2 remains the authorized current Stage A implementation work item. A3 through A11 remain preparation-only.

## Exact next preparation step

Prepare **Stage A12 — Internal-alpha Hardening** from the completed release-design, offline/reconnect, optional-isolation, accessibility, performance, security/privacy, recovery, onboarding/help, telemetry/error-reporting and interface-consistency sources. Keep A12 unactivated and preserve A2 as the current implementation pointer.
