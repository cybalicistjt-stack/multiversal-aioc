import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def j(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def t(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_pca_registered_as_future_interstitial_without_activation():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = j("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = j("governance/application-planning/production-capability-acceleration/PCA_PROGRAM_BACKLOG.json")

    planned = {x["program_id"]: x for x in index["planned_programs"]}
    assert planned["PCA"]["status"] == "owner_approved_planned"
    assert planned["PCA"]["activation_after"] == "CNI-13"
    assert planned["PCA"]["successor"] == "SMB-08"
    assert planned["PCA"]["implementation_authority"] is False
    assert planned["PCA"]["execution_units"] == 16

    assert index["current"]["work_item_id"] == "ARI-04"
    assert index["current"]["source_program"] == "ARI"
    assert index["current"]["implementation_authority"] is True
    assert index["selected_ari"]["current"] == "ARI-04"
    assert index["selected_ari"]["current_state"] == "in_progress"

    reg = {x["program"]: x for x in registry["planned_programs"]}
    assert reg["PCA"]["state"] == "owner_approved_planned"
    assert reg["PCA"]["activation_after"] == "CNI-13"
    assert reg["PCA"]["successor"] == "SMB-08"
    assert reg["PCA"]["implementation_authority"] is False
    assert registry["family_preflight"]["family_id"] == "ARI"

    assert backlog["implementation_authority"] is False
    assert backlog["strict_order"] == [f"PCA-{i:02d}" for i in range(1, 17)]
    assert all(x["estimated_active_minutes"] <= 24 for x in backlog["tranches"])


def test_pca_dependency_placement_is_stable():
    index = j("governance/ai/runtime/ROADMAP_INDEX.json")
    assert "SMB-01..07 → CNI-01..13 → PCA-01..16 → SMB-08 → SMB-09" in index["effective_forward_order"]
    assert index["cni_execution_order"][-1] == "CNI-13"
    assert index["pca_execution_order"][0] == "PCA-01"
    assert index["pca_execution_order"][-1] == "PCA-16"

    amendment = t("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_PCM_PCA_AMENDMENT_2026-09-09.md")
    smb = t("governance/application-planning/system-maturation-buildout/SMB_PCA_INTERSTITIAL_INTEGRATION_AMENDMENT_2026-09-09.md")
    assert "CNI-01..13 → PCA-01..16 → SMB-08" in amendment
    assert "CNI-01..13 → PCA-01..16 → SMB-08" in smb


def test_pcm_catalog_and_clean_room_boundaries():
    catalog = j("governance/application-planning/proprietary-capability-mining/PCM_PRODUCT_CAPABILITY_CATALOG.json")
    clean = t("governance/application-planning/proprietary-capability-mining/PCM_CLEAN_ROOM_AND_RIGHTS_RULES.md").lower()
    pca = t("governance/application-planning/production-capability-acceleration/PCA_PRODUCTION_CAPABILITY_ACCELERATION_PROGRAM.md").lower()

    assert len(catalog["products"]) == 48
    allowed = {"USE_AS_IS", "LICENSE_TEMPORARILY", "STUDY_PATTERNS", "BUILD_MULTIVERSAL_NATIVE", "IGNORE"}
    assert {x["classification"] for x in catalog["products"]} <= allowed
    assert len({x["id"] for x in catalog["products"]}) == 48
    assert all(x["source"].startswith("https://") for x in catalog["products"])

    for phrase in ("do not decompile", "reverse engineer", "public availability alone is insufficient"):
        assert phrase in clean
    assert "clone commercial products" in pca and "not" in pca[: pca.index("clone commercial products")]
    assert "build another vcs" in pca and "not" in pca[max(0, pca.index("build another vcs") - 40): pca.index("build another vcs")]


def test_pca_preserves_existing_owner_domains():
    backlog = j("governance/application-planning/production-capability-acceleration/PCA_PROGRAM_BACKLOG.json")
    boundaries = "\n".join(backlog["boundaries"]).lower()
    for owner in ("ari", "aai", "dwc", "cni", "action/event", "smb-16", "smb-13/brp"):
        assert owner in boundaries
