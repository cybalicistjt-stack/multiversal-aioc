# STAGE-A-A8 — Supplemental Item / Platform / Content-Context Authority Reconciliation

**Document ID:** STAGE-A-A8-R0  
**Status:** OWNER-APPROVED PRE-REVALIDATION AUTHORITY  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-15  
**Application mutation authorized by this document:** No

## 1. Decision

Before STAGE-A-A8 current-repository revalidation, the recovered historical A8 package must be reconciled with the later completed Item Taxonomy, Platform/Vehicle Catalog, and Reality Catalog preparation work.

The Item and Platform preparation are no longer treated as wholly dormant future work: their A8-owned runtime boundaries and future-proof catalog seams become direct A8 revalidation input now. The Reality preparation remains dormant as a subsystem, except for the shared content-context vocabulary and compatibility interface semantics reused across Item, Platform, and Reality domains.

## 2. Adopt into A8 now

A8 revalidation must preserve or introduce implementation seams for the following:

1. **Item Definition vs Item Instance/Asset.** Reusable catalog/product definitions are distinct from owned inventory instances. A8 remains sole runtime authority for item instances, quantity, custody, location, condition, equipment state, consumption, modification, transfer, and inventory history.
2. **Platform/Vehicle Model vs Individual Vehicle Asset.** Reusable model/configuration identity is distinct from a particular owned vehicle with registry/identity marks, crew, damage, modifications, maintenance, provenance, and history.
3. **Reusable product identity ladder.** Generic concept, family/line, model/product, variant and governed configuration identities must be representable without destructive later migration or name-based merging.
4. **Shared Creator Entity seam.** Item makers, manufacturers, brands, cultures, organizations, civilizations, artisans and other origins use a shared persistent creator/origin interface rather than separate incompatible Item and Vehicle manufacturer tables. A creator is not automatically a Faction.
5. **Shared Content Context foundation.** The nine controlled facets — Setting Family, Genre Tradition, Era/Development, Technology Paradigm, Power Paradigm, Environment, Play Domain, Tone/Style, Content Scale — are shared cross-domain vocabulary and are not owned by A8, Items, Vehicles, or Reality individually.
6. **Intrinsic vs affinity vs compatibility separation.** Intrinsic requirements describe what an Item/Vehicle needs; affinity describes thematic/contextual fit; compatibility is a contextual evaluation. Genre affinity is never equivalent to operational compatibility.
7. **Compatibility adapter boundary.** A8 must be able to ask an external setting/context provider whether requirements are satisfied. Until the later Reality/World subsystem is implemented, context may legitimately resolve to unknown/unavailable. A8 must not invent world metaphysics to answer the question.
8. **Provenance/source-state seam.** Current canonical records, source-backed recovery, legacy concepts, authored records, unresolved identities and re-mechanization candidates remain distinguishable.
9. **Economy boundary.** A8 may store/consume availability, restriction, production/service/parts and market-context metadata, but canonical price/value/transaction authority remains with Economy.
10. **Current mechanics protection.** Existing current Item/Vehicle mechanics are preserved by default. Legacy/source mechanics are evidence of intent/provenance only and may not be numerically promoted by direct conversion.

## 3. Add dormant or read-only seams during A8 where inexpensive

The following should be structurally possible but need not become full alpha-facing features during the core A8 slice:

- product lineage and predecessor/successor/derivative relationships;
- creator/manufacturer catalog browsing;
- production history and market-history metadata;
- service-network and parts-availability metadata;
- read-only portfolio/coverage analyzers;
- governed legacy recovery and re-mechanization work queues;
- richer compatibility explanations and diagnostics;
- factory configuration inheritance separate from live installed state.

These may be feature-gated/read-only until later alpha work.

## 4. Explicitly defer from A8

A8 must not absorb:

- the full 44-type Reality/Place topology system;
- Reality-law/metaphysics authoring;
- multiversal variation/timeline/lineage graphs as world authority;
- GM Reality creation and world publication workflows;
- public/community world discovery, follow/bookmark/social/moderation/remix systems;
- automatic cross-reality Body/Mind/Soul/Gear effects beyond a provider-neutral compatibility seam;
- broad content auto-enrichment or AI filling of missing lore/mechanics;
- any public release or production-service authority.

PPIA-12 remains reusable World/Setting authority. PPIA-08 remains Campaign/Scene/current-setting-state authority. The later Reality implementation may provide context to A8; A8 does not own that context.

## 5. A8 alpha implementation outcome

A8 should prove the correct runtime model rather than every future catalog feature. The bounded alpha slice should be able to:

- browse/select an Item Definition;
- instantiate/acquire inventory state;
- change quantity and location;
- equip/unequip and install/remove governed equipment;
- consume/use, damage, repair, modify and transfer an individual Item/Asset under current rules;
- browse/select a Vehicle/Platform Model;
- instantiate an individual Vehicle Asset;
- assign ownership/custody/crew as current A8 authority permits;
- install/remove governed equipment;
- damage, repair and modify the individual vehicle without mutating its reusable model;
- save/reconnect/recover without collapsing Definition and Instance state;
- expose provenance and compatibility state without leaking hidden information or inventing unavailable setting context.

## 6. Migration strategy

Use **expand → project → validate → review → enable**.

Do not begin by rewriting existing CSVs, reinterpreting live inventory fields as catalog metadata, or making newly prepared fields mandatory. Add dormant structures, project existing current records, validate boundaries, review ambiguous mappings, then enable bounded read/write surfaces.

## 7. Source authority

The exact source archive identities and extracted repository files are declared in `STAGE_A_A8_SUPPLEMENTAL_SOURCE_MANIFEST.json`.

The owner-supplied construction conversation confirms design intent and chronology but is not itself executable authority. This reconciliation document is the owner-approved current decision derived from that work.

## 8. Revalidation gate

A8 revalidation must explicitly classify each affected historical A8 path/assumption as:

- `ADOPT_CURRENT`;
- `ADOPT_SUPPLEMENT`;
- `REUSE_IMPLEMENTED`;
- `ADD_DORMANT`;
- `MODIFY_BOUNDED`;
- `DEFER`;
- `PROHIBIT_DUPLICATION`;
- `CONFLICT_REQUIRES_REDESIGN`.

No A8 application mutation begins merely because this reconciliation is merged. After merge, bootstrap/runtime state must point to **STAGE-A-A8 current-repository revalidation** as the exact next operation.