# CAB-04 — Advancement Architecture

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-04  
**State:** `completed_verified` architecture analysis; owner gates recorded separately  
**Owner/final authority:** John Brandon Turner  

## 1. Purpose

Define the distinct jobs of XP, eligibility, prerequisites, tier/depth access, learning/training, grants, acquisition, approval and advancement history so Multiversal advancement can remain classless, source-governed and explainable without collapsing every restriction into price or a universal prior-tier count.

CAB-04 does **not** finalize tier meanings, numeric XP prices, Intelligence/Wisdom formulas, acquisition details, progression pacing, XP awards or respec economics. Those belong to later CAB tranches.

## 2. Authority and source findings

### 2.1 Current Character architecture is already event-based

The current Character framework requires authoritative progression awards, advancement proposals, cost ledgers, validation, optional GM decision, exactly-once commit, before/after evidence and append-only history. It also preserves prerequisites evaluated, grants, substitutions, rules profile and source/provenance.

CAB-04 therefore does not replace the transaction architecture. It defines the game-rule gates that the existing transaction evaluates.

### 2.2 Progression records already separate several gate families

The portable 4,816-record ability corpus contains dedicated fields for:

- `Tier_Prerequisites` — 978 meaningful records in the bounded census;
- `Ability_Prerequisites` — 322;
- `Attribute_Requirements` — 460;
- `Situational_Perk_Requirement` — 470;
- `Environment_or_Context` — 657;
- plus XP price fields, upgrades, equipment/tool requirements and source-specific special rules.

Those fields overlap but are not interchangeable. A Character may have enough XP while lacking the correct biology, attribute, prior technique, context, trainer, faction, transformation, tree depth or Campaign permission.

### 2.3 Ability grants are already a separate concept

Current game-framework material allows species, environments, items, forms, templates, conditions, vehicles and Campaign rules to grant abilities. Grants retain source, reason, duration, activation state and stacking/replacement behavior, and prerequisites/exclusions may be checked at selection and/or activation.

### 2.4 Tier access is not already universalized

CAB-02 established that some trees contain numeric tier-unlock costs while Species/Innate records in the bounded corpus contain direct Ability XP prices but no numeric tier-unlock field. Recovered trees also use many different quantity and explicit-node prerequisite patterns.

CAB-04 therefore treats tier/depth access as a **possible governed gate**, not a universal XP tax or a universal quantity formula. CAB-05 owns the final five-tier semantics.

### 2.5 Training/practice exists as a recovered design family, not a current universal gate

Historical source conversations contain skill practice/training, instructors, challenge-based practice and other learning concepts. The current Character architecture does not require a universal training period for every advancement.

CAB-04 therefore creates a place for governed learning projects without silently making every purchase wait on downtime.

## 3. Core advancement principle

For any proposed permanent advancement, the system asks separate questions in this order:

1. **Authority:** may this subject propose advancement for this Character?
2. **Availability:** is the governing Definition/source/rules profile available and allowed?
3. **Eligibility:** is this Character the kind of Character that may acquire it?
4. **Prerequisites:** has the Character developed the required prior capabilities or statistics?
5. **Tier/depth access:** does the Character currently have access to the relevant developmental band, when the owning progression uses such a gate?
6. **Learning/acquisition readiness:** has any required training, practice, exposure, research, attunement, transformation or narrative acquisition condition been completed?
7. **Affordability:** can the Character pay the authoritative XP cost after grants/waivers/substitutions?
8. **Conflicts/exclusions:** would the selection violate an exclusion, duplicate rule, stacking rule or replacement rule?
9. **Approval:** does Campaign policy require GM/other governed approval?
10. **Commit:** apply exactly once, record resulting grants/substitutions and preserve before/after evidence.

No single answer substitutes for another. In particular, **enough XP never means automatically eligible**.

## 4. Gate definitions

### 4.1 XP — affordability and advancement commitment

XP answers: **Can the Character afford the permanent advancement?**

XP does not by itself establish biology, training, experience, faction standing, prerequisite knowledge, tier access, source access or narrative opportunity.

XP remains a Character advancement balance, not money and not an ordinary asset currency.

The authoritative cost ledger must distinguish:

- base XP cost;
- explicit cost modifiers/waivers;
- grant-funded or free selections;
- substitutions/replacements;
- final XP debited;
- resulting balance.

CAB-06 owns final numeric calibration.

### 4.2 Eligibility — who can ever acquire it under current state

Eligibility answers: **Is this option valid for this Character at all right now?**

Possible eligibility inputs include:

- Species/biology;
- form or transformation state;
- innate-at-creation rule;
- environment or exposure history;
- faction/order/archetype membership;
- possession of a required implant, symbiote, relic or Character-bound progression object;
- campaign/rules-profile permission;
- source/entitlement availability;
- narrative acquisition flag;
- special compatibility rules.

Eligibility is not a surcharge. CAB-09 owns the detailed acquisition taxonomy.

### 4.3 Prerequisites — development dependencies

Prerequisites answer: **What must already be true before this advancement can be learned/selected?**

Supported prerequisite types include:

- explicit Ability/node IDs;
- skill or Knowledge ranks;
- attribute thresholds;
- proficiency/mastery state;
- prior grant/state;
- explicit milestone/achievement;
- tree-specific mastery counts where an owning tree genuinely requires breadth;
- other stable rule references.

CAB-04 recommends explicit prerequisites over a universal filler-buying formula. A prior-tier quantity requirement remains legal when a specific tree needs it, but it should be authored as an explicit prerequisite rather than inherited from a global rule.

### 4.4 Tier/depth access — developmental band permission

Tier access answers: **May the Character select nodes in this developmental band?**

Architecture supports an explicit access state such as:

- inaccessible;
- eligible_to_unlock;
- unlocked/granted;
- temporarily available;
- historically owned but unavailable for new selection.

How five tiers are defined and whether tier access normally costs XP, is granted by mastery, follows explicit node paths, or uses a combination remains CAB-05 work.

CAB-04 rejects treating `tier` itself as proof of a universal price, universal power level or universal prerequisite count.

### 4.5 Learning / training / practice — development process

Learning answers: **Does this advancement require time or developmental work in addition to eligibility and XP?**

CAB-04 defines a governed `learning_project` / `development_project` concept for advancement records that require one. Possible modes include:

- study/research;
- coached training;
- physical practice/drills;
- field practice;
- exposure/acclimation;
- meditation/attunement;
- experimentation/crafting practice;
- social/faction instruction;
- narrative ordeal/milestone.

A learning project records:

- target progression option;
- learning mode;
- source/rule requiring it;
- required progress/time or completion condition;
- accumulated progress;
- trainer/mentor/tool/location requirements if any;
- Intelligence/Wisdom learning hook if applicable;
- completion evidence;
- expiration/interruption rules if relevant.

CAB recommendation: XP is normally debited **when the advancement commits**, not merely when training begins, unless a specific rule explicitly spends XP as part of a failed/consumptive learning attempt.

### 4.6 Intelligence and Wisdom faster-learning hook

The owner requires high Intelligence and/or Wisdom to represent faster learning while rejecting ordinary global percentage XP multipliers.

CAB-04 places that effect on the **learning/development process**, not the XP award stream.

Recommended architecture:

- analytical, technical, scholarly and memory-heavy learning can reference an Intelligence learning hook;
- experiential, perceptual, judgment, instinctive or contemplative learning can reference a Wisdom learning hook;
- an owning rule identifies the relevant learning mode/attribute;
- both attributes do not automatically stack merely because both are high;
- exact thresholds/formulas are deferred to CAB-10 and pacing validation to CAB-16/17.

This lets a high-Intelligence or high-Wisdom Character complete appropriate learning requirements faster without giving that Character permanently larger XP awards for every adventure.

### 4.7 Grants — why a Character receives something without ordinary purchase

Every grant must record a grant reason/type. CAB-04 distinguishes at least:

- `creation_grant`;
- `source_grant` — species, form, background, tree, Ability, item, condition, etc.;
- `campaign_grant`;
- `milestone_grant`;
- `temporary_grant`;
- `replacement_or_upgrade_grant`;
- `migration_or_correction_grant`.

A grant may make final XP cost zero. That does **not** mean every other gate disappears.

Recommended default:

- cost is bypassed/waived when the grant says the selection is free;
- a grant satisfies eligibility when the grant source itself establishes eligibility (for example, the correct Species granting its own innate feature);
- prerequisites, exclusions or learning requirements are bypassed only if the granting rule explicitly establishes, substitutes for or waives them;
- temporary grants retain activation/expiration behavior and do not silently become permanently purchased nodes.

### 4.8 Special acquisition — opportunity rather than price

Some abilities should not appear as ordinary shopping-list selections even though they may eventually cost XP.

Architecture supports acquisition channels such as:

- creation-only innate opening;
- teacher/mentor access;
- faction/order induction;
- exposure/acclimation;
- transformation/implant/symbiosis;
- artifact bond;
- research discovery;
- narrative milestone/ordeal;
- Campaign-awarded opportunity.

Acquisition produces or changes eligibility/readiness. It is not inherently an XP multiplier or discount. CAB-09 owns final rules.

## 5. Advancement state model

An option visible to a Character may project one of these explanatory states:

- `hidden_or_unauthorized` — caller may not discover it;
- `unavailable_source` — source/entitlement/rules-profile unavailable;
- `ineligible` — Character fails acquisition/compatibility rule;
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

The UI/rules engine should explain **why** an option is blocked rather than returning a generic “not enough XP” state.

## 6. Advancement transaction

### Stage 1 — inspect

Player inspects an option with cost, prerequisites, eligibility, tier state, learning requirement, grants, exclusions and source links.

### Stage 2 — readiness evaluation

System evaluates authority, availability, eligibility, prerequisites, tier/depth access and learning/acquisition readiness.

If a learning project is required but incomplete, the Character can begin/continue that project but cannot yet commit the permanent advancement unless the owning rule permits provisional use.

### Stage 3 — proposal and cost ledger

When readiness gates permit selection, create an advancement proposal containing:

- option stable ID/version;
- before-state version;
- evaluated eligibility/prerequisite/tier/learning evidence;
- base/final XP cost;
- grants/waivers/substitutions;
- conflicts/exclusions;
- resulting grants/effects;
- source/rules profile;
- approval requirement.

### Stage 4 — authoritative revalidation

Immediately before commit, revalidate current Character version, XP balance, prerequisites, eligibility, tier state, learning completion, conflicts, entitlements and Campaign policy. Client-side preview is never authoritative.

### Stage 5 — approval where required

Campaign policy may require GM approval for some or all advancements. Silence is not approval.

### Stage 6 — exactly-once commit

Accepted advancement:

- debits final XP cost;
- adds the selected progression node/state;
- applies explicit grants/replacements;
- recalculates derived state;
- records before/after evidence and source/provenance;
- appends the immutable advancement event/receipt.

### Stage 7 — dependent-state integrity

A new advancement must not silently delete or deactivate existing choices. If it replaces/conflicts with them, the proposal must show the substitution/replacement explicitly.

Later respec/correction that would invalidate dependents requires an explicit dependency/cascade plan; CAB-19 owns refund and respec economics.

## 7. Architectural decisions CAB-04 can establish without owner gate

The following follow directly from current architecture and prior CAB decisions:

1. XP, eligibility, prerequisites, tier access, learning/acquisition and approval are separate concepts.
2. XP never substitutes for eligibility or prerequisites.
3. Advancement remains event-based, attributable, source-linked and exactly-once.
4. Every granted element retains grant source/reason.
5. Tier access is representable as a distinct state but CAB-05 owns its final default mechanics.
6. Learning/training can be represented as a governed project rather than an XP multiplier.
7. Intelligence/Wisdom faster learning attaches architecturally to learning progress/readiness, not ordinary global XP gain; the exact formula remains later work.
8. Special acquisition is an opportunity/eligibility concept, not merely a higher price.
9. Respec/correction must preserve history and cannot silently cascade-delete dependents.

## 8. Owner gates

CAB-04 still exposes four policy choices that materially affect CAB-05 and later calibration:

1. whether a universal prior-tier quantity gate exists at all;
2. how broadly learning/training projects apply to post-creation advancement;
3. confirmation that Intelligence/Wisdom affects learning progress rather than XP awards/costs;
4. default grant-bypass semantics.

They are recorded in `CAB-04_OWNER_QUESTIONNAIRE.md`.

## 9. Forward routing

- five-tier semantics and tier access defaults -> CAB-05;
- XP price calibration -> CAB-06;
- acquisition/eligibility taxonomy -> CAB-09;
- Intelligence/Wisdom learning formula plus attribute/skill interaction -> CAB-10;
- ability corpus/tree audit -> CAB-11/CAB-12;
- progression pacing and learning-duration validation -> CAB-16;
- XP awards -> CAB-17;
- long-campaign learning divergence -> CAB-18;
- respec/correction/migration -> CAB-19.
