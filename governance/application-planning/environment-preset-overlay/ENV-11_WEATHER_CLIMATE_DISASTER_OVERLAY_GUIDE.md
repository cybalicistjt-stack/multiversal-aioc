# ENV-11 — Weather, Climate & Disaster Overlay Guide

## Purpose

ENV-11 is the first concrete overlay-content tranche. It turns the ENV-04 overlay resolver into a usable ordinary-weather/natural-disaster library without changing the ENV composition architecture or application runtime.

The library contains **20 reusable overlays**:

1. Heavy Rain
2. Monsoon Regime
3. Fog
4. Thunderstorm
5. Heavy Snow
6. Blizzard
7. Windstorm / Gale
8. Hurricane / Cyclone
9. Tornado
10. Sandstorm / Dust Storm
11. Hailstorm
12. Flood
13. Flash Flood
14. Drought
15. Storm Surge
16. Tsunami / Seiche
17. Wildfire
18. Volcanic Ash
19. Volcanic Eruption
20. Earthquake
21. Avalanche
22. Landslide / Mudslide

> **Correction to the count:** the named list contains 22 ordinary natural-condition identities. The machine-readable library is authoritative and must report the same count before ENV-11 may close. If the library count and this list differ, the regression gate must fail rather than silently choosing one.

## Composition rule

These are conditions applied to an existing archetype/preset/local instance. They are not replacement environment identities.

Examples:

- River / Stream + Heavy Rain + Flood
- Canyon / Badlands + Heavy Rain + Flash Flood
- Taiga / Boreal Forest + Heavy Snow
- Tundra + Blizzard
- Harbor / Dockyards + Hurricane / Cyclone + Storm Surge
- Grassland / Prairie + Drought + Wildfire
- Volcano + Volcanic Eruption + Volcanic Ash
- Alpine / High Mountain + Blizzard + Avalanche
- Coast / Shoreline / Beach + Tsunami / Seiche
- Factory / Refinery + Earthquake

## No hidden event engine

ENV-11 explicitly does **not** turn plausible physical causation into automatic overlay activation.

Heavy Rain does not automatically create Flood. Drought does not automatically create Wildfire. Earthquake does not automatically create Landslide or Tsunami. Hurricane does not automatically create Storm Surge or Tornado. Volcanic Eruption does not automatically create a separate Volcanic Ash activation. Blizzard does not automatically create Avalanche.

This distinction is intentional. A GM, authored event, scenario, future runtime system, or separately governed simulation layer may establish that another condition becomes active. ENV-11 only specifies how already-active conditions compose.

## Effect keys and deduplication

Overlays may overlap mechanically without duplicating effects. Stable effect keys from ENV-04 handle that.

Examples:

- Heavy Rain and Hurricane/Cyclone can both contribute `visibility.precipitation_obscuration`; the resolver uses the declared stack mode rather than applying the same obscuration twice.
- Flood, Flash Flood, Storm Surge and Tsunami/Seiche may all contribute inundation-related movement effects, while each retains unique water-state behavior.
- Windstorm/Gale, Hurricane/Cyclone, Tornado and Blizzard may all contribute high-wind movement complications; explicit supersession and strongest-value rules prevent arbitrary stacking.
- Sandstorm/Dust Storm and Volcanic Ash can both contribute airborne particulate obscuration/load. The particulate effect keys deduplicate while sand abrasion and ash accumulation remain distinct.
- Avalanche and Landslide/Mudslide share mass-movement burial/route-blockage concepts but remain distinct overlays because their applicability and material/context differ.

## Monsoon boundary

`Monsoon Regime` represents an **active seasonal condition**, not a permanent world climate taxonomy. A place where monsoon climate is intrinsic may carry that fact in preset/local climate parameterization. ENV-11 activation is appropriate for the active seasonal regime when its changing water/route/resource consequences matter.

## Preset boundaries preserved

- Floodplain remains a geographic preset and does not imply active Flood.
- Flooded Forest remains a baseline wet environment and does not imply active Flood.
- Sea Ice remains a persistent/seasonal ice preset and does not imply Blizzard or Heavy Snow.
- Sandy Desert and Rocky Desert do not imply Sandstorm/Dust Storm.
- Grassland/Prairie, Savanna and Scrubland/Chaparral do not imply Wildfire or Drought.
- Volcano does not imply Volcanic Eruption or Volcanic Ash.
- Alpine/High Mountain does not imply Avalanche.
- Harbor/Dockyards and Port City do not imply Storm Surge.

## Deferred boundaries

ENV-12 remains authoritative for planetary/physical-condition overlays such as Extreme Heat, Extreme Cold, Low Oxygen, pressure extremes, toxic/corrosive atmosphere, radiation, unusual illumination, altered gravity and vacuum.

ENV-13 remains authoritative for magical, supernatural and multiversal overlays.

ENV-15 remains authoritative for the exact Habitat Signature vocabulary and how these overlays alter ecological suitability. ENV-11 therefore defines no final Habitat Signature fields.

CEW remains authoritative for creature ecology and canonical distribution. No overlay directly creates or removes canonical creatures.

## Application boundary

ENV-11 is content/design authority only. It does not authorize changes to `Multiversal-app`, SCL terrain/runtime mechanics, migrations, encounter runtime, weather simulation, event generation or environment UI.
