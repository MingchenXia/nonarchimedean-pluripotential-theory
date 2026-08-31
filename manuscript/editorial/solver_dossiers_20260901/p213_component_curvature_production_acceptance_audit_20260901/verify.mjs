import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';

// Read-only: hashes, JSON parsing, and two pinned read-only identity checkers.
// No production API, network, service mutation, or production MCP helper call.
const root=path.dirname(fileURLToPath(import.meta.url)), failures=[];
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>fs.readFileSync(p);
const json=p=>JSON.parse(read(p));
const must=(condition,message)=>{if(!condition)failures.push(message);};
const pins=json(path.join(root,'REVIEWED_INPUTS.json')), cov=json(path.join(root,'COVERAGE.json'));
const by=(role,name)=>pins.entries.find(e=>e.role===role&&e.path.endsWith('/'+name))?.path;
must(pins.entries.length===39,'Expected 39 direct pins');
must(new Set(pins.entries.map(e=>e.path)).size===39,'Duplicate pin path');
for(const e of pins.entries){try{const b=read(e.path);must(b.length===e.bytes,'Byte size mismatch '+e.path);must(hash(b)===e.sha256,'SHA mismatch '+e.path);}catch(err){failures.push('Cannot read '+e.path+': '+err.message);}}
must(cov.run_id===pins.run_id,'Coverage/run mismatch');
must(cov.execution_compliance==='EXCEPTION','Execution exception erased');
must(cov.clean_production_gate_accepted===false,'Clean promotion incorrectly asserted');
must(cov.byte_binding==='PASS'&&cov.mathematical_reference_coverage==='PASS','Unexpected limited acceptance');
const parseLines=p=>read(p).toString('utf8').trim().split('\n').map(JSON.parse);
const sc=parseLines(by('memory','statement_checks.jsonl'));
const rc=parseLines(by('memory','reference_checks.jsonl'));
must(sc.length===12&&rc.length===28,'Record counts changed');
must(JSON.stringify(sc.map(x=>x.record.location))===JSON.stringify(cov.statement_locations),'Statement coverage mismatch');
const finals=rc.filter(x=>x.record.status==='matched_and_applicable');
must(finals.length===10,'Expected 10 final source groups');
must(rc.filter(x=>x.record.stage==='required_arxiv_search').length===18,'Expected 18 recorded attempts');
for(const c of cov.references){const r=rc[c.row-1]?.record;must(r?.location===c.location&&r?.status==='matched_and_applicable','Source group mismatch '+c.location);must(r?.arxiv_match_found===false&&r?.web_match_found===true,'Search/fallback status changed '+c.location);must(typeof r?.context_expansion==='string'&&typeof r?.comparison==='string','Missing source reasoning '+c.location);}
for(const x of [...sc,...finals])must(Array.isArray(x.record.critical_errors)&&x.record.critical_errors.length===0&&Array.isArray(x.record.gaps)&&x.record.gaps.length===0,'Recorded mathematical findings changed');
const failed=parseLines(by('memory','failed_checks.jsonl'));
must(failed.length===1&&failed[0].record.mathematical_issue===false,'Failed-check disposition changed');
const result=json(by('result','verification.json'));
const reports=parseLines(by('memory','verification_reports.jsonl'));
must(reports.length===2&&JSON.stringify(reports[0].record.payload)===JSON.stringify(result),'Synthesis does not equal result');
const events=parseLines(by('memory','events.jsonl'));
must(events.some(x=>x.record?.event==='verification_complete'&&x.record.verdict==='correct'),'No completion event');
must(json(by('memory','meta.json')).run_id===pins.run_id,'Metadata run mismatch');
const log=read(by('result','log.md')).toString('utf8');
must(log.includes(cov.execution_exception.exact_error),'Approval exception missing from log');
must(log.includes('from mcp.server import memory_init, memory_append'),'Alternate helper operation missing');
must(log.includes('Run-local metadata repaired after a helper race'),'Metadata caveat absent');
const packet=spawnSync(process.execPath,[by('packet','check_packet.mjs')],{encoding:'utf8'});
must(packet.status===0,'Packet identity checker failed: '+packet.stderr+packet.stdout);
let packetResult;
try{packetResult=JSON.parse(packet.stdout);must(packetResult.failures.length===0,'Packet failures');}catch(e){failures.push('Packet checker JSON error');}
const receiptArgs=[
by('packet','STATEMENT.md'),by('packet','PROOF.md'),by('http','request.json'),
by('http','response.json'),by('http','headers.json'),by('result','log.md'),
by('result','verification.json'),by('runtime','RUNTIME_CAPTURE.json')
];
const binder=spawnSync('python3',[by('read_only_receipt_checker','audit_sequential_rethlas_receipt.py'),...receiptArgs],{encoding:'utf8'});
must(binder.status===0,'Durable receipt checker failed: '+binder.stderr+binder.stdout);
let binding;
try{binding=JSON.parse(binder.stdout);must(binding.audit==='PASS'&&binding.run_id===pins.run_id&&binding.strict_v02_attestation===false,'Receipt binder scope/result mismatch');}catch(e){failures.push('Receipt checker JSON error');}
const rows=read(path.join(root,'SHA256SUMS')).toString('utf8').trim().split('\n');
const expected=new Set(['AUDIT.md','COVERAGE.json','REVIEWED_INPUTS.json','verify.mjs']);
must(rows.length===4,'Expected four own checksums');
for(const row of rows){const m=/^([a-f0-9]{64})  ([^/]+)$/.exec(row);if(!m||!expected.delete(m[2])){failures.push('Malformed/duplicate own checksum');continue;}must(hash(read(path.join(root,m[2])))===m[1],'Own SHA mismatch '+m[2]);}
must(expected.size===0,'Own checksum coverage incomplete');
console.log(JSON.stringify({
run_id:pins.run_id,directPins:pins.entries.length,ownChecksums:rows.length,
statementRecords:sc.length,referenceRecords:rc.length,finalReferenceGroups:finals.length,
packetIdentity:packet.status===0,exactReceiptBinding:binding?.audit??'FAIL',
mathematicalReferenceVerdict:cov.mathematical_reference_coverage,
executionCompliance:cov.execution_compliance,cleanProductionGateAccepted:cov.clean_production_gate_accepted,
writesPerformed:0,meaning:'Identity and record checks only. Mathematical reasoning and compliance assessment are in AUDIT.md.',failures
},null,2));
process.exitCode=failures.length?1:0;

