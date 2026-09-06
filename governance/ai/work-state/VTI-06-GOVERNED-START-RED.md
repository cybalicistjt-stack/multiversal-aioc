# VTI-06 Governed-Start RED

This branch intentionally begins with a control-plane regression that requires VTI-06 to be `in_progress` with its bounded branch/implementation/acceptance authority opened while `production_mutation_authorized` and `scene_map_token_mai_bridge_authorized` remain `false`.

The current selected-only control plane is expected to fail that regression until the governed-start lifecycle projection is applied. This is a governance-registration RED only; no application branch or production implementation exists yet.
