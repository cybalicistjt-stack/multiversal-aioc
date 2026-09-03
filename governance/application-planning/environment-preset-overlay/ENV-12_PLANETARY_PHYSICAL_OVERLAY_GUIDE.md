# ENV-12 — Planetary & Physical-Condition Overlay Guide

**Program:** ENV — Environment Preset & Overlay  
**Tranche:** ENV-12 — Planetary & Physical-Condition Overlays  
**Application implementation authority:** none

## Purpose

ENV-12 turns the physical-condition portion of the environment framework into reusable overlays that can modify any compatible preset or local environment instance without becoming new base-environment identities.

The retained environment framework permits environment definitions to carry gravity, atmosphere, pressure, light, radiation, temperature/climate and hazards. It separately requires species, characters, creatures, equipment, vehicles, powers and adaptations to be evaluated against the environment rather than copied into ENV records.

ENV-12 therefore defines **environment-side conditions and semantic deltas only**. It does not invent universal damage, fatigue, suffocation, decompression, radiation-dose, carrying-capacity, movement-speed, equipment-failure or adaptation formulas.

## Library

ENV-12 authors 15 reusable overlays:

1. Extreme Heat
2. Extreme Cold
3. Toxic Atmosphere
4. Corrosive Atmosphere
5. Low Oxygen
6. High Pressure
7. Low Pressure
8. Radiation
9. Extreme Darkness
10. Extreme Illumination / Glare
11. Low Gravity
12. High Gravity
13. Zero Gravity
14. Variable / Directional Gravity
15. Vacuum

No presets or archetypes are added. The governed library remains **76 presets / 19 archetypes**.

## Baseline fact versus overlay

A planet, moon, station, cave, underwater region or other setting may have one of these conditions as a persistent local fact. The ENV composition model can still express that fact through an active/default overlay at the relevant local scope. The overlay does not imply that the entire planet or World shares the condition.

Likewise, a condition can be episodic. A pressure failure in one compartment, a radiation event in one zone, a temporary gravity shift, or an unusual heat event can use the same reusable overlay without changing the underlying preset identity.

## Temperature

Extreme Heat and Extreme Cold modify the thermal regime relative to local baseline. They are mutually exclusive only when they claim the same materially uniform scope. A world can contain hot and cold zones at once, and a single environment may have a steep thermal gradient when represented with narrower scopes.

Weather remains separate. A Blizzard from ENV-11 does not automatically activate Extreme Cold, and Extreme Cold does not automatically create Heavy Snow or Blizzard. If both are active, they resolve independently and deduplicate only where they share declared effect keys.

## Atmosphere and oxygen

Atmospheric composition, oxygen availability and pressure are separate facts.

- **Toxic Atmosphere** means hazardous atmospheric constituents are present.
- **Corrosive Atmosphere** means the atmosphere chemically attacks exposed material or organisms.
- **Low Oxygen** means oxygen availability is materially reduced while an atmosphere/breathable medium still exists.
- **Low Pressure** means the pressure regime is reduced; it does not by itself assert atmospheric composition.

These distinctions prevent one vague "hostile atmosphere" flag from collapsing several physically and mechanically different environmental conditions.

## Vacuum

Vacuum is intentionally not implemented as automatic activation of Low Oxygen + Low Pressure. It directly provides its own atmosphere and pressure deltas.

When Vacuum and Low Pressure are both present in the same uniform scope, Vacuum supersedes the duplicate low-pressure contribution. When Vacuum and Low Oxygen are both present, Vacuum supersedes the duplicate oxygen-availability contribution. Toxic Atmosphere and Corrosive Atmosphere require a meaningful atmosphere and therefore conflict with Vacuum in the same materially uniform scope.

This is composition resolution, not event causation. ENV-12 does not simulate a hull breach, decompression event, atmosphere loss, or pressure equalization process.

## Pressure

High Pressure and Low Pressure are relative environmental regimes. ENV-12 deliberately does not invent absolute pressure thresholds or decompression math. Those values require source, setting or later local authority.

The same overlay family can represent atmospheric or hydrostatic pressure as long as the local record qualifies which medium/pressure context is being described.

## Radiation

Radiation represents an elevated environmental radiation field and related exposure/shelter context. It does not establish a universal dose scale, damage progression, mutation table or protection formula.

Existing source-backed environment-to-ability relationships remain separate and are reconciled in ENV-14 rather than inferred from the presence of Radiation.

## Light

Extreme Darkness and Extreme Illumination / Glare are both light-regime overlays. They alter ordinary visual-reference and detection context but do not define a participant's senses, vision modes, equipment, powers or immunity.

They conflict only in the same materially uniform scope. A dark cavern with a localized blinding light source can represent the two through distinct scopes instead of forcing an artificial global choice.

## Gravity

ENV-12 defines four gravity regimes:

- Low Gravity
- High Gravity
- Zero Gravity
- Variable / Directional Gravity

All use the same `gravity.regime` / `movement.gravity_context` semantic seam so they cannot accidentally stack as independent bonuses or penalties in one uniform scope.

Variable / Directional Gravity is included because retained project material contains gravity-shift behavior, while the controlling environment framework already establishes gravity as an environment-owned property domain. ENV-12 does **not** copy any specific gravity-shift die, timing, DC, multiplier or event table into the reusable overlay. Exact patterns and event frequency remain source/local data.

Zero Gravity does not mean "space" and Space / Void does not automatically mean Zero Gravity. A constructed rotating habitat, a magical local effect, a high-acceleration vehicle, or another separately governed condition may establish a different gravity regime.

## Interaction and causation boundary

ENV-12 relations resolve simultaneous conditions. They do not create conditions.

Examples:

- Extreme Heat does not automatically create Wildfire.
- Extreme Cold does not automatically freeze every water source.
- Low Pressure does not automatically create Low Oxygen.
- Low Oxygen does not imply Toxic Atmosphere.
- Radiation does not automatically create mutations, abilities or creature variants.
- Vacuum does not automatically create Zero Gravity.
- Zero Gravity does not automatically create Vacuum.

If future runtime systems simulate those transitions, that requires separate application authority and must consume rather than rewrite this content contract.

## ENV-13 / ENV-14 / ENV-15 / CEW boundaries

ENV-12 does not author Magical Saturation, Magical Dead Zone, Reality Instability, Dimensional Bleed, Portal Activity, Psychic Influence, Corruption, Temporal Instability, Chaos/Foam Influence, Dream Influence or Gehenna conditions. Those remain ENV-13.

Ability/adaptation reconciliation remains ENV-14. Habitat Signature vocabulary remains ENV-15. Creature habitat/distribution/classification remains CEW.

## Provenance

The overlay definitions are owner-authorized content design derived from the approved ENV program and retained environment framework. They do not claim to be recovered source prose or to replace source-specific mechanics. Numeric thresholds, formulas and source-specific behavior remain attached to their actual source/local authority when later reconciled.
