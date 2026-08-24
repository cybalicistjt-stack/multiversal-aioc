# GCL-10 — Adventure Structure Library

**Work item:** GCL-10  
**Program:** GCL — GM Construction Library  
**Status:** IN PROGRESS — CANDIDATE LIBRARY BUILT  
**Consumes:** GCL-02/03/04/05/06, CSW-05, D28, MV-IA-F005, MV-IA-F012, APM-04  
**Application implementation authority:** NONE

## Decision

GCL-10 supplies reusable **pre-authoritative adventure skeletons**. It composes existing hook, situation, encounter-archetype, objective/stakes and complication material into larger structures without creating a live Adventure, Campaign, Scene, Session or Encounter.

The production library materializes **160 structures** from **20 adventure families × 8 architecture patterns**, exceeding the GCL-18 proof target of at least 50 adventure structures/variants.

### Adventure families

heist; rescue; expedition; siege; mystery case; faction sandbox; survival journey; hunt; political crisis; point crawl; branching dilemma; defense/holdout; infiltration/exfiltration; escort/convoy; exploration/discovery; race/deadline; rebellion/resistance; disaster response; negotiation summit; artifact recovery.

### Architecture patterns

1. linear with offramps;
2. hub and spoke;
3. branch and reconverge;
4. open route network;
5. escalating clock;
6. layered objectives;
7. faction reactive;
8. threshold loop.

A linear structure is allowed. The library does **not** require nonlinear design, but it never interprets a sequence as a mandatory golden path or a single correct solution.

## Modular composition

Every materialized structure exposes replaceable construction slots for:

- hook/premise — GCL-02;
- situation/scene possibility — GCL-03;
- encounter archetype role — GCL-04;
- objective/stakes/outcome structure — GCL-05;
- complication/escalation/reversal — GCL-06;
- branch/route;
- optional content;
- endpoint/aftermath.

These are composition references and prompts. GCL-10 does not mutate predecessor records or silently create missing governed content.

## Dual projections

Every structure supports two first-class projections:

1. **Ready to use** — a bounded adventure skeleton with named phase roles, replaceable component prompts, branch/recovery options and endpoint choices.
2. **Construction material** — each component slot, route relation, phase role, optional element and endpoint is exposed as independently replaceable material with provenance.

Neither projection uses hidden defaults. Missing governed content remains visibly missing until explicitly supplied or proposed.

## CSW-05 / D28 boundary

CSW-05 remains the nonlinear Plot/Adventure/Narrative Design Lab for pre-authoritative hooks, beats, scene/encounter seeds, revelations, choices, consequences, branches, optional content, failure states and endpoints.

GCL-10 may provide a reusable skeleton to that planning environment, but planning structure does not create D28 Adventure identities. D28 remains authoritative for incorporated Adventure structure and governed Adventure truth. Incorporation requires an explicit owning-domain handoff with provenance; later GCL/CSW edits do not silently update an Adventure and later Adventure edits do not silently rewrite the reusable template.

## Campaign / Scene / Session / Encounter boundary

MV-IA-F005/A5 retains authority for Campaign, Scene and Session identities and state. MV-IA-F012 retains authority for real Encounter construction, participants, quantities, objectives, analysis and live Encounter state.

A GCL-10 phase named `pressure` or a component slot named `encounter_archetype` is structural authoring material only. It cannot place participants, create a Scene, schedule a Session, mutate Campaign state, resolve an objective or assert an Encounter result.

## Branches, failure and endpoints

Structures may expose alternate routes, optional detours, choice branches, convergence, bypasses, retreat/regroup, objective reframing and follow-up adventures.

Failure-resistant design does not mean automatic success. Candidate continuations include partial success, cost/delay, alternate approach, scope reduction, retreat/regroup, a new information question, stakeholder shift or a safe stop with a follow-up opportunity.

Endpoint modes include full success, partial success, fail-forward exit, negotiated exit, escape with cost, unresolved continuation, objective reframing and follow-up seed. These are **candidate structural endpoints**, never runtime outcome assertions.

## AutoGM boundary

APM-04 or other AutoGM systems may consume GCL-10 only through explicit adapters and authorized context. GCL-10 does not direct runtime play, choose the players' route, advance a clock, mutate faction state or decide an outcome.

## Provenance and authorization

Governed references and source-backed facts retain provenance. Authored reusable templates, GM customizations, campaign-local adaptations and optional AI candidates remain distinct.

Authorization filtering applies before protected context is used for recommendations, composition, summaries or AI input. GCL-10 creates no hidden-information access merely because a structure has an empty or replaceable slot.

## AI boundary

AI is optional and proposal-only. It may suggest compatible components, variants, routes, optional scenes or alternate endpoints from authorized context. It may not auto-incorporate an Adventure, create D28 identity, choose a canonical branch, mutate live state, invent governing mechanics as fact, claim completeness/quality, or expose unauthorized context.

## Non-authority summary

GCL-10 has no authority to:

- create or mutate D28 Adventure truth;
- create Campaign, Scene, Session or Encounter runtime state;
- force a route, solution or outcome;
- silently turn optional content into a prerequisite;
- guarantee adventure completeness, quality, balance or player behavior;
- direct AutoGM runtime execution;
- mutate the application critical path.
