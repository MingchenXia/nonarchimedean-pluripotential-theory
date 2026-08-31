import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const base=path.dirname(fileURLToPath(import.meta.url));
const text=f=>fs.readFileSync(f,'utf8');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const assert=(v,s)=>{if(!v)throw new Error(s);};
const plan=JSON.parse(text(path.join(base,'INSERTION_PLAN.json')));
const inputs=JSON.parse(text(path.join(base,'INPUTS.json')));
const labels=s=>[...s.matchAll(/\\label\{([^}]+)\}/g)].map(m=>m[1]);
const refs=s=>[...s.matchAll(/\\(?:Cref|cref|Crefrange|crefrange|eqref|ref)\{[^}]*\}/g)].map(m=>m[0]);
const problems=s=>[...s.matchAll(/\\begin\{problem\}[\s\S]*?\\end\{problem\}/g)].map(m=>m[0]);
let inputChecks=0;
for(const p of inputs.items){const b=fs.readFileSync(p.path);assert(b.length===p.bytes&&hash(b)===p.sha256,'input drift: '+p.role);inputChecks++;}
const patchLines=text(path.join(base,'candidate.patch')).trimEnd().split('\n');
let cursor=0,files=[];
for(const item of plan.files){
 const old=text(path.join(plan.baseline_root,item.target));
 assert(Buffer.byteLength(old)===item.baseline_bytes&&hash(old)===item.baseline_sha256,'baseline drift: '+item.target);
 const edits=item.insertions.map(e=>{
  const offset=e.at==='end'?old.length:old.indexOf(e.anchor);
  assert(offset===e.offset&&(!e.anchor||old.indexOf(e.anchor,offset+1)<0),'anchor mismatch');
  const inserted=(e.prefix||'')+text(path.join(base,e.fragment))+(e.suffix||'');
  assert(hash(inserted)===e.inserted_sha256&&Buffer.byteLength(inserted)===e.inserted_bytes,'fragment drift');
  return {...e,inserted};
 });
 let proposed=old;
 for(const e of [...edits].reverse()) proposed=proposed.slice(0,e.offset)+e.inserted+proposed.slice(e.offset);
 assert(hash(proposed)===item.proposed_sha256&&Buffer.byteLength(proposed)===item.proposed_bytes,'proposed hash');
 let recovered=proposed,shift=0,positions=[];
 for(const e of edits){positions.push([e.offset+shift,e.inserted]);shift+=e.inserted.length;}
 for(const [offset,inserted] of positions.reverse()){assert(recovered.slice(offset,offset+inserted.length)===inserted,'reverse bytes');recovered=recovered.slice(0,offset)+recovered.slice(offset+inserted.length);}
 assert(recovered===old,'original bytes not recovered');
 assert(patchLines[cursor++]==='--- a/'+item.target&&patchLines[cursor++]==='+++ b/'+item.target,'portable patch header');
 const oldLines=old.slice(0,-1).split('\n');let applied=[],oldPos=0,hunks=0;
 while(cursor<patchLines.length&&patchLines[cursor].startsWith('@@ ')){
  const m=/^@@ -(\d+),(\d+) \+(\d+),(\d+) @@$/.exec(patchLines[cursor++]);assert(m,'hunk header');
  const start=+m[1]-1;applied.push(...oldLines.slice(oldPos,start));oldPos=start;
  assert(applied.length===+m[3]-1,'new hunk position');let oldCount=0,newCount=0;
  while(cursor<patchLines.length&&!patchLines[cursor].startsWith('@@ ')&&!patchLines[cursor].startsWith('--- a/')){
   const line=patchLines[cursor++],tag=line[0],value=line.slice(1);
   assert(tag===' '||tag==='+','non-insertion patch');
   if(tag===' '){assert(oldLines[oldPos++]===value,'patch context');oldCount++;}
   applied.push(value);newCount++;
  }
  assert(oldCount===+m[2]&&newCount===+m[4],'patch hunk counts');hunks++;
 }
 applied.push(...oldLines.slice(oldPos));
 assert(applied.join('\n')+'\n'===proposed,'saved patch differs from plan');
 const added=edits.map(e=>e.inserted).join('\n');
 const oldLabels=labels(old),newLabels=labels(added);
 assert(oldLabels.every(l=>labels(proposed).includes(l)),'old label missing');
 assert(newLabels.every(l=>!oldLabels.includes(l)),'new label collision');
 assert(JSON.stringify(problems(old))===JSON.stringify(problems(proposed)),'problem changed');
 // Exact reverse recovery above is the stronger check for every old reference token.
 assert(refs(old).every(r=>proposed.includes(r)),'old reference token missing');
 files.push({target:item.target,baseline_sha256:item.baseline_sha256,proposed_sha256:item.proposed_sha256,hunks,old_labels:oldLabels.length,added_labels:newLabels.length,unchanged_problem_environments:problems(old).length});
}
assert(cursor===patchLines.length,'unparsed patch data');
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)]);
const corpus=walk(path.join(plan.baseline_root,'manuscript/parts')).filter(f=>f.endsWith('.tex')).map(text).join('\n');
const snippets=['ch14_component_curvature.tex','ch14_prerequisite_item.tex','ch72_component_curvature_bridge.tex'].map(f=>text(path.join(base,f))).join('\n');
const newLabels=labels(snippets),allLabels=new Set([...labels(corpus),...newLabels]);
assert(new Set(newLabels).size===newLabels.length,'duplicate new labels');
assert(newLabels.every(l=>!labels(corpus).includes(l)),'new label exists in current corpus');
const newRefs=[...snippets.matchAll(/\\(?:Cref|cref|eqref|ref)\{([^}]+)\}/g)].flatMap(m=>m[1].split(',').map(x=>x.trim()));
assert(newRefs.every(r=>allLabels.has(r)),'unresolved new reference: '+newRefs.filter(r=>!allLabels.has(r)));
const bibText=walk(path.join(plan.baseline_root,'manuscript/bibliography')).filter(f=>f.endsWith('.bib')).map(text).join('\n');
const addedBib=text(path.join(base,'bibliography_addition.bib'));
const keys=s=>[...s.matchAll(/@\w+\s*\{\s*([^,\s]+)/g)].map(m=>m[1]);
assert(keys(addedBib).every(k=>!keys(bibText).includes(k)),'new bibliography key collision');
const allKeys=new Set([...keys(bibText),...keys(addedBib)]);
const citations=[...snippets.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]+)\}/g)].flatMap(m=>m[1].split(','));
assert(citations.every(k=>allKeys.has(k)),'unresolved citation');
const stack=[];
for(const m of snippets.matchAll(/\\(begin|end)\{([^}]+)\}/g)){if(m[1]==='begin')stack.push(m[2]);else assert(stack.pop()===m[2],'environment mismatch');}
assert(stack.length===0,'unclosed environment');
assert(!/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(snippets+addedBib),'control character');
let manifestEntries=0,checksumEntries=0;
if(fs.existsSync(path.join(base,'MANIFEST.json'))){
 const mf=JSON.parse(text(path.join(base,'MANIFEST.json')));
 for(const p of mf.files){const b=fs.readFileSync(path.join(base,p.path));assert(b.length===p.bytes&&hash(b)===p.sha256,'manifest mismatch '+p.path);manifestEntries++;}
 for(const line of text(path.join(base,'SHA256SUMS')).trim().split('\n')){const m=/^([0-9a-f]{64})  (.+)$/.exec(line);assert(m&&hash(fs.readFileSync(path.join(base,m[2])))===m[1],'checksum mismatch');checksumEntries++;}
}
console.log(JSON.stringify({status:'mechanical checks passed; not an independent mathematical or clean production verdict',input_checks:inputChecks,files,new_labels:newLabels.length,new_reference_occurrences:newRefs.length,citation_occurrences:citations.length,manifest_entries:manifestEntries,checksum_entries:checksumEntries},null,2));
