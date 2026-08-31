// Mechanical assembly of independently reviewable fragments; never edits live sources.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';

const here=path.dirname(fileURLToPath(import.meta.url));
const repo='/private/tmp/nappt_p071_20260827';
const live=path.join(repo,'manuscript/parts/part3/ch23_bfj_envelopes.tex');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const original=fs.readFileSync(live,'utf8');
if(hash(original)!=='f311c1dc6f375f98d09e5a076997ebe8c7e5ce836f3efbb686b48afabd87a228')
  throw new Error('Live source changed: rebase and review before assembly');
const read=n=>fs.readFileSync(path.join(here,n),'utf8');
let proposal=original;
function replaceSpan(start,end,replacement) {
  const a=proposal.indexOf(start);
  const b=proposal.indexOf(end,a+start.length);
  if(a<0||b<0||proposal.indexOf(start,a+1)>=0) throw new Error('Ambiguous span '+start);
  proposal=proposal.slice(0,a)+replacement+'\n'+proposal.slice(b);
}
replaceSpan('\\emph{Step 2: a model competitor on the skeleton of \\(\\mathcal Z\\).}',
  '\\emph{Step 4: conclusion.}',read('fixed_skeleton_approximation.tex'));
const example='\\begin{example}[An obstacle envelope on a curve skeleton, in numbers]';
if(proposal.split(example).length!==2) throw new Error('Ambiguous example insertion');
proposal=proposal.replace(example,read('curve_chord_bridge.tex')+'\n'+example);
replaceSpan('\\emph{\\(P\\) is the global envelope.}',
  '\\end{example}',read('numerical_example_end.tex'));
replaceSpan('In dimension one, however, the chain does stabilize, and it stabilizes as',
  '\\end{remark}',read('model_dependence_end.tex'));
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const oldLabels=labels(original),newLabels=labels(proposal);
const missing=oldLabels.filter(x=>!newLabels.includes(x));
const duplicates=newLabels.filter((x,i)=>newLabels.indexOf(x)!==i);
if(missing.length||duplicates.length) throw new Error(JSON.stringify({missing,duplicates}));
const out=path.join(here,'patched');fs.mkdirSync(out,{recursive:true});
const target=path.join(out,'ch23_bfj_envelopes.tex');fs.writeFileSync(target,proposal);
const d=spawnSync('diff',['-u','--label','a/manuscript/parts/part3/ch23_bfj_envelopes.tex',
  '--label','b/manuscript/parts/part3/ch23_bfj_envelopes.tex',live,target],{encoding:'utf8'});
if(![0,1].includes(d.status)) throw new Error(d.stderr);
fs.writeFileSync(path.join(here,'chapter.patch'),d.stdout);
const check=spawnSync('git',['apply','--check',path.join(here,'chapter.patch')],{cwd:repo,encoding:'utf8'});
if(check.status!==0) throw new Error(check.stderr);
const files=['fixed_skeleton_approximation.tex','curve_chord_bridge.tex',
 'numerical_example_end.tex','model_dependence_end.tex','GATE.md','assemble.mjs',
 'patched/ch23_bfj_envelopes.tex','chapter.patch'];
const record=p=>{const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:hash(b)};};
const manifest={date:'2026-08-31',status:'isolated candidate, NOT integrated or production-verified',
 base:'4ec9fb514e9d33d0f8e1b6d918d6264a104cb676',inputs:[record(live),
 record(path.join(repo,'manuscript/parts/part3/ch21_bfj_psh.tex'))],
 outputs:files.map(f=>record(path.join(here,f))),checks:{oldLabels:oldLabels.length,
 newLabels:newLabels.length,missingLabels:missing,duplicateLabels:duplicates,gitApplyCheck:'PASS'}};
fs.writeFileSync(path.join(here,'MANIFEST.json'),JSON.stringify(manifest,null,2)+'\n');
console.log(JSON.stringify({checks:manifest.checks,patch:hash(d.stdout),proposal:hash(proposal)},null,2));
