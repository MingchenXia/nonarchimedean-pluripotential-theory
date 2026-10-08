from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-266/P02.1-original-arbitrary-classical-psh-real-PL-regularization';A=C/'artifacts/codex-xwbHd2'
D=K/'public-P02.1-continuation375-residue-cardinality-and-extended-logarithmic-series-whole-candidate'
P=R/'primary-data-LOCALONLY/P02.1-native266-whole-primary-and-evidence-20261008'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists()
actual=K/'round266-actual-native-final.json';assert sha(actual)=='f66ebb2d1c4e0a01e48a5cb3837900dcbc7ecabbad059c7141f5dfd1162da318'
notes=load(actual);expanded=load(A/'final-notes.json');assert not notes['candidate'] and not expanded['candidate'] and len(notes['notes'])==len(expanded['notes'])==3
assert notes!=expanded and (A/'actualFINAL.json').read_bytes()==(A/'final-notes.json').read_bytes()
for i,n in enumerate(expanded['notes']):assert (A/'notes'/(n['id']+'.md')).read_text()==n['text']+'\n'
assert sha(A/'P02.1-paper.tex')=='9e40baaa81c9326382668d0c59dedaf7a1f8cee252610033d54ad7eb3c692bbd'
assert sha(C/'original-task.json')=='bd21c27a08559c2f03e7b4b467f706886444fdbefbe8c40813fe49601a41f0cc'
D.mkdir();P.mkdir();shutil.copytree(A/'LOCALONLY',P/'LOCALONLY');shutil.copytree(A/'evidence',P/'evidence')
for name in ['P02.1-paper.tex','P02.1-whole-proof.md','whole-source-application-ledger.md','exact-scope.md','original-scope-noncircularity.md','whole-proof-coverage.md','acceptance-decision.json','final-notes.json','actualFINAL.json']:shutil.copyfile(A/name,D/name)
shutil.copyfile(actual,D/'actual-settled-native266-FINAL.json');shutil.copyfile(C/'original-task.json',D/'original-task.json')
for n in notes['notes']:(D/(n['id']+'-actual-settled.md')).write_text(n['text'])
shutil.copytree(A/'notes',D/'expanded-native-notes-DATA')
Q=D/'native-programs-INERT-DATA';Q.mkdir()
for p in sorted((A/'programs').glob('*.py')):shutil.copyfile(p,Q/(p.name+'.DATA.txt'))
for name in ['formula-checks.json','build-artifacts.json','fresh-primary-extraction.json','additional-primary-hashes.json','environment.json','commands.json','new-source-acquisition.json','input-hash.json','delivery-artifacts.json']:shutil.copyfile(A/'evidence'/name,D/name)
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,status='UNREVIEWED whole partial draft; not an original solution; no new correctness grant',whole_original_solved=False,new_accepted_paper=False,
actual_FINAL=dict(path=str(actual),bytes=actual.stat().st_size,sha256=sha(actual),ALL_three_complete_actual_fields_ROOT_physically_read=True,intermediate_messages_excluded=5),
expanded_variant=dict(path=str(A/'final-notes.json'),sha256=sha(A/'final-notes.json'),DIFFERENT_from_actual_settled_FINAL=True,ALL_three_complete_variant_fields_ROOT_physically_read=True,artifact_named_actualFINAL_is_EXPANDED_variant_not_actual_settled_message=True),
whole_ROOT_reading=dict(entire_TeX=True,entire_whole_proof_companion=True,entire_application_ledger=True,entire_scope_noncircularity_coverage_acceptance=True,bounded_overlapping_chunks=True,untruncated_complete_reads=True),
source_reading=dict(ROOT_fresh_complete_applied_units=['GR classical v2 Definition4.1/full4.1.1-3, entire Proposition4.2/immediate proof and entire Theorem4.3/immediate proof; local LF1125-1221'],native266_claimed_applied_primary_reading='Full immediate units as described in ENTIRE retained ledger; attribution to native266, not new ROOT whole-source reading',ROOT_detected_reading_range_discrepancy='Native ledger says LF1105-1202 includes Theorem4.3, but current source Theorem4.3 starts LF1204 and proof ends LF1221. ROOT freshly repaired reading through LF1270. No theorem or whole physical reading inferred solely from native range receipt.',other_native_source_body_reading_not_ROOT_fresh=True,whole_unused_primary_book_or_recursive_foundations_ROOT_freshly_read=False,full_primary_and_pixels_LOCALONLY=True,private_directory=str(P)),
exact_mathematical_scope=['Every complete NONTRIVIALLY valued K: specified Gauss boundary jump on strict n-polydisc n>=2 has a local continuous approximating SEQUENCE iff residue field countable; decreasing semipositive strict realPL NET exists for every residue field; actual relative boundary and full scalar curve test retained.', 'Given negative analytic logarithmic SERIES with bounded analytic factors and positive real coefficients on good strict X: explicit diagonal decreasing semipositive realPL SEQUENCE including negative infinity; analytic input representation is an extra hypothesis.', 'Native upstairs boundary jump may differ from pulled-back original; explicit completed Gauss-valued extension of Qp with uncountable residue field; formula pullback compatibility not a statement about all new upstairs psh.'],
original_gaps=['No all-functions noncircular geometric characterization of arbitrary classical psh germs','No general boundaryless higher-dimensional classification','Sequence obstruction admits explicit nets and does not obstruct a net interpretation','No general analytic-series representation or normalization/chart gluing descent','No trivial valuation theorem'],
semipositivity='Actual strict Laurent G-cover cut at field values; unit-log PL membership BEFORE authenticated classical/already-realPL comparison; geometric residue/model nefness, not generated/current/smooth/FS definition',
execution='Native arithmetic/extraction/build evidence retained as native observations only; ROOT never executes/imports supplied/native program text; compilation does not establish mathematics',compiler_success_ROOT_confirmed=False,protected_editor_open_unchanged=True,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261008.json',qual)
binding=dict(recorded_utc=now,round=266,paper=375,atom='P02.1',public_directory=str(D),private_directory=str(P),whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qual,public_whole_body_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()],private_retention_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(P.rglob('*')) if p.is_file()])
B=K/'P02.1-round266-whole-candidate375-ROOT-proof-source-scope-and-binding-20261008.json';write(B,binding)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x['native266_complete375']=dict(public_directory=str(D),whole_binding=str(B),whole_binding_sha256=sha(B),actual_FINAL_sha256=sha(actual),candidate=False,original_closed=False,new_accepted_paper=False,independent_whole_reconstruction_pending=True);x['updated_utc']=now;write(p,x)
print(json.dumps(dict(round=266,paper=375,whole_public_files=len(binding['public_whole_body_bindings']),private_retention_files=len(binding['private_retention_bindings']),whole_TeX=dict(bytes=(D/'P02.1-paper.tex').stat().st_size,sha256=sha(D/'P02.1-paper.tex')),whole_proof=dict(bytes=(D/'P02.1-whole-proof.md').stat().st_size,sha256=sha(D/'P02.1-whole-proof.md')),whole_binding_sha256=sha(B),candidate=False,new_accepted_paper=False,solved=16,open=26,papers=97),indent=2))
