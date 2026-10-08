from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil

R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-269/P12.3-whole377-isolated-positive-characteristic-and-original-envelopes'
A=C/'artifacts/codex-UtgXD8'
D=K/'public-P12.3-continuation382-isolated-perfect-charp-and-nonisolated-finite-cover-whole-candidate'
P=R/'primary-data-LOCALONLY/P12.3-native269-whole-primary-and-evidence-20261008'
B=K/'P12.3-round269-whole-candidate382-ROOT-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists() and not B.exists()
actual=K/'round269-actual-native-final.json'
assert sha(actual)=='dca9e7382066cce6b1667e9436d2de3df81869d5d83ab24011ae0f8003012791'
j=load(actual); e=load(A/'native-notes.json')
assert not j['candidate'] and not e['candidate'] and len(j['notes'])==len(e['notes'])==9
proof=(A/'whole-proof.md').read_text(); tex=(A/'P12.3-paper.tex').read_text()
assert len(proof)==57471
comparisons=[]
for x,y in zip(j['notes'],e['notes']):
    assert x['id']==y['id'] and x['text']!=y['text']
    assert y['text'] in proof and (A/(y['id']+'.md')).read_text()==y['text']
    comparisons.append(dict(id=x['id'],actual_text_sha256=hashlib.sha256(x['text'].encode()).hexdigest(),expanded_text_sha256=hashlib.sha256(y['text'].encode()).hexdigest(),actual_DIFFERS_expanded=True,expanded_entire_literal_proof_substring=True))
assert (A/'comparison-376.md').read_text()==e['notes'][6]['text']+'\n\n'+e['notes'][7]['text']
extras=['source-application-ledger.md','exact-scope.md','whole-proof-coverage.md']
expected_bodies=[n['text'] for n in e['notes']]+[(A/n).read_text() for n in extras]
assert re.findall(r'\\begin\{OwnProofBody\}\n(.*?)\n\\end\{OwnProofBody\}',tex,re.S)==expected_bodies
grants=load(C/'input.json')['notes']; assert [n['id'] for n in grants]==['G331','B341','E350']
grant_bodies=[(A/'qualified-grants'/f"{n['id']}.txt").read_text() for n in grants]
assert grant_bodies==[n['text'] for n in grants]
assert re.findall(r'\\begin\{QualifiedBody\}\n(.*?)\n\\end\{QualifiedBody\}',tex,re.S)==grant_bodies
paper=proof+''.join('\n\n'+(A/n).read_text() for n in extras)
for n,body in zip(grants,grant_bodies):paper+='\n\n# Entire qualified incoming grant '+n['id']+'\n\n'+body
assert (A/'P12.3-paper.md').read_text()==paper
repairs=load(A/'reports/HLS-capture-repairs.json')
fullsrc=R/'primary-data-LOCALONLY/P12.3-singular-test-ideal-generation-primary-20261008/HLS-mixed-characteristic-generation-published2024.txt'
source=fullsrc.read_text()
for u in repairs:
    p=A/u['file']; assert p.stat().st_size==u['bytes'] and sha(p)==u['sha256'] and p.read_text() in source
assert sha(fullsrc)=='51d8347d5515f57ef1457ea8fa55220d899c5d6cbb6377516fbb4b110a030a88'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
D.mkdir(); P.mkdir()
shutil.copytree(A/'inputs',P/'native-inputs'); shutil.copytree(A/'evidence',P/'native-evidence')
for name in ['P12.3-paper.md','P12.3-paper.tex','whole-proof.md','comparison-376.md','native-notes.json','source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','original-verdict.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
    shutil.copyfile(A/name,D/name)
shutil.copytree(A/'reports',D/'reports'); shutil.copytree(A/'qualified-grants',D/'qualified-grants')
shutil.copyfile(actual,D/'actual-settled-native269-FINAL.json'); shutil.copyfile(C/'original-task.json',D/'original-task.json')
for n in j['notes']:(D/(n['id']+'-actual-settled.md')).write_text(n['text'])
for n in e['notes']:shutil.copyfile(A/(n['id']+'.md'),D/(n['id']+'-expanded.md'))
Q=D/'native-programs-INERT-DATA'; Q.mkdir()
for p in sorted(A.glob('*.py')):shutil.copyfile(p,Q/(p.name+'.DATA.txt'))
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,status='UNREVIEWED complete independent native269 reconstruction; whole original P12.3 OPEN, candidateFALSE. No new accepted paper.',counts=dict(solved=16,open=26,papers=97),whole_original_solved=False,new_accepted_paper=False,
    actual_FINAL=dict(path=str(actual),sha256=sha(actual),all_nine_complete_actual_fields_ROOT_physically_read=True,intermediate_messages_excluded=8),actual_expanded_comparisons=comparisons,
    ROOT_whole_reading=dict(entire_57471_character_proof_ROOT_physically_read=True,untruncated_overlapping_intervals=[[0,19000],[18600,38000],[37600,57471]],all_nine_expanded_bodies_physically_read_within_proof=True,all_expanded_outside_fields_ROOT_read=True,entire_source_application_ledger_scope_coverage_verdict_environment_and_final_audit_ROOT_read=True,comparison376_exact_entire_read_expanded_n7_and_n8=True,TeX_preamble_ROOT_physically_read=True,entire633002byteTeX_own_proof_blocks_exact_read_nine_notes_ledger_scope_coverage=True,entire630608byteMD_exact_read_proof_ledger_scope_coverage_plus_three_qualified_grants=True,all_three_entire_qualified_grants_exact_incoming_note_texts_in_both_formats=True,duplicate_content_identity_NOT_new_fresh_physical_reading=True),
    new_claims='Normal isolated AFFINE finite-type CLOSED codimension>=2 perfect-charp all-support CE with no resolution/smooth-model requirement. Full relative Koszul generation, actual canonical Fitting flattening and primary graph, scheme-global arbitrary-tail big-test trace and corrected Jacobian subadditivity. New actual finite nonflat degree-two cover extends nonisolated quadratic-cone examples to every perfect charp including purely inseparable char2. Independent whole376 reconstruction with all original scopes.',
    source_capture_correction=dict(previous_ROOT377_literal_units_13_and_14_are_INCOMPLETE=True,previous_completeness_and_full_7_5_or_whole_Section8_reading_labels_superseded_by_this_exact_correction=True,missing_tails='7.5(f) basepoint-free-divisor sum; Conjecture8.4 and Question8.5',full_repaired_units_ROOT_now_physically_read_untruncated=True,repair_metadata=repairs,full_primary_text_path=str(fullsrc),full_primary_text_sha256=sha(fullsrc),all_repaired_full_units_LOCALONLY=True,frozen377_and269_not_rewritten=True),
    source_reading='Other new primary reading, including a fresh Smolkin page11 image, is attributed native269, not inferred ROOT fresh reading. Prior qualified grant and ROOT reading scopes retained exactly; no full BS/HH02/threefold book reading asserted. HH02 infinite-field normalization, Kunz/test-elements, coherent cohomology, Serre, Hartogs and historical surface/multiplier foundations explicitly disclosed. ROOT380/381 are separate new proofs, not in native269 frozen input.',
    original_remaining='General normal excellent dimension>=3, arbitrary nonisolated/imperfect/mixed/nonalgebraic/nonclosed scope and char0 infinite-Q supports unresolved. No authentic normal envelope counterexample. Failed nonprimary bound is not a counterexample; actual quadratic example instead has conditional scoped CE.',
    supplied_or_native_programs_executed_or_imported=False,all_native_programs_retained_as_inert_DATA=True,finite_diagnostics_not_analytic_proof=True,all_full_primary_bodies_literal_units_and_pixels_LOCALONLY=True,no_active270_mathematics_read_or_feedback=True,
    compiler='Standalone saved source retained; built-in check follows staging. No successful compilation, PDF, export, install or editor tab claimed.',protected_editor_open_unchanged=True)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261008.json',qual)
(D/'README.md').write_text('Whole candidate382, P12.3\n\nUNREVIEWED complete independent native269 reconstruction. Original P12.3 remains OPEN; candidateFALSE. Counts16/42 solved,26 OPEN,97 accepted papers unchanged. The isolated normal affine perfect-charp CLOSED-point all-support envelope theorem and actual nonisolated quadratic finite-cover family are scoped draft claims requiring independent review. Full9 distinct actual FINAL and expanded bodies, entire proof, source/scope qualifications and incoming whole grants retained.\n\nTwo prior ROOT377 HLS captures were incomplete. The complete repaired units are now physically ROOT read; exact correction metadata is public, full primary bodies remain LOCALONLY. No repeated-body hash is a fresh reading receipt. Historical HH02/cohomological/surface/multiplier foundations are disclosed. Native programs inert DATA, never executed/imported. Compiler success unverified; protected editor unchanged.\n')
binding=dict(recorded_utc=now,round=269,paper=382,atom='P12.3',public_directory=str(D),private_directory=str(P),whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qual,public_whole_body_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()],private_retention_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(P.rglob('*')) if p.is_file()]); write(B,binding)
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x['native269_complete382']=dict(public_directory=str(D),whole_binding=str(B),whole_binding_sha256=sha(B),actual_FINAL_sha256=sha(actual),candidate=False,original_closed=False,new_accepted_paper=False,previous_ROOT377_HLS_capture_completeness_corrected=True); x['updated_utc']=now; write(p,x)
print(json.dumps(dict(round=269,paper=382,public_files=len(binding['public_whole_body_bindings']),private_files=len(binding['private_retention_bindings']),whole_TeX_sha256=sha(D/'P12.3-paper.tex'),whole_proof_sha256=sha(D/'whole-proof.md'),binding_sha256=sha(B),candidate=False,solved=16,open=26,papers=97),indent=2))
