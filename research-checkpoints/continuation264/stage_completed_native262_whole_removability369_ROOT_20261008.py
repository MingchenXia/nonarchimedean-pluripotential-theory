from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-262/P21.3-entire-original-arbitrary-current'
A=C/'artifacts/codex-uZFDii'
D=K/'public-P21.3-continuation369-arbitrary-current-cutoff-and-analytic-locus-removability-whole-candidate'
B=K/'P21.3-round262-whole-candidate369-ROOT-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def bound(p):
 p=Path(p);return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
assert not D.exists() and not B.exists()
assert sha(K/'round262-actual-native-final.json')=='49b00d775106e0878d30573db2282ca2b280b9e648e0ac9684fce1326b8ec308'
assert sha(A/'whole-proof.md')=='8b0df8bc3e27a55502ba8f6c7f1793466b9454e879c091bf409492977dbcd421'
assert sha(A/'P21.3-paper.tex')=='45d03fe2ebb247496c2b83780a2921d2d2396b1f98d1fa5c6280e38cda2dcd2f'
assert sha(C/'original-task.json')=='154859145d82101f876d3cbd8a8a7e6d472e683bec44cd4f073d46c509a2c811'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
j=load(K/'round262-completed-inspection-LOCALONLY.json');assert j['campaign']['status']=='completed' and not j['campaign']['error']
actual=load(K/'round262-actual-native-final.json');expanded=load(A/'notes.json')
assert not actual['candidate'] and not expanded['candidate'] and len(actual['notes'])==len(expanded['notes'])==3
assert (A/'notes.json').read_bytes()==(A/'native-notes.json').read_bytes()
comparison=[dict(id=a['id'],actual_text_equals_expanded=a['text']==e['text']) for a,e in zip(actual['notes'],expanded['notes'])]
assert all(not e['actual_text_equals_expanded'] for e in comparison)
ledger=load(A/'whole-source-application-ledger.json');primary=C/'private-primary-DATA-LOCALONLY/31-cld-v2-full.txt'
assert sha(primary)==ledger['primary_text_sha256']=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
lines=primary.read_text().split('\n');evidence=[];public_units=[]
for u in ledger['application_units']:
 start,end=u['inclusive_LF_interval'];body='\n'.join(lines[start-1:end])+'\n'
 assert body==u['literal_complete_immediate_unit']
 assert hashlib.sha256(body.encode()).hexdigest()==u['evidence_sha256']
 v={k:x for k,x in u.items() if k!='literal_complete_immediate_unit'}
 v.update(literal_source_body_LOCALONLY=True,literal_source_body_bytes=len(body.encode()))
 public_units.append(v);evidence.append(dict(id=u['id'],exact_LF_primary_evidence_verified=True,evidence_sha256=u['evidence_sha256']))
assert len(public_units)==16
D.mkdir();(D/'native-programs-DATA').mkdir()
for name in ['whole-proof.md','P21.3-paper.tex','whole-proof-coverage.json','exact-scope.json','original-scope-and-noncircularity-decision.json','decision-evidence.json',
 'whole-source-application-ledger.md','section-bindings.json','checks-output.json','environment.json','commands.json','native-note-bindings.json']:
 shutil.copyfile(A/name,D/name)
shutil.copytree(A/'sections',D/'sections')
shutil.copyfile(K/'round262-actual-native-final.json',D/'actual-native262-final.json')
shutil.copyfile(A/'notes.json',D/'expanded-local-notes-DATA.json')
shutil.copyfile(C/'original-task.json',D/'original-task.json')
for name in ['reproduce.py','make_notes.py']:shutil.copyfile(A/name,D/'native-programs-DATA'/f'{name}.DATA.txt')
private=K/'P21.3-continuation369-native262-full-source-ledger-LOCALONLY.json';assert not private.exists()
shutil.copyfile(A/'whole-source-application-ledger.json',private)
public={k:v for k,v in ledger.items() if k!='application_units'}
public.update(application_units=public_units,whole_literal_primary_unit_ledger_LOCALONLY=bound(private),
 public_ledger_qualification='Every native-authored source application, hypothesis, exact version/path/LF interval and evidence hash retained. Only literal complete primary-source bodies are LOCALONLY; metadata is not a theorem grant.')
write(D/'whole-source-application-ledger.json',public)
now=datetime.now(timezone.utc).isoformat()
qualification=dict(recorded_utc=now,status='ENTIRE native262 candidateFALSE manuscript; UNREVIEWED, independent reconstruction pending',
 actual_native_FINAL=bound(D/'actual-native262-final.json'),expanded_local_DATA=bound(D/'expanded-local-notes-DATA.json'),actual_vs_expanded_field_comparison=comparison,
 mandatory='All THREE actual settled native262 text fields DIFFER from expanded local notes. Both ENTIRE bodies were read by ROOT, with complete manuscript/whole-proof/source application metadata/scope/coverage/decisions. Expanded local notes are DATA, not the actual FINAL. Native checks/candidate labels are not mathematical grants.',
 whole_standalone_paper=bound(D/'P21.3-paper.tex'),whole_proof=bound(D/'whole-proof.md'),whole_source_ledger=bound(D/'whole-source-application-ledger.json'),private_literal_source_ledger=bound(private),
 ROOT_physically_read='Entire actual FINAL all3fields; expanded local notes all3fields; whole29136byteproof in overlapping0:15900/15400:end; entire30246byteTex in overlapping0:16000/15400:end; whole15742byteown source-application MD and all16JSON application metadata/alltopfields; fullscope/coverage/originaldecision/evidence/checks.',
 ROOT_fresh_primary_immediate_units=['CLD6.5.1--3 incl complete6.5.2 proof','CLD15.2.1--9 whole statements/proofs'],
 retained_prior_ROOT_primary_units=['CLD6.2.1--9','CLD7.2.9--12 and7.3.1','CLD7.7.1--8','CLD15.7.1--2'],
 remaining_native_source_reading_attribution='Other full immediate source units were read by native262 as reported; ROOT metadata/hash verification is NOT fresh physical reading of all primary bodies. Future independent reconstruction receives ENTIRE bound sources and must check all applied immediate statements/proofs.',
 current_degree='T bidegree(p,p), q=n-p; differentiated defect tests(r,r), r=n-p-1. Full original p0...n-1; at top p=n-1, dimensional bound excludes no nonempty locus.',
 exact_partial_scope='Original arbitrary positive doubly closed current, both valuations/singularities/nilpotents/all actual integration weights. EXTRA ordinary off-locus smooth zero-Hessian hypothesis, plus explicit weighted cutoff vanishing or dimZ<n-p-1. No universal regularity/cutoff bound or original solution/counterexample.',
 source_repairs='Exact LF extraction uses split on LF, preserves formfeeds. MisindexedCLD8.5.3 not imported. Source3.3.6 proof dk typo vsdtrop and1.10.2 final composition typo disclosed bynative; no extrapolation.',
 original_closed=False,new_accepted_paper=False,formal_solved=16,formal_OPEN=26,accepted_papers=97,compiler_success=False,formal_verification=False,
 source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,primary_bodies_pixels_LOCALONLY=True,protected_editor_open_unchanged=True)
Q=D/'mandatory-actual-source-scope-and-reader-qualifications-ROOT-20261008.json';write(Q,qualification)
write(B,dict(recorded_utc=now,whole_candidate_directory=str(D),whole_paper=bound(D/'P21.3-paper.tex'),whole_proof=bound(D/'whole-proof.md'),actual_FINAL=bound(D/'actual-native262-final.json'),
 whole_source_ledger=bound(D/'whole-source-application-ledger.json'),mandatory_annotation=bound(Q),actual_vs_expanded=comparison,
 complete_primary_evidence_bindings=evidence,ROOT_reading_qualification=qualification['ROOT_physically_read'],status='UNREVIEWED; no correctness grant; whole original remainsOPEN'))
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=load(p);assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 x.update(updated_utc=now,current_active_batch=[261],native262_complete369=dict(whole_candidate_directory=str(D),whole_binding=bound(B),actual_FINAL=bound(D/'actual-native262-final.json'),
 candidate=False,original_closed=False,new_accepted_paper=False,independent_reconstruction_pending=True))
 write(p,x)
print(json.dumps(dict(whole_candidate=str(D),whole_paper=bound(D/'P21.3-paper.tex'),whole_proof=bound(D/'whole-proof.md'),source_units_exactly_bound=len(evidence),
 all3actual_texts_DIFFER_from_expanded=True,active=[261],formal_solved=16,formal_OPEN=26,accepted_papers=97),indent=2))
