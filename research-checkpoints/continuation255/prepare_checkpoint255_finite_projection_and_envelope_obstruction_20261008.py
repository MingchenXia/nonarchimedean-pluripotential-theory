from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint';C=next((R/'campaigns/round-253').iterdir())
M=G/'upload-manifest-continuation255.json';F=G/'continuation255-publication-records';S=K/'small-batch252-253-public-status-20261008-continuation255'
W=K/'P12.6-continuation348-finite-geometric-projection-and-conductor-envelope-obstruction-working-proof-20261008.md';B=K/'P12.6-continuation348-ROOT-whole-working-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not M.exists() and not F.exists() and not S.exists()
prior=json.loads((G/'push-receipt-continuation254.json').read_text());assert prior['commit_sha']=='6785490a7aec28d210d4a8c9f721f7fc379942db' and not prior['force_update'] and all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert sha(W)==json.loads(B.read_text())['proof']['sha256']
F.mkdir();S.mkdir();now=datetime.now(timezone.utc).isoformat();items=[]
for rnd in [252,253]:
    c=next((R/f'campaigns/round-{rnd}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed'];p=S/f'round{rnd}-public-native-status.json';write(p,st);items.append(dict(round=rnd,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt'],public_status=str(p)))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==14 and x['remaining_open_original_atoms']==28 and x['historical_reviewed_scoped_papers']==95 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=255,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='At most2native252wholeP12.5+346review and253wholeP12.6+348solve. New348 counterexample disproves unrestricted normalizationenvelopecommutation; completefibre-admissible identity andambientdegreefiniteproductprojection requireindependentreconstruction. Continue normal/flat one-slottrace projection andexactenvelope/tower/gauge consequences.14solved28OPEN95papers; protectedP16 OPENUNCHANGED; compile906 has no result.')
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint255: finite geometric projection and an envelope descent obstruction\n\n14/42originals solved,28OPEN,95acceptedpapers; no new original/paper acceptance. CompleteUNREVIEWED ROOT348 proves an explicit normalization-envelope obstruction on R=k[x,y,z]_(x,y,z)/(xy), conductor(x,y), two smoothnormalizationplanes. Continuous bounded f=-1-1/v(y) has unrestricted upstairsenvelope(-1,-2), actually a rawprimaryprofile/Cpotential. At the shared conductor-INFINITE boundarypoint the downstairsenvelope is exactly-2. Hence unrestrictedenvelopepullback equality fails byONE. Ordinaryregular-branchm-adicorder proves the entireenvelope bound, not numericalsamples, unknownenveloperegularity or a literalradialcriterion. Fibremaximum itself jumps alongmonomialvaluations andfailsC/D; verticalcomponents invalidate a naive universalGaloismaximum argument.\n\nCorrectpositive statements are actualCartier/curve-nef finitepullback; fibre-admissible C/D envelopebijection with positive-descent/existence equivalence; and ambientdegree mixedproductprojection for allpulled-back boundedinputs via topgenericdegreesdP andclosedresiduefq, finiteprimefiltration and genuinegeneraldegreecycleprojection. Exactscope excludes arbitraryupstairs nonlineartraceproducts or unrestrictedcontinuousdegreefunction. Counts do not change: originalscopejudge must distinguish a negativeanswer to an unconditionalstatement from incomplete qualifiedfunctoriality.\n\nNative253 Xean gpt-6.1-sol xhigh is frozenon ENTIRE originalP12.6/family, whole348 DATA, onlyfullqualifiedG331/G345. G345 includes complete accepted95paper, mandatory251source/scopeannotation, authorledger/scope/coverage/acceptance, independentwhole sourcequalification/decision andliteralfontrepairhistory. Native252 continues wholeP12.5+346review independently with unchangedinputs andonlyG331/B341; nohotfeedback orACTIVEprivatemath reading. Maximum2nativecampaigns. Allprivateprimary/contextbodies/pixels retainedLOCALONLY; their bindingmetadata public. Compiler906 remains unreturned, noPDFsuccess/error invented. ProtectedP16editor OPENUNCHANGED. Push uses authorizedsame repo/branch/nativeauth, exactblob/tree/ref verification andnonforceupdate.\n')
files=[];seen=set()
def add(p,target=None):
    p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png'];assert not any(x in rel.parts for x in ['source-pages','source-images','primary-data-LOCALONLY'])
    target=target or 'research-checkpoints/continuation255/'+str(rel);assert target not in seen;seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for p in [W,B,R/'prepare_original_finite_functoriality253_20261008.py',R/'launch_original_finite_functoriality253_20261008.py',R/'record_verified254_20261008.py',G/'push-receipt-continuation254.json',Path(__file__)]:add(p)
for name in ['task.json','original-task.json','input.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json','book-context-bindings.json']:add(C/name)
for e in json.loads((C/'mathematical-packet-bindings.json').read_text()):add(e['path'])
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
x=json.loads((R/'active-work.json').read_text());write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=28,historical_reviewed_scoped_papers=95,commit_message='Checkpoint finite geometric projection and continuous-obstacle conductor envelope obstruction',scope='14solved28OPEN95papers unchanged.Whole348unreviewedproof/counterexample and253fullfrozenoriginalsolve; active252unchanged/nohotfeedback/privateoutput; compile906unverified.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,ROOT348_bytes=W.stat().st_size,ROOT348_sha256=sha(W)),indent=2))
