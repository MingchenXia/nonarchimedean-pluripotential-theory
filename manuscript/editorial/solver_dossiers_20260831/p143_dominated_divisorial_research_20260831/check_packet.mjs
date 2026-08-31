import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {fileURLToPath} from "node:url";
const dir=path.dirname(fileURLToPath(import.meta.url));
const root="/private/tmp/nappt_p071_20260827";
const base=path.join(root,"manuscript/editorial/solver_dossiers_20260831");
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
const pinned=[
 ["/private/tmp/mp24.txt","0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62"],
 ["/private/tmp/dxz23.txt","7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244"],
 [path.join(root,"manuscript/parts/part6/ch71_pseudoeffective_mp_dxz.tex"),"c6bc0fb2d6813ed2ca4c6c37df4a7b75ef733a0cae62d97400df78fe087327e2"],
 [path.join(root,"manuscript/parts/part6/ch72_major_open_problems.tex"),"6e671da09d50cc7becd553d319a0cbce0fe6c3622ac77a491550411a32c69b8c"],
 [path.join(base,"p142_raw_transform_usc_research_20260831/statement.tex"),"488868dc2b2d1d62b23864970f8bf36acc0a6c7c85d27eaf66e6a9ed7120c949"],
 [path.join(base,"p142_raw_transform_usc_research_20260831/proof.tex"),"bf991c724e138626fbd8fcd4fc6f613d7979f3bf75a3614c569a1ff3c7d21e21"],
 [path.join(base,"p142_raw_transform_usc_research_20260831/MANIFEST.json"),"c677e7a289d9b957d2269cb7b68da4dfcfa89faa4a761a15e8fd8b6dc65e5a87"]
];
const inputs=pinned.map(([name,expected])=>{
 const b=fs.readFileSync(name),actual=sha(b);
 if(actual!==expected)throw new Error("Input changed: "+name);
 return {path:name,bytes:b.length,sha256:actual};
});
if(process.argv[2]==="--inputs"){
 console.log(JSON.stringify({date:"2026-08-31",inputs},null,2));
 process.exit(0);
}
const names=["statement.tex","proof.tex","diagnostics.tex"];
const tex=names.map(n=>fs.readFileSync(path.join(dir,n),"utf8")).join("\n");
const labels=[...tex.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const refs=[...tex.matchAll(/\\(?:[Cc]ref|eqref|ref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(","));
const duplicateLabels=labels.filter((x,i)=>labels.indexOf(x)!==i);
const unresolvedReferences=refs.filter(x=>!labels.includes(x));
if(duplicateLabels.length||unresolvedReferences.length)throw new Error("Label/reference failure");
if(process.argv[2]==="--manifest"){
 const files=fs.readdirSync(dir).filter(n=>n!=="MANIFEST.json").sort().map(n=>{
  const b=fs.readFileSync(path.join(dir,n));return {path:n,bytes:b.length,sha256:sha(b)};
 });
 console.log(JSON.stringify({date:"2026-08-31",status:"frozen-author-candidate-independent-and-production-review-required",files},null,2));
 process.exit(0);
}
const draft=process.argv[2];
if(!draft)throw new Error("Supply existing draft-mode output directory");
const log=fs.readFileSync(path.join(draft,"main.log"),"utf8");
const badLogLines=log.split("\n").filter(x=>/Warning|Error|Overfull|Underfull|undefined|multiply defined/.test(x));
if(badLogLines.length)throw new Error(badLogLines.join("\n"));
const pdfExists=fs.existsSync(path.join(draft,"main.pdf"));
if(pdfExists)throw new Error("Unexpected PDF: only draft compilation intended");
console.log(JSON.stringify({
 date:"2026-08-31",type:"mechanical-check-not-mathematical-audit",
 inputHashesPreserved:inputs.length,uniqueLabels:labels.length,
 internalReferenceUses:refs.length,duplicateLabels,unresolvedReferences,badLogLines,
 draftDirectory:draft,pdfProduced:false,
 compiledLog:{bytes:fs.statSync(path.join(draft,"main.log")).size,sha256:sha(fs.readFileSync(path.join(draft,"main.log")))}
},null,2));

