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
const prior='../p213_qualified_scalar_assembly_research_20260901/';
pin(prior+'RESEARCH_NOTE.md','5809b99def2c16becb716eb2eb7c24382a8a31655b9b43902804e585cb53bb5c','Complete quasi-smooth scalar input; not an arbitrary-field statement');
pin(prior+'SOURCE_LEDGER.md','e7e80db8edd6233b00b75840fd9af6a57b4d8c4e6a5a419aa4fae4ad7c5954d0','Prior source interfaces');
pin(prior+'MANIFEST.json','535c616d5bddd8f86fb6431ca050af294ca58b09493c2ac7aedc37a4dd33fdb2','Prior exact dependencies');
pin('../p213_normal_extension_source_audit_20260901/AUDIT.md','909574946540d4efc3cf34452250d441914b7356d64aff670b4d39f1aa04ad89','Independent general-complement source/interface argument; not a review of this classification');
pin('../p213_qualified_scalar_assembly_fresh_audit_20260901/AUDIT.md','d7e86b6472b69e18aa76b7baf153ca9acd181f411b51edccd0953b3019c39141','Prior independently scoped review, not production');
pin('/private/tmp/CLD25.txt','021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e','Primary source: support of forms, nilreduction and cycles');
pin('../../rethlas_packets_20260829/p213_componentwise_arbitrary_valuation_live_ready_20260829/p213_componentwise_arbitrary_valuation_proof_live_ready_20260829.tex',null,'Existing curve proof read for comparison only; curve classification and zero-atom conclusions not imported');
const previous=JSON.parse(read(prior+'MANIFEST.json')).entries;
for(const e of previous){const b=fs.readFileSync(path.resolve(own,prior,e.file));if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Prior manifest drift');}
const authored=['RESEARCH_NOTE.md','SOURCE_LEDGER.md','freeze.mjs'];
for(const f of authored){const b=read(f);if(!b.length||b.at(-1)!==10||[...b].some(x=>(x<32&&x!==9&&x!==10)||x===127))throw Error('Text integrity '+f);}
const generated=['INPUT_PINS.json','VALIDATION.json','MANIFEST.json','SHA256SUMS'];
if(process.argv.includes('--freeze')){
 for(const f of generated)if(fs.existsSync(path.join(own,f)))throw Error('Refuse refreeze');
 const write=(f,b)=>fs.writeFileSync(path.join(own,f),b,{flag:'wx'});
 write('INPUT_PINS.json',JSON.stringify({date:'2026-09-01',files:pins},null,2)+'\n');
 write('VALIDATION.json',JSON.stringify({date:'2026-09-01',inputPins:pins.length,priorManifestEntries:previous.length,controlByteErrors:0,mathematicalVerdict:'Not supplied by script',independentStatus:'Complete component classification and curvature reduction await exact-final review',productionStatus:'Not verified',liveChanges:false,atomRetirements:0},null,2)+'\n');
 const entries=[...authored,'INPUT_PINS.json','VALIDATION.json'].map(file=>{const b=read(file);return{file,bytes:b.length,sha256:sha(b)};}).concat(pins);
 const mf=JSON.stringify({date:'2026-09-01',status:'Frozen component scalar classification and curvature-reduction candidate; no production or live promotion',entries},null,2)+'\n';
 write('MANIFEST.json',mf);
 write('SHA256SUMS',entries.map(e=>e.sha256+'  '+e.file).concat(sha(mf)+'  MANIFEST.json').join('\n')+'\n');
}
let manifestEntries=0,checksumEntries=0;
if(fs.existsSync(path.join(own,'MANIFEST.json'))){
 for(const e of JSON.parse(read('MANIFEST.json')).entries){const b=read(e.file);if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Self manifest drift');manifestEntries++;}
 for(const l of read('SHA256SUMS').toString().trimEnd().split('\n')){const m=l.match(/^([a-f0-9]{64})  (.+)$/);if(!m||sha(read(m[2]))!==m[1])throw Error('Self checksum drift');checksumEntries++;}
}
console.log(JSON.stringify({inputPins:pins.length,priorManifestEntries:previous.length,manifestEntries,checksumEntries,allExact:true,noteSha256:sha(read('RESEARCH_NOTE.md')),sourceSha256:sha(read('SOURCE_LEDGER.md')),manifestSha256:manifestEntries?sha(read('MANIFEST.json')):null,checksumSha256:checksumEntries?sha(read('SHA256SUMS')):null,meaning:'Identity only, not mathematical or production acceptance'},null,2));
