# Application Implementation Roadmap — ECI-01 Owner Insertion

**Amendment ID:** MV-APP-ROADMAP-ECI-2026-09-04  
**Applies after:** completed_verified MAL-10  
**Insertion:** ECI-01 before ALP-01  
**Status:** OWNER-APPROVED — EFFECTIVE PLANNING/RUNTIME INSERTION  
**Owner and final authority:** John Brandon Turner

## Decision

MAL-10 is completed_verified. The completed ENV and CEW parallel programs have reached the application handoff state `ready_for_separately_governed_software_selection`. The owner directs that this handoff be consumed now, before the next software family begins, rather than left as an indefinite future dependency.

The effective forward order is amended from:

`MAL-01..10 → ALP-01..08 → VTI-01..12 → SGC-01..08 → ...`

to:

`MAL-01..10 → ECI-01 → ALP-01..08 → VTI-01..12 → SGC-01..08 → ...`

ALP-01's prior `selected_not_started` checkpoint is preserved as historical evidence of the MAL-10 closeout. It is superseded as the current selector by this owner insertion and returns to planned/waiting status until ECI-01 is `completed_verified`.

## ECI-01 — ENV/CEW GM Discovery Integration

ECI-01 is a single software integration tranche consuming:

- `ENV-HS-1.0`;
- `ENV-CD-1.0`;
- `CEW-GM-DISC-1.0`.

It implements the already-designed GM environment→creature discovery seam in `Multiversal-app`. It must preserve the completed ENV/CEW authority boundaries: habitat suitability is not canonical distribution; **can occur here** is not **normally occurs here**; unknown/hidden facts remain unresolved; eligibility is not relationship state; and discovery does not create encounter placement.

ECI-01 is selected only. This amendment does not grant implementation authority, create an implementation branch, reserve migration 0022, or authorize provider activation, tester distribution, release or deployment. A future owner `Continue` must governed-start ECI-01 from the MAL-10 application baseline before product mutation.

## Durability rule

The ECI insertion is a required roadmap dependency, not an informational TODO. `CURRENT_WORK_POINTER.json`, `ROADMAP_INDEX.json`, the authority/lifecycle registries, MAL successor state, ALP activation state and the ECI backlog/checkpoint must agree on the insertion. A control-plane regression protects that agreement so **no later roadmap edit may silently drop** or bypass ECI-01 without an explicit owner-authorized superseding decision.
