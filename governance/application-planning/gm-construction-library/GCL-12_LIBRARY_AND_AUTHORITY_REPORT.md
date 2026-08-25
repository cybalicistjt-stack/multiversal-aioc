# GCL-12 — Campaign Architecture Library

## Result

GCL-12 builds a deterministic, parameterized campaign-architecture library containing **176 materialized structures**: **22 campaign families × 8 architecture patterns**.

The 22 families directly cover the roadmap requirement: episodic, serial, sandbox, faction, villain, exploration, mystery, political, military, survival, settlement, mercantile, academy, resistance, dynasty, generational, time-travel, multiversal, cozy, rotating-cast, asynchronous and anthology campaigns.

The eight structural patterns are modular arcs, escalating serial continuity, hub-and-spoke, open-thread networks, fronts-and-clocks, seasons-and-milestones, legacy turnover and rotating focus.

## Product intent

GCL-12 lets a GM start with a campaign-scale need instead of a blank page. Every record supports both:

- **ready-to-use** projection — a bounded structural starting point; and
- **construction-material** projection — replaceable campaign parts for remixing.

The library provides controlled campaign phase roles, component slots, cadence modes, continuity modes, recovery modes, and endpoint/renewal modes. It is intentionally genre-neutral; GCL-15 will own later genre/tone transformation grammar.

## Authority boundaries

GCL-12 is a planning/content substrate only.

- **MV-IA-F005/A5** remains authoritative for Campaign, Scene and Session identities/state, memberships, roles, Character control, launch snapshots, Events and projections.
- **D28** remains authoritative for Adventure identities and incorporated Adventure truth.
- **CSW-05** remains pre-authoritative narrative/plot planning authority.
- Existing **world/reality/canon authorities** retain World, Reality, Branch, history, timeline and promoted setting truth.
- **Time-travel** records may organize governed temporal material but may not invent causality, paradox, branching, rewrite or temporal-resolution mechanics.
- **Multiversal** records may organize cross-reality campaign preparation but may not create World/Reality/Branch identities or assert compatibility.
- **Asynchronous** records describe preparation cadence only; they do not schedule people, grant permissions, append Events or create persistent runtime state.
- **Cozy, mercantile and settlement** records may propose rhythms and projects but do not mutate economy, market, relationship, settlement or world-state systems.
- AI remains optional, proposal-only and authorization-filtered.

## Deterministic proof

The compact library is encoded as `gcl12-parametric-campaign-architecture-matrix-v1` with no hidden defaults. Materialization order is campaign family first and architecture pattern second, producing stable IDs `GCL12-{family_index:02d}-{pattern_index:02d}`.

The exact library byte stream is digest-bound in the manifest with SHA-256:

`2da0ce698a6459aba06ec11f36f5d92bf29577fd59ff6b076538399b887194d4`

Repository health must reconstruct every one of the 176 records, verify matrix cardinality and digest identity, and reject loss of dual projections or any drift toward live Campaign/world/runtime authority.
