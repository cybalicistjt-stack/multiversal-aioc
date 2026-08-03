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

const app = express();
app.use(express.json({ limit: '2mb' }));

async function fetchText(url) {
  const response = await fetch(url, {
    headers: {
      Accept: 'application/vnd.github+json',
      ...(GITHUB_TOKEN ? { Authorization: `Bearer ${GITHUB_TOKEN}` } : {})
    }
  });
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
  return record.stableId || record.refId || record.databaseId || record.catalogId;
}

function compactRecord(record) {
  return {
    id: recordId(record),
    name: record.name,
    objectType: record.objectType || record.contentType,
    stage: record.developmentStage || record.stage,
    source: record.source || record.provenance?.authority,
    dependencies: record.dependencies || [],
    hasBody: Boolean(record.gameObject || record.object || record.content || record.spec)
  };
}

function toolResult(data, summary) {
  return {
    structuredContent: data,
    content: [{ type: 'text', text: summary }]
  };
}

async function createProposalFile({ title, summary, proposedChanges, affectedIds }) {
  if (!ALLOW_WRITES) throw new Error('AIOC write actions are disabled on this bridge.');
  if (!GITHUB_TOKEN) throw new Error('GITHUB_TOKEN is required for proposal writes.');

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

  const response = await fetch(`${API_BASE}/contents/${path}`, {
    method: 'PUT',
    headers: {
      Authorization: `Bearer ${GITHUB_TOKEN}`,
      Accept: 'application/vnd.github+json',
      'Content-Type': 'application/json',
      'X-GitHub-Api-Version': '2022-11-28'
    },
    body: JSON.stringify({
      message: `bridge: propose ${title}`,
      content: Buffer.from(JSON.stringify(body, null, 2)).toString('base64'),
      branch: REF
    })
  });
  if (!response.ok) throw new Error(`GitHub proposal write returned ${response.status}: ${await response.text()}`);
  const result = await response.json();
  return { proposal: body, path, commitSha: result.commit?.sha || null };
}

function buildServer() {
  const server = new McpServer({ name: 'multiversal-aioc', version: '0.1.0' });

  server.registerTool('aioc_status', {
    title: 'Get AIOC status',
    description: 'Use this when you need the deployed AIOC build, health, content count, and bridge write availability.',
    inputSchema: {},
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async () => {
    const [manifest, health] = await Promise.all([
      fetchJson(`${RAW_BASE}/deployment-manifest.json`).catch(() => null),
      fetchJson(`${RAW_BASE}/operational/health.json`).catch(() => null)
    ]);
    const data = { repository: REPOSITORY, ref: REF, manifest, health, bridge: { writesEnabled: ALLOW_WRITES && Boolean(GITHUB_TOKEN) } };
    return toolResult(data, `AIOC bridge is connected to ${REPOSITORY}@${REF}.`);
  });

  server.registerTool('search_aioc_content', {
    title: 'Search AIOC content',
    description: 'Use this when you need to find canonical Multiversal content records by name, ID, type, source, or text.',
    inputSchema: {
      query: z.string().min(1),
      objectType: z.string().optional(),
      limit: z.number().int().min(1).max(100).default(25)
    },
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
    description: 'Use this when you need the canonical AIOC operating state, active work, constraints, or handoff context.',
    inputSchema: {},
    annotations: { readOnlyHint: true, destructiveHint: false, openWorldHint: false, idempotentHint: true }
  }, async () => {
    const text = await fetchText(`${RAW_BASE}/governance/current-state/AIOC_CURRENT_STATE.md`);
    return toolResult({ markdown: text }, 'Loaded the canonical AIOC current-state record.');
  });

  server.registerTool('create_aioc_change_proposal', {
    title: 'Create AIOC change proposal',
    description: 'Use this when the user has approved recording a governed, reviewable proposal in the AIOC repository. This does not directly alter canonical content.',
    inputSchema: {
      title: z.string().min(3).max(160),
      summary: z.string().min(10).max(4000),
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

app.get('/health', (_req, res) => {
  res.json({ status: 'ok', service: 'multiversal-aioc-mcp-bridge', version: '0.1.0', repository: REPOSITORY, ref: REF, writesEnabled: ALLOW_WRITES && Boolean(GITHUB_TOKEN) });
});

app.post('/mcp', async (req, res) => {
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

app.listen(PORT, () => {
  console.log(`Multiversal AIOC MCP bridge listening on :${PORT}`);
});
