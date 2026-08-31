import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const dir=path.dirname(fileURLToPath(import.meta.url));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=f=>fs.readFileSync(f,'utf8');
const ok=(v,s)=>{if(!v)throw Error(s);};
const inputs=JSON.parse(read(path.join(dir,'INPUTS.json')));
for(const p of inputs.items){const b=fs.readFileSync(p.path);ok(b.length===p.bytes&&hash(b)===p.sha256,'input drift '+p.role);}
const tex=read(path.join(dir,'corollary.tex'));
const imported=inputs.items.filter(p=>['component_latex_candidate','book_problem_context'].includes(p.role)).map(p=>read(p.path)).join('\n');
const getLabels=t=>[...t.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const labels=new Set([...getLabels(imported),...getLabels(tex),inputs.planned_label]);
const refs=[...tex.matchAll(/\\(?:Cref|cref|eqref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
ok(refs.every(r=>labels.has(r)),'unresolved/unplanned reference');
ok(refs.filter(r=>r===inputs.planned_label).length===1,'planned prerequisite missing');
const stack=[];for(const m of tex.matchAll(/\\(begin|end)\{([^}]+)\}/g)){if(m[1]==='begin')stack.push(m[2]);else ok(stack.pop()===m[2],'environment mismatch');}ok(!stack.length,'open environment');
ok(!/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(tex),'control byte');
let manifest=0,sums=0;
if(fs.existsSync(path.join(dir,'MANIFEST.json'))){
for(const p of JSON.parse(read(path.join(dir,'MANIFEST.json'))).files){const b=fs.readFileSync(path.join(dir,p.path));ok(b.length===p.bytes&&hash(b)===p.sha256,'manifest '+p.path);manifest++;}
for(const s of read(path.join(dir,'SHA256SUMS')).trim().split('\n')){let m=/^([a-f0-9]{64})  (.+)$/.exec(s);ok(m&&hash(fs.readFileSync(path.join(dir,m[2])))===m[1],'sums');sums++;}
}
console.log(JSON.stringify({input_pins:inputs.items.length,own_labels:getLabels(tex),reference_occurrences:refs.length,planned_dependency:inputs.planned_label,manifest_entries:manifest,checksum_entries:sums,scope:'mechanical checks only; not independent math/production approval'},null,2));
