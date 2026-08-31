// Exact-byte freeze only. Default invocation is a read-only check.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const old=path.resolve(here,'../../solver_dossiers_20260831');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins=[
 [path.join(old,'p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md'),'3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a','conditional L'],
 [path.join(old,'p213_nonreduced_tube_finite_projection_research_20260831/SOURCE_LEDGER.md'),'cdf06f52596133e91abaa2c2e5870bbfb2db0f56ee71dd10dd2311636ccb9898','L source ledger'],
 [path.join(old,'p213_skeletal_packets_20260831/skeletal_representation/statement.tex'),'5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a','conditional displayed R statement'],
 [path.join(old,'p213_skeletal_packets_20260831/skeletal_representation/proof.tex'),'27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a','conditional R proof'],
 ['/private/tmp/CLD25.txt','021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e','primary extracted text'],
];
const entries=pins.map(([file,expected,role])=>{
 const b=fs.readFileSync(file);if(sha(b)!==expected)throw Error('Changed input '+file);
 return{path:file,bytes:b.length,sha256:expected,role};
});
for(const name of['RESEARCH_NOTE.md','SOURCE_LEDGER.md','freeze.mjs']){
 const file=path.join(here,name),b=fs.readFileSync(file);
 if(/[\x00-\x08\x0b-\x1f\x7f]/.test(b.toString('utf8')))throw Error('Forbidden control '+name);
 entries.push({path:file,bytes:b.length,sha256:sha(b),role:'new authored output'});
}
const tags=[...fs.readFileSync(path.join(here,'RESEARCH_NOTE.md'),'utf8').matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
if(new Set(tags).size!==tags.length)throw Error('Duplicate equation tag');
const manifest=path.join(here,'MANIFEST.json'),sumsPath=path.join(here,'SHA256SUMS');
if(fs.existsSync(manifest)){
 if(process.argv.includes('--freeze'))throw Error('Already frozen');
 const record=JSON.parse(fs.readFileSync(manifest,'utf8'));
 for(const e of record.entries){const b=fs.readFileSync(e.path);if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Manifest mismatch '+e.path);}
 const sums=fs.readFileSync(sumsPath,'utf8').trim().split('\n');
 for(const line of sums){const m=line.match(/^([a-f0-9]{64})  (.+)$/);if(!m||sha(fs.readFileSync(m[2]))!==m[1])throw Error('Checksum mismatch');}
 console.log(JSON.stringify({checked:true,entries:record.entries.length,sums:sums.length,uniqueTags:tags.length,manifestSha256:sha(fs.readFileSync(manifest))}));process.exit(0);
}
if(!process.argv.includes('--freeze')){console.log(JSON.stringify({preflight:true,entries:entries.length,uniqueTags:tags.length,outputs:entries.slice(-3)},null,2));process.exit(0);}
if(fs.existsSync(sumsPath))throw Error('Unexpected checksum file');
const record={date:'2026-09-01',author:'/root',status:'Frozen conditional localization proof; independent and production reviews pending',
 scope:'Current only on the full inverse image of any connected ordinary target open of a finite-projection tube; displayed source coefficients conditional on L and R',
 exclusions:['no current extension','no all-moment rigidity','no construction of outer collars or adapted models','no arbitrary-cell capture','no full P21.3 or priority claim'],
 checks:{forbiddenControls:0,distinctEquationTags:tags.length},entries};
const bytes=JSON.stringify(record,null,2)+'\n';fs.writeFileSync(manifest,bytes,{flag:'wx'});
const sums=entries.map(e=>e.sha256+'  '+e.path).concat(sha(bytes)+'  '+manifest).join('\n')+'\n';fs.writeFileSync(sumsPath,sums,{flag:'wx'});
console.log(JSON.stringify({frozen:true,entries:entries.length,sums:entries.length+1,noteSha256:entries[entries.length-3].sha256,manifestSha256:sha(bytes),sumsSha256:sha(sums)},null,2));
