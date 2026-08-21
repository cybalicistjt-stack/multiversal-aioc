# RSR — Recovered Source Reconciliation

**Program ID:** RSR  
**Status:** IN PROGRESS — RSR-01 COMPLETED_VERIFIED — RSR-02 IN_PROGRESS  
**Activation:** after MSS-05 `completed_verified`  
**Completed through:** RSR-01  
**Current:** RSR-02  
**Successor:** MSS-06 after RSR-07  
**Owner and final authority:** John Brandon Turner  
**Planned:** 2026-08-21  
**Activated:** 2026-08-21

## Purpose

RSR preserves and reconciles the newly recovered legacy Multiversal source bundle `Now this.zip` without allowing old conversations or assistant-generated expansions to become current authority by existence alone.

The retained bundle contains 24 MHT conversation exports spanning worlds/realities, species/cultures, magic and supernatural systems, economy/social structures, campaign/gameplay frameworks, maps/visual references, history/timelines, food/cooking/loot references and other cross-system content. Some subjects already occur in canonical source-recovery or completed implementation work; others appear to be previously missed. RSR gives every recovered source a governed disposition and creates explicit reconciliation work where already-completed families may have been built before these recovered sources were available.

RSR is a reconciliation program, not a replacement architecture. Completed work remains `completed_verified`; reconciliation tranches may add coverage, provenance mappings, candidate content, tests or narrowly justified compatibility changes without rewriting valid prior evidence.

MSS-05 completed_verified at application PR #269 / merge `f36dff5753045bbde1c4059800721c5c35ff97c2`. RSR-01 subsequently completed_verified at AIOC PR #598 / merge `17613c8de1fab250db4539adbb30ebecbb49eccb` after exact archive/provenance/disposition validation. Owner `Continue` governed-started RSR-02 at 2026-08-21T18:12:00Z with implementation authority limited to `governance/rsr-02-world-reality-reconciliation`.

## Source authority and attribution rules

- Current GitHub repository evidence remains authoritative for implementation state.
- The recovered archive is retained source/provenance material, not a current-work selector.
- Owner-authored statements and explicit owner corrections in the recovered conversations outrank surrounding assistant-generated prose.
- Assistant-generated lore, mechanics, formulas, names, factions, perks, maps or extrapolations remain proposals unless independently supported or later owner-approved.
- Existing canonical entities and stable IDs are reused when the recovered source is another version or provenance line for the same subject.
- Conflicts are recorded; they are not silently harmonized.
- Embedded visual assets are preserved by source/archive checksum and media manifest even when the original MHT bytes remain in Project Sources rather than GitHub.
- No recovered source may bypass visibility, provenance, permission, owner-domain, approval or no-invention boundaries.

## RSR-01 completion evidence

RSR-01 verified the exact retained archive SHA-256 `2a5eae712f483d1fb33ff9fb0087e96c4eb8b71b287cc707c196a4c17a2f78f4` and all 24 constituent MHT checksums; indexed 102 visible saved turns as 47 owner/user and 55 assistant turns; inventoried 12 unique embedded media objects excluding auth avatars, 11 substantive; and assigned every source an explicit non-promoting disposition and downstream route. The source-level result is 14 `existing-needs-reconciliation` and 10 `new-candidate`. Exact source bytes remain retained in Project Sources rather than reconstructed from derived indexes.

## Tranches

1. **RSR-01 — Archive Preservation, Extraction, Provenance & Disposition Registry** — `completed_verified`  
   Exact archive and constituent checksums verified; message attribution/hash, media provenance and source-disposition indexes created; all 24 sources routed without automatic canon promotion. Evidence is under `governance/source-material/recovered-legacy/now-this-2026-08-21/` and validated by `scripts/validate_rsr_01.py`.

2. **RSR-02 — MIB-11 World/Reality/Timeline Reconciliation** — `in_progress`  
   Reconcile recovered worlds, realities, timelines, locations and cross-reality relationships against completed MIB-11 World/Reality taxonomy and existing stable IDs. Includes, as source candidates where supported: Black Vegas, Dionasia, Carnival, City of Millennial, Pencrona, Magen Galaxy, Sherazzalla, Vertigon, Skoaltarra/Umbraxis material, Nestor Ra, Consortium/30 Winds, Empire settings and related recovered world/history material. Do not duplicate already-known worlds merely because a second conversation version exists.

3. **RSR-03 — ICF Content/Crafting/Food/Alchemy Reconciliation**  
   Reconcile recovered items, equipment, materials, cooking/food, alchemical or biological ingredients, crafting hooks and source-specific content against completed ICF-01..15. Add candidate content or provenance only where the recovered source supports it; no invented universal formulas or replacement ledgers.

4. **RSR-04 — CEL Cozy/Economy/Life-Loop Reconciliation**  
   Reconcile recovered post-scarcity society, trade, social/economic life, food, culture, household or downtime implications against completed CEL-01..06 and current Economy owners. Preserve the principle that cozy activity remains connected to meaningful economy/state loops rather than becoming an ungoverned side simulation.

5. **RSR-05 — LSS Loot/Scavenge/Salvage Reconciliation**  
   Reconcile recovered loot, item acquisition, salvage, equipment, creature/material recovery and related gameplay hooks against completed LSS-01..10. New source content must use existing ownership, decomposition, condition, economy and provenance seams.

6. **RSR-06 — LNG Language/Culture/Script Reconciliation**  
   Reconcile recovered languages, naming systems, dialect/cultural language material, scripts and language-history implications against completed LNG-01..06. Serpentine Empire language material and any other recovered language evidence receive explicit disposition without replacing completed language authorities.

7. **RSR-07 — MSS-01..04 Supernatural Foundation Reconciliation & Downstream Routing**  
   Reconcile recovered magic, mana/resource models, spells/powers, rituals, supernatural species abilities, portals, timelines/causal material and setting-local supernatural rules against completed MSS-01..04, and record any provenance implications for completed MSS-05 without weakening its completion. Confirm what becomes an input to MSS-06..12, DPL, CCP, WCI, SCL, MAI, SGC or another future owner. No recovered assistant formula becomes canonical automatically; unresolved or contradictory mechanics remain explicit proposals or owner-review items.

## Completion gate

RSR is complete only when:

- every one of the 24 recovered MHT sources has an exact checksum and disposition;
- all substantive embedded visual references are inventoried;
- owner statements/corrections are distinguishable from assistant proposals;
- duplicate/variant source lines are linked rather than multiplied into parallel canon;
- completed families touched by newly recovered evidence have an explicit reconciliation result;
- new candidate content is routed to the correct future owner/program;
- conflicts and unresolved mechanics remain visible rather than silently normalized;
- repository source coverage can prove that no retained recovered source was dropped without a recorded disposition.

## Forward-order rule

RSR-01 is completed_verified. RSR-02 is in progress. RSR-03..07 execute in strict order after RSR-02 reaches `completed_verified`. MSS-06 remains the next MSS tranche, but its effective activation is after RSR-07 so recovered supernatural source coverage is reconciled before deeper tradition/content work proceeds.
