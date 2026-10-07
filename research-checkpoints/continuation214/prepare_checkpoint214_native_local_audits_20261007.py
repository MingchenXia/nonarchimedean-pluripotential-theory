from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation214.json';F=G/'continuation214-publication-records'
S=K/'small-batch209210-public-status-20261007-continuation214'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation213.json').read_text())
assert prior['commit_sha']=='4f5e1cc15498be9e72e0f006fabee990bb1c1b90' and not prior['force_update']
assert all(prior[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
reviews=[K/'P16.4-round207-whole-all-genus-curve-INCONCLUSIVE-review-binding-20261007.json',K/'P05.2-round208-whole-arbitrary-reference-INCONCLUSIVE-review-binding-20261007.json']
for p in reviews:
    b=json.loads(p.read_text());assert b['verdict']=='INCONCLUSIVE' and b['source_unchanged'] and not b['new_accepted_paper'] and not b['original_closed']
working=[next(K.glob(f'P05.2-continuation{n}-*.json')) for n in [276,277]]
for p in working:
    b=json.loads(p.read_text());assert not b['new_mathematical_grant'] and not b['original_closed']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in [207,208,209,210]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P16.4' if n in [207,209] else 'P05.2',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],
        public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
assert items[0]['unsettled_calls']==items[1]['unsettled_calls']==0
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,
    focus='Independent native local-file whole audits209269 curve/210272 arbitrary-reference. Canonical207/208 whole INCONCLUSIVE remain preserved. ROOT276jointmaxclosure/277intrinsicheight are new unreviewed future data, not active audit premises.',
    new_accepted_paper=False,accepted_paper_number=78,original_closed=False)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==78 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,
        whole_INCONCLUSIVE_reviews207208=[dict(path=str(q),sha256=sha(q),verdict='INCONCLUSIVE',new_accepted_paper=False,original_closed=False) for q in reviews],
        P05_2_joint_max_and_original_height_working276277=[dict(path=str(q),sha256=sha(q),new_mathematical_grant=False,original_closed=False) for q in working],
        native_local_source_audits209210=dict(native_worker_role_not_canonical_research_review=True,research_runtime_unchanged=True,
            file_shell_tools_enabled_for_immutable_reads_only=True,only_own_new_audit_artifacts_written=True,
            exact_whole_mathematical_arguments_unchanged=True,earlier_verdicts_not_supplied_as_grants_or_verdict_bias=True,
            original_papers_unchanged=True,task210_cutoff_gap_j_plus_c_corrected_to_paper_j=True,
            new_working276277_not_supplied=True,no_new_acceptance=True),
        next_work='Read and bind whole independently produced local-file audits209/210 after settlement; continue actual original higherdim inverse/all-obstacle classification and remaining33 problems. At most two61xhigh native campaigns; no stopping at support sectors. Preserve original sources/editor/failures and regular verified pushes.',
        github_pending_checkpoint=dict(continuation=214,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint214: preserve whole INCONCLUSIVE reviews and resolve local-file audit access\n\n9/42 originals solved;33 open;78 accepted scoped/supporting papers. No new acceptance or original closure. Whole canonical207 curve269 review is INCONCLUSIVE:25premises/27registeredpassages/28nativepassages/fullreport ROOT-read; actual33mathunits/decodednative input bound. BL85/RG/Berkovich1993 immediate original proof evidence and complete frozen-source access unresolved. One native task-grant citation at invalid external index25 was excluded by kernel and is not primary coverage;27registeredpassages match first27native passages. The review found no concrete counterexample but conditional coherent steps are not grants.\n\nWhole canonical208 arbitrary-reference272 review is INCONCLUSIVE:2premises/6passages/fullreport ROOT-read and exact native-canonical equality;30wholemathunits/native decoded input bound. It independently reconstructed visible13units and literal primary applications but reported an exposed preview omission of116863tokens and no file reader for all frozen source/grant bodies. Full registered691992-byte argument remains intact; a truncated view is not a full audit. The TASK checklist cutoffgap j+c was wrong; unchanged paper gapj was always correct. New210 task corrects the checklist only, without source repair.\n\nSupported Xean native Codex WORKERS209/210 now perform independent WHOLE local-source audits using native file/shell tools on immutable original papers/grants/primaries, in bounded COMPLETEchunks. They write only own retained audit artifacts under the existing workspace-write worker sandbox. The research role remains unchanged, read-only/shell-disabled. This is a capability-appropriate new standalone worker, not a runtime/account/sandbox modification. Parent61xhigh invocation/authentication preserved. Worker notes are ordinary unverified publications, NOT canonical Xean review or automatic acceptance. All original papers/exact whole mathematical arguments unchanged;33mathunits/62originals for209 and30mathunits/fouroriginals for210. Earlier207/208verdicts not supplied as mathematical grants/verdict bias; oldFAILs retained as data. At most two campaigns209/210.\n\nNEW ROOT276 unreviewed working proof jointly decomposes finite reference/input coefficients in a rational cone with EXACT bounded-recession equations, giving global same-reference PA approximation of finite maxima and max closure of the actual completion despite irrational walls; scalar convex caps and an explicit irrational-breakpoint raw line example included. NEW ROOT277 is an explicitly conditional application reconstructing actual cap-domain/weak mixed completion BEFORE bounded IBP, leading to original-reference height2dCM+J_gamma for EVERYfixed-Ccompletedmixedtuple. Its pending272/276 antecedents are not grants. Neither proves ALLcontinuousPC/ALLobstacle envelope regularization or full contact sufficiency. New276/277 are NOT active audit premises/hotfeedback/source repair. General-dimensional originalP16.4 and higherdim originalP05.2 remain open.\n\nBuiltin53/113/27 remain pending withoutSUCCESS; no new manuscript edit or current editor change. No full thirdparty primary bytes/pixels/longquotations/private active output/rawdatabase/authentication/account data published. Publication uses no-force updates and independent tree/blob/ref verification.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation214/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for atom,n,stem in [('P16.4',207,'all-genus-curve'),('P05.2',208,'arbitrary-reference')]:
    for name in [f'{atom}-round{n}-actual-canonical-independent-INCONCLUSIVE-review-20261007.json',f'{atom}-round{n}-exact-native-model-final-INCONCLUSIVE-review-20261007.json',f'{atom}-round{n}-whole-{stem}-INCONCLUSIVE-review-binding-20261007.json']:add(K/name)
for p in working:add(p)
for n in [209,210]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    for name in ['freeze.json','unchanged-mathematical-data-bindings.json','private-primary-packet-bindings.json','launch-record.json']:add(c/name)
for name in ['bind_whole_inconclusive_curve_review207_20261007.py','bind_whole_inconclusive_reference_review208_20261007.py','prepare_curve269_native_local_audit209_20261007.py','launch_curve269_native_local_audit209_20261007.py','prepare_reference272_native_local_audit210_20261007.py','launch_reference272_native_local_audit210_20261007.py','write_joint_max_closure276_20261007.py','write_actual_reference_height277_20261007.py','record_verified213_20261007.py']:add(R/name)
add(G/'push-receipt-continuation213.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),
fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=78,
commit_message='Preserve inconclusive whole reviews and launch independent native local-file audits',
scope='WHOLE207269 and208272INCONCLUSIVE results/fullnativebinding retained; complete localfile/source/grant access unresolved,208visiblepreview omitted116863tokens. Supported native workers209210 perform independent WHOLE audits with file/shell tools/read immutable originals/write own audit artifacts only. Canonical researchrole unchanged; newworker ordinarynotes are not automatic acceptance. Whole matharguments/sources unchanged;210TASKcutoffj+c correctedto unchangedpaperj. ROOT276jointmaxclosure/domaincaps and277intrinsicheight are unreviewed futuredata, notactivepremises/repair/hotfeedback.9originals33open78accepted;atmosttwo61xhigh209210. Builtin53/113/27pendingwithoutSUCCESS. Protectededitor/frozensources/failurespreserved;no fullthirdpartyprimary/privateactive/auth/databasepublication. Verified noforce push.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=78),indent=2))

