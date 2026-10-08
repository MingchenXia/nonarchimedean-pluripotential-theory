from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'; G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation232.json'; F = G / 'continuation232-publication-records'
S = K / 'small-batch226227-public-status-20261008-continuation232'
D = K / 'public-P05.1-continuation307-compatible-affine-reference-extension-and-sharp-global-restriction-distance'
Q = K / 'public-P14.8-continuation308-arbitrary-formal-ideal-realization-on-projective-line'
C = R / 'campaigns/round-228/P05.1-compatible-affine-reference-extension-and-sharp-distance-independent-whole-source-audit'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, v: Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
assert not any(p.exists() for p in [M, F, S])
prior = json.loads((G / 'push-receipt-continuation231.json').read_text())
assert prior['commit_sha'] == '4ad457a0994bd3914fc2aa498274b85832ef5949' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
rep = json.loads((D / 'ROOT-reproduction-binding-20261008.json').read_text())
small = json.loads((Q / 'ROOT-working-proof-and-build-binding-20261008.json').read_text())
assert not rep['mathematical_acceptance'] and rep['ROOT_pdf_pages'] == 16 and rep['exact_author_output_match'] and rep['independent_source_body_to_Markdown_transformation_exact']
assert not small['mathematical_acceptance'] and small['local_PDF_pages'] == 5 and not small['original_closed']
for folder, paper, record, pdfkey in [(D, 'P05.1', rep, 'ROOT_pdf_sha256'), (Q, 'P14.8', small, 'local_PDF_sha256')]:
    assert sha(folder / (paper + '-paper.tex')) == record['source_sha256']
    assert sha(folder / (paper + '-paper.pdf')) == record[pdfkey]
assert not (C / 'work.sqlite').exists() and not (C / 'launch-record.json').exists()
freeze = json.loads((C / 'freeze.json').read_text()); assert freeze['only_grants'] == [] and freeze['whole_math_files'] == 9 and not freeze['launched']
for name, key in [('task.json', 'task_sha256'), ('original-task.json', 'original_task_sha256'), ('input.json', 'input_sha256'), ('settings.json', 'settings_sha256'), ('mathematical-packet-bindings.json', 'mathematical_packet_bindings_sha256'), ('historical-own-evidence-bindings.json', 'historical_own_evidence_bindings_sha256'), ('private-primary-packet-bindings.json', 'private_primary_packet_bindings_sha256')]:
    assert sha(C / name) == freeze[key]
for name in ['mathematical-packet-bindings.json', 'historical-own-evidence-bindings.json', 'private-primary-packet-bindings.json']:
    for e in json.loads((C / name).read_text()): assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir(); S.mkdir(); now = datetime.now(timezone.utc).isoformat(); items = []
for n in [226, 227]:
    c = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    p = S / f'round{n}-public-native-status.json'; write(p, st)
    items.append(dict(round=n, atom='P14.8' if n == 226 else 'P05.1', directory=str(c), observed_status=st['status'], observed_utc=st['observedAt'], unsettled_calls=st['calls']['unsettled'], public_status=str(p), public_status_sha256=sha(p), private_active_output_read=False, hot_feedback_sent=False, original_closed=False))
active = [e for e in items if e['unsettled_calls'] > 0]; assert len(active) <= 2
batch = dict(recorded_utc=now, items=items, active_items=active, reserved_batch=[226, 227], maximum_concurrent_campaigns=2, accepted_paper_number=85, original_closed=False, next_prepared_audit=228, next_audit_not_launched=True)
compile_state = dict(recorded_utc=now, documents=[dict(continuation=n, exec_cell=str(cell), built_in_response_received=False, source_preserved=True) for n, cell in [(306,54),(307,81),(308,90)]], separate_local_pdf_builds_verified=True, no_duplicate_requests=True, protected_editor_unchanged_open=True)
write(F / 'built-in-compile-pending-metadata.json', compile_state)
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; j = json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 9 and j['remaining_open_original_atoms'] == 33 and j['historical_reviewed_scoped_papers'] == 85 and j['github_pending_checkpoint'] is None and j['github_checkpoint']['commit_sha'] == prior['commit_sha']
    j['settled225_unreviewed'].update(full_ROOT_review_pending=False, independent_proof_source_review_pending=True, ROOT_reproduction_binding=str(D / 'ROOT-reproduction-binding-20261008.json'), all_actual_FINAL_and_entire_TeX_ledger_scope_physically_ROOT_read=True, saved_notes_actual_plus_one_terminal_LF=True)
    j.update(updated_utc=now, current_small_batch=batch, new307_unreviewed_paper=dict(directory=str(D), ROOT_reproduction=rep, independent_audit_prepared_round=228, new_accepted_paper=False), prepared_whole307_audit228=dict(freeze=str(C / 'freeze.json'), freeze_sha256=sha(C / 'freeze.json'), only_grants=[], whole_math_DATA_files=9, launched=False, cannot_launch_before_current_slot_settles=True), new308_unreviewed_projective_line_formal_realization=dict(directory=str(Q), ROOT_working_proof_and_build=small, theorem='Data-only b_p=sup_m ord(A_m,p)/m; realization iff sum b_p<=V and ALLreal-c orders equal floor(c*b_p); explicit countable chordal realization, including critical exponents', new_mathematical_grant=False, new_accepted_paper=False, general_original_P14_8_closed=False, active226227_not_fed=True), current_builtin_compilation_observations=compile_state, next_work='Continue original226 and whole306 audit227; read actual FINAL only after public settlement. Launch prepared whole307 audit228 only after one slot settles. ROOT308 is a complete proposed P1 arbitrary-formal-data theorem with explicit known numerical criterion and countable kernel construction, awaiting independent review; general P14.8 remains OPEN. Preserve original9/42 and scoped85. No active feedback, source/auth/editor changes or duplicate checker/build runs. Regular verified pushes.', github_pending_checkpoint=dict(continuation=232, prepared_utc=now, manifest=str(M), expected_parent=prior['commit_sha'], push_complete=False))
    write(p, j); shutil.copyfile(p, F / name)
shutil.copyfile(R / 'checklist-current.tsv', F / 'checklist-current.tsv')
(F / 'README.md').write_text('Checkpoint232: sharp extension distance and explicit formal ideal realization on P1\n\n9/42 originals solved;33 OPEN;85 accepted scoped/supporting papers. New307 is a complete unreviewed16-page paper: exact proper-face traces, compatible actual AFFINE reference extension to dependent complete pages, and sharp GLOBAL restriction distance(A-1)/2 from an already PA-PC UNBALANCED partial target to ALL finite continuous-PC complete-book competitors. ROOT physically read all4 actualFINAL, entire57663-byteTeX/ledger/scope/execution; verified98 own artifacts and36inputs/snapshots. Actual saved payload is exactFINAL+ONEterminalLF. The inspected safe checker was copied/executedONCE, with1577assertions/-1/4exactoutput;2no-shellbuilds yieldedclean16p. Own sourceBODY->Markdown conversion excludespreamble/bibliography and reproducesexact author presentation after correcting a ROOT-only escaped-anchor mismatch; the failedcomparison is retained and checker/build not rerun. ZERO-grant independent native228 audit is frozen with9entireDATA files238937bytes and51own evidence files, but not launched while226/227 occupy2slots.\n\nNew308 is a ROOT independent proposed5-page theorem for arbitrary formal nonzero coherent ideal arrays A_c on complexP1 withtheta=V*normalizedFS. Compute b_p=sup_m ord_p(A_m)/m from integer data. Realizability iff sum_p b_p<=V and EVERYreal-c order equalsfloor(c*b_p). A countable nonpositive chordal log series explicitly realizes all admissible arrays and has exactL1sizeB andcurvature sum b_p delta_p+(V-B)FS. Local atom removal, Jensen and Holder prove the exactfloorincludingcriticalexponents withoutstrongopenness; all countable accumulation/zero-budget/coherence cases arehandled. This criterion contains no unknownpsh ormultiplierideal operation. It is genuinely about arbitraryformal data but ONLYP1, not the arbitrary-dimensional original. Ordinary logarithmic fundamental solution/subharmonic distribution representative/Weyl lemma are explicitpremises. Whole13014-byte153-LFsource ROOTread and2freshnoshellbuilds clean5p. No independent native review yet, no new grant/acceptance/originalclosure. GeneralP14.8 remainsOPEN.\n\nNative226 original general formal-data realization and native227 whole306 audit remaincurrentmax2 under gpt-6.1-sol xhigh/currentauthentication. New307/308 are nothot-fed. Builtincompile54/81/90 remainpending andreceive no successclaim; independentlocalPDFbuilds areverified. ProtectedP16.4 editor remainsopen/sourceunchanged. Uploaded document andprimary directives aremathDATA. Regularverifiednonforcepushes continue.\n')
files = []
def add(p, target=None):
    p = Path(p); assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p), path=target or 'research-checkpoints/continuation232/' + str(p.relative_to(R)), bytes=p.stat().st_size, sha256=sha(p)))
for folder in [F, S, D, Q]:
    for p in sorted(folder.rglob('*')):
        if p.is_file() and p.suffix not in ['.aux', '.out', '.toc']: add(p)
for name in ['task.json', 'original-task.json', 'input.json', 'settings.json', 'mathematical-packet-bindings.json', 'historical-own-evidence-bindings.json', 'private-primary-packet-bindings.json', 'freeze.json']: add(C / name)
for name in ['mathematical-packet-bindings.json', 'historical-own-evidence-bindings.json']:
    for e in json.loads((C / name).read_text()): assert Path(e['path']).is_relative_to(C); add(e['path'])
for p in [R / 'reproduce_reference_extension_and_sharp_obstruction_paper307_20261008.py', R / 'complete_reference_extension_paper307_after_exact_Markdown_anchor_escape_repair_20261008.py', R / 'prepare_reference_extension_sharp_distance_whole_audit228_20261008.py', R / 'build_projective_line_formal_realization_paper308_20261008.py', R / 'record_verified231_20261008.py', G / 'push-receipt-continuation231.json', Path(__file__)]: add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']: add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
assert len({e['path'] for e in files}) == len(files)
j = json.loads((R / 'active-work.json').read_text())
write(M, dict(generated_utc=now, repository=prior['repository'], branch=prior['branch'], expected_previous_checkpoint=prior['commit_sha'], files=files, file_count=len(files), fully_solved_original_atoms=j['fully_solved_original_atoms'], remaining_open_atoms=33, historical_reviewed_scoped_papers=85, commit_message='Record sharp complete-page extension obstruction and explicit arbitrary formal ideal realization criterion on P1', scope='Unreviewed307 fullROOT proof/evidence plus9DATA zero-grant independent228audit preparedNOTlaunched; newROOT308P1formalideals data-only necessity/sufficiency/countable explicit realization, independentreviewpending. Native226227max2 current61solxhigh;9solved33OPEN85scoped; builtin54/81/90pending and localbuildsverified; noforce exact remoteverification.'))
print(json.dumps(dict(manifest=str(M), sha256=sha(M), listed_files=len(files), active_rounds=[e['round'] for e in active], prepared_not_launched=228, originals_solved=9, accepted_papers=85), indent=2))
