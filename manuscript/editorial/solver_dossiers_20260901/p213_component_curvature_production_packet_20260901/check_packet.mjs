import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

// Identity/extraction checks only. No file writes, child processes or network.
const root=path.dirname(fileURLToPath(import.meta.url)), failures=[];
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(path.isAbsolute(p)?p:path.join(root,p));
function check(e){
  try{const b=read(e.path);if(hash(b)!==e.sha256)failures.push('SHA mismatch '+e.path);if(e.bytes!==undefined&&b.length!==e.bytes)failures.push('Size mismatch '+e.path);}
  catch(x){failures.push('Read error '+e.path+': '+x.message);}
}
const inputs=JSON.parse(read('INPUT_PINS.json')).inputs;inputs.forEach(check);
if(inputs.length!==7)failures.push('Expected seven input pins');
const ex=JSON.parse(read('EXTRACT_MAP.json')), source=read(ex.source), text=source.toString('utf8');
if(hash(source)!==ex.sourceSha256)failures.push('Extraction source SHA mismatch');
const reconstructed=[];
for(const s of ex.segments){
  const start=text.indexOf(s.startMarker),end=text.indexOf(s.endMarkerExcluded,start);
  if(start<0||end<start||text.indexOf(s.startMarker,start+1)>=0||text.indexOf(s.endMarkerExcluded,end+1)>=0){failures.push('Nonunique or missing extraction markers '+s.index);continue;}
  const pre=text.slice(0,start),post=text.slice(0,end),block=text.slice(start,end),bb=Buffer.from(block);
  const actual={startUtf8Byte:Buffer.byteLength(pre),endUtf8ByteExclusive:Buffer.byteLength(post),startUnicodeScalar:[...pre].length,endUnicodeScalarExclusive:[...post].length,startLine:pre.split('\n').length,endLineInclusive:post.split('\n').length-1,bytes:bb.length,unicodeScalars:[...block].length,sha256:hash(bb)};
  for(const [key,value]of Object.entries(actual))if(s[key]!==value)failures.push('Segment '+s.index+' '+key+' mismatch');
  reconstructed.push(bb);
}
const proof=read('PROOF.md'), joined=Buffer.concat(reconstructed);
if(!proof.equals(joined))failures.push('PROOF not exact segment concatenation');
if(proof.length!==ex.proofBytes||hash(proof)!==ex.proofSha256)failures.push('Proof identity differs from extraction map');
if(ex.segments.length!==2)failures.push('Expected two extract segments');
const ptext=proof.toString('utf8');
for(const excluded of ['(II) Retain','(1.2)','## 5.','## 6.','## 7.'])if(ptext.includes(excluded))failures.push('Excluded target/body retained: '+excluded);
const mf=JSON.parse(read('MANIFEST.json'));mf.entries.forEach(check);
if(mf.entries.length!==13)failures.push('Expected thirteen manifest entries');
const rows=read('SHA256SUMS').toString('utf8').trimEnd().split('\n'),seen=new Set();
for(const row of rows){const m=/^([a-f0-9]{64})  (.+)$/.exec(row);if(!m){failures.push('Malformed checksum row');continue;}if(seen.has(m[2]))failures.push('Duplicate checksum path '+m[2]);seen.add(m[2]);check({path:m[2],sha256:m[1]});}
if(rows.length!==14)failures.push('Expected fourteen checksum rows');
for(const e of mf.entries)if(!seen.has(e.path))failures.push('Missing checksum '+e.path);
if(!seen.has('MANIFEST.json'))failures.push('Missing manifest checksum');
const authored=['STATEMENT.md','PROOF.md','PACKAGING_REVIEW.md','EXTRACT_MAP.json','INPUT_PINS.json','check_packet.mjs','MANIFEST.json','SHA256SUMS'];
let controlCount=0;
for(const name of authored){const bad=[...read(name).toString('utf8')].filter(c=>{const k=c.codePointAt(0);return(k<32&&k!==9&&k!==10&&k!==13)||k===127;});controlCount+=bad.length;if(bad.length)failures.push('Controls in '+name);}
console.log(JSON.stringify({kind:'read-only packaging identity check, not mathematical or production verification',inputPins:inputs.length,exactExtractSegments:reconstructed.length,proofBytes:proof.length,manifestEntries:mf.entries.length,checksumRows:rows.length,authoredTextFiles:authored.length,forbiddenControls:controlCount,failures},null,2));
process.exitCode=failures.length?1:0;

