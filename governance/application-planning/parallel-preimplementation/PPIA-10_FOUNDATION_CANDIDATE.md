# PPIA-10 — Relationship, Social & Faction Content Framework Foundation Candidate

Status: **FOUNDATION CANDIDATE — NOT PPIA-10 COMPLETE**

This candidate establishes the source/design foundation for PPIA-10 over the verified PPIA-09→PPIA-10 transition and the existing F009/F010/F016 contracts.

## Verified source boundary

- Retained package SHA-256: `c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec`.
- **5 direct PDFs / 44 visually reviewed pages**.
- **2 direct structured CSVs / 1,374 rows / 94 structurally explicit social-or-faction rows**.
- `Abilities_Core.csv`: 82 Social & Influence records (61 Social Play + 21 Politician).
- `Magic_Faction_Abilities.csv`: 12 faction-related records (11 Sacred Order + 1 Warden tree reference).
- The two ten-page social-status PDFs are near-duplicate variants and are not double-counted as independent authority.

## Foundation model

The taxonomy has **18 semantic layers** and **14 presentation profiles**. It preserves F009's fourteen relationship dimensions and seven reveal layers, F010's social interaction/action/resolution separations, and F016's faction placement/membership/rank/office/standing/influence structures.

The authority matrix defines **15 domain handoffs** so Campaign/Scene/Session, Investigation, World/Setting, NPC, inventory, Condition/status, Project/Contract, Asset/Resource/Location, permissions/recovery, proposal/approval and final balance authority remain explicit.

## Blocking invariants

1. Relationship is directional unless an explicit paired edge exists.
2. Relationship, standing/reputation, influence, social status, mood, intent and stance are distinct.
3. Membership, rank, office, permission, ownership, equipment and progression are distinct.
4. Objective truth, NPC belief, Player belief, claims, rumors, motives, secrets and knowledge are distinct.
5. No universal relationship, standing, influence or social DC scale is invented.
6. Persuasion is not mind control; Insight is not exact hidden-truth revelation; Intimidation is not loyalty.
7. Hidden state is filtered before graph topology, counts, search, exports, notifications, realtime, diagnostics and AI context.
8. Persistent social consequences use accepted atomic Event groups and owning-domain Events.
9. Faction standing changes retain an attributable source Event and plausible information path.
10. External references never transfer Item/NPC/Asset/Resource/Location/Project/Contract ownership into PPIA-10.
11. Source progression never grants membership, rank, office, equipment, ownership or permission automatically.
12. Example DCs, Bond thresholds, reaction bands and standing tracks remain examples/profile data unless explicitly bound.
13. Authoritative mutations require `expected_version` plus `operation_id`; ambiguous results use status/current-version lookup before retry.
14. Graph/canvas state is nonauthoritative and **semantic nonvisual** equivalents are required.
15. AI remains proposal/advisory only and has no irreversible social, NPC, reveal, faction or canonical authority.

## Direct reference material retained

`Factions.PDF` contributes eleven unevenly detailed named organizations suitable for later reference fixtures. `Social Gameplay.PDF` contributes ten social skills, social-status/Bond examples and source-specific mechanical examples. The social-status variants contribute area/community versus interpersonal status semantics and concrete examples, including twenty artisan/craftsman/performer statuses. None of these examples silently become universal framework constants.

## Not complete yet

This milestone does not yet define the full PPIA-10 inspector/action corpus, reference fixtures, integrated workflows, final experience specification or acceptance traceability. PPIA-10 remains `started`.

## Activation boundary

No application runtime, STAGE-A-A2, release, deployment, tester access, paid service or production credential is authorized.
