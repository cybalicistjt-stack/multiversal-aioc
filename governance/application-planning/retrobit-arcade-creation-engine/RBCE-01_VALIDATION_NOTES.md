# RBCE-01 Validation Notes

This note records one implementation-facing distinction that must survive handoff: the JSON Schema is a structural gate, not the complete RBCE validator.

The application validator must still perform deterministic semantic checks for stable-ID uniqueness, internal reference resolution, scene graph integrity, delivery consistency, variable type/default consistency, campaign-projection authority, capability readiness, provenance/rights, blocking project tests, deterministic normalization, and playable-versus-publishable lifecycle separation.

The Four-Engine fixture is intended to be consumed by the eventual application test suite as an original/right-cleared golden fixture. Its use of top-down, fixed-room and side-scroll projection references proves format expressiveness only; RBCE-02 remains the owner of detailed 2D projection/physics semantics.

No file in this planning tranche grants application implementation authority or changes the currently selected OPS3 GPR work.
