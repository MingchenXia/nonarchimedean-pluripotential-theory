import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {execFileSync} from "node:child_process";
import {fileURLToPath} from "node:url";
const dir=path.dirname(fileURLToPath(import.meta.url));
const repo="/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory";
const rel="manuscript/parts/part2/ch14_currents.tex";
const baseCommit="db8918d5a533c5a29336d97f70b500540dd9484f";
const cycleDir="../p213_ch14_cycle_source_correction_audit_20260901";
const tateDir="../p213_ch14_tate_measure_source_correction_audit_20260901";
const h=b=>crypto.createHash("sha256").update(b).digest("hex");
const read=p=>fs.readFileSync(path.resolve(dir,p));
const issues=[];
const parents=[
 [cycleDir+"/proposed_replacement.tex","c8219e4f6951634b12cf9b335a3679ec28535e60a735ddcda62daa2d265cbdfa"],
 [cycleDir+"/AUDIT.md","eccc58efa7c9b98c769359d831aa81213f6ba62a3afa973a6df499cf1fb34b37"],
 [cycleDir+"/MANIFEST.json","dc659be99d91da79d35ba626400ea670751ac0438c41321c07fc3c96452dee9e"],
 [cycleDir+"/SHA256SUMS","1b3f218b5ca3b316e49715b2f697a08ce1727a7e88a2e0be0d3a20843de471d0"],
 [tateDir+"/proposed_replacement.tex","22d15d8f39bf0b59a7d704153e5aa7180b522f59affce37afdbe643bad50c95b"],
 [tateDir+"/AUDIT.md","1f02aec1b759f8299fe5e71b3714b5bf0d0607188740aa58382ee7fc6274aa94"],
 [tateDir+"/MANIFEST.json","e315a12cee274c9aa1c4421f46fcaf59d8b336091dab23fbef63b543df101f3a"],
 [tateDir+"/SHA256SUMS","92852345eb78a3c86ca99b88a24b60247bb820d55591b8b3baa615f7929b189d"]
];
for(const [p,sha]of parents)if(h(read(p))!==sha)issues.push("parent pin mismatch: "+p);
let parentManifestEntries=0,parentChecksumEntries=0;
for(const p of [cycleDir,tateDir]){
 for(const e of JSON.parse(read(p+"/MANIFEST.json")).files){
  const b=fs.readFileSync(path.resolve(dir,p,e.path));
  if(b.length!==e.bytes||h(b)!==e.sha256)issues.push("parent manifest mismatch: "+e.path);
  parentManifestEntries++;
 }
 for(const line of read(p+"/SHA256SUMS").toString().trimEnd().split("\n")){
  const m=/^([0-9a-f]{64})  (.+)$/.exec(line);
  if(!m||h(fs.readFileSync(path.resolve(dir,p,m[2])))!==m[1])issues.push("parent checksum mismatch");
  parentChecksumEntries++;
 }
}
const baseBuffer=execFileSync("git",["show",baseCommit+":"+rel],{cwd:repo,maxBuffer:2**22});
const base=baseBuffer.toString("utf8");
const liveBuffer=fs.readFileSync(path.join(repo,rel));
const live=liveBuffer.toString("utf8");
const stripHeader=s=>s.slice(s.indexOf("\\begin{example}")).trimEnd();
const cycleOld=read(cycleDir+"/original_target.tex").toString().trimEnd();
const tateOld=read(tateDir+"/original_target.tex").toString().trimEnd();
const cycleNew=stripHeader(read(cycleDir+"/proposed_replacement.tex").toString());
const tateNew=stripHeader(read(tateDir+"/proposed_replacement.tex").toString());
let expected=base;
const edits=[];
function once(name,a,b){
 const count=expected.split(a).length-1;
 if(count!==1)issues.push(name+" count "+count);
 else {expected=expected.replace(a,b);edits.push(name);}
}
once("Tate example complete replacement",tateOld,tateNew);
once("Line-cycle example and fundamental-cycle theorem/proof complete replacement",cycleOld,cycleNew);
once("Automatic-continuity summary notation",
 "&construction of $\\delta_Y$, $\\delta_\\Sigma$, $u_\\omega$",
 "&construction of $\\delta_Y$, $[\\mu_\\Sigma]$, $u_\\omega$");
once("Tate mass table noun",
 "Tate curve skeleton\n  &mass equals $v_K(q)$",
 "Tate skeleton length measure\n  &mass equals $v_K(q)$");
const preLayoutHash=h(Buffer.from(expected));
once("Double-thickening dense-flat-locus example",
 read("dense_flat_original.tex").toString().trimEnd(),
 read("dense_flat_replacement.tex").toString().trimEnd());
once("Unnumbered display-only chi layout",
 "$\\chi\\in C_c^\\infty((-\\log R,-\\log r))$.",
 "\\[\n                     \\chi\\in C_c^\\infty((-\\log R,-\\log r)).\n\\]");
if(expected!==live)issues.push("full chapter differs from precisely authorized reconstruction");
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const eqrefs=s=>[...s.matchAll(/\\eqref\{([^}]+)\}/g)].map(m=>m[1]);
if(JSON.stringify(labels(base))!==JSON.stringify(labels(live)))issues.push("full ordered labels differ");
if(JSON.stringify(eqrefs(base))!==JSON.stringify(eqrefs(live)))issues.push("full ordered eqrefs differ");
const thm=s=>s.match(/\\begin\{theorem\}\s*\\label\{thm:current-fundamental-cycle\}[\s\S]*?\\end\{theorem\}/)?.[0];
if(!thm(base)||thm(base)!==thm(live))issues.push("fundamental-cycle statement changed");
const refText=["parts/part2/ch11_integration.tex","parts/part2/ch12_tropicalization.tex",
 "parts/part2/ch14_currents.tex","parts/part2/ch15_poincare_lelong.tex","appendices/appJ_normalizations.tex"]
 .map(p=>fs.readFileSync(path.join(repo,"manuscript",p),"utf8")).join("\n");
const newRefs=[...new Set([...((cycleNew+"\n"+tateNew).matchAll(/\\(?:Cref|cref|eqref)\{([^}]+)\}/g))].flatMap(m=>m[1].split(",")))];
for(const r of newRefs)if(!refText.includes("\\label{"+r+"}"))issues.push("missing referenced label: "+r);
const stale=["\\delta_\\Sigma","\\delta_{\\Sigma}","Tate curve skeleton\n  &mass equals"];
for(const s of stale)if(live.includes(s))issues.push("stale Tate notation: "+s);
const own=fs.readdirSync(dir).filter(n=>/\.(md|mjs|json|tex)$/.test(n)||n==="SHA256SUMS");
let controlBytes=0;
for(const [n,b]of [["live chapter",liveBuffer],...own.map(n=>[n,read(n)])]){
 for(let i=0;i<b.length;i++)if((b[i]<32&&b[i]!==9&&b[i]!==10)||b[i]===127){
  controlBytes++;issues.push("control byte in "+n+" at "+i);
 }
}
let manifestEntries=0,checksumEntries=0;
if(fs.existsSync(path.join(dir,"MANIFEST.json")))for(const e of JSON.parse(read("MANIFEST.json")).files){
 const b=read(e.path);
 if(b.length!==e.bytes||h(b)!==e.sha256)issues.push("manifest mismatch: "+e.path);
 manifestEntries++;
}
if(fs.existsSync(path.join(dir,"SHA256SUMS")))for(const line of read("SHA256SUMS").toString().trimEnd().split("\n")){
 const m=/^([0-9a-f]{64})  (.+)$/.exec(line);
 if(!m||h(read(m[2]))!==m[1])issues.push("checksum mismatch");
 checksumEntries++;
}
const result={status:issues.length?"FAIL":"PASS",baseCommit,baseChapterBytes:baseBuffer.length,baseChapterSha256:h(baseBuffer),
 liveChapterBytes:liveBuffer.length,liveChapterSha256:h(liveBuffer),preLayoutHash,expectedSha256:h(Buffer.from(expected)),
 fullExactReconstruction:expected===live,edits,logicalContentChanges:6,layoutOnlyChanges:1,
 fullOrderedLabelCount:labels(live).length,fullOrderedEqrefCount:eqrefs(live).length,
 allLabelsUnchanged:JSON.stringify(labels(base))===JSON.stringify(labels(live)),
 allEqrefsUnchanged:JSON.stringify(eqrefs(base))===JSON.stringify(eqrefs(live)),
 fundamentalStatementUnchanged:thm(base)===thm(live),newReferencedLabels:newRefs,
 parentPins:parents.length,parentManifestEntries,parentChecksumEntries,
 controlBytes,manifestEntries,checksumEntries,issues,
 ...(process.argv.includes("--lists")?{allLabels:labels(live),allEqrefs:eqrefs(live)}:{})};
console.log(JSON.stringify(result,null,2));
process.exitCode=issues.length?1:0;
