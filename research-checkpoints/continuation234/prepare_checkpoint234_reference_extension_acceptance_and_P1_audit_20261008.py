from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation234.json'; F=G/'continuation234-publication-records'; S=K/'small-batch229230-public-status-20261008-continuation234'
D=K/'public-P05.1-continuation307-compatible-affine-reference-extension-and-sharp-global-restriction-distance'
C=next((R/'campaigns/round-229').iterdir()); E=next((R/'campaigns/round-230').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,j:Path(p).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation233.json').read_text())
assert prior['commit_sha']=='aa989fc0954c04ea83818d033a6523abb907e5ed' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
accepted=json.loads((D/'whole-mathematical-paper-acceptance-after-audit228-20261008.json').read_text())
assert accepted['cumulative_accepted_paper_number']==87 and not accepted['original_closed'] and accepted['both_annotations_required_on_import']
assert sha(D/'P05.1-paper.tex')==accepted['source_sha256'] and sha(D/'P05.1-paper.pdf')==accepted['pdf_sha256']
for c in [C,E]:
    f=json.loads((c/'freeze.json').read_text()); assert f['only_grants']==[] and (c/'launch-record.json').is_file()
    for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('historical-own-evidence-bindings.json','historical_own_evidence_bindings_sha256')]: assert sha(c/name)==f[key]
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir(); S.mkdir(); now=datetime.now(timezone.utc).isoformat(); items=[]
for n in [228,229,230]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json'; write(p,st)
    items.append(dict(round=n,atom='P05.1' if n==228 else 'P14.8',observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(c),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
assert all(e['observed_status']=='completed' and e['unsettled_calls']==0 for e in items if e['round']==228)
active=[e for e in items if e['unsettled_calls']>0]; assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[229,230],maximum_concurrent_campaigns=2,accepted_paper_number=87,original_closed=False,prepared_P1_audit229_not_launched=False)
for filename in ['active-work.json','checklist-current.json']:
    p=R/filename; j=json.loads(p.read_text()); assert j['historical_reviewed_scoped_papers']==87 and len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,next_work='Continue exact general original P14.8 proof/source/meaningful-formal-data audit230 and independent projective-line arbitrary-formal-data theorem308 audit229. S307 accepts whole16p scoped mathematics WITH BOTH source and reader annotations, not original P05.1/P05.2. Further research must solve direct positive-balanced shared-face trace/support approximation; separate affine extensions fail at legal cost-1/4 and sharp error(A-1)/2.9solved33OPEN87supporting papers. Preserve frozen current native authentication and protected editor; maximum2 campaigns, regular verified pushes.',github_pending_checkpoint=dict(continuation=234,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    j['prepared_whole307_audit228'].update(completed=True,accepted_whole_scoped_paper_number=87,original_closed=False)
    j['prepared_P1_formal_ideal_audit229'].update(launched=True,launch_record=str(C/'launch-record.json'),launch_record_sha256=sha(C/'launch-record.json'))
    write(p,j); shutil.copyfile(p,F/filename)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint234: accept whole scoped compatible-reference extension and sharp-distance paper\n\n9/42 original problems solved;33OPEN;87accepted scoped/supporting papers. Whole16-pageS307 passes independent reconstructed mathematics and essential-source applications WITH BOTH mandatory annotations. Global-Lipschitz entire-cell extensions preserve actual-face supports, not automatic dependent gluing outside the actual face; legal cost-1/4 refutes that step. Compatible actual-AFFINE references extend to dependent complete pages sharing ONE H with EVERY-H common supports. For rationalA>=1 the all-continuous-competitor GLOBAL restriction error is exactly(A-1)/2 and is attained. The original partial target is alreadyPAandUNBALANCED, so this is no original balanced regularization counterexample. Direct shared-face approximation and originalP05.1/P05.2 remainOPEN.\n\nTwo immutable source-ledger descriptors are harmlessly inaccurate: BMPS886-894 is bounded-relative Definition3.14, and1741-1746 is positive recession Definition4.15; divisor positivity is691-695. The audit retains narrowly specified metadataFAIL alongside mathematical/essential-sourcePASS. Fresh bounded evidencePASS:1577finite assertions/-1/4, exact body-only source-to-Markdown, two unchanged no-shell clean16p builds. ROOT/all4actualFINAL and whole unique reconstruction/source/evidence/coverage read,64frozen134ownhashbindingsverified; supplied scripts not run for acceptance. Universal historical operations/did-read/externalruntime remainsINCONCLUSIVE.\n\nNativeXean gpt-6.1-sol xhigh campaigns229/230 are the only reserved current pair: independentP1criterion308 audit and generalP14.8formal-data candidate309 wholeproof/source/originalscope audit. No candidate automatically closes an original. Builtin54/81/90/134 pending, separate local builds verified. ProtectedP16.4editor unchanged/open, authentication preserved, document directives mathematicalDATA. Full third-party sources remainLOCALONLY.\n')
files=[]
def add(p,target=None):
    p=Path(p); assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation234/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S,D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file() and p.suffix not in ['.aux','.out','.toc']: add(p)
for p in [C/'launch-record.json',K/'P05.1-round228-whole-reference-extension307-mathematical-source-binding-20261008.json',R/'bind_whole_reference_extension307_after_audit228_20261008.py',R/'launch_projective_line_formal_ideal_whole_audit229_20261008.py',R/'extract_settled228_exact_native_result_20261008.py',R/'record_verified233_20261008.py',G/'push-receipt-continuation233.json',Path(__file__)]: add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']: add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=87,commit_message='Accept compatible affine reference extension and sharp global restriction distance with qualifications',scope='Whole scopedS307paper87WITH BOTH mandatoryannotations; native228complete,229230max2active generalP14.8andP1 audits;9solved33OPEN; noautomaticoriginalclosure, noforce, exactremoteverification, fullthirdparty sourcesLOCALONLY.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],accepted_papers=87,originals_solved=9,originals_open=33),indent=2))
