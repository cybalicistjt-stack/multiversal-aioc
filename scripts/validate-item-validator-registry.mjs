import fs from 'node:fs';

const templates = JSON.parse(fs.readFileSync('governance/object-system/item-templates/ITEM_TEMPLATE_REGISTRY.json', 'utf8'));
const validators = JSON.parse(fs.readFileSync('governance/object-system/item-validators/ITEM_VALIDATOR_REGISTRY.json', 'utf8'));
const failures = [];

if (validators.format !== 'multiversal-item-validator-registry') failures.push('unsupported validator registry format');
if (validators.workstream !== '8E-009J') failures.push('wrong workstream');
const templateIds = new Set(templates.templates.map(template => template.templateId));
const validatorIds = new Set(validators.validators.map(validator => validator.templateId));
if (validatorIds.size !== validators.validators.length) failures.push('duplicate validator template ID');
for (const id of templateIds) if (!validatorIds.has(id)) failures.push(`missing validator for ${id}`);
for (const id of validatorIds) if (!templateIds.has(id)) failures.push(`validator references unknown template ${id}`);
for (const validator of validators.validators) {
  if (!validator.requiredChecks?.length) failures.push(`${validator.templateId}: required checks missing`);
  if (!validator.runtimeChecks?.length) failures.push(`${validator.templateId}: runtime checks missing`);
  if (!Array.isArray(validator.blockingAmbiguities)) failures.push(`${validator.templateId}: blocking ambiguities missing`);
}
const weights = validators.completionScoring;
const totalWeight = weights.requiredFieldCoverageWeight + weights.applicableConditionalCoverageWeight + weights.fieldProvenanceWeight + weights.relationshipAndCompatibilityWeight + weights.runtimeBehaviorCoverageWeight + weights.ambiguityResolutionWeight;
if (totalWeight !== 100) failures.push('completion weights must total 100');
if (weights.thresholds.promotionReadyMinimum !== 100) failures.push('promotion-ready threshold must be 100');
if (!validators.promotionGates?.includes('owner approval recorded for exact fingerprint')) failures.push('owner approval gate missing');
if (!validators.boundary?.includes('does not promote content')) failures.push('safety boundary missing');

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log(`Item validator registry validated: ${validators.validators.length} template validators.`);
