# OARC-06 Completion Report

**Work item:** OARC-06 — Game-Ready Golden Cases  
**Status:** completed_verified  
**Completed:** 2026-09-20  
**Contract:** `OARC06.GAME_READY_GOLDEN_CORPUS.v1`

OARC-06 executes all six required operational-asset golden roles across the nine required owner-handoff dimensions without creating a duplicate runtime.

Corpus result: **6 cases total; 3 game-ready; 3 blocked-visible-gap**.

Game-ready now:
- MIB-14 Utility Rover — ordinary vehicle;
- MIB-14 Workshop Outpost — fixed base;
- MIB-14 Field Work Platform — mobile-base-role platform, preserving actual owner kind `platform`.

Blocked-visible-gap:
- MCH-0031 Primax RX-07 Hollowstep;
- SCF-0027 Orrukhal Bastion-Class Carrier;
- nested Orrukhal/carried-craft workflow.

The blocked cases all preserve the same material gap: no exact existing MIB-14 operational definition is bound to the source-only Hollowstep/Orrukhal identity. The golden proof does not synthesize an owner definition, reinterpret source units into MIB-14 mechanics, or promote noncanonical campaign scaffolding.

Installed Orrukhal modules remain configuration evidence rather than implied salvage outputs. Source-unspecified fields remain unresolved. MERA/MBES remain future-owner seams only.

Causal RED: run `35536896956` at `df27aa9a5c3ab90b7b93a5b481caca8ecf0ac1cb`. First production candidate run `35537008531` passed focused and regression behavior but caught one test-helper type mismatch at client typecheck. The bounded correction changed only `characterId` to governed `subjectId`. Exact-head governed GREEN: run `35537101123` at `b5ac8bfe87879f466d154622effe62b112cb4674`. Fresh app main had no drift. PR #661 published via squash as application main `9bce9c663bab487a795491ddea8a5ce7bf8d8944`.

OARC-06 intentionally publishes no full-catalog coverage percentage. OARC-07 — Coverage & Gap Certification — is the strict final selected tranche and must carry the three visible golden blockers into the final ledger.
