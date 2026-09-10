import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_local_first_overlay_is_current_without_selecting_product_work():
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    pointer = j("governance/ai/runtime/CURRENT_WORK_POINTER.json")
    roadmap = j("governance/ai/runtime/ROADMAP_INDEX.json")

    current_paths = {(x["kind"], x["lifecycle"], x["path"]) for x in registry["current"]}
    assert (
        "local_first_execution_overlay",
        "CURRENT",
        "governance/ai/MULTIVERSAL_LOCAL_FIRST_EXECUTION_OVERLAY.md",
    ) in current_paths

    assert registry["active_planning_work"]["work_item"] == pointer["active_attempt"]["work_item_id"]
    assert roadmap["current"]["work_item_id"] == pointer["active_attempt"]["work_item_id"]
    assert roadmap["execution_overlay"]["order_change"] is False
    assert "CNI-01..13 → PCA-01..16 → SMB-08" in roadmap["effective_forward_order"]

    overlay = t("governance/ai/MULTIVERSAL_LOCAL_FIRST_EXECUTION_OVERLAY.md")
    assert "CURRENT_WORK_POINTER.json" in overlay
    assert "Commodity non-reimplementation rule" in overlay
    assert "AI output remains proposal/candidate material" in overlay


def test_smb12_is_local_provider_first_but_provider_neutral():
    roadmap = j("governance/ai/runtime/ROADMAP_INDEX.json")
    amend = t("governance/application-planning/system-maturation-buildout/SMB-12_LOCAL_PROVIDER_FIRST_AMENDMENT_2026-09-10.md")

    strategy = roadmap["smb12_strategy_amendment"]
    assert strategy["first_real_provider"] == "local_provider_through_MIB-15"
    assert strategy["paid_provider_required_for_blocking_workflows"] is False
    assert "does **not** become canonical AI infrastructure" in amend
    assert "Provider-off baseline" in amend
    assert "Optional hosted provider(s)" in amend


def test_open_content_catalog_is_discovery_not_permission():
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    catalog = j("governance/application-planning/resource-source-catalog/OPEN_CONTENT_SOURCE_CATALOG.json")

    support = {x["catalog_id"]: x for x in registry["supporting_catalogs"]}["OCS-01"]
    assert support["asset_permission_authority"] is False
    assert catalog["catalog_id"] == "OCS-01"
    assert len(catalog["sources"]) >= 35

    by_id = {x["id"]: x for x in catalog["sources"]}
    assert by_id["poly_haven"]["rights_tier"] == "A"
    assert by_id["ambientcg"]["rights_tier"] == "A"
    assert by_id["sketchfab"]["rights_tier"] == "C"
    assert by_id["blendswap"]["rights_tier"] == "C"
    assert by_id["openstreetmap"]["rights_tier"] == "B"
    assert by_id["quaternius"]["rights_tier"] == "D"
    assert by_id["quaternius"]["redistribute_raw"] is False

    for source in catalog["sources"]:
        assert source["url"].startswith("https://")
        assert source["license_source"].startswith("https://")
        assert source["rights_tier"] in {"A", "B", "C", "D"}


def test_roadmap_amendment_preserves_order_and_ari_rights_owner():
    amend = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_LOCAL_FIRST_EXECUTION_AMENDMENT_2026-09-10.md")
    catalog_doc = t("governance/application-planning/resource-source-catalog/OPEN_CONTENT_SOURCE_CATALOG.md")

    assert "Roadmap order change:** none" in amend
    assert "ARI remains the owner of resource identity, provenance, rights/use capability and ingestion" in amend
    assert "Catalog membership is not asset permission" in catalog_doc
    assert "Continuously extensible" in catalog_doc or "continuously extensible" in catalog_doc
