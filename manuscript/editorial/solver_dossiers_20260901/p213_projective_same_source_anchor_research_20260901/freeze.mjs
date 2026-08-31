// Mechanical identity, dependency and arithmetic checks; not a proof verifier.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const own=path.dirname(fileURLToPath(import.meta.url));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p);
const records=[];
function pin(file,expected,role){
  const p=path.resolve(own,file),b=read(p),actual=sha(b);
  if(expected&&actual!==expected)throw Error('Pinned input drift: '+file);
  const e={path:path.relative(own,p),bytes:b.length,sha256:actual,role};
  records.push(e);return b;
}
const archiveChecks=[];
function archive(dir,noteHash,manifestHash){
  pin(dir+'/RESEARCH_NOTE.md',noteHash,'Explicit conditional research input');
  const mf=pin(dir+'/MANIFEST.json',manifestHash,'Input archive identity, not a mathematical verdict');
  const sums=pin(dir+'/SHA256SUMS',null,'Input checksum-list identity');
  const parsed=JSON.parse(mf),entries=parsed.entries||parsed.files;
  for(const e of entries){
    const file=e.file||e.path,b=read(path.resolve(own,dir,file));
    if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Input manifest mismatch: '+dir+'/'+file);
  }
  const lines=sums.toString().trimEnd().split('\n');
  for(const line of lines){
    const m=line.match(/^([a-f0-9]{64})  (.+)$/);
    if(!m||sha(read(path.resolve(own,dir,m[2])))!==m[1])throw Error('Input checksum mismatch: '+dir);
  }
  archiveChecks.push({directory:dir,manifestEntries:entries.length,checksumEntries:lines.length});
}
archive('../p213_saturated_open_model_propagation_research_20260901',
  'a77fe9f80d2da71d1c9c81163955808736b38508f49da76f0cf8ad8d81fdbefc',
  '0b3abe46b75019f87f2e8a7206ccd6b98f729ff9c59caacdc9bfac4665f4be91');
archive('../p213_stratum_incidence_controlled_chambers_research_20260901',
  '30d3d66a465dd51e488fa7f4b440aa2d083fc1640bd331fa61a1472acab5df34',
  'a250bf5f9e2473433cb078fd58261d0fab401446cf1b6546e761faa75565dcd3');
archive('../../solver_dossiers_20260831/p213_nonreduced_tube_finite_projection_research_20260831',
  '3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a',
  'd82be02c8b536651f8e9366c407448139c88cf7044158edc419834c515b58fec');
archive('../../solver_dossiers_20260831/p213_ordinary_open_outer_collar_research_20260831',
  'f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b',
  'eea85c5daa7630ffc8d0d2774b2f50fbfd8a4419ddb1b2df95257b8455075bab');
archive('../p213_proper_target_open_comparison_20260901',
  '35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec',
  'ced5e08f745aee9ae83f09e8cf7063099a9532208776ee0e114ac79915cfeefa');
pin('../../solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation/statement.tex',
  '5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a','ONLY displayed R assumed; its proof is not accepted');
pin('../p213_maximal_rank_source_cell_capture_research_20260901/RESEARCH_NOTE.md',
  '4cc25ff627af56aca05c8733e3e5bff65aea21015abe35e49726f9966bb1b384','Related background; not a same-generic-X model input');
pin('../p213_source_cell_residual_curve_access_v2_20260901/RESEARCH_NOTE.md',
  '177d7ea0e2f5fd1cde5e9539b4cd88ce90623a1ee78202f9050b08cb00130d96','Related background; not a same-generic-X model input');
pin('/private/tmp/BFJ_singular_1201.0187_audit_20260831.pdf',
  '8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270','Primary-source bytes');
pin('/private/tmp/BFJ_singular_1201.0187_audit_20260831.txt',
  'df3fa71656240742234907514956389d2f2533e20bb89cd877bd235a922e5f1f','Primary-source text read');
pin('/private/tmp/CLD25.txt',
  '021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e','Primary-source text read');

const authored=['RESEARCH_NOTE.md','SOURCE_LEDGER.md','freeze.mjs'];
for(const file of authored){
  const b=read(path.join(own,file));
  if(!b.length||b[b.length-1]!==10)throw Error('Missing final newline '+file);
  if([...b].some(v=>(v<32&&v!==9&&v!==10)||v===127))throw Error('Control character '+file);
}
const noteHash=sha(read(path.join(own,'RESEARCH_NOTE.md')));
if(noteHash!=='f6626819973ecf135a2065786a0bee3fa1847592fc061f5892da7e31a591117c')throw Error('Reviewed candidate changed');
if(sha(read(path.join(own,'SOURCE_LEDGER.md')))!=='583b2cff4943f043cc2d10ea6532434ad8f860c57bdca28d076ed942280a5f56')throw Error('Source ledger changed');
function det(a){
  if(a.length===1)return a[0][0];
  return a[0].reduce((s,v,j)=>s+(j%2?-1n:1n)*v*det(a.slice(1).map(row=>row.filter((_,k)=>k!==j))),0n);
}
let arithmeticCases=0,invertibleCases=0;
for(let n=2;n<=5;n++)for(let ne=1;ne<=4;ne++)for(let seed=0;seed<12;seed++){
  const normal=Array.from({length:n+1},(_,j)=>BigInt(j===0?ne:1+(seed+j)%5));
  const d=Array.from({length:n},(_,i)=>Array.from({length:n+1},(_,j)=>BigInt(((seed+2)*(i+3)*(j+5)+i*i+3*j)%11-5)));
  const c=d.map(row=>row.slice(1).map((v,j)=>normal[0]*v-row[0]*normal[j+1]));
  const full=det([normal,...d]);
  if(det(c)!==normal[0]**BigInt(n-1)*full)throw Error('Exact affine determinant identity failed');
  arithmeticCases++;if(full!==0n)invertibleCases++;
}
const validation={date:'2026-09-01',noteSha256:noteHash,inputPins:records.length,archiveChecks,
  authoredTextControlCharacters:0,exactIntegerDeterminantCases:arithmeticCases,invertibleCases,
  status:'Mechanical identity and arithmetic checks only. Independent exact-final and production verification are separate.',
  preFreezeChanges:'Reviewer requested explicit nonempty W and separation of actual formal-tube geometry from L. Root supplied those clarifications and sigma-compact local domains for the R interface. No proof of R or new production acceptance.'};
const generated=['INPUT_PINS.json','VALIDATION.json','MANIFEST.json','SHA256SUMS'];
if(process.argv.includes('--freeze')){
  for(const file of generated)if(fs.existsSync(path.join(own,file)))throw Error('Refuse refreeze '+file);
  fs.writeFileSync(path.join(own,'INPUT_PINS.json'),JSON.stringify({date:'2026-09-01',files:records},null,2)+'\n',{flag:'wx'});
  fs.writeFileSync(path.join(own,'VALIDATION.json'),JSON.stringify(validation,null,2)+'\n',{flag:'wx'});
  const files=[...authored,'INPUT_PINS.json','VALIDATION.json'].map(file=>{
    const b=read(path.join(own,file));return{file,bytes:b.length,sha256:sha(b)};
  }).concat(records.map(e=>({file:e.path,bytes:e.bytes,sha256:e.sha256,role:e.role})));
  const manifest={date:'2026-09-01',author:'/root',status:'Frozen authored conditional research, pending independent exact-final and production review',
    scope:'Projective original-X model capture; current conclusions depend explicitly on geometry/L/O/Q/displayed R. No open-problem retirement.',entries:files};
  const mf=Buffer.from(JSON.stringify(manifest,null,2)+'\n');
  fs.writeFileSync(path.join(own,'MANIFEST.json'),mf,{flag:'wx'});
  fs.writeFileSync(path.join(own,'SHA256SUMS'),[...files.map(e=>e.sha256+'  '+e.file),sha(mf)+'  MANIFEST.json'].join('\n')+'\n',{flag:'wx'});
}
let selfEntries=0,selfSums=0;
if(fs.existsSync(path.join(own,'MANIFEST.json'))){
  const mf=JSON.parse(read(path.join(own,'MANIFEST.json')));
  for(const e of mf.entries){const b=read(path.resolve(own,e.file));if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Self manifest mismatch '+e.file);selfEntries++;}
  for(const line of read(path.join(own,'SHA256SUMS')).toString().trimEnd().split('\n')){
    const m=line.match(/^([a-f0-9]{64})  (.+)$/);if(!m||sha(read(path.resolve(own,m[2])))!==m[1])throw Error('Self checksum mismatch');selfSums++;
  }
}
console.log(JSON.stringify({...validation,frozen:fs.existsSync(path.join(own,'MANIFEST.json')),selfEntries,selfSums,
  manifestSha256:fs.existsSync(path.join(own,'MANIFEST.json'))?sha(read(path.join(own,'MANIFEST.json'))):null,
  checksumFileSha256:fs.existsSync(path.join(own,'SHA256SUMS'))?sha(read(path.join(own,'SHA256SUMS'))):null},null,2));
