# Stage A Tester / Reference Campaign Kit — Durable Handoff v0.1.0

Status: **COMPLETE — SYNTHETIC TEST FIXTURE PACKAGE; APPLICATION INTEGRATION DEFERRED**

This handoff closes the owner-approved tester/reference-campaign-kit step that was found missing during the Stage A completion-integrity audit.

## Package

`STAGE_A_TESTER_REFERENCE_CAMPAIGN_KIT_v0.1.0.zip`

SHA-256:

`bea56f266449f8b89d855bca9e36973c20c3dd95dfb79897fe1132c94df457f6`

Validator result:

`STAGE-A TESTER/REFERENCE CAMPAIGN KIT v0.1.0: PASS`

Validated counts:

- 27 portable synthetic records;
- 24 scripted journeys;
- exact 24/24 mapping to IA-D09 `IA09-FX-001` through `IA09-FX-024`;
- 6 role profiles;
- Stage A coverage A2 through A12;
- deterministic reset state;
- synthetic/noncanonical authority preserved.

## Reference fixture

Campaign: **Glass Harbor Incident**

World: **Meridian Testbed**

Session: `ref-session-alpha`

All stable IDs use the `ref-` namespace. All fixture records declare synthetic/test-fixture provenance and `canonical: false`.

The fixture includes bounded examples for:

- Campaign, World, Location, Map and Adventure;
- Characters, NPC and Enemy;
- Scene placements and Session preparation;
- governed Action proposal/approval/GM modification;
- reconnect/status recovery;
- hidden information and no-inference checks;
- Relationship, Faction and Investigation clues;
- combat target/effect resolution;
- Asset transfer contention;
- semantic tactical movement;
- basic Vehicle station/resource operation;
- Campaign-local authoring and unsupported-extension round trip;
- optional AI disabled/unauthorized-provider-failure paths;
- offline mutation denial and stale delegated permission;
- keyboard, screen-reader semantic-equivalent and 200% text journeys;
- release-boundary verification.

## Source authority

The journey catalog maps exactly to the bounded IA-D09 release fixture catalog at:

`governance/application-planning/internal-alpha/IA-D09_FIXTURE_CATALOG.json`

IA-D09 explicitly defines this fixture class as bounded and not a complete-game corpus. The reference Campaign therefore must not replace the A2 11,881-object runtime corpus or broader content validation.

## Security / privacy rule

The portable fixture intentionally contains GM-only facts, an unrevealed clue, hidden enemy/faction details and an unsupported extension payload so later Stage A/A12 regression can prove:

- authorization-before-projection;
- no hidden count/search/graph/AI inference;
- current-authority revalidation after reconnect;
- opaque extension preservation and nonexecution;
- privacy-safe reporting.

No exploit tooling, real credentials, production data or public-target testing is included or authorized.

## Reset / onboarding

The package contains a deterministic initial state, reset digest, checkpoint expectations, a compact story card and a tester quickstart. Reset is scoped only to the synthetic fixture and must never be aimed at production or user data.

## Nonauthorization

This work does **not**:

- implement or activate any application Stage A batch;
- create an application implementation branch;
- authorize tester access;
- authorize real-user data collection;
- authorize production credentials or paid providers;
- authorize release or deployment;
- authorize canonical promotion.

## Current implementation authority

Application main at package preparation:

`dced7f92163050690c807c1fda937146bb8dce85`

**A2 — Universal Object Experience remains the authorized current Stage A implementation.**

A3-A12 preparation work and this reference Campaign kit do not supersede A2.

## Exact next work

Return to the canonical application pointer and begin governed **Stage A A2 — Universal Object Experience** implementation from the ready work order / frozen A2 Sunday-Codex master package. The first implementation slice remains **A2-01** unless current application repository evidence has advanced since this handoff.
