// Mechanical QA and recoverable publication of the already visually reviewed PDF.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const build='/private/tmp/nappt_cld_cycle_repair_20260901_4TqAnG';
const own=path.join(root,'manuscript/editorial/solver_dossiers_20260901/cld_cycle_current_repair_build_20260901');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p);
const snapshotBytes=read(path.join(build,'SOURCE_SNAPSHOT.json'));
const snapshot=JSON.parse(snapshotBytes);
if(snapshot.entries.length!==216)throw Error('Unexpected source count');
for(const e of snapshot.entries){
 for(const base of [snapshot.sourceRoot,build]){
  const b=read(path.join(base,e.path));
  if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Source drift '+base+'/'+e.path);
 }
}
const pdf=read(path.join(build,'book.pdf')),pdfSha=sha(pdf);
if(pdfSha!=='4061c4de8e6af169dea215831e7405cf7a4ef7d637c09928a3b7d964c7c35dfb'||pdf.length!==16618597)throw Error('Unexpected final PDF');
const log=read(path.join(build,'book.log')).toString();
const blg=read(path.join(build,'book.blg')).toString();
const count=re=>(log.match(re)||[]).length;
const logChecks={overfull:count(/Overfull/g),underfull:count(/Underfull/g),undefined:count(/undefined/g),multiplyDefined:count(/multiply defined/g),texErrors:count(/^!/gm),missingCharacters:count(/Missing character/g),bibWarnings:(blg.match(/^Warning--/gm)||[]).length,bibErrors:(blg.match(/error message|I couldn't open|I found no|Illegal,/g)||[]).length};
if(Object.entries(logChecks).some(([k,v])=>k!=='underfull'&&v))throw Error('Final log failure');
const info=execFileSync('/opt/homebrew/bin/pdfinfo',[path.join(build,'book.pdf')],{encoding:'utf8'});
const pages=Number(info.match(/^Pages:\s*(\d+)/m)?.[1]);
const author=info.match(/^Author:[ \t]*(.*)$/m)?.[1];
if(pages!==3478||author!=='')throw Error('PDF metadata drift');
const visualPages=[633,634,635,636,637,638,639,641,642,643,652,653,654,655].map(p=>{
 const b=read(path.join(build,'tmp/pdfs/page-'+String(p).padStart(4,'0')+'.png'));
 return{physical:p,label:String(p-68),bytes:b.length,sha256:sha(b),review:'Root viewed this complete final rendered page, including the changed passages and adjacent transitions.'};
});
const output=path.join(root,'output/pdf/Non-Archimedean_Pluripotential_Theory_current.pdf');
const backup=path.join(root,'output/pdf/Non-Archimedean_Pluripotential_Theory_before_cycle_current_repair_20260901.pdf');
const previousSha='dd0aba9532b258b83af57a84c42d6209f1f9c90f9ba9511e3e2cca442530fc00';
if(sha(read(output))!==previousSha)throw Error('Refuse replacing a changed current PDF');
const record={date:'2026-09-01',sourceFiles:snapshot.entries.length,allLiveAndBuildInputHashesMatch:true,pdf:{path:output,bytes:pdf.length,sha256:pdfSha,pages,author},build:{directory:build,completedExitCode:0,...logChecks},visualPages,previousPdf:{path:backup,sha256:previousSha},snapshotSha256:sha(snapshotBytes),scope:'Known-source Chapter 14 corrections and scoped PDF QA; no research problem retirement or new research theorem promotion'};
if(!process.argv.includes('--publish')){
 console.log(JSON.stringify({preflight:true,...record},null,2));
 process.exit(0);
}
for(const p of [backup,path.join(own,'BUILD_QA.json'),path.join(own,'SOURCE_SNAPSHOT.json')])
 if(fs.existsSync(p))throw Error('Already published or target exists '+p);
fs.copyFileSync(output,backup,fs.constants.COPYFILE_EXCL);
if(sha(read(backup))!==previousSha)throw Error('Backup mismatch');
const temporary=output+'.candidate-'+pdfSha.slice(0,12);
fs.copyFileSync(path.join(build,'book.pdf'),temporary,fs.constants.COPYFILE_EXCL);
if(sha(read(temporary))!==pdfSha)throw Error('Publication copy mismatch');
fs.renameSync(temporary,output);
fs.writeFileSync(path.join(own,'SOURCE_SNAPSHOT.json'),snapshotBytes,{flag:'wx'});
fs.writeFileSync(path.join(own,'BUILD_QA.json'),JSON.stringify(record,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({published:true,pages,pdfSha256:pdfSha,backupPreserved:true,output}));

