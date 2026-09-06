# VTI — Virtual Tabletop Interoperability

**Program ID:** VTI  
**Status:** OWNER-APPROVED — VTI-01 THROUGH VTI-06 COMPLETED_VERIFIED; VTI-07 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ALP-08  
**Successor:** SGC-01  
**Owner and final authority:** John Brandon Turner

## Current state

VTI-01 — VTT Ecosystem, Licensing & Capability Matrix — is `completed_verified` and retired.

VTI-02 — Multiversal External Game Projection Contract — is `completed_verified` and retired. Application PR #416 was squash-merged as `01aa25d60ad71e5ed318b9680f859c6927a90541` after exact-head Linux/Windows/comparator GREEN.

VTI-03 — Stable Identity, Versioning & Synchronization — is `completed_verified` and retired. Application PR #417 was squash-merged as `56ab87c2be214d4d7edb15e0e8d02429a07ee2d4` after exact-head Linux/Windows/comparator GREEN.

VTI-04 — Rules Action & Roll Bridge — is `completed_verified` and retired. Genuine matching acceptance RED was sealed from exact application head `c9a3cc09aa9ce6ce2ca55c35df7ba7032ffb7126` in run `33993535896`. Final exact-head GREEN was established at `8806fce4a0143281942dd2d68a23301c70501999` in run `33994055604`, and application PR #418 was squash-merged as `295424982135337de80cccfac072764ab35183cc`.

VTI-05 — Character Sheet, Item & Compendium Projection — is `completed_verified` and retired. Genuine matching acceptance RED was sealed from exact application head `5ff92aaebc311933a3fa814b22badcb8ee694f76` in run `33997794873` with deterministic receipt `d234d207d409056383670a853e29d6d2748ea5bc59db3892f3c7d9a0133bff7b`. Final exact-head repository health, self-hosted Linux, self-hosted Windows and deterministic comparison all passed at `a26f4aa49f76c668d8a28030d52e3b1719cd25ef` in run `33999669961` with receipt `b093ef2a838a5d76157342f91c54d8fa79b6ab4458aa21f3bac2f762bdcf688b`. Application PR #420 was squash-merged as `6b7e101c08d52362af824b68f43cd983794893c6`.

The owner-directed IC-01 through IC-13 technical UI convergence sequence advanced application `main` to `4bd061a87852f4bb4b17f5d500ae6ab85081c72b`. That sequence did not replace VTI roadmap ownership. The separate owner-only Orange/Ember versus Chromatic palette gate remains open without reopening IC technical implementation.

After the VTI-06 governed start validated, application `main` advanced through `973490e8358fe0a48dad43933ac3675acd188303`, which added only a temporary `placeholder` file, and `e9ddbf9c763faca74689cb3776ad21501c341ba5`, which removed only that file. The current `e9ddbf9c...` tree is `8e9942b47cb5231816d4584397d460eaec522846`, exactly the same tree as `4bd061a...`. This exact-head reconciliation therefore changes no application semantics, VTI scope, or authority; the IC-13 historical closeout anchor remains `4bd061a...`.

VTI-06 — Scene, Map, Token & MAI Bridge — is `completed_verified` and retired. Genuine matching acceptance RED was sealed from exact application head `bf00d1d17befb35560c3ee5c18899d25df209d83` in run `34058733989` with deterministic receipt `456ec49cfaf07080c948cfa8b0024330179433b88f7aabedbc220e486e49103d`. Final exact-head repository health, self-hosted Linux, self-hosted Windows and deterministic comparison all passed at `80cd22e0e28304c0a59aa5954d35d504b55c4ea0` in run `34059463389` with receipt `636c05c378b4c081ae51b3f8b5feb4f5e446471073f0ce0e6a6153c70c5754a1`. Application PR #435 was merged as `1e325045b2fc65d067a5e587f8cde78dcba9f766`. VTI-07 — Permissions, Hidden Information & GM Authority — is the strict successor and is `selected_not_started` from that exact application main with no branch, acceptance-package, implementation or production authority.

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

5. **VTI-05 — Character Sheet, Item & Compendium Projection** — **COMPLETED_VERIFIED**.  
   Present Characters, NPCs, creatures, equipment, powers, conditions, rules references, roll tables and vehicles in provider-neutral projection forms with canonical source references, explicit `present`, `redacted` and `unsupported` fidelity, visibility, ownership, consent, hidden-information filtering and GM authority preserved. No provider-specific adapter, live external mutation or durable VTI persistence was introduced.

6. **VTI-06 — Scene, Map, Token & MAI Bridge** — **COMPLETED_VERIFIED**.  
   Projects existing canonical Multiversal Scene, map-version, placement and MAI/ISE/SSA semantics to provider-neutral scene/map/token envelopes with deterministic normalization, explicit `present`/`redacted`/`unsupported` fidelity, native wall/door/grid semantics only, fail-closed hidden presentation, and preserved visibility, ownership, consent and GM authority. No provider-specific adapter, live external mutation, durable persistence or VTI-07 permission-engine behavior was introduced.

7. **VTI-07 — Permissions, Hidden Information & GM Authority** — **SELECTED_NOT_STARTED**.  
   Preserve ownership, consent, GM adjudication and hidden-information filtering across external clients; prevent hidden counts/content leakage. Selection alone grants no branch, acceptance-package, implementation or production authority.

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
- acceptance RED head `c9a3cc09aa9ce6ce2ca55c35df7ba7032ffb7126`, run `33993535896`, receipt `ee79438a64ccaccabe8acd2953df5f911d1e0ee8b92352952b3026ede1d0e028`;
- final GREEN head `8806fce4a0143281942dd2d68a23301c70501999`, run `33994055604`, receipt `766e06c3f2de74e4cbee599fa56c3d88e4a49fe98481b7f65f70d30a5970050c`;
- application PR #418 merge `295424982135337de80cccfac072764ab35183cc`;
- historical profile fanout `0` and application-feature repair cycles `0`.

## VTI-05 completed contract

VTI-05 established:
- provider-neutral character-sheet projection for Characters, NPCs and creatures with canonical source references and explicit `present`, `redacted` or `unsupported` fidelity;
- provider-neutral item projection for equipment, powers and conditions without provider-specific schemas;
- provider-neutral compendium projection for RuleReference, roll-table and vehicle records where capability supports them;
- deterministic normalization plus visibility, ownership, consent, hidden-information filtering and GM-authority preservation across projection envelopes;
- deterministic invariant validation and receipts;
- explicit proof that provider-specific schemas, credentials/accounts, adapters, live external/canonical mutation, durable VTI persistence/new migration, provider activation, tester distribution, release/deployment and VTI-06+ implementation were not introduced.

Sealed completion evidence:
- acceptance RED head `5ff92aaebc311933a3fa814b22badcb8ee694f76`, run `33997794873`, receipt `d234d207d409056383670a853e29d6d2748ea5bc59db3892f3c7d9a0133bff7b`;
- final GREEN head `a26f4aa49f76c668d8a28030d52e3b1719cd25ef`, run `33999669961`, repository-health job `101396156463`, Linux job `101396170999`, Windows job `101396170914`, comparator job `101396256600`, receipt `b093ef2a838a5d76157342f91c54d8fa79b6ab4458aa21f3bac2f762bdcf688b`;
- application PR #420 merge `6b7e101c08d52362af824b68f43cd983794893c6`;
- historical profile fanout `0` and application-feature repair cycles `0`.

## VTI-06 completed contract

VTI-06 established:
- provider-neutral `scene`, `map` and `token` projection envelopes while Multiversal remains canonical authority;
- direct reuse of canonical `SceneRecord`, `SceneMapVersion` and `ScenePlacementRecord` semantics rather than parallel spatial models;
- wall and door projection only from native semantic dungeon primitives, and grid presentation only from canonical coordinate/calibration state;
- lighting and elevation as unsupported unless an owning native Multiversal semantic source exists;
- MAI/ISE/SSA asset/version references and semantic-construction roles as derivative presentation inputs without transferring asset or spatial authority;
- deterministic source, placement, primitive and related-asset normalization;
- explicit `present`, `redacted` and `unsupported` fidelity with redacted/unsupported values removed rather than inferred or manufactured;
- fail-closed hidden-information and GM-only presentation while preserving ownership, consent, visibility-policy and GM-authority metadata;
- explicit proof that provider-specific schemas, credentials/accounts, adapters, live external/canonical mutation, durable VTI persistence, new migration, provider activation, tester distribution, release/deployment and VTI-07+ implementation were not introduced.

Sealed completion evidence:
- acceptance RED head `bf00d1d17befb35560c3ee5c18899d25df209d83`, run `34058733989`, repository-health job `101555305842`, Linux job `101555324339`, Windows job `101555324315`, comparator job `101555372459`, receipt `456ec49cfaf07080c948cfa8b0024330179433b88f7aabedbc220e486e49103d`;
- final GREEN head `80cd22e0e28304c0a59aa5954d35d504b55c4ea0`, run `34059463389`, repository-health job `101557264698`, Linux job `101557279052`, Windows job `101557279039`, comparator job `101557349207`, receipt `636c05c378b4c081ae51b3f8b5feb4f5e446471073f0ce0e6a6153c70c5754a1`;
- application PR #435 merge `1e325045b2fc65d067a5e587f8cde78dcba9f766`;
- historical profile fanout `0`, application-feature repair cycles `0`, and one final validation-contract wording repair on changed evidence only.

## VTI-07 selection boundary

VTI-07 — Permissions, Hidden Information & GM Authority — is `selected_not_started` as `VTI-07-attempt-001` from exact application main `1e325045b2fc65d067a5e587f8cde78dcba9f766`. Selection records strict order only. No VTI-07 application branch, acceptance package, permission behavior, production mutation or permission-engine implementation is authorized until a separate governed start validates and merges.

A future governed start may bound provider-neutral preservation of canonical Multiversal ownership, consent, visibility, hidden-information and GM-authority decisions across derivative external-VTT clients. External VTTs may not become authoritative for permissions, adjudication or hidden state. Hidden counts/content, redacted identities and GM-only material remain fail-closed with no inference channel. Provider-specific schemas, credentials/accounts, adapter implementation, live external/canonical mutation, durable persistence/new migration, provider activation, tester distribution, release/deployment, VTI-08+ and SGC-01+ remain unauthorized.

## Invariants

- External VTTs are clients/projections, not replacement rules authorities.
- External mutations become governed proposals/operations where authoritative Multiversal state is affected.
- Capability manifests control feature exposure; unsupported fidelity is explicit.
- No VTT adapter may bypass visibility, ownership, consent or GM authority.
- No vendor is selected by roadmap text; Platform selection remains evidence-driven at VTI-09.
- Native SSA/KFR/ODL/MAL/ALP state is projected only where a platform supports it; VTI does not recreate those systems externally.
- VTI-01 through VTI-06 are frozen completed_verified with implementation authority retired.
- VTI-04 external VTT request/presentation clients may not independently resolve Multiversal rules, supply authoritative RNG outcomes, or autonomously exercise GM adjudication.
- Duplicate external requests may not resolve twice when an authoritative receipt can be replayed or status checked.
- IC-01 through IC-13 technical UI convergence may alter presentation composition but not the behavioral/data/permission/provenance authority projected through VTI.
- The post-governed-start placeholder add/remove pair is net-zero and may not be interpreted as new VTI scope or product semantics.
- VTI-06 completed by reusing existing native spatial, Scene, map, placement, visibility and MAI/ISE/SSA semantic authorities rather than duplicating them.
- VTI-07 is selected_not_started from exact application main `1e325045b2fc65d067a5e587f8cde78dcba9f766`; selection grants no branch, acceptance-package, implementation or production authority.
- VTI-08+ and SGC-01+ remain unauthorized until their own governed selections and starts.
