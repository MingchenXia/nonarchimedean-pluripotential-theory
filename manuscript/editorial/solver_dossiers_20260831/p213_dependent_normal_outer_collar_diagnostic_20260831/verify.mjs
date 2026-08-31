import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const m=JSON.parse(fs.readFileSync(path.join(here,'MANIFEST.json'),'utf8'));
for(const e of m.entries){
  const b=fs.readFileSync(e.path);
  if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Manifest mismatch: '+e.path);
  if(e.role==='new diagnostic file'&&[...b].some(c=>(c<32&&c!==9&&c!==10)||c===127))
    throw Error('Forbidden control: '+e.path);
}
const sums=fs.readFileSync(path.join(here,'SHA256SUMS'),'utf8').trim().split('\n');
for(const line of sums){
  const e=line.match(/^([a-f0-9]{64})  (.+)$/);
  if(!e||sha(fs.readFileSync(e[2]))!==e[1])throw Error('Checksum mismatch: '+line);
}
console.log(JSON.stringify({readOnly:true,manifestEntries:m.entries.length,
  checksumEntries:sums.length,forbiddenControls:0,mismatches:0},null,2));
