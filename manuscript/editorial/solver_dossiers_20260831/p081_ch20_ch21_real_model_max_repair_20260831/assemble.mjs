import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const packet=path.dirname(fileURLToPath(import.meta.url));
const repo='/private/tmp/nappt_p071_20260827';
const dossiers=path.dirname(packet);
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const source20=path.join(dossiers,'p081_ch20_ch22_ch24_unit_weight_followup_20260831/patched/ch20_model_forms.tex');
const source21=path.join(repo,'manuscript/parts/part3/ch21_bfj_psh.tex');
const original20=fs.readFileSync(source20,'utf8');
if(hash(original20)!=='bc479b67a29261f001d0409656e150bc3bf9441dbdf1ff90fb4298fe3c1ad414') throw Error('Ch20 parent changed');
const original21=fs.readFileSync(source21,'utf8');
let ch20=original20, ch21=original21;
const operations=[];
function replace(ch,oldText,newText,description){
 let text=ch===20?ch20:ch21;
 if(text.split(oldText).length!==2) throw Error(`nonunique/missing ${ch}: ${description}`);
 text=text.replace(oldText,newText);
 if(ch===20) ch20=text; else ch21=text;
 operations.push({chapter:ch,description,oldSha256:hash(oldText),newSha256:hash(newText)});
}
function range(ch,start,end,newText,description){
 const text=ch===20?ch20:ch21;
 const a=text.indexOf(start),b=text.indexOf(end,a+start.length);
 if(a<0||b<a||text.indexOf(start,a+1)>=0) throw Error(`range failure ${description}`);
 replace(ch,text.slice(a,b),newText,description);
}
const fragment=name=>fs.readFileSync(path.join(packet,name),'utf8');

replace(20,String.raw`\item \emph{The \(\theta\)-psh model functions are stable under finite
 maxima}`,String.raw`\item \emph{The rational \(\theta\)-psh model functions are stable under
 finite maxima}`,'payoff specifies rational potentials');
replace(20,String.raw`convex combinations and rational ones when invoking line bundles or base
ideals.`,String.raw`convex combinations and rational ones when invoking line bundles or base
ideals.  This distinction also matters for maxima: rational model functions
are closed under that operation, whereas real model functions need not be;
see \Cref{ex:ch20-real-max-irrational-breakpoint}.`,'model-space convention');
replace(20,String.raw`This is the entire mechanism of \Cref{prop:ch20-model-max}: the maximum of
two model functions is realized by a sum of ideals, and positivity is then
read off from global generation.`,String.raw`This is the mechanism of the rational maximum assertion in
\Cref{prop:ch20-model-max}: after clearing denominators, a sum of ideals
realizes the maximum, and global generation supplies positivity.`,'ideal mechanism coefficient scope');
replace(20,String.raw`The real \(\theta\)-psh model functions form a convex set and are stable
under finite maxima.`,String.raw`For every real closed model form \(\theta\), the real \(\theta\)-psh
model functions form a convex set.  The rational \(\theta\)-psh model
functions are closed under rational convex combinations and finite maxima.
No ampleness assumption on \(\{\theta\}\) is needed for these assertions.
Finite-maximum closure here applies to rational potentials, not to all of
\(\mathcal D(X)_{\mathbf R}\).`,'correct maximum proposition without rationalizing theta');
replace(20,String.raw`Convexity is immediate from the convexity of the nef cone.  The maximum
requires more care.  First take rational model functions`,String.raw`Real convexity, and rational convexity within the rational subspace,
follow from convexity of the nef cone.  For the maximum assertion, take
rational model functions`,'maximum proof opening');
replace(20,String.raw`\(\varepsilon_j\) tend to zero and using closedness of the nef cone proves
the rational case.  Real model functions follow by rational approximation
on a common finite-dimensional space and another use of closedness.`,String.raw`\(\varepsilon_j\) tend to zero proves the claim.  To justify this last
step on one numerical space, fix a model \(\mathcal Y\) dominating
\(\mathcal X\) on which the rational model function
\(\max\{\varphi_1,\varphi_2\}\) is determined.  Such a model is obtained
by blowing up the sum ideal for any fixed common denominator of
\(D_1,D_2\), independently of the perturbation.  Each perturbed form is
semipositive, hence has nef determination on this same \(\mathcal Y\)
by \Cref{prop:ch20-semipositive-well-defined}.  Closedness of the nef
cone there gives the unperturbed form.  This is the rational maximum
argument of \cite[Proposition 5.8]{BFJ16}; it does not assert that a
uniform limit remains in the model-function space.`,'fixed determining space and removal of false real limit');
replace(20,String.raw`\begin{remark}[Why the naive argument fails]`,fragment('rational_approximation.tex')+'\n'+String.raw`\begin{remark}[Why the naive argument fails]`,'fixed-form density and irrational-breakpoint diagnostic');
replace(20,String.raw`independent of positivity: in dimension \(n\ge2\) the maximum of two model
functions determined on \(\mathcal X\) is usually not determined on
\(\mathcal X\) (\Cref{ex:ch20-max-fails-naively}).`,String.raw`independent of positivity: already on a curve, a maximum can create a
new breakpoint and fail to be determined on the original model.
For rational potentials a higher model realizes the maximum, but an
irrational breakpoint can prevent any model from doing so
(\Cref{ex:ch20-real-max-irrational-breakpoint}).`,'separate vertex maxima from pointwise model maxima');
replace(20,String.raw`\(\max\{\varphi_1,\varphi_2\}\) of two model functions determined on
\(\mathcal X\) is, in dimension \(n\geq2\), in general \emph{not} determined
on \(\mathcal X\), whatever its vertex values.`,String.raw`\(\max\{\varphi_1,\varphi_2\}\) of two rational model functions determined
on \(\mathcal X\) need not be determined on \(\mathcal X\), already in
dimension one.`,'pointwise refinement example scope');
replace(20,String.raw`divisor on \(\mathcal X\); and it is strictly larger than the affine
interpolation of its own vertex values.`,String.raw`divisor on \(\mathcal X\).  By convexity it lies below the affine
interpolation of its vertex values, with strict inequality wherever a
genuine corner prevents equality.`,'correct convex chord inequality');
range(20,String.raw`\begin{corollary}
\label{cor:ch20-truncation}`,String.raw`\begin{proposition}
\label{prop:ch20-maximum-principle}`,fragment('truncation.tex')+'\n','truncation scope and uniform real approximation');
replace(20,String.raw`The maximum construction of \Cref{prop:ch20-model-max} makes the family of
\(\theta\)-psh model functions below a given obstacle upward directed, and
this is exactly what is needed to define an envelope.  We record here the
properties that can be established at model level, and we are explicit about
those that cannot.`,String.raw`We define the model envelope using real model functions, so that real
translations, convex combinations and reference changes remain literal.
The rational subfamily, not the full real family, is closed under maxima.
When the generic class is ample, fixed-form rational approximation shows
that this directed subfamily computes the same envelope.  The distinction
is essential even for continuous obstacles on curves.`,'envelope orientation');
replace(20,String.raw`\item\label{itm:ch20-env:directed} the family in
 \eqref{eq:ch20-model-envelope} is nonempty and upward directed, and
 \(P^{\model}_\theta\varphi\) is the pointwise limit of an increasing net of
 \(\theta\)-psh model functions;`,String.raw`\item\label{itm:ch20-env:directed} the family in
 \eqref{eq:ch20-model-envelope} is nonempty.  Its rational subfamily is
 nonempty and upward directed.  If \(\{\theta\}\) is ample, that
 rational subfamily has the same supremum, so
 \(P^{\model}_\theta\varphi\) is the pointwise limit of an increasing
 net of rational \(\theta\)-psh model functions.  The full real family
 need not be upward directed;`,'exact envelope directedness statement');
range(20,String.raw`\cref{itm:ch20-env:directed}.  Nonemptiness:`,String.raw`\cref{itm:ch20-env:bounds}.`,fragment('envelope_directedness_proof.tex'),'envelope proof preserving obstacle by rational downward shift');
replace(20,String.raw`\(C_\theta(\mathcal X)_{\le g}\) is nonempty and has a largest element`,String.raw`\(C_\theta(\mathcal X)_{\le g}\) is nonempty and has a largest element`,'retain fixed-model curve envelope unchanged');
replace(20,String.raw`\Cref{prop:ch20-curve-envelope} solves the envelope problem inside a fixed
model, by a finite-dimensional argument, and the solution is again a model
function on the same model.  In dimension \(n\geq2\) neither conclusion is
available by this route: \Cref{ex:ch20-max-fails-naively} shows that the
admissible set of vertex vectors is not stable under componentwise maximum,
and even if it were, \Cref{prop:ch20-model-max} produces the maximum only
after a blowup.  This is precisely why`,String.raw`\Cref{prop:ch20-curve-envelope} solves the envelope problem for vertex
constraints on a fixed curve model by a finite-dimensional argument.
It does not identify the pointwise maximum of the corresponding affine
interpolants with the interpolant of their vertexwise maximum.
In higher dimension the one-negative-coefficient argument in
\Cref{prop:ch20-curve-lattice} is no longer available for every vertical
curve, and the ideal construction of \Cref{prop:ch20-model-max} generally
requires a higher model even for rational potentials.  Thus this
fixed-model calculation is not a proof of the global envelope theorem.
The arguments in`,'remove unsupported higher-dimensional vertex-set claim');
replace(20,String.raw`\Cref{chap:bfj-envelopes} needs multiplier ideals rather than convex
geometry, and why continuity of envelopes is a theorem with hypotheses
rather than a formality.  It is also why the theory does not simply take
place on one dual complex.`,String.raw`\Cref{chap:bfj-envelopes} use multiplier ideals, and continuity of envelopes
remains a theorem with hypotheses rather than a formality.  The theory
does not take place on just one dual complex.`,'grammar after fixed-model scope correction');
replace(20,String.raw` &Neither regularity nor \(\operatorname{char}k=0\) is used.  The
  corresponding statement for model metrics over an arbitrary complete
  field is \Cref{prop:semipositive-stability}\,(3).`,String.raw` &The rational-potential maximum assertion uses neither regularity nor
  \(\operatorname{char}k=0\).  The fixed-real-form approximation in
  \Cref{lem:ch20-fixed-form-rational-approximation} additionally uses an
  ample generic class and the positive-representative input.`,'scope table separates rational max from ample density');

replace(21,String.raw`\(\theta\)-psh ones among them form a convex set stable under maxima
(\Cref{prop:ch20-model-max}).`,String.raw`real \(\theta\)-psh ones form a convex set, whereas maximum closure at
model level belongs to the rational subspace
(\Cref{prop:ch20-model-max}).  In an ample generic class, rational and
real \(\theta\)-psh model functions have the same uniform closure
(\Cref{lem:ch20-fixed-form-rational-approximation}).`,'Ch21 opening rational-real distinction');
replace(21,String.raw`\(\varphi\).  A real model function is obtained as a limit, on one common
model, of rational vertical divisors after an arbitrarily small ample
perturbation of the curvature class, exactly as in the last paragraph of the
proof of \Cref{prop:ch20-model-max}; closedness of the nef cone and uniform
convergence of divisor functions give the same conclusions.`,String.raw`\(\varphi\).  For a real \(\theta\)-psh model function, apply
\Cref{lem:ch20-fixed-form-rational-approximation} at the same fixed form
\(\theta\), whose generic class is ample by the standing hypotheses of
this chapter.  The rational approximants satisfy the two inequalities
already proved.  Their uniform convergence passes those inequalities to
the given real model function, without changing the reference form.`,'skeletal inequality real approximation uses fixed theta');
replace(21,String.raw`clause~(2), if \(\psi_k,\chi_k\) are \(\theta_1\)-psh model functions
approximating \(\varphi,\psi\) uniformly on \(\Delta_{\mathcal X}\), then
\(\max\{\psi_k,\chi_k\}\) is again a \(\theta_1\)-psh model function by
\Cref{prop:ch20-model-max}, and the elementary inequality`,String.raw`clause~(2), take real \(\theta_1\)-psh model functions
\(\psi_k,\chi_k\) approximating \(\varphi,\psi\) uniformly on
\(\Delta_{\mathcal X}\).  By
\Cref{lem:ch20-fixed-form-rational-approximation}, replace each by a
rational \(\theta_1\)-psh model function with global uniform error less
than \(1/k\).  Denote these replacements by
\(\widetilde\psi_k,\widetilde\chi_k\).  Their restrictions still
converge to the required functions.  Now
\(\max\{\widetilde\psi_k,\widetilde\chi_k\}\) is a rational
\(\theta_1\)-psh model function by \Cref{prop:ch20-model-max}, and the
elementary inequality`,'PSH maximum proof rationalizes approximants not theta');
replace(21,String.raw`available forms.  The only composition available at model level is the
maximum, and it is available because of the ideal-theoretic mechanism of
\Cref{prop:ch20-model-max}.`,String.raw`available forms.  Maximum stability at the rational model level uses
the ideal-theoretic mechanism of \Cref{prop:ch20-model-max}; the real
psh assertion uses fixed-form approximation as in the proof above.`,'composition discussion scope');

const output=path.join(packet,'patched');fs.mkdirSync(output,{recursive:true});
const entries=[];
for(const [number,name,before,after,source] of [
 [20,'ch20_model_forms.tex',original20,ch20,source20],
 [21,'ch21_bfj_psh.tex',original21,ch21,source21]]){
 const oldLabels=[...before.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
 const newLabels=[...after.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
 const missing=oldLabels.filter(x=>!newLabels.includes(x));
 if(missing.length) throw Error(`lost labels ${missing}`);
 const dest=path.join(output,name);fs.writeFileSync(dest,after,{flag:'wx'});
 entries.push({chapter:number,source,sourceSha256:hash(before),destination:dest,bytes:Buffer.byteLength(after),sha256:hash(after),oldLabels:oldLabels.length,newLabels:newLabels.length,missingLabels:missing});
 const live=path.join(repo,'manuscript/parts/part3',name);
 const diff=spawnSync('git',['diff','--no-index','--',live,dest],{encoding:'utf8'});
 if(![0,1].includes(diff.status)) throw Error(diff.stderr);
 fs.writeFileSync(path.join(packet,`ch${number}.patch`),diff.stdout,{flag:'wx'});
}
const files=['GATE.md','assemble.mjs','rational_approximation.tex','truncation.tex','envelope_directedness_proof.tex','ch20.patch','ch21.patch'].map(name=>{
 const bytes=fs.readFileSync(path.join(packet,name));return {name,bytes:bytes.length,sha256:hash(bytes)};
});
const manifest={date:'2026-08-31',status:'isolated pending independent and production verification',entries,operations,files};
fs.writeFileSync(path.join(packet,'MANIFEST.json'),JSON.stringify(manifest,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({entries,operations:operations.length},null,2));
