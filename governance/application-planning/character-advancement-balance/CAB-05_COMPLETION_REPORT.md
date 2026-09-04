# CAB-05 — Five-Tier Model Completion Report

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-05  
**State:** `completed_verified` analysis; owner policy answers pending  
**Owner/final authority:** John Brandon Turner  

## Completed

CAB-05 defined the shared five-tier model as developmental depth rather than a universal power/price score and separated numeric tier identity, source-local labels, tier access state, progression scope, node prerequisites, and special progression modes.

Durable outputs:

- `CAB-05_FIVE_TIER_MODEL.md` — human-readable tier semantics and access model;
- `CAB-05_TIER_SEMANTICS_v0.1.0.json` — machine-readable tier model and corpus observations;
- `CAB-05_OWNER_QUESTIONNAIRE.md` — four owner policy gates.

## Findings

### 1. Five tiers are strongly supported as a shared structural vocabulary

The bounded 4,816-record Ability corpus contains 3,917 records with numeric Tier 1–5 values. In the bounded tree grouping, 158 of 179 tiered groups contain all five tiers.

This supports preserving five numeric tiers as a shared progression structure.

### 2. Source labels do not supply one canonical naming scheme

Recovered sources use overlapping names such as Foundation, Basic, Advanced, Specialized, Mastery, Elite, Legendary, Apex, and domain-specific terms at different tier numbers. Numeric Tier 1–5 is the stable cross-tree identity; descriptive labels must remain semantic aids and preserve source-local wording.

### 3. Tier is developmental depth, not a universal power score

Direct Ability XP medians rise from Tier 1 through Tier 5, but observed ranges overlap substantially. Tier-5 direct costs range from 200 to 40,000 XP in the bounded numeric set, and nineteen Tier-5 records cost less than the highest observed Tier-1 direct price.

Tier therefore informs depth but cannot independently determine cost, encounter power, rarity, damage, or balance.

### 4. Tier access remains distinct from node cost

CAB-04 already separated tier/depth access from individual node prerequisites and affordability. CAB-05 represents explicit per-scope tier-access state and supports paid, granted, temporary, prerequisite-only, sequential, milestone, innate, and other governed access modes.

### 5. A separate higher-tier cost remains a viable specialization control

Recovered sources strongly attest one-time tier unlock costs but do not use them universally. CAB recommends a normal one-time T2–T5 tier-access XP purchase for ordinary purchasable Ability progressions while allowing explicitly different modes for special progressions. CAB-06 must calibrate any accepted default rather than inheriting legacy schedules unchanged.

### 6. Short trees should not be padded with invented filler

Twenty-one bounded tiered groups are partial/sparse. CAB distinguishes intentional early caps from unexplained internal gaps. The recommended well-formed model permits early caps, expects contiguous tiers through the cap, flags unexplained gaps, and prohibits synthetic filler.

### 7. Tier 5 should mean apex depth inside its own progression

The source corpus contains narrow Tier-5 techniques as well as transformative, legendary, or extremely expensive Tier-5 capabilities. A universal world-shaping Tier-5 floor would make unlike domains artificially identical. CAB recommends apex/capstone depth relative to the owning progression, with actual effect burden calibrated separately.

## Architecture established without owner gate

CAB-05 establishes the following structural requirements:

1. tier identity is numeric Tier 1–5;
2. tier represents relative developmental depth within an explicit progression scope;
3. source-local tier labels remain provenance/display data;
4. tier does not substitute for eligibility, prerequisites, learning, exclusions, or approval;
5. tier access and individual node cost are separately representable;
6. tier scope may be a tree or explicit branch/path and must use stable identity;
7. unlocking one independent scope does not silently unlock another;
8. free-product first-two-tier access remains entitlement, not game-balance semantics;
9. CAB does not synthesize missing Ability records to complete a tier structure;
10. actual power/balance remains multidimensional and is not collapsed into tier.

## Recommendations requiring owner answer

1. Use neutral shared descriptors: **Foundation / Developed / Advanced / Expert / Apex** while keeping numeric tiers authoritative.
2. Ordinary purchasable Ability progressions normally use a separate one-time T2–T5 tier-access XP cost, with special progression access modes explicitly allowed.
3. Permit intentional early caps; expect contiguous tiers through the cap; treat unexplained internal gaps as content-quality warnings; never invent filler.
4. Define Tier 5 as apex/capstone depth within the owning progression, not a universal legendary/world-shaping power floor.

## Owner questionnaire

`CAB-05_OWNER_QUESTIONNAIRE.md` records four questions:

- CAB-Q05-01 — shared semantic descriptors: **A recommended**;
- CAB-Q05-02 — default higher-tier access cost: **A recommended**;
- CAB-Q05-03 — short/sparse tree policy: **A recommended**;
- CAB-Q05-04 — cross-tree Tier-5 meaning: **A recommended**.

Unanswered questions remain unresolved and do not silently default.

## Forward routing

- owner answers -> record before CAB-06 execution;
- tier-access, tree-opening, Ability, HP, attribute and other price calibration -> CAB-06;
- action economy -> CAB-07;
- stacking/synergy -> CAB-08;
- acquisition/eligibility exceptions -> CAB-09;
- attribute/skill valuation and learning formula -> CAB-10;
- corpus and tree completeness/structure audit -> CAB-11/12;
- outlier review -> CAB-13;
- equal-XP and multidimensional balance -> CAB-14/15;
- pacing/awards -> CAB-16/17;
- veteran-depth stress -> CAB-18.

## Completion statement

CAB-05's bounded analysis is complete when these artifacts are merged, the CAB backlog marks CAB-05 `completed_verified`, and CAB-06 is selected but held pending the four owner policy answers. No application implementation authority is created.

## Exact successor

**CAB-06 — XP Cost Calibration Framework** — selected after CAB-05 closeout, with execution held until CAB-05 owner answers are recorded or explicitly deferred.
