// Mechanical assembly into an isolated copy, never into the live book.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
const here=path.dirname(fileURLToPath(import.meta.url));
const repo='/private/tmp/nappt_p071_20260827';
const live=path.join(repo,'manuscript/parts/part3/ch20_model_forms.tex');
const src=fs.readFileSync(live,'utf8');
const fragment=fs.readFileSync(path.join(here,'curve_laplacian_replacement.tex'),'utf8');
const start='\\begin{proposition}\n\\label{prop:ch20-curve-laplacian}';
const end='\\begin{remark}[Multiplicities and edge lengths]';
const i=src.indexOf(start),j=src.indexOf(end,i);
if(i<0||j<0||src.indexOf(start,i+1)>=0)throw Error('Ambiguous replacement');
let dst=src.slice(0,i)+fragment+'\n'+src.slice(j);
const token='identification of its right-hand side with the metric-graph Laplacian\n\\eqref{eq:graph-laplacian} that carries the normalization.';
if(dst.split(token).length!==2)throw Error('Normalization remark changed');
dst=dst.replace(token,'identification with a metric-graph Laplacian that carries the\nnormalization.  For the curvature measure on a nonreduced model, the\ncoefficient is \\(b_i(D\\cdot E_i)\\); node residue degrees must also be\nretained.  The semistable formula above uses \\(\\Delta^{(c)}\\), not the\nunweighted operator \\eqref{eq:graph-laplacian} unless all nodes are rational.');
const output=path.join(here,'patched');fs.mkdirSync(output,{recursive:true});
const target=path.join(output,'ch20_model_forms.tex');fs.writeFileSync(target,dst);
const d=spawnSync('diff',['-u','--label','a/manuscript/parts/part3/ch20_model_forms.tex',
 '--label','b/manuscript/parts/part3/ch20_model_forms.tex',live,target],{encoding:'utf8'});
if(![0,1].includes(d.status))throw Error(d.stderr);
fs.writeFileSync(path.join(here,'chapter.patch'),d.stdout);
const a=spawnSync('git',['apply','--check',path.join(here,'chapter.patch')],{cwd:repo,encoding:'utf8'});
if(a.status!==0)throw Error(a.stderr);
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const before=labels(src),after=labels(dst),missing=before.filter(x=>!after.includes(x)),dups=after.filter((x,i)=>after.indexOf(x)!==i);
if(missing.length||dups.length)throw Error(JSON.stringify({missing,dups}));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const rec=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
const result={date:'2026-08-31',status:'isolated source correction; review gates remain',
 inputs:[rec(live)],outputs:['curve_laplacian_replacement.tex','GATE.md','assemble.mjs','patched/ch20_model_forms.tex','chapter.patch'].map(n=>rec(path.join(here,n))),
 checks:{oldLabels:before.length,newLabels:after.length,missingLabels:missing,duplicateLabels:dups,gitApplyCheck:'PASS'}};
fs.writeFileSync(path.join(here,'MANIFEST.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({checks:result.checks,fragment:sha(fragment),chapter:sha(dst),patch:sha(d.stdout)},null,2));
