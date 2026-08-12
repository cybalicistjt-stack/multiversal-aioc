# PPIA-06 — Species Visual & Morphology Source Addendum v0.1.0

**Work item:** PPIA-06 — Character Appearance Creator  
**Status:** bounded corrective/source-foundation addendum; PPIA-06 remains `started`  
**Owner:** John Brandon Turner  
**Source basis:** owner-supplied `Arthold.zip`, owner-supplied newer `Toba-madra vAlpha.mht`, and explicit owner visual-canon decisions from 2026-08-12.

## Purpose

The verified PPIA-06 foundation correctly established renderer-independent semantics, PPIA-05 Species/Form authority, PPIA-03 equipment authority, nonhumanoid support and explicit renderer failure. The newly supplied species corpus demonstrates that the morphology projection must be richer before Inspector/Action/Reference is designed. This addendum corrects that setup without turning PPIA-06 into a biology authoring system.

## Authority rule

1. Species PDFs are canonical written biological sources unless a newer owner source or explicit owner decision supersedes the specific visual point.
2. Owner-created/labeled concept art is strong visual canon and may supplement/override older visual prose when explicitly confirmed.
3. AI-generated images are reference/inspiration only unless explicitly promoted.
4. Explicit owner decisions resolve known conflicts and are recorded as correction evidence for the PPIA-05 morphology projection consumed by PPIA-06.
5. Contradictory artwork never broadens Species canon automatically.

## Corpus covered

The archive contains **27 PDFs** (25 direct Species documents plus `Kola-Ha Bioengineering` and `Species Perks`) and **88 art files**. Every one of the 25 direct Species is represented in `PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json`; every supplied art filename is inventoried in the visual-authority manifest.

## Required architecture corrections

### 1. Morphology graph, not a humanoid slider stack

Appearance consumes a graph capable of required/optional/source-derived body nodes. It must represent ordinary humanoids, insectoid six-limb plans, nested appendages, tails/wings, form-derived anatomy and composite entities. Moravi (2 arms + 4 legs), Vespin (4 arms + 2 legs), Suula (hands nested inside claws) and ManyToms (repeated constituent bodies) are explicit regression anchors.

### 2. Biological visual state is multi-kind

The system distinguishes baseline biology, lineage/variant, species-bounded authored choice, current Form, derived Form, persistent acquired biology, active biological state, one-time transition state, live pose state, Player cosmetic state, presentation wardrobe and actual equipment projection. These states cannot be flattened into one editable appearance record.

### 3. Species-specific customizer behavior

- **Arborae:** four separately customizable seasonal profiles; current season selects the active one.
- **Mythragara:** authored base + animal identity; hybrid appearance derives from them.
- **Kola-Ha:** baseline aquatic morphology is separate from Bioengineering Forms.
- **Suula:** adaptation history leaves nonerasable markers; active Adaptations visibly update current appearance.
- **Nekron:** one-time ascension into Revenant, Sanguivore or Fragmentarii; second customization derives from base.
- **Furashin:** consciously mutable fur supports up to three simultaneous colors plus pattern/texture.
- **ManyToms:** design one identical constituent identity and compose it as one cohesive collective.
- **The Free:** very broad humanoid android grammar, but not arbitrary nonhumanoid topology.

### 4. Wardrobe and equipment are separate channels

PPIA-06 owns a curated **presentation-only wardrobe/gear library** for making a Character look right; those selections do not need to match inventory and grant no mechanics. PPIA-03 remains owner of actual equipment. When actual gear is projected, the renderer uses topology-compatible visual variants where available and explicit fallback where unavailable. Unrestricted pixel-art warping is forbidden.

### 5. Fixed 2D view contract

`pixel-art-v1` uses a fixed **3/4 full-body master view**. While customizing, the Player can switch among full-body 3/4, portrait/zoom and tactical-token presentation. Zooming is allowed; arbitrary rotation/pseudo-3D is not.

## Resolved source conflicts

The conflict register records the owner resolutions for Vespin limb count, Stygian ears/horns/tail/wings, Rakuuta ears/face feathers, Furashin tails/fur control, Kola-Ha baseline tail/fins, Arborae and Gray height contradictions, Toba-Madra ursine supersession, Giantkin lineage names and Orc tusk visibility. No known visual conflict from this review remains unresolved.

## PPIA-05/PPIA-06 boundary

This addendum does not authorize PPIA-06 to invent or mutate biology. Owner corrections are treated as source-correction evidence feeding the authoritative morphology projection. PPIA-06 consumes that resolved projection and owns only allowed appearance choices, presentation semantics, renderer compatibility, accessibility, presets/randomization and visual-only wardrobe.

## Next design gate

Inspector/Action/Reference must consume taxonomy v0.2 and renderer contract v0.2, not the historical v0.1-only shape. The next package must expose species-specific projection groups and action constraints without turning renderer assets into Species definitions.

No application runtime, STAGE-A-A2, release, deployment, tester access, paid service or production credential is activated by this addendum.
