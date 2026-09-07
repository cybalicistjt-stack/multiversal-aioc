#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
NOW = "2026-09-07T18:56:00-05:00"
APP_HEAD = "8f6b95ed0479069c4a3904f25c2f5a17f00de016"
RUN = 34171468253
REPO = 101892440021
LINUX = 101892476523
WINDOWS = 101892476478
COMPARE = 101892589252
RECEIPT = "24c4c44bdeafd3acdba878552f3547ad2a5389586dc92383a754862fc78d007d"
RED = {
    "head_sha": APP_HEAD,
    "run_id": RUN,
    "repository_health_job": REPO,
    "linux_job": LINUX,
    "windows_job": WINDOWS,
    "deterministic_compare_job": COMPARE,
    "deterministic_receipt_sha256": RECEIPT,
    "matching_red_observed": True,
    "failure_stage": "vti10-invariants",
    "failure_reason": "production contract intentionally absent",
    "linux_artifact_id": 10035840549,
    "windows_artifact_id": 10035849191,
    "comparison_artifact_id": 10035852937,
    "linux_artifact_digest_sha256": "34c098079c847ad721e05d647a2a76140e79a62b7ed08f28ab85370362abdb25",
    "windows_artifact_digest_sha256": "d3c13abf4d267c5a829a95a9fd345fbcde23b7f5baffc8ce568c54aa0e7f27cd",
    "comparison_artifact_digest_sha256": "1caaa6b89fe7e6946e5058e5cfc5d63ca34d0a6f9379a4c03e7b4d08129b4776",
    "raw_evidence_confirmed": True,
    "historical_profile_fanout": 0,
}

def load(path): return json.loads((ROOT / path).read_text(encoding="utf-8"))
def save(path, value): (ROOT / path).write_text(json.dumps(value, separators=(",", ":")) + "\n", encoding="utf-8")

cp_path = "governance/ai/work-state/VTI-10-attempt-001.json"
cp = load(cp_path)
cp["schema_version"] = "0.3.0"
cp["application_pr"] = 439
cp["validation"]["acceptance_red"] = RED
cp["production_mutation_authorized"] = True
cp["selection_boundaries"] = [
    "VTI-09 is completed_verified and retired after the first Foundry VTT deep integration merged.",
    "VTI-10 remains in_progress on integration/vti-10-additional-vtt-adapters-compatibility-matrix from exact application baseline 9bed9b190b1d78bbbce9e208c2daa792c9109466.",
    "Genuine matching self-hosted Linux/Windows VTI-10 RED is sealed from exact head %s / run %s / deterministic receipt %s; bounded production mutation is open only for the registered VTI-10 contract." % (APP_HEAD, RUN, RECEIPT),
    "Provider credentials/accounts, live provider network access, live external/canonical mutation, durable VTI persistence/new migration, provider activation, tester distribution, package publication and release/deployment remain unauthorized.",
    "VTI-11+ and SGC-01+ remain unauthorized."
]
cp["next_action"] = "Implement only packages/contracts/src/virtual-tabletop-interoperability/additional-vtt-adapters-compatibility-matrix-contract.ts, then run the exact current-family VTI-10 Linux/Windows/comparator gate."
cp["implementation_scope"]["authorized"].append("bounded production implementation of packages/contracts/src/virtual-tabletop-interoperability/additional-vtt-adapters-compatibility-matrix-contract.ts after sealed matching RED")
cp["implementation_scope"]["not_authorized"] = [x for x in cp["implementation_scope"]["not_authorized"] if "before sealed matching RED" not in x]
cp["convergence_control"]["retry_basis"]["changed_since_previous"].append("Exact application acceptance head %s produced matching Linux/Windows vti10-invariants RED with deterministic receipt %s and zero historical profile fanout; production authority is now opened only for the registered VTI-10 contract." % (APP_HEAD, RECEIPT))
save(cp_path, cp)

pointer_path = "governance/ai/runtime/CURRENT_WORK_POINTER.json"
pointer = load(pointer_path)
pointer["updated_at"] = NOW
pointer["active_attempt"]["application_pr"] = 439
pointer["bounded_authority"].update({
    "production_mutation_authorized": True,
    "matching_red_observed": True,
    "vti_scope": "VTI-10 matching RED sealed; bounded production mutation is open only for additional-vtt-adapters-compatibility-matrix-contract.ts. Credentials/accounts, live provider access/mutation, persistence, activation, publication, release and successor authority remain closed."
})
pointer["exact_next_action"] = cp["next_action"]
save(pointer_path, pointer)

backlog_path = "governance/application-planning/virtual-tabletop-interoperability/VTI_PROGRAM_BACKLOG.json"
backlog = load(backlog_path)
for row in backlog["tranches"]:
    if row.get("id") == "VTI-10":
        row.update({"production_mutation_authorized": True, "matching_red_observed": True})
backlog["active_contract"].update({
    "production_mutation_authorized": True,
    "matching_red_observed": True,
    "rule": "Matching VTI-10 self-hosted Linux/Windows RED is sealed; bounded production mutation is authorized only for the registered compatibility/adapters contract."
})
backlog["boundaries"] = cp["selection_boundaries"]
save(backlog_path, backlog)

index_path = "governance/ai/runtime/ROADMAP_INDEX.json"
index = load(index_path)
index["updated_at"] = NOW
index["rule"] = "VTI-10 is in_progress with matching acceptance RED sealed; bounded production mutation is open only for the registered VTI-10 contract."
index["current"].update({"application_pr": 439, "production_mutation_authorized": True, "matching_red_observed": True})
index["boundaries"] = cp["selection_boundaries"]
index["selected_vti"]["current_state"] = "in_progress"
save(index_path, index)

runtime_path = "governance/repository-health/RUNTIME_STATE_LIFECYCLE_REGISTRY.json"
runtime = load(runtime_path)
runtime["updated_at"] = NOW
runtime["canonical_selector"]["rule"] = "CURRENT_WORK_POINTER selects VTI-10 in_progress with matching RED sealed and bounded production authority; VTI-09 remains completed_verified and retired."
runtime["application_repository"]["active_validation_family_state"] = "VTI01_VTI02_VTI03_VTI04_VTI05_VTI06_VTI07_VTI08_VTI09_completed_VTI10_matching_red_production_authorized"
runtime["active_work"].update({
    "production_mutation_authorized": True,
    "matching_red_observed": True,
    "execution_rule": "Matching VTI-10 RED is sealed. Production mutation is authorized only for the registered compatibility/adapters contract; all external activation/network/persistence/release/successor boundaries remain closed."
})
runtime["boundaries"] = cp["selection_boundaries"]
save(runtime_path, runtime)

auth_path = "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"
auth = load(auth_path)
auth["updated_at"] = NOW
auth["active_planning_work"]["implementation_scope"] = "VTI-10 matching RED sealed; bounded production contract implementation authorized, with external activation/network/persistence/publication/release/successor authority closed."
a10 = auth["vti_10_authority"]
a10.update({"production_mutation_authorized": True, "matching_red_observed": True})
save(auth_path, auth)

supp_path = ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_VTI10_GOVERNED_START_2026-09-07.md"
text = supp_path.read_text(encoding="utf-8")
if "## Matching RED sealed" not in text:
    text += "\n## Matching RED sealed\n\nApplication PR #439 exact acceptance head `%s` produced matching self-hosted Linux and Windows RED in run `%s`: repository-health selector `%s` passed, Linux `%s` and Windows `%s` both failed only at `vti10-invariants` because the production contract was intentionally absent, and comparator `%s` passed receipt `%s`. Artifacts: Linux `10035840549`, Windows `10035849191`, comparison `10035852937`. Historical profile fanout was zero. Bounded production mutation may now open only for the registered VTI-10 contract; every provider activation, credential, network, persistence, publication, release and successor boundary remains closed.\n" % (APP_HEAD, RUN, REPO, LINUX, WINDOWS, COMPARE, RECEIPT)
supp_path.write_text(text, encoding="utf-8")
