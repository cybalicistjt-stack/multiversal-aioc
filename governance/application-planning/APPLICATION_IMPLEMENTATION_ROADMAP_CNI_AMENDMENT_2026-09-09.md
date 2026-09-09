# Application Implementation Roadmap — CNI Planning Amendment — 2026-09-09

**Status:** OWNER-APPROVED PLANNING AMENDMENT  
**Owner and final authority:** John Brandon Turner  
**Runtime effect:** none; ARI-02 remains the current in-progress work under `CURRENT_WORK_POINTER.json`.  
**Implementation authority created by this amendment:** none.

## Owner decision preserved

The useful architectural examples identified in the Candlekeep Revisited / WeiDU study are to be implemented as Multiversal-native capabilities rather than left as informal inspiration. The implementation must preserve Multiversal's existing governed owner domains and must not copy Baldur's Gate/Forgotten Realms content or assume public repository visibility permits reuse of unlicensed code/assets.

A new critical-path interstitial family is added:

- **CNI — Content & Narrative Interoperability**, after **SMB-07 — Deep Cross-System Simulation** and before **SMB-08 — Core Content Production**.

## Corrected effective forward order

The effective future order is amended to:

`ARI-02..21 → ARI-22A/B/C → MIB-16 → MIB-17 → MIB-18 → SMB-01 → SMB-02 → SMB-03 → SMB-04 → SMB-05 → SMB-06 → SMB-07 → CNI-01..13 → SMB-08 → SMB-09 → SAA-01..20 → SMB-10 → SMB-11 → SMB-12 → SMB-13 → SMB-14 → SMB-15 → SMB-16 → BRP-01..11 → SMB-17 → SMB-18`

Completed predecessors remain completed. This amendment does not reopen any completed family and does not disturb ARI's current execution family/preflight.

## Why CNI is inserted before SMB-08

SMB-08 is where substantial first-party content packs begin and SMB-09 is where the complete first-party campaign is produced. If modular pack identity, dependencies, state scoping, conditional narrative, dialogue/action binding, continuity, cross-pack compatibility and localization separation are delayed until after those tranches, first-party content would either depend on temporary assumptions or require a later migration/retrofit.

SMB-01..07 first establish the production platform, multiplayer, major simulation verticals and deep cross-system behavior. CNI then gives those mature owner domains one governed content/narrative interoperability layer. SMB-08 and SMB-09 become the first major consumers and proofs of that layer.

## CNI scope derived from the reference study

CNI preserves these useful patterns as original Multiversal implementations:

1. modular content packs containing independently selectable components;
2. explicit prerequisites, optional dependencies, versions and compatibility constraints;
3. scoped persistent narrative state rather than one undifferentiated flag namespace;
4. deterministic conditional predicates over permitted game context;
5. structured executable dialogue whose effects route through governed Actions/Events;
6. Character-aware branches using explicit traits/capabilities from owning systems;
7. persistent NPC callbacks and continuity linked to Relationship/Timeline state;
8. one-shot, delayed, re-entry, quest/scene and location triggers;
9. explicit cross-pack extension/patch hooks with conflict detection rather than destructive replacement;
10. localizable text/resource separation from executable logic;
11. dependency/apply dry-run, validation, atomic activation/rollback and deterministic receipts;
12. creator/developer inspection of manifests, dependency graphs, predicates, state references, localization and conflicts;
13. an original Multiversal golden multi-pack compatibility proof.

## Ownership and non-duplication contract

CNI does not replace:

- CSW/Story/Adventure authority over story identity, authored narrative truth and canon;
- Action/Event/approval authority over canonical mutation;
- Character, Relationship, Reputation, Quest, Scene, Campaign or World canonical state;
- ARI resource identity, provenance, rights/use capability or shared asset storage;
- SMB-11 cross-user sharing/interchange authority;
- SMB-16 final product-wide localization/accessibility/device-completion authority.

CNI consumes those owners through explicit projections/contracts and provides interoperability/runtime binding only.

## Reference-source rights boundary

The public Candlekeep Revisited repository was inspected as a reference implementation. The inspected root listing did not expose a root license, and the project necessarily contains/targets Baldur's Gate/Forgotten Realms material. Therefore this amendment authorizes pattern study only. Direct reuse of its dialogue, assets, scripts or setting material is forbidden absent independent rights evidence. WeiDU or any other upstream code is separately license-reviewed before any incorporation.

## Durable planning artifacts

This amendment adds:

- `content-narrative-interoperability/CNI_CONTENT_NARRATIVE_INTEROPERABILITY_PROGRAM.md`
- `content-narrative-interoperability/CNI_PROGRAM_BACKLOG.json`
- `system-maturation-buildout/SMB_CNI_INTERSTITIAL_INTEGRATION_AMENDMENT_2026-09-09.md`

The live `ROADMAP_INDEX.json` and authority registry must register CNI as owner-approved planned work while leaving ARI's current runtime authority untouched. A control-plane regression test must prevent CNI or its SMB-07→SMB-08 insertion from being silently lost.

## Family execution rule

CNI follows the current family method: each planned execution unit targets 24 active minutes or less under a healthy environment, with closeout reserve protected. An oversized unit must be split before governed start. This amendment does not replace the active ARI `FAMILY_EXECUTION_PREFLIGHT.json`; CNI gets a sealed runtime family preflight only when it later becomes the selected family.

## Authority and non-activation rules

- ARI-02 remains the current in-progress unit and retains its existing bounded authority.
- CNI cannot start before SMB-07 reaches `completed_verified` and a later governed start selects CNI-01.
- CNI-02+ remain unauthorized until strict-successor selection advances through the family.
- No provider credential, paid service, scraping/ripping/extraction, copyrighted-content import, tester distribution, public sharing, marketplace, canon promotion or release/deployment authority is created here.
- Removal or relocation of CNI requires a later explicit owner decision and canonical planning amendment.
