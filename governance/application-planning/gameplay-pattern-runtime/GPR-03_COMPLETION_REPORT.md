# GPR-03 Completion Report

**Work item:** GPR-03 — Deterministic Entity, Input, Collision & State Kernel  
**Status:** completed_verified  
**Completed:** 2026-09-20  
**Application contract:** `GPR-03.1`

GPR-03 publishes the bounded deterministic gameplay-instance kernel over the GPR-01 registry seam while preserving MRCS definition authority, frozen MAL authority and canonical owner-domain mutation truth.

Causal RED was established by run `35530223806` at `88dc7ccf4d1209b8697f18242a33537bfcc9dbf9`: selector/repository health passed, while Linux and Windows failed the focused GPR-03 test because the production deterministic-kernel seam was absent.

Exact-head GREEN run `35530339162` passed Linux, Windows and deterministic cross-platform comparison at `ef5d69a5e38cf24d05f6517d67ccab58cf3ddab4`. PR #651 was published through READY candidate `GPR-03-app-001` using squash as application main `b82eb6532d9d1b0815836a9ae3e852ac8fff2839`, after a fresh-main no-overlap integration check against `501e4c5c5359d2368f4fb4c835416a35d77aa7e4`.

The implementation separates live GameplayInstance identity from reusable pattern/configuration identity, normalizes raw device controls into semantic commands, ignores presentation-frame order as mechanics truth, deterministically orders semantic transitions, emits collision/trigger results as local outcomes, enforces explicit entity/spawn/transition caps and preserves unsupported/unknown GPR-01 bindings without fallback.

Fresh ROADMAP_DEPENDENCY_GRAPH.json schema 1.0.4 supplies no interstitial override between GPR-03 and its strict successor. GPR-05 — Owner-Domain Gameplay Operation, Objective & Route Runtime — is therefore selected_not_started.
