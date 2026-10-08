from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation238.json'; F=G/'continuation238-publication-records'
S=K/'small-batch234235-public-status-20261008-continuation238'
C=next((R/'campaigns/round-235').iterdir())
D=K/'public-P05.1-continuation318-free-attachment-multiple-overlap-regularization-unreviewed'
W=K/'P12.2-continuation317-inductive-bounded-conductor-and-finite-descent-working-proof-20261008.md'
B=K/'round233-whole-draft-ROOT-reading-and-classification-continuation-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation237.json').read_text())
assert prior['commit_sha']=='595e0cd1c3faf5edf10ada2c4885abb9399f688e' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
f=json.loads((C/'freeze.json').read_text()); assert (C/'launch-record.json').is_file()
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256')]:assert sha(C/name)==f[key]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert f['structured_imported_notes_count']==5 and f['whole_math_files']==40
assert sha(D/'P05.1-paper.tex')=='ce7d658b740c6043d4a1b60b823904183a5feca233dd4d15a11740de96d8cebc'
assert sha(D/'P05.1-paper.pdf')=='26da53f1c61408cbdb7a814204a5a60913a8db68ca1317383a25b9c6836de950'
F.mkdir(); S.mkdir(); now=datetime.now(timezone.utc).isoformat(); items=[]
for n,atom in [(233,'P05.1'),(234,'P12.2'),(235,'P05.1')]:
    old=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json'; write(p,st)
    items.append(dict(round=n,atom=atom,observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(old),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0]; assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[234,235],maximum_concurrent_campaigns=2,accepted_paper_number=88)
p=D/'ROOT-public-draft-status-20261008.json'; x=json.loads(p.read_text())
x.update(built_in_compiler_status='requested once; completion unverified at checkpoint freeze',built_in_compile_cell=363,editor_new_tab_not_opened=True); write(p,x)
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=json.loads(p.read_text())
    assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(continuation=238,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),P05_1_completed_multiple_overlap_native233=dict(public_draft=str(D),reading_binding=str(B),actual_FINAL=str(K/'round233-actual-native-final.json'),native_registration_valid=True,whole_ROOT_paper_and_five_notes_read=True,own_hashes_verified=43,frozen_hashes_verified=35,new_accepted_paper=False,original_closed=False),P05_1_original_classification_research235=dict(directory=str(C),full_registered_qualified_notes=5,whole_math_files=40,whole_math_bytes=f['whole_math_bytes'],native233_and_ROOT315_unreviewed_DATA_only=True,model='gpt-6.1-sol',reasoning='xhigh',original_closed=False),P12_2_bounded_conductor_working317=dict(path=str(W),sha256=sha(W),bytes=W.stat().st_size,whole_ROOT_physically_read=True,unreviewed=True,fed_native234=False,general_bounded_inductive_image_proposed=True,unbounded_completion_not_proved=True,background_integral_dependence_and_normal_trace_validation_pending=True,new_accepted_paper=False,original_closed=False))
    if name=='checklist-current.json':
        x['active_atoms']=[e['atom'] for e in active]
        for atom,focus in [('P05.1','Original coefficient-separated classification research235: full original ambient/literal/compact/real/all-C_b scope, noncircular costed dual and finite carrier matrix criterion. Five full qualified imported Notes; whole new native233 multiple-overlap draft318 and ROOT315 are UNREVIEWED DATA.'),('P12.2','Original unbounded geometric/smooth/conductor research234 remains frozen with ZERO grants. New ROOT317 independently proposes bounded conductor and arbitrary finite-injection descent by dimension induction and approximate quotient ideal matching; not fed active234, unreviewed, no unbounded descent claim.')]:
            t=next(t for t in x['targets'] if t['id']==atom); t['research_status']='original research active; latest draft unreviewed'; t['current_focus']=focus
    write(p,x); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint238: several-overlap regularization and bounded conductor research\n\n10/42 original atoms solved;32OPEN;88accepted mathematical papers. No acceptance or original closure is made here.\n\nNative233 completed valid registration, candidatefalse, with a new16-page paper318 proposing REAL-PA regularization for finite free attachments of dependent complete affine page groups. Several distinct positive-dimensional overlaps are allowed, old values stay fixed, every trace subgradient lifts, and supports match at every real point on entire incident pages/cells. ROOT read the entire author TeX, allfiveactualFINAL notes, source/scope/coverage/author-review and verified43own+35frozenhashes. This is UNREVIEWED and does not classify arbitrary proper domains or nonfree/cyclic arrangements. Author checks/builds are not ROOT executions or mathematical certification. Builtincompile363 was requested once, completion unverified at freeze; P16.4 editor remains open and unchanged.\n\nNative235 uses FIVE unchanged complete qualified caller-imported Notes with every mandatory annotation, plus native233 and ROOT315 as whole UNREVIEWED DATA. It targets the whole original coefficient-separated classification, noncircular costed weak-star/finite-matrix certificates, allC_b obstacles and exact original compact/literal scope. Native234 continues frozen originalP12.2 unbounded geometric/fullsmooth/conductor research with ZERO grants. Max2active native campaigns; no private active output or hot feedback.\n\nROOT317 independently proposes general BOUNDED normalization/conductor and finite-injection descent of uniform ideal cones in excellent reduced local rings. It handles conductor-infinite points by dimension induction and approximate quotient ideal matching, using conductor/N only at finite-conductor points. Normal-target norm traces and the ideal-integral-dependence criterion remain background validation gates; numerical-nef transfer also requires the separate unaccepted comparison. It does NOT prove unbounded completed descent. ROOT317 is UNREVIEWED, not fed active234, and does not change counts.\n\nFull external primary PDF/text/images remain LOCALONLY; public source metadata and qualified owned papers are included. All uploads are authorized; no force update; exact remote file/tree/ref verification follows the frozen manifest.\n')
files=[]
def add(p,target=None):
    p=Path(p); assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation238/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S,D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for name in ['freeze.json','launch-record.json','task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:add(C/name)
for e in json.loads((C/'mathematical-packet-bindings.json').read_text()):add(e['path'])
for p in [W,B,K/'round233-actual-native-final.json',G/'push-receipt-continuation237.json',R/'record_verified237_20261008.py',R/'capture_completed_balanced_simultaneous_research233_20261008.py',R/'prepare_original_polyhedral_classification235_20261008.py',R/'launch_original_polyhedral_classification235_20261008.py',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=32,historical_reviewed_scoped_papers=88,commit_message='Preserve multiple-overlap regularization draft and continue original dual and conductor research',scope='10solved32OPEN88accepted; new16p318draft unreviewed, native234/235 max2active; ROOT317 bounded conductor/finite-injection working proof, no new acceptance or original closure.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],statuses=[dict(round=e['round'],status=e['observed_status']) for e in items],originals_solved=10,originals_open=32),indent=2))
