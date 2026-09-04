# CAB-04 — Advancement Architecture Completion Report

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-04  
**State:** `completed_verified` analysis; owner policy answers pending  
**Owner/final authority:** John Brandon Turner  

## Completed

CAB-04 defined the advancement architecture that sits underneath XP-buy progression without finalizing prices or five-tier semantics.

Durable outputs:

- `CAB-04_ADVANCEMENT_ARCHITECTURE.md` — human-readable gate/transaction architecture;
- `CAB-04_ADVANCEMENT_STATE_MODEL_v0.1.0.json` — machine-readable gate, state, grant and learning-project model;
- `CAB-04_OWNER_QUESTIONNAIRE.md` — four owner policy gates.

## Findings

### 1. The current Character transaction architecture is already sufficient

Current Character governance already requires advancement award/proposal/cost ledger, authoritative validation, optional decision, exactly-once commit, before/after evidence and append-only history. CAB-04 does not replace this path.

### 2. Advancement restrictions are multidimensional

The bounded 4,816-record ability corpus contains dedicated fields for tier prerequisites, ability prerequisites, attribute requirements, situational-perk requirements, environment/context and other restrictions. These cannot be faithfully represented by XP alone or by one universal tier count.

### 3. XP should answer affordability, not eligibility

A Character can possess enough XP but still be biologically incompatible, lack a prerequisite, lack tier access, lack required training/exposure, violate an exclusion or lack Campaign/source permission. CAB-04 makes those failures independently explainable.

### 4. Tier access is a distinct state, not automatically a tax

Some progression families have tier-unlock XP and quantity gates; others do not. Architecture can represent tier access while CAB-05 decides how five-tier progression should normally unlock.

### 5. Learning/training needs a governed place without becoming universal bookkeeping

Recovered design sources contain training/practice concepts, but the current Character architecture does not mandate training for every purchase. CAB-04 adds a `learning_project`/`development_project` model for options that require study, practice, instruction, exposure, attunement or equivalent development.

### 6. Intelligence/Wisdom faster learning now has an architectural home

The cleanest attachment point is learning-project progress/readiness rather than global XP income. Exact formulas remain CAB-10 work and must be pacing-tested in CAB-16/17/18.

### 7. Grants must not become an uncontrolled bypass

Species, forms, backgrounds, abilities, Campaign rules and other sources can grant capabilities. CAB recommends that a free grant waive cost, establish eligibility where its source inherently does so, and bypass other gates only when explicitly stated.

### 8. Special acquisition is opportunity/eligibility, not price

Creation-only innate openings, mentors, faction induction, exposure, transformation, artifacts, research and narrative milestones should change availability/eligibility/readiness. They do not become ordinary shopping-list options merely because an XP price exists.

## Architecture established without owner gate

CAB-04 establishes the following as structural requirements:

1. separate authority, availability, eligibility, prerequisite, tier/depth, learning/acquisition, affordability, conflict/exclusion, approval and commit gates;
2. XP does not substitute for eligibility or prerequisites;
3. advancement remains event-based, source-linked and exactly-once;
4. grants retain source/reason and explicit bypass behavior;
5. tier access can be represented separately from node cost;
6. learning can be represented as a development project;
7. Intelligence/Wisdom learning benefit attaches architecturally to the learning process, with the exact mechanic deferred;
8. special acquisition remains distinct from price;
9. respec/correction cannot silently destroy history or dependents.

## Recommendations requiring owner answer

1. **No universal prior-tier quantity gate.** Permit tree-specific explicit prerequisites/counts where justified.
2. **Use learning projects only where the owning rule requires learning/development**, rather than for every advancement.
3. **Use Intelligence/Wisdom to accelerate applicable learning progress**, not as a universal XP award multiplier or blanket purchase discount.
4. **Free grants waive cost by default but do not silently bypass unrelated eligibility/prerequisite/exclusion gates.**

## Owner questionnaire

`CAB-04_OWNER_QUESTIONNAIRE.md` contains four questions with recommendations:

- CAB-Q04-01 — universal prior-tier quantity gate: **A**;
- CAB-Q04-02 — breadth of training/practice requirement: **A**;
- CAB-Q04-03 — Intelligence/Wisdom faster-learning attachment: **A**;
- CAB-Q04-04 — grant bypass semantics: **A**.

Unanswered questions remain unresolved and do not silently default.

## Forward routing

- owner answers -> record before CAB-05 execution;
- final five-tier semantics -> CAB-05;
- XP price calibration -> CAB-06;
- acquisition/eligibility details -> CAB-09;
- Intelligence/Wisdom formula and attributes/skills -> CAB-10;
- corpus/tree audit -> CAB-11/12;
- progression pacing/training duration -> CAB-16;
- XP awards -> CAB-17;
- long-campaign learning divergence -> CAB-18;
- respec/correction/migration -> CAB-19.

## Completion statement

CAB-04's bounded architecture work is complete when these artifacts are merged, the CAB backlog marks CAB-04 `completed_verified`, and CAB-05 is selected but held pending the four owner policy answers. No application implementation authority is created.

## Exact successor

**CAB-05 — Five-Tier Model** — selected after CAB-04 closeout, with execution held until CAB-04 owner answers are recorded or explicitly deferred.
