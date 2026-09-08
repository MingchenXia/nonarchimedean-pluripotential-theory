import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";

const dir=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(dir,"../../../..");
const sha256=buffer=>crypto.createHash("sha256").update(buffer).digest("hex");
const readBound=(relative,expected)=>{
  const absolute=path.join(root,relative);
  const bytes=fs.readFileSync(absolute);
  const actual=sha256(bytes);
  if(actual!==expected) throw new Error(`hash mismatch for ${relative}: ${actual}`);
  return {path:relative,bytes:bytes.length,sha256:actual};
};

const candidate="manuscript/editorial/solver_dossiers_20260831/p143_dominated_divisorial_research_20260831";
const p142="manuscript/editorial/solver_dossiers_20260831/p142_raw_transform_usc_research_20260831";
const augmentation="manuscript/editorial/solver_dossiers_20260901/p142_source_closed_production_release_repaired_authored_stage_dossier_v2_20260901/source_augmentation";
const inputs=[
  readBound(`${candidate}/statement.tex`,`4ab292c9cfcc6c298968fca40819c09d560c12c96279947ddae46f4c22c5191f`),
  readBound(`${candidate}/proof.tex`,`bfd983aa2fa4580a9193bdd3f4fca78e7dd527d6ee1843f5ee647e4485180433`),
  readBound(`${candidate}/diagnostics.tex`,`773cd82034b3089abc0cb70112fab30249a55a5d5baf69f6a8680b4c192808d4`),
  readBound(`${p142}/statement.tex`,`488868dc2b2d1d62b23864970f8bf36acc0a6c7c85d27eaf66e6a9ed7120c949`),
  readBound(`${p142}/proof.tex`,`bf991c724e138626fbd8fcd4fc6f613d7979f3bf75a3614c569a1ff3c7d21e21`),
  readBound(`${p142}/MANIFEST.json`,`c677e7a289d9b957d2269cb7b68da4dfcfa89faa4a761a15e8fd8b6dc65e5a87`),
  readBound(`${augmentation}/mp_2409.06221v2.txt`,`0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62`),
  readBound(`${augmentation}/dxz_2302.02541v3.txt`,`7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244`)
];

const tex=["statement.tex","proof.tex","diagnostics.tex"]
  .map(name=>fs.readFileSync(path.join(root,candidate,name),"utf8"))
  .join("\n");
const labels=[...tex.matchAll(/\\label\{([^}]+)\}/g)].map(match=>match[1]);
const references=[...tex.matchAll(/\\(?:[Cc]ref|eqref|ref)\{([^}]+)\}/g)]
  .flatMap(match=>match[1].split(","));
const duplicateLabels=labels.filter((label,index)=>labels.indexOf(label)!==index);
const unresolvedReferences=references.filter(reference=>!labels.includes(reference));
if(duplicateLabels.length || unresolvedReferences.length) {
  throw new Error(JSON.stringify({duplicateLabels,unresolvedReferences}));
}

console.log(JSON.stringify({
  format:"p143-dominated-divisorial-reproducibility-audit-v1",
  status:"PASS_REPRODUCIBLE_FROZEN_INPUTS_ONLY",
  inputs,
  uniqueLabels:labels.length,
  internalReferenceUses:references.length,
  duplicateLabels,
  unresolvedReferences,
  limitations:[
    "not an independent mathematical audit",
    "not a source-closed production verification",
    "not live-manuscript integration authorization",
    "not P14.3 retirement evidence"
  ]
},null,2));
