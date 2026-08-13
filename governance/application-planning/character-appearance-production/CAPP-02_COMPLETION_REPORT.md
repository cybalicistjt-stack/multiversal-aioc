# CAPP-02 Completion Candidate Report
## Preset, Randomization and Lock Libraries

**Work item:** CAPP-02  
**Status:** READY FOR EXACT-HEAD VALIDATION — NOT COMPLETED_VERIFIED  
**Owner:** John Brandon Turner  
**Upstream completed dependency:** CAPP-01

CAPP-02 converts the completed CAPP-01 stable choice/constraint surface into deterministic preset, randomization and lock behavior without inventing missing customization values.

## Delivered candidate surface

- one eligible-choice-set contract over all 25 governed CAPP-01 profiles;
- three governed recipes: randomize all, randomize unlocked and category-scoped randomization;
- SHA-256 deterministic seed behavior using NFC-normalized canonical JSON input and stable choice-ID draw streams;
- source-neutral integer weighting; non-uniform weighting requires explicit source/owner authority;
- stable-ID lock semantics and implicit protection for required/read-only/unknown/unavailable/derived state;
- portable preset schema excluding current Form, persistent/active biology, actual equipment, renderer asset IDs, live pose and hidden state;
- 19 profile-specific policies for source-backed edge cases;
- 5 concrete source-backed direct/conditional pools where CAPP-01 exposes finite values or explicit optional presence;
- synthetic/noncanonical materialization of one base reference preset for every CAPP-01 profile;
- 20 special reference cases covering linked seasons, derived hybrids, transitions, persistent/live biology, collective identity and conditional appendage state;
- three fixed deterministic test vectors;
- repository-side deterministic reference materializer and hosted completion validator.

## Deliberate no-invention rule

CAPP-01 contains many source-bounded customization statements but does not enumerate every possible body, face, hair, surface, color, marking or wardrobe value. CAPP-02 therefore does not manufacture option lists or distributions. Where no concrete source-backed value set exists, randomization returns `no_concrete_source_values` and preserves the existing value.

## Special-case protections

The candidate preserves Arborae seasonal profiles and upstream current season, Mythragara derived hybrid behavior, Nekron one-time upstream ascension plus post-transition customization namespaces, Suula persistent/active adaptation authority, Furashin preferred-versus-live phenotype separation, ManyToms design-once/replicate identity, Kola-Ha upstream Bioengineering Forms, Stygian wing non-mechanical semantics, Vespin/Moravi topology, Rakuuta no-horns canon, Toba-Madra biological-versus-cosmetic fur channels, Gray unavailable hair/ears, and The Free humanoid-android topology boundary.

## Completion boundary

This package is a candidate only. It is **NOT COMPLETED_VERIFIED** until its exact final PR head passes the applicable hosted workflow matrix, the PR is merged, the merge is signed/verified, and that evidence is projected into the CAPP backlog/checkpoint/runtime state.

CAPP-03 remains planned and is not activated by this candidate. STAGE-A-A2 remains authorized/not activated; DS-008 remains unfinished/blocked_non_owner; Apple/WP-011 remains separate. No application runtime, release, deployment, tester access, paid service, production credential or unsupported canonical promotion is authorized.
