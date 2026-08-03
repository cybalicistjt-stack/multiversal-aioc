import express from 'express';
import crypto from 'node:crypto';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { z } from 'zod';

const PORT = Number(process.env.PORT || 8787);
const REPOSITORY = process.env.AIOC_GITHUB_REPOSITORY || 'cybalicistjt-stack/multiversal-aioc';
const REF = process.env.AIOC_GITHUB_REF || 'main';
const GITHUB_TOKEN = process.env.GITHUB_TOKEN || '';
const ALLOW_WRITES = process.env.AIOC_ALLOW_WRITES === 'true';
const BRIDGE_TOKEN = process.env.AIOC_BRIDGE_TOKEN || '';
const PUBLIC_BASE = (process.env.AIOC_PUBLIC_BASE || 'https://cybalicistjt-stack.github.io/multiversal-aioc').replace(/\/$/, '');
const RAW_BASE = `https://raw.githubusercontent.com/${REPOSITORY}/${REF}`;
const API_BASE = `https://api.github.com/repos/${REPOSITORY}`;
const SHARED_STATE_PATH = 'governance/shared-state/AIOC_SHARED_STATE.json';
const MAX_FETCH_BYTES = 1_000_000;

const app = express();
app.use(express.json({ limit: '6mb' }));

function githubHeaders() {
  return {
    Accept: 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    ...(GITHUB_TOKEN ? { Authorization: `Bearer ${GITHUB_TOKEN}` } : {})
  };
}

function authorized(req) {
  if (!BRIDGE_TOKEN) return true;
  const header = req.headers.authorization || '';
  return header === `Bearer ${BRIDGE_TOKEN}`;
}

function requireBridgeAuth(req, res, next) {
  if (!authorized(req)) return res.status(401).json({ error: 'Unauthorized AIOC bridge request.' });
  next();
}

async function fetchResponse(url, options = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), options.timeoutMs || 20_000);
  try {
    return await fetch(url, {
      redirect: 'follow',
      cache: 'no-store',
      ...options,
      signal: controller.signal,
      headers: { ...(options.headers || {}) }
    });
  } finally {
    clearTimeout(timer);
  }
}

async function fetchText(url, options = {}) {
  const response = await fetchResponse(url, options);
  if (!response.ok) throw new Error(`${url} returned ${response.status}`);
  const text = await response.text();
  if (Buffer.byteLength(text, 'utf8') > MAX_FETCH_BYTES) throw new Error(`${url} exceeded the ${MAX_FETCH_BYTES}-byte inspection limit.`);
  return text;
}

async function fetchJson(url, options = {}) {
  return JSON.parse(await fetchText(url, options));
}

async function contentDatabase() {
  const db = await fetchJson(`${RAW_BASE}/content-db/index.json`, { headers: githubHeaders() });
  if (!Array.isArray(db.records)) throw new Error('AIOC content database has no records array.');
  return db;
}

function recordId(record) {
  return record?.stableId || record?.refId || record?.databaseId || record?.catalogId || record?.id;
}

function compactRecord(record) {
  return {
    id: recordId(record),
    name: record.name,
    objectType: record.objectType || record.contentType || record.objectKind,
    stage: record.developmentStage || record.stage,
    source: record.source || record.provenance?.authority || record.provenance?.source,
    dependencies: record.dependencies || [],
    hasBody: Boolean(record.gameObject || record.object || record.content || record.spec)
  };
}

function toolResult(data, summary) {
  return { structuredContent: data, content: [{ type: 'text', text: summary }] };
}

function requireWrites() {
  if (!ALLOW_WRITES) throw new Error('AIOC write actions are disabled on this bridge.');
  if (!GITHUB_TOKEN) throw new Error('GITHUB_TOKEN is required for AIOC writes.');
}

async function readRepositoryJson(path) {
  if (!GITHUB_TOKEN) {
    return { value: await fetchJson(`${RAW_BASE}/${path}`), sha: null };
  }
  const response = await fetchResponse(`${API_BASE}/contents/${path}?ref=${encodeURIComponent(REF)}`, { headers: githubHeaders() });
  if (!response.ok) throw new Error(`GitHub read ${path} returned ${response.status}: ${await response.text()}`);
  const payload = await response.json();
  const decoded = Buffer.from(payload.content.replace(/\n/g, ''), 'base64').toString('utf8');
  return { value: JSON.parse(decoded), sha: payload.sha };
}

async function writeRepositoryJson(path, value, sha, message) {
  requireWrites();
  const response = await fetchResponse(`${API_BASE}/contents/${path}`, {
    method: 'PUT',
    headers: { ...githubHeaders(), 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message,
      content: Buffer.from(`${JSON.stringify(value, null, 2)}\n`).toString('base64'),
      branch: REF,
      ...(sha ? { sha } : {})
    })
  });
  if (!response.ok) throw new Error(`GitHub write ${path} returned ${response.status}: ${await response.text()}`);
  return response.json();
}

async function mutateSharedState({ expectedRevision, actor, reason, mutate }) {
  requireWrites();
  const { value: state, sha } = await readRepositoryJson(SHARED_STATE_PATH);
  if (expectedRevision !== undefined && expectedRevision !== state.revision) {
    throw new Error(`Shared-state revision conflict: expected ${expectedRevision}, current ${state.revision}. Reload before writing.`);
  }
  const beforeRevision = Number(state.revision || 0);
  await mutate(state);
  state.revision = beforeRevision + 1;
  state.updatedAt = new Date().toISOString();
  state.updatedBy = actor;
  state.history = Array.isArray(state.history) ? state.history : [];
  state.history.push({ revision: state.revision, at: state.updatedAt, actor, reason });
  state.history = state.history.slice(-250);
  const result = await writeRepositoryJson(SHARED_STATE_PATH, state, sha, `bridge state: r${state.revision} ${reason}`);
  return { state, commitSha: result.commit?.sha || null };
}

async function latestRepositoryCommit() {
  const response = await fetchResponse(`${API_BASE}/commits/${encodeURIComponent(REF)}`, { headers: githubHeaders() });
  if (!response.ok) throw new Error(`GitHub commit lookup returned ${response.status}`);
  const commit = await response.json();
  return { sha: commit.sha, committedAt: commit.commit?.committer?.date || null, message: commit.commit?.message || '' };
}

function extractHtmlSummary(html) {
  const title = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i)?.[1]?.trim() || null;
  const links = [...html.matchAll(/<a\b[^>]*href=["']([^"']+)["']/gi)].map(match => match[1]);
  const scripts = [...html.matchAll(/<script\b[^>]*src=["']([^"']+)["']/gi)].map(match => match[1]);
  const stylesheets = [...html.matchAll(/<link\b[^>]*rel=["']stylesheet["'][^>]*href=["']([^"']+)["']/gi)].map(match => match[1]);
  const text = html.replace(/<script[\s\S]*?<\/script>/gi, ' ').replace(/<style[\s\S]*?<\/style>/gi, ' ').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
  return { title, links: [...new Set(links)], scripts: [...new Set(scripts)], stylesheets: [...new Set(stylesheets)], textPreview: text.slice(0, 1000) };
}

async function inspectLiveResource(path, expectText = []) {
  const safePath = String(path || '/').startsWith('/') ? String(path || '/') : `/${path}`;
  const url = `${PUBLIC_BASE}${safePath}`;
  const started = Date.now();
  try {
    const response = await fetchResponse(url);
    const contentType = response.headers.get('content-type') || '';
    const body = await response.text();
    const checks = expectText.map(value => ({ value, found: body.includes(value) }));
    return {
      path: safePath,
      url,
      ok: response.ok && checks.every(check => check.found),
      status: response.status,
      contentType,
      bytes: Buffer.byteLength(body, 'utf8'),
      durationMs: Date.now() - started,
      checks,
      html: contentType.includes('text/html') ? extractHtmlSummary(body) : undefined,
      json: contentType.includes('json') ? JSON.parse(body) : undefined
    };
  } catch (error) {
    return { path: safePath, url, ok: false, status: null, durationMs: Date.now() - started, error: String(error?.message || error) };
  }
}

async function verifyLiveAioc(expectedCommit) {
  const checks = await Promise.all([
    inspectLiveResource('/', ['operational']),
    inspectLiveResource('/operational/', ['Multiversal']),
    inspectLiveResource('/operational/health.json'),
    inspectLiveResource('/deployed-build.json'),
    inspectLiveResource('/content-assistant.html', ['Content Completion Assistant']),
    inspectLiveResource('/content-structure.html', ['Content Structure']),
    inspectLiveResource('/content-library.html', ['Content Library']),
    inspectLiveResource('/studio.html', ['Design Studio']),
    inspectLiveResource('/content-db/index.json')
  ]);
  const byPath = Object.fromEntries(checks.map(check => [check.path, check]));
  const health = byPath['/operational/health.json']?.json || null;
  const deployed = byPath['/deployed-build.json']?.json || null;
  const contentDb = byPath['/content-db/index.json']?.json || null;
  const repository = await latestRepositoryCommit().catch(error => ({ error: String(error?.message || error) }));
  const targetCommit = expectedCommit || repository.sha || null;
  const commitMatches = Boolean(targetCommit && (deployed?.commit === targetCommit || health?.commit === targetCommit));
  const recordCount = Array.isArray(contentDb?.records) ? contentDb.records.length : contentDb?.recordCount;
  const recordCountValid = recordCount === 487;
  const failed = checks.filter(check => !check.ok).map(check => ({ path: check.path, status: check.status, error: check.error, checks: check.checks }));
  if (!commitMatches) failed.push({ path: 'deployment-commit', expected: targetCommit, deployed: deployed?.commit || health?.commit || null });
  if (!recordCountValid) failed.push({ path: 'content-record-count', expected: 487, actual: recordCount ?? null });
  return {
    result: failed.length ? 'FAIL' : 'PASS',
    publicBase: PUBLIC_BASE,
    expectedCommit: targetCommit,
    deployedCommit: deployed?.commit || health?.commit || null,
    repository,
    commitMatches,
    recordCount,
    recordCountValid,
    checkedAt: new Date().toISOString(),
    checks,
    failed
  };
}

async function createProposalFile({ title, summary, proposedChanges, affectedIds }) {
  requireWrites();
  const now = new Date();
  const stamp = now.toISOString().replace(/[:.]/g, '-');
  const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60) || 'proposal';
  const path = `governance/bridge-proposals/${stamp}-${slug}.json`;
  const body = {
    format: 'multiversal-aioc-bridge-proposal',
    version: '1.0.0',
    proposalId: crypto.randomUUID(),
    createdAt: now.toISOString(),
    createdBy: 'multiversal-aioc-mcp-bridge',
    status: 'PROPOSED',
    title,
    summary,
    affectedIds,
    proposedChanges
  };
  const result = await writeRepositoryJson(path, body, null, `bridge: propose ${title}`);
  return { proposal: body, path, commitSha: result.commit?.sha || null };
}

function buildServer() {
  const server = new McpServer({ name: 'multiversal-aioc', version: '0.3.0' });

  server.registerTool('aioc_status', {
    title: 'Get AIOC status',
    description: 'Use this when you need live deployment health, repository state, shared-state revision, and bridge availability.',
    inputSchema: {},
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: true, idempotentHint: true }
  }, async () => {
    const [manifest, health, shared, repository] = await Promise.all([
      fetchJson(`${PUBLIC_BASE}/deployed-build.json`).catch(() => null),
      fetchJson(`${PUBLIC_BASE}/operational/health.json`).catch(() => null),
      readRepositoryJson(SHARED_STATE_PATH).then(item => item.value).catch(() => null),
      latestRepositoryCommit().catch(() => null)
    ]);
    const data = {
      repository: { name: REPOSITORY, ref: REF, latest: repository },
      publicBase: PUBLIC_BASE,
      manifest,
      health,
      deploymentMatchesRepository: Boolean(repository?.sha && (manifest?.commit === repository.sha || health?.commit === repository.sha)),
      sharedState: shared ? {
        revision: shared.revision,
        updatedAt: shared.updatedAt,
        workingObjectCount: shared.workingObjects?.length || 0,
        structureDecisionCount: Object.keys(shared.structureDecisions || {}).length
      } : null,
      bridge: { version: '0.3.0', writesEnabled: ALLOW_WRITES && Boolean(GITHUB_TOKEN), authenticationEnabled: Boolean(BRIDGE_TOKEN) }
    };
    return toolResult(data, `AIOC bridge is connected to ${REPOSITORY}@${REF}; live deployment match is ${data.deploymentMatchesRepository ? 'confirmed' : 'not confirmed'}.`);
  });

  server.registerTool('verify_live_aioc', {
    title: 'Verify live AIOC deployment',
    description: 'Use this after an AIOC update to inspect live routes, compare the deployed commit to GitHub, validate the certified content count, and return PASS or FAIL evidence.',
    inputSchema: { expectedCommit: z.string().regex(/^[a-f0-9]{40}$/i).optional() },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: true, idempotentHint: true }
  }, async ({ expectedCommit }) => {
    const report = await verifyLiveAioc(expectedCommit);
    return toolResult({ report }, `Live AIOC verification ${report.result}: ${report.failed.length} failed check${report.failed.length === 1 ? '' : 's'}.`);
  });

  server.registerTool('inspect_live_aioc_resource', {
    title: 'Inspect live AIOC resource',
    description: 'Use this when you need to inspect one deployed AIOC page, JSON endpoint, script, or asset and confirm expected text is present.',
    inputSchema: {
      path: z.string().min(1).max(300),
      expectText: z.array(z.string().min(1).max(200)).max(20).default([])
    },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: true, idempotentHint: true }
  }, async ({ path, expectText }) => {
    const inspection = await inspectLiveResource(path, expectText);
    return toolResult({ inspection }, `${inspection.path} returned ${inspection.status ?? 'no status'} and ${inspection.ok ? 'passed' : 'failed'} inspection.`);
  });

  server.registerTool('search_aioc_content', {
    title: 'Search AIOC content',
    description: 'Use this when you need to find canonical Multiversal content records by name, ID, type, source, or text.',
    inputSchema: { query: z.string().min(1), objectType: z.string().optional(), limit: z.number().int().min(1).max(100).default(25) },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async ({ query, objectType, limit }) => {
    const db = await contentDatabase();
    const q = query.toLowerCase();
    const records = db.records
      .filter(record => !objectType || (record.objectType || record.contentType) === objectType)
      .filter(record => JSON.stringify([recordId(record), record.name, record.objectType, record.contentType, record.source, record.tags, record.gameObject]).toLowerCase().includes(q))
      .slice(0, limit)
      .map(compactRecord);
    return toolResult({ query, count: records.length, records }, `Found ${records.length} AIOC content record${records.length === 1 ? '' : 's'}.`);
  });

  server.registerTool('get_aioc_object', {
    title: 'Get AIOC object',
    description: 'Use this when you need the complete canonical record for one stable ID.',
    inputSchema: { id: z.string().min(1) },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async ({ id }) => {
    const db = await contentDatabase();
    const record = db.records.find(item => recordId(item) === id);
    if (!record) throw new Error(`No AIOC object found for ${id}.`);
    return toolResult({ record }, `Loaded ${record.name || id}.`);
  });

  server.registerTool('get_aioc_current_state', {
    title: 'Get AIOC current state',
    description: 'Use this when you need canonical AIOC operating state, active work, constraints, or handoff context.',
    inputSchema: {},
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async () => toolResult({ markdown: await fetchText(`${RAW_BASE}/governance/current-state/AIOC_CURRENT_STATE.md`, { headers: githubHeaders() }) }, 'Loaded the canonical AIOC current-state record.'));

  server.registerTool('get_aioc_shared_state', {
    title: 'Get shared AIOC working state',
    description: 'Use this when you need shared drafts, structure decisions, packs, evidence, review queue, or the revision shared by the browser, ChatGPT, and Codex.',
    inputSchema: { includeHistory: z.boolean().default(false) },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async ({ includeHistory }) => {
    const { value } = await readRepositoryJson(SHARED_STATE_PATH);
    const state = includeHistory ? value : { ...value, history: undefined };
    return toolResult({ state }, `Loaded shared AIOC state revision ${value.revision}.`);
  });

  server.registerTool('list_aioc_working_objects', {
    title: 'List shared AIOC working objects',
    description: 'Use this when you need drafts and game-object work shared across AIOC, ChatGPT, and Codex.',
    inputSchema: { query: z.string().optional(), stage: z.string().optional(), limit: z.number().int().min(1).max(200).default(50) },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async ({ query, stage, limit }) => {
    const { value } = await readRepositoryJson(SHARED_STATE_PATH);
    const q = query?.toLowerCase();
    const objects = (value.workingObjects || [])
      .filter(item => !stage || item.developmentStage === stage)
      .filter(item => !q || JSON.stringify([recordId(item), item.name, item.objectType, item.description, item.tags]).toLowerCase().includes(q))
      .slice(0, limit)
      .map(compactRecord);
    return toolResult({ revision: value.revision, count: objects.length, objects }, `Found ${objects.length} shared working object${objects.length === 1 ? '' : 's'}.`);
  });

  server.registerTool('get_aioc_working_object', {
    title: 'Get shared AIOC working object',
    description: 'Use this when you need the complete editable working object for one stable ID.',
    inputSchema: { id: z.string().min(1) },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async ({ id }) => {
    const { value } = await readRepositoryJson(SHARED_STATE_PATH);
    const object = (value.workingObjects || []).find(item => recordId(item) === id);
    if (!object) throw new Error(`No shared working object found for ${id}.`);
    return toolResult({ revision: value.revision, object }, `Loaded shared working object ${object.name || id}.`);
  });

  server.registerTool('upsert_aioc_working_object', {
    title: 'Create or update shared AIOC working object',
    description: 'Use this when the user approves saving a draft or revision into shared AIOC state. This does not alter canonical content.',
    inputSchema: {
      expectedRevision: z.number().int().min(0),
      actor: z.string().min(1).max(120),
      object: z.object({ id: z.string().min(1), name: z.string().min(1), objectType: z.string().min(1), developmentStage: z.string().default('Draft') }).passthrough()
    },
    annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async ({ expectedRevision, actor, object }) => {
    const result = await mutateSharedState({
      expectedRevision,
      actor,
      reason: `upsert working object ${object.id}`,
      mutate: state => {
        state.workingObjects = Array.isArray(state.workingObjects) ? state.workingObjects : [];
        const index = state.workingObjects.findIndex(item => recordId(item) === object.id);
        const stamped = { ...object, stableId: object.stableId || object.id, updatedAt: new Date().toISOString(), updatedBy: actor };
        if (index >= 0) state.workingObjects[index] = { ...state.workingObjects[index], ...stamped };
        else state.workingObjects.push(stamped);
      }
    });
    return toolResult({ revision: result.state.revision, object: result.state.workingObjects.find(item => recordId(item) === object.id), commitSha: result.commitSha }, `Saved ${object.name} to shared AIOC state revision ${result.state.revision}.`);
  });

  server.registerTool('record_aioc_structure_decision', {
    title: 'Record AIOC content structure decision',
    description: 'Use this when the user approves classifying a source record as standalone, reusable generic, parent component, granted variant, duplicate, or obsolete.',
    inputSchema: {
      expectedRevision: z.number().int().min(0),
      actor: z.string().min(1).max(120),
      sourceId: z.string().min(1),
      classification: z.enum(['standalone', 'reusable-generic', 'parent-component', 'granted-variant', 'duplicate', 'obsolete']),
      targetId: z.string().optional(),
      notes: z.string().max(4000).default('')
    },
    annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async input => {
    const result = await mutateSharedState({
      expectedRevision: input.expectedRevision,
      actor: input.actor,
      reason: `classify ${input.sourceId} as ${input.classification}`,
      mutate: state => {
        state.structureDecisions = state.structureDecisions || {};
        state.structureDecisions[input.sourceId] = {
          sourceId: input.sourceId,
          classification: input.classification,
          targetId: input.targetId || null,
          notes: input.notes,
          decidedAt: new Date().toISOString(),
          decidedBy: input.actor
        };
      }
    });
    return toolResult({ revision: result.state.revision, decision: result.state.structureDecisions[input.sourceId], commitSha: result.commitSha }, `Recorded structure decision for ${input.sourceId}.`);
  });

  server.registerTool('create_aioc_change_proposal', {
    title: 'Create AIOC change proposal',
    description: 'Use this when the user approves recording a governed, reviewable proposal. This does not directly alter canonical content.',
    inputSchema: {
      title: z.string().min(3).max(160),
      summary: z.string().min(10).max(4000),
      proposedChanges: z.array(z.object({
        operation: z.enum(['add', 'update', 'merge', 'retire', 'link']),
        targetId: z.string().min(1),
        details: z.string().min(1)
      })).min(1).max(100),
      affectedIds: z.array(z.string()).max(100).default([])
    },
    annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: true, idempotentHint: false }
  }, async input => {
    const result = await createProposalFile(input);
    return toolResult(result, `Created governed proposal ${result.proposal.proposalId}.`);
  });

  return server;
}

app.get('/health', async (_req, res) => {
  const shared = await readRepositoryJson(SHARED_STATE_PATH).then(item => item.value).catch(() => null);
  res.json({
    status: 'ok',
    service: 'multiversal-aioc-mcp-bridge',
    version: '0.3.0',
    repository: REPOSITORY,
    ref: REF,
    publicBase: PUBLIC_BASE,
    writesEnabled: ALLOW_WRITES && Boolean(GITHUB_TOKEN),
    authenticationEnabled: Boolean(BRIDGE_TOKEN),
    sharedStateRevision: shared?.revision ?? null
  });
});

app.get('/api/shared-state', requireBridgeAuth, async (_req, res) => {
  try {
    const { value } = await readRepositoryJson(SHARED_STATE_PATH);
    res.json(value);
  } catch (error) {
    res.status(500).json({ error: String(error?.message || error) });
  }
});

app.put('/api/shared-state', requireBridgeAuth, async (req, res) => {
  try {
    const { expectedRevision, actor = 'browser-aioc', reason = 'browser shared-state synchronization', state: incoming } = req.body || {};
    if (!incoming || typeof incoming !== 'object') return res.status(400).json({ error: 'A state object is required.' });
    const result = await mutateSharedState({
      expectedRevision,
      actor,
      reason,
      mutate: state => {
        state.workingObjects = Array.isArray(incoming.workingObjects) ? incoming.workingObjects : state.workingObjects || [];
        state.structureDecisions = incoming.structureDecisions && typeof incoming.structureDecisions === 'object' ? incoming.structureDecisions : state.structureDecisions || {};
        state.packLists = Array.isArray(incoming.packLists) ? incoming.packLists : state.packLists || [];
        state.reviewQueue = Array.isArray(incoming.reviewQueue) ? incoming.reviewQueue : state.reviewQueue || [];
        state.evidence = incoming.evidence && typeof incoming.evidence === 'object' ? incoming.evidence : state.evidence || {};
      }
    });
    res.json({ revision: result.state.revision, commitSha: result.commitSha, state: result.state });
  } catch (error) {
    const message = String(error?.message || error);
    res.status(message.includes('revision conflict') ? 409 : 500).json({ error: message });
  }
});

app.post('/mcp', requireBridgeAuth, async (req, res) => {
  const server = buildServer();
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
  res.on('close', () => {
    transport.close().catch(() => {});
    server.close().catch(() => {});
  });
  try {
    await server.connect(transport);
    await transport.handleRequest(req, res, req.body);
  } catch (error) {
    if (!res.headersSent) res.status(500).json({ jsonrpc: '2.0', error: { code: -32603, message: String(error?.message || error) }, id: null });
  }
});

app.listen(PORT, () => console.log(`Multiversal AIOC MCP bridge v0.3.0 listening on :${PORT}`));
