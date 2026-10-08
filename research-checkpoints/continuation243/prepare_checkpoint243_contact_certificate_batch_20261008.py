from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
C=next((R/'campaigns/round-239').iterdir())
M=G/'upload-manifest-continuation243.json'; F=G/'continuation243-publication-records'
S=K/'small-batch238-239-public-status-20261008-continuation243'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation242.json').read_text())
assert prior['commit_sha']=='79f007ee717f62ced9ae236a278a0157bc34f1f0'
assert not prior['force_update'] and all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
f=json.loads((C/'freeze.json').read_text()); assert (C/'launch-record.json').is_file() and f['structured_imported_notes_count']==8
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256')]:assert sha(C/name)==f[key]
for name in ('mathematical-packet-bindings.json','private-primary-packet-bindings.json'):
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n,atom in ((238,'P12.2'),(239,'P05.2')):
    old=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom=atom,observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(old),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[238,239],maximum_concurrent_campaigns=2,accepted_paper_number=89)
for name in ('active-work.json','checklist-current.json'):
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==11 and x['remaining_open_original_atoms']==31 and x['historical_reviewed_scoped_papers']==89 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,current_small_batch=batch,current_active_batch=[e['round'] for e in active],github_pending_checkpoint=dict(continuation=243,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    if name=='checklist-current.json':
        x['active_atoms']=[e['atom'] for e in active]
        t=next(t for t in x['targets'] if t['id']=='P05.2');assert not t['fully_solved'] and t['closure']=='open'
        t.update(research_status='whole original finite-carrier PCC-tree/raw-contact certificate239 active',current_focus='Accepted O323 original regularity supplies exact operator-domain bridge; UNREVIEWED ROOT327 finite carrier/geometry/tree/raw intersection proposal is independently reconstructed in239. ALLC_b contact, source geometry and meaningful original classification must be proved. P05.2 remainsOPEN.')
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint243: two-original small batch and contact certificate proposal\n\n11/42 original problems solved;31OPEN;89 accepted original/scoped papers. Previous242 was independently file/tree/ref verified at commit79f007ee717f62ced9ae236a278a0157bc34f1f0. No new original or paper acceptance in this checkpoint.\n\nNative238 independently reconstructs originalP12.2 geometric-cone comparison, full conductor descent and smooth BFJ with ZERO grants, exact corrected Keeler/Stacks sources and whole unreviewed326. Native239 independently seeks originalP05.2 all-obstacle contact classification with eight WHOLE qualified registered support Notes, including newly accepted originalP05.1 O323 with both mandatory annotations. Its39whole mathematical files610346B and four primary files are frozen.\n\nNEWROOT327 is explicitly UNREVIEWED mathematical DATA: finite-carrier PC rows, geometric finite PCC-tree near-maximality and directly saturated raw top intersection contact certificates are proposed as a meaningful input-only infinite iff classification, with genuine completed-domain construction and ALLC_b extension. None of these new assertions is granted. Mathematical/source/noncircularity/original-scope review is required before closure. No finite algorithm or universal regularity is claimed.\n\nAt most two native gpt-6.1-sol xhigh campaigns; actual public status snapshots included. Native private ACTIVE outputs, credentials, third-party full primary texts/PDFs/pixels and supplied executable code are excluded. Source metadata and full owned research proposals/qualified papers are public. Historical FAIL/INCONCLUSIVE records are preserved; no authentication/runtime/editor changes. ProtectedP16.4 editor remains open unchanged.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation243/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S):
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for name in ('freeze.json','launch-record.json','task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','qualified-imported-note-bindings.json','private-primary-packet-bindings.json'):add(C/name)
for e in json.loads((C/'mathematical-packet-bindings.json').read_text()):add(e['path'])
for p in (K/'P05.2-continuation327-finite-carrier-PCC-tree-and-raw-contact-certificate-working-proposal-20261008.md',G/'push-receipt-continuation242.json',R/'record_verified242_20261008.py',R/'prepare_original_contact_certificate239_20261008.py',R/'launch_original_contact_certificate239_20261008.py',Path(__file__)):add(p)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=31,historical_reviewed_scoped_papers=89,commit_message='Research full polyhedral contact certificates alongside geometric conductor reconstruction',scope='11solved31OPEN89accepted; original238/239 at most2; ROOT327 unreviewed and eight whole qualified contact239 grants frozen.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=11,originals_open=31,accepted_papers=89),indent=2))
