import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def test_mlr_is_parallel_and_does_not_replace_product_authority():
    registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    pointer = load_json("governance/ai/runtime/CURRENT_WORK_POINTER.json")
    manifest = load_json("governance/ai/runtime/LOCAL_WORKSTATION_RESOURCE_MANIFEST.json")

    # MLR must coexist with whichever product tranche is canonical now; it must not
    # hard-code or replace that selection merely because product work advances.
    assert registry["active_planning_work"]["work_item"] == pointer["active_attempt"]["work_item_id"]
    assert registry["active_planning_work"]["implementation_authority"] == pointer["active_attempt"]["implementation_authority"]

    parallel = registry["parallel_machine_local_work"]
    assert parallel["work_item"] == "MLR-01"
    assert parallel["lifecycle"] == "CURRENT_COMPATIBLE"
    assert parallel["product_implementation_authority"] is False
    assert parallel["repository_mutation_authority"] is False
    assert parallel["may_execute_in_parallel"] is True

    paths = {(item["kind"], item["path"], item["lifecycle"]) for item in registry["current"]}
    assert ("machine_local_work_order", "governance/ai/runtime/LOCAL_WORKSTATION_RESOURCE_ACQUISITION_WORK_ORDER.md", "CURRENT_COMPATIBLE") in paths
    assert ("machine_local_resource_manifest", "governance/ai/runtime/LOCAL_WORKSTATION_RESOURCE_MANIFEST.json", "CURRENT_COMPATIBLE") in paths

    planned = {item["program"]: item for item in registry["planned_programs"]}
    assert planned["CNI"]["successor"] == "PCA-01"
    assert planned["PCA"]["successor"] == "SMB-08"
    assert planned["PCA"]["implementation_authority"] is False

    assert manifest["work_order_id"] == "MLR-01"
    assert manifest["product_implementation_authority"] is False
    assert manifest["repository_mutation_authority"] is False
    assert manifest["architecture"] == "x86_64-amd64"
    assert manifest["tiers"]["D"]["intent"] == "registry_only_no_product_dependency_change"
