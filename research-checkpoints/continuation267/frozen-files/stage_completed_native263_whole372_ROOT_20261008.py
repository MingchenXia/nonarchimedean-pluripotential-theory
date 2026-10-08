from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-263/P21.3-whole369-and-closed-factors367368-independent-completion';A=C/'artifacts/codex-Oa7zxW'
D=K/'public-P21.3-continuation372-middle-cone-repair-and-logarithmic-analytic-trace-removability-whole-candidate'
P=R/'primary-data-LOCALONLY/P21.3-native263-whole-source-ledger-20261008'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists()
actual=K/'round263-actual-native-final.json';assert sha(actual)=='415f6348c94b637046f117fd96643c17dc58e5349cee36d592b4e8b17acb7a0f'
n=load(actual);assert not n['candidate'] and len(n['notes'])==4
assert load(A/'notes.json')==n and load(A/'note-bodies.json')==n
assert (A/'proof-body.md').read_text() in (A/'whole-proof.md').read_text()
original=(C/'original-task.json').read_bytes();assert len(original)==38253 and hashlib.sha256(original).hexdigest()=='154859145d82101f876d3cbd8a8a7e6d472e683bec44cd4f073d46c509a2c811'
assert (A/'original-task-unchanged.json').read_bytes()==original
assert sha(A/'inputs-LOCALONLY/CLD-v2-full.txt')=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
assert sha(A/'inputs-LOCALONLY/CLD-v2.pdf')=='5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719'
ledger=load(A/'source-ledger-independent.json');assert len(ledger['units'])==31 and ledger['source_bodies_LOCALONLY'] and not ledger['whole_CLD_read_claim']
source_lines=(A/'inputs-LOCALONLY/CLD-v2-full.txt').read_text().split('\n');private=[]
for unit in ledger['units']:
 first,last=unit['inclusive_LF_interval'];body='\n'.join(source_lines[first-1:last])+'\n';evidence=A/'inputs-LOCALONLY'/(unit['id']+'.txt')
 assert body.encode()==evidence.read_bytes() and len(body.encode())==unit['literal_source_body_bytes'] and hashlib.sha256(body.encode()).hexdigest()==unit['evidence_sha256'],unit['id']
 private.append(dict(**unit,literal_body=body))
D.mkdir();P.mkdir()
for name in ['P21.3-review-paper.tex','whole-proof.md','proof-body.md','source-ledger-independent.json','independent-whole-review.json','original-decision.json','whole-proof-coverage.json','actual-expanded-comparison.json','checks-output.json','finite-diagnostic.json','environment.json','commands.json','artifact-bindings.json','input-bindings-verified.json']:
 shutil.copyfile(A/name,D/name)
shutil.copyfile(actual,D/'actual-native263-final.json');shutil.copyfile(A/'notes.json',D/'local-notes-SAME-actual-fields-DATA.json')
shutil.copyfile(C/'original-task.json',D/'original-task.json')
for note in n['notes']:(D/(note['id']+'.md')).write_text(note['text'])
Q=D/'native-programs-INERT-DATA';Q.mkdir()
for p in sorted(A.glob('*.py')):shutil.copyfile(p,Q/(p.name+'.DATA.txt'))
for p in sorted((A/'inputs-LOCALONLY').glob('*')):
 if p.is_file() and (p.name in ['CLD-v2-full.txt','CLD-v2.pdf','page80.png','page162.png'] or p.stem in {u['id'] for u in ledger['units']}):shutil.copyfile(p,P/p.name)
write(P/'full-literal-source-ledger-LOCALONLY.json',dict(source_metadata=ledger,units=private,primary_bodies_and_pixels_LOCALONLY=True))
now=datetime.now(timezone.utc).isoformat()
qualification=dict(recorded_utc=now,whole_original_solved=False,new_accepted_paper=False,status='UNREVIEWED whole mathematical draft, candidateFALSE; independent reconstruction pending',actual_FINAL=dict(path=str(actual),sha256=sha(actual),bytes=actual.stat().st_size,notes=4,all_actual_text_fields_equal_local_notes=True,locally_written_serialization_not_actual_NATIVE_message=True),whole_ROOT_reading=dict(whole_proof=True,whole_TeX=True,all_four_actual_FINAL_texts_and_summaries=True,complete_source_application_metadata_in_whole_proof=True,whole_verdicts_scope_coverage=True,bounded_overlapping_chunks=True,truncation_repaired_or_absent=True),source_reading=dict(native263_fresh_complete_applied_units=31,ROOT_fresh_complete_immediate_units=['CLD1.2.6','CLD1.2.11-13 including proofs'],ROOT_other_source_reading='Prior logical-turn readings retained and attributed in old bindings; source retention/hash equality is not new physical reading',ROOT_fresh_PDF_pixel_inspection=False,all_31_literal_units_byte_verified_against_complete_authentic_source=True,whole_primary_and_recursive_foundations_freshly_read=False,private_literal_ledger=str(P/'full-literal-source-ledger-LOCALONLY.json'),private_literal_ledger_sha256=sha(P/'full-literal-source-ledger-LOCALONLY.json'),source_bodies_pixels_LOCALONLY=True),mandatory_repairs_to_prior_working_drafts=dict(ROOT367='Submitted strong-positive domination of arbitrary symmetric complementary tests is false in middle degrees. Complete replacement using middle PSD cone and compact6.5.2 is in whole372; submitted proof unaccepted.',ROOT368='Same strong-cone gap; whole372 independently reconstructs both cross terms, measure uniqueness and exact smooth-limit scopes after repair.',published_source_prints='Native263 reports printed CLD7.2.9 strong-domination and3.3.10 exterior-exponent errors with retained PDF pixels; algebraic replacements proved in whole372. ROOT freshly read cone statements/proofs, not those pixels.'),new_theorem_scope='Continuous h, ordinary smooth zero smooth Hessian off locally Zariski closed analytic Z, and local ordinary smooth harmonic trace g=h on Z. Constructed logarithmic cutoff curvature<=4LM and energy<=24L^2M, actual middle decompositions mass<=C(F+28M); isolated analytic points all p including n-1. Off-locus/trace hypotheses NOT proved for all original equal-curvature differences.',factor_scope='Initial BT for explicit potential class required; actual factor product positive/doubly closed. Every scalar approximant times FIXED T closed; form coefficients in FIXED common charts and SMOOTH limit. Nonclosed weighted torus NOT original counterexample.',residual='Arbitrary individually continuous psh equal-curvature pairs and arbitrary positive doubly closed currents on all original analytic spaces/ordinary opens remain unresolved. No general current density/harmonic lift/CPsh recognition granted.',supplied_programs_and_native_copies_executed_or_imported=False,compiler_success_confirmed=False,protected_editor_open_unchanged=True,other_ACTIVE_mathematics_read_or_supplied=False)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261008.json',qualification)
(D/'README.md').write_text('Whole native263 draft372, UNREVIEWED and original P21.3 unresolved. Four actual FINAL fields agree with locally serialized notes, unlike prior262 actual-versus-expanded differences. Full proofs, source metadata and separate old-proof repair verdicts retained. Primary literal bodies and PDF pixels remain LOCALONLY. Native program copies are inert DATA and have not been executed or imported by ROOT. Compilation not confirmed; no acceptance/count increase. Mandatory ROOT qualification accompanies every future use.\n')
binding=dict(recorded_utc=now,round=263,paper=372,atom='P21.3',public_directory=str(D),private_source_directory=str(P),status=qualification['status'],whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qualification,public_whole_body_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()])
B=K/'P21.3-round263-whole-candidate372-ROOT-proof-source-scope-and-binding-20261008.json';write(B,binding)
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=load(p);assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 x['native263_complete372']=dict(public_directory=str(D),whole_binding=str(B),whole_binding_sha256=sha(B),actual_FINAL_sha256=sha(actual),candidate=False,original_closed=False,new_accepted_paper=False,independent_whole_reconstruction_pending=True,prior367368_strong_cone_step_requires_repair=True);x['updated_utc']=now;write(p,x)
print(json.dumps(dict(round=263,paper=372,whole_public_files=len(binding['public_whole_body_bindings']),whole_TeX=dict(bytes=(D/'P21.3-review-paper.tex').stat().st_size,sha256=sha(D/'P21.3-review-paper.tex')),whole_proof=dict(bytes=(D/'whole-proof.md').stat().st_size,sha256=sha(D/'whole-proof.md')),whole_binding_sha256=sha(B),candidate=False,new_accepted_paper=False,solved=16,open=26,papers=97),indent=2))
