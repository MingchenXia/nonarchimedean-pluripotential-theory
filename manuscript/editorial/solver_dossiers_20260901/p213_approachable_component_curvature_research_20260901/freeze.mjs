// Mechanical identities only. Read-only unless explicitly called with --freeze.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const own=path.dirname(fileURLToPath(import.meta.url));
const read=f=>fs.readFileSync(path.resolve(own,f));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins=[];
function pin(file,expected,role){const b=read(file),h=sha(b);if(expected&&h!==expected)throw Error('Input drift '+file);pins.push({file,bytes:b.length,sha256:h,role});}
const prior='../p213_component_scalar_classification_research_20260901/';
pin(prior+'RESEARCH_NOTE.md','73f5d4323d81abc8b711aa4dd0d37def0f1ebd789ae19ae9e167c3b2502d4b84','Scalar classification only for consequence II; not used by componentwise equivalence I');
pin(prior+'SOURCE_LEDGER.md','ee8c6bf9cc37ebf3d909ee78d45175398b4fdf75fbcebd70c1989e2f32b4d8c9','Previously checked component and cycle source interfaces');
pin(prior+'MANIFEST.json','a264c37c448550648df933e0ca27802cf68db52894e63e92e0dee2c895d18136','Exact prior dependencies');
pin('/private/tmp/CLD25.txt','021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e','Primary text: approximation, polar nullity and pushforward');
const previous=JSON.parse(read(prior+'MANIFEST.json')).entries;
for(const e of previous){const b=fs.readFileSync(path.resolve(own,prior,e.file));if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Prior manifest drift');}
const authored=['RESEARCH_NOTE.md','SOURCE_LEDGER.md','freeze.mjs'];
for(const f of authored){const b=read(f);if(!b.length||b.at(-1)!==10||[...b].some(x=>(x<32&&x!==9&&x!==10)||x===127))throw Error('Text integrity '+f);}
const generated=['INPUT_PINS.json','VALIDATION.json','MANIFEST.json','SHA256SUMS'];
if(process.argv.includes('--freeze')){
 for(const f of generated)if(fs.existsSync(path.join(own,f)))throw Error('Refuse refreeze');
 const write=(f,b)=>fs.writeFileSync(path.join(own,f),b,{flag:'wx'});
 write('INPUT_PINS.json',JSON.stringify({date:'2026-09-01',files:pins},null,2)+'\n');
 write('VALIDATION.json',JSON.stringify({date:'2026-09-01',inputPins:pins.length,priorManifestEntries:previous.length,controlByteErrors:0,mathematicalVerdict:'Not supplied by script',independentStatus:'Awaiting exact-final audit',productionStatus:'Not verified',liveChanges:false,atomRetirements:0},null,2)+'\n');
 const entries=[...authored,'INPUT_PINS.json','VALIDATION.json'].map(file=>{const b=read(file);return{file,bytes:b.length,sha256:sha(b)};}).concat(pins);
 const mf=JSON.stringify({date:'2026-09-01',status:'Frozen approachable-pair componentwise curvature candidate; no production or live promotion',entries},null,2)+'\n';
 write('MANIFEST.json',mf);
 write('SHA256SUMS',entries.map(e=>e.sha256+'  '+e.file).concat(sha(mf)+'  MANIFEST.json').join('\n')+'\n');
}
let manifestEntries=0,checksumEntries=0;
if(fs.existsSync(path.join(own,'MANIFEST.json'))){
 for(const e of JSON.parse(read('MANIFEST.json')).entries){const b=read(e.file);if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Self manifest drift');manifestEntries++;}
 for(const l of read('SHA256SUMS').toString().trimEnd().split('\n')){const m=l.match(/^([a-f0-9]{64})  (.+)$/);if(!m||sha(read(m[2]))!==m[1])throw Error('Self checksum drift');checksumEntries++;}
}
console.log(JSON.stringify({inputPins:pins.length,priorManifestEntries:previous.length,manifestEntries,checksumEntries,allExact:true,noteSha256:sha(read('RESEARCH_NOTE.md')),sourceSha256:sha(read('SOURCE_LEDGER.md')),manifestSha256:manifestEntries?sha(read('MANIFEST.json')):null,checksumSha256:checksumEntries?sha(read('SHA256SUMS')):null,meaning:'Identity only, not mathematical or production acceptance'},null,2));
