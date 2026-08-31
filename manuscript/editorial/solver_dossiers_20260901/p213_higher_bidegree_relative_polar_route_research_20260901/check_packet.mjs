import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {fileURLToPath} from "node:url";

const base=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>crypto.createHash("sha256").update(b).digest("hex");
const fail=m=>{throw new Error(m);};
const pinDoc=JSON.parse(fs.readFileSync(path.join(base,"INPUT_PINS.json"),"utf8"));
const checkedPins=[];
for (const p of pinDoc.pins) {
  if (!p.verify_at_check) continue;
  const b=fs.readFileSync(p.path);
  if (b.length!==p.bytes || hash(b)!==p.sha256) fail("Input mismatch: "+p.path);
  checkedPins.push(p.path);
}
const owned=["RESEARCH_NOTE.md","SOURCE_LEDGER.md","VALIDATION.md","README.md","INPUT_PINS.json","check_packet.mjs"];
const controls=[];
for(const rel of owned){
  const b=fs.readFileSync(path.join(base,rel));
  for(let i=0;i<b.length;i++) if((b[i]<32&&b[i]!==9&&b[i]!==10)||b[i]===127) controls.push({rel,offset:i,byte:b[i]});
}
if(controls.length) fail(JSON.stringify(controls));
const note=fs.readFileSync(path.join(base,"RESEARCH_NOTE.md"),"utf8");
if(!note.includes("a\\ge4")||!note.includes("2\\mathrm e(a+1)")||!note.includes("UNVERIFIED RESEARCH CANDIDATE")) fail("Scope marker missing");
const tags=[...note.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
if(new Set(tags).size!==tags.length) fail("Repeated displayed tag");
let endpointCases=0;
for(let a=4;a<=64;a++){
  const l=a+1;
  // -dd(r^l)+l^2*r^(l-2)*eta has coefficients (l,l).
  // l*beta has coefficients (l,l*a).
  const thetaCoefficient=l, etaCoefficient=l*l-l*(l-1);
  if(thetaCoefficient>l || etaCoefficient>l*a || etaCoefficient!==l) fail("Endpoint coefficient comparison");
  const M=3.25, B=1/(2*M);
  const val=l/B*Math.exp(2*B*M), expected=2*Math.E*l*M;
  if(Math.abs(val-expected)>1e-10*expected) fail("Exponential constant");
  endpointCases++;
}
const u=[2,2,0,0],v=[1,1,1,1],w=[2,2,1,1];
const sum=a=>a.reduce((s,x)=>s+x,0);
const canonical=[sum(u),sum(v)];
const weighted=u.map((x,i)=>w[i]*(x-v[i])).reduce((s,x)=>s+x,0);
if(canonical[0]!==4||canonical[1]!==4||weighted!==2)fail("Fan arithmetic");
let bidegreeCases=0;
for(let n=2;n<=12;n++)for(let p=1;p<n;p++){
  const d=n-p;
  if(p+d-1!==n-1||p+1>n)fail("Bidegree");
  bidegreeCases++;
}
const mfPath=path.join(base,"MANIFEST.json");
const preliminary=process.argv.includes("--unfrozen");
let manifestEntries=0,checksumEntries=0;
if(!preliminary){
  const mf=JSON.parse(fs.readFileSync(mfPath,"utf8"));
  for(const e of mf.entries){
    const b=fs.readFileSync(path.resolve(base,e.path));
    if(b.length!==e.bytes||hash(b)!==e.sha256)fail("Manifest mismatch: "+e.path);
    manifestEntries++;
  }
  for(const line of fs.readFileSync(path.join(base,"SHA256SUMS"),"utf8").trimEnd().split("\n")){
    const m=line.match(/^([a-f0-9]{64})  (.+)$/);
    if(!m)fail("Malformed checksum line");
    if(hash(fs.readFileSync(path.resolve(base,m[2])))!==m[1])fail("Checksum mismatch: "+m[2]);
    checksumEntries++;
  }
  const expected=[...owned,"INTERNAL_CHECK.json","MANIFEST.json","SHA256SUMS"].sort();
  const actual=fs.readdirSync(base).sort();
  if(JSON.stringify(expected)!==JSON.stringify(actual))fail("Unexpected or missing owned file");
}
console.log(JSON.stringify({
 status:"MECHANICAL CHECK PASS; NOT A MATHEMATICAL VERDICT",
 mode:preliminary?"pre-freeze":"read-only frozen verification",
 frozenInputPins:checkedPins.length,
 historicalMutableContextObservations:pinDoc.pins.filter(x=>!x.verify_at_check).length,
 authoredControlByteViolations:controls.length,
 uniqueDisplayedTags:tags.length,
 integerEndpointCases:endpointCases,
 bidegreeCases,
 fanCanonicalSlopes:canonical,
 fanWeightedDefect:weighted,
 manifestEntries,checksumEntries,
 writesPerformed:0,
 sourceScope:"Full CPsh; arbitrary positive closed base; relative trace-integrability explicit; a>=4",
 exclusions:"No analytic BT counterexample; no all-current regularization; no production or live integration."
},null,2));
