#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const base='/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831';
const candidate=path.join(base,'p213_general_snc_wall_residual_functional_research_20260831');
const digest=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};};
const pins={
'RESEARCH_NOTE.md':'1c8011863516d8bdc900b3432b270c923126ee36d6600d915f714dc016553ae7',
'OBSTRUCTIONS_AND_SOURCE_COMPARISON.md':'a101573735710ab80d881dd29750b7fa777265c9926f35c50929c3d866b7dc72',
'SOURCE_AND_INPUTS.md':'05b06d9ad8b132b5e915314b0f5a47c334f5e6e621b786f7515c4594138c0867',
'VALIDATION.json':'d7e72c6b6fbad1ed6293718fd84aaf02d85ce41eb007e2d680bf2cd93460251d',
'MANIFEST.json':'2ee5bb8478d7f4cd04b1632af51028c90023cc18323e9db5c8f67deea25d36b8',
'SHA256SUMS':'6d218ef106058a0b0b686612fcf923c969be81a5349d6f87dbdc8695482c38c5'};
const pinned=Object.entries(pins).map(([name,expected])=>{const x=digest(path.join(candidate,name));return {...x,expected,match:x.sha256===expected};});
const checkEntry=e=>{const x=digest(path.isAbsolute(e.path)?e.path:path.join(candidate,e.path));return {...x,expected_bytes:e.bytes,expected_sha256:e.sha256,match:x.bytes===e.bytes&&x.sha256===e.sha256};};
const manifest=JSON.parse(fs.readFileSync(path.join(candidate,'MANIFEST.json'),'utf8')).entries.map(checkEntry);
const validation=JSON.parse(fs.readFileSync(path.join(candidate,'VALIDATION.json'),'utf8'));
const embedded=[...validation.outputs,...validation.inputs].map(checkEntry);
const sums=fs.readFileSync(path.join(candidate,'SHA256SUMS'),'utf8').trim().split('\n').map(line=>{const m=line.match(/^([a-f0-9]{64})\s+\*?(.+)$/);if(!m)throw Error('Malformed checksum line');const x=digest(path.isAbsolute(m[2])?m[2]:path.join(candidate,m[2]));return {...x,expected:m[1],match:x.sha256===m[1]};});
const texts=['RESEARCH_NOTE.md','OBSTRUCTIONS_AND_SOURCE_COMPARISON.md','SOURCE_AND_INPUTS.md'].map(name=>{const b=fs.readFileSync(path.join(candidate,name));return {name,lines:b.toString('utf8').split('\n').length-1,forbidden_control_bytes:[...b].filter(x=>x<32&&![9,10,13].includes(x)).length};});
const result={date:'2026-08-31',reviewer:'/root/p081_weighted_repair_fresh',candidate,pinned,manifest,embedded,sums,texts,counts:{pinned:pinned.length,manifest:manifest.length,embedded:embedded.length,sums:sums.length,mismatches:[...pinned,...manifest,...embedded,...sums].filter(x=>!x.match).length},compile:'Not performed: frozen candidate is a Markdown research packet',production_calls:false,git_actions:false};
if(process.argv[2]){const a=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));result.audit_manifest=a.entries.map(checkEntry);result.audit_manifest_mismatches=result.audit_manifest.filter(x=>!x.match).length;}
console.log(JSON.stringify(result,null,2));
if(result.counts.mismatches||result.audit_manifest_mismatches||texts.some(x=>x.forbidden_control_bytes))process.exitCode=1;

