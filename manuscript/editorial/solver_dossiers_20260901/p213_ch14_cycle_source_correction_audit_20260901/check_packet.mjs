import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {fileURLToPath} from "node:url";
const dir=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>crypto.createHash("sha256").update(b).digest("hex");
const issues=[];
const p=JSON.parse(fs.readFileSync(path.join(dir,"INPUT_PINS.json"),"utf8"));
for(const e of p.source_files){
  const b=fs.readFileSync(e.path);
  if(b.length!==e.bytes||hash(b)!==e.sha256)issues.push("source mismatch: "+e.path);
}
const own=["AUDIT.md","proposed_replacement.tex","original_target.tex","original_star_context.tex","INPUT_PINS.json","check_packet.mjs"];
let controls=0;
for(const n of own){
  const b=fs.readFileSync(path.join(dir,n));
  for(let i=0;i<b.length;i++)if((b[i]<32&&b[i]!==9&&b[i]!==10)||b[i]===127){
    controls++;issues.push("control "+b[i]+" in "+n+" at "+i);
  }
  if(!b.length||b[b.length-1]!==10)issues.push("missing final LF: "+n);
}
const old=fs.readFileSync(path.join(dir,"original_target.tex"),"utf8");
const tex=fs.readFileSync(path.join(dir,"proposed_replacement.tex"),"utf8");
const theorem=s=>s.match(/\\begin\{theorem\}[\s\S]*?\\end\{theorem\}/)?.[0];
if(!theorem(old)||theorem(old)!==theorem(tex))issues.push("theorem statement changed");
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(x=>x[1]);
if(JSON.stringify(labels(old))!==JSON.stringify(labels(tex)))issues.push("target label mismatch");
const eqrefs=s=>[...s.matchAll(/\\eqref\{([^}]+)\}/g)].map(x=>x[1]);
if(JSON.stringify(eqrefs(old))!==JSON.stringify(eqrefs(tex)))issues.push("original equation references changed");
const stack=[];
for(const m of tex.matchAll(/\\(begin|end)\{([^}]+)\}/g)){
  if(m[1]==="begin")stack.push(m[2]);
  else if(stack.pop()!==m[2])issues.push("environment imbalance: "+m[2]);
}
if(stack.length)issues.push("unclosed environments");
let braces=0;
for(let i=0;i<tex.length;i++){
  if(tex[i]==="{"&&tex[i-1]!=="\\")braces++;
  if(tex[i]==="}"&&tex[i-1]!=="\\")braces--;
  if(braces<0)issues.push("early closing brace");
}
if(braces!==0)issues.push("brace imbalance");
const live=fs.readFileSync(p.live_context.path);
const liveMatches=live.length===p.live_context.bytes&&hash(live)===p.live_context.sha256;
if(liveMatches){
  const s=live.toString("utf8");
  const a=s.indexOf("\\begin{example}[Cycle currents on the Berkovich line]");
  const b=s.indexOf("\\label{thm:current-fundamental-cycle}",a);
  const z=s.indexOf("\\end{proof}",b)+"\\end{proof}".length;
  if(s.slice(a,z)+"\n"!==old)issues.push("snapshot not exact current excerpt");
}
const manuscript=path.resolve(path.dirname(p.live_context.path),"../..");
const ch14=live.toString("utf8");
const ch15=fs.readFileSync(path.join(manuscript,"parts/part2/ch15_poincare_lelong.tex"),"utf8");
const appJ=fs.readFileSync(path.join(manuscript,"appendices/appJ_normalizations.tex"),"utf8");
for(const r of eqrefs(tex))if(!appJ.includes("\\label{"+r+"}"))issues.push("missing equation label: "+r);
const bib=fs.readFileSync(path.join(manuscript,"bibliography/NonArchimedean.bib"),"utf8");
const refs=[...tex.matchAll(/\\Cref\{([^}]+)\}/g)].flatMap(m=>m[1].split(","));
for(const r of refs)if(!(ch14+ch15).includes("\\label{"+r+"}"))issues.push("missing external label: "+r);
if(!/@misc\{CLD25,/.test(bib))issues.push("missing CLD25 bib key");
let entries=0,sums=0;
const mf=path.join(dir,"MANIFEST.json");
if(fs.existsSync(mf))for(const e of JSON.parse(fs.readFileSync(mf,"utf8")).files){
  const b=fs.readFileSync(path.resolve(dir,e.path));
  if(b.length!==e.bytes||hash(b)!==e.sha256)issues.push("manifest mismatch: "+e.path);
  entries++;
}
const sf=path.join(dir,"SHA256SUMS");
if(fs.existsSync(sf))for(const line of fs.readFileSync(sf,"utf8").trimEnd().split("\n")){
  const m=/^([0-9a-f]{64})  (.+)$/.exec(line);
  if(!m||hash(fs.readFileSync(path.resolve(dir,m[2])))!==m[1])issues.push("checksum mismatch");
  sums++;
}
console.log(JSON.stringify({status:issues.length?"FAIL":"PASS",primaryPins:p.source_files.length,
 authoredFiles:own.length,controlBytes:controls,theoremStatementUnchanged:theorem(old)===theorem(tex),
 labels:labels(tex),equationReferencesPreserved:eqrefs(tex),externalReferences:refs.length,liveMatchesAuditedRevision:liveMatches,
 manifestEntries:entries,checksumEntries:sums,issues},null,2));
process.exitCode=issues.length?1:0;
