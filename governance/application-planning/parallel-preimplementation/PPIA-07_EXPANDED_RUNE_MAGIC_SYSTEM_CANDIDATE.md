# PPIA-07 Expanded Rune Construction Magic System Candidate

Status: **owner-directed expansion candidate; not final PPIA-07 completion until exact-head validation and merge**

## Decision

The earlier eight-operation-rune grammar was intentionally minimal. The owner has now directed that the rune set be expanded into a fully usable magic system.

The implementation-ready candidate therefore expands the core vocabulary to **34 runes** while retaining the verified compositional model:

- **16 Operation Runes** — what the magic does.
- **18 Essence Runes** — what magical domain, medium, or essence the operation acts through or upon.
- **4 Connectors** remain separate grammar operators: THEN (`>`), WITH (`&`), WHEN (`@`), and IF (`?`).
- Shape, target, range, duration, trigger, condition, magnitude and other parameters remain typed modifier slots rather than multiplying the basic rune count.

This keeps the system learnable: players learn a small set of verbs and a small set of magical nouns, then combine them.

## Source basis and boundary

The retained structured spell catalog contains **385 spells**, ten primary schools, and seven gameplay roles. Normalizing its compound fields produces fourteen recurring effect families and twenty-two recurring subtype families. The expanded vocabulary routes every one of those normalized effect/subtype families without turning individual spells into runes.

Retained source evidence directly supports:

- Creation, Destruction, Void, Perception, Transition, Emotion, Balance, Stasis, Essence and Energy schools;
- damage, healing/restoration, warding, creation/summoning, perception, movement/planar travel, restraint/control, emotion/mind control, debuff/resource control, illusion/concealment, transformation and countermagic;
- fire, cold, lightning, air, water, earth/mineral, acid, force, radiant/light, void/necrotic, life/essence, psychic/emotion, nature, planar/spatial, temporal, thunder/sound and generic arcane energy;
- spirits and spirit-facing magic through Shamanism/Voodoo/familiar material;
- programmable composition, sequencing, triggers, conditions, shape/radius changes, secondary effects and Resonance through Scripts & Macros;
- rune engraving, enchanting, materials, crafting checks and recovery through crafting/enchanting sources.

The exact 34-rune catalog is **governed design**, not recovered source canon. Source-specific prices, mana, damage, healing, save DCs, durations, ranges, resistance, counterspell, Overreach, Resonance, crafting and XP remain owning-rule inputs.

## The 16 Operation Runes

The verified eight remain unchanged as stable concepts:

`SOURCE, MOVE, SHAPE, BIND, CHANGE, SENSE, WARD, LINK`

Eight new operations complete the major magical effect space:

- `RESTORE` — healing, repair, cleansing, replenishment.
- `UNMAKE` — damage, destruction, unraveling, negation and countermagic routes.
- `VEIL` — concealment, disguise, obscuration and illusion.
- `CALL` — summoning/conjuring referenced creatures, spirits, constructs or effects.
- `BANISH` — dismissal, exile and planar ejection.
- `COMMAND` — emotion, charm, fear, compulsion and mental influence.
- `DRAIN` — resource suppression, weakening, mana/life siphoning and debuff routes.
- `IMBUE` — enchantment, persistent infusion, charging and rune inscription.

These are broad verbs, not named spells. A player can reuse the same operation in many contexts.

## The 18 Essence Runes

Elemental/energy:

`FIRE, COLD, LIGHTNING, AIR, WATER, EARTH, ACID, FORCE, LIGHT, SOUND, ARCANE`

Metaphysical/cosmological:

`VOID, LIFE, MIND, SPIRIT, NATURE, SPACE, TIME`

Essence runes occupy typed payload/domain slots. In canonical text they appear as, for example:

`SOURCE[payload=rune:FIRE]`

An Essence Rune is not a standalone executable operation in v0.2.0. This keeps the AST and player mental model deterministic: **verb + magical noun**.

## Why 34 instead of hundreds

The 385 retained spells do not need 385 rune glyphs. The source spell catalog collapses cleanly into reusable effect and essence families. A small vocabulary produces a much larger construction space:

- Fire bolt: `SOURCE[FIRE] + MOVE`
- Wall of stone: `SOURCE[EARTH] + SHAPE[wall]`
- Heal: `RESTORE[LIFE]`
- Charm: `COMMAND[MIND]`
- Invisibility: `VEIL[LIGHT]`
- Spirit summon: `CALL[SPIRIT]`
- Teleport: `MOVE[SPACE]`
- Time stasis: `BIND[TIME]`
- Dispel: `UNMAKE[ARCANE]`
- Flaming weapon: `IMBUE[FIRE]`
- Life drain: `DRAIN[LIFE] > LINK[self]`

The detailed canonical syntax remains in the JSON contract/reference corpus; the examples above are player-facing shorthand.

## Multi-essence construction

There is no implicit `FIRE+LIGHTNING` payload syntax. Mixed essences use the already verified `WITH` connector and explicit grouping:

`(SOURCE[payload=rune:FIRE]&SOURCE[payload=rune:LIGHTNING])>SHAPE[geometry=storm-field]`

This avoids hidden precedence and allows each branch to carry its own source, target, restrictions and provenance.

## School compatibility

The ten retained magic schools remain school/tradition classifications, not additional mandatory runes. Each school can be expressed through characteristic rune combinations:

- Creation — SOURCE/CALL/SHAPE/IMBUE
- Destruction — UNMAKE/SOURCE/MOVE/DRAIN
- Void — UNMAKE/DRAIN/VEIL/BANISH + VOID
- Perception — SENSE/VEIL/LINK
- Transition — MOVE/CHANGE/CALL/BANISH/LINK + SPACE/TIME
- Emotion — COMMAND/VEIL/SENSE/LINK + MIND
- Balance — RESTORE/DRAIN/LINK/WARD
- Stasis — BIND/WARD/IMBUE + TIME/SPACE/FORCE
- Essence — RESTORE/DRAIN/CHANGE/IMBUE/CALL + LIFE/SPIRIT/VOID/NATURE
- Energy — SOURCE/MOVE/SHAPE/WARD/UNMAKE + elemental/energy essences

School restrictions, archetype access and setting-local rules still come from owning rules.

## Learnability

The UI should not present all 34 glyphs as one undifferentiated wall.

Starter operations: `SOURCE, MOVE, SHAPE, SENSE, WARD, RESTORE`.

Starter essences: `FIRE, COLD, AIR, WATER, EARTH, FORCE, LIGHT, LIFE`.

The remaining runes appear through category browsing, search, progression guidance and context. This is **progressive disclosure**, not a new hard gameplay unlock table.

## Completeness test

The source coverage audit records:

- 385/385 spell rows routed to supported school and gameplay-role families;
- 14/14 normalized effect-family tokens mapped to Operation Runes;
- 22/22 normalized subtype tokens mapped to Essence Runes;
- zero unmapped effect tokens;
- zero unmapped subtype tokens;
- zero source spell IDs marked unroutable at the vocabulary level.

That is a **vocabulary coverage** claim only. Exact spell reconstruction still requires each spell's source fields and owning rules.

## Preserved safeguards

- No spell name automatically becomes a rune.
- Unknown or missing mechanics remain unknown.
- Valid grammar does not imply affordability, success, balance or universal legality.
- PPIA-11 retains final balance calibration.
- PPIA-03 retains Item Definition/instance ownership for inscriptions and enchanted items.
- PPIA-08 retains Campaign/Scene runtime state.
- PPIA-12 retains setting-local rule scope.
- Permission filtering precedes hidden-reference resolution and aggregation.
- Every visual topology has an equivalent ordered textual/nonvisual path.
- Authoritative mutations use expected-version plus operation-ID/idempotent recovery.

## Completion impact

The final PPIA-07 Experience Specification must use the **34-rune v0.2.0 vocabulary**, not freeze the older eight-operation set as the complete rune catalog. The earlier eight-rune artifact remains valuable provenance for how the grammar began, while v0.2.0 is the owner-directed expansion candidate for final implementation-ready design.
