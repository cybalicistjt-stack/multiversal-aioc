# CAB-09 — Source Acquisition Audit

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-09  
**Purpose:** identify the acquisition/eligibility patterns that must survive normalization.

## 1. Bounded source surface

The CAB portable Ability corpus contains 4,816 records across five Ability CSVs:

| Source surface | Rows | Acquisition relevance |
|---|---:|---|
| `Abilities_Core.csv` | 1,256 | ordinary Skill/activity and martial progressions; explicit prerequisites, equipment/context, and tier gates occur in-source |
| `Species_Innate_Abilities.csv` | 2,203 | 260 Species Perks, 539 Innate Abilities, 1,404 Elementalist rows; mixed acquisition/biology semantics |
| `Magic_Faction_Abilities.csv` | 118 | magic specializations, Shamanism/Voodoo, Chaos Magic, Sacred Order, Scripts/Macros, faction references |
| `Prestige_Env_Abilities.csv` | 1,018 | includes 296 Environment-Based Ability rows, 192 Prestige-tree rows, plus Divine, performance, psionic, proficiency and special content |
| `Profession_Crafting_Abilities.csv` | 221 | crafting/repair/enchanting, business, alchemy, cooking, animal handling, mining, chemistry, investment/trade |

The structured spell surface separately contains **385 spells**.

## 2. Existing structured gate fields

The Ability CSV schema already distinguishes:

- `Tier_Prerequisites`;
- `Ability_Prerequisites`;
- `Attribute_Requirements`;
- `Situational_Perk_Requirement`;
- `Weapon_or_Tool_Requirement`;
- `Environment_or_Context`;
- `Special_Rules`;
- direct Ability XP, tier-unlock XP and upgrade XP;
- source/provenance.

CAB-04 previously established that these are separate advancement gates. CAB-09 does not repurpose any one of them as a universal acquisition field.

A strict non-placeholder screen of the retained CSV copy found many explicit restrictions, including hundreds of environment/context references and hundreds of tier/prerequisite records. The exact counts depend on whether aggregate phrases such as `Varies by tier; see member records` are treated as meaningful at the aggregate row, so CAB-09 does not promote that screen into a canonical corpus statistic. The stable finding is qualitative: acquisition is already multidimensional and source-specific.

## 3. Species / innate evidence

`Species_Innate_Abilities.csv` is deliberately mixed:

- 260 Species Perk rows;
- 539 Innate Ability rows;
- 1,404 Elementalist rows.

PPIA-05 explicitly rejects automatic promotion from dataset membership to biological fact. It also states that a `Species Perk` can be biological, learned, cultural, mystical, technological, or mixed, and that an `Innate Ability` label requires source/rule interpretation rather than automatic physiology inference.

The retained dataset includes explicit Species prerequisites in some rows, while most rows do not publish a Species prerequisite in the normalized prerequisite field. This makes **source ownership classification** mandatory before assuming automatic grant, Species-only selection, or universal availability.

### CAB-09 consequence

Species/innate content must distinguish at least:

- automatic biological/source grant;
- Species/lineage-qualified selectable option;
- creation-only innate option;
- later-acquirable awakening/adaptation/transformation/implant path;
- non-biological learned/archetype content that merely shares the dataset;
- unresolved acquisition.

## 4. Environment / adaptation evidence

`Prestige_Env_Abilities.csv` contains 296 rows sourced to `Environment-Based Abilities(4).PDF`.

PPIA-05 records that these include social, trade, technical, exploration, and learned environment perks as well as environment-specific capabilities. It explicitly states that environment linkage does not automatically make an Ability a biological Adaptation.

The corpus also contains `Environment_or_Context` values such as underwater, zero-g, wilderness, stations, asteroid fields, gas-giant atmospheres, open space, ruins, battlefield and other locations/states.

### CAB-09 consequence

CAB must distinguish:

- environment as a use condition;
- environment as eligibility evidence;
- environment as an exposure/acclimation requirement;
- environment as a temporary grant source;
- permanent Adaptation acquisition;
- source silence.

Current presence in an environment is insufficient evidence for permanent acquisition unless the owning rule says so.

## 5. Prestige evidence

The retained special surface contains 192 rows sourced to `Prestige Trees(2).PDF`.

Prior CAB authority already establishes:

- Prestige may legitimately start at Tier 3;
- Tiers 1–2 are not missing;
- explicit entry requirements are mandatory;
- entry normally pays the CAB-06 T3 access anchor after requirements;
- no T1/T2 back-pay;
- no automatic extra-tree opening surcharge;
- the first Prestige Ability remains separately granted/purchased.

Source examples include prerequisite packages based on Knowledges, Charisma/social abilities, prior perks, medical/alchemy/support trees, and other advanced development.

### CAB-09 consequence

Prestige acquisition is an **entry transaction**, not merely a Tier-3 Ability purchase.

## 6. Faction/order evidence

The magic/faction surface includes source-backed examples in which organization identity and specialized training matter. Recovered Sacred Order material requires high-ranking status/training/attunement for some content. Warden source evidence states that factions possess specialized Ability trees reflecting their training/tasks.

### CAB-09 consequence

CAB must separate:

- membership/standing as eligibility;
- induction/training as acquisition readiness;
- permanent learned Ability ownership;
- benefits dependent on continuing affiliation, patronage, office, facility, relic or supernatural source;
- future-access closure after membership loss.

Treating every faction Ability as either permanently erased on expulsion or permanently independent of the faction would both be overbroad.

## 7. Profession / crafting evidence

`Profession_Crafting_Abilities.csv` contains 221 rows from crafting/repair/enchanting, business, alchemy, cooking, animal training, mining, chemistry and investment/trade sources.

The source surface includes tool, ingredient, Skill/check, prior-tree and situational requirements. Examples include proper/rare/enchanted tools, ingredients, and high Skill modifiers.

### CAB-09 consequence

XP purchase cannot bypass the actual craft/profession acquisition requirements. Training, tools, facilities, ingredients, prior Skills/Abilities, and practice can remain independent gates.

## 8. Structured magic/spell evidence

`Magic_Spells.csv` contains 385 records.

All 385 publish:

- an `Archetype_Access` rule;
- a `Minimum_Caster_Tier`;
- `Learning_XP_Cost` stating **0 XP for the spell itself; XP purchases slots or ready-known capacity under the archetype rules**.

The current tier distribution is:

- Tier 1: 192 spells;
- Tier 2: 124;
- Tier 3: 47;
- Tier 4: 11;
- Tier 5: 11.

### CAB-09 consequence

The structured spell catalog cannot be converted into ordinary per-spell shopping merely because CAB uses XP elsewhere. Spell acquisition must preserve archetype eligibility, caster tier, owning learning/discovery semantics, and capacity/slot economics.

## 9. Forms, implants, symbiotes, relics and external dependencies

CAB-04 already recognizes forms/transformation, implants/symbiotes/relics and narrative acquisition as eligibility/acquisition dimensions. PPIA-05 also distinguishes Character body/form state from reusable source Definitions and distinguishes installed/bioengineered/symbiotic systems from baseline Species biology.

### CAB-09 consequence

The advancement ledger needs to distinguish permanent Character ownership from capability projected by a current dependency. Removal/loss may suspend a dependency-granted capability without falsifying acquisition history.

## 10. Companions / mounts / familiars / pets

CEW-11 establishes that mount, pet/companion, familiar, work/service and combat-partner status are **relationship pathways, not creature types**.

CEW-11 explicitly states that profile eligibility does not create:

- ownership;
- bonding;
- taming;
- training;
- obedience;
- placement.

It also makes unknown first-class and preserves voluntary consent for person-level/sapient creatures. Physical capability, intelligence, morphology, source collection membership and NPC presentation do not establish a relationship pathway.

### CAB-09 consequence

Character advancement can grant relationship eligibility/capacity/techniques, but actual relationship formation remains in the governing CEW/CCP workflow. CAB cannot instantiate a creature relationship by purchasing an Ability.

## 11. Cross-source conclusions

The evidence supports these durable conclusions:

1. **There is no single acquisition economy.**
2. **An XP number is not acquisition authority.**
3. **Source-family membership is not enough to infer grant versus purchase versus special access.**
4. **Creation-only, Species, form, environment, membership, training, Prestige, magic, installed-object, relationship and milestone acquisition are materially distinct.**
5. **Temporary dependency grants must not silently become permanent advancement.**
6. **Source silence must remain unknown/unresolved rather than guessed.**
7. **Permanent learned capability and continuing-source-dependent capability need separate lifecycle semantics.**

These findings are implemented in `CAB-09_ACQUISITION_AND_ELIGIBILITY.md` and the machine model.