# VTI — Virtual Tabletop Interoperability

**Program ID:** VTI  
**Status:** OWNER-APPROVED — VTI-01 COMPLETED_VERIFIED; VTI-02 IN_PROGRESS  
**Activation:** after completed_verified ALP-08  
**Successor:** SGC-01  
**Owner and final authority:** John Brandon Turner

## Current state

VTI-01 — VTT Ecosystem, Licensing & Capability Matrix — is `completed_verified`. Application PR #415 was validated at exact head `7c377f1add2e00bbadb4007a043fee69709bd923` by self-hosted Linux, self-hosted Windows and deterministic cross-platform comparison in run `33986901523`, then squash-merged to application `main` as `027fad06d0bac3a20d56f0cc2a674581662cd1b9`. The acceptance RED remains sealed from exact head `c6bdb094499894f6b1e4b93d4910c8bbe6eb261d` / run `33986160384`.

VTI-01 implementation authority is retired. Its completed contract remains deterministic, read-only and evidence-backed: capability state is explicit as supported, unsupported, conditional or unknown; public-source provenance is preserved; no vendor was selected or ranked; no credential, external-account, adapter, synchronization, persistence, canonical-state, provider, tester, release or deployment mutation was performed.

VTI-02 — Multiversal External Game Projection Contract — is the strict successor and is `in_progress` from exact application main `027fad06d0bac3a20d56f0cc2a674581662cd1b9` as `VTI-02-attempt-001` on registered branch `integration/vti-02-multiversal-external-game-projection-contract`. Acceptance-package authority is open; production mutation remains locked until genuine matching Linux/Windows RED with deterministic comparison evidence.

VTI-02 is bounded to provider-neutral projections for Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference. It may preserve canonical source references, explicit projection availability (`present`, `redacted`, `unsupported`), visibility scope, ownership reference, consent requirement and GM-authority requirement, plus deterministic field/object ordering and receipts. It may not define provider-specific schemas or implement external-object mapping/versioning/synchronization (VTI-03), rules action/roll bridging (VTI-04), later platform-native presentation, permission-engine, SDK or adapter behavior.

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

2. **VTI-02 — Multiversal External Game Projection Contract** — **IN_PROGRESS**.  
   Provider-neutral Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference projections. Acceptance-package authority is open; production mutation remains locked until matching RED. External-object mapping/versioning/synchronization and rules-action bridging remain deferred to VTI-03 and VTI-04 respectively.

3. **VTI-03 — Stable Identity, Versioning & Synchronization**  
   External-object mappings, fingerprints, stale/conflict handling, reconnect, deduplication, tombstones and MIB-03-based retry/recovery.

4. **VTI-04 — Rules Action & Roll Bridge**  
   VTT request → Multiversal validation/resolution → owner receipts/result → VTT presentation for rolls, attacks, checks, powers, resources, conditions, initiative, reactions and GM adjudication.

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

## VTI-01 completed contract

VTI-01 established:
- platform identity, hosting/self-hosting and licensing/distribution classification from explicit evidence;
- capability states `supported`, `unsupported`, `conditional` and `unknown` without inference of support;
- source provenance containing stable evidence identity, publisher, title, locator and accessed date;
- deterministic ordering of platforms, evidence references, constraints and deterministic receipts;
- capability-driven Level 1/2/3 integration ceilings without treating them as vendor ranking or selection;
- explicit authority boundaries proving no external/canonical mutation, credentials, adapters, persistence, provider activation, tester distribution, release or deployment occurred.

Sealed completion evidence:
- acceptance RED head `c6bdb094499894f6b1e4b93d4910c8bbe6eb261d`, run `33986160384`, receipt `e73e56c1a649615af429d120a53331900758ce2b68a7587ccef36943e283c7cf`;
- final GREEN head `7c377f1add2e00bbadb4007a043fee69709bd923`, run `33986901523`, repository-health job `101362058899`, Linux job `101362075923`, Windows job `101362075959`, comparator job `101362151897`, receipt `be8c090d2482898fbcdc8ffc93b93a31b7cb2eae3c8c0e238a221a990f8ce761`;
- application PR #415 merge `027fad06d0bac3a20d56f0cc2a674581662cd1b9`.

## VTI-02 governed-start boundary

VTI-02 may define a provider-neutral projection contract for Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference objects. At governed start:
- application branch `integration/vti-02-multiversal-external-game-projection-contract` is authorized from exact baseline `027fad06d0bac3a20d56f0cc2a674581662cd1b9`;
- acceptance-package authority is `true`;
- production-mutation authority is `false` until genuine matching Linux/Windows RED is sealed;
- canonical source references may identify projected Multiversal objects, but external-object mappings, versioning, fingerprints, stale/conflict handling, reconnect, deduplication and tombstones remain VTI-03 scope;
- rules action/roll bridging remains VTI-04 scope;
- provider-specific schemas, credentials, external accounts, adapters, synchronization, canonical-state mutation, persistence and provider/tester/release activation remain unauthorized;
- Platform selection remains evidence-driven and is deferred to VTI-09;
- visibility, ownership, consent, hidden-information filtering and GM authority remain mandatory preserved constraints;
- VTI-03+ and SGC-01+ remain unauthorized.

## Invariants

- External VTTs are clients/projections, not replacement rules authorities.
- External mutations become governed proposals/operations where authoritative Multiversal state is affected.
- Capability manifests control feature exposure; unsupported fidelity is explicit.
- No VTT adapter may bypass visibility, ownership, consent or GM authority.
- No vendor is selected by roadmap text; platform selection is evidence-driven at VTI-09.
- Native SSA/KFR/ODL/MAL/ALP state is projected only where a platform supports it; VTI does not recreate those systems externally.
- VTI-01 is frozen completed_verified with implementation authority retired.
- VTI-02 is in_progress with acceptance-package authority and production mutation locked pending matching RED.
- VTI-03+ and SGC-01+ remain unauthorized until their own governed selections and starts.
