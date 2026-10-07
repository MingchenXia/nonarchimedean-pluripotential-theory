from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation197.json';F=G/'continuation197-publication-records';S=K/'small-batch189191-public-status-20261007-continuation197'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation196.json').read_text())
assert prior['commit_sha']=='4092a26d39c5eb2a94b4894517b3d574cdaaf7cb' and prior['files']==45
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
C=next((R/'campaigns/round-192').iterdir());assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in (189,191):
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,prepared_next_round=192,prepared_next_round_launched=False,focus='Independent189 whole genus-zero review and full-original191 actual general-field equation author. New unreviewed232 primary scope diagnosis and233/234 actual generic-curve/Shilov estimate routes, exact energy polynomial and actual convex-series/FS-net recognition proof working supplement. No active input edited or hot feedback; prepared192 whole continuous-completion review waits for a slot.')
names=('P16.4-continuation232-Shilov-finite-inverse-primary-scope-reading-20261007.json','P16.4-continuation233-generic-curve-Shilov-estimate-working-observation-20261007.json','P16.4-continuation233-energy-polynomial-and-convex-series-working-addendum-20261007.json','P16.4-continuation234-generic-hyperplane-incidence-Shilov-working-observation-20261007.json')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==74 and j['remaining_open_original_atoms']==33
    j.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=197,status='prepared_for_authorized_push'))
    j['continuation232_234_unreviewed_generic_curve_route']=dict(records=[dict(path=str(K/n),sha256=sha(K/n)) for n in names],mathematical_grants=False,original_closed=False,active_native_inputs_modified=False,new_accepted_papers=0)
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=now,originals_solved=9,originals_open=33,cumulative_accepted_papers=74,new_original_closure=None,new_independent_verdict=None,active_batch=[x['round'] for x in active],prepared_only_next_round=192,unreviewed_working_routes=[233,234],new_primary_scope_diagnosis=232,full_new_primary_PDF_published=False,protected_editor_unchanged_open=True,all_actual_curve_incidence_model_and_scaling_premises_require_independent_review=True),indent=2)+'\n')
files=[];seen=set()
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.py')
    remote=remote or 'research-checkpoints/continuation197/'+str(p.relative_to(R));assert remote not in seen;seen.add(remote)
    files.append(dict(local=str(p),path=remote,bytes=p.stat().st_size,sha256=sha(p)))
for d in (F,S):
    for p in sorted(d.iterdir()):add(p)
for n in names:add(K/n)
for n in ('retrieve_shilov_finite_primary232_20261007.py','write_shilov_scope232_and_generic_curve_route233_20261007.py','write_generic_curve233_energy_addendum_20261007.py','write_generic_incidence_curve234_20261007.py','record_verified196_20261007.py'):add(R/n)
add(G/'push-receipt-continuation196.json');add(Path(__file__))
for n in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/n,'manuscript/editorial/xean_research_20261003/'+n)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=74,commit_message='Record actual generic-curve route and energy scaling proof work',scope='Quote-free232 literalFang2511.21835v1 scope audit: whole pertinent inverse/continuity/MA-comparison proof units and only originalPDF page17 visually checked; actual506999-byte primaryPDF retained PRIVATELY. Standing maximally-complete/full-value-group and continuous-metric MA comparison premises remain; zero-simplex-coordinate finite-log-matrix and displayed n^d error concerns are unresolved proof-audit questions, not a claimed counterexample. Unreviewed233 working route through a generic curve for every finite model-Shilov norming point, with actual model/semistable/slope/field-recognition premises explicitly open. Explicit energy boundB(tu)<=tA0+[n(n+1)/2]t^2B and conditional sublinear/coercivity constants reconstructed; actual convex-series/FS-majorant directed-net argument excludes uniform collapse by raw energy, without normalizedPSH compactness. Refined234 uses full generic hyperplane incidence, isometric Gauss fields and residual-parameter independence to seek actual typeII lifts and allpoint norm preservation; no existence/attainment/compactness or every-solution uniqueness theorem granted. New mathDATA only; active189/191 publicstatus only, immutable frozen inputs and no hot feedback. Prepared192 waits.9/42 originals solved,33 open,74 accepted. Protected editor/auth/runtime unchanged; no full third-party source uploaded.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],prepared_only_next_round=192,accepted_papers=74),indent=2))
