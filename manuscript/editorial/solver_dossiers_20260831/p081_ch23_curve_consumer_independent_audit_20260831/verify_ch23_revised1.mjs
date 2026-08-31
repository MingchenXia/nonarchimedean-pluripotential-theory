import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root='/private/tmp/nappt_p071_20260827';
const dossier=path.join(root,'manuscript/editorial/solver_dossiers_20260831/p081_ch23_curve_consumer_repair_20260831');
const dir=path.join(dossier,'revised1');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p,'utf8');
const check=(p,h)=>{if(hash(fs.readFileSync(p))!==h)throw Error('Changed bytes: '+p);};
check(path.join(dir,'MANIFEST.json'),'413ae8813d17aeb142aceec46447ad71154c6fdb7140d52e1b4677af47184ac4');
check(path.join(dossier,'MANIFEST.json'),'d174891d4af1c3dc947f8bdfabfc5dbd9dcbb668f70a2b7f15989adc1607cc4a');
const manifests=[dossier,dir].map(p=>JSON.parse(read(path.join(p,'MANIFEST.json'))));
const counts=[];
for(const m of manifests){
 const es=[...m.inputs,...m.outputs];counts.push(es.length);
 for(const e of es){const b=fs.readFileSync(e.path);if(hash(b)!==e.sha256||b.length!==e.bytes)throw Error('Manifest mismatch: '+e.path);}
}
const oldBridge=read(path.join(dossier,'curve_chord_bridge.tex'));
const newBridge=read(path.join(dir,'curve_chord_bridge.tex'));
const add=read(path.join(dir,'snc_addendum.tex'));
if(oldBridge.replace('\\begin{proof}\n','\\begin{proof}\n'+add)!==newBridge)throw Error('Unexpected bridge revision');
const oldFull=read(path.join(dossier,'patched/ch23_bfj_envelopes.tex'));
let expected=oldFull.replace(oldBridge,newBridge);
const replacements=[
 ['smooth point of the special fibre lying on the component created by the','smooth \\(\\widetilde K\\)-rational point of the special fibre lying on the component created by the'],
 ['The contact set is \\(\\{e_2\\}\\), since','The skeletal contact set is \\(\\{e_2\\}\\); its full analytic preimage\n\\(p_{\\mathcal X}^{-1}(\\{e_2\\})\\) is the global contact set, since'],
 ['slope \\(+1\\) on \\([e_2,e_4]\\), that is, harmonic off the contact set, with\nthe two boundary slopes exactly saturating the constraints','slope \\(+1\\) on \\([e_2,e_4]\\).  It is the total curvature\n\\(\\theta+\\mathrm d\\mathrm d^cP\\), not the Laplacian of \\(P\\) alone,\nthat vanishes off the contact set.  The two boundary slopes exactly saturate the constraints'],
 ['divisor of \\(P\\) satisfies the homogeneous Laplace equation','divisor of \\(P\\) satisfies the reference-adjusted curvature equation']
];
for(const[a,b]of replacements){if(expected.split(a).length!==2)throw Error('Ambiguous text');expected=expected.replace(a,b);}
const full=path.join(dir,'patched/ch23_bfj_envelopes.tex');
if(expected!==read(full))throw Error('Unexpected full-copy change');
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const live=path.join(root,'manuscript/parts/part3/ch23_bfj_envelopes.tex');
const oldLabels=labels(read(live)),newLabels=labels(expected);
if(oldLabels.some(l=>!newLabels.includes(l))||new Set(newLabels).size!==newLabels.length)throw Error('Label loss/duplicate');
execFileSync('git',['apply','--check',path.join(dir,'chapter.patch')],{cwd:root});
check(path.join(path.dirname(dossier),'p081_ch23_curve_consumer_independent_audit_20260831/AUDIT.md'),'feb04a45f2b20bfc62773be8274510cb2f5d3b965777480276d132f528449b5c');
console.log(JSON.stringify({earlier_manifest_entries:counts[0],revised_manifest_entries:counts[1],mismatches:0,
exact_revision_scope:'SNC insertion plus four reviewed wording/centre changes only',old_labels:oldLabels.length,new_labels:newLabels.length,
git_apply_check:'passed, not applied',earlier_audit_preserved:true,production_submitted:false},null,2));
