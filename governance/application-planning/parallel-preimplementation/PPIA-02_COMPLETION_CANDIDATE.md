# PPIA-02 Completion Candidate

**Work item:** PPIA-02 — Creature & NPC Experience  
**State:** **COMPLETED_VERIFIED**  
**Original design PR:** #217  
**Original design merge:** `f6568e77de2790e9012a95942435c8d88b2e1dd5`  
**Required completion amendment PR:** #219  
**Validated amendment head:** `1909a607bbb3ff57a959ae8cc47058ad2882a4e3`  
**Verified completion merge:** `f768345a44a662a5a1981f4cb35d218c926a5cb6`

## Completion-gate result

PPIA-02 now has the implementation-ready Creature/NPC experience packet required by its completion gate: permission-safe presentation, authoring, encounter, variant, relationship, asset, transformation, accessibility, provenance, and source-grounded/synthetic acceptance contracts.

The completion boundary is intentionally **two-part**. PR #217 merged the integrated design packet, but its final completion validator subsequently exposed that the merged reference set contained only 12 of the intended 13 cases. PPIA-02 therefore was not treated as complete from PR #217 alone. PR #219 restored the missing `PPIA02-RC-013` runtime transformation/privacy/reconnect case, integrated the recovered R1 provenance material, and passed the complete exact-head gate.

## Exact-head validation

Required amendment head `1909a607bbb3ff57a959ae8cc47058ad2882a4e3` passed all four applicable gates:

- Validate PPIA-02 Completion Contract — PASS, run `31506614994`;
- Validate PPIA-02 Foundation — PASS, run `31506614982`;
- Validate PPIA Program — PASS, run `31506614892`;
- Validate Operational AIOC Baseline — PASS, run `31506614861`.

PR #219 then squash-merged as `f768345a44a662a5a1981f4cb35d218c926a5cb6`.

## Source and authority package

The verified packet includes:

- `PPIA-02_SOURCE_AND_DESIGN_INVENTORY.md`;
- 23 dedicated Creature PDFs plus `Player Creatures.PDF` inventoried with SHA-256 provenance;
- representative source review for Creature Types, Havalaea Creatures, Dragons, and Player Creatures;
- explicit exclusion of the unsuccessful 487-object semantic-parse database from Creature/NPC content authority;
- source/provenance/inference boundaries inherited from PPIA-01.

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
- is excluded from ordinary canonical Library results unless an authorized source-recovery/deferred view is explicitly selected;
- cannot be quick-added or launched as a Scene/Encounter participant without a governed usable Definition or Campaign-local authored object;
- cannot receive an invented stat block, CR, ecology, relationships, or mechanics merely to make it usable;
- cannot be auto-bound to a similarly named existing Creature/NPC;
- remains a later convert/bind/exclude/supersede/waive decision with provenance.

**This historical recovery request is now resolved.** No further `Aaac (1).zip` upload is required for PPIA-02.

## Experience architecture

The completed packet includes:

- 7 object/experience layers;
- 8 presentation profiles;
- 10 experience contexts;
- 13 Inspector section/field groups;
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

The R1 addendum does not create an eleventh mutation workflow. Source-recovery inspection remains non-authoritative; any later conversion/binding action must use a separately governed owning workflow and preserve provenance.

## Reference cases

The verified packet contains **13 governed reference cases**:

- 7 source-grounded cases;
- 6 explicitly noncanonical synthetic QA cases.

`PPIA02-RC-013` specifically covers live alternate-form transformation, hidden-form privacy, authoritative runtime state, and reconnect/stale-cache recovery.

The 93 recovered R1 creature candidates are not converted into reference-case lore, synthetic creatures, or canonical Definitions. They remain provenance/source-recovery evidence.

## Acceptance and traceability

The packet contains **36 requirements across 16 categories**. The R1 addendum maps formal-deferral behavior to existing requirements:

- `PPIA02-REQ-003` — name similarity cannot create identity/merge;
- `PPIA02-REQ-007` — privacy filtering occurs before serialization and derived counts;
- `PPIA02-REQ-034` — authorized provenance views distinguish source/content states;
- `PPIA02-REQ-035` — incomplete/deferred evidence remains inspectable without invented replacement fields.

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

## Next governed work

PPIA-02 is completed_verified. The dependency-optimized sequence advances to **PPIA-03 — Items, Equipment & Inventory Experience** after the continuity/roadmap projection merges canonically.
