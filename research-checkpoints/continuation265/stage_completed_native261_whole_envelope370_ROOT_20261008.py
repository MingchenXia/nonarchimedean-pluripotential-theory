from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-261/P12.3-whole365-finite-correction364'
A=C/'artifacts/codex-B0KVpm'
D=K/'public-P12.3-continuation370-whole-envelope-and-general-normal-finite-correction-candidate'
B=K/'P12.3-round261-whole-candidate370-ROOT-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def bound(p):return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
assert not D.exists() and not B.exists()
assert sha(K/'round261-actual-native-final.json')=='59a5a6f1d825cc2bfee89203a69c25d1b20e1b8871d589a325237fcc04bd20b2'
assert sha(C/'input.json')=='97300abd6014232e0bbbef0097df9c7337ac2f5a1e8163a58571f2a97b794493'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
j=load(K/'round261-completed-inspection-LOCALONLY.json');assert j['campaign']['status']=='completed' and not j['campaign']['error']
actual=load(K/'round261-actual-native-final.json');expanded=load(A/'native-notes.json');local_actual=load(A/'actual-FINAL.json')
assert not actual['candidate'] and not expanded['candidate'] and len(actual['notes'])==len(expanded['notes'])==14
comparisons=[];coverage=[];w=(A/'whole-proof.md').read_text();md=(A/'P12.3-paper.md').read_text();tex=(A/'P12.3-paper.tex').read_text()
for a,e,l in zip(actual['notes'],expanded['notes'],local_actual['notes']):
 assert a['id']==e['id']==l['id'] and a['text']==l['text'] and a['text']!=e['text']
 comparisons.append(dict(id=a['id'],actual_text_equals_local_actual=True,actual_text_equals_expanded=False,actual_text_bytes=len(a['text'].encode()),expanded_text_bytes=len(e['text'].encode())))
 n=(A/(e['id']+'.md')).read_text();assert e['text'] in n and e['text'] in w and e['text'] in md
 coverage.append(dict(id=e['id'],expanded_entire_body_exactly_present_in_whole_ROOT_read_proof=True,whole_note_file_heading_and_outside_body_read=True,whole_expanded_summary_detailedSummary_support_read=True,duplicate_retention_is_not_fresh_physical_reading=True))
decision=load(A/'acceptance-decision.json');assert decision['candidate'] is False
D.mkdir();(D/'native-programs-DATA').mkdir();(D/'reports-DATA').mkdir()
for name in ['P12.3-paper.tex','P12.3-paper.md','whole-proof.md','whole-source-application-ledger.md','whole-proof-coverage.md','exact-scope.md','original-scope-and-noncircularity.md','acceptance-decision.json','README.md','diagnostic-inputs.json','diagnostic-output.json']:
 shutil.copyfile(A/name,D/name)
for i in range(1,15):shutil.copyfile(A/f'n{i}.md',D/f'n{i}.md')
shutil.copyfile(K/'round261-actual-native-final.json',D/'actual-native261-final.json')
shutil.copyfile(A/'actual-FINAL.json',D/'local-actual-FINAL-DATA.json')
shutil.copyfile(A/'native-notes.json',D/'expanded-native-notes-DATA.json')
shutil.copyfile(C/'original-task.json',D/'original-task.json')
for p in sorted(A.glob('*.py')):shutil.copyfile(p,D/'native-programs-DATA'/(p.name+'.DATA.txt'))
for name in ['duplicate-coverage.json','environment.json','final-audit.json','own-artifact-hashes.json','rerun-commands.json']:
 shutil.copyfile(A/'reports'/name,D/'reports-DATA'/name)
now=datetime.now(timezone.utc).isoformat()
Q=D/'mandatory-actual-source-scope-and-reader-qualifications-ROOT-20261008.json'
qualification=dict(recorded_utc=now,status='ENTIRE native261 candidateFALSE standalone mathematical draft; original OPEN; UNREVIEWED pending further independent reconstruction',
 actual_native_FINAL=bound(D/'actual-native261-final.json'),expanded_native_DATA=bound(D/'expanded-native-notes-DATA.json'),local_actual_DATA=bound(D/'local-actual-FINAL-DATA.json'),actual_vs_expanded_field_comparison=comparisons,
 ROOT_entire_mathematical_reading='All14 actual text fields fully read before continuation; whole68431byteproof in overlapping0:15700/15300:30800/30400:46000/45600:61200/60800:end; entire70730byteTex in overlapping0:16400/16000:32600/32200:48800/48400:64500/64100:end. Whole own source ledger/scope/coverage/originaldecision read; all14 expanded text bodies exactly occur in that physically ROOT-read whole proof, and every expanded summary/detailedSummary/support plus separate file heading/outside body read. Duplicate byte coverage proves retention, not an additional fresh proof/source reading.',
 expanded_duplicate_coverage=coverage,
 only_existing_qualified_grants=['ENTIRE G331 with all mandatory source/model/actual-Cartier/Keeler erratum/SH quotient-colon/zero/curve/smoothCLOSED/gauge/support qualifications','ENTIRE B341 with full bounded moments and actual curve-reference scope','ENTIRE E350 with existing specified-D limit/support/Borel/capacity/energy/sign/truncation/net/gauge/source qualifications'],
 mandatory_source_attribution='Fresh whole current Stacks/BdFF/BFJ immediate statement/proof and BdFF four page-image readings are reported by native261. ROOT read ENTIRE own application ledger and all manuscript proofs; ROOT retained prior source readings including general BdFF units from ROOT363/364, but hash/metadata/duplicate checks do NOT constitute fresh whole primary/PDF reading. Future independent reconstruction receives full immutable source packets and must independently verify all applied immediate statements/proofs; recursive foundations remain published background.',
 source_scope=['Current Stacks0BGJ/0BGP condition4 normal completions; full actual possibly nonreduced connected fibre0AY8/0B5Y/0D2N/0B5S; supported divisor cycles0AYA before Chow','THREE-author BdFF Duke2012 generalSections1--3/3.17; isolatedSection4/4.11 never applied to general nonisolated germ; source-nef fixed-zero-base-trace direction is core/C to source ONLY','BFJ smooth AFFINE CLOSED point over algclosed characteristic-zero field, closed faces/all retractions and ENTIRE3.18/3.22 estimate; no arbitrary-characteristic or singular retraction theorem','Current SH17.4.7 uses finite quotient by eventual annihilator, not literal unquotiented colon; Keeler v5 entire erratum retained in qualified G331'],
 exact_partial_scope='All excellent NORMAL surfaces all fields/characteristics; exact smooth and isolated normal CLOSED algebraic algclosedchar0 CE; normal targets of ACTUAL finite reduced EVERY-minimal-component-dominating CE covers; full reduced normalization envelope for finite continuous obstacles ONLY when ALL actual normal centres have CE, positive iff full-fibre constancy; direct all excellent reduced curves. General normal CLOSED algebraic algclosedchar0 dim>=2 continuity of GLOBAL finite-continuous raw envelope on OPEN{v(Q)<infinity}, Q=d(K)Jac, via general3.17 and actual primary truncation, with all supports.',
 remaining_original='No global continuity or geometric positivity proved on CLOSED{v(Q)=infinity} outside isolated/proved actual CE-cover sectors. Higherdim positive/mixed-characteristic and arbitrary excellent/nonalgebraic/nonclosed normal residual remains. No NORMAL counterexample, no unproved universal smooth cover, source-nef converse, increasing-limit positivity or pole normalization formula. Failure of error bound not CE failure.',
 finite_diagnostics='Only the enumerated98matrices1154principal43210quadratic392smooth48parity484MAXcases reported by native; no universal mathematical certificate and supplied programs never executed/imported by ROOT.',
 original_closed=False,new_accepted_paper=False,formal_solved=16,formal_OPEN=26,accepted_papers=97,compiler_success=False,formal_verification=False,
 source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,primary_bodies_pixels_LOCALONLY=True,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_open_unchanged=True)
write(Q,qualification)
write(B,dict(recorded_utc=now,whole_candidate_directory=str(D),whole_standalone_tex=bound(D/'P12.3-paper.tex'),whole_standalone_markdown_and_qualified_grants=bound(D/'P12.3-paper.md'),whole_proof=bound(D/'whole-proof.md'),actual_FINAL=bound(D/'actual-native261-final.json'),whole_source_application_ledger=bound(D/'whole-source-application-ledger.md'),mandatory_annotation=bound(Q),actual_vs_expanded=comparisons,status='UNREVIEWED whole draft; ZERO new correctness grant; original remainsOPEN'))
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=load(p);assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 x.update(updated_utc=now,native261_complete370=dict(whole_candidate_directory=str(D),whole_binding=bound(B),actual_FINAL=bound(D/'actual-native261-final.json'),candidate=False,original_closed=False,new_accepted_paper=False,independent_reconstruction_pending=True));write(p,x)
print(json.dumps(dict(whole_candidate=str(D),whole_paper=bound(D/'P12.3-paper.tex'),whole_proof=bound(D/'whole-proof.md'),all14actual_texts_DIFFER_from_expanded=True,all14actual_texts_EQUAL_local_actual=True,whole_expanded_body_coverage_verified=True,formal_solved=16,formal_OPEN=26,accepted_papers=97),indent=2))
