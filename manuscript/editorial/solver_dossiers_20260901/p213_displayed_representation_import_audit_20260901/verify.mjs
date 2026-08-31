// Read-only identity and directed-graph checks; not mathematical or production certification.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const auditDirectory = path.dirname(fileURLToPath(import.meta.url));
const pins = JSON.parse(fs.readFileSync(path.join(auditDirectory, 'REVIEWED_INPUTS.json'), 'utf8'));
function verify(base, entry) {
  const target = path.resolve(base, entry.file ?? entry.path);
  const bytes = fs.readFileSync(target);
  const actual = crypto.createHash('sha256').update(bytes).digest('hex');
  if (actual !== entry.sha256 || (entry.bytes !== undefined && bytes.length !== entry.bytes)) {
    throw new Error(`Identity mismatch: ${target}`);
  }
  return target;
}
for (const entry of pins.inputs) verify(auditDirectory, entry);
let manifestEntries = 0;
for (const entry of pins.manifests) {
  const manifestPath = verify(auditDirectory, entry);
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const entries = manifest.entries ?? manifest.files;
  if (!Array.isArray(entries)) throw new Error(`Unsupported manifest schema: ${manifestPath}`);
  for (const item of entries) {
    verify(path.dirname(manifestPath), item);
    manifestEntries++;
  }
}

const graph = JSON.parse(fs.readFileSync(path.join(auditDirectory, 'DEPENDENCY_GRAPH.json'), 'utf8'));
const byId = new Map(graph.nodes.map(node => [node.id, node]));
if (byId.size !== graph.nodes.length) throw new Error('Duplicate dependency node');
const active = new Set();
const finished = new Set();
const topologicalOrder = [];
function visit(id) {
  if (finished.has(id)) return;
  if (active.has(id)) throw new Error(`Dependency cycle at ${id}`);
  const node = byId.get(id);
  if (!node) throw new Error(`Missing dependency node ${id}`);
  active.add(id);
  for (const prerequisite of node.requires) visit(prerequisite);
  active.delete(id);
  finished.add(id);
  topologicalOrder.push(id);
}
for (const node of graph.nodes) visit(node.id);
process.stdout.write(JSON.stringify({
  pinnedFiles: pins.inputs.length,
  pinnedManifests: pins.manifests.length,
  manifestEntries,
  allExact: true,
  dependencyNodes: graph.nodes.length,
  acyclic: true,
  topologicalOrder,
  writesPerformed: 0,
  meaning: 'Identity and graph syntax only; substantive review is AUDIT.md'
}, null, 2) + '\n');
