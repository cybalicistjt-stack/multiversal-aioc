# OARC-04 Completion Report

**Work item:** OARC-04 — Operational Specialization Profiles  
**Status:** completed_verified  
**Completed:** 2026-09-20  
**Contract:** `OARC04.OPERATIONAL_SPECIALIZATION_PROFILES.v1`

OARC-04 adds bounded, provenance-preserving specialization profiles for ordinary vehicles, mecha, ships and bases without creating a second operational runtime.

Vehicles preserve raw source specialization facts. Mecha preserve frame/class, mobility, EP/energy, interface, modules, sensors and shields while source-absent heat remains unresolved. Ships preserve hull/scale, shields, FTL, hangar evidence, hardpoints, power, reactor/fuel and endurance while life-support capacity remains unresolved without a dedicated source field; detailed power-grid simulation remains deferred by PPIA-04 IA-D08-003. Bases may project existing MIB-14 configuration and reference-only facility evidence, while habitation remains unresolved through SMB-05's explicit housing-reference seam.

Mixed OARC-03 provenance remains mixed. Missing values do not receive defaults. MERA and MBES remain reserved owner seams only.

Causal RED: run `35531146908` at `b5ed29350036e01f1478694208101bee3e733fee`. Exact-head governed GREEN: run `35531294278` at `b46f749ee83225d0acd7a3a270e2e8314b55c7f4`. Fresh app-main drift had zero overlap with the OARC-04 write set. PR #652 published via squash as application main `665f7a67ed1685280aa5177dd890209f325bfa01`.

Fresh AIOC state preserves GPR-06 and MRCS-19 independently. ROADMAP_DEPENDENCY_GRAPH.json schema 1.0.4 contains no OARC interstitial override. OARC-05 — Containment & Large-Asset Relationships — is the strict selected successor and is not started by this closeout.
