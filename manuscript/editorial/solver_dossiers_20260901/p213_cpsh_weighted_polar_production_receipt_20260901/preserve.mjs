// Exclusive mechanical preservation of a completed actual production run.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root='/Users/mingchen/Projects/Yethlas/nonarchimedean_pluripotential_theory';
const scratch='/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260901';
const own=path.join(root,'manuscript/editorial/solver_dossiers_20260901/p213_cpsh_weighted_polar_production_receipt_20260901');
const runId='20260831T204323Z_180a3827dff7';
const server='/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/results/'+runId;
const packet=path.join(scratch,'p213_cpsh_weighted_polar_production_packet_20260901');
const client=path.join(scratch,'p213_cpsh_weighted_polar_production_run_20260901');
const runtime=path.join(scratch,'rethlas_runtime_check_20260901');
const python='/Users/mingchen/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3';
const checker=path.join(root,'manuscript/editorial/tools/audit_sequential_rethlas_receipt.py');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const pairs=[
 [path.join(packet,'STATEMENT.md'),'inputs/STATEMENT.md'],
 [path.join(packet,'PROOF.md'),'inputs/PROOF.md'],
 ...['request.json','response.json','headers.json'].map(p=>[path.join(client,p),'client/'+p]),
 ...['log.md','verification.json'].map(p=>[path.join(server,p),runId+'/'+p]),
 ...['RUNTIME_CAPTURE.json','capture_runtime.py'].map(p=>[path.join(runtime,p),'runtime/'+p])
];
const originalArgs=[path.join(packet,'STATEMENT.md'),path.join(packet,'PROOF.md'),...['request.json','response.json','headers.json'].map(p=>path.join(client,p)),path.join(server,'log.md'),path.join(server,'verification.json'),path.join(runtime,'RUNTIME_CAPTURE.json')];
const originalAudit=JSON.parse(execFileSync(python,[checker,...originalArgs],{encoding:'utf8'}));
if(originalAudit.audit!=='PASS'||originalAudit.verdict!=='correct')throw Error('Actual receipt not accepted by binding checker');
for(const [,rel]of pairs)if(fs.existsSync(path.join(own,rel)))throw Error('Target exists '+rel);
for(const p of ['PRESERVATION.json','ARCHIVED_RECEIPT_BINDING.json','COMMIT_PATHS.nul'])
 if(fs.existsSync(path.join(own,p)))throw Error('Record exists '+p);
const copied=pairs.map(([source,rel])=>{
 const b=fs.readFileSync(source),target=path.join(own,rel);
 fs.mkdirSync(path.dirname(target),{recursive:true});
 fs.copyFileSync(source,target,fs.constants.COPYFILE_EXCL);
 if(!fs.readFileSync(target).equals(b))throw Error('Copy mismatch '+rel);
 return{source,path:rel,bytes:b.length,sha256:sha(b)};
});
const archivedArgs=['inputs/STATEMENT.md','inputs/PROOF.md','client/request.json','client/response.json','client/headers.json',runId+'/log.md',runId+'/verification.json','runtime/RUNTIME_CAPTURE.json'].map(p=>path.join(own,p));
const archivedAudit=JSON.parse(execFileSync(python,[checker,...archivedArgs],{encoding:'utf8'}));
fs.writeFileSync(path.join(own,'ARCHIVED_RECEIPT_BINDING.json'),JSON.stringify(archivedAudit,null,2)+'\n',{flag:'wx'});
const record={date:'2026-09-01',runId,model:'gpt-5.6-sol',reasoningEffort:'xhigh',copied,originalBindingAudit:originalAudit,archivedBindingPass:archivedAudit.audit==='PASS',scope:'Actual sequential Markdown production receipt and exact inputs. Binding is not a mathematical proof, source audit, novelty certificate, or strict-v0.2 item attestation. Substantive acceptance audit is separate.'};
fs.writeFileSync(path.join(own,'PRESERVATION.json'),JSON.stringify(record,null,2)+'\n',{flag:'wx'});
const relative=path.relative(root,own);
const paths=['preserve.mjs','CHECKPOINT.md','PRESERVATION.json','ARCHIVED_RECEIPT_BINDING.json','COMMIT_PATHS.nul',...copied.map(e=>e.path)].map(p=>path.join(relative,p));
for(const p of paths)if(p!==path.join(relative,'COMMIT_PATHS.nul')&&!fs.existsSync(path.join(root,p)))throw Error('Commit path missing '+p);
fs.writeFileSync(path.join(own,'COMMIT_PATHS.nul'),paths.join('\0')+'\0',{flag:'wx'});
console.log(JSON.stringify({preserved:true,runId,files:copied.length,commitPaths:paths.length,archivedBinding:archivedAudit.audit,verdict:archivedAudit.verdict}));
