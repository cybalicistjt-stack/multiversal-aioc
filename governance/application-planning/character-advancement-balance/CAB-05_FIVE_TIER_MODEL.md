# CAB-05 — Five-Tier Model

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-05  
**State:** `completed_verified` analysis; owner policy gates recorded separately  
**Owner/final authority:** John Brandon Turner  

## 1. Purpose

Define what Multiversal's five Ability tiers mean, how tier/depth access relates to prerequisites and XP, how short or sparse trees are treated, and how the tier vocabulary remains useful without becoming a universal power score.

CAB-05 does **not** set final XP prices, action-economy balance, stacking rules, acquisition details, attribute valuation, award pacing, or corpus-wide repricing. Those belong to later CAB tranches.

## 2. Authority inherited from CAB-01 through CAB-04

CAB-05 inherits the following owner-approved constraints:

- Ability Points are deprecated.
- XP is the ordinary permanent Character-advancement currency.
- XP governs affordability; it does not substitute for eligibility or prerequisites.
- Five tiers remain the working model unless later evidence supports an explicit owner-approved change.
- Tier is not automatically identical to XP price.
- There is no universal prior-tier quantity gate.
- Tree/path-specific explicit mastery requirements remain legal when authored.
- Learning projects are conditional by default and may be explicitly modified by GM/Campaign policy.
- Intelligence/Wisdom faster learning attaches to applicable learning progress/readiness, not blanket XP multipliers or blanket purchase discounts.
- Free grants waive only the gates their source explicitly governs.
- Character breadth is not inherently imbalance; effective simultaneous capability is evaluated separately.

## 3. Source findings

### 3.1 Current framework supports tier/rank but does not define one universal semantic table

The current Character and Ability framework requires stable node IDs, explicit tier or rank, prerequisites, grants, exclusions, cost, source, and progression history. It does not define a universal numerical power score for tiers.

The approved product entitlement that limits free users to the first two tiers is an entitlement boundary only. It does not redefine the underlying game-balance meaning of Tier 1 or Tier 2.

### 3.2 The five-tier pattern is strongly represented

Bounded census of the five portable Ability CSV families used by CAB:

- total Ability records: **4,816**;
- records carrying a numeric Tier 1–5 value: **3,917**;
- tiered tree groups in the bounded grouping: **179**;
- groups containing all five tiers: **158**;
- groups that are partial, sparse, begin above Tier 1, or end before Tier 5: **21**.

This strongly supports retaining a shared five-band vocabulary while also proving that not every recovered tree is complete or uniformly structured.

### 3.3 Source tier names are inconsistent but follow a broad depth progression

Common or recurring source-language patterns include:

- Tier 1: Foundation, Foundational Skills, Basic, Fundamentals;
- Tier 2: Advanced, Specialized, Intermediate, Developed techniques;
- Tier 3: Advanced Mastery, Mastery, Signature or mature capability;
- Tier 4: Elite, Mastery, Supreme, extreme/hybrid capability;
- Tier 5: Legendary, Apex, Master, capstone capability.

The labels are not consistent enough to promote any recovered wording as a universal source fact. The numeric tier remains the stable cross-tree identifier; descriptive names are presentation/semantic aids.

### 3.4 XP tends to rise with tier, but tier is not an exact price or power value

Among records with both numeric tier and numeric direct Ability XP cost, the bounded corpus shows:

| Tier | Numeric records | Median direct XP | Observed range |
|---|---:|---:|---:|
| 1 | 272 | 250 | 20–3,000 |
| 2 | 264 | 700 | 40–7,500 |
| 3 | 270 | 1,500 | 60–15,000 |
| 4 | 226 | 3,000 | 110–25,000 |
| 5 | 215 | 5,000 | 200–40,000 |

The medians show a real depth/cost tendency, but the ranges overlap heavily. Nineteen bounded Tier-5 records cost less than the highest observed Tier-1 direct price. Some sources also use separate tier-entry costs while others, especially Species/Innate material, do not.

Therefore:

- tier may inform expected developmental depth;
- tier alone cannot determine final XP price;
- tier alone cannot determine encounter power;
- same-tier options in different trees are not automatically equivalent.

CAB-06 owns price calibration. CAB-07/08/15 own simultaneous-power and multidimensional balance consequences.

## 4. Tier as developmental depth

CAB-05 defines tier as **relative developmental depth within the owning progression scope**.

A tier answers:

> How deep into this particular progression has the Character developed, and what band of options may this progression expose?

It does **not** answer by itself:

- how many XP the option must cost;
- how much damage it deals;
- whether it is more useful than every lower-tier option in another tree;
- whether it is universally rare, legendary, or world-altering;
- whether the Character is eligible to acquire it;
- whether its action economy, stacking, resources, summons, defenses, or challenge-bypass effects are balanced.

### 4.1 Candidate cross-tree semantic descriptors

CAB recommends keeping the numeric tier authoritative and using the following neutral descriptors as a shared semantic aid:

| Tier | Candidate descriptor | Developmental meaning |
|---|---|---|
| **Tier 1** | **Foundation** | Entry capability, literacy, basic control, fundamental technique, or first reliable expression of the progression. |
| **Tier 2** | **Developed** | Expanded or specialized capability; reliable application beyond fundamentals; meaningful breadth or refinement. |
| **Tier 3** | **Advanced** | Mature/specialized competence, signature techniques, stronger combinations, or a meaningful increase in scope or control. |
| **Tier 4** | **Expert** | High-leverage, elite, transformative, or highly refined capability within the progression; significant encounter or problem-shaping potential. |
| **Tier 5** | **Apex** | Capstone or identity-defining depth for that progression; exceptional mastery/scope relative to that tree, without creating a universal cross-tree power floor. |

Source-local labels such as `Legendary`, `Mastery`, `Elite`, `Advanced`, `Foundational`, or domain-specific names remain valid display/provenance labels. They do not override the numeric tier or create separate tier systems.

The descriptor table remains an owner policy gate in `CAB-05_OWNER_QUESTIONNAIRE.md`.

## 5. Progression scope

Tier access applies to an explicit **progression scope**, not automatically to every option sharing a broad category name.

A progression scope may be:

- an entire Ability Tree;
- a declared branch/path inside a larger tree;
- another stable progression graph where the owning rule explicitly defines tiered depth.

Every tier-access record should identify its `tier_scope_id`.

Default recommendation:

- ordinary single-path trees use the tree as the scope;
- a branch/path may declare independent depth when branch specialization is mechanically meaningful;
- unlocking Tier 4 in one independent branch does not silently unlock Tier 4 in another independent branch merely because both sit under the same parent label.

CAB-12 will audit tree/branch structures against this model.

## 6. Tier-access state

CAB-04 already established tier/depth access as a gate distinct from node cost. CAB-05 refines the state model.

For a given progression scope and tier, access may be:

- `not_applicable` — progression does not use that tier;
- `inaccessible` — Character cannot currently pursue the tier;
- `eligible_to_unlock` — all non-cost access conditions are satisfied;
- `unlocked_paid` — access was purchased;
- `unlocked_granted` — access was granted by an authorized source;
- `temporarily_available` — temporary rule grants access without permanent ownership;
- `historically_owned_unavailable_for_new_selection` — preserved history where source/entitlement/current rules no longer permit new selection.

A Character must still satisfy node-specific eligibility, prerequisites, learning/acquisition readiness, exclusions, XP affordability, and approvals after tier access is available.

## 7. Higher-tier access cost — candidate default

Recovered sources use several incompatible approaches:

- separate XP cost to unlock a tier plus separate Ability prices;
- sequential purchase with no separately expressed tier-entry tax;
- source-granted or innate access;
- explicit prior-node/count prerequisites;
- special acquisition or faction/progression access.

CAB therefore does not pretend every historical tree already follows one identical rule.

### 7.1 CAB recommendation

For an **ordinary purchasable five-tier Ability progression**, CAB recommends:

1. Tier 1 access is established when the progression is legitimately opened/entered.
2. Tiers 2–5 use a **one-time tier-access XP purchase** by default after all non-cost access conditions are satisfied.
3. Individual Abilities within the unlocked tier retain their own XP prices unless granted/free.
4. The tier-access cost is a depth/specialization commitment and is calibrated in CAB-06; CAB-05 does not preserve the old 500 / 2,000 / 5,000 / 10,000 / 20,000 schedule as final.
5. A progression may explicitly use another access mode—prerequisite-only, grant, acquisition milestone, sequential node, or other governed mode—when its owning rules require it.
6. Species/Innate, environmental, transformation, faction, artifact, spell-capacity, or other special progressions are not forced into the ordinary purchasable-tree mode merely because they carry tier labels.

This preserves a real cost to specialization/depth without restoring the universal filler-count ladder.

Whether this becomes the normal default is an owner gate.

## 8. Prerequisites inside the tier model

Because the universal prior-tier quantity ladder is retired, progression depth is established through authored structure rather than filler.

A higher-tier node may require any combination of:

- access to the target tier;
- one or more explicit prior nodes;
- a branch/path state;
- a Skill/Knowledge/proficiency threshold;
- an Attribute threshold;
- a milestone, perk, achievement, or mentor;
- learning/project completion;
- an acquisition/eligibility condition;
- a tree-specific mastery count where genuinely useful.

A tier unlock does **not** automatically grant every node in that tier and does not waive node-specific prerequisites.

## 9. Short, capped, and incomplete trees

CAB distinguishes a deliberately short progression from a source/content gap.

### 9.1 Recommended well-formed default

- A progression may intentionally **cap before Tier 5** when no deeper content is justified.
- A complete progression should normally occupy **contiguous tiers** from its declared starting tier through its declared cap.
- A missing intermediate tier is a content-quality/provenance warning unless the owning rule explicitly declares the gap intentional.
- CAB does not invent filler Abilities merely to populate five tiers.
- A tree capped at Tier 3 is not automatically "weaker" than every five-tier tree; it simply has no published depth beyond its cap.
- A later expansion may add deeper tiers through normal governed content/versioning.

Recovered groups that begin at Tier 3, contain only Tier 5, or skip intermediate tiers remain source-visible and should be reviewed in CAB-11/12 rather than silently normalized.

This policy remains an owner gate.

## 10. Tier and grants

CAB-04 grant semantics remain controlling:

- a free grant waives XP cost when the source says it is free;
- a source may establish eligibility and/or tier access when it explicitly grants those states;
- unrelated prerequisites, learning requirements, exclusions, or branch-depth requirements are not silently bypassed;
- temporary grants do not become permanent tier ownership unless explicitly converted by a governed rule.

A Species grant can therefore provide a Tier-appropriate innate ability without making every ordinary Ability of the same tier available for purchase.

## 11. Tier and Character creation

CAB-03 remains controlling:

- the normal Character starts with five free Ability Trees;
- Tier-1 access in those five trees is free;
- five eligible Tier-1 Abilities are free;
- extra-tree opening costs and higher-tier costs remain subject to CAB-06 calibration;
- the current 1,300-XP normal-start default remains recalibratable.

CAB-05 does not use creation grants to infer post-creation tier-unlock prices.

## 12. Tier and entitlement

The approved product rule limiting free-product access to the first two Ability tiers remains an **entitlement rule**, not a balance rule.

It must not be used to infer that:

- Tier 2 is a power ceiling for ordinary gameplay;
- Tier 3 automatically requires payment in Character XP because of product entitlement;
- entitlement status changes an Ability's tier;
- a granted higher-tier Ability becomes mechanically Tier 2 for a free user.

Product access and Character advancement remain separate decisions.

## 13. Balance interpretation

A tier gives CAB a useful structural axis for later audits, but final balance remains multidimensional.

Later CAB work must separately evaluate:

- action/reaction economy;
- passive stacking;
- resource costs and regeneration;
- summons/minions;
- defenses, immunities, and recovery;
- range, mobility, information, control, and challenge bypass;
- environment/context dependence;
- acquisition rarity;
- grant chains and substitutions;
- synergy with other owned abilities.

A narrow Tier-5 technique can legitimately cost less and contribute less simultaneous encounter power than a broad Tier-3 reality-altering capability. That is not automatically a tier error; CAB-11–15 must inspect the actual record and its owning progression.

## 14. Owner policy gates

CAB-05 requires owner judgment on four points before CAB-06 can safely calibrate tier and Ability costs:

1. the shared semantic descriptor vocabulary;
2. whether ordinary tiered Ability trees normally pay a separate one-time T2–T5 tier-access XP cost;
3. how short/sparse trees are treated;
4. whether Tier 5 means apex depth within its own progression rather than a universal legendary/world-shaping power floor.

These are recorded in `CAB-05_OWNER_QUESTIONNAIRE.md`.

## 15. Forward routing

- tier-access and Ability price calibration -> CAB-06;
- action economy and simultaneous power -> CAB-07;
- stacking/synergy -> CAB-08;
- acquisition/eligibility exceptions -> CAB-09;
- attribute/skill interaction -> CAB-10;
- sparse/malformed tree and corpus audit -> CAB-11/CAB-12;
- high-risk outlier review -> CAB-13;
- equal-XP and multidimensional benchmarks -> CAB-14/CAB-15;
- pacing and awards -> CAB-16/CAB-17;
- veteran-depth stress -> CAB-18.
