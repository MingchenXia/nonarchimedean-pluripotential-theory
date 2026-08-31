import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const root="/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901/p213_proper_target_open_comparison_20260901";
const visual="/private/tmp/p213_target_open_source_visual.tojdvY";
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
const rec=(file,role)=>{const b=fs.readFileSync(file);return{path:file,bytes:b.length,sha256:sha(b),role};};
const pins=[
 ["RESEARCH_NOTE.md","35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec"],
 ["MANIFEST.json","ced5e08f745aee9ae83f09e8cf7063099a9532208776ee0e114ac79915cfeefa"],
 ["SHA256SUMS","4abb30a6de188717e8c5efad60c8da17fdccdf421c3244fcbe80bd5a85856b8e"]
];
const errors=[];
const pinResults=pins.map(([name,expected])=>{const r=rec(path.join(root,name),"announced candidate pin");const match=r.sha256===expected;if(!match)errors.push("announced pin "+name);return{...r,expected,match};});
const manifest=JSON.parse(fs.readFileSync(path.join(root,"MANIFEST.json")));
const inputRecords=manifest.entries.map(e=>{
 const r=rec(e.path,"candidate manifest: "+e.role);
 if(r.sha256!==e.sha256||r.bytes!==e.bytes)errors.push("candidate manifest "+e.path);
 return r;
});
for(const name of ["MANIFEST.json","SHA256SUMS"])inputRecords.push(rec(path.join(root,name),"candidate freeze record"));
const sums=fs.readFileSync(path.join(root,"SHA256SUMS"),"utf8").trim().split("\n");
for(const line of sums){
 const m=line.match(/^([a-f0-9]{64})  (.+)$/);
 if(!m||sha(fs.readFileSync(m[2]))!==m[1])errors.push("candidate checksum "+line);
}
const pdf=rec("/private/tmp/CLD25.pdf","primary source PDF visually checked");
if(pdf.sha256!=="5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719")errors.push("primary PDF hash");
inputRecords.push(pdf);
for(const p of [332,357,359,396,399,424])inputRecords.push(rec(path.join(visual,p+".png"),"visual source QA printed page "+p));
const note=fs.readFileSync(path.join(root,"RESEARCH_NOTE.md"),"utf8");
const tags=[...note.matchAll(/\\tag\{([^}]+)\}/g)].map(m=>m[1]);
if(tags.length!==new Set(tags).size)errors.push("duplicate equation tag");
const hygiene=["RESEARCH_NOTE.md","SOURCE_LEDGER.md","freeze.mjs"].map(name=>{
 const b=fs.readFileSync(path.join(root,name));const controls=[...b].filter(x=>(x<32&&x!==9&&x!==10)||x===127).length;
 if(controls)errors.push("control bytes "+name);
 return{name,bytes:b.length,unexpectedControls:controls};
});
process.stdout.write(JSON.stringify({
 date:"2026-09-01",reviewer:"/root/p213_skeletal_hostile",readOnly:true,
 candidatePins:pinResults,candidateManifestEntries:manifest.entries.length,candidateChecksumEntries:sums.length,
 equations:{count:tags.length,unique:new Set(tags).size},hygiene,
 sourcePagesVisuallyInspected:[332,357,359,396,399,424],inputRecords,
 errors,status:errors.length?"FAILED":"EXACT_INPUTS_MATCH",
 scope:"Byte and hygiene verification only, separate from the written independent mathematical audit."
},null,2)+"\n");
if(errors.length)process.exitCode=1;
