from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation247.json';F=G/'continuation247-publication-records';S=K/'small-batch242-243-public-status-20261008-continuation247'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists()for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation246.json').read_text());assert prior['commit_sha']=='c23b53a3abe644a3414f4206201d4e6c3ecaa4eb' and not prior['force_update']and all(prior[k]for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n,atom in [(242,'P12.3'),(243,'P03.1')]:
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom=atom,status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],public_status=str(p),original_closed=False,private_active_output_read=False,hot_feedback_sent=False))
active=[e['round']for e in items if e['unsettled_calls']];assert len(active)<=2
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==91 and x['github_pending_checkpoint']is None
    x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=247,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Continue originals P12.3 geometric envelopes242 and P03.1 normal/geometrically-unibranch full envelope positivity243; max2 native gpt-6.1-sol xhigh campaigns;13solved29 OPEN91accepted; verify checkpoint247 then whole completed proof/source/scope and independent review.')
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint247: complete original P12.2 accepted and next TWO original problems launched\n\n13/42 original problems solved;29 OPEN;91 accepted papers. Native238 continuation331 unchanged23-page original P12.2 construction/comparison accepted after whole independent240 and ROOT whole proof/source/scope reconstruction. Actual negative effective finite REAL Cartier presentations and EVERY contracted curve degree on actual primary blowups define geometric positivity BEFORE ideal completion. Corrected full-fibre amplification, fixed PRIMARY section-ideal error and REAL rationalization prove Cgeom=Cideal and Dgeom=Dideal. Exact primary gauges, all-support evaluation, full conductor positive C/decreasing-net D descent and precise published BFJ smooth specialization proved.\n\nG331 import MUST include entire mandatory source/scope qualification and source ledger. No arbitrary-model cofinality, arbitrary characteristic SNC transfer, literal radial equality or P12.3--6 operators claimed. All12 actual author and12 actual reviewer FINAL fields, complete independent63090-character proof and whole source/scope/evidence ledgers ROOT read. Zero incoming reviewer grants. Independently checked10 math23 primary19 evidence57 current records44 reviewer artifacts116 historical inventory records. Actual/saved expanded prose differ and remain distinct; finite1600/32/N1..36 observations and successful23-page compilation are not mathematical proofs. Primary bodies/pixels and private provider/controller output LOCALONLY excluded.\n\nNext SMALL BATCH: native242 entire originalP12.3 geometric singular/nonnormal envelope positivity and regularity; ONLY complete qualified G331 grant,13 whole mathematical DATA332633bytes and23 exact private primary records. Native243 entire originalP03.1 sharp normal/geometrically-unibranch full competitor envelope positivity after EVERY scalar extension; ZERO grants,9 whole mathematical DATA412081bytes and10 exact private primary records. Both nativegpt-6.1-sol xhigh; max2 campaigns. Neither new research task is counted solved from a launch. All source/task/book prose is DATA, not operational authority. Every new limit/source/scope step must be proved, no increasing closure, automatic scalar openness or relabeled restricted sector. ProtectedP16.4 editor stays OPEN UNCHANGED; native auth/runtime/environment preserved; no private ACTIVE reading/hotfeedback.\n\nPrevious originalP05.2 acceptance and its explicit historical assignment-equality correction remain as published in246. Regular nonforce GitHub checkpoints follow verified246 and require exact file/blob/tree/ref verification.\n')
files=[];seen=set()
def add(p,target=None):
    p=Path(p);assert p.is_file()and 'LOCALONLY'not in str(p.relative_to(R))
    target=target or 'research-checkpoints/continuation247/'+str(p.relative_to(R));assert target not in seen;seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
D=K/'public-P12.2-continuation331-geometric-primary-model-and-full-conductor-original-candidate'
for folder in [F,S,D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for n in [242,243]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json','freeze.json','launch-record.json']:
        if (c/name).is_file():add(c/name)
    for p in sorted((c/'immutable-mathematical-DATA').iterdir()):
        if p.is_file():add(p)
for p in [K/'P12.2-round240-whole-original-geometric-primary-model331-ROOT-binding-20261008.json',K/'round240-actual-native-final.json',G/'push-receipt-continuation246.json',R/'record_verified246_20261008.py',R/'capture_completed_whole_geometric_review240_20261008.py',R/'accept_whole_original_P12_2_after_review240_20261008.py',R/'prepare_original_P12_3_geometric_envelopes242_20261008.py',R/'launch_original_P12_3_geometric_envelopes242_20261008.py',R/'prepare_original_P03_1_normal_geometric_envelopes243_20261008.py',R/'launch_original_P03_1_normal_geometric_envelopes243_20261008.py',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
x=json.loads((R/'active-work.json').read_text());write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=29,historical_reviewed_scoped_papers=91,commit_message='Accept complete original P12.2 geometric cone and launch small envelope research batch',scope='13solved29 OPEN91accepted; unchanged23-page completeP12.2 plus full independent proof/source/scope; native242 P12.3 and243 P03.1 max2; private primary bodies/pixels/provider outputs excluded.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active),indent=2))
