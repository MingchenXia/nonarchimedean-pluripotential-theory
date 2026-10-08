from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation241.json';F=G/'continuation241-publication-records';S=K/'small-batch236237-public-status-20261008-continuation241'
W=K/'P12.2-continuation324-normal-target-coefficient-trace-and-finite-gap-addendum-20261008.md'
V=K/'native-built-in-compiler-completion-addendum-after-checkpoint240-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists()for p in[M,F,S,V]);prior=json.loads((G/'push-receipt-continuation240.json').read_text())
assert prior['commit_sha']=='62154b4bdeef51c9ca38ba7eb1a84b5e79c56039' and not prior['force_update']
assert all(prior[k]for k in['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();results=[]
for cell,folder,file,busy in [
 (403,'public-P12.2-continuation321-smooth-recovery-and-conductor-saturation-unreviewed','P12.2-paper.tex',None),
 (424,'public-P05.1-continuation323-coefficient-separated-dual-classification-candidate','P05.1-paper.tex',None),
 (363,'public-P05.1-continuation318-free-attachment-multiple-overlap-regularization-unreviewed','P05.1-paper.tex',None),
 (429,'public-P05.1-continuation313-all-face-nontermination-and-simultaneous-linear-certificate-unreviewed','P05.1-paper.tex',332),
 (430,'public-P12.2-continuation316-numerical-Cartier-bounded-comparison-and-isolated-descent-unreviewed','P12.2-paper.tex',333),
 (134,'public-P14.8-continuation309-general-formal-ideal-realization-candidate','P14.8-paper.tex',None),
 (228,'public-P14.8-continuation308-arbitrary-formal-ideal-realization-on-projective-line','P14.8-paper.tex',None),
 (81,'public-P05.1-continuation307-compatible-affine-reference-extension-and-sharp-global-restriction-distance','P05.1-paper.tex',None),
 (431,'public-P05.1-continuation306-balanced-cellwise-Lipschitz-and-single-cell-real-regularization','P05.1-paper.tex',54)]:
    p=K/folder/file;results.append(dict(compile_cell=cell,path=str(p),kind='success',tool_message='The current source compiled successfully with the desktop editor\'s compiler.',source_current_sha256=sha(p),source_bytes=p.stat().st_size,prior_busy_cell=busy,prior_busy_not_source_failure=busy is not None,source_not_modified_for_this_compile=True,new_tab_not_opened=True))
write(V,dict(recorded_utc=now,tool='codex_app.compile_latex_document',results=results,legacy_cell90=dict(path=str(K/'public-P14.8-continuation308-arbitrary-formal-ideal-realization-on-projective-line/P14.8-paper.tex'),kind='success',source_version_binding_not_claimed=True,reason='The source was mathematically repaired after that historical request; the corrected-source request228 is the separate current verification.'),all_results_are_actual_returned_tool_diagnostics=True,compiler_exports_no_PDF=True,source_compilation_not_mathematical_acceptance=True,historical_published_freezes_unmodified=True,protected_editor_unchanged_open=True,new_accepted_paper=False,original_closed=False))
F.mkdir();S.mkdir();items=[]
for n,atom in[(236,'P12.2'),(237,'P05.1')]:
    old=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st);items.append(dict(round=n,atom=atom,observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(old),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[236,237],maximum_concurrent_campaigns=2,accepted_paper_number=88)
for name in['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint']is None
    x.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(continuation=241,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),native_compile_completion_addendum=dict(path=str(V),sha256=sha(V),nine_current_source_successes=True,old_busy_then_success_retained=True,compiler_not_mathematical_verdict=True),P12_2_normal_target_trace_working324=dict(path=str(W),sha256=sha(W),bytes=W.stat().st_size,whole_ROOT_physically_read=True,unreviewed=True,all_prime_support_norm_coefficient_proof_proposed=True,rational_difference_lattice_uniform_real_closure_corrected=True,finite_positive_gap_all_bottom_convention_explicit=True,fed_active236237=False,new_accepted_paper=False,original_closed=False))
    if name=='checklist-current.json':x['active_atoms']=[e['atom']for e in active]
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint241: all-support trace addendum and returned compiler diagnostics\n\n10/42solved;32OPEN;88accepted. Native236P12.2 reconstruction and237P05.1wholecandidate review retain frozen inputs; no new acceptance, sourcePASS or originalclosure.\n\nROOT324 independently reconstructs normal-target coefficient norm traces directly at everyprime-supportsemivaluation: lift only to a finite integral algebra, quotient by support before Gauss division, retain genericinseparablemultiplicity, use rationaldifference lattice then uniformrealclosure, and take finite positiveweighted decreasing limits. Verticalsourcecomponents receive no inventedgenericdegree. It also explicitly chooses a FINITEpositive lowergap even when the active set is entirelybottom; n*sigma directly handles bottomonactive/zerooffactive after boundedindicator descent. This is UNREVIEWED and not fed as hotfeedback to active236/237. HistoricalROOT317/319/320publishedbytes stay unchanged.\n\nActual nativecompiler returns now verify nine current sources:306,307,corrected308,309,313,316,318,321,323. Initial busy results332,333,54 and one successful retry each are preserved. Legacy90success is recorded without claiming a source-version binding because308was subsequently repaired; corrected-request228is separate. Builtincompiler success is source/build evidence only, exportsnoPDF, and does not certify mathematics. Public frozen status files remain unchanged; this new addendum records late outcomes. ProtectedP16.4editor staysopenunchanged; no newtab.\n\nFull external primary sources remainLOCALONLY. All uploads authorized; noforceupdate; exactremote file/tree/ref verification follows.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file()and'LOCALONLY'not in str(p.relative_to(R));files.append(dict(local=str(p),path=target or'research-checkpoints/continuation241/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in[F,S]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for p in[W,V,G/'push-receipt-continuation240.json',R/'record_verified240_20261008.py',Path(__file__)]:add(p)
for name in['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path']for e in files})==len(files);x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=32,historical_reviewed_scoped_papers=88,commit_message='Preserve all-support coefficient trace proof and returned LaTeX compiler receipts',scope='10solved32OPEN88accepted; ROOT324unreviewednotfedactive; ninecompiledsourcesverified asbuildonly; native236237max2active.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round']for e in active],statuses=[dict(round=e['round'],status=e['observed_status'])for e in items]),indent=2))
