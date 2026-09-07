# VTI-10 — Governed Start

**Status:** in_progress / acceptance authority only  
**Application baseline:** `9bed9b190b1d78bbbce9e208c2daa792c9109466`
**Application branch:** `integration/vti-10-additional-vtt-adapters-compatibility-matrix`

VTI-10 is the strict successor to completed_verified VTI-09. The test-first AIOC governed-start RED failed only because VTI-10 remained `selected_not_started`. This projection opens the application branch and acceptance package, but production mutation remains closed until a genuine matching self-hosted Linux/Windows RED is sealed.

The acceptance target covers the remaining VTI-01 surveyed platforms at their evidence-backed ceilings: Fantasy Grounds Unity Level 3; Roll20 Level 2 conditional companion/automation; Owlbear Rodeo Level 2 extension; Tabletop Simulator Level 2 Lua/JSON companion; Alchemy RPG Level 1 export/content pack. Capability states must remain precise and must not promote unknown support.

No provider credentials/accounts, live network access, live external/canonical mutation, durable persistence/new migration, provider activation, tester distribution, publication, release/deployment, VTI-11+ or SGC-01+ authority is opened.

Projection evidence: helper run `34170916589` passed the VTI-10 lifecycle regression and repository-health validation before committing the helper-free projected tree. The subsequent bot-authored PR audit was `action_required`, so a user-authored evidence-only candidate was created without changing authority semantics.

Validation-repair evidence: run `34171168575` passed the full control-plane suite and repository-health validation after aligning `ROADMAP_INDEX`, making the VTI-09 successor regression lifecycle-aware, and entering diagnostic mode for the second validation-contract repair. This update seals that exact repaired semantic tree as a user-authored candidate.

## Matching RED sealed

Application PR #439 exact acceptance head `8f6b95ed0479069c4a3904f25c2f5a17f00de016` produced matching self-hosted Linux and Windows RED in run `34171468253`: repository-health selector `101892440021` passed, Linux `101892476523` and Windows `101892476478` both failed only at `vti10-invariants` because the production contract was intentionally absent, and comparator `101892589252` passed receipt `24c4c44bdeafd3acdba878552f3547ad2a5389586dc92383a754862fc78d007d`. Artifacts: Linux `10035840549`, Windows `10035849191`, comparison `10035852937`. Historical profile fanout was zero. Bounded production mutation may now open only for the registered VTI-10 contract; every provider activation, credential, network, persistence, publication, release and successor boundary remains closed.
