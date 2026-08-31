// Read-only exact identities and dependency syntax. Not a mathematical certificate.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
const auditDirectory = path.dirname(fileURLToPath(import.meta.url));
const pins = JSON.parse(fs.readFileSync(path.join(auditDirectory, 'REVIEWED_INPUTS.json'), 'utf8'));
const targetDirectory = path.resolve(auditDirectory, pins.targetDirectory);
function check(base, entry) {
  const target = path.resolve(base, entry.file ?? entry.path);
  const bytes = fs.readFileSync(target);
  const digest = crypto.createHash('sha256').update(bytes).digest('hex');
  if (digest !== entry.sha256 || (entry.bytes !== undefined && bytes.length !== entry.bytes)) throw new Error(`Identity mismatch: ${target}`);
  return target;
}
for (const entry of pins.inputs) check(auditDirectory, entry);
const sourcePins = JSON.parse(fs.readFileSync(path.join(targetDirectory, 'INPUT_PINS.json'), 'utf8')).files;
for (const entry of sourcePins) check(targetDirectory, entry);
const visitedManifests = new Set();
let manifestEntries = 0;
function visitManifest(manifestPath) {
  if (visitedManifests.has(manifestPath)) return;
  visitedManifests.add(manifestPath);
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const entries = manifest.entries ?? manifest.files;
  if (!Array.isArray(entries)) throw new Error(`Unknown manifest schema: ${manifestPath}`);
  for (const entry of entries) {
    const target = check(path.dirname(manifestPath), entry);
    manifestEntries++;
    if (path.basename(target) === 'MANIFEST.json') visitManifest(target);
  }
}
visitManifest(path.join(targetDirectory, 'MANIFEST.json'));
function checkSums(base, optional=false) {
  const sumPath = path.join(base, 'SHA256SUMS');
  if (optional && !fs.existsSync(sumPath)) return 0;
  const lines = fs.readFileSync(sumPath, 'utf8').trim().split('\n');
  for (const line of lines) {
    const match = line.match(/^([a-f0-9]{64})\s+[*]?(.+)$/);
    if (!match) throw new Error(`Malformed checksum: ${sumPath}`);
    check(base, {sha256: match[1], file: match[2]});
  }
  return lines.length;
}
const sourceChecksums = checkSums(targetDirectory);
const ownChecksums = checkSums(auditDirectory, true);
const graphsRead = new Set();
const nodes = [];
function readGraph(graphPath) {
  if (graphsRead.has(graphPath)) throw new Error('Repeated graph import');
  graphsRead.add(graphPath);
  const graph = JSON.parse(fs.readFileSync(graphPath, 'utf8'));
  if (graph.baseGraph) readGraph(path.resolve(path.dirname(graphPath), graph.baseGraph));
  nodes.push(...graph.nodes);
}
readGraph(path.join(auditDirectory, 'DEPENDENCY_EXTENSIONS.json'));
const byId = new Map(nodes.map(node => [node.id, node]));
if (byId.size !== nodes.length) throw new Error('Duplicate proof node');
const active = new Set();
const done = new Set();
const order = [];
function visitNode(id) {
  if (done.has(id)) return;
  if (active.has(id)) throw new Error(`Proof dependency cycle: ${id}`);
  const node = byId.get(id);
  if (!node) throw new Error(`Missing prerequisite: ${id}`);
  active.add(id);
  for (const prerequisite of node.requires) visitNode(prerequisite);
  active.delete(id);
  done.add(id);
  order.push(id);
}
for (const node of nodes) visitNode(node.id);
process.stdout.write(JSON.stringify({
  directPins: pins.inputs.length,
  sourceInputPins: sourcePins.length,
  checkedManifests: visitedManifests.size,
  checkedManifestEntries: manifestEntries,
  sourceChecksums,
  ownChecksums,
  proofNodes: nodes.length,
  acyclic: true,
  exactIdentities: true,
  topologicalOrder: order,
  writesPerformed: 0,
  meaning: 'Identity and DAG syntax only; exact-scope mathematical review is AUDIT.md.'
}, null, 2) + '\n');
