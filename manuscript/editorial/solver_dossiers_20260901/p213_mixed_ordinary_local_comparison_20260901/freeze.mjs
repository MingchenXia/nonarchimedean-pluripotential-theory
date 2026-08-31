// Default: read-only identity check. --freeze writes new manifest files exclusively.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const old='../../solver_dossiers_20260831';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pins=[
 [`${old}/p213_point_retaining_mixed_blowup_research_20260831/RESEARCH_NOTE.md`,'1d8531a8cc4df4a11f21e56ba02ad4393f192f1ad8bec55c1c9cb27126ce4f55','P geometric premise'],
 [`${old}/p213_point_retaining_mixed_blowup_research_20260831/SOURCE_LEDGER.md`,'f8369a2fd6d2ae112ba2be316eef3a794901f97ee9a6c8055066b20fb982c450','P source ledger'],
 [`${old}/p213_ordinary_open_outer_collar_research_20260831/RESEARCH_NOTE.md`,'f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b','O ordinary-local premise'],
 [`${old}/p213_ordinary_open_outer_collar_research_20260831/SOURCE_LEDGER.md`,'6cceb8f6f03141e6115262fbe2b164227b1b51afa939b627c18047680241c776','O source ledger'],
 ['../p213_proper_target_open_comparison_20260901/RESEARCH_NOTE.md','35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec','Q conditional restricted-source premise'],
 ['../p213_proper_target_open_comparison_20260901/SOURCE_LEDGER.md','cbaa9e9c851539fdeb1f04c7030912fd0eb6cfcd1c088f4b234a682938df953e','Q source ledger'],
 [`${old}/p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md`,'3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a','L conditional geometry'],
 [`${old}/p213_skeletal_packets_20260831/skeletal_representation/statement.tex`,'5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a','R displayed conditional identity'],
 [`${old}/p213_skeletal_packets_20260831/skeletal_representation/proof.tex`,'27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a','R proof interface'],
 [`${old}/p213_point_retaining_mixed_blowup_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md`,'13697cdbb10c9e49dd576da4997f83974b5a0a420853e823c0ea684970a332cc','P independent review provenance'],
 ['../p213_ordinary_open_outer_collar_independent_audit_20260901/INDEPENDENT_EXACT_BYTE_AUDIT.md','54baec9bfce2a4d664434b260ef6395c56357025f400925058380e58ff07cf4c','O independent review provenance'],
 ['../p213_proper_target_open_comparison_independent_audit_20260901/INDEPENDENT_EXACT_BYTE_AUDIT.md','0ea9513fc0070fcc300bf3b43fa9da8ddc4363a8f063abae63527e3e80589603','Q independent review provenance'],
];
const entries=pins.map(([relative,expected,role])=>{
 const b=fs.readFileSync(path.resolve(here,relative));
 if(sha(b)!==expected)throw Error('Input changed '+relative);
 return {path:relative,bytes:b.length,sha256:expected,role};
});
for(const name of ['RESEARCH_NOTE.md','SOURCE_LEDGER.md','freeze.mjs']){
 const b=fs.readFileSync(path.join(here,name));
 if([...b].some(c=>(c<32&&c!==9&&c!==10)||c===127))throw Error('Unexpected control '+name);
 entries.push({path:name,bytes:b.length,sha256:sha(b),role:'new authored output'});
}
const text=fs.readFileSync(path.join(here,'RESEARCH_NOTE.md'),'utf8');
const tags=[...text.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
if(new Set(tags).size!==tags.length)throw Error('Duplicate equation tags');
const manifest=path.join(here,'MANIFEST.json'),sumfile=path.join(here,'SHA256SUMS');
if(fs.existsSync(manifest)){
 if(process.argv.includes('--freeze'))throw Error('Already frozen');
 const m=JSON.parse(fs.readFileSync(manifest,'utf8'));
 for(const e of m.entries){const b=fs.readFileSync(path.resolve(here,e.path));if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Changed manifest entry '+e.path);}
 const lines=fs.readFileSync(sumfile,'utf8').trim().split('\n');
 for(const line of lines){const r=line.match(/^([a-f0-9]{64})  (.+)$/);if(!r||sha(fs.readFileSync(path.resolve(here,r[2])))!==r[1])throw Error('Changed checksum');}
 console.log(JSON.stringify({checked:true,entries:m.entries.length,sums:lines.length,uniqueTags:tags.length,manifestSha:sha(fs.readFileSync(manifest))}));process.exit(0);
}
if(!process.argv.includes('--freeze')){console.log(JSON.stringify({preflight:true,entries:entries.length,uniqueTags:tags.length,outputs:entries.slice(-3)},null,2));process.exit(0);}
if(fs.existsSync(sumfile))throw Error('Unexpected existing checksum file');
const m={date:'2026-09-01',author:'/root',status:'Frozen conditional synthesis; independent and production review required',scope:'Mixed SNC residual-curve coefficients for a current only on ordinary W at an assumed independent normal point; specified source interpretation conditional on Q and displayed R',exclusions:['no all-moment rigidity','no arbitrary-cell capture','no higher-bidegree result','no current extension','no production or priority claim'],checks:{forbiddenControls:0,distinctEquationTags:tags.length},entries};
const bytes=JSON.stringify(m,null,2)+'\n';fs.writeFileSync(manifest,bytes,{flag:'wx'});
const sums=entries.map(e=>e.sha256+'  '+e.path).concat(sha(bytes)+'  MANIFEST.json').join('\n')+'\n';fs.writeFileSync(sumfile,sums,{flag:'wx'});
console.log(JSON.stringify({frozen:true,entries:entries.length,sums:entries.length+1,noteSha:entries.at(-3).sha256,manifestSha:sha(bytes),sumsSha:sha(sums)},null,2));
