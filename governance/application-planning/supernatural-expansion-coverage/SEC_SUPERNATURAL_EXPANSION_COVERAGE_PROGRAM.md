# SEC — Supernatural Expansion & Coverage

**Program ID:** SEC  
**Status:** IN PROGRESS — SEC-01 IN_PROGRESS  
**Corrective placement:** intended between MSS-11 and MSS-12  
**Current corrective execution:** SEC-01..09 → MSS-12 post-SEC re-proof → resume CCP-02  
**Owner and final authority:** John Brandon Turner  
**Repaired:** 2026-08-23 America/Chicago

## Why this program exists

SEC defines and proves supernatural/spell corpus completeness. A later roadmap reconciliation accidentally omitted SEC-01..09 and allowed MSS-12, then CCP-01, to execute first. Their actual implementation and validation evidence remains valid and is not rewritten. This repair restores the intended dependency: **MSS-11 → SEC-01..09 → MSS-12 post-SEC re-proof → CCP-02**. CCP-01 remains completed_verified historical work; CCP-02 stays parked with no implementation authority.

MSS-12's existing packaging/workbench/balance/golden-proof implementation remains `completed_verified` for the corpus it actually consumed, but final supernatural-corpus coverage is provisional until SEC-09 finishes and MSS-12 is re-proved against the SEC output. The post-SEC re-proof may be evidence-only if no code changes are necessary, but it cannot be skipped.

## Tranches

1. **SEC-01 — Full Supernatural Corpus & Spell Coverage Audit** — `in_progress`  
   Normalize the 385 spells against Living Spellbooks, faction abilities, species innates, prestige powers, recovered RSR material, Rune Construction, rituals, and later MSS material. Detect duplicates, variants, missing descriptions, mechanically identical spells with different names, and powers that should not be duplicated as spells.
2. **SEC-02 — Multiversal Capability & Purpose Taxonomy** — `planned`  
   Stop treating spell school as the main coverage measure. Build a multidimensional matrix covering combat, defense, healing, mobility, exploration, survival, communication, information gathering, stealth, social interaction, crafting, infrastructure, logistics, environmental manipulation, travel, summoning, spirit interaction, anti-magic, portal work, temporal manipulation, reality manipulation, and mundane-quality-of-life utility. Define what complete actually means.
3. **SEC-03 — Effect-Family Expansion Audit** — `planned`  
   Re-evaluate the existing 14 effect families. Investigate whether coarse buckets such as Utility should split into first-class capabilities such as Adaptation/Resistance, Communication, Binding/Banishment, Resource Transfer, Environment/Weather, Purification/Corruption, Construction/Repair, Probability/Luck, Identity/Soul, Technology Interface, Spatial Containment, Causality and Translation. These are candidates, not pre-approved families.
4. **SEC-04 — Spell-Family & Variant Grammar** — `planned`  
   Establish when several spells are members of one family rather than unrelated records: elemental protection variants, bolt/burst/wall/aura/weapon/ward forms, single/group/area versions, lesser/greater versions, detect/locate/analyze versions, summon/create/control versions and similar structures. Variants may inherit structure without imposing a universal mathematical formula.
5. **SEC-05 — Tradition, Reality & Magic-Law Coverage Matrix** — `planned`  
   Cross the capability model against arcane, elemental, innate, shamanic, voodoo, divine, chaos, psychic/psionic, spirit-based, technological supernatural systems, mixed traditions, and setting-local systems. Determine whether capabilities vary by tradition/reality or are legitimately unavailable under some magic laws.
6. **SEC-06 — Core Multiversal Spell-Family Expansion** — `planned`  
   Fill broad reusable gaps in defense, mobility, sensory magic, communication, restoration, utility, environmental manipulation, object interaction, crafting assistance, containment, concealment, rescue, logistics, information and related everyday/adventuring uses so the catalog is not predominantly damage-oriented.
7. **SEC-07 — Exotic & Reality-Scale Spell Expansion** — `planned`  
   Cover Multiversal-specific capabilities such as spirit/soul magic, conceptual magic, anti-magic, causality, dimensional effects, portals, reality compatibility, timelines, void phenomena, supernatural technology, artificial magical systems, divine intervention frameworks, chaos effects, living spells, unusual species magic and setting-specific laws while keeping them scoped where required.
8. **SEC-08 — Redundancy, Balance, Progression & Usability Pass** — `planned`  
   Analyze every spell/family for purpose overlap, power-band distribution, counterplay, acquisition/access, concentration/duration burden, noncombat usefulness and discoverability. Search facets must include what a user wants to accomplish, not only school or element.
9. **SEC-09 — Multiversal Spell Coverage Proof** — `planned`  
   Produce the completeness matrix and require every compatible capability area to be covered, deliberately setting-restricted, owned by another supernatural mechanism, or explicitly unresolved. Hand the expanded corpus to MSS-12 for content packs, workbench, balance and golden proof.

## Invariants

- The retained 385-row `Magic_Spells.csv` corpus is evidence, not completeness proof by count alone.
- SEC never silently deletes, merges or replaces source spells. Duplicate/variant findings remain review dispositions until later governed acceptance.
- Powers, species innates, prestige/faction abilities, Living Spellbook effects, rituals, Rune constructions and other supernatural mechanisms keep their owning identities. Overlap does not automatically convert one mechanism into another.
- Source-stated mechanics are distinguished from mechanics completed/inferred during retained-corpus normalization.
- SEC-02 defines capability completeness; school/element counts alone are insufficient.
- SEC-03 candidate effect families remain investigative candidates until that tranche accepts them.
- SEC-04 family inheritance cannot invent a universal numeric formula.
- Reality/tradition incompatibility may be a valid deliberate restriction rather than a gap.
- RSR recovered assistant-generated material remains proposal-only unless independently supported or owner-approved.
- Completed MSS-01..11 remain controlling runtime authorities for their domains while SEC audits/expands content coverage.
- Existing MSS-12 implementation evidence remains historically valid but must be re-proved against SEC-09 output before supernatural-corpus completion is final.
- CCP-01 remains completed_verified; CCP-02 is parked and unauthorized until the post-SEC MSS-12 re-proof completes.
- AI may classify, compare and propose; it cannot canonize a merge, decide a power must become a spell, invent missing mechanics, or promote recovered proposals.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.
- No provider/payment activation, tester distribution, release or deployment is authorized by SEC.

## Current-work rule

`SEC-01-attempt-001` is the sole CURRENT application checkpoint and is `in_progress` on `integration/sec-01-supernatural-corpus-coverage-audit`. SEC-02 and later SEC work remain unauthorized until SEC-01 reaches `completed_verified`. CCP-02 remains parked and has no implementation authority.
