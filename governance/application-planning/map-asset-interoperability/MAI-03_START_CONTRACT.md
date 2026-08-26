# MAI-03 Governed Start Contract

This bounded start records the resolved implementation contract for **MAI-03 — Grid, Coordinates, Scale & Projection Engine**.

- Exact AIOC base: `fc0b4e8f82a1e1808d5b80b8b7f876aa66d3215f`
- Exact application base: `78c07e2102fdf6a7939a00a47b58e25150e66018`
- Implementation branch: `integration/mai-03-grid-coordinates-scale-projection-engine`
- World owner: MIB-11 / D18 World
- Provenance owner: D29 authoring-provenance

Authorized coordinate spaces are asset-local pixel, map pixel, grid coordinate and normalized map. Authorized projection families are square, gridless, flat/point hex, isometric and staggered. Authorized mechanics are deterministic pure coordinate projection/inversion, MAI-02 transform application/inversion, normalized-map conversion and explicit finite positive pixels-per-unit scale conversion.

Coordinates, transforms, scale and projections are presentation data only. They may not create World/location/topology/navigation or combat identity. MAI-04 connectivity/autotile semantics and all later MAI runtime/import/resolver/workbench/integration tranches remain unauthorized. Migration `0022` remains unreserved.
