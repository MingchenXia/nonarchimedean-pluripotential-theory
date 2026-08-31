import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {fileURLToPath} from "node:url";

const dir=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>crypto.createHash("sha256").update(b).digest("hex");
const issues=[];
const pins=JSON.parse(fs.readFileSync(path.join(dir,"INPUT_PINS.json"),"utf8"));
for(const item of pins.files){
  const b=fs.readFileSync(item.path);
  if(b.length!==item.bytes||hash(b)!==item.sha256) issues.push("input mismatch: "+item.path);
}
const authored=["RESEARCH_NOTE.md","SOURCE_LEDGER.md","INPUT_PINS.json","check_packet.mjs","VALIDATION.md"];
let controls=0;
for(const name of authored){
  const p=path.join(dir,name);
  if(!fs.existsSync(p)){issues.push("missing authored file: "+name);continue;}
  const b=fs.readFileSync(p);
  for(let i=0;i<b.length;i++){
    if((b[i]<32&&b[i]!==9&&b[i]!==10)||b[i]===127){
      controls++;issues.push("control byte "+b[i]+" in "+name+" at "+i);
    }
  }
  if(b.length===0||b[b.length-1]!==10)issues.push("missing final LF: "+name);
}
const note=fs.readFileSync(path.join(dir,"RESEARCH_NOTE.md"),"utf8");
const markers=[
"PROJECTIVE","g\\circ p_N=g","FULL inverse image",
"BFJ Lemma 3.5(ii)","BFJ Proposition 3.12(ii)",
"not a proof of P21.3","SAME-GENERIC-X",
"EVERY vertex of the common chamber","No arbitrary current is pulled back",
"Every new top chamber contains the retained E"
];
for(const m of markers)if(!note.includes(m))issues.push("missing scope/formula marker: "+m);
const tags=[...note.matchAll(/\\tag\{([^}]+)\}/g)].map(x=>x[1]);
if(new Set(tags).size!==tags.length)issues.push("duplicate equation tags");
let arithmeticCases=0;
for(let n=2;n<=7;n++)for(let ne=1;ne<=5;ne++)for(let de=-3;de<=3;de++)
for(let h=1;h<=4;h++)for(let xp=1;xp<=3;xp++){
  const oldN=[ne,...Array.from({length:n-1},(_,j)=>j+2)];
  const oldD=[de,...Array.from({length:n-1},(_,j)=>2*j-3)];
  const oldV=[h+xp,...Array.from({length:n-1},(_,j)=>j+1)];
  const newN=[ne,ne,...oldN.slice(1)],newD=[de,de,...oldD.slice(1)];
  const newV=[xp,h,...oldV.slice(1)];
  const dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0);
  if(dot(oldN,oldV)!==dot(newN,newV)||dot(oldD,oldV)!==dot(newD,newV))
    issues.push("monomial chart mismatch");
  if(newD[1]*oldN[0]!==oldD[0]*newN[1])issues.push("exceptional value mismatch");
  arithmeticCases++;
}
let manifestEntries=0,sumEntries=0;
const mf=path.join(dir,"MANIFEST.json");
if(fs.existsSync(mf)){
  const m=JSON.parse(fs.readFileSync(mf,"utf8"));
  for(const e of m.files){
    const p=path.resolve(dir,e.path),b=fs.readFileSync(p);
    if(b.length!==e.bytes||hash(b)!==e.sha256)issues.push("manifest mismatch: "+e.path);
    manifestEntries++;
  }
}
const sf=path.join(dir,"SHA256SUMS");
if(fs.existsSync(sf)){
  for(const line of fs.readFileSync(sf,"utf8").trimEnd().split("\n")){
    const m=/^([0-9a-f]{64})  (.+)$/.exec(line);
    if(!m){issues.push("invalid checksum line");continue;}
    if(hash(fs.readFileSync(path.resolve(dir,m[2])))!==m[1])issues.push("checksum mismatch: "+m[2]);
    sumEntries++;
  }
}
console.log(JSON.stringify({
  status:issues.length?"FAIL":"PASS",
  mode:fs.existsSync(mf)?"frozen-manifest-check":"pre-manifest-check",
  inputPins:pins.files.length,authoredFiles:authored.length,controlBytes:controls,
  equationTags:tags.length,arithmeticCases,manifestEntries,sumEntries,issues
},null,2));
process.exitCode=issues.length?1:0;
