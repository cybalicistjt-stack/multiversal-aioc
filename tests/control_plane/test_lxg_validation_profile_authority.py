import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json"
WORK_ORDER = ROOT / "governance/ai/runtime/LOCAL_EXECUTION_GATEWAY_WORK_ORDER.md"


def test_lxg_validation_profile_scope_is_narrow_and_non_product():
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    lxg = registry["parallel_developer_infrastructure"]
    assert lxg["work_item"] == "LXG-01"
    assert lxg["validation_profile"] == "LXG-01"
    assert lxg["validation_scope"] == "explicit_integration"
    assert lxg["product_implementation_authority"] is False
    assert lxg["allowed_application_paths"] == [
        "tools/local_execution_gateway/**",
        "tests/tools/local_execution_gateway/**",
        "docs/development/LXG-01-*.md",
        "governance/application-planning/validation-core/profiles/LXG-01.json",
        "governance/application-planning/validation-core/ACTIVE_FAMILY_CONTRACT.json",
    ]

    work_order = WORK_ORDER.read_text(encoding="utf-8")
    assert "explicit_integration_profiles" in work_order
    assert "must never become the ARI active family" in work_order
    assert "ARI family identity, remaining work, sealed proof and ordinary rules remain unchanged" in work_order
