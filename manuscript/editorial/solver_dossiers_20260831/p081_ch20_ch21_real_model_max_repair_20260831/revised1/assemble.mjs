import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
const here=path.dirname(fileURLToPath(import.meta.url)),parent=path.dirname(here);
const repo='/private/tmp/nappt_p071_20260827';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const inputs=[['ch20_model_forms.tex','7b287229f071aceeaa8396a8ea00bd6f6d70a566f67bdd452fc72bd2281fb586'],['ch21_bfj_psh.tex','957e2a2d16ff85c036aa42c1647aa055f56767fb9973a02b34d4853899d39310']];
const chapters=inputs.map(([name,hash])=>{const source=path.join(parent,'patched',name),text=fs.readFileSync(source,'utf8');if(sha(text)!==hash)throw Error('parent changed');return {name,source,before:text,after:text};});
const changes=[];
function replace(i,oldText,newText,note){const e=chapters[i];if(e.after.split(oldText).length!==2)throw Error('nonunique '+note);e.after=e.after.replace(oldText,newText);changes.push({chapter:e.name,note,before:sha(oldText),after:sha(newText)});}
replace(0,String.raw`nonempty, containing \(\mathcal A\).  Only closedness of the nef cone and
the implication `+String.fromCharCode(96,96)+String.raw`nef \(+\) ample \(\Rightarrow\) ample'' are used later; we
do not need, and do not assert, openness of the ample cone inside \(V\).`,String.raw`nonempty, containing \(\mathcal A\), and open in \(V\): it is the
intersection of \(V\) with the open ample cone of
\(N^1(\cX_s)\).  This is relative openness in the numerical space under
consideration; the restriction map need not be surjective.  The nef cone
therefore has nonempty interior as well.`,'replace stale openness denial by relative-open-cone argument');
replace(0,String.raw`\Cref{lem:ch20-special-fibre-test}\,\cref{itm:ch20-sft:cone} is invoked four
times: in \Cref{prop:ch20-model-max} to make an ample perturbation of a real
class ample; in \Cref{lem:ch20-ample-propagation} and Step~4 of
\Cref{prop:ch20-positive-representative}, both times to add a relatively nef
and a relatively ample class; and in Step~2 of
\Cref{thm:ch20-mixed-hodge} to approximate a relatively nef class by
relatively ample ones.  Every one of these uses only the two facts named at
the end of the proof.  The openness of the ample cone that is used in
Step~1 of \Cref{prop:ch20-positive-representative} is the classical
statement on the smooth projective variety \(X\), not a statement about
\(N^1(\cX/R)\).`,String.raw`The cone facts play distinct roles.  Adding an ample class to a nef one
is used in \Cref{prop:ch20-model-max,lem:ch20-ample-propagation} and in
the positive-representative construction.  Closedness is used when the
perturbation tends to zero, and nef classes are approximated by ample
ones in \Cref{thm:ch20-mixed-hodge}.  Openness on the relative numerical
space is used when rounding vertical divisor coefficients in
\Cref{lem:ch20-fixed-form-rational-approximation}; openness of the
generic ample cone is used in Step~1 of
\Cref{prop:ch20-positive-representative}.  Neither use requires an
identification of the relative numerical space with all of
\(N^1(\cX_s)\).`,'cone-usage ledger');
replace(0,String.raw`Second---and this is the obstruction that always occurs---the maximum
\(\max\{\varphi_1,\varphi_2\}\) of two rational model functions determined
on \(\mathcal X\) need not be determined on \(\mathcal X\), already in
dimension one.  Its restriction to a face of
\(\Delta_{\mathcal X}\) of positive dimension is a maximum of two affine
functions, hence convex and piecewise affine but not affine, so by`,String.raw`Second, there is a separate obstruction when the affine pieces genuinely
cross.  Suppose two rational model functions determined on \(\mathcal X\)
have restrictions to a face such that neither dominates the other
throughout that face.  Their maximum on that face is convex and piecewise
affine but not affine.  Thus their pointwise maximum need not be
determined on \(\mathcal X\), already in dimension one: by`,'qualify non-affineness by crossing');
replace(1,String.raw`in \cite[Lemma~5.3]{BFJ16}.`,String.raw`in \cite[\S5.2]{BFJ16}.`,'verified location of relative-ideal approximation');
fs.mkdirSync(path.join(here,'patched'),{recursive:true});
const entries=[];
for(const e of chapters){
 const dest=path.join(here,'patched',e.name);fs.writeFileSync(dest,e.after,{flag:'wx'});
 const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
 const oldLabels=labels(e.before),newLabels=labels(e.after);
 if(oldLabels.some(l=>!newLabels.includes(l))||new Set(newLabels).size!==newLabels.length)throw Error('labels changed');
 const relative='manuscript/parts/part3/'+e.name;
 const diff=spawnSync('diff',['-u','--label','a/'+relative,'--label','b/'+relative,path.join(repo,relative),dest],{encoding:'utf8'});
 if(![0,1].includes(diff.status))throw Error(diff.stderr);
 const patch=path.join(here,e.name.replace('.tex','.patch'));fs.writeFileSync(patch,diff.stdout,{flag:'wx'});
 const check=spawnSync('git',['apply','--check',patch],{cwd:repo,encoding:'utf8'});if(check.status!==0)throw Error(check.stderr);
 entries.push({name:e.name,source:e.source,sourceSha256:sha(e.before),destination:dest,bytes:Buffer.byteLength(e.after),sha256:sha(e.after),oldLabels:oldLabels.length,newLabels:newLabels.length,patch:{path:patch,sha256:sha(diff.stdout),check:'git apply --check passed; not applied'}});
}
const files=['GATE.md','assemble.mjs'].map(name=>{const b=fs.readFileSync(path.join(here,name));return{name,bytes:b.length,sha256:sha(b)};});
const result={date:'2026-08-31',status:'isolated revised1 pending reviews',changes,entries,files};
fs.writeFileSync(path.join(here,'MANIFEST.json'),JSON.stringify(result,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify(result,null,2));
