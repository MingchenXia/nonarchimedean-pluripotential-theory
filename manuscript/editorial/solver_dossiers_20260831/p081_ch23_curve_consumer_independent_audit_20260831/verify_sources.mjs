// Read-only byte/assembly check for the independently reviewed frozen Ch23 candidate.
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
const root='/private/tmp/nappt_p071_20260827';
const dir=path.join(root,'manuscript/editorial/solver_dossiers_20260831/p081_ch23_curve_consumer_repair_20260831');
const digest=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p,'utf8');
const manifestPath=path.join(dir,'MANIFEST.json');
if(digest(fs.readFileSync(manifestPath))!=='d174891d4af1c3dc947f8bdfabfc5dbd9dcbb668f70a2b7f15989adc1607cc4a')throw Error('Candidate manifest changed');
const manifest=JSON.parse(read(manifestPath));
const entries=[...manifest.inputs,...manifest.outputs];
for(const e of entries){
 const b=fs.readFileSync(e.path);
 if(b.length!==e.bytes||digest(b)!==e.sha256)throw Error('Manifest mismatch: '+e.path);
}
const live=manifest.inputs[0].path;
const original=read(live);
let proposal=original;
const fragment=n=>read(path.join(dir,n));
function replaceSpan(start,end,replacement){
 const a=proposal.indexOf(start),b=proposal.indexOf(end,a+start.length);
 if(a<0||b<0||proposal.indexOf(start,a+1)>=0)throw Error('Ambiguous assembly span');
 proposal=proposal.slice(0,a)+replacement+'\n'+proposal.slice(b);
}
replaceSpan('\\emph{Step 2: a model competitor on the skeleton of \\(\\mathcal Z\\).}','\\emph{Step 4: conclusion.}',fragment('fixed_skeleton_approximation.tex'));
const example='\\begin{example}[An obstacle envelope on a curve skeleton, in numbers]';
if(proposal.split(example).length!==2)throw Error('Ambiguous example insertion');
proposal=proposal.replace(example,fragment('curve_chord_bridge.tex')+'\n'+example);
replaceSpan('\\emph{\\(P\\) is the global envelope.}','\\end{example}',fragment('numerical_example_end.tex'));
replaceSpan('In dimension one, however, the chain does stabilize, and it stabilizes as','\\end{remark}',fragment('model_dependence_end.tex'));
const full=path.join(dir,'patched/ch23_bfj_envelopes.tex');
if(proposal!==read(full))throw Error('Fragment/fullcopy mismatch');
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const oldLabels=labels(original),newLabels=labels(proposal);
const missing=oldLabels.filter(l=>!newLabels.includes(l));
const duplicates=newLabels.filter((l,i)=>newLabels.indexOf(l)!==i);
if(missing.length||duplicates.length)throw Error('Labels changed');
const gitBytes=execFileSync('git',['show',manifest.base+':'+path.relative(root,live)],{cwd:root});
if(!gitBytes.equals(fs.readFileSync(live)))throw Error('Live Ch23 differs from base');
execFileSync('git',['apply','--check',path.join(dir,'chapter.patch')],{cwd:root});
const extraSources=[
 ['/private/tmp/thuillier2005.txt','9612f1cd9b4478e4bfafd9a5a7490dd670854043b0df65ce67cd84c73be204cf'],
 [path.join(root,'manuscript/editorial/solver_dossiers_20260831/p081_degree_zero_tate_obstruction_audit_20260831/sources/GJKM_published_2019.txt'),'942bef601044149054cb615612f8709358e22bd59d56bfe10be124dac94a689e'],
 [path.join(root,'manuscript/parts/part3/ch20_model_forms.tex'),'531024045204686aaf0fc12ff0e825bf67367551cd310a26c956740b4d164baa'],
 [path.join(root,'manuscript/editorial/solver_dossiers_20260831/p081_ch29_ch31_weighted_full_scope_isolated_repair_20260831/revised2/ch29_curve_replacement.tex'),'3760582c91ed79994f0d6817adfecd08a80eb720ff12c27b39b11966893b1d0c']
];
for(const[p,h]of extraSources)if(digest(fs.readFileSync(p))!==h)throw Error('Source changed: '+p);
console.log(JSON.stringify({status:'mechanical checks only; mathematical findings are in AUDIT.md',
manifest_entries:entries.length,manifest_mismatches:0,original_labels:oldLabels.length,new_labels:newLabels.length,
missing_labels:missing,duplicate_labels:duplicates,fragment_fullcopy_match:true,live_Ch23_unchanged:true,
git_apply_check:'passed; check only, not applied',extra_source_hashes_checked:extraSources.length,
compile_performed_by_this_audit:false,production_submitted:false},null,2));
