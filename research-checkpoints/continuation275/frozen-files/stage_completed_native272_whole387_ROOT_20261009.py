from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil
R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-272/P16.7-whole383-intrinsic-E1-and-actual-branch-Dirac'; A=C/'artifacts/codex-hhK319'
D=K/'public-P16.7-continuation387-two-atom-and-nonpluripolar-radial-whole-candidate'
P=R/'primary-data-LOCALONLY/P16.7-native272-whole-primary-and-evidence-20261009'
B=K/'P16.7-round272-whole-candidate387-ROOT-proof-source-scope-and-binding-20261009.json'
J=K/'round272-ROOT-whole-content-identity-audit-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists() and not B.exists()
assert sha(J)=='ea9c92f3c1628bd971cd6de3e385f15764c7645357f6813609bf5b7a82047ae4'
assert sha(A/'proof-companion.md')=='af5de296d5b29031b29c4a18cfee282f751d81f00337fde45dcb8682eb2eaa36'
assert sha(A/'P16.7-independent-paper.tex')=='8714e7f62596a840da1f56eccd0c7f0445c3ac24554653f9c9859bfd7bf4012c'
assert sha(K/'round272-actual-native-final.json')=='5e123c2fc531184ef5572511e2ccaf874b3bdd15dd5b83aff02f2ad92f5a9df4'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
st=load(K/'round272-completed-inspection-LOCALONLY.json')['campaign']; assert st['status']=='completed' and not st['error']
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
actual=load(K/'round272-actual-native-final.json'); expanded=load(A/'expanded-notes.json')
assert not actual['candidate'] and not expanded['candidate'] and len(actual['notes'])==len(expanded['notes'])==5
old=load(C/'private-primary-packet-bindings.json'); context=load(C/'book-context-bindings.json')
assert len(old)==321 and len(context)==17
for e in old+context:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
D.mkdir(); P.mkdir(); blobs=P/'deduplicated-whole-source-DATA'; blobs.mkdir(); private=[]; copied={}
def retain(p,role):
    p=Path(p); digest=sha(p)
    if digest not in copied:
        dst=blobs/(digest+p.suffix); shutil.copyfile(p,dst); assert sha(dst)==digest; copied[digest]=dst
    dst=copied[digest]; private.append(dict(path=str(dst),origin=str(p),bytes=dst.stat().st_size,sha256=digest,LOCALONLY=True,role=role,whole_body_retained=True,correctness_grant=False))
for e in old:retain(e['path'],'Entire frozen primary/evidence DATA, retention is not fresh ROOT physical reading')
for e in context:retain(e['path'],'Entire book context LOCALONLY; no new ROOT whole-context reading claim')
for directory in ['sources-LOCALONLY','inputs-LOCALONLY']:
    for p in sorted((A/directory).rglob('*')):
        if p.is_file():retain(p,'Native272 retained entire primary/reading/input DATA; new source readings attributed native272 unless exact fresh ROOT intervals specified')
retain(A/'reader-emissions.jsonl','Entire native272 source emission record LOCALONLY')
cld=A/'sources-LOCALONLY/004-004-CLD-literal_extract.txt'
assert sha(cld)=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
lines=cld.read_text().split('\n'); fresh=[]
for lo,hi,label in [(6040,6152,'Complete5.2.5statement/immediateproof'),(10505,10590,'Complete8.8.6statement/immediateproof'),(16858,16926,'Complete12.2.7-10statements/immediateproof')]:
    p=P/f'ROOT387-CLDv2-full-LF{lo}-{hi}-LOCALONLY.txt'; p.write_text('\n'.join(lines[lo-1:hi])+'\n')
    fresh.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),inclusive_LF=[lo,hi],ROOT_physically_read_entire_untruncated=True,scope=label,deep_dependency_not_new_whole_proof='12.2.8 cites [50]Theorem3.4; recursive calibration/coherence/analytic foundations not all newly read'))
for name in ['P16.7-independent-paper.tex','P16.7-independent-paper.md','proof-companion.md','expanded-notes.json','source-application-ledger.md','README.md','final-notes.json','actual-final-notes.json','commands.txt']:
    shutil.copyfile(A/name,D/name)
shutil.copyfile(K/'round272-actual-native-final.json',D/'actual-settled-native272-FINAL.json'); shutil.copyfile(J,D/J.name)
for aa,bb in zip(actual['notes'],expanded['notes']):
    (D/(aa['id']+'-actual-settled.md')).write_text(aa['text']+'\n'); shutil.copyfile(A/'notes'/(bb['id']+'.md'),D/(bb['id']+'-expanded.md'))
for name in ['original-task.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','freeze.json','launch-record.json']:
    shutil.copyfile(C/name,D/('frozen-native272-'+name))
reports=D/'reports'; reports.mkdir()
for p in sorted((A/'evidence').iterdir()):
    if p.is_file():shutil.copyfile(p,reports/p.name)
inert=D/'native-programs-INERT-DATA'; inert.mkdir()
for p in sorted(A.glob('*.py')):shutil.copyfile(p,inert/(p.name+'.DATA.txt'))
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,status='UNREVIEWED complete independent native272 draft; original P16.7 OPEN/candidateFALSE; no acceptance/count increase',counts=dict(solved=16,open=26,papers=97),whole_original_solved=False,new_accepted_paper=False,actual_FINAL=dict(path=str(K/'round272-actual-native-final.json'),sha256=sha(K/'round272-actual-native-final.json'),all_five_entire_actual_fields_ROOT_physically_read_untruncated=True,intermediate_messages_excluded=10),ROOT_whole_reading=dict(entire63788character_companion_physically_read=True,overlapping_character_intervals=[[0,18000],[17700,36500],[36200,55000],[54700,63788]],all_five_DIFFERENT_expanded_bodies_exact_within_companion=True,all_five_entire_expanded_outside_fields_physically_read=True,entire11827byte_source_ledger_physically_read_within_companion=True,all_entire_proof_ledger_body_exact_TeX_encoding=True,entire_unique_preamble_physically_read=True,duplicate_identity_not_separate_fresh_reading=True,entire_README_and_scope_and_all_public_reports_except_large_retention_metadata_physically_read=True),scope='Independent383 scoped-positive review under disclosed published foundations, not acceptance. New actual outside atom delta_o, all realN>0 two-atom formula, finite branch equations, exact restricted Dirac dual, discrete-grid intrinsic radial unbounded/nonpluripolar full-mass products, energy/comparison/separated compactness/variations/countable equations. Entire original all-direction and arbitrary-support residual remains OPEN.',primary_reading='Fresh ROOT entire immediate CLDv2 8.8.6,12.2.7-10 and5.2.5 units specified below. New native source readings attributed native272, not new ROOT recursive whole-proof credit. CLD12.2.8 deeper [50]Theorem3.4 not freshly authenticated whole proof. CT/Ducros raw PDFs not retained by native272 because direct retrieval failed; complete applied primary retrieval bodies retained. No new correctness grant.',fresh_ROOT_primary_units=fresh,original_remaining='Full all-direction psh/E1/mixed operators/decreasing continuity/separated compactness/all-obstacle envelopes+orthogonality/fullfirstvariation/fullfinite-energycriterion/EVERYadmissiblearbitrarysupport/fulluniquenessOPEN. Fixed2delta_xi_N0 fulladmissibility/universalsolutionorobstructionUNPROVED. Restrictedbranchcapneveruniversal.',all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,native_audit_and_build_read_AS_DATA_only=True,no_active_math_feedback=True,compiler='Saved standalone uncompiled; built-in request follows without opening a tab. No successful diagnostic/PDF claimed.',protected_editor_OPEN_UNCHANGED=True)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261009.json',qual); write(D/'private-retained-manifest-metadata.json',private)
public=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()]
write(B,dict(recorded_utc=now,round=272,paper=387,atom='P16.7',public_directory=str(D),private_directory=str(P),whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qual,public_files=public,private_primary_evidence_and_book_files=private,fresh_ROOT_primary_units=fresh,private_distinct_full_body_blobs=len(copied)))
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=[],native272_status='COMPLETED actualFINAL/expanded/wholeproof/source/scope ROOT read; whole387 staged UNREVIEWED',native272_whole387=dict(directory=str(D),binding=str(B),binding_sha256=sha(B),candidate=False,status='UNREVIEWED two-atom and nonpluripolar discrete radial theory'),next_work='Prepare independent native273 ENTIRE ROOT384385 and whole387383, then full originalP16.7. Publish275 whole385386387/frozen273 beforelaunch; at mostTWO. No original closure/countincrease; protected editor unchanged. Next full native paper388 free.'); write(p,x)
print(json.dumps(dict(paper=387,public_files=len(public),private_records=len(private),private_distinct_blobs=len(copied),binding=str(B),binding_sha256=sha(B),original_closed=False,new_accepted=False),indent=2))
