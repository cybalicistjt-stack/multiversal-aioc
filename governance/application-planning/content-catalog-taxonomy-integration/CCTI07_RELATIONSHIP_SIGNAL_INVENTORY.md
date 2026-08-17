# CCTI-07 — Relationship Signal Inventory

**Mode:** read-only; no relationship promotion.

Selected explicit relationship-bearing fields across the target catalogs contain **63,195 non-empty field occurrences**. High-value structured inputs include:

- EVA Suits: `Mount or Slot`, `Compatibility`, `Power or Consumable` — 430/430 each.
- Ranged Weapons: `Ammo or Power` — 230/230.
- Computers: `Compatibility_C`, `Power_Source`, `Upgrade_Path`, `Interface` — 1,000/1,000 each.
- Symbiotes/Cybernetics: host, need/power, maintenance/bond and upgrade-path fields — 572/572 each.
- Living Spellbooks: suite, bonding, compatibility, upgrade, material/fuel and skill/tool fields — 1,501/1,501 each.
- Vehicles: installed equipment, fuel/energy, upgrade path and maintenance requirements — 1,200/1,200 each.
- Mecha: creator, power, weapons/systems, installed mods, salvage, compatibility and upgrade fields — 2,117/2,117 each.
- Spacecraft: creator, reactor, weapons/systems, installed modules, compatibility and upgrade fields — 2,311/2,311 each.

This proves signal availability, not that every raw string already names a canonical target.

Content V2 already has **216 exact resolved cross-package relationship rows** touching the CCTI target under conservative ID/catalog matching: 189 `PRIMARY_ATTACK_USES` and 27 `CARRIES_EQUIPMENT`.

CCTI-07 must preserve that governed relationship layer and separately parse structured catalog fields into reviewable candidate edges. Candidate edges may resolve only through stable IDs, explicit aliases, source evidence, prepared compatibility/lineage registries, or owner-reviewed decisions.

Prohibited shortcuts: no parentage from name similarity; no manufacturer identity from generic nouns/placeholders; no installed-state claim from definition compatibility; no automatic fuel/ammo/material target from text alone; no silent same-name merging across Item/Vehicle/Mecha/Spacecraft catalogs.
