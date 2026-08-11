# PPIA-05 — Species, Forms & Character Biology Experience Specification v1.0.0

**Work item:** PPIA-05  
**Status:** IMPLEMENTATION-READY DESIGN SPECIFICATION  
**Owner:** John Brandon Turner  
**Primary repository:** `cybalicistjt-stack/multiversal-aioc`  
**Application runtime mutation authorized by this document:** No  
**STAGE-A-A2 activation authorized by this document:** No

## 1. Purpose

PPIA-05 defines the implementation-ready Species, Forms & Character Biology experience without reopening completed Internal Alpha design. It binds reusable Species and Form Definitions, lineages and variants, biological traits and innate Abilities, morphology/body plans, Character Species/Form selection, current body/form state, transformations, Adaptations, senses, movement and physiology, compatibility and vulnerabilities, bioengineering/symbiosis, knowledge/reveal boundaries, provenance, recovery and accessible operation into one coherent contract.

The primary owning authorities remain **MV-IA-F002 — Universal Object Experience**, **MV-IA-F004 — Character Creation and Advancement**, **MV-IA-F006/F007 — authoritative Action and combat resolution**, **MV-IA-F020/F021 — permission-safe projection and recovery**, and **MV-IA-F022 — Accessibility and Adaptive Interface**. PPIA-02 owns Creature/NPC source and playable-conversion semantics. PPIA-03 owns generic Item/Asset/cybernetic semantics only where a source actually models an Asset or installed object. PPIA-06, PPIA-08, PPIA-11 and PPIA-12 retain their downstream appearance, environment-authoring, balance and world/culture responsibilities.

PPIA-05 does not authorize application implementation, release, deployment, tester access, paid services, credentials, production activation or unsupported canonical promotion.

## 2. Authority and source basis

### 2.1 Direct retained source library

The retained direct Species/Form/Biology source basis contains **29 direct Species/Form/Biology PDFs / 654 pages**. Exact filenames, page counts and SHA-256 values remain recorded in `PPIA-05_SOURCE_AND_DESIGN_INVENTORY.md`.

The retained sources include dedicated Species documents, `Oaran Species.PDF`, the Species Perks sources, `Mythragara vAlpha2.PDF`, `Suula.PDF`, `Kola-Ha Bioengineering.PDF`, and other source documents that demonstrate distinct Species, lineage, Form, Adaptation, morphology, physiology and biological-modification patterns. Source prose may mix biology, appearance, culture, history, belief, profession and other facets; document locality does not collapse those meanings.

### 2.2 Supporting environment and Adaptation sources

PPIA-05 also retains **6 supporting environment/Adaptation PDFs / 233 pages**. These provide context for environment-linked capability language but are not automatic physiology authority. An environment-based Ability can be learned, social, technical, exploratory, mystical, tactical or otherwise non-biological. **Environment linkage does not make an Ability a biological Adaptation.**

### 2.3 Governed mixed Ability surface

The governed Species/Elementalist/Innate Ability surface contains **2,203 rows**:

- **260 Species Perks**;
- **539 Innate Abilities**;
- **1,404 Elementalist rows**.

Dataset membership, tree adjacency, Species eligibility, naming, source-document placement or narrative similarity does not automatically establish biology ownership. A Species Perk can be biological, learned, cultural, mystical, technological or mixed. An Innate Ability label is evidence requiring source/rule interpretation, not permission to invent anatomy or physiology.

### 2.4 Supporting environment-Ability surface

The supporting prestige/environment/special Ability surface contains **1,018 rows**, including **296 Environment-Based Ability Collection rows**. PPIA-05 uses this surface as an Adaptation/classification cross-check only. PPIA-08 and PPIA-12 continue to own Campaign/Scene and world/environment authoring.

### 2.5 Shapeshifter reconciliation boundary

The retained Shapeshifter evidence contains **60 detailed Ability rows and 57 pricing-only rows**. Combat Forms are 20 detailed / 20 pricing-only; Environmental Adaptations 20 / 19; Utility Transformations 20 / 18. **Zero automatic merges are authorized.** Name, tier, position, order, similarity or apparent pairing cannot collapse a pricing-only row into a detailed Ability without exact evidence or an explicitly governed recommendation.

### 2.6 Source-truth states

Source fact, source absence, source-unspecified state, conflict, inference, recommendation, Character selection, Campaign reveal state, current body/form state, temporary Effect/Condition and environment constraint remain distinguishable.

**Unknown is not a human default.** Source-unspecified limbs, organs, lifespan, metabolism, breathing, movement, reproductive biology, compatibility, vulnerability, limitation or Adaptation state is not silently replaced with normal-human anatomy, universal compatibility, absence, zero or a fabricated value.

## 3. Thirteen semantic identity/state layers

PPIA-05 preserves thirteen semantic layers. An implementation may package them differently internally but may not collapse their meaning.

1. **Reusable Species Definition** — stable source identity, version, source-backed biological facts, eligibility/grants and provenance.
2. **Lineage / Subspecies / Species Variant** — explicit source-backed relationship identity, variant differences, grants and provenance.
3. **Reusable Form / Alternate-Form Definition** — Form identity, eligibility, source mechanics, morphology, senses/movement, limitations and provenance.
4. **Biological Trait / Species Perk / Innate Ability Definition** — stable trait/Ability identity, prerequisites, source-defined effect, sourced cost/limits, eligibility and biology-ownership classification.
5. **Morphology / Body Plan / Anatomy** — sourced size/body plan, limbs/organs, natural weapons, covering/exoskeleton/skin, reproductive/sex biology where sourced and visible biological markers.
6. **Character Species / Form Selection and Grants** — stable Character-scoped references, accepted selection, grants, rules profile, pack lock and validation state.
7. **Current Character Body / Form State** — current active Form, body configuration, Form-specific capabilities, current biological presentation and expected version.
8. **Transformation / Adaptation State** — active transformation, known/acquired Adaptations, active slots, sourced swap/cooldown/duration state and provenance.
9. **Senses / Movement / Physiology** — senses, breathing, movement modes, sourced speeds/constraints, environment tolerances, metabolism and lifespan where sourced.
10. **Biological Compatibility / Limits / Vulnerabilities** — explicit incompatibilities, resistances/vulnerabilities, Form exclusions, host compatibility, strain/rejection limits and body-plan requirements.
11. **Bioengineering / Symbiosis / Biological Modification** — source-backed biological modification relation, Form/growth/tuning state, host relationship, temporary/permanent status, strain/maintenance where sourced and modification history.
12. **Knowledge / Reveal / Visibility Projection** — Player-known biology, GM/source-truth visibility, revealed Forms, known vulnerabilities, private Character biology and projection provenance.
13. **Source / Provenance / History / Recovery** — source coordinates, fact/inference/recommendation/conflict state, selection history, transformation/Adaptation history, bioengineering history, operation IDs, expected versions and recovery receipts.

Definition inspection does not create Character selection. Form inspection does not activate a Form. Character selection does not rewrite a Species Definition. A transformation changes authorized current state, not source truth. Temporary Effects, Conditions, equipment and Campaign environment do not silently become permanent biology.

## 4. Species/Form Inspector and projection model

`PPIA-05_SPECIES_FORM_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json` defines thirteen field groups aligned one-to-one with the layers above and fourteen governed action contracts:

- `inspect_compare`;
- `select_species_form`;
- `choose_lineage_variant`;
- `playable_conversion_handoff`;
- `activate_end_form`;
- `invoke_transformation`;
- `acquire_swap_adaptation`;
- `use_innate_ability`;
- `validate_biology_compatibility`;
- `apply_bioengineering_modification`;
- `correction_respec_proposal`;
- `reveal_hide_biology`;
- `source_conflict_resolution_candidate`;
- `history_export_recovery`.

Every projection authorizes before Species/Form existence, body details, variants, hidden Forms, weaknesses, counts, facets, compare targets, compatibility warnings, provenance, history, exports, diagnostics, notifications or AI/service context are serialized or aggregated.

Hidden Forms, vulnerabilities, transformation triggers, private Character biology and restricted provenance are removed before aggregates. An unauthorized viewer must not infer hidden state from changed counts, missing capacity, compare results, warning text, action menus, failure strings, export rows, diagnostics or AI summaries.

## 5. Culture-versus-biology and classification boundary

Culture, society, belief, philosophy, profession, learned behavior, world history, faction role, ordinary learned skills, equipment, temporary Effects, temporary Conditions and Campaign environment are not immutable biology unless explicit source/rule evidence establishes a biological mechanism.

A Species-gated choice does not prove physiology. Species Perk is an eligibility/source-ownership label, not an anatomy label. Environment-based does not mean biological Adaptation. Same name, shared document, visual similarity or narrative similarity does not create lineage, Form identity, exact mechanics or compatibility.

The implementation must preserve biology-ownership classification and provenance separately from eligibility. Mixed or unresolved classification remains visible as such to authorized users rather than being normalized for UI convenience.

## 6. Lineages, subspecies and variants

Lineage/subspecies/variant relationships require explicit source-backed relationship evidence. Shared naming fragments, source-document grouping, appearance or thematic similarity are review hints only.

Character selection stores the chosen relationship by stable ID and version evidence. It does not mutate the reusable lineage graph. If the source relationship changes or conflicts, the Character retains attributable historical state and the owning correction workflow determines any later change.

## 7. Forms and current body state

A reusable Form Definition is distinct from a Character currently using that Form. Form inspection never activates it. Current-form state is server-authoritative Character/runtime state and includes expected-version/recovery semantics.

Permanent, temporary, alternate and transformation-driven Forms remain distinguishable where source rules distinguish them. A Form change records the current body-state delta and history; it does not rewrite the Species or Form Definition.

`Mythragara vAlpha2.PDF` is an explicit source anchor for shapeshifting, Form availability, sensory/mental shifts, limitations and Form traits. Exact mechanics remain source-backed; names alone do not supply missing rules.

## 8. Transformations and Shapeshifter operations

Transformation execution routes through MV-IA-F006/F007 or the owning Ability workflow when authoritative Action resolution applies. Eligibility, compatibility, target/context and governed Resource/cost requirements are validated before commit.

Accepted transformation result and governed costs commit atomically. Denied or failed-before-commit transformations consume nothing. Unauthorized error text cannot disclose hidden Forms, triggers or capabilities.

The 60 detailed / 57 pricing-only Shapeshifter boundary remains binding. Runtime transformation does not provide authority to reconcile, merge or invent source Ability records.

## 9. Adaptations and environment-linked capability

Known/acquired Adaptations remain distinct from currently active Adaptation slots/state. Acquisition, learning, activation or swap follows the explicit owning rule, including sourced costs, slots, incompatibilities, cooldowns and durations.

`Suula.PDF` is a key source anchor for active Adaptations, XP-purchased Adaptations, swapping, learning, incompatibilities, extremophile biology and visible markings. The application may express these mechanics only where supported by source/rule evidence.

Environment-Based Abilities remain a separate learned/contextual source surface unless explicit Species/Form/innate/body evidence establishes biological ownership. A Scene or world environment may constrain current capability without rewriting Species physiology.

## 10. Innate Abilities and Species Perks

Trait/Ability Definition identity remains separate from Character grant and execution state. Eligibility, prerequisites, source effect, costs/limits and biology-ownership classification are separately inspectable.

`use_innate_ability` routes authoritative execution through F006/F007 or the owning Ability workflow. Executing an Ability never reclassifies it as physiological. Outcome and governed costs commit atomically where applicable.

The mixed 2,203-row Ability dataset remains mixed. Elementalist rows do not become biology because they share a file with Species and Innate rows.

## 11. Morphology, anatomy, senses, movement and physiology

Morphology and physiology are source-backed fact surfaces, not default-filled Character sheets. Sourced facts may include size/body plan, limbs/organs, natural weapons, coverings, reproductive/sex biology, senses, breathing, locomotion, environmental tolerance, metabolism and lifespan.

Source absence remains unknown/source-unspecified. The UI must not synthesize human-default limbs, organs, breathing, reproductive biology, lifespan, metabolism or movement merely to avoid blank fields.

Appearance prose and mechanical biology remain distinguishable. PPIA-06 owns full visual Character Appearance Creator behavior; PPIA-05 provides the source-backed biological constraints and visible markers that PPIA-06 may consume.

Every diagrammatic/body-plan fact requires a textual equivalent and semantic label. Body-diagram pointing, silhouette recognition or color cannot be required to understand or select biology.

## 12. Compatibility, limits and vulnerabilities

Compatibility requires explicit source/rule evidence. **Absence of an incompatibility rule is not universal compatibility.** Unknown compatibility remains unknown and is handled by the owning workflow's blocking/warning policy rather than silently becoming compatible.

Hidden vulnerabilities and incompatibilities are filtered before compare results, warnings, failure text, action menus, counts, diagnostics and AI context. A service or assistant cannot infer or independently publish hidden biological weaknesses.

## 13. Bioengineering, symbiosis and modification

`Kola-Ha Bioengineering.PDF` establishes biological Forms/modification as a source-backed biological system that can be physical, sensory, psychic or environmental and can range from temporary Adaptation to permanent symbiotic evolution. These Forms are not generic equipment by default.

A modification operation requires explicit authority, host compatibility evidence, the sourced temporary/permanent rule, expected version and idempotency. Modification history is append-only.

PPIA-03 Asset/cybernetic semantics apply only where a source/rule actually models an Asset or installed object. PPIA-05 does not relabel biological Forms as inventory merely to reuse UI.

## 14. Character selection, advancement and correction

MV-IA-F004 owns Character Species/Form selection, grants, advancement and correction. Character state stores stable references and accepted grants under rules-profile and pack-lock validation.

Correction/respec operations preserve attributable before/after state and append history. They do not erase prior accepted state or rewrite reusable source Definitions. Unknown compatibility or missing source mechanics cannot be invented to make a correction succeed.

## 15. Playable Creature conversion

PPIA-02 owns source Creature/NPC identity and playable-conversion semantics. Conversion hands a source-backed playable Species/Form candidate into MV-IA-F004 without relabeling or mutating the original Creature Definition.

Source Creature, playable Species/Form draft and Character instance remain separate identities. Retained, normalized, excluded and unlocked facts remain attributable. Linked Abilities stay stable references instead of copied or forked rule text.

## 16. Integrated workflow set

`PPIA-05_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json` defines **15 integrated workflows**:

1. `SF-WF-001` — Library / Species / Form reference and comparison.
2. `SF-WF-002` — Character creation Species / Form selection.
3. `SF-WF-003` — Lineage / subspecies / variant selection.
4. `SF-WF-004` — Character Species / Form correction and advancement.
5. `SF-WF-005` — Current Form activation, end and reversion.
6. `SF-WF-006` — Transformation execution.
7. `SF-WF-007` — Adaptation acquisition, learning, activation and swap.
8. `SF-WF-008` — Innate Ability / Species Perk execution.
9. `SF-WF-009` — Morphology, senses, movement and physiology projection.
10. `SF-WF-010` — Biological compatibility / limits validation.
11. `SF-WF-011` — Bioengineering / symbiosis / biological modification.
12. `SF-WF-012` — Playable Creature conversion to Character Species/Form draft.
13. `SF-WF-013` — Campaign reveal / hidden biological knowledge.
14. `SF-WF-014` — Source conflict / recommendation / provenance review.
15. `SF-WF-015` — History / export / reconnect / ambiguous-network recovery.

Ten of these workflows perform authoritative mutations. Mutation workflows define revalidation points, expected-version/concurrency boundaries and operation-ID/idempotency recovery.

## 17. Cross-domain handoffs

The workflow matrix defines **10 cross-domain handoff contracts** (`SF-HO-001` through `SF-HO-010`). Handoffs carry stable IDs, semantic context, version/provenance and the minimum authorized state. A receiving workflow does not inherit mutation authority merely because another surface authorized inspection.

The owning boundaries are:

- **F002** — Universal Object browse/inspect/compare and constrained-selection surfaces;
- **F004** — Character selection, grants, advancement and correction;
- **PPIA-02** — Creature/NPC forms and playable conversion source semantics;
- **PPIA-03** — explicit Item/Asset/cybernetic relations only;
- **F006/F007** — authoritative Action/result/cost behavior;
- **F020/F021** — permission-safe projection, expected-version, reconnect and idempotent recovery;
- **PPIA-06** — visual Character Appearance Creator;
- **PPIA-08** — Campaign/Scene environment authoring;
- **PPIA-11** — encounter and balance calibration;
- **PPIA-12** — world-specific culture, history and environment extensions.

PPIA-05 does not absorb those domains.

## 18. Privacy, reveal and service/AI projection

Authorization occurs before Species/Form existence, search, variant lists, body details, hidden Forms, vulnerabilities, compare targets, counts, facets, warnings, provenance, exports, diagnostics, notifications and AI/service retrieval.

Unknown-to-Player is not false-in-source. Campaign reveal state is audience-scoped and never rewrites source truth. GM authority is Campaign-scoped and does not imply unrelated user-private or other-Campaign Character biology access. Assistant GM authority remains delegation-scoped.

Creator/Owner/Admin authoring authority does not silently become Character/runtime mutation authority. Service/AI actors receive the minimum necessary role-safe projection and cannot independently choose Species/Form, transform, reveal, respec, bioengineer, classify unresolved content or promote source recommendations.

## 19. Recovery, concurrency and reconnect

Every authoritative Species/Form/biology mutation uses expected-version or an equivalent concurrency boundary and an operation identity/idempotency contract. **No broad offline authoritative Species/Form or biology mutation is permitted.**

If a mutation result is ambiguous, the client queries operation status using the original operation ID before retry. Retry reuses the same idempotency identity. It cannot duplicate Species/Form selection, correction, Form activation/reversion, transformation, Adaptation acquisition/swap, Ability cost, bioengineering state, reveal state or history entries.

Reconnect reauthorizes current Character/Campaign, role, rules profile, pack lock, visible Forms/weaknesses, permissions, current body/form state, relevant versions and operation status. Cached revoked or hidden state cannot restore authority.

## 20. Responsive and accessible operation

Expanded layouts may show multi-column identity, morphology, traits, Forms, compatibility and history regions. Medium layouts prioritize identity, source status, current Character/Form state and primary action. Compact layouts use single-column cards/sheets with persistent identity and current state while secondary sections collapse without losing validation meaning.

All core workflows support keyboard and touch. Screen-reader output announces semantic layer, source/classification/conflict status, prerequisites, current Form state, Adaptation state, compatibility/unknown state, validation errors and authoritative operation result.

High zoom reflows tables and relation graphs into labeled rows/cards. Reduced-motion users receive transformation/state results textually; animation is never the sole carrier of meaning. Color, drag, hover, silhouette recognition, body-diagram pointing and animation are never required to complete a workflow.

## 21. Reference-case acceptance corpus

`PPIA-05_REFERENCE_CASES_v0.1.0.json` contains **20 reference cases**: **12 contract-grounded, 5 synthetic QA and 3 guardrail cases**, with zero canonical synthetic records.

The corpus covers Species Definition versus Character selection, culture/biology separation, mixed Oaran facets, Species Perk classification, mixed-dataset non-promotion, explicit lineage evidence, Mythragara Form/current-state separation, Shapeshifter zero-auto-merge, Suula Adaptation state, environment-Ability separation, Kola-Ha bioengineering, atomic transformation, unknown anatomy, compatibility uncertainty, hidden biology non-inference, playable Creature conversion, temporary Effect/Condition/equipment/environment boundaries, ambiguous-network recovery, accessible nonvisual operation and source-conflict/provenance behavior.

Every reference case is traced by the integrated workflow layer and the acceptance/traceability matrix.

## 22. Acceptance and traceability

`PPIA-05_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json` defines **42 acceptance requirements across 14 categories**. It traces exactly:

- **13** Species/Form Inspector projection groups;
- **14** governed action contracts;
- **15** integrated workflows;
- **10** cross-domain handoffs;
- **20** reference cases.

The matrix is the deterministic bridge from source/design evidence to implementation and QA acceptance. A requirement cannot be considered satisfied merely because a screen exists; its semantic, privacy, source, recovery and accessibility constraints remain binding.

## 23. Downstream ownership and non-expansion boundary

PPIA-05 is deliberately bounded. It provides biological facts, rules, state and handoffs needed by other work, but it does not absorb:

- PPIA-06 visual appearance editing and full character-appearance creator behavior;
- PPIA-08 Campaign/Scene environment authoring;
- PPIA-11 encounter/balance calibration;
- PPIA-12 world-specific culture, history, faction or environment authoring;
- generic PPIA-03 Item/Asset inventory behavior unless source rules explicitly model an Asset/cybernetic/installable relation;
- PPIA-02 Creature/NPC source identity and ecology beyond the defined playable-conversion handoff.

Culture remains authored as culture. Environment remains authored as environment. Biology remains source/rule-backed biology.

## 24. Completion boundaries

PPIA-05 completion does **not**:

- alter raw Species, Form, Ability or environment PDF/CSV source material;
- restore the obsolete 487-object semantic database as content authority;
- automatically promote any mixed Ability row to Species/Form/biological ownership;
- classify every Species Perk or Innate Ability as physiology;
- convert learned or contextual environment Abilities into biological Adaptations without explicit evidence;
- merge any of the 57 Shapeshifter pricing-only rows into the 60 detailed rows by name, tier, order, position or similarity;
- create lineage, Form identity or compatibility from same-name, shared-document, visual or narrative similarity;
- invent human-default anatomy, physiology, lifespan, breathing, movement, reproductive biology or metabolism;
- treat absence of incompatibility as universal compatibility;
- convert temporary Effects, Conditions, equipment or Campaign environment into permanent source biology;
- expose hidden Forms, weaknesses, triggers or private Character biology through counts, warnings, errors, exports, diagnostics or AI context;
- activate STAGE-A-A2;
- mutate application runtime;
- authorize release, deployment, tester access, paid services, production credentials or unsupported canonical promotion.

## 25. Implementation handoff

An implementation conforming to PPIA-05 must begin from the verified source/taxonomy, Inspector/action, reference-case and workflow/handoff artifacts rather than reconstructing biology from prose or UI assumptions.

The implementation team must preserve stable IDs, source/version provenance, Character/source/runtime separation, classification uncertainty, privacy filtering, expected-version/idempotency recovery and accessibility from the first data model through final UI. It must route ownership to F002/F004/F006/F007/F020/F021, PPIA-02, PPIA-03 and downstream PPIA-06/08/11/12 exactly as defined instead of locally duplicating those systems.

This specification is implementation-ready design evidence only. PPIA-05 may be marked `completed_verified` only after its exact completion candidate passes every applicable repository gate, merges to canonical `main`, and the post-merge completion checkpoint records the exact validated head, PR, merge SHA and next dependency-optimized PPIA tranche.
