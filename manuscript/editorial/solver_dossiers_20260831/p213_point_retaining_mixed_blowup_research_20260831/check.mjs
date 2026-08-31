import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const dir=path.dirname(fileURLToPath(import.meta.url));
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
const inputs=[
  ["../p213_mixed_snc_wall_blowup_reduction_20260831/RESEARCH_NOTE.md","9463a10f2918a01a214c458052a50c5604293a6e4192f7c5aa1c91234c7e1120","scoped presentation/predecessor"],
  ["../p213_mixed_snc_wall_blowup_reduction_20260831/SOURCE_LEDGER.md","dbde85d634fd9d9d248f5118202564a134fc4ce5df22b32451aa191bac0f956a","predecessor source interface"],
  ["../p213_mixed_snc_wall_blowup_reduction_20260831/MANIFEST.json","34049f77811973f0e9d074bc7d8d88ae9f5aa4e586b3590d75b388f856f607fb","predecessor freeze provenance"],
  ["../p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md","3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a","conditional optional Section 9 input"],
  ["../p213_nonreduced_tube_finite_projection_research_20260831/SOURCE_LEDGER.md","cdf06f52596133e91abaa2c2e5870bbfb2db0f56ee71dd10dd2311636ccb9898","conditional local source interface"],
  ["../p213_mixed_snc_wall_blowup_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md","3533d2eb0d352c2f80a6e61af5afb0017c274db4ba4c0b7c0474f47cbe9909b6","provenance only; not a new complete audit"]
];
const errors=[];
const record=(rel,role)=>{
  const b=fs.readFileSync(path.resolve(dir,rel));
  return {path:rel,bytes:b.length,sha256:sha(b),role};
};
const inputRecords=inputs.map(([rel,expected,role])=>{
  const r=record(rel,role);
  if(r.sha256!==expected) errors.push("input hash mismatch: "+rel);
  return {...r,expectedSha256:expected,match:r.sha256===expected};
});
const localNames=["RESEARCH_NOTE.md","SOURCE_LEDGER.md","INTERNAL_CHECK_AND_SCOPE.md","check.mjs"];
const localRecords=localNames.map(rel=>record(rel,"authored candidate/check"));
const hygiene=[];
for(const rel of localNames) {
  const b=fs.readFileSync(path.join(dir,rel));
  const bad=[...b].filter(x=>(x<32&&x!==9&&x!==10)||x===127).length;
  if(bad) errors.push("unexpected control bytes: "+rel);
  if(rel.endsWith(".md")&&b.toString().includes(String.fromCharCode(92,96))) errors.push("escaped Markdown backtick: "+rel);
  hygiene.push({path:rel,unexpectedControlBytes:bad,lines:b.toString().split("\n").length-1});
}
const note=fs.readFileSync(path.join(dir,"RESEARCH_NOTE.md"),"utf8");
const tags=[...note.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
if(new Set(tags).size!==tags.length) errors.push("duplicate equation tag");

const abs=a=>a<0n?-a:a;
const gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;};
const R=(a,b=1n)=>{
  a=BigInt(a);b=BigInt(b);
  if(b===0n)throw Error("zero denominator");
  if(b<0n){a=-a;b=-b;}
  const g=gcd(a,b);return [a/g,b/g];
};
const add=(a,b)=>R(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>R(-a[0],a[1]);
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>R(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>R(a[0]*b[1],a[1]*b[0]);
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
const ident=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>R(i===j?1:0)));
const det=M=>{
  const A=M.map(r=>r.map(a=>R(...a)));let d=R(1);
  for(let i=0;i<A.length;i++){
    let p=i;while(p<A.length&&A[p][i][0]===0n)p++;
    if(p===A.length)return R(0);
    if(p!==i){[A[i],A[p]]=[A[p],A[i]];d=neg(d);}
    const pivot=A[i][i];d=mul(d,pivot);
    for(let j=i+1;j<A.length;j++){
      const f=div(A[j][i],pivot);
      for(let k=i;k<A.length;k++)A[j][k]=sub(A[j][k],mul(f,A[i][k]));
    }
  }
  return d;
};
const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((sum,a,k)=>add(sum,mul(a,B[k][j])),R(0))));
const vectorLeft=(v,A)=>A[0].map((_,j)=>v.reduce((sum,a,k)=>add(sum,mul(a,A[k][j])),R(0)));
const sameMatrix=(A,B)=>A.every((r,i)=>r.every((a,j)=>eq(a,B[i][j])));
let cases=0;
for(let n=2;n<=7;n++)for(const N0 of [1,2,5])for(const Np of [0,1,4])for(let h=1;h<n;h++){
  const N=Array.from({length:n},(_,i)=>i===0?N0:i===h?0:(i%3)+1);
  const normalA=ident(n),normalB=ident(n),inverseA=ident(n),inverseB=ident(n);
  normalA[h][0]=R(-1);normalB[0][h]=R(-1);
  inverseA[h][0]=R(1);inverseB[0][h]=R(1);
  for(const M of [normalA,normalB,inverseA,inverseB])if(!eq(det(M),R(1)))errors.push("normal determinant");
  if(!sameMatrix(mm(normalA,inverseA),ident(n))||!sameMatrix(mm(normalB,inverseB),ident(n)))errors.push("normal inverse");
  const NA=vectorLeft(N.map(x=>R(x)),inverseA),NB=vectorLeft(N.map(x=>R(x)),inverseB);
  if(!NA.every((a,i)=>eq(a,R(N[i]))))errors.push("Case A multiplicity");
  if(!NB.every((a,i)=>eq(a,R(i===h?N0:N[i]))))errors.push("Case B multiplicity");
  const retainedA=ident(n);
  for(let i=1;i<n;i++)if(i!==h)retainedA[h-1][i-1]=R(N[i],N0);
  retainedA[h-1][n-1]=R(Np,N0);
  if(!eq(det(retainedA),R(1)))errors.push("retained rational shear determinant");
  const retainedN=[...N.slice(1),Np].map(x=>R(x));
  if(!vectorLeft(retainedN,retainedA).every((a,i)=>eq(a,retainedN[i])))errors.push("Case A retained weighted relation");
  cases++;
}
// Exact inverse normal matrix for pi=rt, z=r^2*t, in final order (t,r).
const example=[[R(1),R(1)],[R(1),R(2)]];
if(!eq(det(example),R(1)))errors.push("example determinant");
const out={
  status:errors.length?"FAILED":"PASSED_AUTHOR_MECHANICAL_CHECKS",
  independentAudit:false,productionVerification:false,
  date:"2026-09-01",
  inputPins:{count:inputRecords.length,mismatches:inputRecords.filter(r=>!r.match).length,records:inputRecords},
  localRecords,
  textHygiene:hygiene,
  equations:{count:tags.length,unique:new Set(tags).size,tags},
  exactAlgebra:{multiplicitySlotCases:cases,dimensions:"2 through 7",N0:[1,2,5],Np:[0,1,4],
    checks:["both normal determinants","both inverse identities","both multiplicity transformations","rational retained shear determinant","Case A weighted affine linear relation","sqrt(2) example exponent determinant"],
    independentWeightsNumericallyTested:false,analyticGeometryTested:false},
  errors,
  scope:"Read-only author byte/hygiene/algebra checks; not a substitute for the written proof or fresh independent audit."
};
process.stdout.write(JSON.stringify(out,null,2)+"\n");
if(errors.length)process.exitCode=1;

