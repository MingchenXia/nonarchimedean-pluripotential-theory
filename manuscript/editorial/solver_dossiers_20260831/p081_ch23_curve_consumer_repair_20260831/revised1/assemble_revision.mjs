// Mechanical revision; frozen parent and live chapter remain untouched.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
const here=path.dirname(fileURLToPath(import.meta.url)),parent=path.dirname(here);
const repo='/private/tmp/nappt_p071_20260827';
const live=path.join(repo,'manuscript/parts/part3/ch23_bfj_envelopes.tex');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const source=fs.readFileSync(live,'utf8');
if(sha(source)!=='f311c1dc6f375f98d09e5a076997ebe8c7e5ce836f3efbb686b48afabd87a228')throw Error('Live source changed');
const old=fs.readFileSync(path.join(parent,'patched/ch23_bfj_envelopes.tex'),'utf8');
if(sha(old)!=='a3e00bb50daa668f107a8847e55408e69c554a88ddc7b6f8dfdf63f785599fca')throw Error('Frozen parent changed');
const add=fs.readFileSync(path.join(here,'snc_addendum.tex'),'utf8');
const bridgeOld=fs.readFileSync(path.join(parent,'curve_chord_bridge.tex'),'utf8');
const bridgeNew=bridgeOld.replace('\\begin{proof}\n','\\begin{proof}\n'+add);
let proposed=old.replace(bridgeOld,bridgeNew);
function once(a,b){if(proposed.split(a).length!==2)throw Error('Ambiguous replacement '+a);proposed=proposed.replace(a,b);}
once('smooth point of the special fibre lying on the component created by the',
 'smooth \\(\\widetilde K\\)-rational point of the special fibre lying on the component created by the');
once('The contact set is \\(\\{e_2\\}\\), since',
 'The skeletal contact set is \\(\\{e_2\\}\\); its full analytic preimage\n\\(p_{\\mathcal X}^{-1}(\\{e_2\\})\\) is the global contact set, since');
once('slope \\(+1\\) on \\([e_2,e_4]\\), that is, harmonic off the contact set, with\nthe two boundary slopes exactly saturating the constraints',
 'slope \\(+1\\) on \\([e_2,e_4]\\).  It is the total curvature\n\\(\\theta+\\mathrm d\\mathrm d^cP\\), not the Laplacian of \\(P\\) alone,\nthat vanishes off the contact set.  The two boundary slopes exactly saturate the constraints');
once('divisor of \\(P\\) satisfies the homogeneous Laplace equation',
 'divisor of \\(P\\) satisfies the reference-adjusted curvature equation');
fs.mkdirSync(path.join(here,'patched'),{recursive:true});
const target=path.join(here,'patched/ch23_bfj_envelopes.tex');
fs.writeFileSync(target,proposed);fs.writeFileSync(path.join(here,'curve_chord_bridge.tex'),bridgeNew);
const d=spawnSync('diff',['-u','--label','a/manuscript/parts/part3/ch23_bfj_envelopes.tex',
 '--label','b/manuscript/parts/part3/ch23_bfj_envelopes.tex',live,target],{encoding:'utf8'});
if(![0,1].includes(d.status))throw Error(d.stderr);
fs.writeFileSync(path.join(here,'chapter.patch'),d.stdout);
const c=spawnSync('git',['apply','--check',path.join(here,'chapter.patch')],{cwd:repo,encoding:'utf8'});
if(c.status!==0)throw Error(c.stderr);
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const a=labels(source),b=labels(proposed),missing=a.filter(x=>!b.includes(x)),dups=b.filter((x,i)=>b.indexOf(x)!==i);
if(missing.length||dups.length)throw Error(JSON.stringify({missing,dups}));
const rec=p=>{const b=fs.readFileSync(p);return{path:p,bytes:b.length,sha256:sha(b)};};
const manifest={date:'2026-08-31',status:'candidate revision, independent and production gates remain',
 inputs:[live,path.join(parent,'MANIFEST.json'),path.join(parent,'patched/ch23_bfj_envelopes.tex')].map(rec),
 outputs:['snc_addendum.tex','curve_chord_bridge.tex','patched/ch23_bfj_envelopes.tex','chapter.patch','assemble_revision.mjs','GATE.md'].map(n=>rec(path.join(here,n))),
 checks:{oldLabels:a.length,newLabels:b.length,missingLabels:missing,duplicateLabels:dups,gitApplyCheck:'PASS'}};
fs.writeFileSync(path.join(here,'MANIFEST.json'),JSON.stringify(manifest,null,2)+'\n');
console.log(JSON.stringify({checks:manifest.checks,bridge:sha(bridgeNew),chapter:sha(proposed),patch:sha(d.stdout)},null,2));
