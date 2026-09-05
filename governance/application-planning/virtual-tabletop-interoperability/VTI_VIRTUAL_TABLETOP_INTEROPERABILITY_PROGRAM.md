# VTI — Virtual Tabletop Interoperability

**Program ID:** VTI  
**Status:** OWNER-APPROVED — VTI-01 THROUGH VTI-02 COMPLETED_VERIFIED; VTI-03 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ALP-08  
**Successor:** SGC-01  
**Owner and final authority:** John Brandon Turner

## Current state

VTI-01 — VTT Ecosystem, Licensing & Capability Matrix — is `completed_verified`. Application PR #415 was validated at exact head `7c377f1add2e00bbadb4007a043fee69709bd923` by self-hosted Linux, self-hosted Windows and deterministic cross-platform comparison in run `33986901523`, then squash-merged to application `main` as `027fad06d0bac3a20d56f0cc2a674581662cd1b9`.

VTI-02 — Multiversal External Game Projection Contract — is `completed_verified`. Genuine matching acceptance RED was sealed from exact application head `db4a4c436cb6eeb011afd9614568fb68f070c785` in run `33989074845`: Linux and Windows both failed at `vti02-invariants` because the production contract was intentionally absent, while deterministic comparison passed with receipt `7005e6b204a3b24a1e8a6e8e8ac2f80a295540afaf9fc9b3bbfb733a5f39ccc7`. Final exact-head GREEN was then established at `e24f1e045d6dd5c6f332ebc4392acf2ba9f6e281` in run `33989626004`: repository health, self-hosted Linux, self-hosted Windows and deterministic cross-platform comparison all passed with receipt `a66e9f4557713aa2807c960cb3c018a222c4316cadeb4afbfd8e5be4199ff7bd`. Application PR #416 was squash-merged as `01aa25d60ad71e5ed318b9680f859c6927a90541`.

VTI-02 implementation authority is retired. Its completed contract remains provider-neutral and deterministic: projection kinds are Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference; canonical Multiversal source references are preserved; field availability is explicit as `present`, `redacted` or `unsupported`; redacted/unsupported values are not manufactured; visibility, ownership, consent and GM-authority metadata remain preserved constraints. No vendor selection/ranking, provider-specific schema, external-object mapping/versioning/synchronization, rules-action bridge, credentials, external-account mutation, adapter implementation, canonical-state mutation, hidden-information bypass, persistence, migration, provider activation, tester distribution, release or deployment was performed.

VTI-03 — Stable Identity, Versioning & Synchronization — is the strict successor and is `selected_not_started` as `VTI-03-attempt-001` from exact application main `01aa25d60ad71e5ed318b9680f859c6927a90541`. Selection grants no implementation branch, implementation authority, acceptance-package authority or production-mutation authority. A future owner `Continue` must governed-start VTI-03 before any implementation work begins.

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
   Provider-neutral Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference projections with canonical source references, explicit present/redacted/unsupported availability, preserved visibility/ownership/consent/GM-authority metadata, deterministic normalization and deterministic receipts. External-object mapping/versioning/synchronization remains deferred to VTI-03 and rules-action bridging remains deferred to VTI-04.

3. **VTI-03 — Stable Identity, Versioning & Synchronization** — **SELECTED_NOT_STARTED**.  
   External-object mappings, fingerprints, version negotiation, stale/conflict handling, reconnect, deduplication, tombstones and MIB-03-based retry/recovery. Selection alone grants no implementation authority.

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

## VTI-02 completed contract

VTI-02 established:
- provider-neutral projection kinds Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and RuleReference;
- opaque canonical Multiversal source-object references and canonical related-source references without external identifier mappings;
- explicit field availability `present`, `redacted` and `unsupported`;
- hidden or unavailable values are stripped rather than manufactured;
- preserved visibility scope, ownership references, consent requirements and GM-authority requirements without implementing the later permission engine;
- deterministic field ordering, related-reference ordering, projection ordering and deterministic receipts;
- explicit authority boundaries proving that external-object mapping/versioning/synchronization, rules-action bridging, provider-specific schemas, credentials, external/canonical mutation, adapters, persistence, migration, provider activation, tester distribution, release and deployment remain outside VTI-02.

Sealed completion evidence:
- acceptance RED head `db4a4c436cb6eeb011afd9614568fb68f070c785`, run `33989074845`, receipt `7005e6b204a3b24a1e8a6e8e8ac2f80a295540afaf9fc9b3bbfb733a5f39ccc7`;
- final GREEN head `e24f1e045d6dd5c6f332ebc4392acf2ba9f6e281`, run `33989626004`, repository-health job `101369414996`, Linux job `101369443543`, Windows job `101369443490`, comparator job `101369746269`, receipt `a66e9f4557713aa2807c960cb3c018a222c4316cadeb4afbfd8e5be4199ff7bd`;
- application PR #416 merge `01aa25d60ad71e5ed318b9680f859c6927a90541`.

## VTI-03 selection boundary

VTI-03 is selected only from exact application main `01aa25d60ad71e5ed318b9680f859c6927a90541`.

Selection alone does not authorize implementation. A future governed start may bound:
- stable external-object mappings and identities;
- fingerprints and version negotiation;
- stale/conflict handling;
- reconnect and retry/recovery behavior using MIB-03 semantics;
- deduplication and tombstones.

Until that governed start:
- implementation branch, acceptance-package authority and production-mutation authority are `false`;
- external synchronization mutation, durable VTI persistence and any new migration are unauthorized;
- rules action/roll bridging remains VTI-04 scope;
- provider-specific schemas, credentials, external accounts, adapters and platform selection remain unauthorized;
- Platform selection remains evidence-driven and is deferred to VTI-09;
- visibility, ownership, consent, hidden-information filtering and GM authority remain mandatory preserved constraints;
- VTI-04+ and SGC-01+ remain unauthorized.

## Invariants

- External VTTs are clients/projections, not replacement rules authorities.
- External mutations become governed proposals/operations where authoritative Multiversal state is affected.
- Capability manifests control feature exposure; unsupported fidelity is explicit.
- No VTT adapter may bypass visibility, ownership, consent or GM authority.
- No vendor is selected by roadmap text; Platform selection remains evidence-driven at VTI-09.
- Native SSA/KFR/ODL/MAL/ALP state is projected only where a platform supports it; VTI does not recreate those systems externally.
- VTI-01 and VTI-02 are frozen completed_verified with implementation authority retired.
- VTI-03 is selected_not_started with no implementation branch or authority.
- VTI-04+ and SGC-01+ remain unauthorized until their own governed selections and starts.
