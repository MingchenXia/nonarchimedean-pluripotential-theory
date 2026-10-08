from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-239').iterdir());A=C/'artifacts/codex-hcfWTS'
D=K/'public-P05.2-continuation332-carrier-tree-primitive-polynomial-whole-original-candidate'
B=K/'round239-whole-candidate-ROOT-reading-and-independent-review-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not B.exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256')]:assert sha(C/name)==f[key]
own=json.loads((A/'own-bindings.json').read_text())['files'];assert len(own)==33
for e in own:
    p=Path(e['path']).resolve();assert p.is_relative_to(A.resolve()) and p.stat().st_size==e['bytes'] and sha(p)==e['sha256']
frozen=[]
for name in ('mathematical-packet-bindings.json','private-primary-packet-bindings.json'):
    for e in json.loads((C/name).read_text()):assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256'];frozen.append(e)
assert len(frozen)==43
inp=json.loads((C/'input.json').read_text());native_inp=json.loads((A/'input.json').read_text());assert inp['task']==native_inp['task'] and inp['notes']==native_inp['notes']
ib=json.loads((A/'input-bindings.json').read_text())
for e in [ib[k]for k in ('initial_input','original','packet_manifest','primary_manifest')]+ib['immutable_streams']:assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
assert len(ib['immutable_streams'])==43
for n,e,q in zip(inp['notes'],ib['qualified_note_texts'],json.loads((C/'qualified-imported-note-bindings.json').read_text())):
    assert n['id']==e['id']==q['id'] and len(n['text'].encode())==e['text_bytes']==q['text_bytes'] and hashlib.sha256(n['text'].encode()).hexdigest()==e['text_sha256']==q['text_sha256']
assert len(inp['notes'])==8
actual_path=K/'round239-actual-native-final.json';actual=json.loads(actual_path.read_text());saved=json.loads((A/'native-notes.json').read_text());assert actual==saved and actual['candidate'] is True and len(actual['notes'])==5
known={n['id']for n in inp['notes']}
for n in actual['notes']:assert all(s in known for s in n['support']) and n['id'] not in known;known.add(n['id'])
assert (A/'P05.2-paper.tex').read_bytes().count(b'\n')==343
assert sha(A/'P05.2-paper.tex')=='d6fbbffcaaa533a425524e9b582e2c7eb1712cfbe63d3e8fbe745c3108a3b896' and sha(A/'P05.2-paper.pdf')=='b7ce4fe7d6c3860c0a6b211e25cd3bdf137baa6ea0c942f1431e302d13a62a08'
pages=next(int(s.split(':',1)[1].strip())for s in subprocess.run(['pdfinfo',str(A/'P05.2-paper.pdf')],capture_output=True,text=True,check=True).stdout.splitlines()if s.startswith('Pages:'));assert pages==14
now=datetime.now(timezone.utc).isoformat()
write(B,dict(recorded_utc=now,round=239,role_status='completed',author_candidate=True,actual_FINAL_path=str(actual_path),actual_FINAL_sha256=sha(actual_path),whole_five_actual_notes_all_fields_ROOT_read=True,note_display_groups=['n1,n2','n3,n4,n5'],whole_authoritative_paper_ROOT_read=True,paper_display_ranges=['1-85','86-170','171-255','256-350'],paper_LF_lines=343,paper_source_sha256=sha(A/'P05.2-paper.tex'),pdf_sha256=sha(A/'P05.2-paper.pdf'),pdf_pages=14,whole_source_ledger_exact_scope_coverage_decision_ROOT_read=True,whole_original_statement_family_dossier_completionCriteria_ROOT_read=True,original_problem_display_character_ranges=['0:19000','19000:38000','38000:end'],parallel_argument_separately_whole_ROOT_read_not_claimed=True,own_artifact_hashes_verified=33,frozen_math_primary_hashes_verified=43,input_reported_streams_plus_controls_hashes_verified=47,all_eight_qualified_note_texts_verified=True,controller_and_native_task_and_notes_exactly_equal=True,controller_and_native_assignment_and_bytes_differ=True,all_saved_actual_note_fields_and_candidate_equal=True,saved_actual_serialization_bytes_distinct=True,supplied_programs_not_executed_or_imported=True,ROOT328_not_frozen_or_supplied_to_author239=True,infinite_structural_criterion_meaningfulness_independent_review_pending=True,new_accepted_paper=False,original_closed=False))
D.mkdir();E=D/'evidence';E.mkdir()
for name in ('P05.2-paper.tex','P05.2-paper.pdf','argument.md','native-notes.json','source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','original-scope-and-noncircularity-decision.md'):shutil.copyfile(A/name,D/name)
for name in ('own-bindings.json','input-bindings.json','build-bindings.json','build-results.json','build-run-1-results.json','initial-diagnostics.md','environment.json','check-input.json','check-output.json','commands.json','build-run-1-stage-1.log','build-run-1-stage-2.log','build-run-1-stage-3.log','build-run-1-stage-4.log','build-run-1-stage-5.log'):shutil.copyfile(A/name,E/name)
for p in (B,actual_path):shutil.copyfile(p,E/p.name)
write(D/'ROOT-public-candidate-status-20261008.json',dict(recorded_utc=now,continuation=332,native_round=239,author_candidate=True,status='UNREVIEWED whole-original P05.2 solution candidate; original remains OPEN',whole_ROOT_paper_five_actual_notes_source_scope_coverage_decision_read=True,own_hashes_verified=33,frozen_math_primary_hashes_verified=43,qualified_note_texts_verified=8,saved_and_actual_note_fields_match_serialization_bytes_differ=True,author14_page_source_PDF_unchanged=True,author_build_not_ROOT_execution=True,built_in_compiler_status='not yet requested',external_source_bodies_excluded=True,infinite_structural_meaningfulness_pending=True,new_accepted_paper=False,original_closed=False,protected_P16_editor_unchanged_open=True))
(D/'ROOT-README.md').write_text('UNREVIEWED14-page whole-original P05.2 solution candidate, native239 / continuation332.\n\n11/42 originals solved;31 OPEN;89 accepted papers. AuthorcandidateTRUE awaits independent whole-original mathematical/source/scope/noncircularity review. Whole343LF authoritative paper, all5 actual FINAL note fields, exact source ledger/scope/coverage/decision and full original55562-character family dossier ROOT-read.33own+43frozen+47reported-input hash records and8 qualified note texts independently verified. Saved/actual note fields equal, serialization bytes differ. Controller/native task and notes equal; assignment/serialization differs and both records remain bound. Parallel argument supplied as data without a separate whole ROOT reading claim.\n\nClaims an input-only INFINITE carrier/tree/primitive-polynomial criterion iff genuine endpoint domain and exact contact for ALL bounded continuous obstacles, via raw-tree identity, exact finite PC rows/raw polynomials, strict global majorants BEFORE MA, independent O323 ALLC_b endpoint domains, local rational PA bumps, legal-tree tails and fixed-C completed measure/contact limits. Original meaning of structural classification requires independent judgment; no finite algorithm/taxonomy/universal-real theorem or P05.5 is claimed. Positive-dimensional literal pairs fail admitted-obstacle domain, compact positive-dimensional embedded balanced category empty, dimensionzero/empty direct. Full qualified imported assumptions/mandatory annotations retained; source bodies LOCALONLY. Initial build/rerun/expected no-shell warnings preserved. ROOT328 finite-vertex strengthening was NOT an author239 input and is not silently retrospective proof. ProtectedP16.4 editor remains open unchanged.\n')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==11 and x['remaining_open_original_atoms']==31 and x['historical_reviewed_scoped_papers']==89
    x.update(updated_utc=now,P05_2_candidate239=dict(status='completed author whole-original candidate; independent review pending',candidate=True,public_directory=str(D),ROOT_reading_binding=str(B),original_closed=False));write(p,x)
print(json.dumps(dict(public_candidate=str(D),reading_binding=str(B),source_sha256=sha(D/'P05.2-paper.tex'),pdf_sha256=sha(D/'P05.2-paper.pdf'),own_hashes_verified=33,frozen_hashes_verified=43,qualified_note_texts_verified=8),indent=2))
