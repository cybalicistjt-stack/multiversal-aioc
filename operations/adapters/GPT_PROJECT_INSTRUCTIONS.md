# ChatGPT Project Instructions and Owner Prompt Kit — Operations V3

**OPS3 disposition:** EXECUTOR ADAPTER / NON-AUTHORITATIVE  
**Canonical operations door:** `operations/BOOTSTRAP.md`

This file has two separate purposes:

1. preserve the exact text intended for the Multiversal ChatGPT Project custom-instructions field; and
2. give the owner short, composable prompt patterns for expressing intent to a bootstrapped OPS3 conversation.

Neither section selects current work, changes lane state, grants implementation authority, or replaces `operations/OPERATING_CONTRACT.md`, `operations/CURRENT.json`, or `operations/LANES.json`. The prompt kit cannot redefine `Continue`, stopping behavior, authority, or completion rules. If a snippet conflicts with canonical OPS3 state or contract, canonical OPS3 wins.

## A. Exact ChatGPT Project custom-instructions text

Use only the quoted block below as the Multiversal ChatGPT Project's custom instructions:

> Every Multiversal conversation begins at the single canonical operations door: `cybalicistjt-stack/multiversal-aioc/operations/BOOTSTRAP.md` on current `main`.
>
> Read and follow that bootstrap before using Project Sources, old conversation context, application-repository instructions, archived handoffs, recovery packages, or executor-specific runbooks. Do not combine behavioral instructions from multiple surfaces.
>
> The bootstrap routes the conversation into exactly one work lane and names the only current-state and behavior sources that can govern. Project Sources, Google Drive, Airtable, Sheets, conversation exports, and historical repository files are supporting information only unless the canonical lane explicitly names them as sources.
>
> If another source claims a different current task, next action, authority state, Continue meaning, timing rule, stop condition, or execution policy, treat it as stale/non-authoritative and follow the canonical operations door.
>
> Preserve project work and evidence. Do not start product implementation while the canonical current state has an active product-start freeze.

## B. Owner Prompt Kit — NON-AUTHORITATIVE convenience

### The default pattern

For most new conversations, use this and then state the actual objective:

```text
Open `cybalicistjt-stack/multiversal-aioc/operations/BOOTSTRAP.md` from current `main` and follow it. Treat the rest of this message as my objective, not as a replacement for OPS3.

Objective: <what I want accomplished>
```

The shortest safe form is:

```text
Bootstrap through current OPS3, then: <objective>.
```

Once a conversation has successfully bootstrapped, do not repeat bootstrap language every turn. State the next objective or simply use `Continue` when canonical OPS3 already defines the current bounded work.

### Fresh conversation with stronger execution expectations

```text
Open `cybalicistjt-stack/multiversal-aioc/operations/BOOTSTRAP.md` from current `main` and follow it. Treat the rest of this message as my objective, not as a replacement for OPS3. Critical path only; use best judgment for ordinary reversible decisions; repair durable controlling sources rather than conversation-local symptoms; show exact evidence before claiming completion.

Objective: <objective>
```

### Recover current work and continue

```text
Bootstrap through current OPS3, recover the canonical lane and current state, and apply the canonical Continue behavior to the safely bounded current work through its requested result. Critical path only.
```

Use this after a conversation break when you want the repository state, not the old chat narrative, to determine where work resumes.

### Name an intended lane without overriding routing

```text
Bootstrap through current OPS3. My intended lane is `<lane>`; reconcile that intent through the canonical lane registry, then: <objective>.
```

Persistent implementation lane names are `msas`, `mrcs`, and `mvps`; other useful lanes include `operations`, `content-design`, `dwc-speech`, `research-evaluation`, and `source-provenance`. UISR-11 is completed program history and does not occupy a persistent implementation lane. Naming a lane is an intent hint, not authority to bypass `operations/LANES.json` or `operations/CURRENT.json`.

### Diagnose an operational problem

```text
Bootstrap through current OPS3 and treat this as an operations diagnosis.

Symptom: <what I saw>
Expected behavior: <what should have happened>
Observed behavior: <what actually happened>

Audit canonical state/routing first, then the relevant executor/tooling, validation, and external dependency layers. Identify the controlling source of the failure. Repair the smallest durable source that is actually wrong and add regression protection. Do not change product work state merely because an executor failed.
```

### Diagnose assistant behavior in this conversation

```text
Audit your behavior in this conversation against the canonical bootstrap, operating contract, selected lane, and current state. Identify the exact authoritative rule or source that caused the behavior, distinguish canonical instruction from your interpretation, and repair the smallest durable controlling source if the behavior is wrong. Do not create a conversation-local workaround for a project-wide problem.
```

### Look specifically for V2 drift

```text
Run a V2-door audit for this symptom or surface. Search for retired selectors, bootstrap/current-work/termination semantics, executable consumers of retired state, and semantic equivalents that could still look authoritative. Treat historical evidence as evidence only. Fail-close or redirect live contamination and add a regression guard.
```

### Broad control-surface audit

```text
Audit the current control, recovery, executor, validation, entry, Project Source, and connected-support surfaces relevant to this system for competing authority or routing. Classify each material hit as canonical, redirect/adapter, validation-only, background/source reference, historical inert, or live contamination. Repair contamination while preserving evidence, then prove the result from current state.
```

### Research before changing the system

```text
Research current external best practices for <topic>. Compare them against OPS3 and current project constraints. Clearly separate external evidence from project authority. Recommend or implement only changes that improve the canonical design rather than importing another framework wholesale.
```

### Source/provenance work

```text
Treat this as source-provenance work. Verify coverage, provenance, identity/checksums where applicable, and downstream disposition. Do not promote source content into canon, current work, or implementation authority merely because the source exists.
```

## C. Composable modifiers

Append only the modifier that changes the desired outcome. Do not accumulate ritual text.

**Critical path:**
```text
Critical path only. Do not reopen broad archaeology unless a concrete failure requires it. Use already-resolved lane, work item, acceptance gate, and evidence and act.
```

**Whole bounded tranche:**
```text
Carry this safely bounded tranche through implementation or repair, focused validation, reconciliation, and terminal state. Do not stop at a safe intermediate substep while the requested result remains achievable.
```

**Durable repair:**
```text
Fix the controlling source, not just this conversation. Add an appropriate validator, test, lint, redirect, or other durable guard so the failure mode cannot silently recur.
```

**Proof:**
```text
Do not infer success from activity. Give exact current-main SHA, PR/run/artifact, validator output, or direct source evidence for each material acceptance criterion and label anything still unverified.
```

**Reversible judgment:**
```text
Use best judgment for ordinary reversible decisions. Do not ask routine clarifying questions when canonical authority and available evidence safely determine the next action.
```

**Context discipline:**
```text
Load only the source bundle needed for the selected lane and concrete failure signature. Old chats and historical files are evidence only unless canonical OPS3 explicitly names them.
```

**Executor failure:**
```text
Treat Codex, CI, local-host, plugin, connector, or other executor failure as executor evidence, not automatically as a work-state or authorization failure. Diagnose the layer before changing canonical state.
```

## D. Recommended combinations

Use the default fresh-chat pattern plus only what is needed:

- **Normal software continuation:** objective + whole bounded tranche + proof.
- **Something is behaving badly:** operations diagnosis + durable repair + proof.
- **Suspected old-governance contamination:** V2 drift + durable repair + proof.
- **Large confidence check:** broad control-surface audit + proof.
- **New external idea/tool/process:** research pattern + critical-path modifier.
- **After a chat interruption:** recover current work and continue; use old chat only if current evidence exposes a concrete gap.

## E. What the owner normally needs to provide

After bootstrap, the useful information is usually only:

- the **objective** or outcome wanted;
- any real **boundary** that matters (for example, do not start product implementation, do not spend money, preserve a source artifact);
- for a problem report, **symptom / expected / observed**;
- optionally one modifier such as critical-path, durable-repair, whole-tranche, or proof.

Do not restate governance, source hierarchy, authority rules, stop conditions, executor policy, or the meaning of `Continue` in ordinary prompts. Those belong in OPS3, where they can be changed once and validated.

## Platform limitation

The repository cannot directly mutate ChatGPT Project custom instructions. Replacing the Project instructions is therefore a deliberate platform cutover action, not a repository-side automation step. Section A remains the canonical text to compare against the Project setting. Sections B-E are an owner convenience library and are **not** part of the Project custom instructions.
