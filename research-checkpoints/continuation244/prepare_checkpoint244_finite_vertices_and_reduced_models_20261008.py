from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation244.json';F=G/'continuation244-publication-records';S=K/'small-batch238-239-public-status-20261008-continuation244'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists()for p in(M,F,S))
prior=json.loads((G/'push-receipt-continuation243.json').read_text())
assert prior['commit_sha']=='fe311b244a6dd0a6fc16b669ec93048148acb6aa' and not prior['force_update'] and all(prior[k]for k in('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n,atom in((238,'P12.2'),(239,'P05.2')):
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom=atom,observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(c),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[238,239],maximum_concurrent_campaigns=2,accepted_paper_number=89)
b=R/'primary-data-LOCALONLY/P12.2-geometric-singular-cone-20261008';pdf=b/'BFJ-valuations-psh.pdf';txt=b/'BFJ-valuations-psh.txt'
assert sha(pdf)=='26d2d8dd2546efd55a148b4ff233892e88cfeab6c34de7fa613a7ad2e543d7f8' and sha(txt)=='9a72054bc227fca9231feb65ec631e6b4a91e68c10307d38fa5c23d5965de93f'
source_meta=K/'P12.2-additional-smooth-BFJ-definitions-and-approximation-ROOT-reading-20261008.json';assert not source_meta.exists()
write(source_meta,dict(recorded_utc=now,original_url='https://sebastien.boucksom.perso.math.cnrs.fr/publis/BFJ_psh.pdf',pdf_path=str(pdf),pdf_sha256=sha(pdf),text_path=str(txt),text_sha256=sha(txt),whole_immediate_units_ROOT_reread=[dict(LF_inclusive=[958,1025],units='Definition2.5, entire2.6 explanation, Proposition2.7 immediate argument and Definition2.8 canonical all-retraction extension'),dict(LF_inclusive=[1158,1237],units='Complete3.11 immediate proof,3.12,3.13 immediate proof and3.14 immediate proof, final476 continuation included')],application_qualifications=['BFJ smooth affine closed-point hypotheses: algebraically closed characteristiczero field; no singular/nonnormal/general-field/positive-characteristic SNC transfer.','Closed-simplex continuity in3.11 uses multiplier errors and bounded thinness; interior convexity alone is insufficient.','The zero function is retained separately: the printed3.13 proper-primary construction can produce a unit ideal at zero; a decreasing strictly negative proper-primary sequence cannot converge to zero. Late terms for a nonzero formal function are proper by3.14 and multiplier bounds.','The identically minus-infinity bottom is in the extended decreasing ideal cone but excluded from ordinary formal psh functions, which are real-valued on quasimonomials.','All-semivaluation recovery uses2.8 and commuting retraction/approximation infima. Source3.14 supplies quasimonomial finiteness for nonbottom decreasing limits.','Recursive Hironaka/Izumi/multiplier/subadditivity foundations and every46PDF page are not newly reconstructed or visually read.'],private_source_bodies_excluded_from_publication=True,new_mathematical_grant=False,new_accepted_paper=False,original_closed=False,private_active_output_read=False,hot_feedback_sent=False))
working=[next(K.glob('P05.2-continuation328-*.md')),next(K.glob('P12.2-continuation329-*.md'))]
for name in('active-work.json','checklist-current.json'):
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==11 and x['remaining_open_original_atoms']==31 and x['historical_reviewed_scoped_papers']==89 and x['github_pending_checkpoint']is None
    x.update(updated_utc=now,current_small_batch=batch,current_active_batch=[e['round']for e in active],github_pending_checkpoint=dict(continuation=244,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),ROOT328_329_independent_working_data=dict(paths=[str(p)for p in working],sha256=[sha(p)for p in working],new_mathematical_grants=False,new_accepted_papers=False,private_active_output_read=False,hot_feedback_sent=False))
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint244: finite vertex contact certificates and reduced primary models\n\n11/42originals solved;31OPEN;89accepted papers. NO new original/paper acceptance. Native238 and239 retain their original frozen inputs, nativegpt-6.1-sol xhigh and maximum two concurrent campaigns. Only public settled/running status snapshots are read; private ACTIVE output and hot feedback are excluded.\n\nNEW UNREVIEWEDROOT328 independently strengthens the contact-certificate proposal: positive-growth gamma makes every gamma-affine carrier cell pointed; exact common recession and convexity transfer vertex upper bounds to GLOBAL uniform bounds. Hence finitely many finite legal PCC trees, rather than an all-real-point tree quantifier, can certify near-maximality. Finite PC rows and saturated raw contact polynomials then propose a complete input-only infinite certificate, with genuine decreasing-domain construction before measure use and ALLC_b local-approximation/tightness passage. Meaningful original structural scope and mathematical/source correctness still require independent whole review. It was not supplied to ACTIVE239.\n\nNEW UNREVIEWEDROOT329 supplies a generic Rees-algebra proof of reduced primary blowup components and the global sections injection into Q(R), avoiding an unqualified assumption that an arbitrary primary generator is regular. ROOT326 historical bytes remain unchanged. It was not supplied to ACTIVE238.\n\nAdditional actual ROOT primary readings include complete Rees existence/residue and dimension-formula units with primary223/224PDF pixels, and complete smoothBFJ definitions/retraction/approximation/closed-simplex/Izumi immediate units. Only hashes/application/read metadata are public; full external source bodies and images remainLOCALONLY. No whole-source or recursive historical proof attestation, no automatic acceptance from reading/compilation/hashes. Source model/category/unit/bottom qualifications remain explicit. ProtectedP16.4 editor stays open unchanged; no auth/runtime change.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file()and 'LOCALONLY'not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation244/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in(F,S):
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for p in working+[source_meta,K/'P12.2-additional-Rees-residue-and-dimension-formula-ROOT-reading-20261008.json',G/'push-receipt-continuation243.json',R/'record_verified243_and_additional_source_reads_20261008.py',Path(__file__)]:add(p)
for name in('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path']for e in files})==len(files);x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=31,historical_reviewed_scoped_papers=89,commit_message='Develop finite vertex contact certificates and reduced Rees model sections',scope='11solved31OPEN89accepted; independent UNREVIEWEDROOT328329 and primary-read metadata; unchanged native238239 inputs,maximum2.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round']for e in active]),indent=2))
