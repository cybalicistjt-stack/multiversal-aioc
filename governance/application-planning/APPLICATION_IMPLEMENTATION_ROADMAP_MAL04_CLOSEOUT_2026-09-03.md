# Application Implementation Roadmap — MAL-04 Closeout

**Date:** 2026-09-03  
**Status:** MAL-04 COMPLETED_VERIFIED; MAL-05 SELECTED_NOT_STARTED  
**Owner and final authority:** John Brandon Turner

## MAL-04 completed evidence

- Governed-start AIOC PR: `930`
- Governed-start AIOC Repository Health: run `33806212574`, job `100817186863`
- Governed-start AIOC merge: `dd99bed7649e6b4453d05344dbf7f2b976db23a4`
- Exact application baseline: `87d08c663606e0d0e1afc9955b069891367b8f83`
- Initial acceptance head: `d780d2d7e4f9fb0f062bc5fac0853d1ddc04d224`
- Initial acceptance run: `33806411769`; exposed one case-sensitive governed proof-marker mismatch before genuine RED
- Genuine RED head: `18959997549427c531a26f3b711c9340cb9d2458`
- Genuine RED run: `33806564900`
- RED selector/repository-health job: `100818335853`
- RED Linux job: `100818380409`
- RED Windows job: `100818380596`
- RED deterministic comparator: `100818551107`
- RED deterministic receipt: `ec284051c9d7b79ae695a5baa027fc64271f249290c593d74cbabfddd4f4061d`
- Production contract/panel introduction: atomic
- Final validated head: `b5a6193dd50ae9831eec03b62240b477571e5021`
- Final run: `33806823707`
- Final selector/repository-health job: `100819175197`
- Final Linux job: `100819212041`
- Final Windows job: `100819212005`
- Final deterministic comparator: `100819391588`
- Final deterministic receipt: `e76f63502ca8485cc883cc30f34b2c2af25a8bdf85f69b42d10b35412ec0a81b`
- Linux artifact: `9913245504`, zip SHA-256 `b442449c5a1af7211a0f6ff9610f2511b147132df2b0b7555feb1c5004b96e7f`
- Windows artifact: `9913249814`, zip SHA-256 `3e422fc91d69413b1b363d656226d6e06d4f3a17ac16d148f84ed458959585b2`
- Comparison artifact: `9913257423`, zip SHA-256 `60d463206cf542cb1694b12bc1790c0892ffbcb69e219878647151946ae958e5`
- Application PR: `399`
- Application merge: `d0f246ea192ccaf964abb66756f06de454a02ecd`
- Historical predecessor profile fanout: `0`
- Unchanged-evidence reruns: `0`
- No-progress cycles: `0`
- Post-merge stale-pointer incidents: `0`

MAL-04 freezes original MAL-local interaction, simple-conflict, hazard, pickup-reference and objective primitives over MAL-01..03. Hidden or unauthorized state remains unresolved. Conflict/hazard/pickup/objective progress never mutates canonical Combat, Character, World, Inventory, Event, Project, progression or reward truth.

## Convergence

MAL-04 completed in one owner execution cycle. Governed start required no repository-state repair. One validation-contract/acceptance-marker repair occurred before genuine RED. The first production head passed the complete declared final gate without feature repair. Diagnostic mode was not entered.

## Strict successor

MAL-05 — NPC/Enemy Behavior & Tiny State Machines — is selected from exact application main `d0f246ea192ccaf964abb66756f06de454a02ecd` with:

- state: `selected_not_started`
- implementation branch: `null`
- implementation authority: `false`

A future owner `Continue` must perform MAL-05 governed start before any MAL-05 application mutation. Canonical NPC/Character, Combat, Inventory, Action/Event, World/Scene, Project/progression and Permission owners remain authoritative. MAL-06+, ALP-01+, provider activation, tester distribution, release and deployment remain unauthorized.
