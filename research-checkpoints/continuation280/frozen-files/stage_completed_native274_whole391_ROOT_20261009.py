from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil
R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-274/P12.3-whole386-Jensen-completion-and-original-residual'; A=C/'artifacts/codex-gTwO5f'
D=K/'public-P12.3-continuation391-completion-Jensen-and-formal-lift-whole-candidate'
P=R/'primary-data-LOCALONLY/P12.3-native274-whole-primary-and-evidence-20261009'
B=K/'P12.3-round274-whole-candidate391-ROOT-proof-source-scope-and-binding-20261009.json'
J=K/'round274-ROOT-whole-content-identity-audit-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists() and not B.exists()
assert sha(J)=='1229e19ec7a40ddcaabb7e141768d1b12a1da0d7da148a493169db98540f8ad5'
assert sha(K/'round274-actual-native-final.json')=='b0ba56d2c9a57c645f073050b3fb1d63216bfb85e29b7d754c2c7f73c40a6cac'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
st=load(K/'round274-completed-inspection-LOCALONLY.json')['campaign']; assert st['status']=='completed' and not st['error']
actual=load(K/'round274-actual-native-final.json'); expanded=load(A/'native-notes.json')
assert not actual['candidate'] and not expanded['candidate'] and len(actual['notes'])==len(expanded['notes'])==5
old=load(C/'private-primary-packet-bindings.json'); context=load(C/'book-context-bindings.json')
assert len(old)==730 and len(context)==3
for e in old+context:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
D.mkdir(); P.mkdir(); blobs=P/'deduplicated-whole-source-DATA'; blobs.mkdir(); private=[]; copied={}
def retain(p,role):
    p=Path(p); digest=sha(p)
    if digest not in copied:
        dst=blobs/(digest+p.suffix); shutil.copyfile(p,dst); assert sha(dst)==digest; copied[digest]=dst
    dst=copied[digest]; private.append(dict(path=str(dst),origin=str(p),bytes=dst.stat().st_size,sha256=digest,LOCALONLY=True,role=role,whole_body_retained=True,correctness_grant=False))
for e in old:retain(e['path'],'Whole frozen primary/evidence DATA; not fresh ROOT recursive reading')
for e in context:retain(e['path'],'Whole book context LOCALONLY, not newly wholly ROOT read')
for folder in ['sources-LOCALONLY','inputs-LOCALONLY','book-context-LOCALONLY']:
    for p in sorted((A/folder).rglob('*')):
        if p.is_file():retain(p,'Native274 retained entire source/input DATA; native reading not freshly attributed ROOT')
for name in ['P12.3-completion-and-formal-lifting.tex','whole-proof.md','completion-proof.md','independent-review.md','source-application-ledger.md','README.md','native-notes.json','coverage.md','original-residual.md','scope-and-decision.json']:
    shutil.copyfile(A/name,D/name)
shutil.copyfile(K/'round274-actual-native-final.json',D/'actual-settled-native274-FINAL.json'); shutil.copyfile(J,D/J.name)
for aa,ee in zip(actual['notes'],expanded['notes']):
    (D/(aa['id']+'-actual-settled.md')).write_text(aa['text']+'\n'); shutil.copyfile(A/(ee['id']+'.md'),D/(ee['id']+'-expanded.md'))
for name in ['original-task.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json','freeze.json','launch-record.json']:
    shutil.copyfile(C/name,D/('frozen-native274-'+name))
reports=D/'reports'; reports.mkdir()
for p in sorted((A/'reports').iterdir()):
    if p.is_file():shutil.copyfile(p,reports/p.name)
inert=D/'native-programs-INERT-DATA'; inert.mkdir()
for p in sorted(A.glob('*.py')):shutil.copyfile(p,inert/(p.name+'.DATA.txt'))
now=datetime.now(timezone.utc).isoformat(); audit=load(J)
correction=K/'P12.3-G331-existing-completion-and-envelope-transfer-ROOT-scope-correction-20261009.json'
qual=dict(recorded_utc=now,status='UNREVIEWED entire independent native274 draft; original P12.3 OPEN/candidateFALSE; no acceptance/count increase',counts=dict(solved=16,open=26,papers=97),whole_original_solved=False,new_accepted_paper=False,only_incoming_grants=['ENTIRE qualifiedG331','ENTIRE qualifiedB341','ENTIRE qualifiedE350'],actual_FINAL=dict(path=str(K/'round274-actual-native-final.json'),sha256=sha(K/'round274-actual-native-final.json'),all_five_entire_actual_fields_ROOT_physically_read_untruncated=True,intermediate_messages_excluded=8),ROOT_whole_reading=dict(entire43457character_companion_physically_read_untruncated=True,overlapping_character_intervals=audit['character_intervals'],all_five_DIFFERENT_expanded_outside_fields_physically_read=True,expanded_n5_entirely_physically_read=True,entire13801byte_source_ledger_coverage_residual_physically_read=True,entire_body_and_examined386_literal_math_TeX_encoding=True,entire_unique_TeX_segments_physically_read=True,full_qualified_grant_appendices_exact_identity_not_new_fresh_reading=True),completion_novelty_correction=audit['completion_scope_correction'],authoritative_correction_record=dict(path=str(correction),sha256=sha(correction)),scope='Independent whole386 scoped positive judgment, not acceptance. Completion/Jensen corollary transport plus direct full compactHausdorff subprobability Jensen duality. New q-independent formal trace-discriminant compatible Frobenius lift under actual generically separable normalization/perfect coefficient field; completed-diagonal residue coefficient field hypothesis retained.',formal_remaining='Single discriminant can vanish on regular puncture and have infinite support value. Compatible primary multiplier IDEAL and BIG completed-diagonal product/restriction/subadditivity not proved. Generalexcellent isolatedformalcharp CE and generalJensen LHC OPEN.',source_scope='Native274 immediate primary readings attributed native274. ROOT has not newly recursively verified all its historical algebraic/test/duality/resolution dependencies or all3 whole book bodies. Fresh ROOT formal Noether different retrieval is separate and was not native274 input.',all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,native_assemble_delivery_entirely_read_AS_DATA_only=True,compiler='Built-in compilation not verified; no replacement editor or PDF',protected_editor_OPEN_UNCHANGED=True)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261009.json',qual); write(D/'private-retained-manifest-metadata.json',private)
public=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()]
write(B,dict(recorded_utc=now,round=274,paper=391,atom='P12.3',public_directory=str(D),private_directory=str(P),whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qual,public_files=public,private_primary_evidence_and_book_files=private,private_distinct_full_body_blobs=len(copied)))
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,native274_status='COMPLETED actualFINAL/expanded/wholeproof/source/scope ROOT read; whole391 staged UNREVIEWED',native274_whole391=dict(directory=str(D),binding=str(B),binding_sha256=sha(B),candidate=False,status='UNREVIEWED Jensen and formaltrace lift, completionnovelty corrected'),next_work='Native275 generalE1 continues. ROOT formal Noether different primary proof investigation and nextP12.3 campaign; publish280 whole391+275launch. At mostTWO; no originalclosure/countincrease; protected editor unchanged.'); write(p,x)
print(json.dumps(dict(paper=391,public_files=len(public),private_records=len(private),private_distinct_blobs=len(copied),binding=str(B),binding_sha256=sha(B),original_closed=False,new_accepted=False),indent=2))
