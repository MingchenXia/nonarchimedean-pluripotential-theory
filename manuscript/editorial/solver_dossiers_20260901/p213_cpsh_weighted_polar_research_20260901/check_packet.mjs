import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

// Read-only identity checker. No child processes, network, or writes.
const root=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const failures=[];
function inspect(name,expected,bytes){
  const p=path.isAbsolute(name)?name:path.join(root,name);
  try{
    const b=fs.readFileSync(p);
    if(hash(b)!==expected) failures.push('SHA256 mismatch: '+p);
    if(bytes!==undefined && b.length!==bytes) failures.push('Byte count mismatch: '+p);
    return b;
  }catch(e){failures.push('Read failed: '+p+': '+e.message); return null;}
}
const pins=JSON.parse(fs.readFileSync(path.join(root,'INPUT_PINS.json'),'utf8'));
for(const e of pins.inputs) inspect(e.path,e.sha256,e.bytes);
if(pins.inputs.length!==5) failures.push('Expected five external input pins');
const mf=JSON.parse(fs.readFileSync(path.join(root,'MANIFEST.json'),'utf8'));
for(const e of mf.entries) inspect(e.path,e.sha256,e.bytes);
if(mf.entries.length!==10) failures.push('Expected ten manifest entries');
const rows=fs.readFileSync(path.join(root,'SHA256SUMS'),'utf8').trimEnd().split('\n');
const seen=new Set();
for(const row of rows){
  const m=/^([a-f0-9]{64})  (.+)$/.exec(row);
  if(!m){failures.push('Malformed checksum row: '+row);continue;}
  if(seen.has(m[2])) failures.push('Duplicate checksum path: '+m[2]);
  seen.add(m[2]); inspect(m[2],m[1]);
}
if(rows.length!==11) failures.push('Expected eleven checksum rows');
for(const e of mf.entries) if(!seen.has(e.path)) failures.push('Manifest entry absent from checksum list: '+e.path);
if(!seen.has('MANIFEST.json')) failures.push('Manifest checksum missing');
const textFiles=['RESEARCH_NOTE.md','SOURCE_LEDGER.md','VALIDATION.md','INPUT_PINS.json','check_packet.mjs','MANIFEST.json','SHA256SUMS'];
let badControls=0;
for(const name of textFiles){
  const txt=fs.readFileSync(path.join(root,name),'utf8');
  const bad=[...txt].filter(c=>{const a=c.codePointAt(0);return(a<32&&a!==9&&a!==10&&a!==13)||a===127;});
  badControls+=bad.length;
  if(bad.length) failures.push('Forbidden controls in '+name+': '+bad.length);
}
console.log(JSON.stringify({kind:'read-only byte identity check, NOT mathematical or production verification',externalPins:pins.inputs.length,manifestEntries:mf.entries.length,checksumRows:rows.length,authoredTextFiles:textFiles.length,forbiddenControls:badControls,failures},null,2));
process.exitCode=failures.length?1:0;

