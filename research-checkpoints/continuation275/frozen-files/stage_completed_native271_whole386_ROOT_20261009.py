from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-271/P12.3-whole382380381-independent-proof-and-original-residual'
A=C/'artifacts/codex-1mbVtK'
D=K/'public-P12.3-continuation386-repaired-perfect-charp-and-Jensen-residual-whole-candidate'
P=R/'primary-data-LOCALONLY/P12.3-native271-whole-primary-and-evidence-20261009'
B=K/'P12.3-round271-whole-candidate386-ROOT-proof-source-scope-and-binding-20261009.json'
J=K/'round271-ROOT-whole-content-identity-audit-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists() and not B.exists()
assert sha(J)=='ab71f6b118fdbde78a6fb4c74736c32bf424f0a8a949d1118b5b2d7230775ae1'
assert sha(A/'whole-proof.md')=='ec315b90d92f409ac4ea9d70affc5794f015f9ed1e3bb8af8d266b92b777c46f'
assert sha(A/'P12.3-independent-paper.tex')=='e216e3970d750a05d761b44bfc8af8842f31d134e1624993cd9e629831146f77'
assert sha(K/'round271-actual-native-final.json')=='0b22c4a1b088c3e8015c6b6ba572ef219d3bb5f08ecd0699d0f971f4f612cad1'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
st=load(K/'round271-completed-inspection-LOCALONLY.json')['campaign']; assert st['status']=='completed' and not st['error']
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
actual=load(K/'round271-actual-native-final.json'); expanded=load(A/'native-notes.json')
assert not actual['candidate'] and not expanded['candidate'] and len(actual['notes'])==len(expanded['notes'])==9
old=load(C/'private-primary-packet-bindings.json'); context=load(C/'book-context-bindings.json')
assert len(old)==392 and len(context)==3
for e in old+context:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
D.mkdir(); P.mkdir(); blobs=P/'deduplicated-whole-source-DATA'; blobs.mkdir()
private=[]; copied={}
def retain(p,role):
    p=Path(p); digest=sha(p)
    if digest not in copied:
        dst=blobs/(digest+p.suffix); shutil.copyfile(p,dst); assert sha(dst)==digest; copied[digest]=dst
    dst=copied[digest]; private.append(dict(path=str(dst),origin=str(p),bytes=dst.stat().st_size,sha256=digest,LOCALONLY=True,role=role,whole_body_retained=True,correctness_grant=False))
for e in old:retain(e['path'],'Entire frozen private primary/evidence body; retention is not fresh physical reading')
for e in context:retain(e['path'],'Entire book context LOCALONLY; native271 reading attributed native, not new ROOT reading')
for p in sorted((A/'review').rglob('*')):
    if p.is_file():retain(p,'Native271 retained complete source/reading/identity unit DATA; no source publication or new ROOT reading claim')
retain(A/'reports/displays.jsonl','Entire native271 reading display record LOCALONLY')
for name in ['P12.3-independent-paper.tex','whole-proof.md','native-notes.json','source-ledger.md','coverage.md','scope-and-verdict.json','README.md']:
    shutil.copyfile(A/name,D/name)
shutil.copyfile(K/'round271-actual-native-final.json',D/'actual-settled-native271-FINAL.json')
shutil.copyfile(J,D/J.name)
for aa,bb in zip(actual['notes'],expanded['notes']):
    (D/(aa['id']+'-actual-settled.md')).write_text(aa['text']+'\n')
    shutil.copyfile(A/(bb['id']+'.md'),D/(bb['id']+'-expanded.md'))
for name in ['original-task.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','freeze.json','launch-record.json']:
    shutil.copyfile(C/name,D/('frozen-native271-'+name))
reports=D/'reports'; reports.mkdir()
for name in ['final-audit.json','whole-body-coverage-checks.json','delivery-environment.json','environment.json','bounded-diagnostics.json','delivery-execution.json']:shutil.copyfile(A/'reports'/name,reports/name)
inert=D/'native-programs-INERT-DATA'; inert.mkdir()
for p in sorted(A.glob('*.py')):shutil.copyfile(p,inert/(p.name+'.DATA.txt'))
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,status='UNREVIEWED complete independent native271 draft; whole original P12.3 OPEN/candidateFALSE; no acceptance/count increase',counts=dict(solved=16,open=26,papers=97),whole_original_solved=False,new_accepted_paper=False,actual_FINAL=dict(path=str(K/'round271-actual-native-final.json'),sha256=sha(K/'round271-actual-native-final.json'),all_nine_entire_fields_ROOT_physically_read_untruncated=True,intermediate_messages_excluded=8),ROOT_whole_reading=dict(entire58012character_proof_physically_read=True,overlapping_character_intervals=[[0,19000],[18600,38000],[37600,57100],[56700,58012]],all_nine_DIFFERENT_expanded_outside_fields_and_entire_footers_physically_read=True,all_entire_expanded_mathematical_sections_physically_read_within_whole_proof=True,expanded_sections_exact_after_only_boundary_whitespace_normalization=True,entire_source_ledger11555bytes_scope_coverage_README_and_six_public_reports_physically_read=True,entire635580byteTeX_mathematical_body_exact_literal_math_and_escaped_prose_identity=True,entire_appendices_ledger_coverage_scope_and_qualified_G331B341E350_exact=True,entire_unique_preamble_physically_read=True,whole_content_identity_not_new_fresh_duplicate_body_reading=True),scope='ROOT380 exact relative regularity and ROOT381 exact perfect-extension kernel/image module lemmas get native scoped PASS. Literal382 REJECTED AS WRITTEN at arbitrary-element HH normalization/imperfect K(t) route; generatorwise direct infinite-perfect lifting and perfect descent repair the isolated all-support theorem. New Jensen subprobability raw dual and CE iff weak lower hemicontinuity proved relative to qualified C. Normal raw envelopes zero or uniformly negative. Surrounding surface/isolatedchar0/finite-cover/conductor/curve chain scoped and full original residual retained.',ordinary_published_background_boundary='New exact primary readings attributed native271, not fresh ROOT proof trees. Complete HH02 immediate3.4 previously ROOT read and exact generator/perfect-field correction retained. Recursive HH6/LS/reducedvariant/HH2/Kunz, duality/cohomology/Lipman/BdFF/BFJ foundations explicitly disclosed as ordinary published background; no claim all historical proofs freshly authenticated. Native scoped PASS is not ROOT final acceptance.',original_remaining='Arbitrary excellent normal dim>=3/general nonisolated perfect-charp/char0 infinite-Q/mixed/imperfect/nonalgebraic/nonclosed OPEN. New Jensen criterion lacks general lower hemicontinuity; no genuine normal continuous signed primary/model counterexample obtained. Nonnormal/increasing energy spikes are not normal raw-envelope counterexamples.',all_primary_bodies_literal_source_units_pixels_and_new_full_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,native_build_delivery_read_AS_DATA_only=True,no_other_ACTIVE272_math_read_or_hot_feedback=True,compiler='Standalone saved; built-in compile follows. No successful diagnostic/PDF/export/install/newtab claimed. Other requests pending/unverified.',protected_editor_OPEN_UNCHANGED=True)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261009.json',qual)
write(D/'private-retained-manifest-metadata.json',private)
public=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()]
binding=dict(recorded_utc=now,round=271,paper=386,atom='P12.3',public_directory=str(D),private_directory=str(P),whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qual,public_files=public,private_primary_evidence_and_book_files=private,private_distinct_full_body_blobs=len(copied))
write(B,binding)
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=[272],native271_status='COMPLETED captured and ENTIRE distinct actual/expanded/whole proof/source/scope ROOT read; public whole386 staged UNREVIEWED',native271_whole386=dict(directory=str(D),binding=str(B),binding_sha256=sha(B),candidate=False,status='UNREVIEWED complete repaired chain and Jensen residual proof'),next_work='Prepare independent native273 entire ROOT384385 and383, plus full originalP16.7 without active272 feedback; publish275 whole385386/frozen273 before launch; maxTWO. Native272 continues. Next complete native paper387 free.16solved26OPEN97accepted unchanged; protected editor unchanged.'); write(p,x)
print(json.dumps(dict(paper=386,public_files=len(public),private_records=len(private),private_distinct_blobs=len(copied),public_directory=str(D),binding=str(B),binding_sha256=sha(B),original_closed=False,new_accepted=False),indent=2))
