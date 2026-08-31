import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';

const audit=path.dirname(fileURLToPath(import.meta.url));
const editorial='/private/tmp/nappt_p071_20260827/manuscript/editorial';
const d31=editorial+'/solver_dossiers_20260831/';
const d01=editorial+'/solver_dossiers_20260901/';
const v1=d01+'p213_two_cluster_positive_transport_research_20260901';
const v2=d01+'p213_two_cluster_positive_transport_research_v2_20260901';
const hash=b=>createHash('sha256').update(b).digest('hex');
const record=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:hash(b)};};
const errors=[];
function checkPacket(dir,name) {
 const manifest=JSON.parse(fs.readFileSync(dir+'/MANIFEST.json','utf8'));
 const manifestChecks=manifest.entries.map(e=>{
  const actual=record(path.resolve(dir,e.path));
  const ok=actual.sha256===e.sha256&&(e.bytes===undefined||e.bytes===actual.bytes);
  if(!ok) errors.push(name+' manifest: '+e.path);
  return {...actual,ok};
 });
 const sumChecks=fs.readFileSync(dir+'/SHA256SUMS','utf8').trim().split('\n').map(line=>{
  const m=/^([a-f0-9]{64})  (.+)$/.exec(line);
  if(!m) throw new Error(name+' malformed checksum line');
  const actual=record(path.resolve(dir,m[2]));
  const ok=actual.sha256===m[1];
  if(!ok) errors.push(name+' checksum: '+m[2]);
  return {...actual,ok};
 });
 return {name,dir,manifestEntries:manifestChecks.length,checksumEntries:sumChecks.length,manifestChecks,sumChecks};
}
if(process.argv.includes('--self')){
 const result=checkPacket(audit,'independent audit');
 console.log(JSON.stringify({result,errors},null,2));
 if(errors.length) process.exitCode=1;
} else {
 const histories={
 L:d31+'p213_nonreduced_tube_finite_projection_research_20260831',
 O:d31+'p213_ordinary_open_outer_collar_research_20260831',
 Q:d01+'p213_proper_target_open_comparison_20260901',
 diagnostic:d01+'p213_common_constant_propagation_diagnostic_20260901'
 };
 const r=d31+'p213_skeletal_packets_20260831/skeletal_representation';
 const pins=[
 [v1+'/RESEARCH_NOTE.md','292087eb0b34072f15f7bb2426e8adf27fe03858aa85f30107538adf0962e4bf'],
 [v1+'/MANIFEST.json','0bda4e908fa42e8b683ef96fbe61ae34298482829d77fae645adab157dab717b'],
 [v1+'/SHA256SUMS','162116e70eb80c6f4f844e5e7a826f39b15e29116e0546215db8c81aa3c95e4d'],
 [v2+'/RESEARCH_NOTE.md','67b018aaac4b0d418dd99c04abe1e58773370ba19a7ebd83219f6d12b6e6b945'],
 [v2+'/REVISION_RECORD.md','a8b51d7f7c52be844d3e46eea21cddf0203a6c783088822ad7d174a35480bd1f'],
 [v2+'/MANIFEST.json','52f88c482d5fdaf7624b11c5a6a52d3ad6e616ded1d82be85ffe75dd99282e9d'],
 [v2+'/SHA256SUMS','d16af74c4a8c17569c283f7a20140bc6a71f421c0ab0a37e1950bea0ab38894b'],
 [histories.L+'/RESEARCH_NOTE.md','3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a'],
 [histories.O+'/RESEARCH_NOTE.md','f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b'],
 [histories.Q+'/RESEARCH_NOTE.md','35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec'],
 [r+'/statement.tex','5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a'],
 [r+'/proof.tex','27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a'],
 [histories.diagnostic+'/DIAGNOSTIC.md','0961f3f5b771605e7acf580e490dc404a95f95447b3291b55fcc10b4a97b304f'],
 ['/private/tmp/CLD25.txt','021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e'],
 ['/private/tmp/CLD25.pdf','5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719']
 ];
 const principalPins=pins.map(([p,expected])=>{
  const actual=record(p),ok=actual.sha256===expected;
  if(!ok)errors.push('Principal pin: '+p);
  return {...actual,expected,ok};
 });
 const candidates=[checkPacket(v1,'original v1'),checkPacket(v2,'preserved v2')];
 const historical=Object.entries(histories).map(([name,dir])=>checkPacket(dir,name));
 const old=fs.readFileSync(v1+'/RESEARCH_NOTE.md','utf8');
 const revised=fs.readFileSync(v2+'/RESEARCH_NOTE.md','utf8');
 const replacements=[
  [String.raw`Off the bad tubes \(t=0\).`,
   String.raw`Off the bad tubes \(t=0\), so \(\chi'(t)=0\) on an ordinary neighborhood of each such point because \(\chi\) is constant near zero; this makes no assertion that \(\mathrm d''t=0\) there.`],
  [String.raw`At the order-zero bad point 1 the entire shallow collar has \(|\zeta|=1\), hence \(\mathrm d''t=0\). Away from the bad tubes the same identity holds.`,
   String.raw`At the order-zero bad point 1, the entire shallow collar is an actual ordinary open set on which \(|\zeta|=1\); hence \(\mathrm d''t=0\) there. Away from the bad tubes we use only \(t=0\): since \(\chi\) is constant on a neighborhood of zero, \(\chi'(t)=0\) on an ordinary neighborhood of each such point. No vanishing of \(\mathrm d''t\) near the generic residual center is asserted.`]
 ];

 let forward=old,reverse=revised;
 const changes=replacements.map(([a,b])=>{
  const oldMatches=old.split(a).length-1,newMatches=revised.split(b).length-1;
  if(oldMatches!==1||newMatches!==1)errors.push('Nonunique expected replacement');
  forward=forward.replace(a,b);reverse=reverse.replace(b,a);
  return {old:a,new:b,oldMatches,newMatches};
 });
 const exactForward=forward===revised,exactReverse=reverse===old;
 if(!exactForward||!exactReverse)errors.push('Proof changed outside the two exact replacements');
 const structural=[['v1',old],['v2',revised]].map(([name,t])=>{
  const tags=[...t.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
  const result={name,tags,uniqueTags:new Set(tags).size,
   displayOpen:(t.match(/\\\[/g)||[]).length,displayClose:(t.match(/\\\]/g)||[]).length,
   inlineOpen:(t.match(/\\\(/g)||[]).length,inlineClose:(t.match(/\\\)/g)||[]).length};
  if(tags.length!==result.uniqueTags||result.displayOpen!==result.displayClose||result.inlineOpen!==result.inlineClose)
   errors.push('Structural delimiter/tag check: '+name);
  return result;
 });
 const controls=[];
 for(const dir of [v1,v2])for(const f of fs.readdirSync(dir).filter(f=>/\.(md|mjs|json)$/.test(f)||f==='SHA256SUMS')){
  const p=dir+'/'+f,b=fs.readFileSync(p);
  const forbidden=[...b].filter(x=>(x<32&&x!==9&&x!==10)||x===127).length;
  controls.push({path:p,forbidden});
  if(forbidden)errors.push('Forbidden controls: '+p);
 }
 const uniqueInputs=new Map();
 for(const p of principalPins)uniqueInputs.set(p.path,record(p.path));
 for(const c of candidates){
  for(const e of c.manifestChecks)uniqueInputs.set(e.path,record(e.path));
  for(const f of ['MANIFEST.json','SHA256SUMS'])uniqueInputs.set(c.dir+'/'+f,record(c.dir+'/'+f));
 }
 console.log(JSON.stringify({
  date:'2026-09-01',reviewer:'/root/p213_skeletal_hostile',mode:'read-only independent integrity checks',
  principalPins,candidates,historical,revision:{changes,exactForward,exactReverse,
   recoveredV1Sha256:hash(Buffer.from(reverse))},structural,controls,
  uniqueInputs:[...uniqueInputs.values()],errors
 },null,2));
 if(errors.length)process.exitCode=1;
}

