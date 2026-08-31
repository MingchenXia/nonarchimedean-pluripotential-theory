import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)}};
const specs=[
 {version:'original',dir:"/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_source_cell_residual_curve_access_20260901",count:14,sums:15,pins:{
  'RESEARCH_NOTE.md':'46eba8ebccb7d87c404c184a83ae51bce9f84e2d14f636fba19212d1fe73c596',
  'MANIFEST.json':'a50514a0fce52b892f171e261ba8e9c2bcd2990cc869f1e1026ce1453091c7c2',
  'SHA256SUMS':'3a1a25e1988e4e12839ba3fb88c32c60133a02e04c25c996bbe6008742edf2d3'}},
 {version:'v2',dir:"/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_source_cell_residual_curve_access_v2_20260901",count:16,sums:17,pins:{
  'RESEARCH_NOTE.md':'177d7ea0e2f5fd1cde5e9539b4cd88ce90623a1ee78202f9050b08cb00130d96',
  'MANIFEST.json':'c912270c7f14e791bea153775c628fb3f75d02b53dce327c91e92f04d738afb6',
  'SHA256SUMS':'8979b1174460a7cfe910094aef7d27faac46d2aecc12f9ab4d581becefb2b163'}}
];
const errors=[],records=new Map();
const add=(r,role)=>{if(!records.has(r.path))records.set(r.path,{path:r.path,bytes:r.bytes,sha256:r.sha256,role})};
const versions=specs.map(sp=>{
 const pins=Object.entries(sp.pins).map(([f,h])=>{const r=read(path.resolve(sp.dir,f));const match=r.sha256===h;if(!match)errors.push(sp.version+' pin '+f);add(r,sp.version+' freeze record');return{...r,expectedSha256:h,match}});
 const m=JSON.parse(fs.readFileSync(path.join(sp.dir,'MANIFEST.json'),'utf8'));
 const entries=m.entries.map(e=>{const r=read(path.resolve(sp.dir,e.path));const match=r.bytes===e.bytes&&r.sha256===e.sha256;if(!match)errors.push(sp.version+' entry '+e.path);add(r,e.role);return{...r,expectedBytes:e.bytes,expectedSha256:e.sha256,match}});
 const sums=fs.readFileSync(path.join(sp.dir,'SHA256SUMS'),'utf8').trim().split('\n').map(s=>{const a=s.match(/^([a-f0-9]{64})  (.+)$/);if(!a)throw Error('Malformed checksum');const r=read(path.resolve(sp.dir,a[2]));const match=r.sha256===a[1];if(!match)errors.push(sp.version+' checksum '+a[2]);return{...r,expectedSha256:a[1],match}});
 const t=fs.readFileSync(path.join(sp.dir,'RESEARCH_NOTE.md'),'utf8');
 const tags=[...t.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
 if(entries.length!==sp.count||sums.length!==sp.sums||tags.length!==12||new Set(tags).size!==12)errors.push(sp.version+' counts');
 if([...t].some(c=>(c.charCodeAt(0)<32&&!'\n\r\t'.includes(c))||c.charCodeAt(0)===127))errors.push(sp.version+' control byte');
 return{version:sp.version,pins,entries,sums,equationTags:tags,checks:{pins:pins.length,entries:entries.length,sums:sums.length,distinctTags:new Set(tags).size}};
});
const old=fs.readFileSync(path.join(specs[0].dir,'RESEARCH_NOTE.md'),'utf8');
const revised=fs.readFileSync(path.join(specs[1].dir,'RESEARCH_NOTE.md'),'utf8');
const oldSentence='Let Delta be a compact full-dimensional source cell for F, on which F is affine-injective.';
const newSentence='Let Delta be a compact full-dimensional source cell for the restriction F|W, explicitly with Delta contained in W, on which F is affine-injective.';
const versionLine='Version 2: the source cell is explicitly required to belong to W. The frozen first version remains unchanged; see the source ledger.\n';
const expected=old.replace('Date: 1 September 2026. Research author: /root.\n','Date: 1 September 2026. Research author: /root.\n'+versionLine).replace(oldSentence,newSentence);
const exactTwoNoteChanges=expected===revised;
if(!exactTwoNoteChanges)errors.push('Unexpected mathematical-note revision');
const textRecord=read('/private/tmp/CLD25.txt');
const primaryMatch=textRecord.sha256==='021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e';
if(!primaryMatch)errors.push('CLD text pin');
add(textRecord,'primary CLD text; specified passages read in this audit');
console.log(JSON.stringify({scope:'Read-only exact-byte and revision checks, not proof or production verification',versions,revision:{exactTwoNoteChanges,oldSentence,newSentence,versionLine},primaryText:{...textRecord,match:primaryMatch},inputRecords:[...records.values()],checks:{inputRecords:records.size,mismatches:errors.length},errors},null,2));
if(errors.length)process.exitCode=1;

