// Mechanical QA and recoverable publication after the recorded root visual review.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import {execFileSync} from 'node:child_process';
const root='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const build='/private/tmp/nappt_cld_hypothesis_repair_20260901_LvcVnD';
const previousBuild='/private/tmp/nappt_cld_hypothesis_repair_20260901_45pIZg';
const own=path.join(root,'manuscript/editorial/solver_dossiers_20260901/cld_hypothesis_repair_build_20260901');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p);
const snapshotBytes=read(path.join(build,'SOURCE_SNAPSHOT.json')),snapshot=JSON.parse(snapshotBytes);
for(const e of snapshot.entries){const b=read(path.join(snapshot.sourceRoot,e.path));if(b.length!==e.bytes||sha(b)!==e.sha256)throw Error('Live source drift '+e.path);}
const pdf=read(path.join(build,'book.pdf')),pdfSha=sha(pdf);
if(pdfSha!=='dd0aba9532b258b83af57a84c42d6209f1f9c90f9ba9511e3e2cca442530fc00')throw Error('Unexpected final PDF');
const log=read(path.join(build,'book.log')).toString(),blg=read(path.join(build,'book.blg')).toString();
const count=re=>(log.match(re)||[]).length;
const logChecks={overfull:count(/Overfull/g),underfull:count(/Underfull/g),undefined:count(/undefined/g),multiplyDefined:count(/multiply defined/g),texErrors:count(/^!/gm),missingCharacters:count(/Missing character/g),bibWarnings:(blg.match(/^Warning--/gm)||[]).length,bibErrors:(blg.match(/error message|I couldn't open|I found no|Illegal,/g)||[]).length};
if(Object.entries(logChecks).some(([k,v])=>k!=='underfull'&&v))throw Error('Final log failure');
const info=execFileSync('/opt/homebrew/bin/pdfinfo',[path.join(build,'book.pdf')],{encoding:'utf8'});
const pages=Number(info.match(/^Pages:\s*(\d+)/m)?.[1]),author=info.match(/^Author:[ \t]*(.*)$/m)?.[1];
if(pages!==3476||author!=='')throw Error('PDF metadata drift');
const visualPages=[793,794,870,871,891,892,1205,1206,1207].map(p=>{
 const b=read(path.join(build,`tmp/pdfs/page-${p}.png`));
 return{physical:p,label:String(p-68),sha256:sha(b),sameAsFirstRenderedAndViewedVersion:b.equals(read(path.join(previousBuild,`tmp/pdfs/page-${p}.png`))),review:'Root viewed the original nine rendered pages; seven final renders are byte-identical, and the two changed final pages 1206/1207 were rendered and viewed again.'};
});
if(visualPages.filter(p=>p.sameAsFirstRenderedAndViewedVersion).length!==7)throw Error('Unexpected visual delta');
const output=path.join(root,'output/pdf/Non-Archimedean_Pluripotential_Theory_current.pdf');
const backup=path.join(root,'output/pdf/Non-Archimedean_Pluripotential_Theory_before_CLD_hypothesis_repair_20260901.pdf');
const previousSha='d7b7bbff8e567f4156e4cc201df8979813cd3b952c70658317bce75d658b0b4d';
if(sha(read(output))!==previousSha)throw Error('Refuse replacing a changed current PDF');
const record={date:'2026-09-01',sourceFiles:snapshot.entries.length,allLiveInputHashesMatch:true,pdf:{path:output,bytes:pdf.length,sha256:pdfSha,pages,author},build:{directory:build,completedExitCode:0,...logChecks},visualPages,previousPdf:{path:backup,sha256:previousSha},snapshotSha256:sha(snapshotBytes),scope:'Existing-result corrections and scoped PDF QA only; no new research theorem or production Rethlas claim'};
if(!process.argv.includes('--publish')){console.log(JSON.stringify({preflight:true,...record},null,2));process.exit(0);}
for(const p of [backup,path.join(own,'BUILD_QA.json'),path.join(own,'SOURCE_SNAPSHOT.json')])if(fs.existsSync(p))throw Error('Already published or target exists '+p);
fs.copyFileSync(output,backup,fs.constants.COPYFILE_EXCL);
if(sha(read(backup))!==previousSha)throw Error('Backup mismatch');
const temporary=output+'.candidate-'+pdfSha.slice(0,12);
fs.copyFileSync(path.join(build,'book.pdf'),temporary,fs.constants.COPYFILE_EXCL);
if(sha(read(temporary))!==pdfSha)throw Error('Publication copy mismatch');
fs.renameSync(temporary,output);
fs.writeFileSync(path.join(own,'SOURCE_SNAPSHOT.json'),snapshotBytes,{flag:'wx'});
fs.writeFileSync(path.join(own,'BUILD_QA.json'),JSON.stringify(record,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({published:true,pages,pdfSha256:pdfSha,backupPreserved:true,output}));
