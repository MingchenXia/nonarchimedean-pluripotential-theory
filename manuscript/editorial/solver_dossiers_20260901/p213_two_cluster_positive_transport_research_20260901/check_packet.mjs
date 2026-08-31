import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

const dir=path.dirname(fileURLToPath(import.meta.url));
const editorial='/private/tmp/nappt_p071_20260827/manuscript/editorial';
const d31=editorial+'/solver_dossiers_20260831/';
const d01=editorial+'/solver_dossiers_20260901/';
const packetDirs={
 L:d31+'p213_nonreduced_tube_finite_projection_research_20260831',
 O:d31+'p213_ordinary_open_outer_collar_research_20260831',
 Q:d01+'p213_proper_target_open_comparison_20260901',
 diagnostic:d01+'p213_common_constant_propagation_diagnostic_20260901'
};
const rdir=d31+'p213_skeletal_packets_20260831/skeletal_representation';
const pins=[
 [packetDirs.L+'/RESEARCH_NOTE.md','3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a','L conditional principal'],
 [packetDirs.O+'/RESEARCH_NOTE.md','f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b','O conditional principal; author-related'],
 [packetDirs.Q+'/RESEARCH_NOTE.md','35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec','Q conditional principal'],
 [rdir+'/statement.tex','5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a','displayed R only'],
 [rdir+'/proof.tex','27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a','R proof provenance, not established'],
 [packetDirs.diagnostic+'/DIAGNOSTIC.md','0961f3f5b771605e7acf580e490dc404a95f95447b3291b55fcc10b4a97b304f','frozen diagnostic motivation'],
 ['/private/tmp/CLD25.txt','021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e','primary text read'],
 ['/private/tmp/CLD25.pdf','5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719','primary PDF identity, no new render']
];
const hash=b=>createHash('sha256').update(b).digest('hex');
const info=(p,role)=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:hash(b),role};};
const errors=[];
const entries=[];
for(const [p,expected,role] of pins){
 const e=info(p,role);entries.push(e);
 if(e.sha256!==expected) errors.push('Principal pin mismatch: '+p);
}
const histories=[];
for(const [name,pdir] of Object.entries(packetDirs)){
 for(const filename of ['SOURCE_LEDGER.md','MANIFEST.json','SHA256SUMS'])
   entries.push(info(pdir+'/'+filename,name+' preserved '+filename));
 const m=JSON.parse(fs.readFileSync(pdir+'/MANIFEST.json','utf8'));
 let n=0;
 for(const e of m.entries){
   const p=path.resolve(pdir,e.path), got=info(p,'');
   if(got.sha256!==e.sha256 || (e.bytes!==undefined&&got.bytes!==e.bytes))
      errors.push(name+' historical manifest mismatch: '+p);
   n++;
 }
 let s=0;
 for(const line of fs.readFileSync(pdir+'/SHA256SUMS','utf8').trim().split('\n')){
   const match=line.match(/^([0-9a-f]{64})  (.+)$/);
   if(!match){errors.push(name+' bad checksum line');continue;}
   const p=path.resolve(pdir,match[2]);
   if(info(p,'').sha256!==match[1]) errors.push(name+' historical checksum mismatch: '+p);
   s++;
 }
 histories.push({name,manifestEntries:n,checksumEntries:s});
}
const controls=[];
for(const filename of ['RESEARCH_NOTE.md','SOURCE_LEDGER.md','check_packet.mjs','VALIDATION.md','MANIFEST.json','SHA256SUMS']){
 const p=dir+'/'+filename;
 if(!fs.existsSync(p)) continue;
 const b=fs.readFileSync(p);
 const bad=[];
 for(let i=0;i<b.length;i++) if((b[i]<32&&b[i]!==9&&b[i]!==10)||b[i]===127) bad.push(i);
 controls.push({file:filename,forbiddenControls:bad.length});
 if(bad.length) errors.push('Forbidden control bytes: '+filename);
 if(!['MANIFEST.json','SHA256SUMS'].includes(filename))
   entries.push(info(p,'new authored output'));
}
const note=fs.readFileSync(dir+'/RESEARCH_NOTE.md','utf8');
const tags=[...note.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
const structural={
 equationTags:tags.length,
 uniqueEquationTags:new Set(tags).size,
 displayOpen:(note.match(/\\\[/g)||[]).length,
 displayClose:(note.match(/\\\]/g)||[]).length,
 inlineOpen:(note.match(/\\\(/g)||[]).length,
 inlineClose:(note.match(/\\\)/g)||[]).length
};
if(structural.equationTags!==structural.uniqueEquationTags) errors.push('Duplicate equation tags');
if(structural.displayOpen!==structural.displayClose||structural.inlineOpen!==structural.inlineClose) errors.push('Unbalanced math delimiters');
let arithmeticCases=0;
for(let n=2;n<=12;n++){
 const d=n-1,ell=1;
 for(const scale of [1/4,1/3,1/2,2/3]){
   const u=Array.from({length:d},(_,i)=>scale*(i+1)/(d*(d+1)/2));
   const sum=u.reduce((a,b)=>a+b,0), alpha0=ell-sum;
   const delta=alpha0/4, s=delta/2;
   const y0=ell-sum-s, zMinusC=y0+sum;
   if(!(u.every(x=>x>0)&&alpha0>0&&y0>0&&zMinusC>0&&zMinusC<ell))
      errors.push('Positive-margin sample failed');
   if(Math.abs(zMinusC-(ell-s))>1e-12)
      errors.push('Infinity substitution sample failed');
   let residual=ell;
   for(const pivot of [...u,alpha0]) residual-=pivot;
   if(Math.abs(residual)>1e-12) errors.push('Ordered pivot product sample failed');
   arithmeticCases++;
 }
}
const finalVerification={manifestEntries:0,checksumEntries:0};
if(fs.existsSync(dir+'/MANIFEST.json')){
 const own=JSON.parse(fs.readFileSync(dir+'/MANIFEST.json','utf8'));
 for(const e of own.entries){
   const got=info(path.resolve(dir,e.path),'');
   if(got.sha256!==e.sha256||got.bytes!==e.bytes) errors.push('Own manifest mismatch: '+e.path);
   finalVerification.manifestEntries++;
 }
}
if(fs.existsSync(dir+'/SHA256SUMS')){
 for(const line of fs.readFileSync(dir+'/SHA256SUMS','utf8').trim().split('\n')){
   const m=line.match(/^([0-9a-f]{64})  (.+)$/);
   if(!m){errors.push('Malformed own checksum');continue;}
   if(info(path.resolve(dir,m[2]),'').sha256!==m[1]) errors.push('Own checksum mismatch: '+m[2]);
   finalVerification.checksumEntries++;
 }
}
console.log(JSON.stringify({date:'2026-09-01',directPins:pins.length,histories,controls,structural,arithmeticCases,arithmeticStatus:'Sanity checks only; not a mathematical proof or test of Q-independence',entries,finalVerification,errors},null,2));
if(errors.length)process.exitCode=1;

