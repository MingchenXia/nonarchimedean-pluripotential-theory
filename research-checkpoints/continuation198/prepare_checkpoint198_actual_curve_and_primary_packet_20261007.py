from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation198.json';F=G/'continuation198-publication-records';S=K/'small-batch189192-public-status-20261007-continuation198'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation197.json').read_text())
assert prior['commit_sha']=='f3842d75e9846de2c0332daa35aa0ca14772d921' and prior['files']==21 and not prior['force_update']
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
C=next((R/'campaigns/round-193').iterdir());assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
C192=next((R/'campaigns/round-192').iterdir());assert (C192/'launch-record.json').exists() and (C192/'work.sqlite').exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in (189,191,192):
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n==192 else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
assert next(x for x in items if x['round']==191)['observed_status']=='completed'
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,prepared_next_round=193,prepared_next_round_launched=False,focus='Whole independent189 genus-zero review and192 continuous-completion/envelope review. Native191 settled candidatefalse; entire conditional235 paper read/reproduced but no independent verdict or unconditional curve claim. Frozen193 original author with six complete grants, unreviewed235/233/234/236/237 and sixteen read-only private primary files waits for one slot.')
b=K/'P16.4-round191-settled-partial-author-binding-20261007.json'
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==74 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=198,status='prepared_for_authorized_push'))
    j['P16_4_completed_partial_author191']=dict(candidate=False,original_closed=False,unconditional_all_genus_claim=False,source=str(K/'public-P16.4-continuation235-positive-graph-and-conditional-actual-curve/P16.4-paper.tex'),source_sha256='3e517c6b9ce68a29f11d5c35e2bc9f809de728812c7e5a73db1d34a7d0f1e110',whole_binding=str(b),whole_binding_sha256=sha(b),independent_verdict=None,new_accepted_paper=False,remaining_actual_geometry='R1-R5 model/skeleton/same-bundle realization/local frames/finite orbit; corrected FK88 bibliography and alternative non-Noetherian primary236 now supplied to future193')
    j['prepared_next_original_campaign']=dict(round=193,directory=str(C),freeze=str(C/'freeze.json'),freeze_sha256=sha(C/'freeze.json'),prepared_only=True,launched=False,only_complete_grants=['O217','D214','N220','T171','Q222','C218'],unreviewed_data=[233,234,235,236,237],private_primary_files=16,full_primary_files_published=False,maximum_active_campaigns=2)
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=now,originals_solved=9,originals_open=33,cumulative_accepted_papers=74,new_original_closure=None,new_independent_verdict=None,active_batch=[x['round'] for x in active],prepared_only_next_round=193,new_conditional_paper235=True,whole235_source884_and_argument330_lines_read=True,whole235_five_notes_bound_native=True,own_finite_interpolation140_raw_mass210_reproduced=True,built_in_native_and_public235_compilers_success=True,root_pdf235_pages_visually_read=[1,13],root_local235_minor_underfull_warning=True,actual_geometry_still_unverified=True,primary236_new_literal_Fujiwara_Kato2017v5=True,FK88_identity_correction='Freitag-Kiehl1988, notFujiwara-Kato',primary236_published_full_pdf=False,prepared193_private_primary_files=16,unreviewed_actual_generic_point_and_Radon_proof237=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[];seen=set()
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name
    assert 'frozen-primary-data-LOCALONLY' not in p.parts
    remote=remote or 'research-checkpoints/continuation198/'+str(p.relative_to(R));assert remote not in seen;seen.add(remote)
    files.append(dict(local=str(p),path=remote,bytes=p.stat().st_size,sha256=sha(p)))
for d in (F,S):
    for p in sorted(d.iterdir()):add(p)
D=K/'public-P16.4-continuation235-positive-graph-and-conditional-actual-curve'
for p in sorted(D.rglob('*')):
    if p.is_file() and p.suffix not in ('.aux','.log','.out') and '__pycache__' not in p.parts:add(p)
A=next((R/'campaigns/round-191').iterdir())/'artifacts/codex-Futrx3'
assert sha(A/'P16.4-paper.pdf')=='4a1cc32aca4fa9ef7228a841222c25e4de49d552089861643c6e0f7e446f74b1'
add(A/'P16.4-paper.pdf','research-checkpoints/continuation198/root-checks/public-P16.4-continuation235-positive-graph-and-conditional-actual-curve/evidence/unchanged-native-author.pdf')
for n in ('P16.4-round191-completed-actual-author-result-20261007.json','P16.4-round191-native-model-final-partial-author-20261007.json','P16.4-round191-settled-partial-author-binding-20261007.json','P16.4-continuation236-formal-algebraization-primary-reading-and-citation-correction-20261007.json','P16.4-continuation237-generic-incidence-point-and-Radon-dual-working-addendum-20261007.json'):add(K/n)
for n in ('task.json','original-task.json','input.json','settings.json','freeze.json','mathematical-data-bindings.json','private-primary-packet-bindings.json'):add(C/n)
add(C192/'launch-record.json')
for n in ('bind_and_reproduce_actual_curve_bridge235_20261007.py','record_curve235_and_formal236_reading_20261007.py','retrieve_formal_algebraization_primary236_20261007.py','write_generic_curve237_point_and_dual_addendum_20261007.py','prepare_original_field_equation193_with_actual_primary_packet_20261007.py','launch_frozen_original_field_equation193_20261007.py','record_verified197_20261007.py'):add(R/n)
add(G/'push-receipt-continuation197.json');add(Path(__file__))
for n in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/n,'manuscript/editorial/xean_research_20261003/'+n)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=74,commit_message='Preserve conditional curve proof and prepare actual primary-source repair',scope='Entire unchanged native191 conditional235 thirteen-page paper: all884 source/330 argument lines, five canonical notes and quote-free Markdown ledger read, exact native/request/canonical/frozen binding,59 artifact hashes and six grants checked. Own140 interpolation/210 raw-mass cases reproduced; two builds and native/public built-in compilers succeeded; only PDF1/13 visually read, one minor underfull diagnostic preserved. Candidatefalse with R1-R5 actual geometry and arbitrary-dimensional original open; no independent verdict/new acceptance. LiteralFujiwara-Kato1308.4734v5 original7385801-byte PDF retained privately; complete pertinent units read with omittedEGA-based algebraization proof explicitly open. CorrectGJKM FK88 toFreitag-Kiehl1988; new primary is an alternative, not same source. Unreviewed237 refined actual generic-incidence analytic-point/function-field/residual-dimension argument and Radon increasingCONT-net finite-dual implication. Freeze193 entireoriginal author with six complete grants and private sixteen-file read-only original-primary packet; full third-party source bytes omitted from Git. Launched192 only after191 settled; active189/192 public statuses only, no hotfeedback/private-active reads.9/42 originals solved,33 open,74 accepted. Protected editor/auth/runtime unchanged.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],prepared_only_next_round=193,accepted_papers=74),indent=2))
