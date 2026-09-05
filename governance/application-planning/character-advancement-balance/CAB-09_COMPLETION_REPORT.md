# CAB-09 — Completion Report

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-09 — Acquisition & Eligibility  
**Status:** `completed_verified` candidate pending branch merge  
**Decision authority:** standing owner recommendation delegation from `CAB-08_OWNER_DECISIONS_2026-09-05.md`

## Completed work

CAB-09:

1. separated **eligibility** from **acquisition** and both from XP affordability;
2. defined thirteen acquisition modes covering ordinary purchase, creation selection, grants, source-qualified options, training, exposure/acclimation, membership, Prestige, magic/archetype access, bonds/installations, creature relationships, narrative/milestone acquisition, and temporary-state grants;
3. established a first-class eligibility-dimension model;
4. reconciled Species/innate acquisition with PPIA-05 biology/source-ownership rules;
5. reconciled environment/adaptation acquisition with exposure/context rules;
6. preserved Prestige Tier-3 entry and faction/profession acquisition distinctions;
7. preserved the current structured spell rule: 0 direct spell-learning XP with archetype/caster-tier/capacity semantics;
8. separated permanent Character advancement from externally dependent grants;
9. integrated CEW/CCP mount/pet/familiar/companion eligibility without creating ownership or relationship state;
10. established `acquisition_unresolved` for source silence;
11. defined acquisition projection states and receipt/provenance requirements;
12. recorded seven recommendations as owner-approved under the standing CAB delegation.

## Source findings

- The bounded Ability corpus remains 4,816 records across the five CAB CSVs.
- The 2,203-row Species/Innate surface is mixed: 260 Species Perks, 539 Innate Abilities, 1,404 Elementalist rows. Dataset membership is not automatic biology or grant authority.
- The 1,018-row Prestige/Environment surface includes 296 Environment-Based Ability rows and 192 Prestige-tree rows among other special content.
- The profession/crafting surface contains 221 rows with authored tool, ingredient, Skill/check, prior-tree and situational requirements.
- The magic/faction surface contains 118 rows with source-specific specialization, faction, training and ritual semantics.
- The structured spell surface contains 385 spells. All publish archetype access/minimum caster tier and state 0 XP for the spell itself, with XP used for slots/ready-known capacity.
- CEW-11 establishes that relationship-pathway eligibility does not create ownership, bond, taming, training, obedience, placement or consent.

## Owner-delegated decisions

All seven CAB-09 recommendations are adopted:

1. eligibility does not equal acquisition/ownership;
2. Species/innate acquisition distinguishes automatic grant, source-qualified selection, creation-only access and explicit later/cross-Species bridges;
3. environmental presence does not automatically grant permanent advancement;
4. permanent learned faction/profession capability is separated from continuing-affiliation-dependent grants, and Prestige retains its explicit Tier-3 entry transaction;
5. structured spells retain archetype/caster-tier access and 0 direct per-spell learning XP;
6. external dependencies and creature relationships remain distinct from permanent Character ownership;
7. source silence remains unresolved rather than inferred.

Authority: `CAB-09_OWNER_DECISIONS_2026-09-05.md`.

## Unresolved / deferred

CAB-09 intentionally does not resolve:

- exact Attribute, Skill, Knowledge and proficiency prices or formulas — CAB-10;
- corpus-wide missing acquisition classification — CAB-11;
- structural tree-entry defects — CAB-12;
- high-risk transformations, summon/grant chains, external dependency exploits and special acquisition combinations — CAB-13;
- equal-XP/reference-value consequences of free/granted access — CAB-14/15;
- learning/acclimation duration and campaign pacing — CAB-16/18;
- refunds/corrections after eligibility or dependency changes — CAB-19;
- final corpus repair implementation map — CAB-22.

No Ability corpus rows were silently rewritten and no Multiversal-app implementation authority was created.

## Exact successor

**CAB-10 — Attributes, Skills & Proficiencies** — `selected_not_started`.