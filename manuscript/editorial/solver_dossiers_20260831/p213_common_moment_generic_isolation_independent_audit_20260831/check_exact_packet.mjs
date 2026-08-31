import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

const audit=path.dirname(fileURLToPath(import.meta.url));
const candidate=path.resolve(audit,'../p213_common_moment_generic_isolation_research_20260831');
function snapshot(p){const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
const pins=[
 ['RESEARCH_NOTE.md','b3ef8bdbae6bce6459fd8b472ace0ed81567d8e465292841fc2331fc421ce079'],
 ['SOURCE_LEDGER.md','4de53dd9f687dd473258e3baf2933768317dff435b893c6818e821987b9f6a4d'],
 ['MANIFEST.json','3a80d5a0b68668adeb158bb56bb3689f8f5e63fe18dce0bae4065c4b7e1dd5e0']
].map(([name,expected])=>{const actual=snapshot(path.join(candidate,name));return{...actual,expected,matches:actual.sha256===expected};});
function manifestCheck(file){
 const m=JSON.parse(fs.readFileSync(file,'utf8'));
 const entries=m.entries.map(e=>{const actual=snapshot(path.resolve(path.dirname(file),e.path));return{...actual,expectedBytes:e.bytes,expectedSha256:e.sha256,role:e.role,matches:actual.bytes===e.bytes&&actual.sha256===e.sha256};});
 return{path:file,entryCount:entries.length,entries,mismatches:entries.filter(e=>!e.matches)};
}
function sumsCheck(file){
 const lines=fs.readFileSync(file,'utf8').trim().split(/\r?\n/).filter(l=>l&&!l.startsWith('#'));
 const entries=lines.map(l=>{const m=l.match(/^([0-9a-f]{64})\s+[* ]?(.+)$/);if(!m)throw Error('Bad checksum record '+l);const actual=snapshot(path.resolve(path.dirname(file),m[2]));return{...actual,expected:m[1],matches:actual.sha256===m[1]};});
 return{path:file,entryCount:entries.length,entries,mismatches:entries.filter(e=>!e.matches)};
}
const authorManifest=manifestCheck(path.join(candidate,'MANIFEST.json'));
const authorChecksums=sumsCheck(path.join(candidate,'SHA256SUMS'));
const historicalChecksums=sumsCheck(path.resolve(candidate,'../p213_product_common_moment_supplement_20260831/SHA256SUMS'));
const raw=fs.readFileSync(path.join(candidate,'RESEARCH_NOTE.md'),'utf8');
const tags=[...raw.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
const structural={tagCount:tags.length,tags,duplicateTags:tags.filter((v,i)=>tags.indexOf(v)!==i),prohibitedControlCharacters:[...raw.matchAll(/[\x00-\x08\x0b\x0c\x0e-\x1f]/g)].map(m=>m.index)};
const auditManifest=fs.existsSync(path.join(audit,'MANIFEST.json'))?manifestCheck(path.join(audit,'MANIFEST.json')):null;
const defectCount=pins.filter(p=>!p.matches).length+authorManifest.mismatches.length+authorChecksums.mismatches.length+historicalChecksums.mismatches.length+structural.duplicateTags.length+structural.prohibitedControlCharacters.length+(auditManifest?.mismatches.length??0);
console.log(JSON.stringify({schema:'common-moment-independent-exact-check-v1',date:'2026-08-31',candidate,audit,pins,authorManifest,authorChecksums,historicalChecksums,structural,auditManifest,defectCount,limitations:'Hash/structural checks are not mathematical proof. R is an explicit assumption for this audit.',operations:{candidateEdits:false,priorAuditEdits:false,liveEdits:false,production:false,git:false,texCompile:false,newPdf:false}},null,2));
process.exitCode=defectCount?1:0;

