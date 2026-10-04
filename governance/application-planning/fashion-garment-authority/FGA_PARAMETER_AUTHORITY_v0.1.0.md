# FGA Parameter Authority — Garment Construction Vocabulary

**Authority ID:** FGA-PARAM-1  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED IMPLEMENTATION FOUNDATION  
**Effective date:** 2026-10-04  
**Owner/final authority:** John Brandon Turner

## Decision

FGA-PARAM-1 is the finite semantic garment-construction vocabulary behind Fashion authoring. It is presentation-only and composes through CAS-WARD-001 and MCCS-09. It cannot alter Character anatomy, Species/Form truth, equipment ownership/stats, or mechanics.

## Garment registry

| ID | Semantic path | Kind | Purpose |
|---|---|---|---|
| FGA-GAR-001 | `garment.family` | enum_ref | Garment family/type |
| FGA-GAR-002 | `garment.silhouette` | enum_ref | Overall silhouette/cut |
| FGA-GAR-003 | `garment.length` | ordinal7 | Bounded relative garment length |
| FGA-GAR-004 | `garment.sleeve_structure` | enum_ref | Sleeve/arm-opening construction |
| FGA-GAR-005 | `garment.neckline_collar` | enum_ref | Neckline/collar construction |
| FGA-GAR-006 | `garment.fit_profile` | enum_ref | Fit/ease profile |
| FGA-GAR-007 | `garment.hem_profile` | enum_ref | Hem shape/finish |
| FGA-GAR-008 | `garment.closure_profile` | enum_ref | Closure construction |
| FGA-GAR-009 | `garment.panel_layout` | layer_set_ref | Reusable panel arrangement |
| FGA-GAR-010 | `garment.pocket_layout` | layer_set_ref | Pocket arrangement |
| FGA-GAR-011 | `garment.material_ref` | enum_ref | Material family |
| FGA-GAR-012 | `garment.pattern_ref` | enum_ref | Pattern family |
| FGA-GAR-013 | `garment.trim_layers` | layer_set_ref | Trim/edge/detail layers |
| FGA-GAR-014 | `garment.palette_zone_set` | palette_zone_set_ref | Garment color zones |
| FGA-GAR-015 | `garment.topology_accommodation_profile` | profile_ref | Topology-specific openings, clearances and fit accommodations |

## Rules

1. The registry is garment vocabulary, not a universal control sheet; garment family and topology eligibility constrain available fields.
2. Topology accommodation may fit existing anatomy but never add/remove anatomy or substitute a humanoid body.
3. Garment geometry and presentation remain separate from actual equipment authority.
4. FGA state compiles through MCCS-09/CAPP/PPIA fit, anchor, mask and occlusion rules.
5. PAPT production scales by reusable garment primitives/panels/materials/masks, not whole-character or whole-outfit raster combinations.
6. Smaller CAS-SD1/Retrobit views may declare detail loss while preserving one garment semantic identity.
7. Clothing/reference matching is a later proposal adapter and cannot become garment truth.
8. Oaran/world fashion metadata may select/style these primitives but cannot redefine their geometry semantics.
