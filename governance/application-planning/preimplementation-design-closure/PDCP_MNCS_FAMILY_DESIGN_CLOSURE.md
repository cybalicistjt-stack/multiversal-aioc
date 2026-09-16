# PDCP — MNCS Family Design Closure

**Program:** MNCS — Multiversal NPC & Creature Studio  
**PDCP status:** design-closed family reduction  
**Implementation authority:** none  
**Historical baseline:** 24 tranches  
**Effective implementation/proof plan:** 13 tranches  
**Capability loss detected:** false

## Reduction decision

MNCS remains the creator-facing NPC/creature construction, progressive-resolution and runtime-handoff studio. It does **not** become a generic procedural-generation engine, autonomous-agent engine, life-simulation runtime, reputation ledger, general AI layer, provenance/versioning platform, or presentation renderer.

The reduced family keeps only implementation seams that remain distinct after applying completed owner contracts and PDCP Packets 01, 03, 05, 06 and 07.

Effective surviving order:

`MNCS-01 → MNCS-04 → MNCS-05 → MNCS-06 → MNCS-08 → MNCS-10 → MNCS-12 → MNCS-14 → MNCS-15 → MNCS-18 → MNCS-20 → MNCS-22 → MNCS-24`

Historical IDs remain provenance. Sparse IDs are intentional.

## Owner boundary conclusions

### Generic generation infrastructure

PCA recipe/generation infrastructure remains the reusable DAG/seed/cache/batch substrate. MNCS supplies NPC/creature-specific recipes, constraints, selective-regeneration policy and interpretation. Historical `MNCS-02` and `MNCS-03` therefore fold into the studio core rather than survive as parallel generic engines.

### Entity truth and progressive resolution

PPIA-02 and Character/NPC/Creature owners retain Definition, placement, live instance, playable conversion and entity identity authority. Packet 06 closes aggregate↔individual accounting, refinement/collapse and fidelity semantics. MNCS implements the creator-facing bindings and promotion/demotion workflows only.

### Social/autonomous behavior

PDCP Packet 01 closes social-decision/norm semantics; Packet 03 closes bounded autonomous selection/offscreen-action semantics. MNCS retains persona, knowledge, relationship/reputation, creature-behavior and roleplay-authoring inputs but does not build a second social-decision or autonomous-agent runtime.

### Life context

DPL/Profession, household/organization, Economy and Project/Time owners retain work, household, schedule, project, service and life-simulation truth. Historical `MNCS-09` has no standalone MNCS runtime after owner absorption. NPC-specific life-context projections bind into `MNCS-06`, group/population construction in `MNCS-15`, continuity in `MNCS-20`, and final proof in `MNCS-24`.

### Mechanics

Species/Form, Ability, Action/Event, Effect, Condition, Resource, Inventory/Asset, progression and CAB/domain owners retain mechanics truth. `MNCS-10` becomes the single mechanics-on-demand/loadout/capability composition seam by absorbing historical `MNCS-11`.

### Creature ecology and behavior

World/Environment/Species/Form retain ecological truth and live Action/Combat owners retain adjudication. `MNCS-12` absorbs historical `MNCS-13` as one creature ecology/behavior/tactics authoring seam; `MNCS-14` remains separate because species/form/stage/template/variant composition has different compatibility and provenance work.

### Group and population generation

Packet 06 supplies the shared multi-resolution accounting contract. `MNCS-15` absorbs historical `15+16+17` as one social-group/population/ecosystem-cohort generation and individualization seam. It must support households/crews/crowds and creature herds/packs/swarms without materializing every member or double-counting promoted individuals.

### Privacy, conversation prep and reveal

`MNCS-18` absorbs historical `MNCS-19` because secrets/aliases/reveal state and at-table roleplay/conversation prep share the same permission-filtered GM-facing dossier surface. Dialogue/social runtime authority remains elsewhere.

### Continuity and simulation resolution

Packet 05 closes persistent-history semantics and Packet 06 closes resolution changes. `MNCS-20` absorbs historical `MNCS-21` as one continuity, event-history, promotion/demotion/retirement and resolution-management seam. Regeneration cannot overwrite lived history.

### Batch/import/review/provenance/AI

ARI/PCA own generic provenance, rights, version/review/import-export and production governance; Packet 07 owns generic creator review/preview/debug boundaries; provider orchestration remains generic infrastructure. Historical `MNCS-23` therefore has no standalone runtime. NPC/creature-specific presets/batch recipes bind into `MNCS-01/05/15`; structured handoff into `MNCS-22`; provenance/review/AI-candidate evidence into `MNCS-24`.

### Runtime handoff

`MNCS-22` remains distinct. Acceptance into Scene/Encounter/Social/Investigation/Exploration/MAS and placement/live-instance creation are real integration seams and should not be buried inside golden proof.

## Surviving implementation/proof tranches

1. **MNCS-01 — Studio Core, NPC/Creature Recipe/Constraint Engine & Resolution Authority**  
   Absorbs historical 01, 02 and 03 plus MNCS-specific batch/preset residuals from 23. Implements the creator workspace, stable candidate IDs, field locks/rerolls, deterministic recipe receipts, authorized context projection and resolution-ladder invariants over shared PCA/PPIA/Packet-06 substrates.

2. **MNCS-04 — Identity, Naming, Culture, Language, Demographic & Origin Construction**  
   Retained as a distinct identity/origin construction seam.

3. **MNCS-05 — Instant Improv, Role-First & Situation-First Generation**  
   Retained as the five-second GM workflow; uses the core recipe/constraint system without forcing dossier depth.

4. **MNCS-06 — Persona, Goals, Knowledge, Belief & Actor-Context Authoring**  
   Absorbs historical 06+07 and life-context projection residuals from 09. Supplies Packet-01/03 actor inputs without becoming social/autonomous runtime authority.

5. **MNCS-08 — Relationships, Factions, Reputation & Party-Association Influence**  
   Retained to protect the MIB-09 integration, Campaign-scoped party-association decomposition, event attribution and privacy requirements.

6. **MNCS-10 — Mechanics-on-Demand, Rules Profile, Ability, Equipment & Capability Composition**  
   Absorbs historical 10+11. References canonical mechanics rather than copying them.

7. **MNCS-12 — Creature Ecology, Behavior, Social Structure, Territory & Tactics Authoring**  
   Absorbs historical 12+13 while preserving owner-domain ecology truth and live adjudication boundaries.

8. **MNCS-14 — Species, Form, Stage, Template, Variant, Mutation & Role Composition**  
   Retained as the compatibility/provenance seam for reusable creature/NPC variation.

9. **MNCS-15 — Household, Crew, Crowd, Population, Herd/Pack/Swarm & Ecosystem-Cohort Generation**  
   Absorbs historical 15+16+17 plus group/life-context residuals from 09. Uses Packet-06 accounting and stable individualization.

10. **MNCS-18 — Secrets, Aliases, Reveal Conditions, Conversation Prep & Roleplay Card**  
    Absorbs historical 18+19. Permission filtering occurs before search, counts, summaries, exports and AI context.

11. **MNCS-20 — Continuity, Events, Advancement, Life/Ecology Change & Resolution Management**  
    Absorbs historical 20+21 plus continuity residuals from 09. Preserves identity/history across promotion, demotion, retirement and reduced simulation detail.

12. **MNCS-22 — Governed Runtime Handoff & MAS Cast Integration**  
    Retained for acceptance/placement/live-instance handoff into Scene, Encounter, Social, Investigation, Exploration, Combat and Adventure workflows.

13. **MNCS-24 — Golden Progressive NPC/Creature Generation & Campaign-Continuity Proof**  
    Retained final proof; also carries MNCS-23 domain-specific import/review/provenance/AI-candidate evidence.

## Historical tranche dispositions

The machine-readable `PDCP_MNCS_REDUCTION_RECEIPT.json` records all 24 baseline rows. No historical tranche is silently dropped.

## Cross-family overlap resolution

- **PCA-02/03 and production governance:** generic recipe/DAG/generation/cache/batch infrastructure.
- **PPIA-02 / Character/NPC/Creature:** entity identity, Definition/placement/live-instance/conversion truth.
- **MCCS:** appearance/presentation outputs only.
- **MIB-09:** relationship/reputation mutation and attribution.
- **DPL/Profession + Project/Time + Economy/Organization:** life/work/household/schedule/project truth.
- **PDCP Packet 01:** social decision/norm contracts.
- **PDCP Packet 03:** bounded autonomy/offscreen-action contracts.
- **PDCP Packet 05:** history/legacy/deferred-consequence semantics.
- **PDCP Packet 06:** multi-resolution aggregate/cohort/individual semantics.
- **PDCP Packet 07:** generic preview/review/debug/AI-boundary semantics.
- **reduced MRCS:** reusable NPC/creature role/behavior/template definitions.
- **reduced GPR + Action/Event/domain runtimes:** accepted gameplay execution.
- **ARI/PCA:** provenance/rights/version/review/import-export infrastructure.
- **MAS:** downstream Adventure cast consumption; no Adventure-only duplicate NPC generator.

## Golden validation vectors

The reduced implementation must preserve at least these 48 vectors:

1. stable candidate identity survives selective reroll;
2. locked field is never overwritten by regeneration;
3. accepted field conflict is reported, not silently replaced;
4. same deterministic recipe/seed/context yields the same deterministic receipt where claimed;
5. unknown context remains unresolved rather than invented;
6. unauthorized hidden context is filtered before generation;
7. instant-improv NPC is playable without full dossier construction;
8. improvised NPC can deepen without identity replacement;
9. nonhuman/nameless identity construction does not force human naming assumptions;
10. culture/language/origin proposal remains distinct from accepted truth;
11. persona values/goals/fears remain portrayal inputs rather than mind-control authority;
12. knowledge, belief, suspicion and misinformation remain distinct;
13. actor-relative knowledge prevents omniscient autonomous context;
14. life-context projection references DPL/Project/Economy owners rather than cloning them;
15. direct and party-association reputation remain separately inspectable;
16. party-association effect remains Campaign-scoped;
17. association reputation preserves initiating Event/actor attribution;
18. hidden reputation data does not leak through counts/search/AI;
19. mechanics-on-demand can stop at qualitative/minimal competence;
20. missing numeric mechanics are not fabricated;
21. abilities/equipment/resources reference owner records rather than copied prose;
22. hidden inventory remains permission-filtered;
23. ecology inputs respect World/Environment/Species constraints;
24. creature behavior package does not auto-adjudicate live combat;
25. predator/prey/resource relationships remain ecological guidance until owner Events commit consequences;
26. species/form/stage/template composition validates compatibility;
27. variants preserve base/provenance instead of cloning full unrelated definitions;
28. household/crew group generation creates explicit member relationships;
29. population generation does not materialize every member;
30. promoted population member is removed from exclusive aggregate remainder;
31. herd/pack/swarm generation shares aggregate accounting without forcing humanoid group semantics;
32. aggregate refinement cannot invent personal history retroactively;
33. persistent individual survives later aggregate collapse;
34. group/population counts never double-count individualized members;
35. secrets/reveal layers are filtered before player-facing projection;
36. aliases/disguises do not rewrite canonical identity;
37. roleplay card can show safe cues without exposing private motives;
38. conversation prep does not become autonomous dialogue authority;
39. authoritative Events update continuity without regeneration overwriting history;
40. promotion/demotion changes active detail, not identity/history;
41. retirement/archive state preserves historical references;
42. offscreen/catch-up behavior uses canonical time/Event semantics rather than wall clock;
43. Scene/Encounter handoff creates/updates the correct placement/live-instance layer;
44. MAS cast handoff preserves source/version/provenance;
45. generic import/review/provenance remains ARI/PCA-backed rather than duplicated;
46. optional AI disabled still permits every blocking generation/construction path;
47. AI enrichment remains visibility-safe candidate content only;
48. full golden flow proves NPC, creature, group/population, reputation, continuity and runtime handoff with no duplicate identity or owner-authority leak.

## Roadmap/DAG reconciliation

`MNCS-01` remains the family start milestone and `MNCS-24` remains the final/golden milestone consumed by downstream gates. No DAG mutation is required for this reduction.

Historical baseline: **24**.  
Effective future implementation/proof tranches: **13**.  
Standalone tranches removed: **11**.  
Capability loss: **none detected**.

Next PDCP family review after merge: **MCCS**.
