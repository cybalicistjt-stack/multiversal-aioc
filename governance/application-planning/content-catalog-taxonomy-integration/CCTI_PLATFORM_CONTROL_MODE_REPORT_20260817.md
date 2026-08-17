# CCTI Platform Universal Taxonomy — Control Mode Candidate Projection

**Date:** 2026-08-17  
**Status:** candidate disposition complete; not enabled

Exact Platform v0.11.0 defines `control_mode` as a **multi-select** facet with 10 controlled values. This tranche applies it conservatively to the **2,984 platform/model/named-asset/archetype rows**. The **2,644 non-model rows** remain explicitly not applicable to platform control mode rather than inheriting host behavior.

## Result

- applicable platform rows with candidates: **2,984 / 2,984**;
- non-model rows explicitly N/A: **2,644**;
- candidate assertions: **3,172**;
- silently unaccounted rows: **0**.

Value distribution: `autonomous` 19, `bonded` 90, `bound` 29, `crewed` 1,424, `mixed` 18, `semi-auto` 33, `single` 1,559.

## Evidence posture

Direct crew/pilot counts establish the base direct-control candidate. Explicit platform-owned autonomy, remote-control, bonded/symbiotic/empathic control, or ritual/command control can add a secondary mode. The pass deliberately does **not** treat autonomous damage control, fleet AI, remote sensors, generic neural/manual redundancy, or zero-crew nonplatform records as evidence of whole-platform autonomous/remote/bonded control.

## Validation

PASS: exact 10-value registry membership; 5,628/5,628 disposition accounting; 2,984/2,984 applicable platform coverage; 2,644/2,644 non-model N/A; zero duplicate same-value assertions; source/master hashes remain the verified CCTI hashes; no candidate enablement/mechanics/runtime/game-ready change.

## Next

Proceed to the final universal Platform facet, `platform_nature`, then run a cross-facet review before any adoption proposal.
