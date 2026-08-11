# PPIA-02 Completion Candidate

**Work item:** PPIA-02 — Creature & NPC Experience  
**State:** PR #217 MERGED — REQUIRED R1 RECOVERY AMENDMENT PENDING EXACT-HEAD VALIDATION/MERGE  
**Original completion PR:** #217  
**Original completion merge:** `f6568e77de2790e9012a95942435c8d88b2e1dd5`  
**Amendment branch:** `governance/ppia-02-r1-completion-amendment`

## Completion-gate requirement

PPIA-02 delivers an implementation-ready Creature/NPC experience packet with permission-safe presentation, authoring, encounter, variant, relationship, asset, transformation, accessibility, and source-grounded reference contracts.

PR #217 merged the full Creature/NPC design packet. Immediately before/around that closure, owner-supplied R1 evidence became available and materially improved the provenance boundary. This amendment is therefore required before the PPIA-02 continuity checkpoint advances to the next tranche.

## Source and authority package

The merged PPIA-02 packet includes:

- `PPIA-02_SOURCE_AND_DESIGN_INVENTORY.md`;
- 23 dedicated Creature PDFs + `Player Creatures.PDF` inventoried with SHA-256 provenance;
- representative source review for Creature Types, Havalaea Creatures, Dragons, and Player Creatures;
- explicit exclusion of the unsuccessful 487-object semantic-parse database from Creature/NPC content authority;
- respect for the later 8E-009 CSV-first registry without falsely treating it as a dedicated Creature catalog.

## Recovered 8E-008G-R1 source accountability

Owner-supplied `This.zip` recovered the substantive 8E-008G-R1 closure outputs and was canonically recorded in merge `d271d1e7ec453cd153a7bf5768b3df837ba677a9`.

Recovered R1 result:

- 101 / 101 acceptance checks PASS;
- 7,144 / 7,144 structural candidates accounted;
- 2,766 formerly unbound candidates closed;
- 0 unbound source sections remain;
- 158,189 authoritative records provenance-accounted;
- 1,671 candidates formally deferred rather than silently excluded.

R1 passes source accountability, not Public Canon completeness. Formal deferral is neither canonical promotion nor exclusion.

The recovered R1 register contains **93 formally deferred creature candidates**. PPIA-02 retains their exact identity/source/page/heading subset in `PPIA-02_R1_DEFERRED_CREATURE_CANDIDATES.csv` and governs their experience in `PPIA-02_R1_PROVENANCE_AND_DEFERRED_CREATURE_ADDENDUM_v0.1.0.json`.

A formally deferred creature candidate may be inspected as authorized source-recovery/provenance evidence but:

- is not a canonical Creature/NPC Definition;
- is excluded from ordinary canonical Library results unless a source-recovery/deferred filter is explicitly requested and authorized;
- cannot be quick-added or launched as a Scene/Encounter participant without a governed usable Definition or Campaign-local authored object;
- cannot receive an invented stat block, CR, ecology, relationships, or mechanics merely to make it usable;
- cannot be auto-bound to a similarly named existing Creature/NPC;
- remains a later convert/bind/exclude/supersede/waive decision with provenance.

**This historical recovery request is now resolved.** No further upload of `Aaac (1).zip` or the historically named R1 wrapper is required to complete PPIA-02.

## Experience architecture

The merged packet retains:

- 7 object/experience layers;
- 8 presentation profiles;
- 10 experience contexts;
- 13 Inspector section families;
- permission-before-serialization projections;
- explicit no-A2/no-runtime-mutation boundaries.

## Workflow package

`PPIA-02_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json` defines ten governed workflows:

1. Library / Inspector reference
2. GM NPC & Creature Manager authoring
3. Scene quick-add / placement
4. Encounter preparation / balance analysis
5. Live runtime
6. Investigation / social NPC use
7. Exploration / bestiary / discovery
8. Variant / template / stage comparison
9. Summon / minion / spawn
10. Playable creature conversion

The R1 addendum does not create an eleventh mutation workflow. Source-recovery inspection remains non-authoritative; any later conversion/binding action must use a separate governed owning workflow and preserve provenance.

## Integrated specification

`PPIA-02_CREATURE_NPC_EXPERIENCE_SPEC_v1.0.0.md` remains the primary integrated specification. The R1 addendum supplements its source, Inspector, provenance, and completion sections with the explicit `formally_deferred_source_candidate` state and no-silent-promotion rule.

## Reference cases

The merged packet retains 13 governed reference cases:

- 7 source-grounded cases;
- 6 explicitly noncanonical synthetic QA cases.

The 93 recovered R1 creature candidates are **not** converted into reference-case lore, synthetic creatures, or canonical Definitions. They remain a provenance/source-recovery dataset.

## Acceptance and traceability

The existing 36 requirements in 16 categories remain unchanged. The R1 addendum maps formal-deferral behavior to existing requirements:

- `PPIA02-REQ-003` — name similarity cannot create identity/merge;
- `PPIA02-REQ-007` — privacy filtering occurs before serialization and derived counts;
- `PPIA02-REQ-034` — authorized provenance views distinguish source/content states;
- `PPIA02-REQ-035` — incomplete/deferred evidence remains inspectable without invented replacement fields.

The completion validator additionally verifies:

- canonical R1 merge/hash and PASS result;
- the 93-candidate subset's SHA-256, row count, unique IDs, and source distribution;
- no-silent-promotion behavior;
- source-recovery privacy/authoring/Scene/Encounter boundaries;
- the fact that the earlier optional owner upload request has been resolved.

## Key non-negotiable outcomes

- Hidden Creature/NPC existence and derived cardinality never reach unauthorized projections.
- Definition, placement, and live-instance identities remain separate.
- Presentation profile never grants authority or creates a canonical type.
- Campaign-local authoring never becomes source truth silently.
- Encounter balance output remains advisory.
- Runtime state never writes back to reusable Definitions.
- Type modifiers and source variants never auto-merge by name.
- Runtime transformations use the owning Ability/Action/Session workflow.
- Summons preserve source/placement/instance/controller/master distinctions.
- Playable conversion produces Character/species draft/provenance, not identity equivalence.
- Incomplete/conflicted sources remain usable without invented replacement facts.
- Formally deferred R1 creature candidates remain source-recovery/provenance evidence until a separate governed disposition creates/binds/excludes/supersedes/waives them.
- PPIA-02 does not activate A2, implement runtime behavior, release, deploy, or promote unsupported source content.

## Closure condition

PR #217 is already merged. PPIA-02 continuity may advance to PPIA-03 only after this R1 amendment passes all applicable exact-head gates and is merged canonically, followed by a completion checkpoint/readback that cites both the original PPIA-02 merge and the R1 amendment merge.
