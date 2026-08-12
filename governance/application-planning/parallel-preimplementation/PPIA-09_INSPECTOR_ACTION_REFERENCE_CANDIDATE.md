# PPIA-09 — Investigation / Mystery Inspector, Action & Reference Candidate

**Work item:** PPIA-09 — Investigation & Mystery Authoring Kit  
**Version:** 0.1.0  
**State:** INSPECTOR / ACTION / REFERENCE CANDIDATE — NOT PPIA-09 COMPLETE  
**Foundation merge:** `511b7b3edc0b88ff8ea5683fd093d2853b50ccf1`

## 1. Purpose

Convert the verified PPIA-09 source/design foundation into deterministic inspector, mutation, diagnostic and reference-case contracts without reopening source authority or claiming final PPIA-09 completion.

This milestone preserves the source-backed Investigation model while supplying implementation-ready product semantics where the retained sources explicitly left gaps.

## 2. Preserved source and design authority

This candidate retains:

- 3 directly relevant retained PDFs / 53 visually reviewed pages;
- the direct `V05_Investigation.md` interface-design authority;
- verified MV-IA-F011 Investigation and Clue Board semantics;
- all 10 F011 core record families;
- all 15 F011 typed connection predicates;
- all 24 F011 deterministic fixtures;
- 16 PPIA-09 semantic layers;
- 12 PPIA-09 presentation profiles;
- 12 PPIA-09 domain handoffs;
- source guidance that important information should appear in at least two places to reduce stalls;
- source support for dynamic / extra clues, red herrings, false evidence, unreliable witnesses, corrupted information, reconstructed timelines and separate Player / GM dossier projections.

The Vanishing of Dr. Wen is retained only as a source-backed reference-mystery identity and projection example. This milestone does **not** invent unprovided Dr. Wen clue, culprit, motive, timeline or solution content.

## 3. Inspector projection contract

The matrix defines exactly **16 projection groups**, one for each verified semantic layer:

1. Investigation case definition;
2. objective truth and GM solution;
3. Clue Definition and source template;
4. Campaign Clue discovery and analysis;
5. Observation / Claim / statement;
6. Evidence and owning-domain reference;
7. witness/source reliability and authenticity;
8. Hypothesis / theory / deduction;
9. typed semantic Connection;
10. Question / lead / next step;
11. timeline / temporal order / alibi;
12. contradiction / false lead / uncertainty;
13. discovery condition / reveal / audience;
14. solvability / redundancy / progression / stall recovery;
15. conclusion / resolution / outcome / history;
16. permission / provenance / version / recovery / accessibility.

Permission filtering precedes protected reference resolution, counts, search, diagnostics and derived views. A visual graph is never the sole authoritative representation.

## 4. Governed action surface

The matrix defines exactly **30 actions**:

- **8 reads** for Investigation, GM truth, clue/evidence, timeline/alibi, hypotheses/connections, solvability diagnostics, reveal preview and history/recovery/accessibility;
- **22 authoritative mutations** for case authoring, truth/solution, clue templates and Campaign Clues, discovery/analysis, observations, claims, evidence references, annotations, hypotheses, connections, questions/leads, timeline/alibi records, contradiction review, false-lead/corruption metadata, revelation dependencies, stall-recovery clues, reveal transitions, conclusions and explicit acceptance of generated proposals.

Every authoritative mutation requires `expected_version` plus `operation_id`. Ambiguous outcomes require operation-status/current-version lookup before retry.

## 5. Truth, belief and annotation semantics

PPIA-09 locks these separations:

- objective truth ≠ GM solution/conclusion;
- visible ≠ true;
- Observation ≠ Claim ≠ Evidence;
- witness belief ≠ witness reliability ≠ statement truth;
- source authenticity ≠ content truth;
- Hypothesis ≠ fact;
- contradiction ≠ automatic falsehood;
- confidence ≠ objective truth probability;
- relevance ≠ truth;
- graph position ≠ semantic relationship.

The new normalized annotation dimensions are **governed PPIA-09 design, not recovered source canon**:

- confidence;
- relevance;
- authenticity;
- source reliability.

Each annotation is attributable and stores its basis, author, visibility, review state and version. PPIA-09 defines no mandatory universal numeric probability scale. Unknown and unset remain valid.

## 6. Timeline and alibi semantics

The timeline/alibi contract supports exact, bounded-window, relative-before, relative-after and unknown temporal forms.

Alibi review states are governed design used only for comparison and review. Temporal incompatibility may surface a contradiction, but the system never chooses a truth winner automatically.

PPIA-12 retains World/Setting chronology ownership. PPIA-09 may reference chronology and attributable Events/Claims, but Player-visible chronology remains permission-filtered separately from hidden GM or Setting truth.

## 7. Contradiction semantics

Governed contradiction classifications:

- temporal;
- location;
- identity;
- causal;
- statement;
- source-authenticity;
- evidence-state;
- custom.

Governed review states:

- unreviewed;
- acknowledged;
- under-review;
- explained;
- resolved-by-authorized-conclusion;
- superseded.

A resolved contradiction preserves both prior inputs and the authorized explanation/conclusion reference. It does not rewrite source history.

## 8. Revelation dependency and solvability diagnostics

The source does not define a universal deterministic solvability algorithm, so the following is explicitly **governed PPIA-09 authoring design**.

Authors may label revelations `required`, `optional` or `bonus` and connect them using explicit dependency kinds. A read-only diagnostic traverses only author-declared routes and dependencies.

For required revelations it reports:

- reachable required revelations;
- unreachable required revelations;
- explicit route counts;
- single-point warnings;
- circular dependency warnings;
- authorization-blocked route warnings;
- stall-recovery coverage.

The diagnostic never resolves the Investigation, changes reveal state, invents routes or decides Player success.

## 9. Source-grounded redundancy guidance

The Investigation source explicitly says each important piece of information should appear in **at least two places** to reduce stalls.

PPIA-09 implements this as a deterministic authoring warning:

- authors may mark a revelation `important_for_progression`;
- explicit distinct routes are counted after `duplicate-of` collapse;
- fewer than two distinct routes produces a warning;
- two or more routes satisfies that warning condition;
- this does **not** create a universal clue count for the mystery as a whole;
- it does **not** guarantee narrative quality or Player success.

## 10. False-lead and corrupted-evidence diagnostics

The source directly permits red herrings, false evidence, unreliable witnesses and corrupted information.

PPIA-09 therefore supports attributable misleading-material states and read-only diagnostics that can report:

- no authored correction path;
- misleading material is the only explicit route to a required revelation;
- all required routes are blocked;
- a correction/recovery route exists;
- source state remains unresolved.

These are authoring findings, not universal fairness verdicts. No universal red-herring fairness threshold is introduced.

## 11. Stall recovery

Dynamic / extra clues are source-backed. A stall-recovery route must retain:

- recovery identity;
- trigger or delivery reason;
- author;
- source;
- audience;
- delivery mode;
- Event policy;
- version.

Adaptive recovery never silently rewrites prior clues or objective truth and never bypasses permissions or owning Action/Ability/Campaign/Scene/Setting rules.

## 12. Reference corpus

The companion corpus defines exactly **36 deterministic cases**.

Cases `PPIA09-RC-001` through `PPIA09-RC-024` preserve every existing F011 deterministic fixture one-to-one.

Cases `PPIA09-RC-025` through `PPIA09-RC-036` add the deeper PPIA-09 authoring coverage:

25. Dr. Wen dossier projection integrity;
26. important revelation single-route warning;
27. important revelation with two independent routes;
28. circular revelation dependency;
29. false lead with authored recovery route;
30. misleading material as sole required route;
31. timeline/alibi contradiction review;
32. source-quality dimension separation;
33. Research success cannot bypass reveal permission;
34. hidden World/Setting timeline fact does not leak;
35. dynamic extra clue retains provenance;
36. cross-case correlation creates a lead, not truth.

All 30 actions and all 16 projection groups are exercised by the reference corpus.

## 13. Ownership and privacy boundaries

PPIA-09 continues to preserve:

- PPIA-08 Campaign / Scene / Session ownership;
- PPIA-02 Creature / NPC identity;
- PPIA-03 Item / Asset ownership;
- PPIA-04 Vehicle ownership;
- PPIA-12 World / Setting truth and chronology;
- MV-IA-F009 Relationship facts/history;
- MV-IA-F010 social statements, rumors and secrets;
- PPIA-01 / later PPIA-06 Action and Ability resolution;
- MV-IA-F020 permission and hidden-information filtering;
- MV-IA-F021 expected-version/idempotent recovery;
- MV-IA-F022 accessibility and nonvisual parity.

Evidence, events, locations, people, vehicles and source objects remain references to their owning domains.

## 14. Accessibility

Every required Investigation operation has keyboard, touch, high-zoom/reflow and screen-reader-compatible operation. Typed connections have ordered textual predicates. Timeline and solvability diagnostics have table/list equivalents. Drag, graph position, color, hover and animation are never sole carriers of required meaning.

## 15. AI boundary

AI may receive only authorized context and may organize or propose material. It cannot reveal hidden truth, infer concealed existence, promote a hypothesis, decide a contradiction, resolve a case, create canonical clues or mutate authoritative state without an explicit authorized acceptance action and provenance.

## 16. Milestone boundary

This milestone does **not** complete PPIA-09.

It establishes the deterministic inspector/action/reference and solvability/uncertainty authoring contracts required for the next integrated Investigation/Mystery workflow milestone.

No application runtime, STAGE-A-A2 activation, release, deployment, tester access, paid service or production credential is authorized.
