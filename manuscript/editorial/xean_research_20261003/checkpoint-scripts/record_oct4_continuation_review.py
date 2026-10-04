"""Record read reviews with immutable source bindings; do not alter campaigns."""
from pathlib import Path
import datetime,hashlib,json

root=Path('/workspace/research')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
for rel,allow in [('round-16/P06.2-curve-two-sign-regularization-review',False),
                  ('round-18/P05.2-fixed-rational-reference-review',True)]:
    d=root/'campaigns'/rel
    c=json.loads((d/'run.json').read_text())['campaign'];r=c['result']
    assert c['status']=='completed'
    b=json.loads((d/'source-artifact-binding.json').read_text())
    f=json.loads((d/'freeze.json').read_text())
    assert sha(d/'argument.md')==f['argument_sha256']==b['review_argument_sha256']
    for p,k in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:
        assert sha(Path(b[p]))==b[k]==f[k]
    assert sha(Path(f['source_workspace'])/'status.json')==b['source_status_sha256']==f['source_status_sha256']
    assert all(type(p['premise']) is int and 0<=p['premise']<len(r['premises']) and p['statement']==r['premises'][p['premise']] for p in r['passages'])
    assert (r['verdict']=='PASS')==allow
    record={'recorded_utc':now,'full_report_premises_and_passages_read':True,
      'run_sha256':sha(d/'run.json'),'argument_sha256':sha(d/'argument.md'),
      'freeze_sha256':sha(d/'freeze.json'),'source_artifact_binding_sha256':sha(d/'source-artifact-binding.json'),
      'verdict':r['verdict'],'premises':len(r['premises']),'passages':len(r['passages']),
      'all_proof_tex_status_hashes_bound':True,'publish_exact_scope':allow,'original_atom_solved':False,
      'root_full_main_and_all_canonical_notes_read':allow,
      'assessment':('Fixed rational-reference graph-product iff accepted, broader original and arbitrary-real-reference negative assertion open. Only harmless equation cross-reference correction required.' if allow else 'INCONCLUSIVE: missing/authentication and semistable-local-structure, harmonic-factorization/slope and arbitrary-extension foundations remain unclosed. No paper published. Root has not read the whole assembled main proof or all canonical notes; this record attests full review result and source bindings only.')}
    assert not (d/'review-read-attestation.json').exists()
    (d/'review-read-attestation.json').write_text(json.dumps(record,indent=2)+'\n')
    if allow:
        w=Path(f['source_workspace']);rr=json.loads((w.parents[1]/'run.json').read_text())['campaign']['result']
        read={'recorded_utc':now,'main_argument':str(w/'P05.2-argument.md'),
          'main_argument_sha256':sha(w/'P05.2-argument.md'),'full_main_read':True,
          'newline_ranges':[[1,240],[241,500],[501,len((w/'P05.2-argument.md').read_text().split('\n'))]],
          'all_canonical_notes_read':True,
          'canonical_notes':[{'id':n['id'],'text_sha256':hashlib.sha256(n['text'].encode()).hexdigest(),'characters':len(n['text'])} for n in rr['notes']],
          'author_audit_research_build_evidence_and_full_diagnostic_program_read':True,
          'exact_review_read_bound':True,'original_atom_solved':False}
        (d/'root-draft-read-record.json').write_text(json.dumps(read,indent=2)+'\n')

repair=root/'campaigns/round-17/P06.2-recognition-source-proof-repair'
r=json.loads((repair/'run.json').read_text())['campaign']['result'];w=Path(r['workspace'])
claim=json.loads((w/'status.json').read_text());assert claim['status']=='incomplete'
evidence={'recorded_utc':now,'source_workspace':str(w),'run_sha256':sha(repair/'run.json'),
 'status_sha256':sha(w/'status.json'),'claim':claim,
 'queued_preparer_outcome':'Exited at exact-id guard: researcher status id is P06.2-R0-source-proof-repair rather than P06.2. No independent review call was made. Frozen result/helper preserved.',
 'mathematical_outcome':'No recognition theorem claimed and no standalone theorem TeX produced. Research records concrete unresolved dependencies. Do not publish as solved; supporting lemmas remain unaudited.',
 'root_full_proof_or_all_notes_read':False,'original_atom_solved':False}
(repair/'incomplete-outcome.json').write_text(json.dumps(evidence,indent=2)+'\n')

active=root/'active-work.json';j=json.loads(active.read_text())
for item in j['continuations']:
    if item['directory'].endswith('P06.2-curve-two-sign-regularization-continuation'):
        item['state']='Committed unverified draft; exact review INCONCLUSIVE23/19 fully read and bound; no publication; original scope open.'
    if item['directory'].endswith('P06.2-recognition-source-proof-repair'):
        item['state']='Completed incomplete: no intrinsic universal recognition theorem claimed. Concrete source/foundation gaps retained. Queued reviewer exited exact-id guard before review; no publication.'
    if item['directory'].endswith('P05.2-fixed-rational-reference-continuation'):
        item['state']='Committed fixed rational-reference graph-product partial theorem; exact PASS0/0 fully read and source bound; root complete main/all notes/audit/program read. Publication next; original scope open.'
d=root/'campaigns/round-19/P06.2-general-finite-galois-continuation'
m=json.loads((d/'input-manifest.json').read_text())
j['continuations'].append({'atom':'P06.2','directory':str(d),'tool_session_id':61624,
 'model':'gpt-6.1-sol','reasoning':'xhigh','state':'Fresh finite-Galois all-pure-dimensions complementary-test ascent research running; proposal fallible, no grant; original scope open.',
 'queued_review_directory':m['review_directory'],'queued_review_tool_session_id':5538,
 'review_preparer':m['review_preparer'],'inputs':m['inputs']})
j['updated_utc']=now
j['next_work']='Publish exact accepted fixed rational-reference graph-product theorem; preserve P06 inconclusive/incomplete source chains and read new proof where useful; fresh finite-Galois complementary-test campaign continues. Keep original42 open and push regularly.'
j['turn_checkpoint']='P05 fixed rational-reference graph-product PASS0/0 read/bound, publication next. P06 two-sign INCONCLUSIVE23/19 preserved; recognition repair incomplete/no theorem. Fresh P06 finite-Galois all-dimensional gate active. All42original open.'
active.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print('Two complete review results bound; incomplete repair preserved; fresh finite-Galois campaign registered.')
