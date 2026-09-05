# VTI — Virtual Tabletop Interoperability

**Program ID:** VTI  
**Status:** OWNER-APPROVED — VTI-01 THROUGH VTI-03 COMPLETED_VERIFIED; VTI-04 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ALP-08  
**Successor:** SGC-01  
**Owner and final authority:** John Brandon Turner

## Current state

VTI-01 — VTT Ecosystem, Licensing & Capability Matrix — is `completed_verified` and retired.

VTI-02 — Multiversal External Game Projection Contract — is `completed_verified` and retired. Application PR #416 was squash-merged as `01aa25d60ad71e5ed318b9680f859c6927a90541` after exact-head Linux/Windows/comparator GREEN.

VTI-03 — Stable Identity, Versioning & Synchronization — is `completed_verified`. Genuine matching acceptance RED was sealed from exact application head `fdb9139a5c75e30b03af16dec9815287eebcc763` in run `33991472091`: Linux and Windows both failed at `vti03-invariants` because the production contract was intentionally absent, while deterministic comparison passed with receipt `8337ef2af2cfe67ebf3acaf6aceac2593267bdf26c1f3eccd79d5bf22e8c7ba1`. Final exact-head GREEN was established at `47d08c706fcafdfb7cb602e3e19a43eef85b6896` in run `33992208512`: repository health, self-hosted Linux, self-hosted Windows and deterministic cross-platform comparison all passed with receipt `af6bf644b06ea1e9ac28f60226f939195d67c89bf88fb622c66dfc8544d54e25`. Application PR #417 was squash-merged as `56ab87c2be214d4d7edb15e0e8d02429a07ee2d4`.

VTI-03 implementation authority is retired. Its completed provider-neutral deterministic contract preserves Multiversal canonical authority, stable external-object mappings, fingerprints, version negotiation, stale/conflict handling, reconnect, deduplication, tombstones, MIB-03 status-before-retry/receipt replay/fail-closed recovery semantics, and visibility/ownership/consent/GM-authority metadata without performing live external synchronization or durable persistence.

VTI-04 — Rules Action & Roll Bridge — is the strict successor and is `selected_not_started` as `VTI-04-attempt-001` from exact application main `56ab87c2be214d4d7edb15e0e8d02429a07ee2d4`. No branch, acceptance package, production mutation or bridge implementation is authorized before a separately validated governed start.

## Purpose

VTI lets compatible external VTTs present and interact with Multiversal campaigns at the deepest level each platform safely permits, while Multiversal remains the canonical rules/campaign authority.

Integration levels are capability-driven:
- Level 1: export/content pack;
- Level 2: synchronized companion;
- Level 3: native Multiversal VTT system/rules package where the platform supports it.

VTI follows the native mine-note-derived semantic families so adapters project mature native state rather than becoming the first implementation of spatial semantics, knowledge/familiarity, organization dynamics, microgames or learning/achievement behavior.

## Tranches

1. **VTI-01 — VTT Ecosystem, Licensing & Capability Matrix** — **COMPLETED_VERIFIED**.  
   Evidence-backed deterministic classification of target-platform system/rules packages, modules/plugins, sheets, compendiums, maps/scenes, automation, APIs/live communication, import/export and distribution constraints. Capability remains explicit as supported, unsupported, conditional or unknown, with source provenance and no vendor selection.

2. **VTI-02 — Multiversal External Game Projection Contract** — **COMPLETED_VERIFIED**.  
   Provider-neutral Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference projections with canonical source references, explicit `present`, `redacted` or `unsupported` availability, preserved visibility/ownership/consent/GM-authority metadata, deterministic normalization and deterministic receipts.

3. **VTI-03 — Stable Identity, Versioning & Synchronization** — **COMPLETED_VERIFIED**.  
   Provider-neutral external-object mappings, fingerprints, version negotiation, stale/conflict handling, reconnect, deduplication, tombstones and MIB-03 retry/recovery semantics. Live external synchronization mutation, provider-specific schemas and durable VTI persistence remain outside the completed contract.

4. **VTI-04 — Rules Action & Roll Bridge** — **SELECTED_NOT_STARTED**.  
   Future governed-start scope: VTT request → Multiversal validation/resolution → authoritative owner receipts/result → VTT presentation for rolls, attacks, checks, powers, resources, conditions, initiative, reactions and GM adjudication. No implementation authority exists yet.

5. **VTI-05 — Character Sheet, Item & Compendium Projection**  
   Present Characters, NPCs, creatures, equipment, powers, conditions, rules references, roll tables and vehicles in platform-native forms where supported.

6. **VTI-06 — Scene, Map, Token & MAI Bridge**  
   Translate Multiversal Scene + MAI/ISE/SSA projections to maps, tokens, walls, doors, lighting, grid/elevation/notes and GM-only material supported by the target VTT.

7. **VTI-07 — Permissions, Hidden Information & GM Authority**  
   Preserve ownership, consent, GM adjudication and hidden-information filtering across external clients; prevent hidden counts/content leakage.

8. **VTI-08 — Adapter SDK, Capability Manifest & Deterministic Reference VTT**  
   Define the adapter SDK and a fake/reference VTT so the entire integration contract can be tested without a commercial platform.

9. **VTI-09 — First Full Platform Integration**  
   Select the best supported platform at implementation time based on current APIs/licensing; deliver the first deep playable integration without precommitting the roadmap to a vendor.

10. **VTI-10 — Additional VTT Adapters & Compatibility Matrix**  
    Add feasible platforms at the maximum safe level each supports and publish a precise capability matrix rather than vague “VTT compatible” claims.

11. **VTI-11 — Adventure / Campaign Package Export**  
    Export maps, encounters, creatures, NPCs, tokens, journals/handouts, treasure, tables, environments and other permitted content into platform package formats.

12. **VTI-12 — Integrated Cross-VTT Golden Proof**  
    Prove one governed adventure resolves the same authoritative events natively and through an external VTT projection, including reconnect, stale/duplicate requests, GM adjudication and hidden information.

## VTI-03 completed contract

VTI-03 established:
- stable provider-neutral bindings between canonical `sourceObjectId` references and derivative `externalObjectId` references;
- deterministic canonical/external fingerprints and expected-version gating;
- deterministic `create`, `unchanged`, `update`, `stale`, `conflict` and `tombstone` decisions;
- highest-mutually-supported protocol version negotiation without manufacturing unsupported compatibility;
- MIB-03-derived `status-before-retry`, receipt replay, retry, reconnect-status-before-retry and fail-closed idempotency-conflict semantics;
- preserved visibility, ownership, consent and GM-authority metadata;
- deterministic normalization and receipts independent of supplied mapping order;
- explicit proof that no provider-specific schema, credentials/accounts, adapter, live external/canonical mutation, hidden-information bypass, durable VTI persistence, new migration, provider activation, tester distribution, release/deployment or VTI-04+ implementation occurred.

Sealed completion evidence:
- acceptance RED head `fdb9139a5c75e30b03af16dec9815287eebcc763`, run `33991472091`, Linux job `101374374550`, Windows job `101374374562`, comparator job `101374421980`, receipt `8337ef2af2cfe67ebf3acaf6aceac2593267bdf26c1f3eccd79d5bf22e8c7ba1`;
- final GREEN head `47d08c706fcafdfb7cb602e3e19a43eef85b6896`, run `33992208512`, repository-health job `101376327007`, Linux job `101376342387`, Windows job `101376342347`, comparator job `101376421747`, receipt `af6bf644b06ea1e9ac28f60226f939195d67c89bf88fb622c66dfc8544d54e25`;
- application PR #417 merge `56ab87c2be214d4d7edb15e0e8d02429a07ee2d4`.

## VTI-04 selection boundary

VTI-04 is selected only from exact application main `56ab87c2be214d4d7edb15e0e8d02429a07ee2d4`.

Until a separate governed start validates and merges:
- no VTI-04 application branch exists;
- `implementation_authority`, `acceptance_package_authorized` and `production_mutation_authorized` remain `false`;
- rules-action and roll bridging remains unimplemented;
- provider-specific schemas, credentials, external accounts, adapters and platform selection remain unauthorized;
- live external synchronization/canonical mutation, durable VTI persistence and any new migration remain unauthorized;
- Platform selection remains evidence-driven and deferred to VTI-09;
- hidden information may not be manufactured or bypassed;
- VTI-05+ and SGC-01+ remain unauthorized.

## Invariants

- External VTTs are clients/projections, not replacement rules authorities.
- External mutations become governed proposals/operations where authoritative Multiversal state is affected.
- Capability manifests control feature exposure; unsupported fidelity is explicit.
- No VTT adapter may bypass visibility, ownership, consent or GM authority.
- No vendor is selected by roadmap text; Platform selection remains evidence-driven at VTI-09.
- Native SSA/KFR/ODL/MAL/ALP state is projected only where a platform supports it; VTI does not recreate those systems externally.
- VTI-01 through VTI-03 are frozen completed_verified with implementation authority retired.
- VTI-04 is selected_not_started with no branch, acceptance or production authority.
- VTI-05+ and SGC-01+ remain unauthorized until their own governed selections and starts.
