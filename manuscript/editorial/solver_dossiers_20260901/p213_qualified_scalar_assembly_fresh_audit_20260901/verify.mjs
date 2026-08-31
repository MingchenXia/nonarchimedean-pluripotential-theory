// Read-only provenance and graph checks. This script is not a mathematical proof.
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
  const sha256 = crypto.createHash('sha256').update(bytes).digest('hex');
  if (sha256 !== entry.sha256 || (entry.bytes !== undefined && bytes.length !== entry.bytes)) {
    throw new Error(`Identity mismatch: ${target}`);
  }
  return target;
}
for (const item of pins.inputs) check(auditDirectory, item);
const importedPins = JSON.parse(fs.readFileSync(path.join(targetDirectory, 'INPUT_PINS.json'), 'utf8')).files;
for (const item of importedPins) check(targetDirectory, item);

let manifestEntries = 0;
const manifestPaths = [path.join(targetDirectory, 'MANIFEST.json')];
for (const item of importedPins) {
  if (path.basename(item.file) === 'MANIFEST.json') manifestPaths.push(path.resolve(targetDirectory, item.file));
}
for (const manifestPath of manifestPaths) {
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const entries = manifest.entries ?? manifest.files;
  if (!Array.isArray(entries)) throw new Error(`Unsupported manifest: ${manifestPath}`);
  for (const item of entries) {
    check(path.dirname(manifestPath), item);
    manifestEntries++;
  }
}
let sourceChecksumLines = 0;
for (const line of fs.readFileSync(path.join(targetDirectory, 'SHA256SUMS'), 'utf8').trim().split('\n')) {
  const match = line.match(/^([a-f0-9]{64})\s+[*]?(.+)$/);
  if (!match) throw new Error('Malformed source checksum line');
  check(targetDirectory, {sha256: match[1], file: match[2]});
  sourceChecksumLines++;
}

const extension = JSON.parse(fs.readFileSync(path.join(auditDirectory, 'DEPENDENCY_EXTENSIONS.json'), 'utf8'));
const base = JSON.parse(fs.readFileSync(path.resolve(auditDirectory, extension.baseGraph), 'utf8'));
const nodes = [...base.nodes, ...extension.nodes];
const byId = new Map(nodes.map(node => [node.id, node]));
if (byId.size !== nodes.length) throw new Error('Duplicate graph node');
const active = new Set();
const done = new Set();
const order = [];
function visit(id) {
  if (done.has(id)) return;
  if (active.has(id)) throw new Error(`Dependency cycle at ${id}`);
  const node = byId.get(id);
  if (!node) throw new Error(`Missing prerequisite ${id}`);
  active.add(id);
  for (const prerequisite of node.requires) visit(prerequisite);
  active.delete(id);
  done.add(id);
  order.push(id);
}
for (const node of nodes) visit(node.id);
process.stdout.write(JSON.stringify({
  directlyPinnedFiles: pins.inputs.length,
  sourceInputPins: importedPins.length,
  checkedManifests: manifestPaths.length,
  manifestEntries,
  sourceChecksumLines,
  allExact: true,
  dependencyNodes: nodes.length,
  acyclic: true,
  topologicalOrder: order,
  writesPerformed: 0,
  meaning: 'Identity and graph syntax only. The independent mathematical review is AUDIT.md.'
}, null, 2) + '\n');
