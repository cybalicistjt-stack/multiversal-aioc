# CAB-06 — Source Cost Audit

**Program:** CAB — Character Advancement & Balance  
**Purpose:** bounded quantitative evidence for XP calibration; source prices remain provenance, not automatically current calibrated rules.

## Corpus coverage

Five portable Ability CSV families:

| Source family | Records |
|---|---:|
| Core Abilities | 1,256 |
| Species / Innate | 2,203 |
| Magic / Faction | 118 |
| Prestige / Environment | 1,018 |
| Profession / Crafting | 221 |
| **Total** | **4,816** |

Numeric/source-expressed XP coverage:

- direct `Ability_XP_Cost`: **1,712** records;
- `Tier_Unlock_XP`: **1,338** records;
- `Upgrade_Cost_XP`: **402** records.

A majority of records therefore cannot be normalized by copying an existing numeric price.

## Direct Ability XP distribution

Across the 1,712 numeric direct costs:

| Percentile | XP |
|---|---:|
| 5% | 150 |
| 10% | 200 |
| 25% | 387.5 |
| 50% | 700 |
| 75% | 2,500 |
| 90% | 5,000 |
| 95% | 7,500 |
| 99% | 20,000 |

Observed range extends from approximately 20 XP to 50,000 XP.

The most frequent individual prices include 500, 300, 1,000, 2,000, 5,000, 400, 1,500, 3,000, 200, 350, and 150 XP. The corpus does not exhibit one clean global interval or one source-consistent progression.

## Tier medians and overlap

For records carrying both numeric Tier 1–5 and numeric direct XP:

| Tier | Records | Median direct XP | Observed range |
|---|---:|---:|---:|
| 1 | 272 | 250 | 20–3,000 |
| 2 | 264 | 700 | 40–7,500 |
| 3 | 270 | 1,500 | 60–15,000 |
| 4 | 226 | 3,000 | 110–25,000 |
| 5 | 215 | 5,000 | 200–40,000 |

The medians rise, but overlap is large enough that tier cannot be used as an exact direct-cost table.

## Common direct-price ladders

Among tree groups with numeric direct prices in all five tiers, recurring median ladders include:

- **500 / 1,000 / 2,000 / 3,500 / 5,000** — 12 groups;
- **175 / 500 / 1,250 / 2,750 / 6,250** — 10 groups;
- **50 / 75 / 150 / 200 / 300** — 8 groups;
- **3,000 / 7,500 / 15,000 / 25,000 / 40,000** — 4 groups;
- several additional 200–500 starting ladders with 5,000–12,250 Tier-5 medians.

These ladders differ by more than two orders of magnitude at comparable nominal depth.

## Tier-unlock evidence

The most common recovered unlock vector is:

**500 / 2,000 / 5,000 / 10,000 / 20,000**

observed across 51 grouped progressions in the bounded parse.

Other observed vectors include:

- 500 / 1,500 / 5,000 / 10,000 / 20,000;
- 500 / 1,500 / 3,500 / 7,000 / 15,000;
- 100 / 250 / 500 / 1,000 / 2,000;
- 500 / 3,000 / 7,000 / 15,000 / 30,000;
- 300 / 600 / 1,200 / 2,400 / 4,800;
- special progressions with no separate lower-tier unlock values.

The source evidence therefore supports the *existence* of one-time depth costs but not one universally authoritative numeric schedule.

## Upgrade-cost evidence

There are 402 numeric upgrade prices. Their distribution is also highly dispersed:

- 10th percentile: roughly 150 XP;
- 25th percentile: roughly 1,500 XP;
- median: roughly 4,000 XP;
- 75th percentile: roughly 11,250 XP;
- 90th percentile: roughly 30,000 XP;
- 95th percentile: roughly 40,000 XP;
- 99th percentile: roughly 50,000 XP.

This strongly argues against inheriting a universal upgrade percentage or table.

## Outlier evidence

The corpus contains both likely underpriced and likely over-/differently-priced records relative to their described mechanics.

Examples visible in the bounded data include:

- Tier-4/Tier-5 martial records priced around 110–300 XP while granting strong damage, permanent attack/damage bonuses, advantage, or additional-move effects;
- Tier-3/Tier-4 psionic records priced at 15,000–25,000 XP for effects such as levitation, prediction, area force, or information access;
- Tier-5/Mastery psionic records at 40,000–50,000 XP;
- high-cost magical/faction capstones around 20,000 XP that include summons, transformations, domination, large-area damage, or severe fate/control effects.

CAB-06 does not declare which individual record is correct from price text alone. These examples prove that source price cannot substitute for burden review.

## Source-family medians are not safe universal tables

Examples among numeric direct-cost records:

- Core commonly follows approximately 500 / 1,000 / 2,000 / 3,500 / 5,000 medians;
- Profession/Crafting is often cheaper in lower tiers;
- Species/Innate numeric examples are often substantially higher by later tiers but most Species records have no numeric direct cost at all;
- Prestige/Environment mixes low environmental/practical costs with extremely high psionic costs;
- Magic/Faction contains both moderate and very high capstones.

Domain/source family therefore cannot be used as a blanket discount or surcharge. Price must follow the actual capability record.

## Recovered non-Ability anchors

CAB-02/CAB-03 recovered additional design-generation anchors including:

- extra Ability Tree: 1,000 XP;
- Attribute +1: 250 XP;
- Skill rank: 250 XP;
- Knowledge tier: 500 XP;
- proficiency: 750 XP;
- creation HP purchases with a recovered cumulative 300 / 750 / 1,250 / 2,000 ladder;
- multiple conflicting tier-unlock schedules.

These are calibration inputs, not automatically accepted current prices. CAB-10 owns broad-stat/Skill/Knowledge/proficiency valuation; CAB-14/15 own survivability comparison; CAB-16 owns absolute pacing scale.

## Audit conclusion

The source corpus supports four firm conclusions:

1. there is a real XP-buy design tradition;
2. one-time progression/tier access costs are strongly source-attested;
3. direct Ability prices usually increase with depth but cannot be derived from tier alone;
4. the numeric source economy is too fragmented to adopt wholesale without a common burden-calibration framework.
