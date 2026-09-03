# ENV-16 — Environment Creature-Discovery Contract & GM Preset Projection — Completion Report

**Program:** ENV — Environment Preset & Overlay  
**Tranche:** ENV-16 — Environment Creature-Discovery Contract & GM Preset Projection  
**Candidate closeout:** ENV-16 is complete at the content-contract level when this exact head passes canonical repository health and is merged without stale-authority conflict. The strict successor is CEW-01.

## Delivered contract

ENV-16 establishes `ENV-CD-1.0`, the provider-neutral content/API seam by which a resolved environment can expose source-supported creature candidates to an authorized GM without inventing creature identity, distribution, frequency, visibility, relationship or encounter state.

The contract consumes `ENV-HS-1.0` and preserves the ENV-15 distinction between ecological suitability and canonical distribution.

## Authority intersection

The projection explicitly intersects:

- ENV resolved composition, active overlays and Habitat Signature;
- CEW/existing creature habitat predicates and ecological fit;
- CEW creature distribution/frequency/season/activity facts as they become available;
- existing World/Reality/Setting/Place authority;
- existing Campaign/GM/visibility authority;
- explicit creature overlay interactions;
- optional externally owned ecology, encounter, NPC and partnership facets.

No new creature, ecology, World, visibility, NPC, mount, pet or familiar ledger is created.

## GM projection

The contract defines explainable GM facets for:

- native/common;
- possible/tolerated;
- migratory/seasonal;
- introduced/invasive;
- rare/exceptional;
- overlay-enabled;
- canonical-presence conflicts;
- excluded/blocked;
- unresolved candidates.

The projection also defines normal, include-blocked and include-unresolved query modes so missing/blocked content can remain visible to authorized GM/content diagnostics rather than silently disappearing.

## Critical conflict rules

- habitat compatibility never manufactures distribution;
- explicit distribution absence blocks habitat-derived presence unless separate authoritative local/campaign placement establishes an introduction;
- explicit canonical presence is preserved with a warning when ecological evidence conflicts instead of being silently deleted;
- temporary overlay/season/activity conditions affect current occurrence without rewriting baseline range;
- campaign/GM visibility can suppress otherwise suitable/distributed candidates;
- material unknowns remain unresolved;
- no hidden numeric discovery score or last-write-wins conflict rule is authorized.

## CEW handoff

ENV-16 intentionally does not pre-populate creature ecology. `ENV-CD-1.0` can operate with partial CEW data because missing material facts fail closed as unresolved.

CEW-01 begins source census and identity recovery. Later CEW tranches populate habitat predicates, distribution, ecology, personhood and partnership facets, and CEW-16 returns the completed creature corpus through this seam.

## Boundaries

ENV-16 grants no `Multiversal-app` implementation authority and performs no runtime/UI/schema/migration/terrain/SCL/encounter mutation. Selecting an environment does not spawn, place, tame, own, bond, mount, familiar-link, NPC-convert, reveal or grant abilities to any creature.

## Artifacts

- `ENV-16_CREATURE_DISCOVERY_PROJECTION_MODEL_v1.0.0.json`
- `ENV-16_ENVIRONMENT_CREATURE_DISCOVERY_CONTRACT.md`
- `ENV-16_DISCOVERY_PROJECTION_EXAMPLES_v1.0.0.json`
- `ENV-16_COMPLETION_REPORT.md`
- `tests/control_plane/test_env16_creature_discovery_projection.py`

## Exact next tranche

`CEW-01 — Creature Source Census & Identity Ledger`
