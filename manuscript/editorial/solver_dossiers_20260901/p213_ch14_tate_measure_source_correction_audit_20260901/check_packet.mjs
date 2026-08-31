import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {fileURLToPath} from "node:url";
const dir=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>crypto.createHash("sha256").update(b).digest("hex");
const read=n=>fs.readFileSync(path.resolve(dir,n));
const issues=[];
const pins=JSON.parse(read("INPUT_PINS.json"));
for(const p of pins.source_files){
  const b=fs.readFileSync(p.path);
  if(b.length!==p.bytes||hash(b)!==p.sha256)issues.push("source mismatch: "+p.path);
}
const own=["AUDIT.md","proposed_replacement.tex","original_target.tex","INPUT_PINS.json","check_packet.mjs"];
for(const n of ["MANIFEST.json","SHA256SUMS"])if(fs.existsSync(path.join(dir,n)))own.push(n);
let controls=0;
for(const n of own){
  const b=read(n);
  for(let i=0;i<b.length;i++)if((b[i]<32&&b[i]!==9&&b[i]!==10)||b[i]===127){
    controls++;issues.push("control byte in "+n+" at "+i);
  }
  if(!b.length||b.at(-1)!==10)issues.push("missing final LF: "+n);
}
const tex=read("proposed_replacement.tex").toString("utf8");
const old=read("original_target.tex").toString("utf8");
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const eqrefs=s=>[...s.matchAll(/\\eqref\{([^}]+)\}/g)].map(m=>m[1]);
if(JSON.stringify(labels(tex))!==JSON.stringify(labels(old)))issues.push("label mismatch");
if(JSON.stringify(eqrefs(tex))!==JSON.stringify(eqrefs(old)))issues.push("eqref mismatch");
const stack=[];
for(const m of tex.matchAll(/\\(begin|end)\{([^}]+)\}/g)){
  if(m[1]==="begin")stack.push(m[2]);
  else if(stack.pop()!==m[2])issues.push("environment mismatch: "+m[2]);
}
if(stack.length)issues.push("unclosed environment");
let braces=0;
for(let i=0;i<tex.length;i++){
  if(tex[i]==="{"&&tex[i-1]!=="\\")braces++;
  if(tex[i]==="}"&&tex[i-1]!=="\\")braces--;
  if(braces<0)issues.push("early closing brace");
}
if(braces)issues.push("unbalanced braces");
const live=fs.readFileSync(pins.live_context.path);
const liveMatches=live.length===pins.live_context.bytes&&hash(live)===pins.live_context.sha256;
if(liveMatches){
  const s=live.toString("utf8");
  const a=s.indexOf("\\begin{example}[The current of integration over a skeleton]");
  const z=s.indexOf("\\end{example}",a)+"\\end{example}".length;
  if(a<0||s.slice(a,z)+"\n"!==old)issues.push("original snapshot mismatch");
}
const manuscript=path.resolve(path.dirname(pins.live_context.path),"../..");
const refText=["parts/part2/ch11_integration.tex","parts/part2/ch12_tropicalization.tex","parts/part2/ch14_currents.tex"]
  .map(n=>fs.readFileSync(path.join(manuscript,n),"utf8")).join("\n");
const refs=[...tex.matchAll(/\\Cref\{([^}]+)\}/g)].flatMap(m=>m[1].split(","));
for(const r of refs)if(!refText.includes("\\label{"+r+"}"))issues.push("missing label: "+r);
const bib=fs.readFileSync(path.join(manuscript,"bibliography/NonArchimedean.bib"),"utf8");
if(!/@misc\{CLD25,/.test(bib))issues.push("missing CLD25 key");
if(!tex.includes("\\mu_\\Sigma=i_*(\\rd s)"))issues.push("missing explicit measure");
if(tex.includes("\\delta_\\Sigma=\\delta_{E}"))issues.push("old degree-confused equation retained");
let manifestEntries=0,checksumEntries=0;
if(fs.existsSync(path.join(dir,"MANIFEST.json"))){
  for(const e of JSON.parse(read("MANIFEST.json")).files){
    const b=read(e.path);
    if(b.length!==e.bytes||hash(b)!==e.sha256)issues.push("manifest mismatch: "+e.path);
    manifestEntries++;
  }
}
if(fs.existsSync(path.join(dir,"SHA256SUMS"))){
  for(const line of read("SHA256SUMS").toString("utf8").trimEnd().split("\n")){
    const m=/^([0-9a-f]{64})  (.+)$/.exec(line);
    if(!m||hash(read(m[2]))!==m[1])issues.push("checksum mismatch");
    checksumEntries++;
  }
}
console.log(JSON.stringify({status:issues.length?"FAIL":"PASS",sourcePins:pins.source_files.length,
 authoredTextFiles:own.length,controlBytes:controls,labels:labels(tex),equationReferences:eqrefs(tex),
 externalReferences:refs.length,liveMatchesAuditedRevision:liveMatches,manifestEntries,checksumEntries,issues},null,2));
process.exitCode=issues.length?1:0;
