from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil
R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-273/P16.7-whole385387-full-bounded-dual-and-intrinsic-E1'; A=C/'artifacts/codex-Bxz0sA'
D=K/'public-P16.7-continuation390-bounded-dual-and-radial-E1-whole-candidate'
P=R/'primary-data-LOCALONLY/P16.7-native273-whole-primary-and-evidence-20261009'
B=K/'P16.7-round273-whole-candidate390-ROOT-proof-source-scope-and-binding-20261009.json'
J=K/'round273-ROOT-whole-content-identity-audit-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists() and not B.exists()
assert sha(J)=='09c9658d0f4a0b6ee54badc8afe0e8016e75d4520a61c0d26906aff5b5cd601a'
assert sha(K/'round273-actual-native-final.json')=='5c4a45988933d63930e4aa145a5844818c11d45d1822002369b3b8ea397cfb01'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
st=load(K/'round273-completed-inspection-LOCALONLY.json')['campaign']; assert st['status']=='completed' and not st['error']
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
actual=load(K/'round273-actual-native-final.json'); expanded=load(A/'final-notes.json')
assert not actual['candidate'] and not expanded['candidate'] and len(actual['notes'])==len(expanded['notes'])==4
old=load(C/'private-primary-packet-bindings.json'); context=load(C/'book-context-bindings.json')
assert len(old)==557 and len(context)==17
for e in old+context:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
D.mkdir(); P.mkdir(); blobs=P/'deduplicated-whole-source-DATA'; blobs.mkdir(); private=[]; copied={}
def retain(p,role):
    p=Path(p); digest=sha(p)
    if digest not in copied:
        dst=blobs/(digest+p.suffix); shutil.copyfile(p,dst); assert sha(dst)==digest; copied[digest]=dst
    dst=copied[digest]; private.append(dict(path=str(dst),origin=str(p),bytes=dst.stat().st_size,sha256=digest,LOCALONLY=True,role=role,whole_body_retained=True,correctness_grant=False))
for e in old:retain(e['path'],'Whole frozen primary/evidence DATA; retention is not fresh physical reading')
for e in context:retain(e['path'],'Whole book context LOCALONLY; not wholly freshly ROOT read')
for directory in ['sources-LOCALONLY','inputs-LOCALONLY']:
    for p in sorted((A/directory).rglob('*')):
        if p.is_file():retain(p,'Native273 entire source/input DATA; native source reading not newly attributed ROOT')
retain(A/'emissions.jsonl','Whole native273 emission record; emission is not correctness or ROOT reading')
for name in ['P16.7-bounded-dual-paper.tex','proof-companion.md','source-application-ledger.md','README.md','final-notes.json','actual-final-notes.json','commands.txt','scoped-verdict.json','original-verdict.json']:
    shutil.copyfile(A/name,D/name)
shutil.copyfile(K/'round273-actual-native-final.json',D/'actual-settled-native273-FINAL.json'); shutil.copyfile(J,D/J.name)
for aa,ee in zip(actual['notes'],expanded['notes']):
    (D/(aa['id']+'-actual-settled.md')).write_text(aa['text']+'\n'); shutil.copyfile(A/(ee['id']+'.md'),D/(ee['id']+'-expanded.md'))
for name in ['original-task.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','freeze.json','launch-record.json']:
    shutil.copyfile(C/name,D/('frozen-native273-'+name))
reports=D/'reports'; reports.mkdir()
for p in sorted((A/'evidence').iterdir()):
    if p.is_file():shutil.copyfile(p,reports/p.name)
inert=D/'native-programs-INERT-DATA'; inert.mkdir()
for p in sorted(A.glob('*.py')):shutil.copyfile(p,inert/(p.name+'.DATA.txt'))
now=datetime.now(timezone.utc).isoformat(); audit=load(J)
qual=dict(recorded_utc=now,status='UNREVIEWED complete independent native273 draft; original P16.7 OPEN/candidateFALSE; no acceptance/count increase',counts=dict(solved=16,open=26,papers=97),whole_original_solved=False,new_accepted_paper=False,actual_FINAL=dict(path=str(K/'round273-actual-native-final.json'),sha256=sha(K/'round273-actual-native-final.json'),all_four_entire_actual_fields_ROOT_physically_read_untruncated=True,intermediate_messages_excluded=8),ROOT_whole_reading=dict(entire64776character_companion_physically_read=True,overlapping_character_intervals=audit['character_intervals'],all_four_DIFFERENT_expanded_bodies_exact_in_companion=True,all_four_entire_expanded_outside_fields_physically_read=True,entire16600byte_source_ledger_physically_read_in_companion=True,all_entire_proof_ledger_body_exact_TeX_encoding=True,entire_unique_preamble_physically_read=True,duplicate_identity_not_separate_fresh_reading=True),native_version_evidence_correction=audit['correction'],scope='Declared local smooth-approximation bounded class: genuine Green/mixed products/variation/concavity/tangent/comparison. Exact FULL bounded dual1/6+2Z/3 for actual radial measures. Continuous/discrete radial nonpluripolar full mass, equations, energies, comparison, segment variation and radial uniqueness. No original all-direction completion.',class_definition_boundary='Native273 Ctheta means continuous weights locally uniformly approximable by ordinary smooth middle-positive weights. No identification with every stage of smallest continuous-psh sheaf is granted. ROOT388 separately seeks a Hilbert-gradient closure argument for that larger definition; ROOT388/389 were not native273 input and remain UNREVIEWED.',primary_reading='Entire applied source units freshly read by native273 as its ledger specifies; ROOT has not newly recursively read all deeper source proofs or all17 book bodies. Fresh independent ROOT Ducros2012 applied units/pixels/errata are separately recorded and were not fed into native273.',ROOT_fresh_Ducros_record=dict(path=str(K/'P16.7-Ducros2012-local-dimension-ROOT-primary-reading-and-version-scope-20261009.json'),sha256=sha(K/'P16.7-Ducros2012-local-dimension-ROOT-primary-reading-and-version-scope-20261009.json')),original_remaining='Full all-directionE1/product approximation independence/full mass/decreasing continuity/compactness/all analytic obstacle envelopes+orthogonality/full unbounded variation/EVERY admissible arbitrary-support equation/full uniqueness OPEN.2delta_xi_N fulladmissibility/cap unresolved.',all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,native_build_deliverables_and_identity_audit_entirely_read_AS_DATA_only=True,compiler='Built-in compilation not verified; no editor tab opened or replacement PDF compiled.',protected_editor_OPEN_UNCHANGED=True)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261009.json',qual); write(D/'private-retained-manifest-metadata.json',private)
public=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()]
write(B,dict(recorded_utc=now,round=273,paper=390,atom='P16.7',public_directory=str(D),private_directory=str(P),whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qual,public_files=public,private_primary_evidence_and_book_files=private,private_distinct_full_body_blobs=len(copied)))
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=[],native273_status='COMPLETED actualFINAL/expanded/wholeproof/source/scope ROOT read; whole390 staged UNREVIEWED',native273_whole390=dict(directory=str(D),binding=str(B),binding_sha256=sha(B),candidate=False,status='UNREVIEWED bounded dual and continuous/discrete radial theory'),native274_status='COMPLETED exact actualFINAL captured; whole review pending',next_work='Freeze native275 entire390+ROOT388389+fresh Ducros source reading for independent bounded class/energy and all-direction E1 operator review. Publish279 beforelaunch, at mostTWO. Whole native274 reading next; no originalclosure/countincrease; protected editor unchanged.'); write(p,x)
print(json.dumps(dict(paper=390,public_files=len(public),private_records=len(private),private_distinct_blobs=len(copied),binding=str(B),binding_sha256=sha(B),original_closed=False,new_accepted=False),indent=2))
