# GCL-02 — Hook, Premise & Inciting-Situation Library Report

**Work item:** GCL-02  
**Attempt:** GCL-02-attempt-001  
**Status:** in progress — candidate library authored  
**Branch:** `governance/gcl-02-hook-premise-library`

## 1. Purpose

GCL-02 supplies a broad reusable library of reasons for a GM's players to become engaged without forcing the GM to start from a blank page and without turning a hook into a predetermined plot.

The controlling content rule is:

> **A hook creates a reason to engage, not a required solution.**

The library is structural and parameterized. It supplies premise patterns, triggers, open slots, stakes prompts, escalation prompts, open questions, discovery facets and composition targets. The GM or an authorized downstream consumer binds setting- or Campaign-specific people, places, objects, resources, threats and obligations later.

## 2. Source and authority basis

### GCL-01

GCL-01 is the completed shared grammar. GCL-02 inherits stable IDs, explicit versions, typed/open slots, compatibility, provenance, dual ready-to-use/construction-material projections, deterministic/manual composition, conflict preservation and owning-domain acceptance.

GCL-02 does not weaken those rules merely because it is authored library content rather than synthetic fixtures.

### CSW-05

CSW-05 defines a `hook` as a **reason to engage** inside a pre-authoritative nonlinear narrative design lab. Its structural material remains planning/proposal material until an explicit handoff into an owning Adventure/Campaign authority. GCL-02 therefore supplies hook construction material to CSW rather than creating a golden path, resolved plot or canonical branch.

### MV-IA-F005

F005 preserves the difference between reusable Definitions, Campaign-local placements/bindings and live Session state. GCL-02 records are reusable Definitions/construction material only. Selecting a hook may seed a Campaign-local draft, but does not itself create or mutate a Campaign, Scene, launch snapshot or Session.

## 3. Corpus

The v0.1.0 candidate contains **120 reusable hooks** across **12 driver families**, ten hooks per family:

1. disruption/anomaly;
2. obligation/debt;
3. loss/disappearance;
4. opportunity/discovery;
5. threat/deadline;
6. request/patronage;
7. accusation/status;
8. relationship/loyalty;
9. secret/revelation;
10. rivalry/race;
11. arrival/transition;
12. fallout/legacy.

This exceeds the later GCL-18 starter proof target of 100 hooks without claiming that GCL-18 is complete. GCL-18 remains the integrated curation/proof gate across many GCL families.

## 4. Parameterization

Hooks use a controlled shared slot vocabulary such as:

- initiating actor;
- affected actor;
- target;
- location;
- disruption;
- obligation;
- opportunity;
- threat;
- evidence;
- resource;
- relationship;
- rival;
- deadline;
- authority actor;
- past event;
- new arrival.

A premise may say that a known route to `{location}` has vanished or that an `{obligation}` from `{past_event}` has come due, but it does not invent the location, obligation or event. Those remain explicit open bindings until a permitted consumer supplies them.

The validator checks that every placeholder used by a premise/trigger is declared, every declared slot comes from the controlled vocabulary, and every production hook exposes at least one replaceable slot.

## 5. Intent-first discovery

The library is intentionally not designed as a 120-row screen the GM must browse.

Every record carries facets for:

- current construction need;
- play emphasis;
- scope;
- duration band;
- prep depth;
- tone;
- structural genre affinity;
- intent keywords/tags.

This means later GCL-16 discovery can answer requests such as:

- “I need something to start tonight's session.”
- “Give me a social complication that can grow into an adventure.”
- “I need a mystery hook with a relationship angle.”
- “We just finished a major victory; what consequence can start the next arc?”
- “Players ignored the expected lead; give me another open route into the same broad problem.”

Driver-family browsing remains available to expert users, but it is secondary to need-first recommendation.

## 6. Genre strategy

GCL-02 v0.1.0 hooks are deliberately `genre_neutral` structural records. They can later be expressed through fantasy, science fiction, horror, western, superhero, cyberpunk, cozy, historical, modern or Multiversal settings without multiplying near-identical library records.

GCL-15 owns the mature genre/tone reskinning grammar. GCL-02 does not preempt it by baking setting-specific mechanics or canon into hook identity.

## 7. Storage and materialization

The corpus uses two explicit storage forms:

- one small explicit-record shard, useful as a human-readable reference example;
- versioned `gcl02-columnar-v1` packs for the larger corpus.

Columnar storage is only a serialization optimization. Each file declares its ordered column names. A row is first reconstructed into the named compact record; then `GCL-02_HOOK_MATERIALIZATION_PROFILE_v0.1.0.json` deterministically expands that compact record into the GCL-01 reusable template grammar.

There are **no hidden semantic defaults**. Profile-supplied authority/provenance/projection values are explicit versioned inherited data and remain attributable.

## 8. Solution openness

Every record carries `no_prescribed_solution: true`.

The family contract forbids compact fields for:

- required solution;
- canonical outcome;
- mandatory player choice;
- guaranteed resolution.

Hooks may provide stakes and escalation prompts, but these are questions/pressures for the GM to use, replace or ignore. They do not say that players must fight, negotiate, investigate, travel, accept a patron, trust an NPC, discover one clue or choose one branch.

## 9. Downstream composition

The records deliberately expose composition targets rather than complete adventures. Expected consumers include:

- **GCL-03** — turn a hook into a playable situation/scene structure;
- **GCL-05** — attach objectives, stakes and outcome structures;
- **GCL-06** — add or replace complications/escalations;
- **GCL-09** — use evidence/question hooks as mystery/investigation seeds;
- **GCL-10** — place a hook inside a reusable adventure architecture;
- **GCL-12** — use fallout/transition hooks at campaign scale;
- **GCL-13** — bind dramatic roles and relationship situations;
- **GCL-14** — connect fallout and consequences;
- **GCL-15** — reskin structural expression by genre/tone;
- **CSW-05** — seed nonlinear narrative planning;
- **MV-IA-F005** — seed authorized Campaign/Scene drafts through explicit owning-domain actions.

No consumer may treat the GCL record itself as live state.

## 10. AI boundary

The deterministic/manual library is fully useful without AI.

Optional AI may later recommend a compatible hook, propose a value for an explicitly open slot, suggest a variant, or reskin expression. It may only use authorized context, must preserve provenance, and produces proposal-only material. AI cannot select canonical outcomes, infer hidden Campaign facts, or promote the hook into runtime truth.

## 11. Candidate validation gates

Before GCL-02 may be `completed_verified`, the current AIOC repository-health validator must verify at minimum:

- GCL-01 remains `completed_verified`;
- GCL-02 is the active/closing GCL tranche;
- exact 120-record corpus count;
- exact 12-family coverage and 10 records per family;
- unique stable IDs;
- required compact fields;
- deterministic materialization and no hidden defaults;
- controlled slot vocabulary and declared placeholders;
- solution openness and forbidden prescribed-solution fields;
- stakes/escalation/open-question minimums;
- representative discovery breadth;
- `genre_neutral` structural strategy;
- runtime authority remains `none`;
- owning-domain acceptance remains mandatory;
- AI is optional and proposal-only.

Successful exact-head repository-health evidence and merge evidence are required before closeout.
