# VTI — Virtual Tabletop Interoperability

**Program ID:** VTI  
**Status:** OWNER-APPROVED — VTI-01 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ALP-08  
**Successor:** SGC-01  
**Owner and final authority:** John Brandon Turner

## Current state

ALP-08 completed_verified and the ALP program is frozen complete. VTI-01 — VTT Ecosystem, Licensing & Capability Matrix — is the strict successor and is `selected_not_started` from exact application main `e61109affe9d662e6da6eb214c1acc870079c1a7` as `VTI-01-attempt-001`.

VTI-01 has no implementation branch, no implementation authority, no acceptance-package authority and no production-mutation authority. A future owner `Continue` must governed-start VTI-01 before any VTI implementation work begins.

## Purpose

VTI lets compatible external VTTs present and interact with Multiversal campaigns at the deepest level each platform safely permits, while Multiversal remains the canonical rules/campaign authority.

Integration levels are capability-driven:
- Level 1: export/content pack;
- Level 2: synchronized companion;
- Level 3: native Multiversal VTT system/rules package where the platform supports it.

VTI follows the native mine-note-derived semantic families so adapters project mature native state rather than becoming the first implementation of spatial semantics, knowledge/familiarity, organization dynamics, microgames or learning/achievement behavior.

## Tranches

1. **VTI-01 — VTT Ecosystem, Licensing & Capability Matrix** — **SELECTED_NOT_STARTED**.  
   Survey target platforms and classify system/rules packages, modules/plugins, sheets, compendiums, maps/scenes, automation, APIs, live communication, import/export and distribution constraints.

2. **VTI-02 — Multiversal External Game Projection Contract**  
   Provider-neutral Character, Creature, Item, Action, Condition, Encounter, Scene, Vehicle and Rule-reference projections for adapters.

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

## Invariants

- External VTTs are clients/projections, not replacement rules authorities.
- External mutations become governed proposals/operations where authoritative Multiversal state is affected.
- Capability manifests control feature exposure; unsupported fidelity is explicit.
- No VTT adapter may bypass visibility, ownership, consent or GM authority.
- No vendor is selected by roadmap text; platform selection is evidence-driven at VTI-09.
- Native SSA/KFR/ODL/MAL/ALP state is projected only where a platform supports it; VTI does not recreate those systems externally.
- VTI-01 selection grants no vendor choice, external account mutation, credential use, provider activation, tester distribution, release or deployment authority.
- VTI-02+ and SGC-01+ remain unauthorized until their own governed selections and starts.
