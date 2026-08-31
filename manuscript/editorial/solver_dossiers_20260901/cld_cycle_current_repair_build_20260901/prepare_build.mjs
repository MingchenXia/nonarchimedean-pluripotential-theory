// Mechanical exclusive build snapshot for the known-source Chapter 14 repair.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const source=path.join(root,'manuscript');
const base='db8918d5a533c5a29336d97f70b500540dd9484f';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const old=p=>execFileSync('git',['show',base+':manuscript/'+p],{cwd:root});
const tokens=(s,re)=>[...s.matchAll(re)].map(m=>m[0]);
const changed=['parts/part2/ch14_currents.tex'];
const changes=changed.map(p=>{
 const before=old(p),after=fs.readFileSync(path.join(source,p));
 const a=before.toString(),b=after.toString();
 for(const re of [/\\label\{[^}]*\}/g,/\\eqref\{[^}]*\}/g])
  if(JSON.stringify(tokens(a,re))!==JSON.stringify(tokens(b,re)))throw Error('Label/eqref drift '+p);
 if(/[\x00-\x08\x0b-\x1f\x7f]/.test(b))throw Error('Forbidden controls '+p);
 return{path:p,beforeSha256:sha(before),afterSha256:sha(after),beforeBytes:before.length,afterBytes:after.length,labels:tokens(b,/\\label\{[^}]*\}/g).length,eqrefs:tokens(b,/\\eqref\{[^}]*\}/g).length};
});
const unchanged=['parts/part6/ch72_major_open_problems.tex','editorial/open_problem_atomic_inventory_20260824.md','book.tex'];
for(const p of unchanged)if(sha(old(p))!==sha(fs.readFileSync(path.join(source,p))))throw Error('Protected source drift '+p);
const names=['book.tex','latexmkrc'];
function collect(relative){
 for(const e of fs.readdirSync(path.join(source,relative),{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))){
  const p=path.join(relative,e.name);
  if(e.isSymbolicLink())throw Error('Source symlink '+p);
  if(e.isDirectory())collect(p);
  else if(/\.(?:tex|sty|cls|ist|bst|bib|png|jpe?g|pdf|eps)$/.test(e.name))names.push(p);
 }
}
for(const d of ['style','frontmatter','parts','appendices','bibliography','figures'])if(fs.existsSync(path.join(source,d)))collect(d);
for(let i=0;i<names.length;i++)if(names[i].endsWith('.tex')){
 const text=fs.readFileSync(path.join(source,names[i]),'utf8').replace(/(?<!\\)%[^\n]*/g,'');
 for(const m of text.matchAll(/\\(?:input|include|draftinclude)\s*\{([^}]+)\}/g)){
  if(m[1].includes('#'))continue;
  const p=m[1].endsWith('.tex')?m[1]:m[1]+'.tex';
  if(path.isAbsolute(p)||p.split('/').includes('..'))throw Error('Unsafe TeX input '+p);
  if(!fs.existsSync(path.join(source,p)))throw Error('Missing TeX input '+p);
  if(!names.includes(p))names.push(p);
 }
}
if(new Set(names).size!==names.length)throw Error('Duplicate source');
const build=fs.mkdtempSync('/private/tmp/nappt_cld_cycle_repair_20260901_');
const entries=names.sort().map(p=>{
 const b=fs.readFileSync(path.join(source,p)),t=path.join(build,p);
 fs.mkdirSync(path.dirname(t),{recursive:true});
 fs.copyFileSync(path.join(source,p),t,fs.constants.COPYFILE_EXCL);
 if(sha(fs.readFileSync(t))!==sha(b))throw Error('Copy mismatch');
 return{path:p,bytes:b.length,sha256:sha(b)};
});
const record={date:'2026-09-01',baseCommit:base,sourceRoot:source,build,changes,unchangedProblemInputs:unchanged,scope:'Known-source cycle-current corrections; no new research theorem promoted',entries};
fs.writeFileSync(path.join(build,'SOURCE_SNAPSHOT.json'),JSON.stringify(record,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({build,files:entries.length,changes}));
