# MSLR Spatial Architecture Research Amendment — 2026-09-21

**Status:** owner-approved family architecture amendment during governed MSLR-01 causal RED  
**Effect on roadmap:** no new tranches; reduced order remains MSLR-01/03/04/07/08/13/14/16/18.

## Reviewed references

- Interactive Hyperbolic Tiling in the Poincaré Disc (Malin Christersson): https://www.malinc.se/noneuclidean/en/poincaretiling.php
- HyperRogue documentation/project architecture: https://zenorogue.github.io/hyperrogue-doc/ and https://github.com/zenorogue/hyperrogue

These references inform clean-room architectural ideas only. HyperRogue implementation source is GPL-2.0 and is not incorporated by this amendment.

## Adopted ideas

1. intrinsic geometry/law, gameplay substrate/discretization and projection are separate layers;
2. projection distortion does not alter intrinsic geometry or identity;
3. canonical identity is owner-backed, not floating/projection-coordinate identity;
4. quotient identifications and orientation-changing topology are first-class authored semantics;
5. exponentially growing/unbounded spaces require lazy local addressability rather than exhaustive enumeration;
6. fundamental-domain plus transformation/group generation is a reusable authoring pattern;
7. regular Schläfli {p,q} tilings are an optional specialized generator family, not a universal geometry rule;
8. pathfinding, pursuit, travel, tactical movement and range must consume the same accepted spatial law semantics;
9. golden proof must include projection-invariance and discrete/continuous realization equivalence.

## Immediate MSLR-01 consequence

Because the owner approved this amendment after the original MSLR-01 RED but before production GREEN, the acceptance test is widened and causal RED is re-established before implementation. No production implementation had been attached at the time of approval.
