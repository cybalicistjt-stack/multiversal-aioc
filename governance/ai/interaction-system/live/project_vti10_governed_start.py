#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NOW = "2026-09-07T18:39:00-05:00"
BRANCH = "integration/vti-10-additional-vtt-adapters-compatibility-matrix"
BASE = "9bed9b190b1d78bbbce9e208c2daa792c9109466"
SUPP = "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_VTI10_GOVERNED_START_2026-09-07.md"

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def save(path, value):
    (ROOT / path).write_text(json.dumps(value, separators=(",", ":")) + "\n", encoding="utf-8")

cp_path = "governance/ai/work-state/VTI-10-attempt-001.json"
cp = load(cp_path)
cp.update({
    "schema_version": "0.2.0",
    "status": "in_progress",
    "started_at": NOW,
    "implementation_branch": BRANCH,
    "implementation_authority": True,
    "branch_creation_authorized": True,
    "acceptance_package_authorized": True,
    "production_mutation_authorized": False,
    "application_baseline_sha": BASE,
    "next_action": "Create the registered VTI-10 application branch from exact main and land acceptance-only tests/docs/profile/verifier. Production remains unauthorized until a genuine matching self-hosted Linux/Windows RED is sealed."
})
cp["implementation_scope"] = {
    "authorized": [
        "acceptance scaffolding for Fantasy Grounds Unity Level 3 derivative ruleset/extension/module projection",
        "acceptance scaffolding for Roll20 Level 2 derivative companion/automation projection constrained by sandbox and Pro-gated evidence",
        "acceptance scaffolding for Owlbear Rodeo Level 2 derivative extension/scene/metadata projection",
        "acceptance scaffolding for Tabletop Simulator Level 2 derivative Lua/JSON companion projection",
        "acceptance scaffolding for Alchemy RPG Level 1 export/content-pack projection",
        "a deterministic compatibility matrix preserving VTI-01 supported/conditional/unknown states and exact integration ceilings"
    ],
    "not_authorized": [
        "production provider adapter implementation before sealed matching RED",
        "provider credentials/accounts or live provider network access",
        "live external synchronization mutation or canonical game-state mutation",
        "durable VTI persistence or new migration",
        "provider activation, tester distribution, package publication, release or deployment",
        "VTI-11+ or SGC-01+ implementation"
    ]
}
cc = cp.setdefault("convergence_control", {})
cc["owner_continue_count"] = 1
cc["execution_cycles"] = 1
cc["repair_cycles"] = max(int(cc.get("repair_cycles", 0)), 1)
cc["repository_state_repair_cycles"] = max(int(cc.get("repository_state_repair_cycles", 0)), 1)
cc["last_failure_signature"] = "An accidental governed-start supplement write reached AIOC main because the branch argument was omitted; the exact file was immediately reverted, restoring the prior canonical tree before branch work continued."
cc["last_failure_class"] = "repository_state"
cc["retry_basis"] = {"changed_since_previous": ["AIOC main tree was restored exactly before the governed-start branch was created.", "The test-first governed-start RED then failed only because VTI-10 remained selected_not_started, as intended."]}
save(cp_path, cp)

pointer_path = "governance/ai/runtime/CURRENT_WORK_POINTER.json"
pointer = load(pointer_path)
pointer["updated_at"] = NOW
pointer["roadmap_supplements"] = [SUPP]
pointer["selection_reason"] = "VTI-10 governed start after exact test-first control-plane RED; only branch creation and acceptance-package authority are open."
pointer["active_attempt"].update({
    "work_item_id": "VTI-10", "attempt_id": "VTI-10-attempt-001", "status": "in_progress",
    "implementation_branch": BRANCH, "implementation_authority": True, "application_baseline_sha": BASE,
    "active_item": "VTI-10 — Additional VTT Adapters & Compatibility Matrix"
})
pointer["bounded_authority"].update({
    "vti_implementation": True, "vti_work_item": "VTI-10", "vti_branch": BRANCH,
    "acceptance_package_authorized": True, "production_mutation_authorized": False,
    "matching_red_observed": False, "tester_distribution": False, "release_or_deployment": False,
    "paid_provider_activation": False,
    "vti_scope": "VTI-10 governed-start acceptance only; production remains closed until matching RED. No credentials, live provider access/mutation, persistence, activation, publication, release or successor authority."
})
pointer["exact_next_action"] = "Create VTI-10 application branch from exact application main and land acceptance-only package; observe matching self-hosted Linux/Windows RED before production mutation."
save(pointer_path, pointer)

backlog_path = "governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json"
backlog = load(backlog_path)
backlog["application_baseline_sha"] = BASE
backlog["current_item"] = "VTI-10"
backlog["current_attempt"] = "VTI-10-attempt-001"
for row in backlog["tranches"]:
    if row.get("id") == "VTI-10":
        row.update({
            "status": "in_progress", "implementation_authority": True, "implementation_branch": BRANCH,
            "application_baseline_sha": BASE, "branch_creation_authorized": True,
            "acceptance_package_authorized": True, "production_mutation_authorized": False,
            "provider_activation_authorized": False, "matching_red_observed": False
        })
backlog["active_contract"] = {
    "work_item": "VTI-10", "status": "in_progress", "implementation_branch": BRANCH,
    "implementation_authority": True, "acceptance_package_authorized": True,
    "production_mutation_authorized": False, "matching_red_observed": False,
    "rule": "VTI-10 acceptance package is authorized after governed start; production remains closed until genuine matching self-hosted Linux/Windows RED."
}
backlog["boundaries"] = [
    "VTI-01 through VTI-09 remain completed_verified and frozen with implementation authority retired.",
    "VTI-10 is in_progress from exact application main %s with only branch creation and acceptance-package authority open." % BASE,
    "Production provider adapters require sealed matching VTI-10 RED before mutation authority opens.",
    "No provider credentials/accounts, live network access, live external/canonical mutation, durable persistence/new migration, provider activation, tester distribution, package publication, release or deployment is authorized.",
    "VTI-11+ and SGC-01+ remain unauthorized."
]
save(backlog_path, backlog)

runtime_path = "governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json"
runtime = load(runtime_path)
runtime["updated_at"] = NOW
runtime["canonical_selector"]["rule"] = "CURRENT_WORK_POINTER selects VTI-10 in_progress governed-start acceptance; VTI-09 is completed_verified and retired."
runtime["work_state"].update({"selected_checkpoint": cp_path, "selected_checkpoint_role": "active_implementation"})
runtime["application_repository"].update({
    "canonical_main": BASE,
    "active_validation_family_state": "VTI01_VTI02_VTI03_VTI04_VTI05_VTI06_VTI07_VTI08_VTI09_completed_VTI10_in_progress_acceptance",
    "sealed_predecessor_baseline": BASE
})
runtime["active_work"].update({
    "work_item": "VTI-10", "attempt_id": "VTI-10-attempt-001", "state": "in_progress", "role": "active_implementation",
    "implementation_branch": BRANCH, "implementation_authority": True, "acceptance_package_authorized": True,
    "production_mutation_authorized": False, "matching_red_observed": False,
    "execution_rule": "Acceptance-only VTI-10 work is authorized. Production mutation requires a sealed matching self-hosted Linux/Windows RED."
})
runtime["boundaries"] = backlog["boundaries"]
runtime["selected_vti"].update({
    "current": "VTI-10", "current_state": "in_progress", "implementation_authority": True,
    "implementation_branch": BRANCH, "application_baseline_sha": BASE, "strict_next": "VTI-11"
})
save(runtime_path, runtime)

auth_path = "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"
auth = load(auth_path)
auth["updated_at"] = NOW
auth["active_planning_work"].update({
    "work_item": "VTI-10", "attempt_id": "VTI-10-attempt-001", "state": "in_progress",
    "implementation_branch": BRANCH, "implementation_authority": True, "application_baseline_sha": BASE,
    "implementation_scope": "Bounded VTI-10 branch plus acceptance package only; production requires sealed matching RED."
})
a10 = auth.setdefault("vti_10_authority", {})
a10.update({
    "selected_not_started": False, "status": "in_progress", "retired": False,
    "implementation_branch": BRANCH, "implementation_authority": True, "branch_creation_authorized": True,
    "acceptance_package_authorized": True, "production_mutation_authorized": False, "matching_red_observed": False,
    "additional_adapters_compatibility_matrix_authorized": True,
    "provider_activation_authorized": False, "tester_distribution_authorized": False,
    "release_or_deployment_authorized": False, "vti11_plus_authorized": False, "sgc01_plus_authorized": False
})
# replace current roadmap supplement registration if present
for row in auth.get("current", []):
    if row.get("kind") == "roadmap_supplement":
        row["path"] = SUPP
save(auth_path, auth)

program_path = ROOT / "governance/application-planning/virtual-tabletop-interoperability/VTI_VIRTUAL_TABLETOP_INTEROPERABILITY_PROGRAM.md"
text = program_path.read_text(encoding="utf-8")
text = text.replace("10. **VTI-10 — Additional VTT Adapters & Compatibility Matrix** — **SELECTED_NOT_STARTED**", "10. **VTI-10 — Additional VTT Adapters & Compatibility Matrix** — **IN_PROGRESS**")
text = text.replace("VTI-10 — Additional VTT Adapters & Compatibility Matrix — is `selected_not_started`", "VTI-10 — Additional VTT Adapters & Compatibility Matrix — is `in_progress` under governed-start acceptance authority")
program_path.write_text(text, encoding="utf-8")

supp = ROOT / SUPP
supp.write_text("""# VTI-10 — Governed Start\n\n**Status:** in_progress / acceptance authority only  \n**Application baseline:** `9bed9b190b1d78bbbce9e208c2daa792c9109466`\n**Application branch:** `integration/vti-10-additional-vtt-adapters-compatibility-matrix`\n\nVTI-10 is the strict successor to completed_verified VTI-09. The test-first AIOC governed-start RED failed only because VTI-10 remained `selected_not_started`. This projection opens the application branch and acceptance package, but production mutation remains closed until a genuine matching self-hosted Linux/Windows RED is sealed.\n\nThe acceptance target covers the remaining VTI-01 surveyed platforms at their evidence-backed ceilings: Fantasy Grounds Unity Level 3; Roll20 Level 2 conditional companion/automation; Owlbear Rodeo Level 2 extension; Tabletop Simulator Level 2 Lua/JSON companion; Alchemy RPG Level 1 export/content pack. Capability states must remain precise and must not promote unknown support.\n\nNo provider credentials/accounts, live network access, live external/canonical mutation, durable persistence/new migration, provider activation, tester distribution, publication, release/deployment, VTI-11+ or SGC-01+ authority is opened.\n""", encoding="utf-8")
