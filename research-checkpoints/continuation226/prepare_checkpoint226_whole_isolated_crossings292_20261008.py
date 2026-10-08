from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
D=K/'public-P05.1-continuation292-isolated-affine-crossings-global-real-regularization'
C=R/'campaigns/round-222/P05.1-unchanged-independent-common-subspace-pages-whole-native-local-source-audit'
M=G/'upload-manifest-continuation226.json';F=G/'continuation226-publication-records';S=K/'small-batch221222-public-status-20261008-continuation226'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation225.json').read_text())
assert prior['commit_sha']=='6d5e6e9d461447b3425ba5804990203a3d09ac3e' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
acc=D/'whole-mathematical-paper-acceptance-after-audit220-20261008.json';a=json.loads(acc.read_text())
assert a['cumulative_accepted_paper_number']==84 and not a['original_closed'] and a['native_universal_history_INCONCLUSIVE_retained']
for p,k in [(a['source'],'source_sha256'),(a['argument'],'argument_sha256'),(a['pdf'],'pdf_sha256'),(a['review_binding'],'review_binding_sha256'),(a['reader_clarifications'],'reader_clarifications_sha256')]:assert sha(p)==a[k]
assert (C/'launch-record.json').exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
coverage=(D/'evidence/independent-local-audit220/wholeproof-and-premise-coverage.md').read_text()
units=[l for l in coverage.splitlines() if l.startswith('| ') and 'PASS within scoped domain' in l]
displays=[l for l in coverage.splitlines() if l.startswith('| ') and '| PASS;' in l]
assert len(units)==17 and len(displays)==41
F.mkdir();S.mkdir();now=datetime.now(timezone.utc).isoformat();items=[]
for n in [220,221,222]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom='P05.1',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
assert items[0]['observed_status']=='completed' and items[0]['unsettled_calls']==0
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,accepted_paper_number=84,original_closed=False,focus='220 entire isolated292 mathematical audit checked and S292 accepted;221 dependent common-H joint-dual author;222 unchanged295 independent common-H audit launched with frozen unbiased packet. All general original gaps remain.')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers']==84 and len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None and j['github_checkpoint']['commit_sha']==prior['commit_sha']
    j.update(updated_utc=now,current_small_batch=batch,settled220_whole_audit_checked=dict(actual_FINAL=str(K/'round220-actual-native-final.json'),actual_FINAL_sha256=sha(K/'round220-actual-native-final.json'),all6_whole_ROOT_read=True,whole_report_unique_contents_and_17_units_41_displays_ROOT_read=True,mathematics='PASS',source_application='PASS with explicit splitlines-record versus literal-LF locator clarification',required_reproduction='PASS',universal_retrospective_history='INCONCLUSIVE',acceptance=str(acc),original_closed=False),next_work='After PUBLIC221 settles, extract controlling actualFINAL and whole new paper into reserved continuation298, read complete source/notes/ledger/scope/evidence, independently verify safe finite checks/build/source conversion before scoped acceptance. Keep222 unbiased whole295 audit running; no third campaign. Continue general all-face compatibility and globalLip derivation with complete296/297 working data, and remaining33original goals. Regular verified pushes; pending builtin62/94/136 wait only; protected editor open unchanged.',github_pending_checkpoint=dict(continuation=226,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    write(p,j);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint226: whole isolated-affine-crossing regularization paper accepted\n\n9/42 original problems solved,33 open,84 accepted scoped/supporting papers. Whole unchanged17-page454-LF continuation292 and all6 controlling authorFINAL have passed an independent native gpt-6.1-sol xhigh mathematical reconstruction and ROOT whole mathematical checks, conditional on exactly5whole grants/allclarifications. S292 covers arbitrary positive REAL weights and actual REAL positive-growth references on finite complete rational equal-dimensional planes with pairwise empty or point intersection, including dependent branches and multiple distinct meetings. Branchconvexity plus common ambient supports is equivalent to continuousPC on every inherited carrier. Global rational-spatial/real-height majorants preserve exact actual recession and any finite rational contacts, then a common4dyadic shift gives globally decreasing genuineREAL regularization for ALL continuousrelativePC functions and ALL-C_b ACTUAL envelopes before MA. Whole primitive signed/zero recursion, all-dimensional covolume conversion, BBGS commutation/refinement/balance, raw positivity/mass/IBP/determinants and every-crossing/every-reference finite-PA negativecontact roofs are reconstructed.\n\nAll6 independent actualFINAL are controlling, savedJSON differs only by one terminalfile newline. Entire report/source/history unique content was read; exact duplicatedparagraphs are bound separately. Whole17contiguousunits and41displays cover numbered and unnumbered claims. All93frozen and55own identities match; safe finite code/input/output agrees exactly with prior ROOT once-only reproduction, no redundant tests/builds. Whole finite output was read. Two prior ROOT local builds0/0, firstreference warnings retained, final clean17pages; whole correct standaloneMarkdown exact and original wrongGFM failure preserved. No PDFvisual proof check or builtincompile success claimed.\n\nSource row-number clarification is explicit: native220 read_primary uses Python splitlines which also splits formfeeds; its LF labels are extractedrecords. Exact BBGS record615-682 maps to literalLF604-670 and complete3.15 ending. Other named-unit mappings are saved. Contents were whole-read. BMPS formalrationalweights versus reconstructedREAL extension, fullBBGS paired double-sum, source3.19 reference slip and harmless literalqquad separator are explicit. Native mathematical/sourcePASS and concretehistorical reproductionPASS remain; universal retrospective did-read/no-operation claims remainINCONCLUSIVE. Neither draftnativeverdict nor ROOTscopedacceptance closes originals or certifies all historical operations.\n\n222 independently audits unchangedwhole295 with frozen33math99history4primary and exactly6wholegrants/allqualifications. It was launched onlyafterPUBLIC220completed;221 dependentcommon-H author remains the other slot. No priorreviewbias, newS291/S292/dependentproof feedback or runtimeauth changes. General positive-dimensional overlaps, singularsupports, nonseparableproducts, broaderabstractcompact/literal categories/fullclassification and non-PAcontact sufficiency remainOPEN. WholeROOT296 singlecellLip construction and297 unbalancedboundary errorfloor remain UNREVIEWED data.\n\nExisting protected editor stays open unchanged; builtin62/94/136 pending, wait only. No supplied auditor emitter/orchestrator/binder/build script executed; no originalsourcequotes/pixels/privateACTIVE/controllerstreams/auth uploads. No-force push requires exact remote blobs/nativeGitTree/ref verification.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation226/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for p in [D/'P05.1-paper.tex',D/'argument.md',D/'P05.1-paper.pdf',D/'source-ledger.md',D/'scope-and-gaps.md',D/'root-reproduction-binding-20261008.json',acc,Path(a['reader_clarifications']),Path(a['review_binding'])]:add(p)
for p in sorted((D/'evidence/independent-local-audit220').rglob('*')):
    if p.is_file() and p.suffix not in ['.pdf','.aux','.out','.log']:add(p)
for name in ['task.json','input.json','settings.json','freeze.json','original-task.json','mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json','launch-record.json']:add(C/name)
for name in ['extract_settled220_exact_native_result_20261008.py','bind_whole_isolated_crossings292_after_audit220_20261008.py','launch_common_subspace_whole_audit222_20261008.py','record_verified225_20261008.py']:add(R/name)
add(G/'push-receipt-continuation225.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=84,commit_message='Accept whole isolated-affine-crossing regularization and launch independent common-subspace audit',scope='Whole unchanged17p454LF S292 and independent220actualFINAL/report/source/history checked; locator conventions clarified, nativeuniversalhistoryINCONCLUSIVE retained.222 wholeunchanged295 unbiased audit launched after220slotfree;221dependentcommonH remains.9solved33open84accepted; builtinpending protectededitorunchanged. Exact noforce blob/tree/refverification.'))
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=84),indent=2))
