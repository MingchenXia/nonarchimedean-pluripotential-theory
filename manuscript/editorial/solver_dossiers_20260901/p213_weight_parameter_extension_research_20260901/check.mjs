import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const own=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const manifest=JSON.parse(fs.readFileSync(path.join(own,'MANIFEST.json')));
for(const p of manifest.files){
 const b=fs.readFileSync(path.resolve(own,p.path));
 if(b.length!==p.bytes||hash(b)!==p.sha256)throw Error('Identity mismatch '+p.path);
}
for(const line of fs.readFileSync(path.join(own,'SHA256SUMS'),'utf8').trimEnd().split('\n')){
 const m=/^([a-f0-9]{64})  (.+)$/.exec(line);
 if(!m||hash(fs.readFileSync(path.resolve(own,m[2])))!==m[1])throw Error('Checksum mismatch');
}
const note=fs.readFileSync(path.join(own,'RESEARCH_NOTE.md'),'utf8');
if(/[\x00-\x08\x0b-\x1f\x7f]/.test(note))throw Error('Control byte');
console.log(JSON.stringify({identity:'PASS',manifestFiles:manifest.files.length,newMathVerified:false,cleanProductionGate:false,scope:'Frozen source and proof identities only'}));
