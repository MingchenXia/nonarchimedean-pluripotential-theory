import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const base='/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831';
const source=path.join(base,'p213_nonreduced_tube_finite_projection_research_20260831');
const hash=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};};
const check=e=>{const a=hash(e.path);return {...a,expected_bytes:e.bytes,expected_sha256:e.sha256,match:a.bytes===e.bytes&&a.sha256===e.sha256};};
const pins={
'RESEARCH_NOTE.md':'3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a',
'MANIFEST.json':'d82be02c8b536651f8e9366c407448139c88cf7044158edc419834c515b58fec',
'SHA256SUMS':'ffa51a4eb20e08654387444c57b8fff6e8bb995f182ed112c694bf995b476c6f'};
const pinned=Object.entries(pins).map(([n,h])=>{const a=hash(path.join(source,n));return {...a,expected:h,match:a.sha256===h};});
const manifest=JSON.parse(fs.readFileSync(path.join(source,'MANIFEST.json'),'utf8')).entries.map(check);
const sums=fs.readFileSync(path.join(source,'SHA256SUMS'),'utf8').trim().split('\n').map(l=>{const m=l.match(/^([a-f0-9]{64})  (.+)$/);if(!m)throw Error('Invalid sum');const a=hash(m[2]);return {...a,expected:m[1],match:a.sha256===m[1]};});
const control_checks=['RESEARCH_NOTE.md','SOURCE_LEDGER.md','freeze.mjs'].map(n=>{const b=fs.readFileSync(path.join(source,n));return {name:n,forbidden_control_bytes:[...b].filter(x=>x<32&&![9,10,13].includes(x)).length};});
const result={date:'2026-08-31',reviewer:'/root/p081_weighted_repair_fresh',source,pinned,manifest,sums,control_checks,counts:{pins:pinned.length,manifest:manifest.length,sums:sums.length,mismatches:[...pinned,...manifest,...sums].filter(x=>!x.match).length}};
if(process.argv[2]){result.audit_manifest=JSON.parse(fs.readFileSync(process.argv[2],'utf8')).entries.map(check);result.audit_manifest_mismatches=result.audit_manifest.filter(x=>!x.match).length;}
console.log(JSON.stringify(result,null,2));
if(result.counts.mismatches||result.audit_manifest_mismatches||control_checks.some(x=>x.forbidden_control_bytes))process.exitCode=1;

