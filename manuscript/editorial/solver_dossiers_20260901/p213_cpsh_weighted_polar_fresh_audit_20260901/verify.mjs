// Read-only exact identity, graph syntax, and bounded arithmetic checks; not a proof certificate.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const auditDirectory=path.dirname(fileURLToPath(import.meta.url));
const pins=JSON.parse(fs.readFileSync(path.join(auditDirectory,'REVIEWED_INPUTS.json'),'utf8'));
const targetDirectory=path.resolve(auditDirectory,pins.targetDirectory);
function check(base,entry){
  const target=path.resolve(base,entry.file??entry.path), data=fs.readFileSync(target);
  if(crypto.createHash('sha256').update(data).digest('hex')!==entry.sha256 ||
     (entry.bytes!==undefined&&entry.bytes!==data.length)) throw new Error(`Identity mismatch: ${target}`);
  return target;
}
for(const entry of pins.inputs) check(auditDirectory,entry);
const sourcePins=JSON.parse(fs.readFileSync(path.join(targetDirectory,'INPUT_PINS.json'),'utf8')).inputs;
for(const entry of sourcePins) check(targetDirectory,entry);
const visitedManifests=new Set(); let manifestEntries=0;
function visitManifest(manifestPath){
  if(visitedManifests.has(manifestPath))return;
  visitedManifests.add(manifestPath);
  const data=JSON.parse(fs.readFileSync(manifestPath,'utf8')), entries=data.entries??data.files;
  if(!Array.isArray(entries))throw new Error(`Unknown manifest: ${manifestPath}`);
  for(const entry of entries){
    const target=check(path.dirname(manifestPath),entry); manifestEntries++;
    if(path.basename(target)==='MANIFEST.json')visitManifest(target);
  }
}
visitManifest(path.join(targetDirectory,'MANIFEST.json'));
function checkSums(base,optional=false){
  const file=path.join(base,'SHA256SUMS');
  if(optional&&!fs.existsSync(file))return 0;
  const lines=fs.readFileSync(file,'utf8').trim().split('\n');
  for(const line of lines){
    const match=line.match(/^([a-f0-9]{64})\s+[*]?(.+)$/);
    if(!match)throw new Error(`Malformed checksum: ${file}`);
    check(base,{sha256:match[1],file:match[2]});
  }
  return lines.length;
}
const sourceChecksums=checkSums(targetDirectory), ownChecksums=checkSums(auditDirectory,true);
const graph=JSON.parse(fs.readFileSync(path.join(auditDirectory,'DEPENDENCY_GRAPH.json'),'utf8'));
if(graph.baseGraph)throw new Error('This audit requires a standalone graph');
const nodes=new Map(graph.nodes.map(node=>[node.id,node]));
if(nodes.size!==graph.nodes.length)throw new Error('Duplicate node');
const active=new Set(),done=new Set(),order=[];
function visit(id){
  if(done.has(id))return;
  if(active.has(id))throw new Error(`Cycle at ${id}`);
  const node=nodes.get(id);if(!node)throw new Error(`Missing node ${id}`);
  if(/scalar_classification|R_displayed|hierarchy_collapse/.test(id))throw new Error(`Forbidden proof prerequisite ${id}`);
  active.add(id);for(const parent of node.requires)visit(parent);
  active.delete(id);done.add(id);order.push(id);
}
for(const node of graph.nodes)visit(node.id);
let endpointCases=0;
for(let n=1;n<=32;n++)for(let k=1;k<=n;k++)for(let a=4;a<=12;a++){
  const l=BigInt(k+a),b=k===n?1n:2n;
  const theta=b*l,eta=b*l*((b-1n)*l+1n),den=l-1n,num=2n*l*(l+1n);
  if(theta*den>num||eta>num)throw new Error('Bracket coefficient bound fails');
  if((k===n&&(theta!==l||eta!==l))||(k<n&&(theta!==2n*l||eta!==2n*l*(l+1n))))throw new Error('Endpoint coefficient mismatch');
  endpointCases++;
}
process.stdout.write(JSON.stringify({directPins:pins.inputs.length,sourceInputPins:sourcePins.length,
  checkedManifests:visitedManifests.size,checkedManifestEntries:manifestEntries,sourceChecksums,ownChecksums,
  standaloneProofNodes:nodes.size,acyclic:true,classificationOrRImported:false,endpointArithmeticCases:endpointCases,
  exactIdentities:true,topologicalOrder:order,writesPerformed:0,
  meaning:'Checksums, dependency syntax and bounded coefficient arithmetic only; mathematical review is AUDIT.md.'},null,2)+'\n');
