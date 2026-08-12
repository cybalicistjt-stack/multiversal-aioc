# PPIA-10 — Relationship, Social & Faction Content Framework

## Source and Design Inventory v0.1.0

Status: **FOUNDATION SOURCE INVENTORY — NOT PPIA-10 COMPLETE**

### Retained package

`MV_Master_01_Core.zip` — SHA-256 `c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec`.

### Direct retained game-source review

Five directly relevant PDFs were rendered and visually reviewed: **5 PDFs / 44 pages**. They are `Factions.PDF` (4), `Social Gameplay.PDF` (18), `Social status.PDF` (10), `Social status effects 1.PDF` (10), and `social status effects for artisans, craftsmen, and performers.PDF` (2). `Social status.PDF` and `Social status effects 1.PDF` are near-duplicate variants (normalized text similarity about 0.985), so overlapping wording is not double-counted as independent authority.

Two retained structured CSVs provide **1,374 rows** total. `Abilities_Core.csv` has 1,256 rows, including **82 structurally explicit Social & Influence Skill records**: 61 Social Play Ability Tree records and 21 Politician Tree records. `Magic_Faction_Abilities.csv` has 118 rows, including **12 structurally explicit faction-related records**: 11 Sacred Order high-ranking-agent records plus one Warden faction-tree reference that explicitly states the member trees are not published.

`V06_Social.md` provides the Social Hub, Conversation Interface, Relationship Graph, Reputation Dashboard, Negotiation Workspace, Organization & Faction Profiles, GM Social Director, responsive recovery and accessibility presentation intent.

### Direct source observations

- `Social Gameplay.PDF` presents ten social skills: Persuasion, Deception, Intimidation, Insight, Performance, Negotiation, Empathy, Command, Street Smarts, and Investigation. Its DCs are examples, not a universal table.
- The social-status sources distinguish **area/community status** from **interpersonal status**. They provide concrete mechanical examples, but they do not define one mandatory global status registry.
- `Social Gameplay.PDF` provides five example Bond types — Kindred, Blood, Rivalry, Romantic, and Mentor — plus source-specific Bond XP examples. PPIA-10 retains those as source examples rather than universalizing their thresholds.
- The artisan/craftsman/performer source contributes **20 profession/performance-specific social-status examples**.
- `Factions.PDF` contains **11 named faction/organization/government headings** with uneven detail, including explicit material about membership, mandates/access to resources, clandestine activity, governance, rivalry, sponsorship, reputation and changing membership. This supports reference fixtures, not a fabricated uniform schema.

### Canonical design inputs

F009, F010 and F016 are not replaced. PPIA-10 integrates them. F009 supplies fourteen directional relationship dimensions, multiple scale-profile kinds, seven reveal layers, Bonds/leverage/favors/promises/debts/oaths/obligations and 24 fixtures. F010 supplies three interaction modes, fourteen Action categories, seven alpha Actions, six resolution methods, seven degree outcomes, twenty-nine possible outcome Event draft types and 24 fixtures. F016 supplies sixteen faction contract families, nine visibility layers, explicit membership/rank/office/standing/influence separation, seven converted organization profiles, a 956-record progression corpus and 24 fixtures.

### Source gaps retained as gaps

No source reviewed here defines a universal relationship scale, universal standing scale, universal influence scale, universal social DC table, automatic reciprocal relationships, title/progression-derived faction membership, rank-derived permission, or AI authority to decide/reveal/commit social outcomes. The relationship register contains only four source-explicit relationship facts, the faction register contains zero stable faction references, and the social-mechanic register does not turn its 209 names into 209 executable Actions.

### Foundation consequence

PPIA-10 therefore uses typed ownership and explicit source/profile bindings. Similar words such as **fear**, **loyalty**, **reputation**, **social status**, **standing**, and **influence** do not justify merging the records that own them. Persistent consequences remain Event-backed and delegated to their owning domains.

### Runtime boundary

This inventory authorizes design work only. It does not activate application runtime, STAGE-A-A2, release, deployment, tester access, paid services or production credentials.
