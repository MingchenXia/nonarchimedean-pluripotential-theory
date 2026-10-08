from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation245.json';F=G/'continuation245-publication-records';S=K/'small-batch240-241-public-status-20261008-continuation245'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists()for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation244.json').read_text())
assert prior['commit_sha']=='1ebf677734a444e776c6024bf2cf09684d930381' and not prior['force_update'] and all(prior[k]for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n,atom in ((240,'P12.2'),(241,'P05.2')):
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st);items.append(dict(round=n,atom=atom,observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(c),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[240,241],maximum_concurrent_campaigns=2,accepted_paper_number=89)
for name in ('active-work.json','checklist-current.json'):
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==11 and x['remaining_open_original_atoms']==31 and x['historical_reviewed_scoped_papers']==89 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,current_small_batch=batch,current_active_batch=[e['round']for e in active],github_pending_checkpoint=dict(continuation=245,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Continue independent whole originalP12.2review240 and P05.2review241; read actual final whole proof/source/scope before acceptance.11 solved31 OPEN89 accepted. Regular verified GitHub push245 pending; max2 campaigns.')
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint245: two complete original solution candidates and their independent whole reviews\n\n11/42 originals solved;31 OPEN;89 accepted papers. NO new acceptance from candidate flags, builds or hashes. Native238 P12.2 returns12 local proof notes and an unchanged23-page candidate331 with independent curve-nef primary-model/ideal comparison, full smooth specialization and conductor descent. Native239 P05.2 returns5notes and an unchanged14-page candidate332 with an infinite carrier/tree/primitive-polynomial iff criterion for genuine domain and exact ALLC_b contact. Both authoritative papers and actual final outputs, whole source/scope/coverage/decision and controlling original dossiers ROOT-read; private completed stdout excluded. P12.2 savedexpanded note prose differs from actual; P05.2 note fields match but newline serialization differs. Exact differences preserved.\n\nNative240 independently reviews ENTIRE originalP12.2, all12proofs/exactsourceapplications/meaningful independentgeometry/primarymodel scope. ZERO caller grants. Native241 independently reviews ENTIRE originalP05.2, all5proofs/exactsourceapplications/allCb-domain gates/infinite structural classification and compact original scope. Eight complete qualified caller Notes unchanged, BOTH O323annotations retained; candidate not granted. ROOT328 finite-vertex strengthening is separate UNREVIEWEDdata, not retroactively an author239input/premise. At most2active nativegpt-6.1-sol xhigh campaigns. Public status only for ACTIVEcalls, no hotfeedback/privateoutput.\n\nActual built-in compilation succeeded for both unchanged candidate sources with protectedP16.4 editor open unchanged and no newtabs. Independent identity audits verify238:77own+36frozen+39reportedinputs;239:33own+43frozen+47reportedinputs+8qualifiedtexts. Finiteauthorchecks/build histories are reproducibility observations only; initialwarnings/failures retained. All external primary bodies/images/excerpts and privatecontroller/provider outputs LOCALONLY excluded; only publicmetadata included. NewROOT330 gives independent all-support Cartier generation/uniform fixed-primary error working proof, no grant/originalclosure. HistoricalFAIL/INCONCLUSIVE preserved; no backend/billing/read-attestation fabricated. Regular GitHub publication follows verified244 via nonforce update, exact file/blob/tree/ref verification.\n')
files=[];seen=set()
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY'not in str(p.relative_to(R))
    target=target or 'research-checkpoints/continuation245/'+str(p.relative_to(R));assert target not in seen;seen.add(target)
    files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S,K/'public-P12.2-continuation331-geometric-primary-model-and-full-conductor-original-candidate',K/'public-P05.2-continuation332-carrier-tree-primitive-polynomial-whole-original-candidate'):
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for n in (240,241):
    c=next((R/f'campaigns/round-{n}').iterdir())
    for name in ('task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','historical-own-evidence-bindings.json','qualified-imported-note-bindings.json','freeze.json','launch-record.json'):
        if (c/name).is_file():add(c/name)
    for folder in (c/'immutable-mathematical-DATA',c/'immutable-own-evidence'):
        for p in sorted(folder.iterdir()):
            if p.is_file():add(p)
for p in [K/'P12.2-continuation330-all-support-generated-Cartier-sections-working-addendum-20261008.md',G/'push-receipt-continuation244.json',R/'record_verified244_20261008.py',R/'bind_candidate238_and_capture_completed239_20261008.py',R/'bind_whole_contact_candidate239_and_stage332_20261008.py',R/'prepare_original_geometric_candidate_whole_review240_20261008.py',R/'launch_original_geometric_candidate_whole_review240_20261008.py',R/'prepare_original_contact_candidate_whole_review241_20261008.py',R/'launch_original_contact_candidate_whole_review241_20261008.py',Path(__file__)]:add(p)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=31,historical_reviewed_scoped_papers=89,commit_message='Preserve complete P12.2 and P05.2 candidates and launch independent whole-original reviews',scope='11solved31 OPEN89accepted; full23p/14p unreviewed wholeoriginal candidates331332; unchanged frozen native240241,max2; primary bodies/privateoutputs excluded.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round']for e in active]),indent=2))
