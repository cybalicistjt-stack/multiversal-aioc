# CAB-12 — Ability-Tree Structural Audit

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-12

## 1. Purpose

Audit whether the bounded Ability corpus structurally supports CAB-05's five-tier developmental-depth model without forcing every source into identical tree size, prerequisite counts, or starting tier.

## 2. Tiered progression census

Using source dataset + Tree_ID as the grouping key and considering groups with at least one numeric Tier 1–5 member, the corpus contains **179 tiered progression groups**.

### Tier coverage

- 158 groups contain all five numeric tiers 1–5;
- 174 groups begin at Tier 1;
- 3 groups legitimately begin at Tier 3 and are Prestige progressions;
- 1 group begins at Tier 5 (`Traveler Ultimate Abilities`), an explicitly ultimate-only special progression;
- 1 group begins at Tier 2 (`Heavy Weapons Combat Ability Tree`) and requires provenance/content review rather than an invented Tier 1.

Caps:

- 163 groups reach Tier 5;
- 2 cap at Tier 4;
- 12 cap at Tier 3;
- 2 cap at Tier 1.

A short progression is therefore normal source reality and is not evidence that filler must be authored.

## 3. Internal gaps

Only one numeric-tier group has an unexplained internal gap between its observed start and cap:

- `TREE-SKL-029` — `Temporal & Reality Bending Science`: observed Tier 1 and Tier 3 members, no Tier 2 members in the bounded source.

CAB-12 marks this `structural_gap_review_required`. It does not create Tier-2 Abilities.

Prestige Tier-3 starts and the Tier-5 ultimate-only progression are not gaps because their declared scope begins above Tier 1.

## 4. Tree-size distribution

Across the 179 tiered groups:

- minimum numeric-tier member count: 3;
- median: 20;
- mean: about 21.9;
- maximum: 70;
- 22 groups contain 10 or fewer numeric-tier members;
- 61 contain 30 or more.

A universal prerequisite such as `buy N prior-tier Abilities` would affect small and large trees very differently. This independently supports the owner-approved CAB-04 decision against a universal 5/4/3/2 or two-from-prior-tier gate.

## 5. Structural progression contract

Every governed progression scope should be able to state:

- stable Tree/Progression ID;
- source-qualified identity/provenance;
- declared starting tier;
- declared cap tier;
- member Ability IDs;
- branches/subpaths and whether they share or separate tier access;
- explicit prerequisites/dependencies;
- any tree-local mastery-count requirement;
- acquisition mode;
- tier-access mode and costs/grants;
- exclusions/replacements;
- whether a gap is intentional, source-unknown, or repair-needed.

## 6. Contiguity rule

Default expectation:

> From a progression's declared starting tier through its declared cap, numeric tiers should be contiguous unless the owning source explicitly defines a sparse/ultimate/milestone structure.

An absent internal tier becomes a review state, not an automatic error and never a content-generation instruction.

## 7. Prestige and advanced-entry structures

Owner authority remains controlling:

- Prestige may declare Tier 3 as its actual start;
- Tiers 1–2 are not missing in that scope;
- entry requirements remain explicit and must be satisfied;
- T3 access cost applies under CAB-06 unless granted/substituted;
- the first Prestige Ability remains separate.

Other advanced-entry structures may exist only when source/governed authority explicitly establishes the higher starting tier. CAB does not infer advanced entry from missing rows alone.

## 8. Branches

Branches are progression topology, not automatic separate XP currencies.

A progression must explicitly say whether branch choice:

- shares the parent tier-access state;
- opens an independent branch-access state;
- is exclusive or compatible with sibling branches;
- requires a prior node/path;
- allows cross-branch prerequisites.

CAB-05's rule remains: independent progressions do not automatically unlock one another.

## 9. Dependency graph

Machine-ready prerequisites should prefer stable Ability/node IDs and explicit predicate types over prose-only counts. Tree-local counts remain legal where genuinely authored.

A dependency graph must reject/flag:

- self-dependency;
- cycles that make acquisition impossible;
- dependency on missing/unresolvable member IDs;
- prerequisite tiers above the dependent node without an explicit special rule;
- hidden universal filler-count assumptions.

Because much of the retained corpus stores prerequisites in prose rather than stable IDs, CAB-12 cannot responsibly certify the corpus cycle-free. Such rows are `dependency_graph_unresolved` until normalized.

## 10. Published counts and headers

Tree headers, collection rows, pricing listings, upgrades, and references coexist with numeric-tier member records. `Published_Ability_Count` therefore cannot be compared mechanically to the number of numeric-tier rows without first classifying those record roles. Apparent count mismatches are audit leads, not automatic corruption.

## 11. Adopted structural decisions

Under the standing owner delegation CAB-12 adopts:

1. declared start/cap are first-class progression properties;
2. contiguous tiers are expected only from declared start through declared cap;
3. Prestige T3 and explicit ultimate/special starts are valid advanced-entry structures;
4. unexplained internal gaps are review states and never trigger filler generation;
5. no universal prior-tier quantity gate;
6. branches explicitly declare shared vs independent access and compatibility;
7. prerequisite graphs should migrate toward stable IDs/predicates and unresolved prose stays unresolved rather than guessed.

No delegation guardrail triggered.

## 12. Successor

CAB-13 — High-Risk Ability Audit.