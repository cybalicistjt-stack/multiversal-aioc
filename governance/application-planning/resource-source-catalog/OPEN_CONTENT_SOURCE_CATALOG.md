# Open Content & Reusable Asset Source Catalog

**Catalog ID:** OCS-01  
**Version:** 1.0.0  
**Status:** OWNER-APPROVED PLANNING / DISCOVERY CATALOG  
**Verified through:** 2026-09-10  
**Machine-readable catalog:** `OPEN_CONTENT_SOURCE_CATALOG.json`

## Purpose

Maintain a durable catalog of online locations from which Multiversal may later discover or acquire lawful source assets, reference data, reusable media, models, fonts, maps, audio or base assets for modification. The catalog includes both genuinely open/public-domain libraries and high-value mixed-license repositories such as Sketchfab.

**Catalog membership is not asset permission.** Every acquired item still enters through ARI identity/provenance/rights/use-capability rules. A source may change its license or terms after catalog verification.

## Rights tiers

- **Tier A — preferred:** library-wide or clearly marked CC0/public-domain/open-access material suitable for modification and commercial use, subject to non-copyright rights and site-access terms.
- **Tier B — open with conditions:** broadly reusable under attribution, share-alike, database or similarly enforceable open-license conditions.
- **Tier C — mixed/per-item:** the repository contains useful open material but license/rights must be verified for every individual item or dataset before acquisition/use.
- **Tier D — permissive but not open / reference-first:** useful material may be modified/used under a custom or proprietary license, but redistribution, model use or other rights are restricted. Do not treat it as open content.

## Acquisition rules

1. Prefer canonical upstream APIs/downloads and documented bulk mechanisms; do not scrape sites whose terms forbid scraping/data mining.
2. Capture source URL, asset ID, author/owner, exact license/rights statement, retrieval date, file hash, original metadata and any attribution/share-alike obligations.
3. A license badge or marketplace filter is evidence to verify, not sufficient proof by itself when canonical upstream terms disagree.
4. `NC`, `ND`, editorial-only, personal-use-only, unclear/no-license and custom-license assets fail commercial/derivative eligibility unless a later rights decision explicitly clears them.
5. Public-domain/CC0 status does not erase trademark, privacy, publicity, cultural-property or endorsement restrictions.
6. Store originals and modifications as separate ARI lineage nodes. A modified base asset never hides its source/license history.
7. Discovery aggregators such as Openverse and Europeana are pointers to upstream works; preserve the original host and rights evidence.
8. No bulk mirror is implied by this catalog. Acquisition happens when an owning tranche/project needs specific content and storage/rights rules permit it.

## Preferred Tier A sources

High-value default starting points include **Poly Haven**, **ambientCG**, **Kenney**, **Natural Earth**, **Smithsonian Open Access**, **The Met Open Access**, **Cleveland Museum of Art Open Access**, **National Gallery of Art Open Access**, **NYPL Public Domain Collections**, **Wikidata**, and **LibriVox**. Their exact scope/caveats are recorded in the JSON catalog.

## Tier B sources

Useful openly licensed sources with continuing obligations include **Game-icons.net**, **Google Fonts**, **OpenMoji**, **Heroicons**, **OpenStreetMap**, and **GeoNames**. Government-produced **USGS**, **NASA**, and **NOAA** material is also highly reusable but requires item/source checks for third-party content, trademarks, endorsement, likeness/publicity and similar exceptions.

## Tier C mixed/per-item sources

**Sketchfab** is a major 3D discovery source and supports Creative Commons downloads, but also contains standard/editorial/commercially licensed material. Download API use requires authenticated user access and per-model permission verification.

Other major mixed sources include **OpenGameArt**, **Freesound**, **Openverse**, **Europeana**, **Internet Archive**, **itch.io game assets**, **Musopen**, **GBIF**, **OpenTopography**, **Hugging Face Hub**, and the Library of Congress **Free to Use and Reuse** collections. These are valuable precisely because they expose item-level licenses/rights, not because the entire host is uniformly licensed.

## Tier D/reference-first sources

**Quaternius** is retained as a useful game-asset source, but its official Quaternius Asset License v1.0 (updated 2026-08-28) is no longer treated as CC0. It allows free commercial use and modification inside products but forbids redistribution of the assets themselves, including modified versions, as standalone assets/packs.

**Civitai** may be useful for local ComfyUI model/LoRA discovery, but models can carry bespoke/base-model restrictions and the service has access/automation terms. It is reference/manual-review by default, never a bulk-trusted model source.

## Continuous expansion rule

The internet cannot be exhaustively enumerated. OCS-01 is therefore a governed **continuously extensible source registry**. When a new source is found, add it with a rights tier, canonical terms/license URL, acquisition method, automation restrictions, content categories and verification date before treating it as an approved discovery source.

Openverse's provider ecosystem, Wikimedia Commons institutional uploads, Europeana partners, public museum APIs and government open-data portals should be used to discover additional upstream sources; those upstream institutions should be promoted to first-class catalog entries when they become recurring production sources.

## Roadmap integration

- **ARI** owns actual acquisition, identity, provenance, rights/use capability, deduplication, lineage and recovery.
- **PCA** may use cleared assets as recipe inputs or modification bases and registers generated derivatives back through ARI.
- **SMB-08/09** use the catalog to reduce first-party content-production cost.
- **SAA/P3D** may consume eligible ARI resources but do not gain rights merely because a source is cataloged.

This catalog does not alter `CURRENT_WORK_POINTER.json`, authorize bulk downloads, activate external credentials or promote any third-party material into Multiversal canon.