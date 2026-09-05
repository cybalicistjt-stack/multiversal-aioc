# VTI — Virtual Tabletop Interoperability

**Program ID:** VTI  
**Status:** OWNER-APPROVED — VTI-01 THROUGH VTI-04 COMPLETED_VERIFIED; VTI-05 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ALP-08  
**Successor:** SGC-01  
**Owner and final authority:** John Brandon Turner

## Current state

VTI-01 — VTT Ecosystem, Licensing & Capability Matrix — is `completed_verified` and retired.

VTI-02 — Multiversal External Game Projection Contract — is `completed_verified` and retired. Application PR #416 was squash-merged as `01aa25d60ad71e5ed318b9680f859c6927a90541` after exact-head Linux/Windows/comparator GREEN.

VTI-03 — Stable Identity, Versioning & Synchronization — is `completed_verified` and retired. Application PR #417 was squash-merged as `56ab87c2be214d4d7edb15e0e8d02429a07ee2d4` after exact-head Linux/Windows/comparator GREEN.

VTI-04 — Rules Action & Roll Bridge — is `completed_verified` and retired. Genuine matching acceptance RED was sealed from exact application head `c9a3cc09aa9ce6ce2ca55c35df7ba7032ffb7126` in run `33993535896`: Linux and Windows both failed at `vti04-invariants` because the production contract was intentionally absent, while deterministic comparison passed with receipt `ee79438a64ccaccabe8acd2953df5f911d1e0ee8b92352952b3026ede1d0e028`. Final exact-head GREEN was established at `8806fce4a0143281942dd2d68a23301c70501999` in run `33994055604`: repository health, self-hosted Linux, self-hosted Windows and deterministic cross-platform comparison all passed with receipt `766e06c3f2de74e4cbee599fa56c3d88e4a49fe98481b7f65f70d30a5970050c`. Application PR #418 was squash-merged as `295424982135337de80cccfac072764ab35183cc`.

VTI-04 completed the provider-neutral VTT request → Multiversal validation/resolution → authoritative result/receipt → VTT presentation bridge for roll, attack, check, power, resource, condition, initiative, reaction and GM-adjudication actions. Multiversal remains the rules and authoritative RNG authority. Duplicate/idempotent requests reuse completed VTI-03/MIB-03 receipt replay, status-before-retry and fail-closed semantics. Visibility, ownership, consent, hidden-information filtering and GM authority remain preserved.

VTI-05 — Character Sheet, Item & Compendium Projection — is the strict successor and is `selected_not_started` as `VTI-05-attempt-001` from exact application main `295424982135337de80cccfac072764ab35183cc`. No VTI-05 branch, acceptance package, production mutation or provider integration is authorized before a future governed start validates and merges.

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

4. **VTI-04 — Rules Action & Roll Bridge** — **COMPLETED_VERIFIED**.  
   Provider-neutral VTT request → Multiversal validation/resolution → authoritative receipt/result → VTT presentation semantics for rolls, attacks, checks, powers, resources, conditions, initiative, reactions and GM adjudication. External VTTs remain request/presentation clients and do not become rules or RNG authorities. Duplicate requests replay authoritative receipts or status-check before retry rather than resolving twice.

5. **VTI-05 — Character Sheet, Item & Compendium Projection** — **SELECTED_NOT_STARTED**.  
   Present Characters, NPCs, creatures, equipment, powers, conditions, rules references, roll tables and vehicles in platform-native forms where supported. Selection only: no implementation branch or projection mutation is authorized before its governed start.

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

## VTI-04 completed contract

VTI-04 established:
- provider-neutral request envelopes for `roll`, `attack`, `check`, `power`, `resource`, `condition`, `initiative`, `reaction` and `gm-adjudication` actions;
- canonical source-object and actor references plus expected canonical version/fingerprint checks used to reject stale requests;
- deterministic authorization/validation dispositions before canonical resolution;
- a Multiversal-owned resolution handoff in which the external VTT never becomes rules or RNG authority;
- authoritative result/receipt envelopes and deterministic VTT presentation envelopes;
- explicit `present`, `redacted` and `unsupported` result-field fidelity without manufacturing hidden information;
- preserved visibility, ownership, consent and GM-authority metadata;
- completed VTI-03/MIB-03 authoritative receipt replay, status-before-retry and fail-closed same-idempotency conflict behavior;
- deterministic normalization and receipts independent of supplied request ordering;
- explicit proof that no provider-specific schema, credentials/accounts, adapter, live external/canonical mutation, hidden-information bypass, durable VTI persistence, new migration, provider activation, tester distribution, release/deployment or VTI-05+ implementation occurred.

Sealed completion evidence:
- acceptance RED head `c9a3cc09aa9ce6ce2ca55c35df7ba7032ffb7126`, run `33993535896`, repository-health job `101379876588`, Linux job `101379894331`, Windows job `101379894324`, comparator job `101379945379`, receipt `ee79438a64ccaccabe8acd2953df5f911d1e0ee8b92352952b3026ede1d0e028`;
- final GREEN head `8806fce4a0143281942dd2d68a23301c70501999`, run `33994055604`, repository-health job `101381251547`, Linux job `101381267156`, Windows job `101381267141`, comparator job `101381348850`, receipt `766e06c3f2de74e4cbee599fa56c3d88e4a49fe98481b7f65f70d30a5970050c`;
- application PR #418 merge `295424982135337de80cccfac072764ab35183cc`;
- historical profile fanout `0` and application-feature repair cycles `0`.

## VTI-05 selection boundary

VTI-05 is selected only from exact application main `295424982135337de80cccfac072764ab35183cc`.

A future governed start may bound:
- Character, NPC and creature projection into supported platform-native sheets/actors;
- equipment, powers, conditions and RuleReference projection with canonical source references;
- roll-table and vehicle projection where the target platform supports those forms;
- explicit `present`, `redacted` and `unsupported` fidelity rather than manufacturing unsupported data;
- visibility, ownership, consent, hidden-information filtering and GM-authority preservation;
- deterministic normalization, invariant validation and receipts needed to prove the projection contract.

Until that governed start validates and merges:
- `implementation_authority`, `branch_creation_authorized`, `acceptance_package_authorized` and `production_mutation_authorized` remain `false`;
- no VTI-05 application branch may be created;
- provider-specific schemas, credentials, external accounts, adapters and platform selection remain unauthorized;
- live external synchronization/canonical mutation, durable VTI persistence and any new migration remain unauthorized;
- Platform selection remains evidence-driven and deferred to VTI-09;
- hidden information may not be manufactured or bypassed;
- VTI-06+ and SGC-01+ remain unauthorized.

## Invariants

- External VTTs are clients/projections, not replacement rules authorities.
- External mutations become governed proposals/operations where authoritative Multiversal state is affected.
- Capability manifests control feature exposure; unsupported fidelity is explicit.
- No VTT adapter may bypass visibility, ownership, consent or GM authority.
- No vendor is selected by roadmap text; Platform selection remains evidence-driven at VTI-09.
- Native SSA/KFR/ODL/MAL/ALP state is projected only where a platform supports it; VTI does not recreate those systems externally.
- VTI-01 through VTI-04 are frozen completed_verified with implementation authority retired.
- VTI-04 external VTT request/presentation clients may not independently resolve Multiversal rules, supply authoritative RNG outcomes, or autonomously exercise GM adjudication.
- Duplicate external requests may not resolve twice when an authoritative receipt can be replayed or status checked.
- VTI-05 is selected_not_started and has no implementation branch or mutation authority.
- VTI-06+ and SGC-01+ remain unauthorized until their own governed selections and starts.
