# PPIA-07 — Completion Candidate

**Work item:** PPIA-07 — Rune Construction RPG System  
**State:** COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES  
**Owner:** John Brandon Turner

## Verified upstream milestones

### Foundation — PR #241

Squash merge: `183d199d69f5cce121d4b971f33fe6c0145a6c45`

Established source boundaries from 9 retained Rune-relevant PDFs / 170 pages and 4 structured CSVs / 2,225 rows, including 3 explicit rune-crafting records and 16 structured Scripts & Macros records; 15 identity/state layers; 12 presentation profiles; and explicit no-invention boundaries for missing canonical rune grammar/cost data.

### Deterministic grammar/reference — PR #242

Squash merge: `15202626a0ba96d7675ee4ab4cbec4923158cd63`

Established deterministic Rune Construction syntax, explicit grouping/no guessed connector precedence, canonical linear serialization, validity rules and 20 bounded grammar/reference cases.

### Cost, complexity, stability and progression — PR #243

Squash merge: `210ca8f13eaba7c1ea295c280368c68a13a300f3`

Established SCI complexity bands, CSL stability-attention bands, 12 typed owning-rule resource adapters, six counterplay hooks, four progression-guidance bands and 16 deterministic/guardrail benchmarks while preserving PPIA-11 final balance authority.

### Integrated Rune Builder workflows — PR #244

Squash merge: `f6ed3a71cf5dc01b14f85879e9acbdf5152af437`

Established 16 end-to-end Rune Builder workflows, 18 governed actions including 7 PPIA-07 authoritative mutation actions, 10 cross-domain handoffs and complete traceability across the 15-layer taxonomy, 20 grammar cases and 16 cost/stability benchmarks.

### Owner-directed full magic-system expansion — PR #245

Squash merge: `86617eb2b9a823950708a88e1a049d5ec72e56d0`

Established the implementation-ready vocabulary basis:

- 34 core runes;
- 16 Operation Runes;
- 18 Essence Runes;
- inherited THEN/WITH/WHEN/IF connector grammar;
- 34 expanded-rune reference cases;
- retained `Magic_Spells.csv` coverage across 385 spells, 10 schools, 7 gameplay roles, 14 normalized effect families and 22 normalized subtype families;
- zero vocabulary-level unroutable spell IDs.

## Owner-directed blind rune-play requirement

Before final completion the owner added a required gameplay mode:

> Players must be able to construct runes blind to the resolved effect. The GM is notified of the interpreted effect and chooses whether it goes through.

The completion package therefore adds a governed `blind-gm-adjudicated` consumer profile built on MV-IA-F006 and IA-D04-002 rather than inventing a second approval engine.

Blind mode requires:

- player can build, serialize, syntax-validate and submit the Rune Construction;
- player receives no interpreted/predicted effect before adjudication;
- suppression is server-side projection, not client hiding;
- authorized GM receives the complete interpreted effect, targets, costs, SCI/CSL, counterplay, warnings, provenance, versions and predicted mutations;
- final decisions are exactly approve, deny and modify-and-approve;
- silence/timeout is never approval;
- modify-and-approve preserves immutable original player construction plus exact semantic diff/reasons;
- GM expression rewrite can never be silent or attributed to the player;
- approved result commits atomically;
- permission, recovery, accessibility, AI and offline boundaries remain intact;
- post-resolution learning remains Campaign/Session/perception-policy controlled.

## Current completion-candidate package

This final package adds:

- `PPIA-07_RUNE_CONSTRUCTION_EXPERIENCE_SPEC_v1.0.0.md` — integrated final implementation-ready design candidate;
- `PPIA-07_BLIND_RUNE_PLAY_CONSUMER_PROFILE_v1.0.0.json` — Rune-specific F006/IA-D04-002 proposal/approval extension;
- `PPIA-07_BLIND_RUNE_PLAY_REFERENCE_CASES_v1.0.0.json` — 16 blind-play cases;
- `PPIA-07_ACCEPTANCE_TRACEABILITY_MATRIX_v1.0.0.json` — 48 blocking requirements across 16 categories;
- deterministic PPIA-07 completion validation and CI.

## Completion coverage

The candidate integrates and preserves:

1. 34 core runes: 16 Operation + 18 Essence;
2. four explicit connection types with no implicit mixed precedence;
3. canonical linear/AST round-trip semantics;
4. typed modifiers and external references;
5. deterministic-supported / governed-adjudication-required / unresolved-owning-rule / invalid semantic classification;
6. 12 typed resource/capacity/crafting/progression/counterplay adapters;
7. SCI structural-complexity calculation and four bands;
8. CSL stability-attention calculation and four bands;
9. four proposal-stage progression-guidance bands;
10. six counterplay hooks;
11. PPIA-03 Item/enchanting ownership boundary;
12. PPIA-08 Campaign/Scene/Session policy/current-state boundary;
13. PPIA-12 setting-local magic-rule boundary;
14. PPIA-11 final balance authority;
15. standard Rune preview mode;
16. blind GM-adjudicated Rune mode;
17. complete GM effect card and explicit approve/deny/modify-and-approve decision model;
18. immutable original proposal and field-addressed modification diff;
19. permission-before-resolution/search/count/export/diagnostic/notification/AI behavior;
20. expected-version, operation-ID, status lookup, reconnect and idempotent recovery;
21. offline draft-only authority boundary;
22. keyboard/touch/screen-reader/high-zoom/reflow/reduced-motion and canonical nonvisual operation;
23. player-AI hidden-effect side-channel prohibition;
24. 385-spell vocabulary-routing coverage;
25. all 20 original grammar/reference cases;
26. all 34 expanded-rune cases;
27. all 16 cost/stability/progression benchmarks;
28. all 16 Rune Builder workflows;
29. all 18 Rune Builder actions;
30. all 10 cross-domain handoffs;
31. all 16 blind-play reference cases;
32. all 48 final acceptance requirements.

## Completion boundaries

PPIA-07 completion does **not**:

- claim the 34-rune vocabulary is verbatim source canon;
- replace the retained spell catalog;
- define universal mana, charge, material, damage, healing, duration, XP, failure or backlash formulas;
- promote SCI to power or CSL to failure probability;
- bypass resistance, counterspell, saves, target validity, crafting rules or setting-local limitations;
- allow blind-mode interpreted effects to reach the player before GM adjudication through UI payloads, errors, counts, history, exports, diagnostics, notifications or AI;
- make silence or timeout approval;
- allow GM changes to erase or silently replace the player's submitted Rune Construction;
- permit broad offline authoritative Rune mutation or resolution;
- activate STAGE-A-A2;
- mutate application runtime;
- authorize release, deployment, tester access, paid services, production credentials or unsupported canonical promotion.

## Required completion evidence

PPIA-07 may become `completed_verified` only after:

1. the exact completion-candidate head passes the dedicated PPIA-07 completion validation;
2. every applicable expanded-rune, workflow, cost/stability, grammar, foundation, transition, PPIA Program, continuity, interaction, operational and regression gate passes on that same exact head;
3. the completion PR merges into canonical `main`;
4. the post-merge checkpoint records the exact validated head, PR, merge SHA and `completed_verified` state;
5. canonical PPIA program continuity advances `current_work_item_id` to the next dependency-optimized item, PPIA-08, without claiming PPIA-08 work has begun before its own governed attempt exists.

Until all conditions are satisfied, this document is a candidate and PPIA-07 remains `started`.
