from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'; G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation224.json'
F = G / 'continuation224-publication-records'
S = K / 'small-batch220221-public-status-20261008-continuation224'
D = K / 'public-P05.1-continuation295-independent-common-subspace-pages-global-real-regularization'
D291 = K / 'public-P05.1-continuation291-compact-balanced-charts-and-independent-affine-branches'
A = R / 'campaigns/round-218/P05.1-unchanged-compact-balanced-charts-and-independent-bouquets-whole-native-local-source-audit/artifacts/codex-IIclyq'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, v: Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
assert not any(p.exists() for p in [M, F, S])
prior = json.loads((G / 'push-receipt-continuation223.json').read_text())
assert prior['commit_sha'] == 'd7ff360d16ec8f01542a3718dc5341052eda974e' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
rep = json.loads((D / 'root-reproduction-binding-20261008.json').read_text())
assert not rep['new_accepted_paper'] and not rep['original_closed'] and rep['finite_output_byte_exact'] and rep['source_to_standalone_GFM_bytes_exact'] and rep['pdf_pages'] == 14
for name, key in [('P05.1-paper.tex','source_sha256'),('argument.md','argument_sha256'),('P05.1-paper.pdf','pdf_sha256')]:
    assert sha(D / name) == rep[key]
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
audit = json.loads((A / 'audit-report.json').read_text())
assert audit['verdicts'] == dict(mathematical_proofs='PASS', source_ledger='FAIL', mathematical_source='FAIL', historical_evidence='INCONCLUSIVE', concrete_historical_reproduction='PASS')
own = json.loads((A / 'own-artifact-bindings.json').read_text())
assert len(own['files']) == 67
for e in own['files']:
    p = A / e['filename']
    assert p.resolve().is_relative_to(A.resolve()) and sha(p) == e['sha256'] and p.stat().st_size == e['bytes']
for e in json.loads((A / 'frozen-file-bindings.json').read_text()):
    assert e['matches'] and sha(e['path']) == e['expected_sha256'] == e['sha256']
E = D291 / 'evidence/independent-local-audit218-unreviewed'; assert not E.exists(); E.mkdir()
for e in own['files']:
    if e['LOCALONLY'] or e['filename'].endswith('.pdf'):
        continue
    p = E / e['filename']; p.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(A / e['filename'], p)
for name in ['own-artifact-bindings.json','validation-report.json']:
    shutil.copy2(A / name, E / name)
for name, target in [('round218-actual-native-final.json','exact-native-final.json'),('round218-registered-native-result.json','registered-native-worker-result.json'),('round218-actual-final-extraction-binding-20261008.json','actual-final-extraction-binding.json')]:
    shutil.copy2(K / name, E / target)
final = json.loads((K / 'round218-actual-native-final.json').read_text())
saved = json.loads((A / 'native-notes.json').read_text())
delta = [dict(id=a['id'], different_fields=[k for k in set(a) | set(b) if a.get(k) != b.get(k)], actual_text_bytes=len(a['text'].encode()), saved_text_bytes=len(b['text'].encode())) for a,b in zip(final['notes'],saved['notes'])]
write(E / 'ROOT-publication-binding-no-acceptance.json', dict(recorded_utc=datetime.now(timezone.utc).isoformat(), exact_FINAL_all7_whole_ROOT_read=True, whole_source_application_audit_ROOT_read=True, whole_full_audit_and_coverage_ROOT_read_still_pending=True, all67_auditor_artifact_hashes_verified=True, all115_auditor_input_hashes_verified=True, own_LOCALONLY_primary_bodies_and_pixels_not_published=True, own_reproduction_PDFs_not_duplicated_in_upload=True, exact_FINAL_is_controlling=True, saved_expanded_notes_are_historical=True, saved_notes_differences=delta, unchanged_native218_combined_math_source_FAIL_retained=True, geometric_PASS_distinct=True, historical_INCONCLUSIVE_retained=True, ROOT_source_corrections_separate=True, mathematical_acceptance=False, original_closed=False, supplied_auditor_programs_not_executed=True))
now = datetime.now(timezone.utc).isoformat(); F.mkdir(); S.mkdir(); items = []
for n in [218,219,220,221]:
    c = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    p = S / f'round{n}-public-native-status.json'; write(p, st)
    items.append(dict(round=n, atom='P05.1', directory=str(c), observed_status=st['status'], observed_utc=st['observedAt'], public_status=str(p), public_status_sha256=sha(p), unsettled_calls=st['calls']['unsettled'], private_active_output_read=False, hot_feedback_sent=False, original_closed=False))
active = [e for e in items if e['unsettled_calls'] > 0]; assert len(active) <= 2
batch = dict(recorded_utc=now, items=items, active_items=active, maximum_concurrent_campaigns=2, accepted_paper_number=82, original_closed=False, focus='220 independent whole unchanged292 isolated-crossing local audit;221 arbitrary-dependent common-H joint-dual author.218 completed geometricPASS/sourceFAIL/historyINCONCLUSIVE, entire reports ROOT review pending;219 complete295 14p unreviewed paper reproduced.')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms']) == 9 and j['remaining_open_original_atoms'] == 33 and j['historical_reviewed_scoped_papers'] == 82 and j['github_pending_checkpoint'] is None and j['github_checkpoint']['commit_sha'] == prior['commit_sha']
    j.update(updated_utc=now, current_small_batch=batch, settled218_unreviewed_audit=dict(geometric_verdict='PASS', source_ledger_verdict='FAIL', combined_verdict='FAIL', historical_verdict='INCONCLUSIVE', all7_exactFINAL_whole_ROOT_read=True, entire_source_audit_ROOT_read=True, full_audit_coverage_ROOT_read_pending=True, harmless_source_corrections=str(D291/'harmless-source-ledger-corrections-after-audit218-20261008.json'), unchanged_frozen_source_ledger_retained=True, acceptance=False, original_closed=False), new295_unreviewed_paper=rep, next_work='Continue completeROOT218 report/coverage/evidence checks and source-correction-qualified independent judgement, not unqualifiedPASS. Prepare whole295 independent audit after PUBLIC220/221 settlement frees a slot. Read exact settled220/221 outputs only then. Continue all33 original goals; at mosttwo61xhighnative campaigns; nohotfeedback/privateACTIVE. Builtin291cell62/292cell94/295cell136 pending, no duplicates or tab changes.', github_pending_checkpoint=dict(continuation=224,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    j['new292_unreviewed_paper']['independent_audit220_prepared_not_launched'] = False
    j['new292_unreviewed_paper']['independent_audit220_launched'] = True
    j['settled217_status'].update(whole_source_read_in_progress=False,whole_source_ROOT_read=True)
    write(p,j); shutil.copyfile(p,F/name)
shutil.copyfile(R / 'checklist-current.tsv', F / 'checklist-current.tsv')
(F / 'README.md').write_text('Checkpoint224: common-subspace paper, source corrections and next bounded batch\n\n9/42 originals solved;33 open;82 accepted scoped/supporting papers, unchanged. Whole new295 is an UNREVIEWED 14-page independent-normal common-H book paper. ROOT read its entire source, all6 controlling actualFINAL notes, whole ledger/scope/coverage/execution and inspected the safe bounded arithmetic. All61 own artifact,25 mathematical and4 primary hashes verified. Exact finite output reproduced once;3 no-shell-escape TeX passes succeed and source to standaloneGFM conversion is byte-exact. Whole-H trace via compact dual minimizing fibers and entire PA epigraph generators precedes global decreasing regularization, then every actual C_b envelope enters the genuine domain BEFORE granted mixedMA. Initial missingmacro failure and reconstructed historical source, reference/layout warnings, final disabled-shell package warning are retained. Saved219 notes equal actualFINAL after parsing; registeredArtifacts suffix separate. No mathematical acceptance or original closure follows from reproduction.\n\nIndependent ordinary native218 audit gives scoped geometricPASS, unchanged sourceledgerFAIL, combined mathematical/sourceFAIL, historicalINCONCLUSIVE and concrete reproductionPASS. ROOT read all7 actualFINAL notes and entire sourceaudit; full299KB audit/192KB coverage ROOT-reading remains pending. All67 own artifact and115 input identities checked. Public safe evidence preserves the exactFINAL and distinct expanded saved notes; primaryLOCALONLY bodies/pixels and duplicate reproductionPDFs excluded. No supplied audit emitter/binder/rerunner executed.\n\nTwo verified harmless source corrections are a separate reader clarification; the original ledger/TeX/frozen input remain unchanged. BMPS v1 Definitions2.19/2.20 have rational weights, not real; real extension is a separate reconstructed proof/BBGS domain. BBGS complete3.15 is LF604-670, not604-667. ROOT independently read the entire immediate original units. These corrections do not change the nativeFAIL or certify historic reading. No primary excerpts republished.\n\nNative220 and221 launched only after218/219 PUBLICcompleted.220 audits the entire unchanged292 isolated-crossing paper with exactly5whole grants, allclarifications and its own frozen history; newerjointdual andS282acceptance excluded.221 authors arbitrary-dependent common-H jointdual regularization from whole293294DATA including fullold289 and exactly6whole grants; historicalnative215INCONCLUSIVE retained. Both use nativegpt-6.1-sol xhigh onecall and unchangedauthentication/sandbox, maximumtwo. Nohotfeedback/privateACTIVE/controllerstream/SQL reads. Differentoverlapspaces/generaloriginal classification remainOPEN.\n\nBuilt-in standalone compiler requests291cell62,292cell94 and295cell136 remainpending, no duplicate or resultclaim. Protected original editor remains openunchanged. Upload noforce independently checks everyremote blob, nativeGitTree andbranchref.\n')
files=[]
def add(p,target=None):
    p=Path(p); assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation224/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()): add(p)
for folder in [D,E]:
    for p in sorted(folder.rglob('*')):
        if not p.is_file() or 'LOCALONLY' in str(p.relative_to(folder)): continue
        if p.suffix in ['.pdf','.aux','.out','.log'] and p != D/'P05.1-paper.pdf': continue
        add(p)
add(D291/'harmless-source-ledger-corrections-after-audit218-20261008.json')
for n in [220,221]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    for name in ['task.json','input.json','settings.json','freeze.json','original-task.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','launch-record.json']: add(c/name)
    if (c/'historical-own-evidence-bindings.json').exists(): add(c/'historical-own-evidence-bindings.json')
for name in ['launch_isolated_crossings_audit220_20261008.py','prepare_dependent_common_subspace_paper221_20261008.py','launch_dependent_common_subspace_paper221_20261008.py','extract_settled218219_exact_native_results_20261008.py','reproduce_and_publish_common_subspace295_20261008.py','record_verified223_20261008.py']: add(R/name)
add(G/'push-receipt-continuation223.json'); add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']: add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=82,commit_message='Preserve independent audit source defects and complete common-subspace paper',scope='Whole295 unreviewed14p paper/exactFINAL/all safe own history/ROOTrepro; native218 scoped geometricPASS-sourceFAIL-historyINCONCLUSIVE retained, exact7FINAL separate from expanded history, twoROOTsourcecorrections noacceptance.220221 native61xhigh max2batch frozen+launched.9solved33open82accepted unchanged. Nativecompiler62/94/136pending protectededitorunchanged; no private/primaryquotes/pixels/authuploads; noforce blob/nativeGit/refverification.'))
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=82),indent=2))
