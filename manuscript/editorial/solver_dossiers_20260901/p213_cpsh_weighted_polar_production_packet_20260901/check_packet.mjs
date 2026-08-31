import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
// Read-only byte/extraction validation: no subprocesses, network or writes.
const root=path.dirname(fileURLToPath(import.meta.url)),failures=[];
const read=p=>fs.readFileSync(path.isAbsolute(p)?p:path.join(root,p));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
function check(e){try{const b=read(e.path);if(hash(b)!==e.sha256)failures.push('Hash mismatch '+e.path);if(e.bytes!==undefined&&e.bytes!==b.length)failures.push('Size mismatch '+e.path);}catch(x){failures.push('Read failed '+e.path+': '+x.message);}}
const inputs=JSON.parse(read('INPUT_PINS.json')).inputs;inputs.forEach(check);
if(inputs.length!==7)failures.push('Expected seven inputs');
const map=JSON.parse(read('EXTRACT_MAP.json')),source=read(map.source),text=source.toString('utf8');
if(hash(source)!==map.sourceSha256)failures.push('Source extraction SHA mismatch');
for(const e of map.outputs){
 const a=text.indexOf(e.startMarker),z=text.indexOf(e.endMarkerExcluded,a);
 if(a<0||z<a||text.indexOf(e.startMarker,a+1)>=0||text.indexOf(e.endMarkerExcluded,z+1)>=0){failures.push('Missing/nonunique markers '+e.file);continue;}
 const pre=text.slice(0,a),post=text.slice(0,z),body=text.slice(a,z),expected=Buffer.from(body);
 const actual={startUtf8Byte:Buffer.byteLength(pre),endUtf8ByteExclusive:Buffer.byteLength(post),startUnicodeScalar:[...pre].length,endUnicodeScalarExclusive:[...post].length,startLine:pre.split('\n').length,endLineInclusive:post.split('\n').length-1,bytes:expected.length,unicodeScalars:[...body].length,sha256:hash(expected)};
 for(const[k,v]of Object.entries(actual))if(e[k]!==v)failures.push('Map mismatch '+e.file+' '+k);
 if(!read(e.file).equals(expected))failures.push('Not exact source substring '+e.file);
}
if(map.outputs.length!==2)failures.push('Expected two output extracts');
const statement=read('STATEMENT.md'),proof=read('PROOF.md'),p=proof.toString('utf8');
if(!proof.subarray(0,statement.length).equals(statement))failures.push('Statement not exact proof prefix');
for(let k=1;k<=8;k++)if(!p.includes('## '+k+'. '))failures.push('Missing complete proof section '+k);
for(const forbidden of ['## 9.','SOURCE_AUDIT.md','Section 9'])if(p.includes(forbidden))failures.push('Excluded optional dependency/text '+forbidden);
const mf=JSON.parse(read('MANIFEST.json'));mf.entries.forEach(check);
if(mf.entries.length!==13)failures.push('Expected thirteen manifest entries');
const rows=read('SHA256SUMS').toString('utf8').trimEnd().split('\n'),seen=new Set();
for(const row of rows){const m=/^([a-f0-9]{64})  (.+)$/.exec(row);if(!m){failures.push('Malformed checksum');continue;}if(seen.has(m[2]))failures.push('Duplicate checksum');seen.add(m[2]);check({path:m[2],sha256:m[1]});}
if(rows.length!==14)failures.push('Expected fourteen checksum rows');
for(const e of mf.entries)if(!seen.has(e.path))failures.push('Missing checksum '+e.path);
if(!seen.has('MANIFEST.json'))failures.push('Missing manifest checksum');
const own=['STATEMENT.md','PROOF.md','PACKAGING_REVIEW.md','EXTRACT_MAP.json','INPUT_PINS.json','check_packet.mjs','MANIFEST.json','SHA256SUMS'];let controls=0;
for(const name of own){const bad=[...read(name).toString('utf8')].filter(c=>{const n=c.codePointAt(0);return(n<32&&n!==9&&n!==10&&n!==13)||n===127;});controls+=bad.length;if(bad.length)failures.push('Controls '+name);}
console.log(JSON.stringify({kind:'read-only packaging identity, not mathematical or production verification',inputPins:inputs.length,exactExtracts:map.outputs.length,statementBytes:statement.length,proofBytes:proof.length,manifestEntries:mf.entries.length,checksumRows:rows.length,authoredTextFiles:own.length,forbiddenControls:controls,failures},null,2));process.exitCode=failures.length?1:0;

