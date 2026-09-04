# ECI — Environment & Creature Integration

**Program ID:** ECI  
**Status:** OWNER-APPROVED — ECI-01 IN_PROGRESS  
**Activation:** after completed_verified MAL-10  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Selected by owner insertion:** 2026-09-04

## Current state

ECI-01 — ENV/CEW GM Discovery Integration — is `in_progress` from exact application main `5af518c1a88a5f07dbd4d1f328b18ef07f6e2ee2` on branch `integration/eci-01-env-cew-gm-discovery-integration` with bounded implementation authority. Acceptance-first matching self-hosted Linux/Windows RED is required before production mutation. ALP-01 remains planned/waiting until ECI-01 is `completed_verified`.

## Purpose

ECI is the application-side integration point for the completed ENV and CEW content/API programs. It exists so their finished work cannot remain documentation-only or be silently skipped by the software roadmap.

ECI consumes the completed upstream contracts exactly as authored:

- `ENV-HS-1.0` — the resolved Habitat Signature describing material environment conditions;
- `ENV-CD-1.0` — the controlling read-only environment-to-creature discovery projection;
- `CEW-GM-DISC-1.0` — the creature-side GM discovery, ecology, provenance and facet handoff.

ECI creates no second environment catalog, creature catalog, World/distribution ledger, relationship ledger, personhood ledger or encounter ledger. Existing owners remain authoritative.

## Tranche

### ECI-01 — ENV/CEW GM Discovery Integration

Implement the completed ENV/CEW handoff in the Multiversal application so an authorized GM can select or resolve an environment and discover source-supported creature and wildlife candidates with useful reasons and provenance.

The application integration must:

1. consume a resolved environment and `ENV-HS-1.0` rather than re-deriving environment truth;
2. use `ENV-CD-1.0` as the controlling gate/order for environment-to-creature discovery;
3. consume `CEW-GM-DISC-1.0` for creature-side identity, taxonomy, habitat, distribution, ecological role, cognition/personhood, Havalaea, partnership and expansion evidence;
4. preserve the distinction between **can occur here** and **normally occurs here**;
5. evaluate World/Reality/Setting/Place distribution and visibility before ecological fit can be shown as presence;
6. preserve canonical-presence conflicts as explainable warnings rather than silently deleting or canonizing them;
7. keep missing or unresolved creature facts unresolved;
8. keep CEW-12/13/14/15 noncanonical libraries non-present by default until distribution authority supports presence;
9. expose useful GM filtering/grouping such as native/common, possible/tolerated, seasonal/migratory, introduced/invasive, rare/exceptional, overlay-enabled, blocked/conflict and unresolved where evidence allows;
10. preserve source/provenance and an explainable contribution trace;
11. preserve mount/pet/companion/familiar information as eligibility/pathway information only;
12. preserve Havalaea sapient-animal autonomy, NPC projection semantics and voluntary-consent requirements;
13. preserve encounter ecology as preparation/filtering information only: environment discovery **does not create encounter placement**;
14. never infer canonical range from environment similarity, body plan, type, name similarity or habitat suitability;
15. never create ownership, bond, taming, domestication, personhood, encounter state or canonical creature identity merely because a result is discoverable.

## Governed start

ECI-01 has bounded implementation authority only for the read-only GM discovery seam described above. The exact inherited gate order is `identity_and_authority_gate` → `campaign_visibility_gate` → `canonical_distribution_gate` → `ecological_fit_gate` → `overlay_condition_gate` → `season_activity_gate` → `projection_facet_derivation` → `stable_grouping_and_trace`.

Supported provider-neutral query modes are `normal_discovery`, `include_blocked`, and `include_unresolved`. Supported ecological-fit states remain `preferred`, `compatible`, `conditional`, `incompatible`, and `indeterminate`. No hidden numeric fit/discovery score, ranking formula or facet precedence is authorized.

A normal discovery result may never expose hidden/suppressed material, promote unknown distribution into presence, or convert ecological suitability into canonical range. Explicit canonical presence with incompatible/indeterminate ecology remains an explainable `canonical_presence_conflict` warning. Diagnostic modes may expose blocked/unresolved candidates only to an authorized GM and never promote them into canon.

Havalaea human-level native fauna retain animal ecological identity and autonomy. NPC-capable, mount, pet/companion and familiar facets are read-only eligibility/projection facts only; sapient/person-level partnership remains voluntary-consent gated.

## Roadmap position

The owner insertion is:

`MAL-01..10 → ECI-01 → ALP-01..08 → VTI-01..12 → SGC-01..08 → MIB-16 → MIB-17 → MIB-18 → SMB-01..16 → BRP-01..11 → SMB-17 → SMB-18`

ALP-01's earlier selected-not-started state is retained as historical evidence but is superseded by this owner insertion. ALP resumes only after ECI-01 is `completed_verified`.

## Boundaries

- ECI-01 owns projection/integration mechanics only, not environment, creature, distribution, relationship, personhood or encounter truth.
- No schema/migration is reserved; no durable persistence is authorized.
- No provider activation, tester distribution, release or deployment is authorized.
- No new canon is created by discovery output.
- Unknown and hidden information remain conservative and unresolved.
- No later roadmap edit may silently drop or bypass ECI-01 without an explicit owner-authorized superseding decision.
- ALP-01+ implementation remains unauthorized until ECI-01 closeout.
