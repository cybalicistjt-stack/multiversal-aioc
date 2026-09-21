# MSWI-04 Completion Report

**Work item:** MSWI-04 — Ecology Succession, Food-Web, Migration & Population-Band Runtime  
**Status:** completed_verified  
**Application contract:** `MSWI-04.1`  
**Published application merge:** `24681577aca04d05332ec4325bd8d505ee89f330`

MSWI-04 implements bounded campaign-time ecological systemic response over accepted MNCS, World and Environment definitions without creating a second ecology owner.

Causal RED run `35608316999` at `7d32d6c3be9aac990a749bdc1b8b9667c0343e54` failed all 10 focused calls on Linux and hosted Windows while selector/repository health and runner/toolchain setup passed. Exact-head GREEN run `35608610970` at `0ea02f3da1831be4c262151a1c606746014dc01a` passed repository health, Linux, hosted Windows, focused tests, source invariants, TypeScript typecheck and deterministic comparison. PR #707 published the exact validated head as `24681577aca04d05332ec4325bd8d505ee89f330`.

The runtime preserves owner authority and population uncertainty; applies only authored ecological mechanics; leaves missing carrying-capacity, invasive-species and other unsupported interactions unresolved; records population-state transitions with exact Event/rule/version attribution; preserves Packet-06 multi-resolution identity boundaries; prevents persistent-individual double counting; and drives offscreen progression from Campaign time rather than wall-clock time.

Fresh roadmap authority schema `1.0.4` selects `MSWI-06` as selected_not_started. MSWI-07 remains unauthorized.
