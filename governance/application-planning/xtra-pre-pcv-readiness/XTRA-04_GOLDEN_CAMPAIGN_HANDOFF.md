# XTRA-04 — Source-Grounded Golden Campaign / PCV Handoff

**Status:** versioned pre-PCV first-party fixture and acceptance specification; NOT playable certification.  
**Evidence basis:** current AIOC Beacon Debt canonical source and its A5 synthetic instantiated fixture, not an independently played Session.  
**Machine-readable companion:** [XTRA-04 Beacon Debt Golden Campaign Fixture](XTRA-04_BEACON_DEBT_GOLDEN_CAMPAIGN_FIXTURE_v1.0.0.json).

## Why this fixture

Use the existing **The Beacon Debt — Deterministic Golden Test**, in **Havalaea / Vertigon**, instead of adding an invented adventure. The canonical owner-approved mechanics are explicitly **noncombat**, with packet-local authored targets, no damage/Conditions, and no real two-human player bindings. The AIOC `evidence/content-pipeline/beacon-debt-runtime-instantiated.json` already describes a deterministic A5 Campaign fixture with an immutable launch snapshot and 5 source-pinned scenes, but `playSequenceExecuted=false`, `productionPersistentRuntimeStateCreated=false`, and `characterBindings=[]`. Treat it as input evidence, not successful gameplay.

The exact app/main and AIOC/source reference and blob digests appear in the companion JSON. Source identity, not an assistant-authored mechanics substitution, controls this handoff.

## Playable-path preparation — five stages

| Order | Scene | Type | Source-driven action / observation | Future PCV acceptance |
|---|---|---|---|---|
| 1 | **Gate Pressure** (East Gate Interchange) | Social encounter | Request Priority Exception; source packet target **15**, deterministic input total **15**. The listed success effects are an AccessGranted event draft and displaced-traveler pressure advance, subject to A6 owner approval. | Role-verified GM/Player action proposal; current permission check; exactly one accepted effect and hidden GM truth protected |
| 2 | **Damaged Crossing** (Eastern Bridge) | Exploration | Navigate Transit Crossflow; target **12**, deterministic total **12**; success has **no automatic effect** listed. The bridge starts damaged in a *synthetic* state; no damage is added by this fixture. | Persist exploration progression and route state without inventing new consequences |
| 3 | **Beacon Restoration** | Technical | Restore East Route Beacon; target **15**, input **15**; success authors a RouteBeaconFunctionRestored event *draft*, not direct game-state mutation. | Verified current actor/GM/event owner approves and persists result once |
| 4 | **Listening Market Investigation** | Investigation | Governed discovery of map-leverage clues. `CF-01..CF-06` are hidden initially; **no clue has yet been revealed**. Do not infer that reaching the Scene publishes GM-only secrets. | Reveal only after real authorized discovery event; private projection never leaks before it |
| 5 | **Consequence / Return** | Consequence/continuity | Review any *actual* accepted Events, resource clocks, and revealed facts, then preserve next-session state. No source document claims this happened. | Reconnect and recover durable authorized results on independent devices |

**Scene graph:** Gate Pressure → Damaged Crossing → Beacon Restoration → Listening Market Investigation → Consequence/Return. Source A5 snapshots already hold the exact nodes, map alternatives and next-scene references.

## Starting fixture and permissions

- Owner fixture subject: `subject:beacon-debt-golden-gm` with **one** synthetic GM membership; there is **no current Player binding**, and no persistent character. Real Player and GM identities must come from A3/PCV-03F and A5, not from the fixture.
- Resource clocks start as synthetic values `route-deterioration=1/4` and `refugee-arrival-pressure=1/4`. Effects are bounded owner definitions; predicted effects are **NOT_RUN** and cannot be entered into canonical history by this XTRA file.
- World `world:havalaea@1.0.0`, Setting `setting:vertigon@1.0.0`, Adventure `mv.adventure.beacon-debt.module@1.0.2`, rules `mv.adventure.beacon-debt.rules.golden-test-core@1.0.0`.
- All five scenes have **gridless semantic-location alternatives** and no required media file. This is a legitimate accessible nonvisual fixture, *not* cleared artwork.
- Default permission: GM-only truth until solved; initially revealed clues empty. One visible fact is that the bridge starts damaged; underlying story associations remain protected until appropriate reveal.
- Packet-local total 12 or 15 is a deterministic input for the harness; it is not a universal Difficulty Class or character statistic. No combat, damage, conditions or automatic mutable owner event is authored.

## Non-happy paths and reviewer checks

The companion manifest declares six **NOT_RUN** negative cases: wrong viewer/hidden clue; duplicate action or stale checkpoint; bad pack/digest; unauthenticated synthetic subject; absent media alternative; and unauthorized extrapolation from local check totals.

A reviewer should use the original A5 fixture and canonical mechanics to verify: exact source object ID/version, action success/failure effect reference, actor authority, GM action decision, hidden projection and replay behavior. A source-level verifier ensures the manifest matches the source files; it does not fake backend execution.

## Explicit incomplete product obligations

This fixture is a **noncombat/social encounter** and therefore cannot satisfy the independent combat encounter required by **PCV-04** and **PCV-10**. The full two-human campaign must additionally demonstrate real Character bindings, inventory/resource change, meaningful combat, a suitable first-party asset set, cross-device authorization/reconnect, installed Windows/Android and independent human observations. **PCV-06** also separately requires its gaming/wagering evidence; nothing in this fixture enables real-money stakes.

Commercial/redistribution license clearance is **unverified** for the complete asset chain even when the authored game records carry approved-canon status. XTRA-05 owns the rights/visual/audio coverage audit. This packet has no new art, AI generation or pack distribution rights.

## Handoff acceptance boundaries

- **XTRA-04 may close** when the source-linked versioned manifest, human review and deterministic source-consistency checks are published, with all real-runtime requirements labeled **BLOCKED/NOT_RUN**.
- **PCV-03F** must independently install and prove authenticated roles, server-authoritative Session, idempotency and reconnect.
- **PCV-04/05** may then consume this fixture as a test preparation input under their own activation and add the missing combat/noncombat playable proof.
- **PCV-09/10/MTLC-14** retain their installed UI, accessibility, asset, lifecycle, two-human and measurable evidence gates.
- **XTRA-05** must disposition every required game asset, media, user right, lineage and alternative; no licence may be inferred solely from content canonization.

No live Campaign or Scene was created by this XTRA document; no Player secret was revealed; no application code, parent lane or production entitlement was modified.
