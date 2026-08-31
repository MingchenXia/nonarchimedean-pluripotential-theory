import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const source="/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p143_kahler_truncation_research_20260831";
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
const record=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:sha(b)}};
const expected={
 "statement.tex":"befc29fb89ff79fe90172d03b1fe088e5f19ebf2ca28aedbd4c83cd05f008100",
 "proof.tex":"1ef28983e1ac242f9a23080e24ced0c21531899f56ab29a96312f4ce79757652",
 "MANIFEST.json":"f5e70b72c09601f27d2210391d8f72935bc37564481be9a5818c19f8926c0b8b"
};
const core=Object.entries(expected).map(([name,hash])=>{
 const item=record(path.join(source,name));if(item.sha256!==hash)throw Error("Core hash mismatch: "+name);return item;
});
const manifest=JSON.parse(fs.readFileSync(path.join(source,"MANIFEST.json"),"utf8"));
const entries=manifest.files.map(e=>{
 if(path.dirname(e.path)!==source)throw Error("Unexpected manifest path");
 const item=record(e.path);if(item.bytes!==e.bytes||item.sha256!==e.sha256)throw Error("Manifest mismatch: "+e.path);return item;
});
const parents=JSON.parse(fs.readFileSync(path.join(source,"INPUTS.json"),"utf8")).map(e=>{
 const item=record(e.path);if(item.bytes!==e.bytes||item.sha256!==e.sha256)throw Error("Parent mismatch: "+e.path);return item;
});
const text=["statement.tex","proof.tex"].map(n=>fs.readFileSync(path.join(source,n),"utf8")).join("\n");
const labels=[...text.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const refs=[...text.matchAll(/\\(?:[Cc]ref|eqref|ref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(","));
const duplicateLabels=labels.filter((x,i)=>labels.indexOf(x)!==i);
const missingReferences=refs.filter(x=>!labels.includes(x));
if(duplicateLabels.length||missingReferences.length)throw Error("Reference failure");
const log=fs.readFileSync(path.join(source,"main.log"),"utf8");
const badLogLines=log.split("\n").filter(x=>/^!|Undefined control|(?:LaTeX|Package .*?) Warning:|Overfull \\[hv]box/.test(x));
const underfullLogLines=log.split("\n").filter(x=>/Underfull \\[hv]box/.test(x));
if(badLogLines.length)throw Error("Draft log diagnostics");
const build=JSON.parse(fs.readFileSync(path.join(source,"BUILD.json"),"utf8"));
if(build.pdfProduced||fs.existsSync(path.join(build.scratch,"main.pdf")))throw Error("Unexpected PDF");
const primaryLocal=["/private/tmp/mp24.txt","/private/tmp/dxz23.txt"].map(record);
console.log(JSON.stringify({
 date:"2026-08-31",type:"read-only-exact-byte-check-not-a-production-review",
 sourceDirectory:source,core,manifestEntriesChecked:entries.length,parentInputsChecked:parents.length,
 manifestMismatches:[],parentMismatches:[],uniqueLabels:labels.length,referenceUses:refs.length,
 duplicateLabels,missingReferences,badLogLines,underfullLogLines,pdfProduced:false,
 authorBuildReexecuted:false,primaryLocal,
 primaryWeb:[{url:"https://arxiv.org/html/2312.17150v3",accessed:"2026-08-31",
 note:"Version-pinned primary HTML passages read through web tool; not represented as a locally hashed source file."}],
 entries,parents
},null,2));
