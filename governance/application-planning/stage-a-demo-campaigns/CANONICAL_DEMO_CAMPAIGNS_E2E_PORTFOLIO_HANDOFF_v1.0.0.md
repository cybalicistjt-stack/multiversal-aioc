# Canonical Demo Campaigns + End-to-End Portfolio — Durable Handoff v1.0.0

Status: **PREPARED COMPLETE — CANONICAL DEMO/QA FIXTURES; APPLICATION INTEGRATION DEFERRED**

## Package

`MULTIVERSAL_CANONICAL_DEMO_CAMPAIGNS_E2E_PORTFOLIO_v1.0.0.zip`

SHA-256:

`95c70c8bb83c7cdba56ec10b381fefd0f8abab5fb02fb340b80739e1e755b431`

Validator:

`MULTIVERSAL CANONICAL DEMO CAMPAIGNS + E2E PORTFOLIO v1.0.0: PASS`

Validated totals:

- 4 complete vertical demo Campaigns;
- 57 portable synthetic object records;
- 48 scripted end-to-end steps;
- 52 deterministic checkpoint records;
- 11 shared E2E phases;
- 5 execution modes (demo, onboarding, regression, security, accessibility).

## Canonicality boundary

These Campaigns are **canonical demo/test fixtures**: their stable IDs, exact GM truth, player-visible truth, scripted paths, expected decisions, deterministic checkpoints and reset behavior are governed QA/demo reference evidence.

They are **not canonical Multiversal game lore**. Their names, worlds, NPCs, events and deterministic acceptance outcomes must not be promoted into canonical setting/rules content without a separate content-authority decision.

The deterministic demo-rule profile exists only to make acceptance outcomes reproducible. It does not replace the game framework, balance, real Abilities/Actions/Effects/Conditions, or future owning-domain mechanics.

## Campaign portfolio

### DEMO-01 — Glass Harbor Incident / Meridian Testbed

Primary stress: investigation, social/relationship, hidden clue reveal, combat, shared Asset contention, loot, reconnect.

### DEMO-02 — Ember Road Convoy / Ashen March Testbed

Primary stress: travel, environmental clue, relationship, basic vehicle station/control, resource consumption, combat, cargo/repair, reconnect reauthorization.

### DEMO-03 — Velvet Knives / Nocturne Court Testbed

Primary stress: social/faction authority, protected witness, hidden-information/no-inference, investigation, tactical combat, evidence inventory, reconnect privacy.

### DEMO-04 — Starfall Salvage / Orison Drift Testbed

Primary stress: exploration, environment clue, NPC interaction, bounded project/Asset consumption, vehicle stabilization, combat/hazard, salvage/crafting/inventory, reconnect control.

## Shared vertical contract

Every Campaign exercises:

1. Character creation;
2. Campaign join;
3. Scene/Session open;
4. Investigation;
5. Relationship/Social consequence;
6. Combat or combat/hazard;
7. Loot reveal/acquisition;
8. Inventory/crafting mutation;
9. save/checkpoint;
10. reconnect/current-authority restoration;
11. close/history reconstruction.

Each Campaign contains:

- `OBJECT_REGISTRY.json`;
- `GM_TRUTH.json`;
- `PLAYER_VISIBLE_TRUTH_INITIAL.json`;
- `E2E_SCENARIO.json`;
- `EXPECTED_DECISIONS.csv`;
- `INITIAL_STATE.json`;
- `RESET_STATE.json` with deterministic digest;
- `CHECKPOINTS.json`;
- `DEMO_CARD.md`.

## Authority/privacy requirements

- GM truth must not be delivered to Player clients before authorized reveal/projection.
- Hidden existence/cardinality/topology must not leak through search, counts, graph layout, diagnostics, exports or optional-AI context.
- GM decisions use normal approve/deny/modify-and-approve paths.
- Accepted costs/effects/Assets/history commit atomically through owning-domain authority.
- Duplicate/lost-response retries use operation identity/status lookup rather than duplicate mutation.
- Reconnect reauthorizes current control/role before mutation.
- Offline clients cannot fabricate canonical Events.
- Demo evidence is invalid if expected state is written directly to persistence instead of traversing application/service authority paths.

## Reuse

The earlier `STAGE_A_TESTER_REFERENCE_CAMPAIGN_KIT_v0.1.0.zip` is nested for provenance. Demo 01 upgrades the Glass Harbor concept into the shared demo-portfolio contract without altering the original reference-campaign evidence.

The portfolio is intended for four simultaneous uses:

- guided product demonstration;
- tester onboarding;
- automated/manual regression;
- security/accessibility vertical validation.

## Current implementation authority

Application main at preparation remains:

`dced7f92163050690c807c1fda937146bb8dce85`

**STAGE-A-A2 — Universal Object Experience remains the authorized current application implementation.**

This portfolio does not activate A3-A12 and does not authorize tester access, release, deployment, real-user data, production credentials, paid providers, or canonical content promotion.

## Future integration

As Stage A owning domains become implemented, add thin fixture adapters that preserve these stable demo IDs and semantics. Run each `E2E_SCENARIO.json` through normal application UI/service contracts and compare authoritative receipts/projections against `EXPECTED_DECISIONS.csv` and `CHECKPOINTS.json`.

Do not turn direct database state injection into an E2E substitute.
