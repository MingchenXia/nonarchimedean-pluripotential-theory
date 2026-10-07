from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation202.json';F=G/'continuation202-publication-records';S=K/'small-batch195196-public-status-20261007-continuation202'
D=K/'public-P05.2-continuation247-finite-PA-contact-circuits-and-plane-counterexample'
Z=K/'public-P16.4-continuation227-genus-zero-equation'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation201.json').read_text())
assert prior['commit_sha']=='ff20f082b6aa6ac5c0c422a14a3117e8f2be4bad' and not prior['force_update']
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
za=json.loads((Z/'whole-partial-paper-acceptance189-20261007.json').read_text())
assert za['verdict']=='PASS' and za['source_sha256']==sha(Z/'P16.4-paper.tex')
b=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert b['candidate'] is False and b['canonical_result'] is None and b['root_local_build_exit_codes']==[0,0]
assert b['source_sha256']==sha(D/'P05.2-paper.tex') and b['root_pdf_sha256']==sha(D/'P05.2-paper.pdf')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in (189,194,195,196):
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n in (194,196) else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[i for i in items if i['unsettled_calls']>0];assert len(active)<=2
assert all(i['unsettled_calls']==0 for i in items if i['round'] in (189,194))
visual=D/'root-visual-reading-scope-addendum-20261007.json'
visual.write_text(json.dumps(dict(recorded_utc=now,source_sha256=sha(D/'P05.2-paper.tex'),pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=10,root_actual_visual_read_pages=[1,6,7],root_rendered_but_not_yet_visually_read_pages=[10],whole_pdf_visually_read=False,source_not_modified=True,root_local_build_exit_codes=[0,0],root_exact_public_source_builtin_compiler_success=False,builtin_request_started=True,builtin_request_has_not_returned_diagnostics_at_checkpoint=True,independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False),indent=2)+'\n')
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,completed189_verdict='PASS',completed189_accepted_scoped_paper_number=76,completed194_registration_error=b['native_registration_error'],completed194_candidate=False,completed194_continuation=247,focus='195 actual original-equation author after direct formal FS and residual-curvature primary bridge;196 whole247 independent finite-PA-contact reader with three complete A224/B225/R230 grants and all clarifications. Native189 whole227 accepted76. Native194 exact unregistered final and paper retained, no canonical author result. Original P16.4/P05.2 remain open. Public statuses only; max2.')
C195=next((R/'campaigns/round-195').iterdir());fr=json.loads((C195/'freeze.json').read_text());lr=json.loads((C195/'launch-record.json').read_text())
assert lr['model']=='gpt-6.1-sol' and lr['reasoning']=='xhigh'
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==76 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,
        prepared_next_original_campaign=dict(round=195,atom='P16.4',directory=str(C195),freeze=str(C195/'freeze.json'),freeze_sha256=sha(C195/'freeze.json'),input_sha256=fr['input_sha256'],prepared_only=False,launched=True,only_complete_grants=['O217','D214','N220','T171','Q222','C218'],unreviewed_data=[235,243,244,245,246],private_primary_files=22,full_primary_files_published=False,maximum_active_campaigns=2,launch_record=str(C195/'launch-record.json'),launch_record_sha256=sha(C195/'launch-record.json')),
        github_pending_checkpoint=dict(continuation=202,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint202: whole genus-zero equation accepted; finite PA contact paper under review\n\n9/42 original problems solved,33 open,76 independently accepted scoped/supporting papers. Native189 PASS binds the whole unchanged11-page227 paper, original complete-field genus-zero curves including nonsplit conics, all actual targets and every-solution all-point uniqueness. No all-genus/high-dimensional original closure.\n\nWhole native194 ten-page247 source and argument, exact five-note final, three full accepted grants with all clarifications, four private original-primary hashes and41 native artifact hashes checked. Author kernel registration failed on B225; canonical result is NULL. This failure is preserved. Exact finite raw masses8,4,4 and contact-2 reproduced in an independent copy; two local builds succeeded. Finite PA contact criterion and nonseparable counterexample remain unreviewed. Independent196 reader now launched.\n\nOriginal195 author uses frozen244 proper-completion/field-GAGA primary reading,245 direct same-bundle formal-FS route and246 exact residual-bundle/raw-atomic coefficient chain. These are unreviewed working data. Whole original primary files and original dossier bodies remain private; quote-free reading scopes and hash bindings are published. Two active campaigns maximum, native gpt-6.1-sol xhigh, no active private-output reads or hot feedback. Protected editor preserved.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation202/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S):
    for p in sorted(folder.iterdir()):add(p)
for name in ('P16.4-paper.tex','P16.4-paper.pdf','argument.md','whole-partial-paper-acceptance189-20261007.json','harmless-reader-clarifications189-20261007.json'):
    p=Z/name
    if name=='argument.md' and not p.exists():p=Z/'P16.4-argument.md'
    add(p)
for name in ('P05.2-paper.tex','P05.2-paper.pdf','argument.md','notes.json','source-application-ledger.md','check_certificates.py','certificate-input.json','execution-commands.md','README.md','root-reproduction-binding-20261007.json','root-visual-reading-scope-addendum-20261007.json'):add(D/name)
for p in sorted((D/'evidence').iterdir()):add(p)
for name in ('P16.4-round189-whole-genus-zero-review-binding-20261007.json','P16.4-round189-actual-canonical-independent-review-20261007.json','P16.4-round189-native-model-final-review-20261007.json','P05.2-round194-exact-native-final-unregistered-20261007.json','P05.2-round194-unregistered-author-and-whole-paper-binding-20261007.json','P16.4-continuation244-proper-completion-and-projective-field-GAGA-primary-reading-20261007.json','P16.4-continuation245-direct-formal-FS-recognition-and-horizontal-extension-working-route-20261007.json','P16.4-continuation246-formal-residual-bundle-and-raw-MA-coefficient-primary-application-20261007.json'):add(K/name)
add(K/'public-P16.4-continuation243-target-integrability-incidence-and-local-formal-bridge/builtin-public-source-unverified-request-addendum-20261007.json')
for n in (195,196):
    c=next((R/f'campaigns/round-{n}').iterdir())
    for name in ('freeze.json','mathematical-data-bindings.json','launch-record.json'):add(c/name)
for name in ('bind_and_accept_genus_zero227_review189_20261007.py','bind_and_reproduce_finite_contact247_20261007.py','prepare_finite_contact247_review196_20261007.py','launch_frozen_finite_contact_review196_20261007.py','prepare_original_equation195_after_direct_formal_FS_bridge_20261007.py','launch_frozen_original_equation195_after_direct_formal_FS_20261007.py','retrieve_completion_and_GAGA_primary244_20261007.py','write_primary_comparison244_and_direct_FS245_20261007.py','write_formal_residual_curvature246_primary_application_20261007.py','record_verified201_20261007.py'):add(R/name)
add(G/'push-receipt-continuation201.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=76,commit_message='Accept whole genus-zero equation and preserve finite PA contact proof for review',scope='Whole189/227 independent PASS accepted76, exact native/canonical/frozen bindings and whole grants plus harmless clarifications. Original complete-field genus-zero equation all targets and every-solution all-point uniqueness; general original still open. Native194 exact unregistered five-note final and whole693LF TeX/710LF argument/62LF ledger/214LF checker copied, four primary and41 artifact hashes validated, registration error B225 explicitly preserved, no canonical author result. Finite examples reproduce raw8,4,4/contact-2, two local builds clean, builtin request pending/unverified; no new mathematical acceptance. Root244/245/246 quote-free whole-primary reading scopes and actual same-bundle direct formal-FS/raw residual coefficient working route. Original195 and whole247 reader196 launched native61xhigh, max2, public statuses only. Full original primary PDF/text and original dossier bodies remain private.9/42originals solved33open76accepted; no original closure. Editor and login/runtime unchanged.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[i['round'] for i in active],accepted_papers=76),indent=2))
