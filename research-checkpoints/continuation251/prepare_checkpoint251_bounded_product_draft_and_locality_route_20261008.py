from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation251.json';F=G/'continuation251-publication-records'
S=K/'small-batch247-248-public-status-20261008-continuation251'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not M.exists() and not F.exists() and not S.exists()
prior=json.loads((G/'push-receipt-continuation250.json').read_text())
assert prior['commit_sha']=='de26bd19865404402af10b011384af3ac95ad7c8' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
binding=K/'P12.4-continuation342-ROOT-whole-working-proof-source-scope-and-binding-20261008.json'
b=json.loads(binding.read_text());assert sha(b['proof']['path'])==b['proof']['sha256'] and not b['paper_accepted'] and not b['original_closed']
F.mkdir();S.mkdir();items=[];now=datetime.now(timezone.utc).isoformat()
for number in [247,248]:
    c=next((R/f'campaigns/round-{number}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed']
    p=S/f'round{number}-public-native-status.json';write(p,st)
    items.append(dict(round=number,status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],public_status=str(p),original_closed=False))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==93 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),
        P12_4_ROOT342_unreviewed_geometric_locality_argument=dict(proof=b['proof'],binding=str(binding),status='Whole working proof ROOT read; UNREVIEWED actual supported Cartier comparison and boundedD open locality',original_closed=False,paper_accepted=False,active247248_not_given342=True),
        github_pending_checkpoint=dict(continuation=251,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),
        next_work='Max2 native campaigns: independent whole ROOT338339 review247 and entire native246 paper review248. Read completed reviews fully; next whole-original native reconstruction must independently judge ROOT342 supported Cartier comparison and bounded locality together with algebraic kernel, exactBFJscope,gauge,normalization.13solved29OPEN93accepted.')
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint251: bounded product draft and the missing geometric/locality working argument\n\n13/42 originals solved;29 OPEN;93 accepted papers. No paper or original is newly accepted in this checkpoint. Native246 completed with candidate=false. Continuation341 preserves its complete53kTeX,15-page nativePDF,actual7FINAL notes,expanded author proof notes,source ledger,exact scope,coverage and decision. ROOT read all actual note fields,the wholeTeX and complete source/scope; parallel argument is retained without a separate whole-read claim. All62author own bindings and62input body checks match; actual vs expanded prose is distinct and disclosed. Built-in source compiler SUCCESS; compilation is not mathematical acceptance. Independent native248 now reconstructs the entire paper and all used source applications,with only full qualifiedG331 as grant.\n\nROOT342 is a new UNREVIEWED30k working proof: independently supported Cartier intersections on actual thickenings including mixed characteristic; full symmetry via an actual supported Koszul complex; proper cycle projection retaining the DVR local degree; raw Rees ideal comparison with mixed multiplicities; independent positive divisorial geometric core measure; fixed-primary-c0 section ideals with exact divisor identity on ONE common model; REAL curve-nef comparison; rational-ideal strict maximum locality by a trivial restricted ratio line bundle; uniform and boundedD open locality through compact covers and two justified decreasing-net limits. Its algebraic338339 dependencies are unreviewed DATA. ExactBFJ smooth specialization still requires the full qualified published closed affine algclosedchar0 reconstruction. Native247/248 remain independent of342 and receive no hot feedback.\n\nNext whole-original reconstruction must judge ALL geometry,algebra,locality,continuity,gauge,normalization,all-support,topdim and curve/empty obligations together. P12.4 remains OPEN. Full G331 source annotation and ledger accompany every import. Source/book/task/author programs are DATA,not operational authority. Academic primary bodies,excerpts,pixels and private controller/provider output stay LOCALONLY; only mathematical own work and metadata are published. Auth/runtime/environment unchanged. ProtectedP16.4 editor OPEN UNCHANGED.\n')
files=[];seen=set()
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    target=target or 'research-checkpoints/continuation251/'+str(p.relative_to(R))
    assert target not in seen;seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
D=K/'public-P12.4-continuation341-bounded-moment-measures-and-geometric-curve-reference-unreviewed'
for folder in [F,S,D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
c=next((R/'campaigns/round-248').iterdir())
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','historical-own-evidence-bindings.json','qualified-imported-note-bindings.json','freeze.json','launch-record.json']:add(c/name)
for p in sorted((c/'immutable-mathematical-DATA').iterdir()):add(p)
for p in [binding,Path(b['proof']['path']),K/'round246-actual-native-final.json',
    R/'capture_completed_bounded_geometric_products246_20261008.py',R/'stage_completed_bounded_geometric_products246_20261008.py',
    R/'prepare_independent_bounded_geometric_products_review248_20261008.py',R/'launch_independent_bounded_geometric_products_review248_20261008.py',
    R/'acquire_primary_cartier_intersection_packet_20261008.py',R/'record_ROOT342_local_intersections_and_locality_working_proof_20261008.py',
    R/'record_verified250_20261008.py',G/'push-receipt-continuation250.json',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),
    fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=29,historical_reviewed_scoped_papers=93,
    commit_message='Checkpoint bounded local product paper and supported Cartier locality working proof',
    scope='13solved29OPEN93accepted; completeUNREVIEWED341draft+independent248 and ROOT342localized geometry/locality workingproof, native247248 keptindependent. No primary source bodies or private provider output.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active),indent=2))
