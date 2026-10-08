from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation235.json';F=G/'continuation235-publication-records';S=K/'small-batch231-public-status-20261008-continuation235'
C=next((R/'campaigns/round-231').iterdir())
D=K/'public-P14.8-continuation309-general-formal-ideal-realization-candidate'
E=K/'public-P14.8-continuation308-arbitrary-formal-ideal-realization-on-projective-line'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation234.json').read_text())
assert prior['commit_sha']=='9c8be7be0e6e7f7ab7feeb29b4b2ed1599384a3f' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
accepted=json.loads((D/'whole-original-paper-acceptance-after-audit230-20261008.json').read_text())
assert accepted['original_closed'] and accepted['cumulative_accepted_paper_number']==88 and accepted['both_annotations_required_on_import']
assert sha(D/'P14.8-paper.tex')==accepted['source_sha256'] and sha(D/'P14.8-paper.pdf')==accepted['pdf_sha256']
repair=json.loads((E/'ROOT-representative-repair-and-build-binding-20261008.json').read_text())
assert sha(E/'P14.8-paper.tex')==repair['repaired_source_sha256'] and sha(E/'P14.8-paper.pdf')==repair['repaired_pdf_sha256']
f=json.loads((C/'freeze.json').read_text());assert f['whole_math_files']==24 and f['only_grants']==['B225','R230','S306','S307','S298']
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256')]:assert sha(C/name)==f[key]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
 for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir();S.mkdir();now=datetime.now(timezone.utc).isoformat();items=[]
for n in [229,230,231]:
 c=next((R/f'campaigns/round-{n}').iterdir())
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';write(p,st)
 if n in [229,230]:assert st['status']=='completed' and st['calls']['unsettled']==0
 items.append(dict(round=n,atom='P05.1' if n==231 else 'P14.8',observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(c),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed_by_current_ROOT_acceptance=(n==230)))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[231],maximum_concurrent_campaigns=2,accepted_paper_number=88)
work=K/'P05.1-continuation310-single-original-face-primal-synchronization-working-proof-20261008.md';assert work.is_file()
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert x['historical_reviewed_scoped_papers']==88 and len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['github_pending_checkpoint'] is None
 x.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(continuation=235,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),original_all_face_research231=dict(directory=str(C),freeze=str(C/'freeze.json'),freeze_sha256=sha(C/'freeze.json'),launch=str(C/'launch-record.json'),launch_sha256=sha(C/'launch-record.json'),whole_math_files=24,whole_math_bytes=367744,only_grants=f['only_grants'],original_closed=False),unreviewed_single_face_working310=dict(path=str(work),sha256=sha(work),bytes=work.stat().st_size,whole_ROOT_physically_read=True,new_accepted_paper=False,original_closed=False))
 write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint235: solve original P14.8 through arbitrary formal-data realization\n\n10/42 originals solved;32OPEN;88accepted mathematical papers, including original solutions and scoped support. Whole14-page continuation309 passes independent mathematical, essential-source, meaningful-original-scope and bounded-evidence review230. The chosen original alternative is an exact arbitrary-formal-data realization iff, at every real exponent, using restricted infinite holomorphic approximation/integrability witnesses. No realizability assumption, positive-mass restriction, finite algorithm, ideal-only algebraic axiom, canonical raw selection, P-data/mass reconstruction or extra DXZ interval. BOTH qualifications are mandatory. Componentwise finite assembly includes disconnected/point cases as explicitly annotated ROOT observations.\n\nAll6actual230notes and six complete unique expanded reports were ROOT-read;54frozen and29ownhashbindings verified; existing ROOT14pPDF independently rehashed. Main H/O/N/C applications PASS through directly read Demailly units. Auxiliary DEL/SO original editions remain conditional/INCONCLUSIVE, outside main dependencies. Retain847selectedchecks versus872literalassert evaluations, fence separatorLF,25/96auditor supplied inventory, actual/saved prose differences, historical warning gate and pending builtin compiler134. No checker/build repeated for acceptance.\n\nIndependent P1 audit229 found the one-point upward-spike error in unchanged source308 line105, independently proved the canonical a.e. representative repair and otherwise reconstructed the criterion. Its original FAIL is preserved with the pre-repair source/PDF. The existing source is now corrected, including the local representative argument, and separately rebuilt twice no-shell to a clean5pPDF; no new supporting-paper acceptance is inferred. Builtin revised228 remains unverified/pending.\n\nP05.1 general all-face research231 uses24whole math files367744bytes, five qualified complete grants, four primary DATA sources, and new ROOT310 unreviewed single-face primal synchronization. The next mathematical gap is simultaneous all-face trace/support compatibility. Native229230results were not fed231. At most2native campaigns; all configured gpt-6.1-sol xhigh. Auth/runtime and protected P16.4 editor preserved. Full third-party sources/images and active private outputs are excluded.\n')
files=[]
def add(p,target=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
 files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation235/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S,D,E,C/'immutable-mathematical-packet']:
 for p in sorted(folder.rglob('*')):
  if p.is_file() and p.suffix not in ['.aux','.out','.toc'] and 'LOCALONLY' not in str(p):add(p)
for name in ['freeze.json','launch-record.json','task.json','original-task.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json']:add(C/name)
for p in [work,K/'P14.8-round230-whole-original-formal-realization309-binding-20261008.json',K/'P14.8-original-formal-data-closure-after-audit230-20261008.json',K/'P14.8-round229-projective-line-representative-failure-binding-20261008.json',R/'bind_and_close_original_formal_realization309_after_audit230_20261008.py',R/'bind_projective_line_representative_failure229_20261008.py',R/'rebuild_projective_line308_after_representative_repair_20261008.py',R/'prepare_original_balanced_shared_face_research231_20261008.py',R/'launch_original_balanced_shared_face_research231_20261008.py',R/'extract_settled229230_exact_native_results_20261008.py',R/'record_verified234_20261008.py',G/'push-receipt-continuation234.json',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=32,historical_reviewed_scoped_papers=88,commit_message='Solve original P14.8 by arbitrary formal-data realization; preserve P1 repair and continue all-face research',scope='Original P14.8 arbitrary-formal-data alternative solved with BOTH qualifications;10solved32OPEN88papers. Retain failed P1 review and corrected revision; originalP05.1 research231 max2 campaigns. No force; exact remote verification; full third-party sources LOCALONLY.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=10,originals_open=32,accepted_papers=88),indent=2))
