import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"
INDEX = ROOT / "governance/ai/runtime/ROADMAP_INDEX.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
WORK_ORDER = ROOT / "governance/ai/runtime/LOCAL_EXECUTION_GATEWAY_WORK_ORDER.md"
SPEC = ROOT / "governance/application-planning/local-execution-gateway/LXG_LOCAL_EXECUTION_GATEWAY_SPEC.md"
AMENDMENT = ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_LXG_AMENDMENT_2026-09-10.md"


def _no_duplicate_json(path: Path):
    def pairs_hook(pairs):
        out = {}
        for key, value in pairs:
            assert key not in out, f"duplicate JSON key {key!r} in {path}"
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs_hook)


def test_lxg_is_parallel_not_product_selection():
    registry = _no_duplicate_json(REGISTRY)
    index = _no_duplicate_json(INDEX)
    pointer = _no_duplicate_json(POINTER)
    selected = pointer["active_attempt"]["work_item_id"]

    assert registry["active_planning_work"]["work_item"] == selected
    assert index["current"]["work_item_id"] == selected
    assert index["selected_ari"]["current"] == selected

    lxg = registry["parallel_developer_infrastructure"]
    assert lxg["work_item"] == "LXG-01"
    assert lxg["lifecycle"] == "CURRENT_COMPATIBLE"
    assert lxg["may_execute_in_parallel"] is True
    assert lxg["product_implementation_authority"] is False

    indexed = index["parallel_developer_infrastructure"]
    assert indexed["work_item_id"] == "LXG-01"
    assert indexed["product_order_change"] is False
    assert indexed["product_implementation_authority"] is False
    assert "LXG" not in index["effective_forward_order"]


def test_lxg_authority_is_registered_current_compatible():
    registry = _no_duplicate_json(REGISTRY)
    entries = {(item["kind"], item["path"]): item["lifecycle"] for item in registry["current"]}
    key = ("local_execution_gateway_work_order", "governance/ai/runtime/LOCAL_EXECUTION_GATEWAY_WORK_ORDER.md")
    assert entries[key] == "CURRENT_COMPATIBLE"


def test_lxg_phase1_has_no_general_remote_shell_or_filesystem():
    work_order = WORK_ORDER.read_text(encoding="utf-8")
    spec = SPEC.read_text(encoding="utf-8")
    amendment = AMENDMENT.read_text(encoding="utf-8")
    combined = "\n".join((work_order, spec, amendment)).lower()

    assert "no arbitrary shell" in combined
    assert "unrestricted filesystem" in combined
    assert "loopback" in combined
    assert "secure mcp tunnel" in combined
    assert "search" in work_order and "fetch" in work_order
    assert "local_model_query" in work_order
    assert "product-order change" in amendment or "product order change" in amendment


def test_lxg_scope_is_isolated_from_product_selector():
    registry = _no_duplicate_json(REGISTRY)
    pointer = _no_duplicate_json(POINTER)
    allowed = registry["parallel_developer_infrastructure"]["allowed_application_paths"]
    assert allowed == [
        "tools/local_execution_gateway/**",
        "tests/tools/local_execution_gateway/**",
        "docs/development/LXG-01-*.md",
    ]
    assert registry["active_planning_work"]["work_item"] == pointer["active_attempt"]["work_item_id"]
    assert registry["parallel_developer_infrastructure"]["product_implementation_authority"] is False
