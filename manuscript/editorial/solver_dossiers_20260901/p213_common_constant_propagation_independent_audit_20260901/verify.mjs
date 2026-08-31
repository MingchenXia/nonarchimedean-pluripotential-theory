import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const candidate="/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_common_constant_propagation_diagnostic_20260901";
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:hash(b)}};
const errors=[];
const expected={
 'DIAGNOSTIC.md':'0961f3f5b771605e7acf580e490dc404a95f95447b3291b55fcc10b4a97b304f',
 'MANIFEST.json':'15bda5f26ebd1f1613f1eff16d095eb27059f466dd1e0d0b9cab155d86347a56',
 'SHA256SUMS':'6c0d644f438b68520871b89919eba2e05202972c28f3f6fcb61f298d25cf5164'
};
const pins=Object.entries(expected).map(([f,h])=>{const r=read(path.join(candidate,f));const match=r.sha256===h;if(!match)errors.push('pin '+f);return{...r,expectedSha256:h,match}});
const m=JSON.parse(fs.readFileSync(path.join(candidate,'MANIFEST.json'),'utf8'));
const entries=m.entries.map(e=>{const r=read(path.resolve(candidate,e.path));const match=r.bytes===e.bytes&&r.sha256===e.sha256;if(!match)errors.push('entry '+e.path);return{...r,role:e.role,expectedBytes:e.bytes,expectedSha256:e.sha256,match}});
const sums=fs.readFileSync(path.join(candidate,'SHA256SUMS'),'utf8').trim().split('\n').map(l=>{const a=l.match(/^([a-f0-9]{64})  (.+)$/);if(!a)throw Error('Malformed sum');const r=read(path.resolve(candidate,a[2]));const match=r.sha256===a[1];if(!match)errors.push('sum '+a[2]);return{...r,expectedSha256:a[1],match}});
const checks=JSON.parse(fs.readFileSync(path.join(candidate,'CHECKS.json'),'utf8'));
const embedded=[...checks.own,...checks.external].map(e=>{const r=read(path.resolve(candidate,e.path));const match=r.bytes===e.bytes&&r.sha256===e.sha256;if(!match)errors.push('embedded '+e.path);return{...r,expectedBytes:e.bytes,expectedSha256:e.sha256,match}});
const text=fs.readFileSync(path.join(candidate,'DIAGNOSTIC.md'),'utf8');
const tags=[...text.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
const controls=[...text].filter(c=>(c.charCodeAt(0)<32&&!'\n\r\t'.includes(c))||c.charCodeAt(0)===127).length;
if(entries.length!==10||sums.length!==11||embedded.length!==9||tags.length!==12||new Set(tags).size!==12)errors.push('counts');
if(controls)errors.push('control bytes');
const records=entries.map(({path,bytes,sha256,role})=>({path,bytes,sha256,role}));
for(const {path,bytes,sha256} of pins)if(!records.some(e=>e.path===path))records.push({path,bytes,sha256,role:'candidate freeze record'});
console.log(JSON.stringify({scope:'Read-only exact-byte checks. HistoricalChecks count rows in candidate CHECKS.json are not newly recertified here.',candidate,pins,entries,sums,embeddedChecks:embedded,equationTags:tags,forbiddenControls:controls,inputRecords:records,checks:{pins:pins.length,manifestEntries:entries.length,sums:sums.length,embeddedRecords:embedded.length,distinctTags:new Set(tags).size,inputRecords:records.length,mismatches:errors.length},errors},null,2));
if(errors.length)process.exitCode=1;

