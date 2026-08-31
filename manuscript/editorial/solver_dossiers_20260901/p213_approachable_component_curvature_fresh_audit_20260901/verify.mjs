// Read-only identity and dependency checks, not a mathematical certificate.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
const auditDirectory = path.dirname(fileURLToPath(import.meta.url));
const pins = JSON.parse(fs.readFileSync(path.join(auditDirectory, 'REVIEWED_INPUTS.json'), 'utf8'));
const targetDirectory = path.resolve(auditDirectory, pins.targetDirectory);
function check(base, entry) {
  const target = path.resolve(base, entry.file ?? entry.path);
  const data = fs.readFileSync(target);
  if (crypto.createHash('sha256').update(data).digest('hex') !== entry.sha256 ||
      (entry.bytes !== undefined && data.length !== entry.bytes)) throw new Error(`Identity mismatch: ${target}`);
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
  const data = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const entries = data.entries ?? data.files;
  if (!Array.isArray(entries)) throw new Error(`Unknown manifest format: ${manifestPath}`);
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
    check(base, {sha256:match[1], file:match[2]});
  }
  return lines.length;
}
const sourceChecksums = checkSums(targetDirectory);
const ownChecksums = checkSums(auditDirectory, true);
const graphsRead = new Set(), nodes = [];
function readGraph(graphPath) {
  if (graphsRead.has(graphPath)) throw new Error('Repeated graph import');
  graphsRead.add(graphPath);
  const graph = JSON.parse(fs.readFileSync(graphPath, 'utf8'));
  if (graph.baseGraph) readGraph(path.resolve(path.dirname(graphPath), graph.baseGraph));
  nodes.push(...graph.nodes);
}
readGraph(path.join(auditDirectory, 'DEPENDENCY_EXTENSIONS.json'));
const byId = new Map(nodes.map(node => [node.id,node]));
if (byId.size !== nodes.length) throw new Error('Duplicate proof node');
const active = new Set(), done = new Set(), order = [];
function visitNode(id) {
  if (done.has(id)) return;
  if (active.has(id)) throw new Error(`Dependency cycle: ${id}`);
  const node = byId.get(id);
  if (!node) throw new Error(`Missing prerequisite: ${id}`);
  active.add(id);
  for (const prerequisite of node.requires) visitNode(prerequisite);
  active.delete(id);
  done.add(id);
  order.push(id);
}
for (const node of nodes) visitNode(node.id);
function ancestors(id, result=new Set()) {
  for (const prerequisite of byId.get(id).requires) {
    if (!result.has(prerequisite)) { result.add(prerequisite); ancestors(prerequisite,result); }
  }
  return result;
}
const classification = 'component_all_pure_scalar_classification';
const independentClauses = ['approachable_component_equivalence_I','approachable_common_curvature_criterion','approachable_one_A_or_common_A_potential'];
for (const clause of independentClauses) if (ancestors(clause).has(classification)) throw new Error(`Illicit classification dependency: ${clause}`);
if (!ancestors('approachable_every_open_scalar_consequence_II').has(classification)) throw new Error('Missing classification dependency in II');
process.stdout.write(JSON.stringify({directPins:pins.inputs.length,sourceInputPins:sourcePins.length,
  checkedManifests:visitedManifests.size,checkedManifestEntries:manifestEntries,sourceChecksums,ownChecksums,
  proofNodes:nodes.length,acyclic:true,exactIdentities:true,
  IAndCriterionIndependentOfClassification:true,IIUsesRestrictedClassification:true,
  topologicalOrder:order,writesPerformed:0,
  meaning:'Byte identities and graph syntax only; actual mathematical review is AUDIT.md.'},null,2)+'\n');
