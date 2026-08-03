import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const inputPath = process.argv[2] || 'governance/development-brain/orchestration-routing/AIOC_ORCHESTRATION_ROUTING.generated.json';
const file = path.isAbsolute(inputPath) ? inputPath : path.join(root, inputPath);
if (!fs.existsSync(file)) throw new Error(`Missing orchestration routing artifact: ${inputPath}`);
const data = JSON.parse(fs.readFileSync(file, 'utf8'));
const allowedStatuses = new Set(['routable', 'ambiguous', 'blocked', 'escalation-required']);
const allowedAuthority = new Set(['read-only', 'advisory', 'proposal-only']);
if (data.format !== 'multiversal-aioc-orchestration-routing') throw new Error('Invalid orchestration routing format.');
if (!Array.isArray(data.routes) || data.routes.length === 0) throw new Error('At least one route is required.');
const ids = new Set();
for (const route of data.routes) {
  if (!route.routeId || ids.has(route.routeId)) throw new Error(`Missing or duplicate routeId: ${route.routeId}`);
  ids.add(route.routeId);
  if (!allowedStatuses.has(route.status)) throw new Error(`Invalid status for ${route.routeId}`);
  if (!allowedAuthority.has(route.authorityMode)) throw new Error(`Invalid authority mode for ${route.routeId}`);
  if (!route.coordinatorRoleId || !route.handoff?.authorityPreserved) throw new Error(`Invalid coordinator handoff for ${route.routeId}`);
  if (!Array.isArray(route.reasons) || route.reasons.length === 0) throw new Error(`Missing reasons for ${route.routeId}`);
  if (!Array.isArray(route.evidence) || route.evidence.length === 0) throw new Error(`Missing evidence for ${route.routeId}`);
  if (route.status === 'routable' && (!route.selectedRoleId || route.handoff.toRoleId !== route.selectedRoleId)) throw new Error(`Routable route lacks valid selected role: ${route.routeId}`);
}
const authority = data.authority || {};
if (!authority.advisoryOnly || authority.executionAllowed || authority.canonicalMutationAllowed || authority.approvalGranted || authority.assignmentAllowed || authority.schedulingAllowed) throw new Error('Orchestration authority safeguards failed.');
console.log(`Validated ${data.routes.length} governed orchestration routes.`);
