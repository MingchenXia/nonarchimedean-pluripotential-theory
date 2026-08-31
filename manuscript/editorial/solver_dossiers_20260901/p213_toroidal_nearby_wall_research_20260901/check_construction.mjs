// Supplementary exact lattice checks, not a proof of algebraic or analytic geometry.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const gcd=(a,b)=>b?gcd(b,a%b):a;
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n);
const add=(a,b)=>a.map((x,i)=>x+b[i]);
const abs=x=>x<0n?-x:x;
const eq=(a,b)=>a.every((x,i)=>x===b[i]);
function det(cols){
  const d=cols.length,a=Array.from({length:d},(_,i)=>cols.map(c=>c[i]));
  let prev=1n,sign=1n;
  for(let k=0;k<d-1;k++){
    if(a[k][k]===0n){const j=a.findIndex((r,j)=>j>k&&r[k]!==0n);if(j<0)return 0n;[a[k],a[j]]=[a[j],a[k]];sign=-sign;}
    const pivot=a[k][k];
    for(let i=k+1;i<d;i++)for(let j=k+1;j<d;j++){
      const num=a[i][j]*pivot-a[i][k]*a[k][j];
      if(num%prev!==0n)throw Error('Nonexact Bareiss division');
      a[i][j]=num/prev;
    }
    for(let i=k+1;i<d;i++)a[i][k]=0n;
    prev=pivot;
  }
  return sign*a[d-1][d-1];
}
let seed=2130901,maxSteps=0,totalSteps=0,cases=0;
function random(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n;}
for(let d=3;d<=6;d++)for(let trial=0;trial<160;trial++){
  let a=Array.from({length:d},()=>BigInt(1+random(99)));
  const g=a.reduce(gcd);a=a.map(x=>x/g);
  const N=Array.from({length:d},()=>BigInt(random(6)));if(N.every(x=>x===0n))N[0]=1n;
  const M=dot(N,a);
  let cols=Array.from({length:d},(_,j)=>Array.from({length:d},(_,i)=>i===j?1n:0n));
  let coeff=a.slice(),steps=0;
  for(;;){
    const J=coeff.map((v,i)=>v>0n?i:-1).filter(i=>i>=0);
    const rebuilt=Array.from({length:d},(_,r)=>cols.reduce((s,b,i)=>s+coeff[i]*b[r],0n));
    if(!eq(rebuilt,a)||abs(det(cols))!==1n||coeff.some(x=>x<0n))throw Error('Extraction invariant');
    if(J.length===1){if(coeff[J[0]]!==1n||!eq(cols[J[0]],a))throw Error('Primitive termination');break;}
    const j=J.reduce((j,i)=>coeff[i]<coeff[j]?i:j,J[0]),m=coeff[j],oldSum=coeff.reduce((s,x)=>s+x,0n);
    if(!J.some(i=>dot(N,cols[i])>0n))throw Error('Nonvertical center');
    const sum=J.reduce((v,i)=>add(v,cols[i]),Array(d).fill(0n));
    cols[j]=sum;
    for(const i of J)if(i!==j)coeff[i]-=m;
    const newSum=coeff.reduce((s,x)=>s+x,0n);
    if(oldSum-newSum!==BigInt(J.length-1)*m||newSum>=oldSum)throw Error('Nondecrease');
    if(++steps>10000)throw Error('Termination guard');
  }
  const ai=cols.findIndex(b=>eq(b,a));[cols[0],cols[ai]]=[cols[ai],cols[0]];
  // ell=1 suffices for this rational scaling test.
  for(let i=1;i<d;i++){
    const b=cols[i],Mi=dot(N,b),epsilon=1e-4;
    const numeratorNorm=Math.hypot(...b.map((x,j)=>Number(M*x-Mi*a[j])));
    const k=BigInt(Math.max(1,Math.ceil(numeratorNorm/(epsilon*Number(M*M)))+1));
    cols[i]=b.map((x,j)=>x+k*a[j]);
    const mnew=dot(N,cols[i]);
    if(mnew!==Mi+k*M||mnew<=0n||cols[i].some(x=>x<=0n))throw Error('Shear positivity');
    const distance=Math.hypot(...cols[i].map((x,j)=>Number(x)/Number(mnew)-Number(a[j])/Number(M)));
    if(!(distance<epsilon))throw Error('Normalization convergence');
  }
  if(abs(det(cols))!==1n)throw Error('Shear determinant');
  cases++;totalSteps+=steps;maxSteps=Math.max(maxSteps,steps);
}
const notePath=path.join(here,'RESEARCH_NOTE.md'),note=fs.readFileSync(notePath),str=note.toString('utf8');
const tags=[...str.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
if(new Set(tags).size!==tags.length)throw Error('Duplicate equation tag');
const own=['README.md','RESEARCH_NOTE.md','SOURCE_LEDGER.md','check_construction.mjs'];
for(const name of own){const b=fs.readFileSync(path.join(here,name));if([...b].some(c=>(c<32&&c!==9&&c!==10)||c===127))throw Error('Control byte: '+name);}
const report={date:'2026-09-01',kind:'author supplementary finite checks, not independent or production acceptance',readOnly:true,
  note:{path:notePath,bytes:note.length,sha256:sha(note)},cases,dimensions:[3,4,5,6],totalSteps,maxSteps,
  extractionReconstruction:'exact BigInt',primitiveAndUnimodularity:'exact BigInt determinant',verticality:'exact nonnegative multiplicities',
  normalizationDistanceBudget:0.0001,normalizationDistanceCheck:'floating supplementary check; exact formula proved in note',
  equationTags:tags,forbiddenControls:0,mismatches:0};
if(fs.existsSync(path.join(here,'SHA256SUMS'))){
  const manifest=JSON.parse(fs.readFileSync(path.join(here,'MANIFEST.json')));
  for(const e of manifest.entries){const b=fs.readFileSync(e.path);if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Manifest mismatch: '+e.path);}
  const lines=fs.readFileSync(path.join(here,'SHA256SUMS'),'utf8').trim().split('\n');
  for(const line of lines){const m=line.match(/^([a-f0-9]{64})  (.+)$/);if(!m||sha(fs.readFileSync(m[2]))!==m[1])throw Error('Checksum mismatch: '+line);}
  report.freeze={manifestEntries:manifest.entries.length,checksums:lines.length,mismatches:0};
}
console.log(JSON.stringify(report,null,2));
