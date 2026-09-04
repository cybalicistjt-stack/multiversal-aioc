# CAB-04 — Advancement Architecture

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-04  
**State:** `completed_verified`  
**Owner/final authority:** John Brandon Turner  
**Owner decisions:** `CAB-04_OWNER_DECISIONS_2026-09-04.md`

## 1. Purpose

Define the distinct jobs of XP, eligibility, prerequisites, tier/depth access, learning/training, grants, acquisition, approval, and advancement history so Multiversal advancement remains classless, source-governed, and explainable without collapsing every restriction into price or a universal prior-tier count.

CAB-04 does not finalize tier meanings, numeric XP prices, Intelligence/Wisdom formulas, acquisition details, progression pacing, XP awards, or respec economics. Those remain routed to later CAB tranches.

## 2. Source-backed architecture findings

### Current Character advancement is already event-based

The current Character framework requires authoritative progression awards, advancement proposals, cost ledgers, validation, optional GM decision, exactly-once commit, before/after evidence, and append-only history. It preserves evaluated prerequisites, grants, substitutions, rules profile, and source/provenance.

CAB-04 therefore preserves the existing transaction architecture and defines the game-rule gates it evaluates.

### Progression restrictions are already multidimensional

The bounded 4,816-record Ability corpus contains dedicated fields including:

- `Tier_Prerequisites` — 978 meaningful records;
- `Ability_Prerequisites` — 322;
- `Attribute_Requirements` — 460;
- `Situational_Perk_Requirement` — 470;
- `Environment_or_Context` — 657;
- plus XP prices, upgrades, equipment/tool requirements, and source-specific special rules.

These restrictions overlap but are not interchangeable. A Character may have enough XP while lacking the correct biology, prior technique, attribute, context, trainer, faction, form, tree depth, source permission, or Campaign permission.

### Grants are a distinct concept

Species, environments, items, forms, templates, Conditions, vehicles, Campaign rules, and other sources can grant capabilities. A grant must retain source, reason, duration where relevant, and explicit bypass behavior.

### Tier access is not already universalized

Some progression families use tier-unlock XP and prior-tier requirements; others do not. Species/Innate records in the bounded corpus contain direct Ability XP prices but no numeric tier-unlock field. CAB-04 therefore treats tier/depth access as a distinct possible gate rather than a universal tax or count formula. CAB-05 owns final five-tier semantics.

### Learning/training exists but is not universal

Recovered sources contain practice, instructors, study, exposure, and other development concepts. Current Character architecture does not require training for every purchase. CAB-04 therefore supports governed learning/development projects only where required by the owning rule or explicit GM/Campaign override.

## 3. Core advancement gate order

For a proposed permanent advancement, evaluate separately:

1. **Authority** — may this subject advance this Character?
2. **Availability** — is the Definition/source/rules profile available and allowed?
3. **Eligibility** — is this Character a valid recipient under biology, form, membership, compatibility, acquisition, and Campaign rules?
4. **Prerequisites** — are required prior capabilities/statistics/states satisfied?
5. **Tier/depth access** — does the owning progression require access to this developmental band, and is it open?
6. **Learning/acquisition readiness** — has any required study, practice, exposure, research, attunement, transformation, or narrative acquisition condition been completed?
7. **Affordability** — can the Character pay the authoritative XP cost after explicit grants/waivers/substitutions?
8. **Conflicts/exclusions** — would the selection violate exclusions, duplicate rules, stacking rules, or replacement rules?
9. **Approval** — does Campaign policy require GM or other governed approval?
10. **Commit** — apply exactly once, calculate results, and preserve before/after evidence and history.

No gate substitutes for another. **Enough XP never means automatically eligible.**

## 4. Governed gate semantics

### XP — affordability and permanent advancement commitment

XP answers whether the Character can afford the permanent advancement. XP does not establish eligibility, training, faction standing, prerequisite knowledge, tier access, source access, or narrative opportunity.

The authoritative cost ledger distinguishes base XP cost, explicit modifiers/waivers, grant-funded/free selections, substitutions/replacements, final XP debited, and resulting balance. CAB-06 owns numeric calibration.

### Eligibility — who may acquire the option

Eligibility may depend on Species/biology, form/transformation, innate-at-creation rules, environment/exposure history, faction/order/archetype membership, implants/symbiotes/relics, Campaign rules, source availability, narrative acquisition, or other compatibility rules.

Eligibility is not a surcharge. CAB-09 owns detailed acquisition taxonomy.

### Prerequisites — development dependencies

Prerequisites may include explicit Ability/node IDs, Skill/Knowledge ranks, attributes, proficiency/mastery states, prior grants, milestones, or tree-specific mastery counts.

**Owner decision CAB-Q04-01:** there is **no universal prior-tier quantity gate**. A specific tree/path may require counts or mastery evidence where explicitly authored. Explicit node/path prerequisites are preferred to filler purchasing. The old universal 5 / 4 / 3 / 2 ladder remains deprecated.

### Tier/depth access — developmental band permission

Tier access may project as inaccessible, eligible-to-unlock, unlocked/granted, temporarily available, or historically owned but unavailable for new selection.

Tier itself does not prove universal price, power, or prerequisite count. CAB-05 determines the meaning of the five tiers and the default tier-access mechanism.

### Learning/training/practice — development process

A governed `learning_project` / `development_project` may represent study/research, coached training, physical drills, field practice, exposure/acclimation, meditation/attunement, experimentation/crafting practice, social/faction instruction, or a narrative ordeal/milestone.

A learning project records target option, learning mode, source rule, required progress/time or completion condition, accumulated progress, trainer/tool/location requirements, applicable learning-attribute hook, completion evidence, interruption/expiration rules, and any GM/Campaign override evidence.

**Owner decision CAB-Q04-02:** learning projects are required by default **only where the owning advancement rule requires them**. Advancements with no learning requirement may commit immediately once all other gates are satisfied.

A GM/Campaign advancement policy may explicitly add, waive, shorten, extend, or otherwise modify a learning requirement. The override must be attributable and visible. It modifies the learning/readiness gate only; it does not silently change XP prices, waive unrelated eligibility/prerequisites/exclusions, or rewrite history.

XP is normally debited when the permanent advancement commits, unless an owning rule explicitly consumes XP earlier.

### Intelligence/Wisdom faster learning

**Owner decision CAB-Q04-03:** high Intelligence and/or Wisdom accelerate applicable learning/development projects rather than automatically increasing XP awards or reducing every XP purchase price.

The owning learning mode determines whether Intelligence, Wisdom, or a governed combination applies. Both do not automatically stack merely because both are high. CAB-10 owns formulas; CAB-16/17/18 must validate pacing and long-campaign divergence.

### Grants

Grant types include creation, source, Campaign, milestone, temporary, replacement/upgrade, and migration/correction grants.

**Owner decision CAB-Q04-04:**

- a grant waives XP cost when it says the option is free;
- a grant satisfies eligibility when the grant source itself establishes that eligibility;
- prerequisites, tier/depth access, learning requirements, and exclusions are bypassed only when the granting rule explicitly establishes, substitutes for, or waives them;
- a generic free choice does not automatically bypass biology, compatibility, source availability, or exclusions;
- temporary grants do not silently become permanent purchases.

### Special acquisition — opportunity rather than price

Creation-only innate openings, mentors, faction induction, exposure/acclimation, transformations, implants/symbiosis, artifact bonds, research discoveries, narrative ordeals, and Campaign-awarded opportunities change availability, eligibility, or readiness. They are not merely higher-priced shopping-list entries. CAB-09 owns final semantics.

## 5. Advancement projection states

A Character-facing option may project as:

- `hidden_or_unauthorized`;
- `unavailable_source`;
- `ineligible`;
- `missing_prerequisite`;
- `tier_locked`;
- `learning_required`;
- `learning_in_progress`;
- `ready_unaffordable`;
- `ready_to_propose`;
- `awaiting_approval`;
- `committed`;
- `historical_unavailable`;
- `superseded_or_replaced`.

The system should explain the actual blocking reason instead of returning a generic “not enough XP.”

## 6. Advancement transaction

### Inspect

Show cost, prerequisites, eligibility, tier state, learning requirement, grants, exclusions, and source links.

### Readiness evaluation

Evaluate authority, availability, eligibility, prerequisites, tier/depth access, and learning/acquisition readiness. Incomplete required learning can begin/continue without prematurely committing the permanent advancement.

### Proposal and cost ledger

Record option stable ID/version, before-state version, evaluated gate evidence, base/final XP cost, grants/waivers/substitutions, conflicts/exclusions, resulting grants/effects, source/rules profile, and approval requirement.

### Authoritative revalidation

Immediately before commit, revalidate current Character version, XP balance, prerequisites, eligibility, tier state, learning completion, conflicts, entitlements, and Campaign policy. Client preview is never authoritative.

### Approval where required

Campaign policy may require GM approval. Silence is not approval.

### Exactly-once commit

Debit final XP, add the advancement state, apply explicit grants/replacements, recalculate derived state, record provenance and before/after evidence, and append the immutable event/receipt.

### Dependent-state integrity

New advancement must not silently delete or deactivate existing choices. Replacement/conflict must be explicit. Later respec/correction that would invalidate dependents requires an explicit dependency/cascade plan; CAB-19 owns refund/respec economics.

## 7. Final CAB-04 architecture decisions

CAB-04 establishes:

1. XP, eligibility, prerequisites, tier access, learning/acquisition, exclusions, approval, and commit are separate concepts.
2. XP never substitutes for eligibility or prerequisites.
3. Advancement remains event-based, attributable, source-linked, and exactly-once.
4. There is no universal prior-tier quantity gate; specific paths may explicitly require mastery counts.
5. Tier access is a distinct state; CAB-05 owns final five-tier semantics.
6. Learning/development projects are conditional rather than universal.
7. GM/Campaign policy may explicitly modify learning requirements without silently altering unrelated advancement gates or prices.
8. Intelligence/Wisdom faster learning attaches to applicable learning progress/readiness, not ordinary global XP gain or blanket discounts.
9. Grants retain source/reason and controlled bypass semantics.
10. Special acquisition remains distinct from price.
11. Respec/correction must preserve history and dependent-state integrity.

## 8. Forward routing

- five-tier semantics and tier-access defaults → CAB-05;
- XP price calibration → CAB-06;
- acquisition/eligibility taxonomy → CAB-09;
- Intelligence/Wisdom learning formula and attribute/Skill interaction → CAB-10;
- corpus/tree audit → CAB-11/CAB-12;
- progression pacing and learning-duration validation → CAB-16;
- XP awards → CAB-17;
- long-campaign learning divergence → CAB-18;
- respec/correction/migration → CAB-19.

## 9. Completion

CAB-04 is `completed_verified`. All four owner policy gates are resolved in `CAB-04_OWNER_DECISIONS_2026-09-04.md`.

**Exact successor:** **CAB-05 — Five-Tier Model** — `selected_not_started` and cleared to execute.