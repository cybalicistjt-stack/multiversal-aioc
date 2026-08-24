# GCL-04 Encounter Library & Authority Report

**Work item:** GCL-04 — Encounter Archetype Library  
**Attempt:** GCL-04-attempt-001  
**Classification:** Governed reusable GM construction content  
**Runtime authority:** none  
**Canon authority:** none  
**Owning-domain acceptance required:** yes

## Result

GCL-04 supplies **360 parameterized encounter archetypes** across thirteen structural families:

- 50 combat
- 50 social
- 50 investigation
- 25 exploration
- 25 travel
- 15 stealth
- 15 chase
- 15 survival
- 15 hazard
- 25 puzzle/problem
- 25 political
- 25 hybrid
- 25 boss/solo structural patterns

This completes the encounter-archetype quantity targets currently listed for the eventual GCL-18 proof packs: 50 combat, 50 social, 50 investigation, 50 exploration/travel, 30 chase/stealth, 30 hazard/survival, 25 puzzle/problem and 25 boss/solo. It also adds political and hybrid coverage. Meeting these quantity targets early does **not** complete GCL-18; the later integrated proof gate still requires the remaining GCL families, discovery/composition behavior and downstream proof.

## Structural doctrine

An encounter archetype is a **shape of play**, not an Encounter instance and not a balance label. Each production record exposes:

- a stable archetype ID and encounter family/form;
- a parameterized structure and setup pattern;
- replaceable governed-object slots;
- intent-first discovery metadata;
- participant-structure guidance without participant truth;
- open objective prompts rather than live objective state;
- explicit references to applicable PPIA-11/F012 pressure dimensions;
- escalation prompts;
- multiple exit vectors;
- multiple alternative approaches;
- downstream composition targets;
- explicit `no_balance_claim` and `no_resolved_outcome` invariants.

The deterministic materialization profile expands compact records into the GCL-01 shared grammar with no hidden defaults.

## F012 / PPIA-11 boundary

GCL-04 does not create or approve Encounter drafts, participant placements, quantities, waves, visibility, analysis snapshots, simulations, approvals or Scene attachments. Those remain MV-IA-F012 responsibilities.

Pressure dimensions are recorded only as **independent structural references**. GCL-04 does not assign magnitudes, weights, target bands, easier/harder directions or any universal scalar. GCL-07 later owns GM-facing difficulty/pressure shaping and must consume PPIA-11/F012 uncertainty rules.

## Boss/solo boundary

The 25 boss/solo records are encounter-structure patterns, not creature transformations. They can organize a focal adversary around environment-, objective-, support- or information-driven beats while preserving the adversary's governed source mechanics. GCL-08 remains the owner for source-respecting adversary role/scaling kits.

GCL-04 therefore may not invent powers, phases, resistances, immunities, action economy, stat multipliers, weaknesses or canon merely to create a boss feel.

## Objective and complication boundary

GCL-04 objective prompts remain open questions needed to make an archetype usable. GCL-05 owns the mature reusable objective/stakes/outcome library. GCL-06 owns controlled complications/escalations/reversals/twists. GCL-04 can compose with both later but does not preempt them.

## AI and authority

The full library is deterministic/manual and useful with zero AI. Optional AI may recommend a compatible archetype or propose values for explicitly open slots only from the authorized projection. It cannot create Encounter truth, approve an Encounter, certify balance, invent missing mechanics or publish/promote content automatically.

## Validation target

Repository-health validation must enforce:

- exact 360-record count;
- exact family counts and stable-prefix agreement;
- GCL-18 encounter proof-target coverage;
- unique stable IDs;
- controlled slot vocabulary and declared placeholders;
- encounter-only scope;
- at least two open objective prompts, two pressure references, one escalation, two exit vectors and two alternative approaches per record;
- pressure references limited to the twelve PPIA-11 dimensions;
- deterministic materialization with no hidden defaults;
- no universal scalar/balance guarantee fields;
- runtime/canon nonauthority;
- no Campaign-local Encounter, difficulty-shaping or adversary-transformation authority;
- boss/solo source-mechanics boundary;
- optional AI only;
- no application critical-path mutation.
