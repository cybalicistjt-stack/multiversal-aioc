# VTI-09 — First Platform Selection Evidence

**Observed:** 2026-09-07  
**Decision:** Foundry Virtual Tabletop (`foundry-vtt`)  
**Integration target:** Level 3 — native system/rules package plus bounded adapter integration.

## Current first-party evidence

- Foundry `Introduction to System Development`: `https://foundryvtt.com/article/system-development/` — native `system.json` game-system packages, ES modules, packs, compatibility and install/update manifests.
- Foundry `Introduction to Module Development`: `https://foundryvtt.com/article/module-development/` — add-on modules can add content, interface and functionality; modules support compendium packs and a specialized socket namespace for connected clients.
- Foundry `Software License`: `https://foundryvtt.com/article/license/` — software license owners may develop and distribute Game Systems, Add-on Modules and Worlds subject to rights in included content.
- Foundry `Content Packaging Guide`: `https://foundryvtt.com/article/packaging-guide/` — self-contained module/compendium packaging and manifest-driven installation.
- Foundry `Package Release API`: `https://foundryvtt.com/article/package-release-api/` — programmatic package-release surface exists but requires a package authorization token; VTI-09 does not use that token or activate publication.
- Foundry `Publisher Handbook`: `https://foundryvtt.com/article/publisher-handbook/` — self-publishing Foundry-targeted systems/modules/worlds is supported subject to content rights.

## Selection rationale

VTI-01 already classified Foundry VTT and Fantasy Grounds Unity at the highest Level-3 ceiling, with Roll20, Owlbear Rodeo and Tabletop Simulator shallower for this program and Alchemy shallower still. The 2026-09-07 verification preserves Foundry's documented Level-3 path and adds a strong implementation fit: its JavaScript/ES-module system/module architecture maps directly onto the existing TypeScript provider-neutral VTI SDK, while its native system, document, compendium, scene and socket surfaces allow one adapter to exercise the largest completed VTI contract set without inventing a parallel rules authority.

Fantasy Grounds remains a viable later adapter, but its current ruleset/extension surface is XML/Lua-centric and current September 2026 developer notes warn that ruleset/extension compatibility changes may require updates. Roll20 and Owlbear Rodeo remain strong Level-2 candidates but do not currently exceed Foundry's documented native-system integration ceiling for this first deep adapter.

## Authority boundary

This is provider selection, not provider activation. No Foundry account credential, software-license secret, package-release token, network call, live world mutation, durable VTI persistence, migration, tester distribution, package publication, release or deployment is authorized by this decision. Production provider-specific implementation remains locked until genuine matching VTI-09 acceptance RED is sealed.
