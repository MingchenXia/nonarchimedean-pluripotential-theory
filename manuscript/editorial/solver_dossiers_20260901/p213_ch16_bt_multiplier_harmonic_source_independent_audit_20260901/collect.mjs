import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

// Read-only book/source inspection. All generated evidence stays in this NEW dossier.
const out=path.dirname(fileURLToPath(import.meta.url));
const root='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const ms=path.join(root,'manuscript');
const base='10897afc0b7379ee169f46ecb77184ac7580f177';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const write=(name,s)=>fs.writeFileSync(path.join(out,name),s,{flag:'wx'});
const json=(name,o)=>write(name,JSON.stringify(o,null,2)+'\n');
const git=(...a)=>execFileSync('git',a,{cwd:root,maxBuffer:20*1024*1024});
const targets={
 'manuscript/parts/part2/ch16_bedford_taylor.tex':'41333978fbce28644d1f63aac6431f763dd3f3cc1dd792faf1b20b43ab3a9e83',
 'manuscript/parts/part2/ch19_cld_examples.tex':'4d59d219eec46bea029d6d131e6f55c110a7fbf4c3f30be9dcf4147a4c5a6652'
};
const others=[
 'manuscript/parts/part2/ch15_poincare_lelong.tex',
 'manuscript/parts/part2/ch17_metrized_bundles.tex',
 'manuscript/parts/part2/ch18_delta_forms.tex','manuscript/book.tex',
 '/private/tmp/CLD25.txt',
 '/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_common_constant_cohomology_source_diagnosis_20260901/SOURCE_DIAGNOSIS.md',
 '/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_common_constant_cohomology_source_diagnosis_20260901/SOURCE_LEDGER.md'
];
const inputs=[];
const record=(name,b,extra={})=>inputs.push({path:name,bytes:b.length,sha256:sha(b),...extra});
const preservation=[];
const extract=(s,a,b)=>s.split('\n').slice(a-1,b).map((v,i)=>`${a+i}: ${v}`).join('\n')+'\n';
let excerpts='# Exact source excerpts (line-numbered; not replacement text)\n\n';
for(const [rel,expected] of Object.entries(targets)){
 const abs=path.join(root,rel), now=fs.readFileSync(abs), old=git('show',`${base}:${rel}`);
 if(sha(now)!==expected)throw new Error(`Unexpected reviewed input: ${rel}`);
 record(abs,now,{role:'exact reviewed after-patch input'});
 record(`git:${base}:${rel}`,old,{role:'exact pre-patch input'});
 const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
 const a=labels(old.toString()),b=labels(now.toString());
 preservation.push({path:rel,oldLabelCount:a.length,newLabelCount:b.length,
  removed:a.filter(x=>!b.includes(x)),added:b.filter(x=>!a.includes(x))});
 const spans=rel.includes('ch16')?[[1540,1633],[2358,2400],[3725,3868]]:[[2596,2662]];
 excerpts+=`## BEFORE: ${rel}\nCommit ${base}; SHA256 ${sha(old)}\n\n`;
 for(const [lo,hi] of spans)excerpts+='```tex\n'+extract(old.toString(),lo,hi)+'```\n\n';
 const afterspans=rel.includes('ch16')?[[1612,1639],[2365,2407],[3844,3882]]:[[2596,2696]];
 excerpts+=`## AFTER: ${rel}\nSHA256 ${sha(now)}\n\n`;
 for(const [lo,hi] of afterspans)excerpts+='```tex\n'+extract(now.toString(),lo,hi)+'```\n\n';
 if(rel.includes('ch19')){
  const statement=s=>{const l=s.indexOf('\\label{thm:ch19-canonical-positivity}');
   const lo=s.lastIndexOf('\\begin{theorem}',l),hi=s.indexOf('\\end{theorem}',l)+13;
   return s.slice(lo,hi);};
  preservation.at(-1).canonicalPositivityStatementUnchanged=statement(old.toString())===statement(now.toString());
 }
}
for(const p of others){const abs=path.isAbsolute(p)?p:path.join(root,p);record(abs,fs.readFileSync(abs),{role:'read-only source/input'});}
const labels=[
 'cor:ch16-bt-times-function','cor:ch16-harmonic-convex-positive',
 'prop:ch16-harmonic-continuity','thm:bt-harmonic-compatibility',
 'lem:ch16-normal-slope-vanishes','sec:ch16-harmonic-charts',
 'sec:ch16-harmonic-continuity','thm:ch19-canonical-positivity',
 'thm:ch19-canonical-ma'];
const visited=new Map(),edges=[],unresolved=[],dynamic=[];
const uncomment=line=>line.replace(/(?<!\\)%.*/, '');
function walk(abs){
 if(visited.has(abs))return;
 if(!fs.existsSync(abs)){unresolved.push(abs);return;}
 const b=fs.readFileSync(abs),s=b.toString();visited.set(abs,{bytes:b.length,sha256:sha(b),text:s});
 const clean=s.split('\n').map(uncomment).join('\n');
 for(const m of clean.matchAll(/\\(input|include|draftinclude)\s*\{([^{}]+)\}/g)){
  if(m[2].includes('#')||m[2].includes('\\')){dynamic.push({source:abs,argument:m[2]});continue;}
  const p=m[2].endsWith('.tex')?m[2]:m[2]+'.tex';
  const dest=path.resolve(ms,p);edges.push({source:abs,target:dest});walk(dest);
 }
}
walk(path.join(ms,'book.tex'));
const refs=[];
for(const [p,o] of visited){o.text.split('\n').forEach((line,i)=>{
 const clean=uncomment(line);
 for(const label of labels)if(clean.includes(label))refs.push({path:p,line:i+1,label,
  kind:clean.includes(`\\label{${label}}`)?'definition':'reference',text:line});
});}
const preRefs=[];
for(const [p,o] of visited){
 let s=o.text;
 const rel=path.relative(root,p);
 if(targets[rel])s=git('show',`${base}:${rel}`).toString();
 s.split('\n').forEach((line,i)=>{
  const clean=uncomment(line);for(const label of labels)if(clean.includes(label))preRefs.push({path:p,line:i+1,label,
   kind:clean.includes(`\\label{${label}}`)?'definition':'reference',text:line});
 });
}
const count=list=>Object.fromEntries(labels.map(label=>[label,{definitions:list.filter(x=>x.label===label&&x.kind==='definition').length,
 references:list.filter(x=>x.label===label&&x.kind==='reference').length}]));
json('INPUT_HASHES.json',{baseCommit:base,inputs});
json('ACTIVE_REFERENCE_INVENTORY.json',{method:'Literal uncommented input/include/draftinclude closure from manuscript/book.tex; dynamic macro definition excluded, no TeX execution.',
 files:[...visited].map(([p,o])=>({path:p,bytes:o.bytes,sha256:o.sha256})),edges,unresolved,dynamic,
 beforeCounts:count(preRefs),afterCounts:count(refs),before:preRefs,after:refs});
write('EXACT_CHANGED_PASSAGES.md',excerpts);
write('REVIEWED.diff',git('diff',base,'--',...Object.keys(targets)));
json('CHECKS.json',{baseCommit:base,exactAfterPinsMatch:true,bookFilesWrittenByAuditor:false,
 productionCalls:false,gitMutations:false,compileOrPdfClaim:false,labelPreservation:preservation,
 activeTexFiles:visited.size,unresolvedLiteralIncludes:unresolved.length,dynamicIncludesIgnored:dynamic,
 definitionMultiplicity:count(refs),note:'Reference/label checks are not a mathematical proof audit. Read the authored report and addendum.'});
console.log(JSON.stringify({out,inputs:inputs.length,activeTexFiles:visited.size,
 unresolvedLiteralIncludes:unresolved.length,beforeCounts:count(preRefs),afterCounts:count(refs),preservation},null,2));
