import {plan,copy} from "./preservation_lib.mjs";
const mode=process.argv[2]??"plan";
if(mode==="plan"){
 const p=plan();
 console.log(JSON.stringify({status:"PASS preflight",dossiers:new Set(p.files.map(f=>f.dossier)).size,
 files:p.files.length,bytes:p.files.reduce((a,f)=>a+f.bytes,0),png:p.files.filter(f=>f.relativePath.endsWith(".png")).length,
 copyNew:p.files.filter(f=>f.action==="copy-new").length,checks:p.checks.counts,
 externalPaths:[...new Set(p.checks.occurrences.filter(e=>e.externalToDossier).map(e=>e.originalAbsolutePath))],
 writesPerformed:0},null,2));
}else if(mode==="copy")console.log(JSON.stringify(copy(),null,2));
else throw Error("Only explicit plan or copy is permitted");
