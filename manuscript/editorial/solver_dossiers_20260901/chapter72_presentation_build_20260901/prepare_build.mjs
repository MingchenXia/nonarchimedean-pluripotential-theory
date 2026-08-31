// Mechanical, exclusive source snapshot for a clean whole-book build.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const manuscript=path.join(root,'manuscript');
const chapter='parts/part6/ch72_major_open_problems.tex';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const old=execFileSync('git',['show','7bd98db93381af527abeb04f5148118bf0950aae:manuscript/'+chapter],{cwd:root,encoding:'utf8'});
const now=fs.readFileSync(path.join(manuscript,chapter),'utf8');
const archive=fs.readFileSync(path.join(manuscript,'editorial/chapter72_bedford_taylor_verification_archive_20260901.md'),'utf8');
const blocks=[...archive.matchAll(/```tex\n([\s\S]*?)```/g)].map(m=>m[1]);
if(blocks.length!==2)throw Error('Expected exactly two preserved blocks');
let reconstructed=old;
for(const block of blocks){if(!reconstructed.includes(block))throw Error('Archive differs from original');reconstructed=reconstructed.replace(block,'');}
const compactBlank=s=>s.replace(/\n{2,}/g,'\n\n');
if(compactBlank(reconstructed)!==compactBlank(now))throw Error('Unexpected presentation changes');
const tokens=s=>[...s.matchAll(/\\(?:label|cref|Cref|eqref)\{[^}]*\}/g)].map(m=>m[0]);
if(JSON.stringify(tokens(old))!==JSON.stringify(tokens(now)))throw Error('Cross-reference drift');
const problems=s=>[...s.matchAll(/\\begin\{problem\}[\s\S]*?\\end\{problem\}/g)].map(m=>m[0]);
if(JSON.stringify(problems(old))!==JSON.stringify(problems(now)))throw Error('Problem statement changed');
const names=['book.tex','latexmkrc'];
function collect(relative){for(const e of fs.readdirSync(path.join(manuscript,relative),{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))){
 const p=path.join(relative,e.name);if(e.isSymbolicLink())throw Error('Unexpected source symlink');
 if(e.isDirectory())collect(p);else if(/\.(?:tex|sty|cls|ist|bst|bib|png|jpe?g|pdf|eps)$/.test(e.name))names.push(p);
}}
for(const d of ['style','frontmatter','parts','appendices','bibliography','figures'])if(fs.existsSync(path.join(manuscript,d)))collect(d);
// Some accepted theorem bodies are explicit editorial inputs. Follow only
// literal TeX inputs, never copy the entire research tree or its PDFs.
for(let i=0;i<names.length;i++)if(names[i].endsWith('.tex')){
 const text=fs.readFileSync(path.join(manuscript,names[i]),'utf8').replace(/(?<!\\)%[^\n]*/g,'');
 for(const m of text.matchAll(/\\(?:input|include|draftinclude)\s*\{([^}]+)\}/g)){
  if(m[1].includes('#'))continue;
  const relative=m[1].endsWith('.tex')?m[1]:m[1]+'.tex';
  if(path.isAbsolute(relative)||relative.split('/').includes('..'))throw Error('Unexpected input '+relative);
  if(!fs.existsSync(path.join(manuscript,relative)))throw Error('Missing literal input '+relative);
  if(!names.includes(relative))names.push(relative);
 }
}
if(new Set(names).size!==names.length)throw Error('Duplicate source');
const build=fs.mkdtempSync('/private/tmp/nappt_ch72_presentation_20260901_');
const entries=names.sort().map(relative=>{const b=fs.readFileSync(path.join(manuscript,relative));const target=path.join(build,relative);fs.mkdirSync(path.dirname(target),{recursive:true});fs.copyFileSync(path.join(manuscript,relative),target,fs.constants.COPYFILE_EXCL);if(sha(fs.readFileSync(target))!==sha(b))throw Error('Copy differs');return{path:relative,bytes:b.length,sha256:sha(b)};});
const record={date:'2026-09-01',build,sourceRoot:manuscript,baseCommit:'7bd98db93381af527abeb04f5148118bf0950aae',beforeChapterSha:sha(old),afterChapterSha:sha(now),archiveSha:sha(archive),presentationChecks:{verbatimArchivedBlocks:2,otherwiseIdenticalIgnoringBlankLines:true,crossReferenceTokens:tokens(now).length,problemStatementsUnchanged:problems(now).length},entries};
fs.writeFileSync(path.join(build,'SOURCE_SNAPSHOT.json'),JSON.stringify(record,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({build,sourceFiles:entries.length,checks:record.presentationChecks,beforeChapterSha:record.beforeChapterSha,afterChapterSha:record.afterChapterSha}));
