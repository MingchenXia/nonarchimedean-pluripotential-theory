from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation200.json';F=G/'continuation200-publication-records';S=K/'small-batch189193-public-status-20261007-continuation200'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation199.json').read_text())
assert prior['commit_sha']=='bd39549051dd8f90a4d5889d7134ae0109345d57' and prior['files']==29 and not prior['force_update']
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
C=next((R/'campaigns/round-194').iterdir());assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
cf=json.loads((C/'freeze.json').read_text())
for n,k in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/n)==cf[k]
for e in json.loads((C/'private-primary-packet-bindings.json').read_text()):assert sha(e['path'])==e['sha256']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in (189,193):
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[i for i in items if i['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,prepared_next_round=194,prepared_next_round_launched=False,focus='Independent189 audits whole actual genus-zero equation. Original193 seeks the full unchanged arbitrary-field equation. Prepared194 seeks the remaining full original P05.2 classification after complete acceptedA224/B225/R230 and all clarifications; four read-only original-primary files. New unreviewed finite-orbit240, explicit Cartier/terminal241 and formal238 addendum were not hot-sent to active193.')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==75 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    previous=j['prepared_next_original_campaign'];assert previous['round']==193 and previous['launched'];j['P16_4_original_author193_launch']=previous
    j.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=200,status='prepared_for_authorized_push'),prepared_next_original_campaign=dict(round=194,atom='P05.2',directory=str(C),freeze=str(C/'freeze.json'),freeze_sha256=sha(C/'freeze.json'),input_sha256=cf['input_sha256'],prepared_only=True,launched=False,only_complete_grants=['A224','B225','R230'],unreviewed_data=[229],private_primary_files=4,full_primary_files_published=False,maximum_active_campaigns=2))
    j['P16_4_latest_unreviewed_actual_geometry_routes']=dict(formal_effectiveness=238,finite_actual_Galois_orbit=240,explicit_global_Cartier_and_terminal_points=241,new_accepted_paper=False,original_closed=False,sent_to_active193=False)
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/n,F/n)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=now,originals_solved=9,originals_open=33,cumulative_accepted_papers=75,new_original_closure=None,new_independent_verdict=None,active_batch=[i['round'] for i in active],prepared_only_round=194,prepared194_three_complete_accepted_grants=True,prepared194_private_primary_files=4,BBGS_original_publisher_pdf_pages=44,BBGS_visual_pages_read=[25,27],unreviewed_finite_orbit240=True,unreviewed_actual_Cartier_and_terminal241=True,BL_new_visual_page7=True,full_recursive_primary_dependency_check_claimed=False,full_third_party_sources_published=False,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[];seen=set()
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and 'frozen-primary-data-LOCALONLY' not in p.parts
    remote=remote or 'research-checkpoints/continuation200/'+str(p.relative_to(R));assert remote not in seen;seen.add(remote)
    files.append(dict(local=str(p),path=remote,bytes=p.stat().st_size,sha256=sha(p)))
for d in (F,S):
    for p in sorted(d.iterdir()):add(p)
for n in ('task.json','original-task.json','input.json','settings.json','freeze.json','mathematical-data-bindings.json','original-family-representation-binding.json','private-primary-packet-bindings.json'):add(C/n)
for n in ('P05.2-continuation239-publisher-primary-and-regular-subdivision-scope-20261007.json','P16.4-continuation240-pure-FS-finite-Galois-orbit-working-argument-20261007.json','P16.4-continuation238-cutoff-and-Proj-primary-reading-addendum-20261007.json','P16.4-continuation241-formal-Cartier-gluing-and-terminal-values-working-route-20261007.json'):add(K/n)
for n in ('retrieve_polyhedral_publisher239_primary_20261007.py','record_polyhedral239_and_finite_orbit240_working_reads_20261007.py','write_formal_Cartier241_and_terminal_point_working_route_20261007.py','prepare_original_polyhedral194_after_continuous_completion_20261007.py','launch_frozen_original_polyhedral194_20261007.py','record_verified199_20261007.py'):add(R/n)
add(G/'push-receipt-continuation199.json');add(Path(__file__))
for n in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/n,'manuscript/editorial/xean_research_20261003/'+n)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=75,commit_message='Develop actual Cartier and finite-orbit proofs and prepare contact classification',scope='Prepared ONLY native194 unchanged entireoriginalP05.2,165147-byte input with three complete independently acceptedA224/B225/R230 bodies and all clarifications, unreviewed failed product229 and four original frozen read-only BMPS/BBGS primary PDF/text files. Parent retrieved original BBGS publisher44-pagePDF696627bytes c2817a..., verified identity, read whole pertinent strictness/regular-subdivision/difference-of-concave units and visually checked only PDF25/27; full third-party bytes kept private. New unreviewed240 finite actual Galois orbit from invariant pure-FS genuine MA finite support, without semistable-cover descent. New unreviewed241 explicit global formal-Cartier equations c_v and c_v*x^k, unit transition ratios, actual component-degree/outgoing-slope calculation, strict positivity/polarized same-bundle effectiveness/FS application, terminal-disc value equality including poles and typeIII interior continuity; actual cofinal model/chart/completion/GAGA/kernel hypotheses remain to be proved. BL85 whole printed pertinent1.3/1.4/2.2/2.3/3.10 read, only new PDF7 visual;3.10 correctly identified as cover uniqueness, not algebraization. Add238 positive cutoff and complete Proj/free-locus/base-change primary units. All are working data, no original closure or new acceptance; not hot-sent to immutable active193. Public189/193 statuses only, two-campaign maximum, protected editor/auth/runtime preserved.9/42originals solved33open75accepted.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[i['round'] for i in active],prepared_only_round=194,accepted_papers=75),indent=2))
