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
const RAW_BASE = `https://raw.githubusercontent.com/${REPOSITORY}/${REF}`;
const API_BASE = `https://api.github.com/repos/${REPOSITORY}`;
const SHARED_STATE_PATH = 'governance/shared-state/AIOC_SHARED_STATE.json';

const app = express();
app.use(express.json({ limit: '4mb' }));

function githubHeaders() {
  return {
    Accept: 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    ...(GITHUB_TOKEN ? { Authorization: `Bearer ${GITHUB_TOKEN}` } : {})
  };
}

async function fetchText(url) {
  const response = await fetch(url, { headers: githubHeaders() });
  if (!response.ok) throw new Error(`${url} returned ${response.status}`);
  return response.text();
}

async function fetchJson(url) {
  return JSON.parse(await fetchText(url));
}

async function contentDatabase() {
  const db = await fetchJson(`${RAW_BASE}/content-db/index.json`);
  if (!Array.isArray(db.records)) throw new Error('AIOC content database has no records array.');
  return db;
}

function recordId(record) {
  return record.stableId || record.refId || record.databaseId || record.catalogId || record.id;
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
  const response = await fetch(`${API_BASE}/contents/${path}?ref=${encodeURIComponent(REF)}`, { headers: githubHeaders() });
  if (!response.ok) throw new Error(`GitHub read ${path} returned ${response.status}: ${await response.text()}`);
  const payload = await response.json();
  const decoded = Buffer.from(payload.content.replace(/\n/g, ''), 'base64').toString('utf8');
  return { value: JSON.parse(decoded), sha: payload.sha };
}

async function writeRepositoryJson(path, value, sha, message) {
  requireWrites();
  const response = await fetch(`${API_BASE}/contents/${path}`, {
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
  const beforeRevision = state.revision;
  await mutate(state);
  state.revision = beforeRevision + 1;
  state.updatedAt = new Date().toISOString();
  state.updatedBy = actor;
  state.history = Array.isArray(state.history) ? state.history : [];
  state.history.push({ revision: state.revision, at: state.updatedAt, actor, reason });
  state.history = state.history.slice(-250);
  const result = await writeRepositoryJson(
    SHARED_STATE_PATH,
    state,
    sha,
    `bridge state: r${state.revision} ${reason}`
  );
  return { state, commitSha: result.commit?.sha || null };
}

async function createProposalFile({ title, summary, proposedChanges, affectedIds }) {
  requireWrites();
  const now = new Date();
  const stamp = now.toISOString().replace(/[:.]/g, '-');
  const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60) || 'proposal';
  const path = `governance/bridge-proposals/${stamp}-${slug}.json`;
  const body = {
    format: 'multiversal-aioc-bridge-proposal', version: '1.0.0', proposalId: crypto.randomUUID(),
    createdAt: now.toISOString(), createdBy: 'multiversal-aioc-mcp-bridge', status: 'PROPOSED',
    title, summary, affectedIds, proposedChanges
  };
  const result = await writeRepositoryJson(path, body, null, `bridge: propose ${title}`);
  return { proposal: body, path, commitSha: result.commit?.sha || null };
}

function buildServer() {
  const server = new McpServer({ name: 'multiversal-aioc', version: '0.2.0' });

  server.registerTool('aioc_status', {
    title: 'Get AIOC status',
    description: 'Use this when you need the AIOC build, health, content count, shared-state revision, and bridge write availability.',
    inputSchema: {},
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async () => {
    const [manifest, health, shared] = await Promise.all([
      fetchJson(`${RAW_BASE}/deployment-manifest.json`).catch(() => null),
      fetchJson(`${RAW_BASE}/operational/health.json`).catch(() => null),
      readRepositoryJson(SHARED_STATE_PATH).then(x => x.value).catch(() => null)
    ]);
    const data = {
      repository: REPOSITORY, ref: REF, manifest, health,
      sharedState: shared ? { revision: shared.revision, updatedAt: shared.updatedAt, workingObjectCount: shared.workingObjects?.length || 0, structureDecisionCount: Object.keys(shared.structureDecisions || {}).length } : null,
      bridge: { version: '0.2.0', writesEnabled: ALLOW_WRITES && Boolean(GITHUB_TOKEN) }
    };
    return toolResult(data, `AIOC bridge is connected to ${REPOSITORY}@${REF}.`);
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
      .slice(0, limit).map(compactRecord);
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
    description: 'Use this when you need the canonical AIOC operating state, active work, constraints, or handoff context.',
    inputSchema: {},
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async () => toolResult({ markdown: await fetchText(`${RAW_BASE}/governance/current-state/AIOC_CURRENT_STATE.md`) }, 'Loaded the canonical AIOC current-state record.'));

  server.registerTool('get_aioc_shared_state', {
    title: 'Get shared AIOC working state',
    description: 'Use this when you need shared drafts, structure decisions, packs, evidence, review queue, or the current revision used by the browser, ChatGPT, and Codex.',
    inputSchema: { includeHistory: z.boolean().default(false) },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async ({ includeHistory }) => {
    const { value } = await readRepositoryJson(SHARED_STATE_PATH);
    const state = includeHistory ? value : { ...value, history: undefined };
    return toolResult({ state }, `Loaded shared AIOC state revision ${value.revision}.`);
  });

  server.registerTool('list_aioc_working_objects', {
    title: 'List shared AIOC working objects',
    description: 'Use this when you need drafts and game-object work currently shared across AIOC, ChatGPT, and Codex.',
    inputSchema: { query: z.string().optional(), stage: z.string().optional(), limit: z.number().int().min(1).max(200).default(50) },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async ({ query, stage, limit }) => {
    const { value } = await readRepositoryJson(SHARED_STATE_PATH);
    const q = query?.toLowerCase();
    const objects = (value.workingObjects || [])
      .filter(x => !stage || x.developmentStage === stage)
      .filter(x => !q || JSON.stringify([recordId(x), x.name, x.objectType, x.description, x.tags]).toLowerCase().includes(q))
      .slice(0, limit).map(compactRecord);
    return toolResult({ revision: value.revision, count: objects.length, objects }, `Found ${objects.length} shared working object${objects.length === 1 ? '' : 's'}.`);
  });

  server.registerTool('get_aioc_working_object', {
    title: 'Get shared AIOC working object',
    description: 'Use this when you need the complete editable working object for one stable ID.',
    inputSchema: { id: z.string().min(1) },
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async ({ id }) => {
    const { value } = await readRepositoryJson(SHARED_STATE_PATH);
    const object = (value.workingObjects || []).find(x => recordId(x) === id);
    if (!object) throw new Error(`No shared working object found for ${id}.`);
    return toolResult({ revision: value.revision, object }, `Loaded shared working object ${object.name || id}.`);
  });

  server.registerTool('upsert_aioc_working_object', {
    title: 'Create or update shared AIOC working object',
    description: 'Use this when the user approves saving a draft or revision into shared AIOC working state. This does not alter canonical content.',
    inputSchema: {
      expectedRevision: z.number().int().min(0), actor: z.string().min(1).max(120),
      object: z.object({ id: z.string().min(1), name: z.string().min(1), objectType: z.string().min(1), developmentStage: z.string().default('Draft') }).passthrough()
    },
    annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async ({ expectedRevision, actor, object }) => {
    const result = await mutateSharedState({ expectedRevision, actor, reason: `upsert working object ${object.id}`, mutate: state => {
      state.workingObjects = Array.isArray(state.workingObjects) ? state.workingObjects : [];
      const index = state.workingObjects.findIndex(x => recordId(x) === object.id);
      const stamped = { ...object, stableId: object.stableId || object.id, updatedAt: new Date().toISOString(), updatedBy: actor };
      if (index >= 0) state.workingObjects[index] = { ...state.workingObjects[index], ...stamped };
      else state.workingObjects.push(stamped);
    }});
    return toolResult({ revision: result.state.revision, object: result.state.workingObjects.find(x => recordId(x) === object.id), commitSha: result.commitSha }, `Saved ${object.name} to shared AIOC state revision ${result.state.revision}.`);
  });

  server.registerTool('record_aioc_structure_decision', {
    title: 'Record AIOC content structure decision',
    description: 'Use this when the user approves classifying a source record as standalone, reusable generic, parent component, granted variant, duplicate, or obsolete.',
    inputSchema: {
      expectedRevision: z.number().int().min(0), actor: z.string().min(1).max(120), sourceId: z.string().min(1),
      classification: z.enum(['standalone', 'reusable-generic', 'parent-component', 'granted-variant', 'duplicate', 'obsolete']),
      targetId: z.string().optional(), notes: z.string().max(4000).default('')
    },
    annotations: { readOnlyHint: false, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async input => {
    const result = await mutateSharedState({ expectedRevision: input.expectedRevision, actor: input.actor, reason: `classify ${input.sourceId} as ${input.classification}`, mutate: state => {
      state.structureDecisions = state.structureDecisions || {};
      state.structureDecisions[input.sourceId] = { sourceId: input.sourceId, classification: input.classification, targetId: input.targetId || null, notes: input.notes, decidedAt: new Date().toISOString(), decidedBy: input.actor };
    }});
    return toolResult({ revision: result.state.revision, decision: result.state.structureDecisions[input.sourceId], commitSha: result.commitSha }, `Recorded structure decision for ${input.sourceId}.`);
  });

  server.registerTool('create_aioc_change_proposal', {
    title: 'Create AIOC change proposal',
    description: 'Use this when the user has approved recording a governed, reviewable proposal in the AIOC repository. This does not directly alter canonical content.',
    inputSchema: {
      title: z.string().min(3).max(160), summary: z.string().min(10).max(4000),
      proposedChanges: z.array(z.object({ operation: z.enum(['add', 'update', 'merge', 'retire', 'link']), targetId: z.string().min(1), details: z.string().min(1) })).min(1).max(100),
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
  const shared = await readRepositoryJson(SHARED_STATE_PATH).then(x => x.value).catch(() => null);
  res.json({ status: 'ok', service: 'multiversal-aioc-mcp-bridge', version: '0.2.0', repository: REPOSITORY, ref: REF, writesEnabled: ALLOW_WRITES && Boolean(GITHUB_TOKEN), sharedStateRevision: shared?.revision ?? null });
});

app.post('/mcp', async (req, res) => {
  const server = buildServer();
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
  res.on('close', () => { transport.close().catch(() => {}); server.close().catch(() => {}); });
  try { await server.connect(transport); await transport.handleRequest(req, res, req.body); }
  catch (error) { if (!res.headersSent) res.status(500).json({ jsonrpc: '2.0', error: { code: -32603, message: String(error?.message || error) }, id: null }); }
});

app.listen(PORT, () => console.log(`Multiversal AIOC MCP bridge listening on :${PORT}`));
