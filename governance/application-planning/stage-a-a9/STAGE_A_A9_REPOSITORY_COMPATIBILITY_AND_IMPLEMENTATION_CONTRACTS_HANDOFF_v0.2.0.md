# STAGE-A-A9 Repository Compatibility and Implementation Contracts Handoff v0.2.0

Status: **PREIMPLEMENTATION — NOT ACTIVATED**

Prepared against application main:
`dced7f92163050690c807c1fda937146bb8dce85`

Local artifact:
`STAGE_A_A9_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`

SHA-256:
`2a9a3b41aba8cf4ecf252fc1676b0420c229ac9fab28057c827d15c0251f37a8`

Validator:
**PASS — 31 repository/predecessor anchors; 24 blocking gaps/risks; 10 domain ownership decisions; 32 provider-neutral contracts; 70 exact future path actions covering all 48 REL/FRO/SOC/INV/GLA/NCI source slices; 22 reuse/composition decisions; 26 validation/CI lanes.**

## Compatibility verdict

**COMPATIBLE WITH SEPARATE D24/D25 RUNTIME AND SHARED D05 PROJECTION CONTRACTS.**

The current app repository already provides the correct bounded-domain skeleton but no competing A9 implementation:

- D24 `investigation` is the Investigation source-of-truth boundary;
- D25 `social-relations` is the relationship/faction/social runtime source-of-truth boundary;
- D05 `visibility-projection` owns reusable audience-safe projection behavior;
- D04 `authority-control` remains separate from relationship, faction membership/rank/office, standing and influence;
- persistence, Session command/Event/realtime/reconnect, backup/export and safe observability foundations are reusable.

D24 and D25 public contract/schema/fixture/golden roots are placeholders only on the verified app main.

## Locked architecture rules

1. Do not build one monolithic noncombat domain or shared cross-domain persistence table.
2. D24 and D25 write only their owned canonical persistence. Cross-domain work uses stable references, public contracts, expected versions, reservations, ordered Events and compensation.
3. Existing migration `0001_initial_logical_schema.json` remains immutable. A9 storage is additive and finalized only after A2-A8 predecessor migrations are known.
4. Relationship, faction standing, influence, membership, rank/office, mood, intent, stance, belief, clue, hypothesis, conclusion, permission, ownership and control remain separate concepts/records.
5. F016 is split across stages: A9 operates Campaign faction runtime state; reusable general faction/world authoring remains A10/D29/F015 work.
6. A6 remains the proposal/approval authority for protected sharing and Player-proposed persistent consequences.
7. A7 remains the combat-transition authority. A8 remains Asset/currency/ownership authority. D26 Projects own large permanent political/economic/territorial changes.
8. Social persistent consequences validate through owning-domain adapters and commit as one accepted atomic/compensating Event group or none.
9. Visible clues are not proof of objective truth; Player hypotheses are not promoted to fact by support, links, confidence, votes or graph position.
10. List, outline, table, graph, detail and nonvisual navigation use the same D05-safe semantic node/edge projection.
11. Hidden nodes, edges, endpoints, clues, factions, members, operations, motives and private notes are removed before counts, topology, layout/routing, search, grouping, export, diagnostics, notifications or optional-AI context.
12. Every graph operation has a non-drag keyboard/touch/form equivalent; geometry, color and animation are never authority.
13. Lost responses use original-ID status lookup before retry; reconnect performs P9 repair first, then current authorization/revocation and fresh role-safe projections.
14. Pack update/removal never rewrites or deletes accepted live A9 state; source snapshots, tombstones and history remain.
15. AI is authorized-context-only and draft/summary/organization-only. It has no NPC truth, hidden reveal, social decision, investigation resolution, mutation or canonical authority.

## Repository path plan

Future A9 implementation is mapped into the existing canonical roots:

- `packages/contracts/src/social-relations/**`
- `schemas/domains/social-relations/**`
- `fixtures/domains/social-relations/**`
- `tests/golden/domains/social-relations/**`
- `packages/contracts/src/investigation/**`
- `schemas/domains/investigation/**`
- `fixtures/domains/investigation/**`
- `tests/golden/domains/investigation/**`
- `packages/contracts/src/visibility-projection/**`
- bounded UI composition under `apps/client-ui/src/a9/**`
- focused verifier `tools/verify_stage_a_a9.py`
- focused CI `.github/workflows/validate-stage-a-a9-investigation-social.yml`

The plan covers every preserved source slice:
`REL-S01..08`, `FRO-S01..08`, `SOC-S01..08`, `INV-S01..08`, `GLA-S01..08`, and `NCI-S01..08`.

## Authority holds

- A2 remains the authorized current next application work.
- A3 through A9 remain preparation-only.
- No A9 application implementation branch is created by this handoff.
- No new runtime dependency or production provider is required or authorized.
- No paid service, production credential, real-user data collection, AI NPC authority, canonical promotion, internal-alpha release, production deployment or public release is authorized.

## Exact next preparation step

Prepare **Stage A10 — World Builder and Content Creation** from the completed World/Setting/Adventure/Project design series, preserving A9 Campaign-runtime faction ownership and shifting reusable authoring/provenance workflows into their canonical D29/D07/D18 boundaries without activating A10.
