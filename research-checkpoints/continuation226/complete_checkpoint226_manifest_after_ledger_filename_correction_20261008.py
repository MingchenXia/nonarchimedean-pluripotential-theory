from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
D=K/'public-P05.1-continuation292-isolated-affine-crossings-global-real-regularization'
C=R/'campaigns/round-222/P05.1-unchanged-independent-common-subspace-pages-whole-native-local-source-audit'
M=G/'upload-manifest-continuation226.json';F=G/'continuation226-publication-records';S=K/'small-batch221222-public-status-20261008-continuation226'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not M.exists() and F.is_dir() and S.is_dir()
prior=json.loads((G/'push-receipt-continuation225.json').read_text())
assert prior['commit_sha']=='6d5e6e9d461447b3425ba5804990203a3d09ac3e' and all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
acc=D/'whole-mathematical-paper-acceptance-after-audit220-20261008.json';a=json.loads(acc.read_text());assert a['cumulative_accepted_paper_number']==84
j=json.loads((R/'active-work.json').read_text());assert j['github_pending_checkpoint']['continuation']==226 and j['historical_reviewed_scoped_papers']==84
now=datetime.now(timezone.utc).isoformat();active=j['current_small_batch']['active_items']
failure=F/'initial-manifest-filename-failure.json'
write(failure,dict(recorded_utc=now,initial_helper=str(R/'prepare_checkpoint226_whole_isolated_crossings292_20261008.py'),initial_helper_sha256=sha(R/'prepare_checkpoint226_whole_isolated_crossings292_20261008.py'),exit_code=1,cause='Manifest referenced missing source-ledger.md; actual immutable author filename is source-application-ledger.md.',front_and_public_status_records_already_saved=True,no_upload_attempted=True,no_mathematical_source_change=True,no_checks_or_builds_repeated=True,completion_only=True))
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation226/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for p in [D/'P05.1-paper.tex',D/'argument.md',D/'P05.1-paper.pdf',D/'source-application-ledger.md',D/'scope-and-gaps.md',D/'root-reproduction-binding-20261008.json',acc,Path(a['reader_clarifications']),Path(a['review_binding'])]:add(p)
for p in sorted((D/'evidence/independent-local-audit220').rglob('*')):
    if p.is_file() and p.suffix not in ['.pdf','.aux','.out','.log']:add(p)
for name in ['task.json','input.json','settings.json','freeze.json','original-task.json','mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json','launch-record.json']:add(C/name)
for name in ['extract_settled220_exact_native_result_20261008.py','bind_whole_isolated_crossings292_after_audit220_20261008.py','launch_common_subspace_whole_audit222_20261008.py','record_verified225_20261008.py']:add(R/name)
add(G/'push-receipt-continuation225.json');add(R/'prepare_checkpoint226_whole_isolated_crossings292_20261008.py');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=84,commit_message='Accept whole isolated-affine-crossing regularization and launch independent common-subspace audit',scope='Whole unchanged17p454LF S292 and independent220actualFINAL/report/source/history checked; locator conventions clarified, nativeuniversalhistoryINCONCLUSIVE retained.222 wholeunchanged295 unbiased audit launched after220slotfree;221dependentcommonH remains.9solved33open84accepted; builtinpending protectededitorunchanged. Exact noforce blob/tree/refverification.'))
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=84),indent=2))
