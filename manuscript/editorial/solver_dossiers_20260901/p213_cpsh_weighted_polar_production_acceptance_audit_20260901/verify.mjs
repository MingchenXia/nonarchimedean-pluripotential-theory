import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';

// Read-only. No service/network access, production MCP import or output write.
const root=path.dirname(fileURLToPath(import.meta.url)), failures=[];
const read=p=>fs.readFileSync(p), json=p=>JSON.parse(read(p));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const must=(b,m)=>{if(!b)failures.push(m);};
const pins=json(path.join(root,'REVIEWED_INPUTS.json'));
const cov=json(path.join(root,'COVERAGE.json'));
const by=(role,name)=>pins.entries.find(e=>e.role===role&&e.path.endsWith('/'+name))?.path;
must(pins.entries.length===39&&new Set(pins.entries.map(e=>e.path)).size===39,'Expected 39 unique direct pins');
for(const e of pins.entries){try{const b=read(e.path);must(b.length===e.bytes,'Size mismatch '+e.path);must(hash(b)===e.sha256,'SHA mismatch '+e.path);}catch(err){failures.push('Read failed '+e.path+': '+err.message);}}
must(cov.run_id===pins.run_id,'Run mismatch');
must(cov.execution_compliance==='EXCEPTION'&&cov.clean_production_gate_accepted===false,'Execution caveat erased or clean gate asserted');
must(cov.byte_binding==='PASS'&&cov.mathematical_reference_coverage==='PASS','Limited verdict changed');
const lines=p=>read(p).toString('utf8').trim().split('\n').filter(Boolean).map(JSON.parse);
const sc=lines(by('memory','statement_checks.jsonl')),rc=lines(by('memory','reference_checks.jsonl')),es=lines(by('memory','events.jsonl'));
must(sc.length===18&&rc.length===15&&es.length===53,'Record count mismatch');
must(JSON.stringify(sc.map(x=>x.record.location))===JSON.stringify(cov.statement_locations),'Statement map mismatch');
const statuses={};
for(const c of cov.references){
 const r=rc[c.row-1]?.record;
 must(r?.reference_id===c.reference_id&&r?.location===c.location&&r?.status===c.status,'Reference map mismatch '+c.reference_id);
 must(r?.source_location===c.source_location,'Source locator changed '+c.reference_id);
 must(r?.arxiv_match_found===false&&r?.web_match_found===true,'Fallback status changed '+c.reference_id);
 must(typeof r?.context_expansion==='string'&&typeof r?.application_check==='string','Source comparison missing '+c.reference_id);
 statuses[r.status]=(statuses[r.status]??0)+1;
}
must(JSON.stringify(statuses)===JSON.stringify(cov.source_status_counts),'Source role counts mismatch');
for(const x of [...sc,...rc])must(Array.isArray(x.record.critical_errors)&&x.record.critical_errors.length===0&&Array.isArray(x.record.gaps)&&x.record.gaps.length===0,'Recorded mathematical findings changed');
const attempts=es.filter(x=>x.record?.event==='arxiv_search_attempt');
must(attempts.length===15,'Expected 15 theorem-search attempts');
for(const x of attempts){
 const r=x.record,f=rc.find(y=>y.record.reference_id===r.reference_id)?.record;
 must(r.query===f?.referenced_statement&&r.result.query===r.query,'Full query mismatch '+r.reference_id);
 must(typeof r.result.error==='string'&&r.result.results.length===0,'Transport result changed '+r.reference_id);
}
must(new Set(attempts.map(x=>x.record.reference_id)).size===15,'Duplicate/missing search id');
const done=es.find(x=>x.record?.event==='sequential_and_reference_checks_completed')?.record;
must(done?.statement_items===18&&done?.reference_items===15&&done?.critical_errors===0&&done?.gaps===0,'No source-resolution completion');
const failed=lines(by('memory','failed_checks.jsonl'));
must(failed.length===1&&failed[0].record.mathematical_issue===false&&failed[0].record.reference_ids.length===15,'Failed-check scope changed');
const result=json(by('result','verification.json')),reports=lines(by('memory','verification_reports.jsonl'));
must(reports.length===2&&JSON.stringify(reports[0].record.payload)===JSON.stringify(result),'Synthesis/result mismatch');
must(reports[0].record.validation.valid===true&&reports[1].record.verdict==='correct','Final validation/write changed');
must(json(by('memory','meta.json')).run_id===pins.run_id,'Metadata run mismatch');
const log=read(by('result','log.md')).toString('utf8');
must(log.includes(cov.execution_exception.exact_error),'Approval refusal missing');
must(log.includes('from mcp.server import memory_init, memory_append'),'Direct helper operation missing');
must(log.includes('Connector memory call required unavailable approval'),'Alternate-route event missing');
const proof=read(by('packet','PROOF.md')).toString('utf8');
for(let i=1;i<=8;i++)must(proof.includes('## '+i+'. '),'Missing section '+i);
for(const s of ['## 9.','SOURCE_AUDIT.md','Section 9'])must(!proof.includes(s),'Excluded proof dependency present '+s);
const packet=spawnSync(process.execPath,[by('packet','check_packet.mjs')],{encoding:'utf8'});
must(packet.status===0,'Packet checker failed '+packet.stderr+packet.stdout);
const receiptArgs=[by('packet','STATEMENT.md'),by('packet','PROOF.md'),by('http','request.json'),by('http','response.json'),by('http','headers.json'),by('result','log.md'),by('result','verification.json'),by('runtime','RUNTIME_CAPTURE.json')];
const binder=spawnSync('python3',[by('read_only_receipt_checker','audit_sequential_rethlas_receipt.py'),...receiptArgs],{encoding:'utf8'});
must(binder.status===0,'Receipt checker failed '+binder.stderr+binder.stdout);
let binding;
try{binding=JSON.parse(binder.stdout);must(binding.audit==='PASS'&&binding.run_id===pins.run_id&&binding.strict_v02_attestation===false,'Receipt scope mismatch');}catch(e){failures.push('Receipt JSON parse failed');}
const sums=read(path.join(root,'SHA256SUMS')).toString('utf8').trim().split('\n');
const expected=new Set(['AUDIT.md','COVERAGE.json','REVIEWED_INPUTS.json','verify.mjs']);
must(sums.length===4,'Expected four own checksums');
for(const row of sums){const m=/^([a-f0-9]{64})  ([^/]+)$/.exec(row);if(!m||!expected.delete(m[2])){failures.push('Invalid/duplicate checksum row');continue;}must(hash(read(path.join(root,m[2])))===m[1],'Own SHA mismatch '+m[2]);}
must(expected.size===0,'Missing own checksum');
console.log(JSON.stringify({run_id:pins.run_id,directPins:pins.entries.length,ownChecksums:sums.length,
statementRecords:sc.length,referenceRecords:rc.length,eventRecords:es.length,fullStatementSearchAttempts:attempts.length,referenceRoles:statuses,
packetIdentity:packet.status===0,exactReceiptBinding:binding?.audit??'FAIL',mathematicalReferenceVerdict:cov.mathematical_reference_coverage,
executionCompliance:cov.execution_compliance,cleanProductionGateAccepted:cov.clean_production_gate_accepted,writesPerformed:0,
meaning:'Identity and record checks only; mathematical reasoning and compliance assessment are in AUDIT.md.',failures},null,2));
process.exitCode=failures.length?1:0;

