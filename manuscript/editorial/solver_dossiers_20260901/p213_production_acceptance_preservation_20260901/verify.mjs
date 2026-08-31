import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

// Read-only preservation validation. No child processes, network or writes.
const here=path.dirname(fileURLToPath(import.meta.url));
const repo=path.resolve(here,'../../../../..');
const read=p=>fs.readFileSync(p),json=p=>JSON.parse(read(p));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const failures=[],must=(v,m)=>{if(!v)failures.push(m);};
const map=json(path.join(here,'MAP.json'));
const ids=['20260831T203725Z_6a6a732dcebd','20260831T204323Z_180a3827dff7'];
must(JSON.stringify(map.run_ids)===JSON.stringify(ids),'Unexpected run ids');
must(map.entries.length===22,'Expected 22 preserved files');
must(map.execution_compliance==='EXCEPTION'&&map.clean_production_gate_accepted===false,'Preservation changed compliance disposition');
must(map.original_audit_checkers_fully_relocatable===false,'Relocation caveat erased');
const allowedMemory=new Set(['meta.json','statement_checks.jsonl','reference_checks.jsonl','failed_checks.jsonl','events.jsonl','verification_reports.jsonl']);
const allowedAudit=new Set(['AUDIT.md','COVERAGE.json','REVIEWED_INPUTS.json','verify.mjs','SHA256SUMS']);
let originalsChecked=0,originalsAbsent=0;
for(const e of map.entries){
 must(ids.includes(e.run_id),'Unexpected preserved run');
 must(!path.isAbsolute(e.repository_relative_path)&&!e.repository_relative_path.split('/').includes('..'),'Unsafe relative path');
 must(e.mapped_path===path.join(map.repository_root,e.repository_relative_path),'Historical mapping mismatch');
 const p=path.join(repo,e.repository_relative_path),b=read(p);
 must(b.length===e.bytes&&hash(b)===e.sha256,'Mapped identity mismatch '+p);
 const allowed=e.role==='selected_run_memory'?allowedMemory:e.role==='frozen_acceptance_audit'?allowedAudit:null;
 must(allowed?.has(path.basename(p)),'Unexpected copy role/name '+p);
 if(fs.existsSync(e.original_path)){const a=read(e.original_path);originalsChecked++;must(a.length===e.bytes&&hash(a)===e.sha256&&a.equals(b),'Original/copy drift '+e.original_path);}else originalsAbsent++;
}
must(new Set(map.entries.map(e=>e.repository_relative_path)).size===22,'Duplicate mapped file');
must(map.entries.filter(e=>e.role==='selected_run_memory').length===12,'Expected 12 selected memory files');
const dirs=[...new Set(map.entries.filter(e=>e.role==='frozen_acceptance_audit').map(e=>path.dirname(path.join(repo,e.repository_relative_path))))];
must(dirs.length===2,'Expected two audit directories');
let frozenChecksums=0;
for(const d of dirs){
 must(JSON.stringify(fs.readdirSync(d).sort())===JSON.stringify([...allowedAudit].sort()),'Unexpected audit directory contents '+d);
 const c=json(path.join(d,'COVERAGE.json'));
 must(c.execution_compliance==='EXCEPTION'&&c.clean_production_gate_accepted===false,'Frozen compliance changed '+d);
 const pins=json(path.join(d,'REVIEWED_INPUTS.json'));
 const selected=pins.entries.filter(e=>e.role==='memory');
 must(selected.length===6,'Wrong memory selection '+d);
 for(const e of selected){
  const mapped=map.entries.find(x=>x.role==='selected_run_memory'&&x.original_path===e.path);
  must(mapped?.sha256===e.sha256&&mapped?.bytes===e.bytes,'Memory does not match original role pin '+e.path);
 }
 const rows=read(path.join(d,'SHA256SUMS')).toString('utf8').trim().split('\n');
 must(rows.length===4,'Wrong frozen checksum count');
 for(const row of rows){const m=/^([a-f0-9]{64})  ([^/]+)$/.exec(row);must(Boolean(m),'Malformed frozen checksum');if(m){must(hash(read(path.join(d,m[2])))===m[1],'Frozen checksum mismatch');frozenChecksums++;}}
}
for(const id of ids){
 const d=path.join(here,'memory',id);
 must(JSON.stringify(fs.readdirSync(d).sort())===JSON.stringify([...allowedMemory].sort()),'Unexpected archived memory contents');
 for(const n of allowedMemory){const s=read(path.join(d,n)).toString('utf8');if(n.endsWith('.jsonl'))s.trim().split('\n').filter(Boolean).forEach(JSON.parse);else must(JSON.parse(s).run_id===id,'Metadata run mismatch');}
}
const ownNames=['PRESERVATION.md','MAP.json','verify.mjs','COMMIT_PATHS.json','COMMIT_PATHS.nul','SHA256SUMS'];
const ownPaths=ownNames.map(n=>path.relative(repo,path.join(here,n)).split(path.sep).join('/'));
const expected=[...map.entries.map(e=>e.repository_relative_path),...ownPaths].sort();
const commit=json(path.join(here,'COMMIT_PATHS.json'));
must(expected.length===28&&JSON.stringify(commit)===JSON.stringify(expected),'Commit list scope mismatch');
const nul=read(path.join(here,'COMMIT_PATHS.nul'));
must(nul.equals(Buffer.from(commit.join(String.fromCharCode(0))+String.fromCharCode(0),'utf8')),'NUL list does not match JSON');
const sums=read(path.join(here,'SHA256SUMS')).toString('utf8').trim().split('\n');
const ownExpected=new Set(ownNames.filter(n=>n!=='SHA256SUMS'));
must(sums.length===5,'Expected five wrapper checksums');
for(const row of sums){const m=/^([a-f0-9]{64})  ([^/]+)$/.exec(row);if(!m||!ownExpected.delete(m[2])){failures.push('Malformed/duplicate wrapper checksum');continue;}must(hash(read(path.join(here,m[2])))===m[1],'Wrapper checksum mismatch '+m[2]);}
must(ownExpected.size===0,'Wrapper checksum coverage incomplete');
console.log(JSON.stringify({preservedFiles:map.entries.length,frozenAuditFiles:10,selectedMemoryFiles:12,frozenChecksums,wrapperChecksums:sums.length,
originalsChecked,originalsAbsent,commitPaths:commit.length,NULterminated:nul.at(-1)===0,
executionCompliance:map.execution_compliance,cleanProductionGateAccepted:map.clean_production_gate_accepted,
originalAuditCheckersFullyRelocatable:false,writesPerformed:0,failures},null,2));
process.exitCode=failures.length?1:0;

