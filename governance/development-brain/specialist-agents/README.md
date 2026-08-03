# Specialist Agent Contracts

Release F Step 16 defines bounded specialist roles for the Multiversal Development Brain.

## Contract purpose

Each specialist contract declares a stable role and contract identity, domain scope, responsibilities, required inputs, permitted outputs, evidence requirements, escalation triggers, deterministic handoff requirements, prohibited actions, and authority mode.

The contracts make specialization explicit without granting autonomy beyond existing governance.

## Included specialist roles

- Knowledge Librarian
- Rules and Mechanics Architect
- Setting and Lore Architect
- Content and Pack Architect
- Application and UX Architect
- Verification and Testing Agent
- Governance and Provenance Agent
- Development Coordinator

## Handoff model

The Development Coordinator routes a bounded task context to the narrowest supported specialist. Specialists return findings, evidence, confidence, unresolved questions, and escalation status. Every handoff preserves the authority of the originating sources and may not upgrade read-only or advisory information into executable authority.

Direct specialist-to-specialist execution chains are not authorized by Step 16. Cross-domain work returns to the coordinator for governed routing and later synthesis.

## Diagnostics

The generated artifact reports role overlap, missing capabilities, circular handoffs, unsupported specialization, and authority conflicts. Overlap is visible and requires routing by required output and narrowest responsibility; it is not silently resolved by one specialist claiming another specialist's domain.

## Authority boundary

Specialists are read-only, advisory, or proposal-only. They cannot mutate canonical content, execute work, grant approval, promote or certify content, assign tasks, schedule actions, conceal uncertainty, or exceed source authority.

Step 16 defines contracts only. Runtime orchestration, dispatch, agent execution, and multi-agent synthesis belong to later governed steps.
