import assert from 'node:assert/strict';
import { certifyChange, assertCertifiedChange } from './change-certification.mjs';

const base = {
  plan: { id: 'CHANGE-1', files: ['src/a.js', 'src/b.js'], risk: 'medium' },
  review: { files: ['src/a.js', 'src/b.js'], evidence: ['review://1'], findings: [] },
  validation: { files: ['src/a.js', 'src/b.js'], evidence: ['ci://1'], checks: [{ id: 'tests', status: 'pass' }] },
  continuity: { result: 'PASS', evidence: ['continuity://1'] },
  repositoryHealth: { status: 'healthy', evidence: ['repo://1'] }
};

const clone = value => JSON.parse(JSON.stringify(value));
const tests = [];
const test = (name, fn) => tests.push({ name, fn });

test('aligned change certifies PASS', () => assert.equal(certifyChange(base).result, 'PASS'));
test('missing plan blocks certification', () => assert.equal(certifyChange({ ...base, plan: null }).result, 'FAIL'));
test('continuity failure freezes execution', () => assert.equal(certifyChange({ ...base, continuity: { result: 'FAIL' } }).executionAllowed, false));
test('blocked repository health fails', () => assert.equal(certifyChange({ ...base, repositoryHealth: { status: 'blocked' } }).result, 'FAIL'));
test('missing review coverage fails', () => { const input = clone(base); input.review.files = ['src/a.js']; assert.equal(certifyChange(input).findings.some(x => x.code === 'review.coverage'), true); });
test('missing validation coverage fails', () => { const input = clone(base); input.validation.files = ['src/a.js']; assert.equal(certifyChange(input).findings.some(x => x.code === 'validation.coverage'), true); });
test('unresolved error finding blocks', () => { const input = clone(base); input.review.findings = [{ code: 'bug', severity: 'error', status: 'open' }]; assert.equal(certifyChange(input).result, 'FAIL'); });
test('unresolved warning yields PASS WITH WARNINGS', () => { const input = clone(base); input.review.findings = [{ code: 'note', severity: 'warning', status: 'open' }]; assert.equal(certifyChange(input).result, 'PASS WITH WARNINGS'); });
test('required failed check blocks', () => { const input = clone(base); input.validation.checks = [{ id: 'tests', status: 'fail' }]; assert.equal(certifyChange(input).result, 'FAIL'); });
test('optional failed check warns', () => { const input = clone(base); input.validation.checks = [{ id: 'lint', status: 'fail', required: false }]; assert.equal(certifyChange(input).result, 'PASS WITH WARNINGS'); });
test('high risk requires approval', () => { const input = clone(base); input.plan.risk = 'high'; assert.equal(certifyChange(input).findings.some(x => x.code === 'approval.high-risk'), true); });
test('assertion returns certified result', () => assert.equal(assertCertifiedChange(base).result, 'PASS'));
test('assertion throws governed error on failure', () => assert.throws(() => assertCertifiedChange({ ...base, continuity: { result: 'FAIL' } }), e => e.code === 'change.certification-failed'));

let failures = 0;
for (const { name, fn } of tests) {
  try { await fn(); console.log(`PASS ${name}`); }
  catch (error) { failures += 1; console.error(`FAIL ${name}`); console.error(error); }
}
console.log(`RESULT ${tests.length - failures}/${tests.length} passed`);
if (failures) process.exit(1);
