# PPIA-09 — Investigation & Mystery Authoring Foundation Candidate

**Work item:** PPIA-09 — Investigation & Mystery Authoring Kit  
**State:** FOUNDATION CANDIDATE — NOT PPIA-09 COMPLETE  
**Transition merge:** `a3545f2b77bd2bddade747ffc2ef58863eedff21`

## Foundation result

The Investigation/Mystery authoring domain now has a bounded, source-grounded foundation instead of relying only on the earlier Internal Alpha Clue Board design.

The retained package review covers **3 directly relevant PDFs / 53 pages**, visually reviewed in full, plus the direct Investigation screen-design source and the verified MV-IA-F011 package. Four structured CSV support sources contain **4,936 rows** total; bounded keyword filtering locates 1,570 investigation/research/forensics/evidence-related rows, while the core ability catalog contains **109 records across five explicit Investigation/Knowledge trees**.

This does not mean all 4,936 structured rows are Investigation records. The structured sources are supporting integration evidence and preserve their owning domains.

## Direct source findings locked by the foundation

The source material explicitly supports:

- clue discovery and clue analysis as distinct investigation stages;
- objects, testimony, environmental observations, hidden messages and digital information as clue forms;
- hypothesis formation without any requirement that a theory become truth merely because a Player asserts it;
- red herrings, false evidence, unreliable NPCs and corrupted data;
- witness statements, contradictions and reliability;
- research/archive correlation, historical records and forensic tools;
- surface / hidden / revealed mystery layers;
- reconstructed timelines and temporal reasoning;
- important-information redundancy, including direct guidance that important information should appear in at least two places;
- dynamic/extra clues as a way to recover stalled progress;
- mystery construction around a core event, culprit/responsible actor, motive, twist, setting, clues, NPCs, locations, complications and resolution;
- separate Player-facing dossier material and GM truth/solution material;
- source-backed reference mystery material including **The Vanishing of Dr. Wen**;
- research and Knowledge rules that can help find/interpret/correlate information without defining Investigation truth or permission semantics by themselves.

## Verified F011 foundation retained

PPIA-09 preserves all ten MV-IA-F011 record families:

`Investigation`, `ClueDefinition`, `CampaignClue`, `Observation`, `Claim`, `EvidenceItem`, `Hypothesis`, `Connection`, `Question`, `Conclusion`.

It also preserves the 15 verified semantic connection types and all **24 F011 deterministic fixtures**.

Critical behavior remains unchanged:

- visible clue ≠ objective truth;
- Player deduction/hypothesis ≠ fact;
- witness belief ≠ statement truth ≠ witness reliability;
- false lead may mislead without changing objective truth;
- hidden clue/edge/source information cannot leak through derivative surfaces;
- evidence references owning-domain records rather than copying ownership;
- graph position is presentation state, not semantic authority;
- duplicate delivery/retry is idempotent;
- semantic relationships have nonvisual equivalents;
- GM conclusion preserves attributable history rather than deleting prior Player theories.

## PPIA-09 semantic taxonomy

The foundation defines **16 semantic layers**:

1. Investigation case definition.
2. Objective truth and GM solution.
3. Clue definition and source template.
4. Campaign clue discovery and analysis state.
5. Observation, claim and statement.
6. Evidence item and owning-domain reference.
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

The taxonomy intentionally separates truth, belief, claim, observation, evidence, hypothesis, visibility and knowledge state instead of reducing them to one generic “clue” record.

## Presentation profiles

The foundation defines **12 presentation profiles**:

- investigation-dashboard;
- clue-board-and-semantic-connection-view;
- clue-and-campaign-clue-inspector;
- evidence-inspector-and-source-provenance;
- timeline-alibi-and-event-view;
- witness-source-and-claim-profile;
- hypothesis-theory-builder;
- gm-truth-solution-and-reveal-control;
- lead-question-and-research-tracker;
- solvability-redundancy-and-progress-audit;
- reference-mystery-and-dossier-authoring-workbench;
- history-provenance-recovery-and-accessible-linear-view.

## Ownership and handoffs

The foundation defines **12 domain handoffs** covering:

1. MV-IA-F011 Investigation/Clue Board starting semantics;
2. PPIA-08 Campaign/Scene/Session;
3. MV-IA-F002 universal object/provenance;
4. PPIA-02 Creature/NPC/witness identity;
5. PPIA-03 Item/Asset evidence ownership;
6. PPIA-04 Vehicle references;
7. PPIA-12 World/Setting and chronology;
8. F009/F010 relationship/social statements, rumors and secrets;
9. PPIA-01 / later PPIA-06 rules and action resolution;
10. F020 permissions;
11. F021 recovery/idempotency;
12. F022/accessibility standards.

PPIA-09 owns Investigation/Mystery authoring composition and case-local investigation state. It does not absorb those owning domains.

## Explicit gaps — governed design required later

The source does not supply a complete deterministic implementation contract for:

- objective-truth statement identity/versioning;
- universal confidence/relevance/authenticity/source-reliability scales;
- deterministic solvability/reachability validation;
- machine-checkable clue redundancy rules;
- contradiction taxonomy and resolution workflow;
- red-herring fairness thresholds;
- required versus optional revelation schema;
- universal minimum clue counts;
- universal consequence/balance formulas.

Those gaps are now explicit rather than silently filled. Later PPIA-09 milestones may define implementation-ready **governed design** for them, but must not relabel those additions as recovered source canon.

## Source/design non-assumptions

This foundation does **not** assume:

- visible means true;
- hidden means nonexistent;
- claim means fact;
- contradiction automatically identifies the false side;
- confidence is objective truth probability;
- graph layout is semantic authority;
- a Research/Knowledge success bypasses permissions;
- the source redundancy recommendation creates a universal clue count;
- canonical world timeline facts are automatically Player-known;
- AI-generated theory or connection is authoritative;
- all historical adventure clues have been exhaustively extracted.

## Accessibility and privacy

All future graph/map/timeline/connection work must have ordered semantic text/list/table equivalents. Drag, hover, color, animation and spatial layout may enhance authoring but cannot be the only way to understand or operate the system.

Permission filtering must happen before hidden truth/clue/connection/source existence reaches counts, search, autocomplete, exports, diagnostics, notifications, realtime payloads or AI context.

## What remains before PPIA-09 can complete

This is only the source/design foundation. PPIA-09 still needs, at minimum:

- detailed authoring object and inspector/action contracts;
- deterministic truth/belief/uncertainty metadata rules;
- timeline/alibi and contradiction workflows;
- clue/revelation dependency and solvability/redundancy validation design;
- red-herring/false-evidence handling;
- GM/Player authoring/reveal workflows;
- multiple source-grounded/reference mystery fixtures;
- final acceptance/traceability material.

No application runtime, STAGE-A-A2, release, deployment, tester access, paid service or production credential is activated by this foundation.