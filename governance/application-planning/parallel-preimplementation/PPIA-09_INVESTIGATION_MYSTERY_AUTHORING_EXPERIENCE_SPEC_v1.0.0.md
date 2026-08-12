# PPIA-09 — Investigation & Mystery Authoring Kit Experience Specification v1.0.0

Status: **COMPLETION CANDIDATE — implementation-ready design contract; not complete until the exact completion PR head passes required validation and merges.**

## 1. Purpose

PPIA-09 defines the implementation-ready Investigation & Mystery Authoring experience over the verified Internal Alpha Investigation/Clue Board contract and retained source material. It supports GM mystery construction, Player investigation, clues and evidence, observations and claims, hypotheses and typed connections, timeline/alibi review, contradiction and uncertainty review, reveal/knowledge controls, solvability/redundancy review, stall recovery, conclusions/history, recovery/accessibility, and proposal-only AI.

PPIA-09 does **not** replace Campaign/Scene/Session ownership, source-domain Item/Creature/NPC/Vehicle/Setting ownership, World/Setting chronology, action/ability resolution, permission infrastructure, recovery infrastructure, accessibility standards, or application runtime authority.

## 2. Verified source boundary

The retained source/design boundary is:

- **3 directly relevant PDFs / 53 visually reviewed pages**;
- **4 structured support CSVs / 4,936 rows**;
- **109 explicit Investigation/Knowledge ability-tree rows** in `Abilities_Core.csv`;
- verified MV-IA-F011 with **10 record families, 15 typed connection predicates, and 24 deterministic fixtures**;
- `V05_Investigation.md` as retained screen/design intent;
- **The Vanishing of Dr. Wen** retained as the source-grounded reference-mystery/dossier anchor without inventing missing source facts.

Direct source supports clues/evidence/testimony/environmental observations, distinct discovery and analysis stages, unreliable witnesses, false evidence/red herrings, contradictions, temporal reasoning, surface/hidden/revealed information, dynamic/extra clues, cross-case correlation, provenance, and the guidance that important information should appear in **at least two places**.

The source does **not** define a universal confidence probability scale, deterministic solvability algorithm, universal clue count, universal false-lead fairness threshold, automatic contradiction truth resolver, universal required/optional revelation schema, or universal success/failure formula. Those gaps remain explicit.

## 3. Semantic and presentation model

The completed design retains **16 semantic identity/state layers** and **12 presentation profiles**.

The 16 layers are:
1. Investigation case definition.
2. Objective truth and GM solution.
3. Clue definition and source template.
4. Campaign clue discovery and analysis state.
5. Observation, claim and statement.
6. Evidence and owning-domain reference.
7. Witness/source reliability and authenticity.
8. Hypothesis, theory and deduction.
9. Typed connection and semantic relationship.
10. Question, lead and next step.
11. Timeline, temporal order and alibi.
12. Contradiction, false lead and uncertainty.
13. Discovery condition, reveal and knowledge audience.
14. Solvability, redundancy, progression and stall recovery.
15. Conclusion, resolution, outcome and history.
16. Permission, provenance, version, recovery and accessibility.

The 12 presentation profiles include the Investigation dashboard, clue-board/semantic connection view, clue/campaign-clue inspector, evidence/provenance inspector, timeline/alibi view, witness/source/claim profile, hypothesis builder, GM truth/solution/reveal controls, lead/research tracker, solvability/redundancy audit, reference-mystery/dossier workbench, and history/recovery/accessible linear view.

## 4. Inspector and governed action surface

The implementation contract exposes **16 permission-safe projection groups**, one-to-one with the semantic layers.

It defines **30 governed actions**:
- **22 authoritative mutations**;
- **8 read actions**.

Every authoritative mutation reauthorizes and revalidates current versions, requires `expected_version` plus stable `operation_id`, and uses operation-status/current-version lookup before retry after an ambiguous result. Blind last-write-wins and duplicate authoritative retry are forbidden.

## 5. Truth, belief, evidence and uncertainty

Objective truth, GM solution/conclusion, clue, observation, claim, evidence, hypothesis and Player knowledge are separately typed.

A visible clue or claim may be true, false, incomplete, misleading or unresolved. Visibility never implies truth. Confidence, relevance, authenticity and source reliability are attributable governed annotations; they are not objective truth probabilities and have no mandatory universal numeric scale.

Contradiction records preserve the material in tension and its rationale. Contradiction detection or review **never automatically adjudicates which side is true**. False leads, lies, corrupted evidence and unreliable testimony remain attributable authored content and cannot silently rewrite objective truth.

## 6. Evidence and chronology ownership

Evidence stores `ownerDomain`, `objectId`, `objectVersion` and Investigation-local evidence role/notes. Referencing evidence does not copy or transfer ownership from Items, Creatures/NPCs, Vehicles, Settings, Events or other owning domains.

World/Setting chronology remains **PPIA-12-owned**. PPIA-09 may author case-local timeline/alibi records and permission-safe references to Setting chronology, but a hidden world fact does not automatically become Player knowledge.

## 7. Reveal and permission model

Authorization and permission filtering occur **before** protected truth, clues, links, sources, counts, search, exports, realtime payloads, diagnostics, notifications, AI context, or other derivative aggregates are resolved.

Reveal/withhold/revoke is an explicit governed mutation. Research or Knowledge success may discover or interpret information through owning rules but never bypasses reveal permissions or converts hidden truth into Player-visible state by implication.

## 8. Solvability, redundancy and stall recovery

Solvability diagnostics are deterministic and **read-only** over explicitly authored revelation dependencies/routes. They may report reachable/unreachable required revelations, route counts, single points, circular dependencies, stalls and recovery routes. They never solve the mystery, invent a missing route, mutate objective truth, or change reveal state.

The direct-source **at least two places** guidance is implemented as an authoring warning for important information with fewer than two distinct explicit routes. It is not a universal clue-count law and does not guarantee mystery quality or Player success.

False-lead/corruption diagnostics identify authored risk patterns and recovery routes. They do not create a universal fairness threshold or truth verdict. Dynamic/extra clues retain trigger/delivery reason, source, audience, author and durable Event provenance.

## 9. Reference corpus

The deterministic corpus contains **36 contiguous reference cases**:
- `PPIA09-RC-001..024` preserve all **24 F011 fixtures one-to-one**;
- `PPIA09-RC-025..036` add deeper PPIA-09 cases including The Vanishing of Dr. Wen projection integrity, required-revelation reachability/redundancy, circular dependency, false-lead recovery, sole misleading route, timeline/alibi contradiction review, source-quality separation, research permission, hidden world chronology, dynamic clue provenance and cross-case correlation.

## 10. Integrated workflows

The authoring kit defines **18 end-to-end Investigation/Mystery workflows**. **15 perform authoritative mutation** and **3 are read-only review/recovery/audit workflows**.

Together they cover case/truth setup, clue definition and instantiation, discovery/analysis, evidence and statements, source-quality annotations, hypotheses/connections, leads/research, timeline/alibi, contradiction/false leads, revelation dependencies/solvability, stall recovery, reveal control, Player review, GM dossier/reference-mystery authoring, conclusion/history, AI proposal acceptance, reconnect/accessibility, and cross-domain audit.

Workflow traceability covers all **16 projection groups, 12 presentation profiles, 30 actions, 36 reference cases and 12 domain handoffs with zero coverage gaps**. Each reference case has exactly one primary workflow assignment.

## 11. Accessibility and nonvisual authority

Spatial clue-board placement and graph position are presentation state, not semantic authority. Typed predicates, ordered lists, tables and semantic linear representations remain authoritative equivalents. **Semantic nonvisual representations are mandatory authoritative equivalents for every graph, timeline, relationship, clue-board, and Investigation workflow.**

Keyboard, touch, high-zoom/reflow and screen-reader operation must support the complete Investigation workflow. Drag, hover, color, graph position and animation are never the sole required input or meaning.

## 12. AI boundary

AI may propose organization, connections, theories, clue material, mystery material or review suggestions only from authorized context. Generated output remains **proposal-only** until an authorized user explicitly accepts it through the same governed action/version/provenance rules as human-authored material. AI cannot decide objective truth, reveal protected facts, resolve contradictions authoritatively, or commit state on its own.

## 13. Completion acceptance

The blocking completion matrix contains **48 requirements across 16 categories**, three per semantic category. Every requirement is blocking and traced to governed projections/actions/workflows and deterministic reference evidence. Collectively the matrix exercises all 36 reference cases and records zero intended traceability gaps.

Completion requires the exact PR head to pass `Validate PPIA-09 Completion Contract` plus every applicable repository regression and then merge. A branch, commit, artifact or open PR alone is not completion.

## 14. Activation boundaries

- Application runtime mutation authorized: **No**.
- STAGE-A-A2 activation authorized: **No**.
- Release authorized: **No**.
- Deployment authorized: **No**.
- Tester access authorized: **No**.
- Paid-service activation authorized: **No**.
- Production credentials authorized: **No**.

PPIA-09 is a governed preimplementation design package only.