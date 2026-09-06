# CAB-23 — Final Handoff

**Program:** CAB — Character Advancement & Balance  
**Status:** `COMPLETED_VERIFIED`  
**Owner/final authority:** John Brandon Turner  
**Closed:** 2026-09-05

## 1. CAB is closed

CAB-01 through CAB-23 are complete. There is no CAB-24 and no active CAB successor tranche.

The CAB program established the governing Character advancement/balance rules, validated their economic/pacing behavior, audited the bounded Ability corpus, and produced a prioritized repair/repricing handoff for legacy content that is not yet semantically normalized.

Future work must not reopen CAB by implication. A later change to a settled CAB rule requires new explicit governance authority and must cite the superseded CAB rule.

## 2. Canonical reading order

For future design, content-repair or implementation planning, read CAB in this order:

1. **`CAB-22_FINAL_ADVANCEMENT_RULES.md`** — concise final game-rule authority.
2. **`CAB-20_INTEGRATED_ADVANCEMENT_BALANCE_MODEL.md`** and `CAB-20_INTEGRATED_MODEL_v1.0.0.json` — integrated rule architecture and machine-readable model.
3. **`CAB-21_REFERENCE_CHARACTER_AND_CAMPAIGN_SIMULATION.md`** and `CAB-21_SIMULATION_LEDGER_v1.0.0.json` — validation of starting XP, pacing and long-horizon opportunity costs.
4. **`CAB-22_CONTENT_REPAIR_MAP_v1.0.0.json`** — prioritized legacy-content repair/repricing handoff.
5. **`CAB-19_RESPEC_CORRECTION_AND_MIGRATION.md`** — nonpunitive Character migration and correction behavior.
6. **`CAB-23_COMPLETION_AUDIT.md`** — closure and cross-tranche consistency evidence.
7. Earlier tranche artifacts only when detailed provenance, audit evidence or a specific historical decision is required.

## 3. Settled advancement model

The core rule is:

> XP regulates how fast a Character acquires permanent power. Prerequisites and acquisition rules regulate coherent development and eligibility. Tiers regulate depth. Action economy, resources, stacking and dependencies regulate how much acquired power can matter at once.

Settled CAB direction includes:

- XP as ordinary permanent advancement currency; AP retired;
- five developmental tiers, not Character Levels;
- no universal CR/power scalar;
- 1,300 XP normal starting grant;
- Standard 500 XP/substantive-session long-run pace;
- accomplishment award bands 0/250/500/750/1,000 XP;
- five free starting Ability Trees, free T1 access there, five free T1 Abilities;
- direct Ability pricing by effect burden, not tier;
- separate ordinary progression/tier-access prices;
- Prestige may begin at T3 with explicit requirements and no T1/T2 back-pay;
- governed Attribute/Skill/Knowledge/Proficiency advancement schedules;
- conditional learning projects with capped Int/Wis learning acceleration;
- default 1 Action + 1 Bonus Action + movement + 1 Reaction/round;
- anti-recursion and Free/No-Action limiting rules;
- mechanical interaction groups rather than source-family stacking;
- eligibility/acquisition/affordability separation;
- structured spell surface remains 0 direct per-spell learning XP under its owning capacity rules;
- 16-dimension Character balance comparison rather than a scalar score;
- no blanket breadth tax, Ability-count cap, readied slots or global diminishing-return pricing;
- voluntary respec by Campaign policy, with 100% actual-paid-XP refund when allowed;
- nonpunitive correction and no retroactive XP debt from later repricing.

## 4. What CAB did not claim

CAB completion does **not** mean:

- every one of the 4,816 legacy Ability records has been individually repriced;
- every missing runtime field has been repaired;
- every source omission has been filled;
- every prerequisite has a globally unique stable-ID graph;
- every high-risk mechanic has passed detailed content repair;
- global stable Ability IDs have already been assigned;
- application schemas/UI/runtime automatically implement CAB;
- CAB created a software release mandate.

These distinctions are mandatory. Rules completion and content normalization are separate.

## 5. Immediate legacy-content repair handoff

Use `CAB-22_CONTENT_REPAIR_MAP_v1.0.0.json` as the repair entry point.

### P0 — source integrity and identity

First:

- repair/recover the Rain of Arrows source-field boundary contamination without guessing or deleting provenance;
- use `source_dataset + Record_ID` as the safe current record identity because 1,256 local IDs collide across files and affect 2,512 rows;
- design a governed migration to globally unique stable IDs with aliases/history before cross-file canonicalization depends on those IDs.

### P1 — mechanical determinism/high risk

Then recover/govern the consequential missing semantics for:

- Action Economy;
- trigger/frequency;
- duration/resources;
- stacking/interaction group;
- acquisition mode;
- prerequisite/dependency predicates;
- high-risk action multipliers, summons, immunities, regeneration, transformations, bypasses, resource loops and unbounded scaling.

### P2 — economic and structural normalization

Only after source/semantic confidence is sufficient:

- reprice direct purchases using CAB effect-burden calibration while preserving legacy price provenance;
- migrate ordinary tier-access pricing to CAB anchors where appropriate;
- resolve the Temporal & Reality Bending Science T2 gap from source evidence;
- resolve the Heavy Weapons T2 start without inventing a T1;
- review duplicate name/tree/tier tuples;
- classify mixed Species/Innate content using PPIA-05 and CAB-09 authority.

### P3 — validation and presentation

After material repair batches:

- rerun equal-XP and multidimensional benchmarks;
- perform survivability evidence work before extending direct HP beyond +20;
- project final CAB rules into Player/GM/reference surfaces without collapsing tier, price, acquisition, prerequisite, RAV, timing and balance dimensions.

## 6. Repair/migration invariants

Any future content repair using this handoff must:

- preserve exact source text/source price as provenance;
- distinguish source absence from content defects;
- never invent missing Abilities or prerequisites merely for structural neatness;
- recover source integrity before repricing corrupted content;
- make high-risk semantics deterministic before claiming balance certification;
- avoid retroactive XP debt for previously valid Characters;
- preserve append-only migration/correction evidence;
- rerun CAB benchmarks after material batches.

## 7. Software implementation boundary

CAB is a game-rules/content-governance authority. **CAB itself grants no Multiversal-app implementation, migration, deployment or release authority.**

Application implementation planning may consume these artifacts when the owning software roadmap authorizes that work, but implementation must preserve the CAB distinctions rather than simplifying them away.

## 8. Recovery instruction

A future conversation recovering CAB should not attempt to resume a tranche. CAB is closed.

The correct recovery statement is:

- CAB-01 through CAB-23: `completed_verified`;
- governing final rules: `CAB-22_FINAL_ADVANCEMENT_RULES.md`;
- governing integrated model: `CAB-20_INTEGRATED_ADVANCEMENT_BALANCE_MODEL.md` / JSON;
- validation: CAB-21 simulation;
- outstanding legacy content: CAB-22 repair map;
- completion audit/handoff: CAB-23;
- no unresolved owner-policy question;
- no CAB successor.
