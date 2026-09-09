import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load_text(path: str):
    return (ROOT / path).read_text(encoding="utf-8")


def test_cni_program_is_registered_without_runtime_activation():
    index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
    registry = load_json("governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json")
    backlog = load_json("governance/application-planning/content-narrative-interoperability/CNI_PROGRAM_BACKLOG.json")

    planned = {item["program_id"]: item for item in index["planned_programs"]}
    assert "CNI" in planned
    assert planned["CNI"]["activation_after"] == "SMB-07"
    assert planned["CNI"]["successor"] == "PCA-01"
    assert planned["CNI"]["implementation_authority"] is False
    assert planned["CNI"]["execution_units"] == 13

    assert index["current"]["work_item_id"] == "ARI-04"
    assert index["current"]["source_program"] == "ARI"
    assert index["current"]["implementation_authority"] is True

    registry_planned = {item["program"]: item for item in registry["planned_programs"]}
    assert registry_planned["CNI"]["state"] == "owner_approved_planned"
    assert registry_planned["CNI"]["activation_after"] == "SMB-07"
    assert registry_planned["CNI"]["successor"] == "PCA-01"
    assert registry_planned["CNI"]["implementation_authority"] is False
    assert registry["family_preflight"]["family_id"] == "ARI"

    assert backlog["status"] == "owner_approved_planned"
    assert backlog["implementation_authority"] is False
    assert backlog["successor"] == "PCA-01"
    assert backlog["strict_order"] == [f"CNI-{i:02d}" for i in range(1, 14)]
    assert all(item["estimated_active_minutes"] <= 24 for item in backlog["tranches"])


def test_cni_is_interstitial_between_smb07_and_pca():
    index = load_json("governance/ai/runtime/ROADMAP_INDEX.json")
    pca_amendment = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_PCM_PCA_AMENDMENT_2026-09-09.md")
    cni_successor_amendment = load_text("governance/application-planning/content-narrative-interoperability/CNI_PCA_SUCCESSOR_AMENDMENT_2026-09-09.md")
    program = load_text("governance/application-planning/content-narrative-interoperability/CNI_CONTENT_NARRATIVE_INTEROPERABILITY_PROGRAM.md")

    order = index["effective_forward_order"]
    assert "SMB-01..07 → CNI-01..13 → PCA-01..16 → SMB-08 → SMB-09" in order
    assert "SMB-07 → CNI-01..13 → PCA-01..16 → SMB-08" in pca_amendment
    assert "SMB-07 → CNI-01..13 → PCA-01..16 → SMB-08" in cni_successor_amendment

    assert "CNI-01 — Content Pack Manifest" in program
    assert "CNI-05 — Executable Dialogue Graph" in program
    assert "CNI-09 — Cross-Pack Extension" in program
    assert "CNI-10 — Localization Resource Separation" in program
    assert "CNI-13 — Golden Multi-Pack Narrative Compatibility Proof" in program


def test_reference_study_does_not_authorize_copyrighted_reuse():
    program = load_text("governance/application-planning/content-narrative-interoperability/CNI_CONTENT_NARRATIVE_INTEROPERABILITY_PROGRAM.md")
    amendment = load_text("governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP_CNI_AMENDMENT_2026-09-09.md")

    assert "no direct copying" in program.lower()
    assert "pattern study only" in amendment.lower()
    assert "Baldur's Gate/Forgotten Realms" in program
