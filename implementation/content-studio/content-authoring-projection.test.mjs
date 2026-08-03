import assert from 'node:assert/strict';
import { assertAuthoringAllowed, projectContentDraft } from './content-authoring-projection.mjs';

const base = {
  repositoryId: 'multiversal-aioc',
  branch: 'governance/session-bootstrap-v1',
  milestoneId: 'AIOC-I-005',
  workItemId: 'AIOC-I-005A',
  canonical: {
    repositoryId: 'multiversal-aioc',
    branch: 'governance/session-bootstrap-v1',
    workItemId: 'AIOC-I-005A',
  },
  continuity: { result: 'PASS', evidence: ['continuity://pass'] },
  repositoryHealth: { status: 'healthy', evidence: ['repo://healthy'] },
  knownEntityIds: ['rule.attack', 'species.human'],
  validation: { schemaValid: true, duplicateId: false, issues: [] },
  entity: {
    id: 'ability.precise-strike',
    type: 'ability',
    name: 'Precise Strike',
    schemaVersion: '1.0.0',
    payload: { cost: 2 },
    tags: ['combat', 'combat'],
    dependencies: ['rule.attack'],
    provenance: {
      sourceId: 'source.core-rules',
      sourceType: 'rulebook',
      sourceVersion: '1.0.0',
      locator: 'combat/precise-strike',
      evidence: ['source://core-rules'],
    },
  },
};

const tests = [];
function test(name, fn) { tests.push([name, fn]); }

test('valid draft produces PASS authoring projection', () => {
  const result = projectContentDraft(base);
  assert.equal(result.result, 'PASS');
  assert.equal(result.executionAllowed, true);
  assert.equal(result.authoringPlan.length, 5);
});

test('projection fingerprint is deterministic', () => {
  assert.equal(projectContentDraft(base).fingerprint, projectContentDraft(structuredClone(base)).fingerprint);
});

test('duplicate tags are normalized', () => {
  assert.deepEqual(projectContentDraft(base).entity.tags, ['combat']);
});

test('missing stable id blocks authoring', () => {
  const input = structuredClone(base);
  input.entity.id = '';
  assert.equal(projectContentDraft(input).executionAllowed, false);
});

test('continuity failure blocks authoring', () => {
  const input = structuredClone(base);
  input.continuity.result = 'FAIL';
  assert.equal(projectContentDraft(input).mode, 'recovery');
});

test('blocked repository health blocks authoring', () => {
  const input = structuredClone(base);
  input.repositoryHealth.status = 'blocked';
  assert.equal(projectContentDraft(input).result, 'FAIL');
});

test('repository drift is critical', () => {
  const input = structuredClone(base);
  input.repositoryId = 'multiversal-app';
  assert(projectContentDraft(input).findings.some((f) => f.code === 'REPOSITORY_BINDING_DRIFT'));
});

test('missing provenance field blocks authoring', () => {
  const input = structuredClone(base);
  delete input.entity.provenance.sourceVersion;
  assert(projectContentDraft(input).findings.some((f) => f.code === 'PROVENANCE_FIELD_MISSING'));
});

test('unresolved dependency blocks authoring', () => {
  const input = structuredClone(base);
  input.entity.dependencies.push('rule.unknown');
  assert(projectContentDraft(input).findings.some((f) => f.code === 'DEPENDENCY_UNRESOLVED'));
});

test('duplicate stable id blocks authoring', () => {
  const input = structuredClone(base);
  input.validation.duplicateId = true;
  assert.equal(projectContentDraft(input).executionAllowed, false);
});

test('warning-only validation passes with warnings', () => {
  const input = structuredClone(base);
  input.validation.issues = [{ code: 'STYLE_WARNING', severity: 'warning', message: 'Review wording.' }];
  assert.equal(projectContentDraft(input).result, 'PASS WITH WARNINGS');
});

test('assertion freezes blocked projection', () => {
  const input = structuredClone(base);
  input.validation.schemaValid = false;
  assert.throws(() => assertAuthoringAllowed(projectContentDraft(input)), { code: 'CONTENT_AUTHORING_FROZEN' });
});

let passed = 0;
for (const [name, fn] of tests) {
  try {
    await fn();
    passed += 1;
    console.log(`PASS ${name}`);
  } catch (error) {
    console.error(`FAIL ${name}`);
    throw error;
  }
}
console.log(`RESULT ${passed}/${tests.length} passed`);
