# Multiversal Intrinsic, Affinity & Compatibility System — Item Preparation Step 4

**Status:** future Internal Alpha preparation only  
**Version:** 0.4.0  
**Current-build impact:** none

## Purpose

This layer prevents Multiversal from turning setting compatibility into thousands of repetitive genre tags. It distinguishes **what an item inherently is**, **what fictional contexts it strongly evokes**, and **whether it can actually exist/function inside a particular campaign or setting profile**.

The system is additive. Existing `Genre`, technology/tier, environment, rarity, legality, cost, and domain-native mechanics remain preserved and authoritative for their current purposes.

## Core distinction

### Intrinsic classification

Intrinsic assertions describe the item itself or a real requirement of its operation. Examples include a cybernetic implant requiring a compatible host/interface, a runic artifact being intrinsically arcane/runic, or an EVA module requiring a supported suit mount.

Intrinsic data is sparse and factual. It is not an exhaustive list of worlds in which the item might appear.

### Affinity

Affinity says that an item is **especially characteristic of** a setting family, genre tradition, era, environment, tone, or play context. Affinity is multi-select and nonexclusive.

A revolver can have a strong Western affinity without being forbidden in horror, contemporary, superhero, time-travel, or multiversal campaigns.

### Compatibility

Compatibility is normally **computed**, not stored as a giant list of genres. It evaluates the item's hard requirements against a campaign/setting profile and then applies governed exceptions.

Compatibility does not mean common, legal, cheap, available, or narratively important. Those are separate systems.

## Four compatibility dimensions

1. **Existence compatibility** — can the item's required technological/power basis exist in this setting as itself?
2. **Operational compatibility** — can it function with the available environment, host, interfaces, infrastructure, power, fuel, consumables, etc.?
3. **Rules compatibility** — are the required mechanics/rules modules enabled so the item can be resolved correctly?
4. **Contextual fit** — does the campaign/setting profile include, exclude, or strongly favor the item after affinity and explicit rules are considered?

The overall result is one of: native-compatible, conditional, adapted, intrinsically incompatible, explicitly excluded, explicitly included, unknown, or not evaluated.

## Compatibility is not exhaustive tagging

A mundane rope should not need `Fantasy`, `Horror`, `Western`, `Contemporary`, `Post-Apocalyptic`, `Space Opera`, and dozens of other tags. If it has no hard setting-specific requirement, compatibility can be inferred broadly when a setting profile is evaluated.

This is why `All Genres` is preserved as a **source compatibility signal**, not promoted into the genre taxonomy.

## Affinity examples

- A historically styled revolver may have Western/Frontier affinity while retaining broad mechanical compatibility.
- A cyberdeck may have Cyberpunk affinity and also carry intrinsic Digital/Networked technology requirements.
- A potion may have Fantasy/Alchemy affinity while its actual existence compatibility depends on whether the profile permits the Alchemical or Arcane paradigm represented by the item.
- Arctic survival gear may have Arctic + Survival affinity but can still exist elsewhere; environment affinity is not an existence prohibition.

## Explicit profile exceptions

Campaigns/settings may define governed:

- **Explicit Include** — intentionally allow content despite uncertain/narrow contextual fit.
- **Explicit Exclude** — intentionally remove content from that campaign/profile.
- **Conditional Include** — allow only with a stated adaptation, substitution, reskin, infrastructure, or other condition.

An explicit include does not magically make an impossible intrinsic requirement disappear. If the source concept must change, the result is an **adapted** definition linked to the original rather than silently pretending the original item works unchanged.

## Precedence

1. Hard intrinsic conflicts are evaluated first.
2. Contradictory explicit rules stop for review.
3. Explicit exclusions are applied.
4. Explicit/conditional inclusions are applied when physically/mechanically coherent.
5. Operational and rules requirements are evaluated.
6. Remaining compatibility is inferred from profile capabilities.
7. Affinity influences discovery/ranking, not existence by itself.
8. Legacy/current labels remain evidence, never automatic authority over normalized assertions.
9. Insufficient evidence returns `unknown`.

## Current-catalog review

A read-only preview covers **5,389 current records**.

- `63` records carry an explicit `All Genres` source signal.
- `5,060` records carry a more specific Genre source signal and are treated only as future affinity candidates.
- `266` records have no Genre value; absence is not treated as incompatibility.

No row in this preview receives a final compatibility determination. Record-level intrinsic requirements and campaign profiles do not yet exist as canonical data, so pretending to calculate full compatibility now would manufacture information.

## Internal Alpha posture

At implementation time, normalized assertions and profile exceptions should be additive metadata. Compatibility evaluation should be a read/query service before it is allowed to affect content selection or canonical writes. Current source fields stay available for provenance and migration review.
