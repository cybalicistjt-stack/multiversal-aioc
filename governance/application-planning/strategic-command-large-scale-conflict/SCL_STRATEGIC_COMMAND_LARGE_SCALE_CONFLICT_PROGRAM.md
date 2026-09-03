# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-04; SCL-05 IN_PROGRESS  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-04 are `completed_verified`. SCL-05 — Morale, Cohesion, Leadership & Discipline — is `in_progress` from exact application main `f85be31982530f5fcc9d8ef9b9ef25e30451923e` on branch `integration/scl-05-morale-cohesion-leadership-discipline` with bounded implementation authority.

The governed start is sealed to completed SCL-01..04, retained `Squad & Fleet.PDF` source profile, ODL-03/04, MIB-09, DPL-12, Character-Actors, Permission/visibility, ordinary Action/Combat/Event owners and the current SCL validation family. No broad historical or connected-system rescan is authorized.

## Frozen SCL-04 contract

SCL-04 freezes phase vocabulary `intake`, `eligibility`, `precedence`, `resolution`, `handoff`, `closed` and outcome vocabulary `ready`, `partial`, `blocked`, `invalid`, `conflict`. It coordinates explicit visible order precedence and Action/Combat/Event handoff requests only. Canonical owner domains execute and commit results exactly once.

## Governed SCL-05 contract

The retained `Squad & Fleet.PDF` source (SHA-256 `20d7a5bbeafb7fccf2213aee5470741cb35760270907ff56e075f86ee83ae8da`) explicitly defines squad/fleet morale checks triggered by losing more than 50% HP or the Fleet Commander, using `d20 + Commander's Leadership modifier` against source DC `15` modified by battlefield conditions. Its ambush example also requires a morale check when the defender loses 25% HP in the first round.

SCL-05 therefore freezes morale trigger vocabulary `hp-loss-over-50-percent`, `fleet-commander-loss`, `ambush-first-round-hp-loss-25-percent` and result vocabulary `not-triggered`, `pending`, `passed`, `failed`, `unknown`, `conflict`, `incompatible`. It generates no random roll. A battlefield DC modification is accepted only from explicit visible source/profile evidence.

The source says failed morale causes reduced efficiency (example `-2` attack rolls) **or** retreat. SCL-05 may preserve both as owner-domain consequence references but cannot choose between them, apply the modifier, force retreat, mutate Action/Combat/Event truth or advance campaign time.

The same source mentions Inspiring Command `+2` to morale rolls, Psychological Warfare reducing enemy morale by `2`, morale boosts restoring `10` morale points and victory by morale reaching `0`, but it does not supply a complete initial/max morale pool or universal accumulation model. Those point statements remain source/profile references only; SCL-05 creates no canonical morale-point ledger or arithmetic pool.

ODL-03 remains authoritative for organization-politics cohesion with profile/context bands `low`, `mixed`, `high`. SCL-05 may expose explicit tactical cohesion evidence using those labels only when visible source/profile/context evidence explicitly designates tactical coordination context. It never derives tactical cohesion from organizational cohesion, formation size, morale, title or hidden data.

Leadership influence requires an explicit visible commander/leader reference plus owner/profile evidence. SCL-03 command roles and ODL-04 roles/delegations identify relationships and scopes but do not manufacture a Leadership modifier. Source-profile leadership modifiers may inform morale checks only when explicit.

The retained source defines no discipline scale, check, threshold or consequence formula. Discipline therefore remains an explicit evidence-resolution surface (`resolved`, `unknown`, `conflict`, `incompatible`) with profile/context/provenance. No universal discipline band or mechanic is invented.

MIB-09 remains authoritative for Relationship/Reputation and Loyalty; Character-Actors retains identity/personality/consent/agency; DPL-12 remains the read-only source/profile fear/stress/sanity/trauma boundary with Condition and other owners retaining live effects. SCL-05 does not automatically convert fear, stress, sanity, trauma, loyalty or hidden relationship evidence into morale/cohesion/discipline state.

Permission/visibility filters before triggers, leadership evidence, morale resolution, cohesion/discipline evidence, consequence references, counts, summaries, search, provenance, deterministic receipts or AI context. Hidden existence/cardinality remains undisclosed.

Resolved SCL-05 outputs may emit read-only Action/Combat/Event handoff requests only. Canonical owner domains decide and commit consequences exactly once; SCL-05 receipts cannot be replayed as world-state truth or double-apply an effect.

AI may advise only where separately governed. SCL-05 invokes no provider and grants no autonomous command, roll generation, adjudication, permission, owner mutation or completion authority. No durable SCL-05 persistence is introduced and migration `0022` remains unreserved.

## Tranches

1. **SCL-01 — Source Inventory, Scale Taxonomy & Authority Map** — completed_verified.
2. **SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model** — completed_verified.
3. **SCL-03 — Command Hierarchy, Roles, Orders & Communication** — completed_verified.
4. **SCL-04 — Command Phases & Deterministic Order Resolution** — completed_verified.
5. **SCL-05 — Morale, Cohesion, Leadership & Discipline** — in_progress under bounded governed implementation.
6. **SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness** — planned.
7. **SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position** — planned.
8. **SCL-08 — Vehicle, Mecha, Ship & Fleet Integration** — planned.
9. **SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery** — planned.
10. **SCL-10 — Faction, Settlement, World & Campaign Consequence Integration** — planned.
11. **SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof** — planned.

## Invariants

- Ordinary Combat/Action/Event and canonical constituent/owner-domain truth remain authoritative.
- SCL-01 through SCL-04 completed contracts remain frozen and implementation authority is retired.
- SCL-05 may resolve explicit source/profile morale-check evidence but cannot execute downstream consequences or create a universal morale pool.
- ODL-03 organization cohesion, ODL-04 role/delegation, MIB-09 relationship/reputation, Character-Actors, DPL-12 and Permission/visibility remain authoritative owner seams.
- Missing discipline mechanics and incomplete morale-pool semantics remain explicit source gaps rather than invented rules.
- Logistics/readiness mechanics remain SCL-06.
- No AI autonomous command/adjudication, owner mutation, hidden-data reveal, duplicate ledger, persistence or migration `0022` is authorized.
