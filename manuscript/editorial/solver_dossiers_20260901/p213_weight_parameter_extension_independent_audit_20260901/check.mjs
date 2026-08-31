import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const own=path.dirname(fileURLToPath(import.meta.url));
const read=f=>fs.readFileSync(f,'utf8');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const ok=(v,s)=>{if(!v)throw Error(s);};
const pins=JSON.parse(read(path.join(own,'INPUT_PINS.json'))).items;
for(const p of pins){const b=fs.readFileSync(p.path);ok(b.length===p.bytes&&hash(b)===p.sha256,'input mismatch '+p.role);}
const candidate=path.dirname(pins.find(p=>p.role==='candidate_note').path);
let candidateManifest=0,candidateSums=0;
for(const p of JSON.parse(read(path.join(candidate,'MANIFEST.json'))).files){const b=fs.readFileSync(path.resolve(candidate,p.path));ok(b.length===p.bytes&&hash(b)===p.sha256,'candidate manifest mismatch');candidateManifest++;}
for(const line of read(path.join(candidate,'SHA256SUMS')).trimEnd().split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);ok(m&&hash(fs.readFileSync(path.resolve(candidate,m[2])))===m[1],'candidate sums');candidateSums++;}
let ownManifest=0,ownSums=0;
if(fs.existsSync(path.join(own,'MANIFEST.json'))){
for(const p of JSON.parse(read(path.join(own,'MANIFEST.json'))).files){const b=fs.readFileSync(path.join(own,p.path));ok(b.length===p.bytes&&hash(b)===p.sha256,'audit manifest mismatch');ownManifest++;}
for(const line of read(path.join(own,'SHA256SUMS')).trimEnd().split('\n')){const m=/^([a-f0-9]{64})  (.+)$/.exec(line);ok(m&&hash(fs.readFileSync(path.join(own,m[2])))===m[1],'audit sums');ownSums++;}
}
const note=read(path.join(candidate,'RESEARCH_NOTE.md'));
ok(note.trimEnd().split('\n').length===166,'candidate line count');
for(const f of ['AUDIT.md','SOURCE_MATRIX.md','INPUT_PINS.json','check.mjs'])ok(!/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(read(path.join(own,f))),'control byte '+f);
console.log(JSON.stringify({input_pins:pins.length,candidate_manifest_entries:candidateManifest,candidate_checksums:candidateSums,audit_manifest_entries:ownManifest,audit_checksums:ownSums,byte_identity:'PASS',mathematical_verdict:'See AUDIT.md: independent PASS for new parameter extension conditional on exact energy input',clean_production_gate:false},null,2));
