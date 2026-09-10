import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def test_mlr_closeout_is_complete_and_does_not_replace_product_authority():
    registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
    manifest = load_json("governance/ai/runtime/LOCAL_WORKSTATION_RESOURCE_MANIFEST.json")
    closeout = load_json("governance/ai/work-state/MLR-01_CLOSEOUT_2026-09-10.json")

    # Closing MLR must not replace or advance the independently governed product
    # selection merely because workstation setup is complete.
    assert registry["active_planning_work"]["work_item"] == pointer["active_attempt"]["work_item_id"]
    assert registry["active_planning_work"]["implementation_authority"] == pointer["active_attempt"]["implementation_authority"]

    parallel = registry["parallel_machine_local_work"]
    assert parallel["work_item"] == "MLR-01"
    assert parallel["status"] == "completed_verified"
    assert parallel["lifecycle"] == "COMPLETED_VERIFIED"
    assert parallel["product_implementation_authority"] is False
    assert parallel["repository_mutation_authority"] is False
    assert parallel["may_execute_in_parallel"] is False
    assert parallel["final_validation_pass"] is True
    assert parallel["closeout"] == "governance/ai/work-state/MLR-01_CLOSEOUT_2026-09-10.json"

    paths = {(item["kind"], item["path"], item["lifecycle"]) for item in registry["current"]}
    assert all(kind not in {"machine_local_work_order", "machine_local_resource_manifest"} for kind, _, _ in paths)

    planned = {item["program"]: item for item in registry["planned_programs"]}
    assert planned["CNI"]["successor"] == "PCA-01"
    assert planned["PCA"]["successor"] == "SMB-08"
    assert planned["PCA"]["implementation_authority"] is False

    assert manifest["work_order_id"] == "MLR-01"
    assert manifest["status"] == "completed_verified"
    assert manifest["product_implementation_authority"] is False
    assert manifest["repository_mutation_authority"] is False
    assert manifest["architecture"] == "x86_64-amd64"
    assert manifest["tiers"]["D"]["intent"] == "registry_only_no_product_dependency_change"
    assert manifest["completion_summary"] == {
        "resource_count": 45,
        "installed_verified": 40,
        "already_installed_verified": 5,
        "conditional_deferred": 0,
        "blocked": 0,
        "final_validation_pass": True,
        "product_repositories_modified": False,
    }

    assert closeout["status"] == "completed_verified"
    assert closeout["authority_retirement"]["machine_local_execution_authority"] is False
    assert closeout["authority_retirement"]["current_work_pointer_modified"] is False
    assert closeout["completion_summary"]["tier_a_b_c_resource_count"] == 45

    for evidence in closeout["completion_evidence"].values():
        payload = (ROOT / evidence["path"]).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == evidence["sha256"]

    machine_manifest = load_json(closeout["completion_evidence"]["machine_manifest"]["path"])
    final_receipt = load_json(closeout["completion_evidence"]["final_validation_receipt"]["path"])
    assert len(machine_manifest["entries"]) == 45
    assert machine_manifest["product_repositories_modified"] is False
    assert final_receipt["pass"] is True
    assert final_receipt["resource_count"] == 45
