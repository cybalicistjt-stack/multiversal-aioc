# CAB-09 — Acquisition & Eligibility

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-09  
**State:** `completed_verified` analysis; owner-delegated recommendations recorded separately  
**Owner/final authority:** John Brandon Turner

## 1. Purpose

Define how a Character becomes **eligible for** and then **actually acquires** permanent or conditional progression across ordinary Ability trees, Species/innate options, environmental/adaptation content, Prestige, factions/orders, professions/crafting, magic/spells, forms/transformations, implants/relics/symbiotes, milestone/narrative rewards, companions/mounts/familiars/pets, and other special progression.

CAB-09 does not collapse acquisition into XP affordability. It refines CAB-04's advancement gate architecture and preserves CAB-05 through CAB-08 tier, pricing, action-economy, and interaction rules.

## 2. Core distinction

> **Eligibility is permission to receive an option. Acquisition is the governed event/process that makes the option owned, granted, active, learned, bonded, installed, inducted, or otherwise available to the Character.**

These are not the same thing.

Examples:

- being a member of a Species may make a Species Perk eligible without automatically granting it;
- a biological trait may be automatically granted by Species identity rather than purchased;
- being in a desert may make a situational ability usable without permanently teaching it;
- exposure to an environment may establish an acquisition opportunity without completing acclimation;
- faction membership may open a training tree without granting every faction Ability;
- satisfying Prestige entry requirements may make Tier-3 entry available without granting the first Prestige Ability;
- a spellcasting archetype may establish access to a spell list while individual spell knowledge/capacity follows the owning magic rule;
- a creature may be profile-eligible as a mount/familiar/companion without a live bond, ownership, training, consent, or placement relationship.

XP is evaluated later as affordability unless the acquisition mode explicitly grants or waives cost.

## 3. Evidence boundary

The bounded portable corpus contains distinct source families that cannot responsibly share one acquisition rule:

- `Species_Innate_Abilities.csv`: 2,203 rows, sourced as 260 Species Perks, 539 Innate Abilities, and 1,404 Elementalist rows;
- `Magic_Faction_Abilities.csv`: 118 rows across magic specializations, Shamanism/Voodoo, Chaos Magic, Sacred Order, Scripts/Macros, and faction references;
- `Prestige_Env_Abilities.csv`: 1,018 rows, including 296 Environment-Based Ability rows and 192 Prestige-tree rows among other special families;
- `Profession_Crafting_Abilities.csv`: 221 rows across crafting/repair/enchanting, business, alchemy, cooking, animal handling, mining, chemistry, and trade;
- `Magic_Spells.csv`: 385 structured spells whose source field states the spell itself costs 0 XP while XP purchases spell slots/ready-known capacity under archetype rules.

PPIA-05 further establishes that mixed dataset membership, naming, adjacency, or a `Species Perk`/`Innate Ability` label does not by itself prove immutable biology. CEW-11 establishes that mount/pet/familiar/companion eligibility does not create ownership, bonding, taming, training, obedience, placement, or consent.

CAB-09 therefore governs **acquisition mode explicitly**, rather than guessing it from dataset, source family, name, or price.

## 4. Acquisition-mode taxonomy

Every permanent or conditional Character progression option should identify one or more acquisition modes.

### 4.1 Ordinary purchase

`ordinary_purchase`

The Character is already eligible, satisfies prerequisites/tier/learning rules, and pays the applicable XP debit at commit.

Typical use: ordinary Ability-tree nodes after the progression is legitimately open.

### 4.2 Creation selection

`creation_selection`

The option may be chosen only during Character creation or during an explicitly authorized rebuild/conversion window.

Creation-only status is an acquisition rule, not a price multiplier. A creation-only option does **not** become an ordinary post-creation purchase merely because the Character later has enough XP.

### 4.3 Automatic source grant

`source_grant`

The owning source directly grants the capability because the Character possesses a qualifying identity/state.

Examples may include explicit Species biology, a form's native trait package, or a Campaign/milestone grant.

Actual XP debit may be zero while CAB Reference Advancement Value remains nonzero.

### 4.4 Source-qualified selection

`source_qualified_selection`

A source relationship makes the Character eligible to choose/purchase from a bounded option set but does not grant all options.

Examples include Species-only perks, archetype-only techniques, faction trees, or profession specializations.

### 4.5 Training / instruction / practice

`training_acquisition`

A mentor, instructor, institution, practice regimen, research process, or other learning project is required before commit.

This uses CAB-04's conditional learning-project architecture and Intelligence/Wisdom learning hook where applicable.

### 4.6 Exposure / acclimation / adaptation

`exposure_acquisition`

The Character must experience or acclimate to a qualifying environment, hazard, condition, or field context before the option becomes ready.

Presence alone does not automatically create permanent ownership unless the owning rule explicitly says it does.

### 4.7 Membership / induction / standing

`membership_acquisition`

Faction, order, organization, school, tradition, office, rank, or standing establishes eligibility or provides the acquisition opportunity.

The acquisition record must distinguish permanent learned capability from benefits that remain dependent on current membership/standing.

### 4.8 Prestige entry

`prestige_entry`

A Prestige progression may legitimately begin at Tier 3. Entry requires its explicit prerequisites/eligibility and the CAB-06 Tier-3 access transaction unless an owning rule grants/substitutes another method. No T1/T2 back-pay is created.

The first Prestige Ability remains a distinct grant or purchase.

### 4.9 Archetype / magic access

`archetype_magic_access`

Spell or magic eligibility is determined by the owning archetype/school/focus rules, minimum caster tier, source availability, and any learning/acquisition requirement.

For the current structured 385-spell surface, the spell itself has 0 direct learning XP; XP buys spell slots/ready-known capacity under the owning archetype rules. CAB-09 does not convert those spells into ordinary per-spell XP purchases.

### 4.10 Bond / installation / attunement

`bonded_or_installed_acquisition`

Implants, symbiotes, relics, artifacts, bonded objects, cybernetics, or similar external/installed sources may establish eligibility or grant capability through installation, attunement, bonding, possession, or another owning workflow.

The Character record must distinguish:

- permanent Character-owned advancement;
- capability granted by a currently attached/bonded external source;
- suspended/unavailable capability when that dependency is absent;
- historical acquisition/provenance.

### 4.11 Relationship-pathway acquisition

`relationship_pathway_acquisition`

Mount, pet/companion, familiar, work/service partner, or combat-partner eligibility routes through the governing creature/relationship systems. An Ability may create eligibility, capacity, command options, or a supernatural bond opportunity, but **does not by itself create a live creature relationship unless the owning relationship rule says so**.

Person-level/sapient creatures retain voluntary-consent requirements. NPC presentation does not imply ownership or bond state.

### 4.12 Milestone / narrative acquisition

`milestone_or_narrative_acquisition`

An achievement, quest, ordeal, discovery, pact, revelation, Campaign milestone, or GM-awarded opportunity may establish eligibility, readiness, or a grant.

The event must state what it actually changes. A narrative milestone does not silently bypass unrelated biology, exclusions, or prerequisites.

### 4.13 Temporary / state-gated grant

`temporary_state_grant`

A form, Condition, item, scene, environment, vehicle, possession state, or other temporary context may grant an Ability while the state persists.

Temporary access does not silently become permanent ownership or permanent XP value on the Character ledger.

## 5. Eligibility dimensions

Eligibility may evaluate any combination of:

- Species, lineage, subspecies, variant, or explicit biological trait;
- current Form/transformation/body state;
- prior Character creation selection;
- faction/order/archetype/profession membership or standing;
- explicit Prestige-entry requirements;
- environment/exposure/acclimation history;
- milestone, achievement, narrative history, or Campaign flag;
- Skill/Knowledge/proficiency/mastery state;
- Attribute threshold;
- prior Ability/node/stable-ID ownership;
- item/tool/weapon/implant/relic/symbiote possession or installation;
- spellcasting archetype/school/focus and caster tier;
- relationship-pathway eligibility and consent where applicable;
- source/rules-profile availability;
- Campaign permission;
- explicit exclusions/incompatibilities.

Eligibility is not a surcharge and does not reduce direct effect burden merely because it is hard to obtain.

## 6. Species, innate, biology, and form rules

CAB-09 adopts the PPIA-05 separation among biology, Species eligibility/grants, learned/cultural content, forms, and mixed datasets.

### Default

1. **Explicit automatic biological traits** are granted by the qualifying Species/Form source.
2. **Species-qualified options** are only eligible because of Species/lineage identity when the source says so; they are not automatically granted unless stated.
3. A `Species Perk`, `Innate Ability`, dataset location, tree adjacency, or biological-sounding name does not itself prove either automatic grant or immutable biology.
4. A creation-only innate opening cannot ordinarily be purchased after creation unless its owning rule provides a later acquisition path such as transformation, mutation, bioengineering, awakening, implant/symbiosis, Campaign grant, or another explicit exception.
5. Cross-Species acquisition requires an explicit bridge. XP alone does not create another Species' biology.
6. Form-gated Abilities are usable/acquirable only under the form rules that establish eligibility; CAB-08 form exclusivity remains controlling.

## 7. Environment and adaptation rules

Environment-linked content is not automatically biology and is not automatically learned by entering the location.

CAB-09 default:

- current environment may satisfy a **usage context** for an already-owned Ability;
- qualifying exposure may establish **eligibility** or open a learning/acclimation project;
- the owning rule determines when exposure becomes a permanent Adaptation/Ability;
- source-defined temporary environmental grants remain temporary;
- Campaign/GM may explicitly establish that a prior history/background already satisfies required exposure;
- environment-source membership alone does not prove permanent Character acquisition.

This preserves meaningful environmental development without creating "visit biome, receive permanent power" by accident.

## 8. Factions, orders, professions, and Prestige

### Factions and orders

Membership, induction, rank, standing, initiation, or access to instructors may open a progression. They do not automatically grant the entire progression.

For a **learned permanent Ability**, later loss of membership does not erase the learned Character advancement unless the owning rule explicitly makes the capability dependent on continuing affiliation, patronage, equipment, supernatural link, or office.

Loss of membership may still:

- block new faction acquisitions;
- suspend affiliation-dependent grants;
- remove access to trainers/resources/facilities;
- alter narrative/legal/social permissions.

### Professions and crafting

Profession/crafting progression may require Skills, tools, facilities, ingredients, practice, research, or prior techniques in addition to XP. Paying XP does not waive those requirements.

### Prestige

Prestige entry remains a special advanced acquisition event:

1. satisfy explicit entry prerequisites/eligibility;
2. establish legitimate Prestige access at Tier 3;
3. pay/grant/substitute the T3 access event under CAB-06;
4. acquire the first Prestige Ability separately;
5. continue according to the Prestige progression's own requirements.

## 9. Magic and spells

The current structured spell surface is not an ordinary shopping list.

All 385 structured spell records carry archetype access and a minimum caster tier, and state that the spell itself costs **0 XP** while XP purchases slots/ready-known capacity under the archetype rules.

CAB-09 therefore requires magic acquisition to distinguish:

- permission to use the relevant magic/archetype system;
- school/focus/archetype eligibility;
- caster-tier eligibility;
- actual spell discovery/learning/grant where the owning system requires it;
- capacity/slot/ready-known expenditure;
- spell-specific prerequisites/components/rituals where applicable;
- temporary spell access versus permanent known/available state.

CAB does not invent universal per-spell XP prices.

## 10. Assets, implants, symbiotes, relics, and artifacts

A Character may receive capability from an external or installed source without converting the object itself into Character XP property.

The ledger should identify whether a capability is:

- `character_owned_permanent`;
- `externally_granted_attached`;
- `externally_granted_possessed`;
- `bond_dependent`;
- `form_or_state_dependent`;
- `temporary_grant`;
- `historical_unavailable`.

Loss/removal of the dependency may suspend the granted capability without deleting the immutable acquisition/history record. A permanent Character-bound advancement paid in XP remains distinct from ordinary transferable asset value.

## 11. Companions, mounts, familiars, pets, and person-level partners

CAB-09 consumes CEW/CCP relationship authority rather than inventing a parallel acquisition system.

A Character Ability may grant:

- eligibility for a relationship pathway;
- increased companion capacity;
- command/training options;
- familiar-bond capability;
- mount techniques;
- combat coordination benefits.

It does not automatically instantiate a creature, ownership, obedience, training, placement, or consent state unless the governing relationship workflow explicitly does so.

For person-level/sapient creatures, voluntary consent remains mandatory. Havalaea native animal/NPC capability does not convert person-level partners into tameable property.

CAB-07 still evaluates the independent action economy actually added by a companion relationship.

## 12. Source silence and unknown eligibility

**Unknown is first-class.**

When the source does not establish whether an option is grant-only, purchasable, creation-only, Species-gated, exposure-gated, faction-gated, or otherwise acquirable, CAB does not invent access merely because:

- an XP cost exists;
- the Ability appears in a dataset;
- the Character meets the tier;
- the name resembles another Ability;
- the Character is currently in a relevant environment;
- a creature looks suitable as a mount/familiar;
- a source example shows one Character possessing it.

The option remains `acquisition_unresolved` until source authority or a governed CAB/content decision supplies the missing acquisition rule.

## 13. Acquisition-state model

A Character-facing option may project one of the following acquisition states:

- `hidden_or_unauthorized`;
- `source_unavailable`;
- `eligibility_unknown`;
- `ineligible`;
- `eligible_not_acquired`;
- `acquisition_opportunity_required`;
- `learning_or_acclimation_required`;
- `learning_or_acclimation_in_progress`;
- `dependency_required`;
- `tier_or_prerequisite_blocked`;
- `ready_unaffordable`;
- `ready_to_propose`;
- `awaiting_approval`;
- `granted_active`;
- `owned_permanent`;
- `owned_but_state_inactive`;
- `external_grant_suspended`;
- `temporary_active`;
- `historical_unavailable`;
- `acquisition_unresolved`.

The state must expose the actual blocking or granting reason.

## 14. Acquisition evidence receipt

Every consequential acquisition should preserve:

- option stable ID/version;
- acquisition mode;
- qualifying source/rules profile;
- eligibility evidence evaluated;
- prerequisites/tier state;
- learning/exposure/induction/bond/install evidence where applicable;
- external dependency stable IDs where applicable;
- grant/waiver/substitution authority;
- base/reference/final XP values under CAB-06;
- permanence/state-dependency classification;
- GM/Campaign approval or override evidence where applicable;
- before/after Character state;
- timestamp/event ID;
- provenance and correction history.

This makes later respec, membership loss, form changes, item removal, relationship changes, migration, and audit explainable.

## 15. Owner-delegated CAB-09 policy decisions

Under the standing CAB recommendation delegation recorded in `CAB-08_OWNER_DECISIONS_2026-09-05.md`, CAB-09 adopts the following recommendations as owner-approved:

1. **Eligibility does not equal acquisition or ownership.**
2. **Species/innate acquisition distinguishes automatic grants, source-qualified selections, and mixed/non-biological source membership; cross-Species acquisition requires explicit authority.**
3. **Environmental presence does not automatically create permanent advancement; exposure/acclimation must follow an owning acquisition rule.**
4. **Learned faction/order/profession abilities normally persist after membership loss, while affiliation-dependent grants and future acquisition may suspend/close; explicit owning rules can state otherwise.**
5. **Structured spell acquisition preserves archetype/caster-tier access and 0 direct per-spell learning XP; capacity/slots remain the XP-bearing mechanism under owning rules.**
6. **External dependencies and relationship pathways remain distinct from permanent Character ownership; losing a dependency may suspend its grant without deleting history.**
7. **Source silence produces `acquisition_unresolved`, not inferred eligibility or ineligibility.**

Full authority record: `CAB-09_OWNER_DECISIONS_2026-09-05.md`.

## 16. Forward routing

- Attribute/Skill/Knowledge/proficiency acquisition requirements and learning hooks → CAB-10;
- corpus-wide missing/contradictory acquisition metadata → CAB-11;
- progression placement and tree-entry integrity → CAB-12;
- high-risk acquisition combinations, transformations, summons, grants, and dependency loops → CAB-13;
- equal-XP/reference-value effects of grants/special access → CAB-14/15;
- learning/acclimation pacing → CAB-16;
- long-campaign accumulation of special acquisitions → CAB-18;
- correction/respec when eligibility/dependencies change → CAB-19;
- final repair mapping → CAB-22.

## 17. Completion

CAB-09 is `completed_verified` under the owner's standing CAB recommendation delegation.

**Exact successor:** **CAB-10 — Attributes, Skills & Proficiencies** — `selected_not_started`.