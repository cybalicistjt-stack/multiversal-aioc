# PPIA-05 — Completion Candidate

**Work item:** PPIA-05 — Species, Forms & Character Biology  
**State:** COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES  
**Owner:** John Brandon Turner

## Verified upstream milestones

### Foundation — PR #231

Squash merge: `74e2a5540ddee5560407f7bf1bc8f48e6eb0443c`

Established:

- 29 direct Species/Form/Biology PDFs / 654 pages;
- 6 supporting environment/Adaptation PDFs / 233 pages;
- governed 2,203-row mixed Species/Elementalist/Innate Ability surface: 260 Species Perks, 539 Innate Abilities and 1,404 Elementalist rows;
- supporting 1,018-row prestige/environment/special Ability surface including 296 Environment-Based Ability Collection rows;
- 60 detailed Shapeshifter Ability rows plus 57 pricing-only rows with zero automatic merges;
- 13-layer Species/Form/Biology identity-state taxonomy and 12 presentation profiles;
- explicit culture-versus-biology, Definition-versus-Character/runtime, source-versus-inference, permission, recovery and accessibility boundaries.

### Inspector / projection / reference cases — PR #232

Squash merge: `91a84ed83ed51c33e7c6a2a045fcdb7fa08aaf24`

Established:

- 13 Species/Form Inspector projection groups aligned one-to-one with the taxonomy;
- 14 governed action contracts;
- 20 reference cases: 12 contract-grounded, 5 synthetic QA and 3 guardrail, with zero canonical synthetic records;
- explicit lineage-evidence, Form/current-state, Adaptation, bioengineering, mixed-Ability, Shapeshifter, privacy, recovery, unknown-state and accessible-operation acceptance contracts.

### Integrated workflows — PR #233

Squash merge: `9aa72c8738070c0d94074abd3643b9145baaf163`

Established:

- 15 integrated Species/Form/Biology workflows;
- 10 authoritative mutation workflows with revalidation, expected-version and operation-ID/idempotency boundaries;
- 10 cross-domain handoff contracts;
- explicit coverage of all 20 PPIA-05 reference cases;
- cross-domain routing to F002, F004, PPIA-02, PPIA-03, F006/F007, F020/F021, PPIA-06, PPIA-08, PPIA-11 and PPIA-12 without absorbing those domains.

## Current completion-candidate package

This final package adds:

- `PPIA-05_SPECIES_FORMS_CHARACTER_BIOLOGY_EXPERIENCE_SPEC_v1.0.0.md` — integrated implementation-ready specification;
- `PPIA-05_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json` — 42 requirements across 14 acceptance categories;
- exact trace coverage for 13 projection groups, 14 action contracts, 15 workflows, 10 handoffs and all 20 reference cases;
- deterministic completion validation and CI.

The candidate branch continuity projection remains aligned to the active PPIA-05 completion action before exact-head validation. No `completed_verified` state is projected early.

## Completion coverage

The candidate packet covers:

1. reusable Species Definition, lineage/variant, Form Definition, trait/Ability Definition, Character selection and current body/form state separation;
2. culture, society, belief, philosophy, profession and learned behavior separation from immutable biology;
3. Species eligibility and Species Perk labeling separated from physiology classification;
4. 2,203-row mixed Ability ownership boundary and zero automatic biology promotion;
5. explicit lineage/subspecies/variant relationship evidence and no similarity auto-link;
6. Form Definition versus current Form state and lifecycle separation;
7. F006/F007 transformation execution and atomic result/cost behavior;
8. 60 detailed / 57 pricing-only Shapeshifter zero-auto-merge rule;
9. Suula-style Adaptation acquisition, learning, active-state and incompatibility separation;
10. environment-linked learned/contextual Ability versus biological Adaptation separation;
11. innate Ability/Species Perk execution without runtime reclassification of source ownership;
12. source-backed morphology, anatomy, senses, movement and physiology with no human-default filling;
13. explicit compatibility evidence and no universal-compatibility assumption;
14. Kola-Ha bioengineering/symbiosis as biological modification rather than generic equipment by default;
15. Character Species/Form selection, advancement and correction through F004 with append-only history;
16. PPIA-02 playable Creature conversion handoff without relabeling source Creature identity;
17. permission-before-projection and hidden biological non-inference;
18. operation-ID, expected-version, idempotency, ambiguous-network recovery and reconnect reauthorization;
19. keyboard/touch/screen-reader, compact/high-zoom/reflow, reduced-motion and textual morphology operation;
20. source/provenance/conflict/recommendation distinctions and explicit downstream ownership boundaries.

## Completion boundaries

PPIA-05 completion does **not**:

- mutate raw Species, Form, Ability or environment PDF/CSV source;
- restore the obsolete 487-object semantic database as content authority;
- automatically promote any row in the 2,203-row mixed Ability surface to Species/Form/biological ownership;
- classify every Species Perk or Innate Ability as physiology;
- convert environment-linked learned/contextual Abilities into biological Adaptations without explicit evidence;
- merge any Shapeshifter pricing-only row with a detailed Ability by name, tier, position, order or similarity;
- create lineage, Form identity or compatibility from shared naming, documents, appearance or narrative similarity;
- synthesize human-default anatomy, physiology, lifespan, breathing, movement, reproductive biology or metabolism;
- treat absence of an incompatibility rule as universal compatibility;
- convert temporary Effects, Conditions, equipment or Campaign environment into permanent source biology;
- expose hidden Forms, weaknesses, triggers or private Character biology through aggregates, warnings, errors, exports, diagnostics or AI context;
- absorb PPIA-02 Creature identity/ecology, PPIA-03 generic Asset behavior, PPIA-06 appearance authoring, PPIA-08 environment authoring, PPIA-11 balance calibration or PPIA-12 world/culture authoring;
- activate STAGE-A-A2;
- mutate application runtime;
- authorize release, deployment, tester access, paid services, production credentials or unsupported canonical promotion.

## Required completion evidence

PPIA-05 may become `completed_verified` only after:

1. the exact candidate head passes PPIA-05 completion validation;
2. every applicable PPIA Program, transition, continuity, interaction, operational and regression gate passes on that same exact head;
3. the candidate PR merges into canonical `main`;
4. the post-merge continuity checkpoint records the exact validated head, PR, merge SHA, `completed_verified` state and next dependency-optimized PPIA tranche.

Until all four conditions are satisfied, this document is a candidate, not a completion claim.
