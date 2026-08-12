# PPIA-09 — Investigation & Mystery Authoring Source and Design Inventory

**Work item:** PPIA-09 — Investigation & Mystery Authoring Kit  
**State:** FOUNDATION SOURCE REVIEW  
**Retained package:** `MV_Master_01_Core.zip`  
**Package SHA-256:** `c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec`  
**Transition anchor:** PPIA-08→PPIA-09 merge `a3545f2b77bd2bddade747ffc2ef58863eedff21`

## Review method

The retained package was inspected by filename/content search. The three directly relevant PDFs were text-extracted for search/reference and every page was rendered and visually reviewed. Structured CSVs were inspected by schema and bounded investigation/research/forensics/evidence keyword filtering; those filters locate relevant integration material but do **not** convert every matching row into Investigation-domain authority.

## Direct game-source authority — 3 PDFs / 53 pages

### 1. `Margot McBride's and Investigation.PDF`

- 40 pages.
- SHA-256: `ac76b433d2b0d007667eaf4701070aae738dd20262b9d9c30d13a09a3a888760`.
- Direct authority for investigation gameplay and mystery construction.
- Establishes clue discovery, clue analysis, hypothesis formation and resolution.
- Establishes red herrings, false evidence, interconnected cases, interdimensional investigation, forensic tools and protocols.
- Establishes archives/research, clue correlation, historical records, advanced forensics, recorded interviews, corrupted data and paradox risk.
- Contains a GM mystery-building method with core questions, **surface / hidden / revealed** layers, scenes, NPC encounters, challenges and revelations.
- States that each important piece of information should appear in at least two places as redundancy against stalls.
- Supports dynamic/extra clues, clue advancement, stall recovery and adaptive clue delivery.
- Contains mystery-generator components: core event, culprit, motive, twist, setting, initial clues, complications, resolution and random events.
- Contains Margot McBride Dossier formats separating Player materials from a GM solution/adventure guide, including case summary, evidence/clues, witness statements, leads, key locations, NPC profiles, clue breakdown, timeline/twists and solutions.
- Contains an example dossier, **The Vanishing of Dr. Wen**, and investigation ability/progression material.

### 2. `Knowledge 2-24-25.PDF`

- 11 pages.
- SHA-256: `f3df38da25d46e03724d0161663bb81c805411f62df7886337e95c26594a20a6`.
- Supporting game-rule authority for research/problem-solving and knowledge applicability.
- Establishes five Knowledge tiers, similarity/substitution guidance, research/problem-solving, restricted/secret knowledge access, deep insight, task bonuses and assistance.
- Does **not** define Investigation truth, clue provenance, mystery solvability or reveal semantics; those remain Investigation/permission-domain concerns.

### 3. `Timeline revision.PDF`

- 2 pages.
- SHA-256: `929b3fcf928fd6ec423128ca0688061eaaff812605b5986380553adda3795ffc`.
- Supporting source example of canonical chronological information spanning world/setting events.
- Demonstrates that authored timeline facts may be reusable Setting/World truth.
- Does **not** define an Investigation-specific alibi/timeline schema or automatically expose timeline truth to Players.

## Direct interface-design authority

### `V05_Investigation.md`

Internal Alpha Screen Design Volume 5 defines:

- Investigation Dashboard;
- Clue Board;
- Evidence Inspector;
- Timeline;
- Witness & NPC Profiles;
- Hypothesis Builder;
- GM Investigation Control.

It explicitly requires hidden clues to remain hidden until revealed, connection provenance, testimony contradictions/reliability, player theory construction without changing canonical truth, GM red-herring/reveal control and accessible alternatives to graph-only interaction.

## Verified Internal Alpha contract — MV-IA-F011

`MV-IA-F011 Investigation and Clue Board` is the verified implementation-ready starting contract, not the full PPIA-09 completion claim.

Its core records are:

1. Investigation;
2. Clue Definition;
3. Campaign Clue;
4. Observation;
5. Claim;
6. Evidence Item;
7. Hypothesis;
8. Connection;
9. Question;
10. Conclusion.

Its verified connection vocabulary contains 15 predicates: `supports`, `contradicts`, `explains`, `caused-by`, `leads-to`, `same-source`, `same-subject`, `temporal-before`, `temporal-after`, `located-at`, `owned-by`, `witnessed-by`, `derived-from`, `duplicate-of`, `custom`.

Its companion matrix contains **24 deterministic fixtures**. Critical invariants include:

- Player-visible clue is not objective truth.
- Player deductions/hypotheses are not auto-promoted to fact.
- Speaker belief, reliability and truth remain distinct.
- False leads may mislead without changing objective truth.
- Evidence references owning-domain objects instead of copying ownership.
- Hidden clues, hidden connections and concealed source facts are filtered before derivative surfaces.
- Semantic links remain authoritative even if spatial graph layout changes.
- Duplicate delivery/retry is idempotent.
- Graph meaning has ordered textual/nonvisual equivalents.
- GM resolution creates an attributable conclusion while retaining Player hypothesis history.

`MV-IA-F011_SOURCE_COVERAGE_AND_PROVENANCE.json` explicitly limits F011 to bounded canonical design synthesis and does not claim exhaustive extraction of every historical investigation rule or adventure-specific clue. PPIA-09 therefore performs the deeper source-grounded authoring pass rather than treating F011 as exhaustive.

## Structured support corpus — 4 CSVs / 4,936 rows

These structured sources provide integration evidence and source-backed content references. Keyword hits are discovery aids, not blanket authority claims.

### `Abilities_Core.csv`

- 1,256 rows.
- SHA-256: `0a65391edd6659a7f076760cff6f1368b606904fb746655182c76a89c8bdb6f7`.
- 142 bounded investigation/research/forensics/evidence keyword-hit rows.
- Five explicit Investigation/Knowledge category trees contain **109 records** total:
  - Research and Scholarly Activity Ability/Perk Tree — 21;
  - Investigator Ability Tree — 25;
  - Treasure Hunter Tree — 21;
  - Confronter of Horrors Tree — 21;
  - Hunter Tree — 21.
- Supports action/skill/progression integration but does not make ability records the Investigation authoring schema.

### `Prestige_Env_Abilities.csv`

- 1,018 rows.
- SHA-256: `052897f355daa1719d7e44ad04642f3cdb5ccff208b2302f24c81711f8a205d4`.
- 69 bounded keyword-hit rows.
- Supports specialized investigation/deduction/research capability references and environment-context interactions.

### `Items.csv`

- 761 rows.
- SHA-256: `f67a02a7d36e39f4837dbca4c2b75e3773fe6a0a8de58c278b2703c2b45d5cee`.
- 15 bounded keyword-hit rows.
- Supports Item/Asset evidence references and forensic/investigative tools while PPIA-03 retains Item ownership.

### `Hazards_Traps.csv`

- 1,901 rows.
- SHA-256: `391854834b50bdf175fe0bdd949280adbff67918889daae662fb40c40c418417`.
- 1,344 broad detection/investigation/research/evidence keyword-hit rows, primarily because the catalog systematically carries detection methods and psychological/misleading-clue contexts.
- Supports Scene discovery conditions, environmental observations and misleading/perception-sensitive evidence without transferring Hazard ownership to PPIA-09.

## Canonical repository support contracts

PPIA-09 inherits boundaries rather than duplicating them:

- **PPIA-08** — Campaign/Scene/Session, map/location placement, launch snapshots, live amendments and Campaign-local history.
- **MV-IA-F002** — governed object browse/inspect/search/provenance/relationship traversal.
- **PPIA-02** — Creature/NPC and witness identity/state.
- **PPIA-03** — Item/Asset evidence identity and instance ownership.
- **PPIA-04** — Vehicle evidence/reference identity where applicable.
- **PPIA-12** — reusable World/Setting definitions and canonical Setting timelines.
- **MV-IA-F009** — directional relationship facts/annotations and relationship history.
- **MV-IA-F010** — social statements, rumors, secrets and reveal interactions.
- **MV-IA-F020** — permission and hidden-information filtering.
- **MV-IA-F021** — expected-version/idempotent recovery and reconnect.
- **MV-IA-F022 / accessibility standards** — keyboard, touch, high-zoom/reflow, screen-reader and nonvisual equivalence.
- **PPIA-01 / later PPIA-06 action-resolution boundary** — source-backed Investigation/Research/Knowledge rolls, DCs, resource effects and ability mechanics remain rule-domain behavior rather than mystery-authoring ownership.

## Source-backed authoring findings

The combined sources directly support the following design facts:

1. An Investigation has a hidden or GM-controlled truth/solution that must remain distinct from Player theories.
2. Clues may be physical objects, testimony, environmental observations, hidden messages or digital information.
3. Clues have discovery and analysis stages; analysis can reveal significance, inconsistency or additional clues.
4. Hypotheses are Player/character theories, can be wrong and must not mutate canonical truth merely by being asserted.
5. Red herrings, false evidence, unreliable NPCs and corrupted information are legitimate mystery elements.
6. Witness statements, contradictions and reliability are first-class investigation concerns.
7. Temporal reasoning matters: Investigation UI includes Timeline, source mystery design uses reconstructed timelines, and typed temporal links already exist in F011.
8. Important information should have redundant routes; the source explicitly recommends at least two placements for important information to prevent stalls.
9. Extra/dynamic clues may be introduced when progress stalls, but their delivery conditions and authority must remain attributable.
10. Mystery authoring has recognizable layers: surface clues, hidden connections and revealed/core truth.
11. Mystery construction commonly includes core event, responsible actor/culprit, motive, twist, setting, clues, NPCs, locations, obstacles/complications and possible resolutions.
12. Player-facing case material and GM truth/solution material are separate projections of the same governed case.
13. Research, archives and Knowledge can discover/correlate information, but skill success does not automatically define truth visibility outside the owning reveal/permission rules.
14. Cross-case correlation and historical records are supported.
15. Provenance is required for clues/connections/evidence and remains visible according to authorization.

## Explicit source/design gaps retained for PPIA-09

The sources do **not** provide a single complete deterministic authoring schema for:

- objective-truth statement identity and truth-version semantics;
- normalized confidence, relevance, authenticity and source-reliability dimensions across all clue types;
- a deterministic mystery-solvability algorithm;
- machine-checkable clue redundancy/reachability rules;
- formal contradiction classification and contradiction-resolution workflow;
- exact rules for when a false lead becomes unfair/unsolvable;
- exact authoring representation of required versus optional revelations;
- a universal threshold for how many clues are enough;
- a universal success/failure consequence formula;
- automatic conversion of every Investigation/Knowledge ability into clue truth;
- automatic conversion of world timeline facts into Player-known case facts.

Those gaps remain unknown until PPIA-09 defines **governed design contracts**. Any such contracts must be labeled as Multiversal authoring design rather than recovered source canon.

## Foundation direction

PPIA-09 may normalize the verified/source-backed concepts into implementation-ready authoring primitives, but it must preserve these non-negotiable boundaries:

- truth ≠ belief ≠ claim ≠ hypothesis;
- visible ≠ true;
- hidden ≠ nonexistent;
- evidence object reference ≠ ownership copy;
- contradiction ≠ automatic falsehood;
- confidence ≠ objective truth probability unless an owning rule explicitly says so;
- graph position ≠ semantic relationship;
- research success ≠ permission bypass;
- source redundancy guidance ≠ invented universal clue count;
- GM conclusion ≠ deletion of Player history;
- AI organization/deduction remains proposal-only;
- unknown source gaps remain explicit rather than silently filled.